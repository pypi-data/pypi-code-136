import typing as t

import pyarrow as pa

from sarus_data_spec.manager.asyncio.utils import decoupled_async_iter
import sarus_data_spec.typing as st


class BaseDatasetOp:
    def __init__(self, dataset: st.Dataset):
        self.dataset = dataset

    async def schema(self) -> st.Schema:
        """Computes the schema of the dataspec"""
        raise NotImplementedError

    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        raise NotImplementedError

    def pep_token(
        self, public_context: t.List[str], epsilon: float
    ) -> t.Optional[str]:
        """Return a token if the output is PEP."""
        raise NotImplementedError

    @staticmethod
    async def decoupled_async_iter(
        source: t.AsyncIterator[pa.RecordBatch], buffer_size: int = 1
    ) -> t.AsyncIterator[pa.RecordBatch]:
        return decoupled_async_iter(source=source, buffer_size=buffer_size)


class BaseScalarOp:
    def __init__(self, scalar: st.Scalar):
        self.scalar = scalar

    async def value(self) -> t.Any:
        raise NotImplementedError

    @staticmethod
    async def decoupled_async_iter(
        source: t.AsyncIterator[pa.RecordBatch], buffer_size: int = 1
    ) -> t.AsyncIterator[pa.RecordBatch]:
        return decoupled_async_iter(source=source, buffer_size=buffer_size)
