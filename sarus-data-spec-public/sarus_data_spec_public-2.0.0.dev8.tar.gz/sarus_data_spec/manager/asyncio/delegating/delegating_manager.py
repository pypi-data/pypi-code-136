import typing as t

import pyarrow as pa

from sarus_data_spec import typing as st
from sarus_data_spec.manager.asyncio.base import BaseAsyncManager
from sarus_data_spec.manager.asyncio.delegating.remote_computation import (
    RemoteComputation,
)
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
from sarus_data_spec.manager.ops.asyncio.processor.routing import (
    TransformedDataset,
    TransformedScalar,
)
from sarus_data_spec.manager.ops.asyncio.source.sklearn import create_model
import sarus_data_spec.manager.typing as smt
import sarus_data_spec.protobuf as sp
import sarus_data_spec.storage.typing as storage_typing


class DelegatingManager(BaseAsyncManager):
    """Manager that can compute a result locally or delegate a computation.

    This manager is initialized with a reference to the remote Manager so that
    we can register its statuses in the local storage.

    The local computations implementations are taken from the WorkerManager.

    Subclasses should implement the following three computations to compute
    values remotely:
        - self.remote_to_parquet_computation
        - self.remote_to_arrow_computation
        - self.remote_value_computation

    Subclasses also have to implement the `is_remotely_computed` method to
    decide if a computation should be performed locally or remotely.

    Finally, subclasses should implement the `delegate_manager_statuses` method
    to fetch statuses from the remote Manager.
    """

    def __init__(
        self,
        storage: storage_typing.Storage,
        protobuf: sp.Manager,
        remote_manager: smt.Manager,
    ) -> None:
        super().__init__(storage, protobuf)
        self.remote_manager = remote_manager
        self.local_schema_computation = SchemaComputation(self)
        self.local_to_arrow_computation = ToArrowComputation(self)
        self.local_value_computation = ValueComputation(self)
        self.local_to_parquet_computation = ToParquetComputation(
            self, ToArrowComputation(self)
        )

        # To define in subclasses
        self.remote_to_parquet_computation: RemoteComputation[
            t.AsyncIterator[pa.RecordBatch]
        ]
        self.remote_to_arrow_computation: RemoteComputation[
            t.AsyncIterator[pa.RecordBatch]
        ]
        self.remote_value_computation: RemoteComputation[t.Any]

    def delegate_manager_status(
        self, dataspec: st.DataSpec, task_name: str
    ) -> t.Optional[st.Status]:
        """Fetch the remote status a single Dataspec."""
        statuses = self.delegate_manager_statuses(
            [dataspec], task_name=task_name
        )
        (status,) = statuses
        return status

    def delegate_manager_statuses(
        self, dataspecs: t.List[st.DataSpec], task_name: str
    ) -> t.List[t.Optional[st.Status]]:
        """Fetch the remote statuses for a list of Dataspecs."""
        raise NotImplementedError

    def is_delegated(self, dataspec: st.DataSpec) -> bool:
        """Return True is the dataspec's computation is delegated."""
        raise NotImplementedError

    def is_cached(self, dataset: st.Dataset) -> bool:
        """Sets whether a dataset should be cached or not"""
        raise NotImplementedError

    async def async_to_arrow(
        self, dataset: st.Dataset, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        """Reads asynchronous iterator of dataset batches"""
        is_cached = self.is_cached(dataset)
        is_delegated = self.is_delegated(dataset)
        if is_cached:
            if is_delegated:
                return await self.remote_to_parquet_computation.task_result(
                    dataspec=dataset, batch_size=batch_size
                )
            else:
                return await self.local_to_parquet_computation.task_result(
                    dataspec=dataset, batch_size=batch_size
                )
        else:
            if is_delegated:
                return await self.remote_to_arrow_computation.task_result(
                    dataspec=dataset, batch_size=batch_size
                )
            else:
                return await self.local_to_arrow_computation.task_result(
                    dataspec=dataset, batch_size=batch_size
                )

    async def async_schema(self, dataset: st.Dataset) -> st.Schema:
        """Schema computation is done locally."""
        return await self.local_schema_computation.task_result(
            dataspec=dataset
        )

    async def async_value(self, scalar: st.Scalar) -> t.Any:
        """Reads asynchronously value of a scalar."""
        if self.is_delegated(scalar):
            return await self.remote_value_computation.task_result(
                dataspec=scalar
            )
        else:
            return await self.local_value_computation.task_result(
                dataspec=scalar
            )

    async def async_to_parquet(self, dataset: st.Dataset) -> None:
        await self.local_to_parquet_computation.complete_task(dataspec=dataset)

    async def async_to_arrow_op(
        self, dataset: st.Dataset, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        """Op that enables routing to compute the arrow iterator.
        This method is shared because when the data is not
        cached to parquet, even the Api manager should be
        able to stream its content.
        """
        if dataset.is_transformed():
            iterator = await TransformedDataset(dataset).to_arrow(
                batch_size=batch_size
            )
            return iterator

        else:
            raise ValueError('Dataset should be transformed.')

    async def async_value_op(self, scalar: st.Scalar) -> t.Any:
        if scalar.is_model():
            return await create_model(scalar)
        elif scalar.is_transformed():
            return await TransformedScalar(scalar).value()
        else:
            raise ValueError('Scalar is either transformed or model')

    async def async_schema_op(self, dataset: st.Dataset) -> st.Schema:
        if dataset.is_transformed():
            return await TransformedDataset(dataset).schema()
        else:
            raise ValueError('Dataset is should be transformed.')
