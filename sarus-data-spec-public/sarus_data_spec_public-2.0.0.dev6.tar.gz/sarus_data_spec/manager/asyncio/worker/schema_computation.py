import logging
import traceback
import typing as t

from sarus_data_spec import typing as st
from sarus_data_spec.constants import SCHEMA_TASK
from sarus_data_spec.dataset import Dataset
from sarus_data_spec.manager.asyncio.worker.worker_computation import (
    WorkerComputation,
)
from sarus_data_spec.schema import Schema
from sarus_data_spec.status import error, ready

logger = logging.getLogger(__name__)


class SchemaComputation(WorkerComputation[st.Schema]):
    """Class responsible to compute schemas"""

    task_name = SCHEMA_TASK

    async def execute_computation(self, dataspec: st.DataSpec) -> None:

        try:
            logger.debug(f'STARTED SCHEMA {dataspec.uuid()}')
            schema = await self.manager().async_schema_op(
                dataset=t.cast(Dataset, dataspec)
            )

        except Exception:
            error(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
                properties={"message": traceback.format_exc()},
            )
        else:
            print(f'FINISHED SCHEMA {dataspec.uuid()}')
            ready(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
                properties={'uuid': schema.uuid()},
            )

    async def task_result(
        self, dataspec: st.DataSpec, **kwargs: t.Any
    ) -> st.Schema:
        status = await self.complete_task(dataspec)
        return t.cast(
            Schema,
            dataspec.storage().referrable(
                status.task(self.task_name)['uuid']  # type:ignore
            ),
        )
