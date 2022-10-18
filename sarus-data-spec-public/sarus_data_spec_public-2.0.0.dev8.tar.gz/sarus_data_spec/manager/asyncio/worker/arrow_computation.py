import logging
import traceback
import typing as t

import pyarrow as pa

from sarus_data_spec import typing as st
from sarus_data_spec.constants import ARROW_TASK
from sarus_data_spec.dataset import Dataset
from sarus_data_spec.manager.asyncio.worker.worker_computation import (
    WorkerComputation,
)
import sarus_data_spec.status as stt

BATCH_SIZE = 2000

logger = logging.getLogger(__name__)


class ToArrowComputation(WorkerComputation[t.AsyncIterator[pa.RecordBatch]]):

    task_name = ARROW_TASK

    async def execute_computation(self, dataspec: st.DataSpec) -> None:

        try:
            await self.manager().async_to_arrow_op(
                dataset=t.cast(Dataset, dataspec),
                batch_size=BATCH_SIZE,
            )

        except Exception:
            stt.error(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
                properties={"message": traceback.format_exc()},
            )
        else:
            logger.debug(f'FINISHED ARROW {dataspec.uuid()}')
            stt.ready(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
            )

    async def task_result(
        self, dataspec: st.DataSpec, **kwargs: t.Any
    ) -> t.AsyncIterator[pa.RecordBatch]:
        """Returns the iterator"""
        batch_size = kwargs['batch_size']
        status = await self.complete_task(dataspec=dataspec)
        stage = status.task(self.task_name)
        assert stage
        if stage.ready():
            return await self.manager().async_to_arrow_op(
                dataset=t.cast(Dataset, dataspec), batch_size=batch_size
            )

        raise ValueError('This should not be reached')
