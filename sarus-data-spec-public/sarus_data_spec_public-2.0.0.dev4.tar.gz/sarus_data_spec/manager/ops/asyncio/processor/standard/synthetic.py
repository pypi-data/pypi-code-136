import typing as t

import pyarrow as pa

import sarus_data_spec.typing as st

from .standard_op import StandardDatasetOp


class Synthetic(StandardDatasetOp):
    """Create a Synthetic op class for is_pep."""

    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        raise NotImplementedError("SyntheticOp to_arrow")

    async def schema(self) -> st.Schema:
        raise NotImplementedError("SyntheticOp schema")
