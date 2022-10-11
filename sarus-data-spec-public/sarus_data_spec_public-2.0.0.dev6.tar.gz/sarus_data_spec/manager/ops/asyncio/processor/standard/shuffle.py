import random
import typing as t

import pyarrow as pa

from sarus_data_spec.constants import DATASET_SLUGNAME
from sarus_data_spec.manager.asyncio.utils import async_iter
from sarus_data_spec.manager.ops.asyncio.processor.standard.standard_op import (  # noqa: E501
    StandardDatasetOp,
)
from sarus_data_spec.schema import schema
import sarus_data_spec.typing as st


class Shuffle(StandardDatasetOp):
    """Computes schema and arrow
    batches for a dataspec transformed by
    a user_settings transform
    """

    async def schema(self) -> st.Schema:
        parent_schema = await self.parent_schema()
        return schema(
            self.dataset,
            schema_type=parent_schema.type(),
            protected_paths=parent_schema.protobuf().protected,
            properties=parent_schema.properties(),
            name=self.dataset.properties().get(DATASET_SLUGNAME, None),
        )

    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:

        arrow_batches = [
            batch async for batch in await self.parent_to_arrow(batch_size=1)
        ]
        random.shuffle(arrow_batches)
        return async_iter(
            pa.Table.from_batches(arrow_batches).to_batches(
                max_chunksize=batch_size
            )
        )
