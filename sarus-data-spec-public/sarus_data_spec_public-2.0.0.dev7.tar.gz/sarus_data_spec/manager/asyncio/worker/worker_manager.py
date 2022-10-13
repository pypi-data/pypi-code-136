import typing as t

import pyarrow as pa

from sarus_data_spec import typing as st
from sarus_data_spec.manager.asyncio.private_manager import PrivateManager
from sarus_data_spec.manager.asyncio.worker.arrow_computation import (
    ToArrowComputation,
)
from sarus_data_spec.manager.asyncio.worker.caching_computation import (
    ToParquetComputation,
)
from sarus_data_spec.manager.asyncio.worker.schema_computation import (
    SchemaComputation,
)
from sarus_data_spec.manager.asyncio.worker.value_computation import (
    ValueComputation,
)
from sarus_data_spec.manager.ops.asyncio.foreign_keys import fk_visitor
from sarus_data_spec.manager.ops.asyncio.primary_keys import pk_visitor
from sarus_data_spec.manager.ops.asyncio.processor.routing import (
    TransformedDataset,
    TransformedScalar,
)
from sarus_data_spec.manager.ops.asyncio.source.routing import (
    source_dataset_schema,
)
from sarus_data_spec.manager.ops.asyncio.source.sklearn import create_model
from sarus_data_spec.storage.typing import Storage
import sarus_data_spec.protobuf as sp
import sarus_data_spec.storage.typing as storage_typing


class WorkerManager(PrivateManager):
    """Manager that always executes computations
    in its process"""

    def __init__(
        self, storage: storage_typing.Storage, protobuf: sp.Manager
    ) -> None:
        super().__init__(storage, protobuf)
        self.schema_computation = SchemaComputation(self)
        self.to_arrow_computation = ToArrowComputation(self)
        self.to_parquet_computation = ToParquetComputation(
            self, ToArrowComputation(self)
        )
        self.value_computation = ValueComputation(self)

    async def async_to_arrow(
        self, dataset: st.Dataset, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        """Reads asynchronous iterator of datast batches"""
        if self.is_cached(dataset):
            return await self.to_parquet_computation.task_result(
                dataspec=dataset, batch_size=batch_size
            )
        return await self.to_arrow_computation.task_result(
            dataspec=dataset, batch_size=batch_size
        )

    async def async_schema(self, dataset: st.Dataset) -> st.Schema:
        """reads schema of a dataset asynchronously"""
        return await self.schema_computation.task_result(dataspec=dataset)

    async def async_value(self, scalar: st.Scalar) -> t.Any:
        """Reads asynchronously value of a scalar."""
        return await self.value_computation.task_result(dataspec=scalar)

    async def async_to_parquet(self, dataset: st.Dataset) -> None:
        await self.to_parquet_computation.complete_task(dataspec=dataset)

    async def async_schema_op(self, dataset: st.Dataset) -> st.Schema:
        if dataset.is_transformed():
            return await TransformedDataset(dataset).schema()
        return await source_dataset_schema(dataset=dataset)

    async def async_value_op(self, scalar: st.Scalar) -> t.Any:
        if scalar.is_model():
            return await create_model(scalar)
        elif scalar.is_transformed():
            return await TransformedScalar(scalar).value()
        else:
            raise ValueError('Scalar is either transformed or model')

    async def async_foreign_keys(
        self, dataset: st.Dataset
    ) -> t.Dict[st.Path, st.Path]:
        """Gets foreign keys from the schema"""
        schema = await self.async_schema(dataset)
        return fk_visitor(schema.type())

    async def async_primary_keys(self, dataset: st.Dataset) -> t.List[st.Path]:
        """Gets primary keys from the schema"""
        return pk_visitor((await self.async_schema(dataset)).type())


def manager(storage: Storage, **kwargs: str) -> WorkerManager:
    properties = {'type': 'worker_manager'}
    properties.update(kwargs)
    return WorkerManager(storage, sp.Manager(properties=properties))
