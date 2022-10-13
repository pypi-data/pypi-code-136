from __future__ import annotations

import logging
import os
import typing as t

import pandas as pd
import pyarrow as pa

from sarus_data_spec.arrow.array import convert_record_batch
from sarus_data_spec.manager.asyncio.utils import sync, sync_iterator
from sarus_data_spec.manager.base import Base
from sarus_data_spec.manager.typing import Computation, Manager
from sarus_data_spec.schema import Schema
import sarus_data_spec.status as stt
import sarus_data_spec.typing as st

try:
    import tensorflow as tf

    from sarus_data_spec.manager.ops.asyncio.tensorflow.features import (
        deserialize,
        flatten,
        nest,
        serialize,
        to_internal_signature,
    )
    from sarus_data_spec.manager.ops.asyncio.tensorflow.tensorflow_visitor import (  # noqa: E501
        convert_tensorflow,
    )
except ModuleNotFoundError:
    pass  # error message printed from typing.py


logger = logging.getLogger(__name__)

BATCH_SIZE = 10000


class BaseAsyncManager(Base):
    """Asynchronous Manager Base implementation
    Make synchronous methods rely on asynchronous ones for consistency.
    """

    def value(self, scalar: st.Scalar) -> st.DataSpecValue:
        return sync(self.async_value(scalar=scalar))

    def to_arrow(
        self, dataset: st.Dataset, batch_size: int
    ) -> st.ContextManagerIterator[pa.RecordBatch]:
        return sync_iterator(
            self.async_to_arrow(dataset=dataset, batch_size=batch_size)
        )

    async def async_to_pandas(self, dataset: st.Dataset) -> pd.DataFrame:
        batches_async_it = await self.async_to_arrow(
            dataset=dataset, batch_size=BATCH_SIZE
        )
        arrow_batches = [batch async for batch in batches_async_it]
        return pa.Table.from_batches(arrow_batches).to_pandas()

    def to_pandas(self, dataset: st.Dataset) -> pd.DataFrame:
        return sync(self.async_to_pandas(dataset=dataset))

    def to_tensorflow(self, dataset: st.Dataset) -> tf.data.Dataset:
        return sync(self.async_to_tensorflow(dataset=dataset))

    def schema(self, dataset: st.Dataset) -> Schema:
        return t.cast(Schema, sync(self.async_schema(dataset=dataset)))

    def to_parquet(self, dataset: st.Dataset) -> None:
        sync(self.async_to_parquet(dataset=dataset))

    async def async_to_tensorflow(
        self, dataset: st.Dataset
    ) -> tf.data.Dataset:

        root_dir = os.path.join(
            self.parquet_dir(), "tfrecords", dataset.uuid()
        )
        schema_type = dataset.schema().type()
        signature = to_internal_signature(schema_type)

        if not os.path.exists(root_dir):
            # the dataset is cached first
            os.makedirs(root_dir)

            flattener = flatten(signature)
            serializer = serialize(signature)
            i = 0
            batches_async_it = await self.async_to_arrow(
                dataset=dataset, batch_size=BATCH_SIZE
            )
            async for batch in batches_async_it:
                filename = os.path.join(root_dir, f"batch_{i}.tfrecord")
                i += 1
                await write_tf_batch(
                    filename, batch, schema_type, flattener, serializer
                )

        # reading from cache
        glob = os.path.join(root_dir, "*.tfrecord")
        filenames = tf.data.Dataset.list_files(glob, shuffle=False)
        deserializer = deserialize(signature)
        nester = nest(signature)
        return tf.data.TFRecordDataset(filenames).map(deserializer).map(nester)


async def write_tf_batch(
    filename: str,
    batch: pa.RecordBatch,
    schema_type: st.Type,
    flattener: t.Callable,
    serializer: t.Callable,
) -> None:
    with tf.io.TFRecordWriter(filename) as writer:
        batch = convert_tensorflow(
            convert_record_batch(record_batch=batch, _type=schema_type),
            schema_type,
        )
        batch = tf.data.Dataset.from_tensor_slices(batch).map(flattener)
        for row in batch:
            as_bytes = serializer(row)
            writer.write(as_bytes)


T = t.TypeVar("T")


class BaseComputation(Computation[T]):
    """General class that implements some
    methods of the protocol shared by all task
    computations"""

    task_name = ''

    def __init__(self, manager: Manager):
        self._manager = manager

    def manager(self) -> Manager:
        return self._manager

    def launch_task(self, dataspec: st.DataSpec) -> None:
        raise NotImplementedError

    def delegate_manager_status(
        self, dataspec: st.DataSpec
    ) -> t.Optional[st.Status]:
        raise NotImplementedError

    async def task_result(self, dataspec: st.DataSpec, **kwargs: t.Any) -> T:
        raise NotImplementedError

    async def complete_task(self, dataspec: st.DataSpec) -> st.Status:
        """Poll the last status for the given task and if no status
        is available either performs the computation or delegates it
        to another manager. Then keeps polling until either the task
        is completed or an error occurs."""

        manager_status = stt.last_status(
            dataspec=dataspec, manager=self.manager(), task=self.task_name
        )

        if manager_status is None:
            self.launch_task(dataspec=dataspec)
            return await self.complete_task(dataspec)

        else:
            last_task = t.cast(st.Stage, manager_status.task(self.task_name))
            if last_task.ready():
                return manager_status
            elif last_task.pending():
                return await self.pending(dataspec)
            elif last_task.processing():
                return await self.processing(dataspec)
            elif last_task.error():
                error_message = last_task.properties()['message']
                await self.error(dataspec)
                raise DataSpecErrorStatus(error_message)
            else:
                raise ValueError(f"Inconsistent status {manager_status}")

    async def pending(self, dataspec: st.DataSpec) -> st.Status:
        """The behaviour depends on the manager"""
        raise NotImplementedError

    async def processing(self, dataspec: st.DataSpec) -> st.Status:
        """The behaviour depends on the manager"""

    async def error(
        self,
        dataspec: st.DataSpec,
    ) -> None:
        """The DataSpec already has an Error status.
        In this case, we clear the statuses so that the
        task can be relaunched in the future.
        """
        stt.clear_task(dataspec=dataspec, task=self.task_name)


class DataSpecErrorStatus(Exception):
    ...
