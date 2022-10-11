import asyncio
import logging
import typing as t

import pyarrow as pa

from sarus_data_spec.manager.asyncio.base import (
    BaseComputation,
    DataSpecErrorStatus,
    T,
)
from sarus_data_spec.manager.typing import Manager
import sarus_data_spec.status as stt
import sarus_data_spec.typing as st

logger = logging.getLogger(__name__)

# This is done to avoid circular dependencies..


class TypedWorkerManager(Manager, t.Protocol):
    async def async_value_op(self, scalar: st.Scalar) -> st.DataSpecValue:
        ...

    async def async_schema_op(self, dataset: st.Dataset) -> st.Schema:
        ...

    async def async_to_arrow_op(
        self, dataset: st.Dataset, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        ...


class WorkerComputation(BaseComputation[T]):
    def __init__(self, manager: TypedWorkerManager):
        self._manager: TypedWorkerManager = manager

    def manager(self) -> TypedWorkerManager:
        return self._manager

    async def processing(self, dataspec: st.DataSpec) -> st.Status:
        """If processing, wait for the task to be ready.
        Such a case can happen if another manager has taken the computation
        of the task. After a given timeout, an error is raised.
        """

        for i in range(100):
            status = stt.last_status(
                dataspec=dataspec, task=self.task_name, manager=self.manager()
            )
            assert status
            logger.debug(f'POLLING {self.task_name} {dataspec.uuid()}')
            stage = status.task(self.task_name)
            assert stage
            if not stage.processing():
                break
            await asyncio.sleep(1)

        assert stage
        if stage.processing():
            # clear the status processing
            # and relaunch task
            status.clear_task(self.task_name)  # type: ignore
        return await self.complete_task(dataspec)

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
            task_name = self.task_name + dataspec.uuid()
            task = find_task(task_name)
            if task is not None:
                await task
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
                error_message = f"{self.task_name}: {error_message}"
                await self.error(dataspec)
                raise DataSpecErrorStatus(error_message)
            else:
                raise ValueError(f"Inconsistent status {manager_status}")

    def launch_task(self, dataspec: st.DataSpec) -> None:

        status = stt.last_status(
            dataspec=dataspec, manager=self.manager(), task=self.task_name
        )
        if status is None:
            stt.processing(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
            )
            asyncio.create_task(
                self.execute_computation(dataspec),
                name=self.task_name + dataspec.uuid(),
            )

    async def execute_computation(self, dataspec: st.DataSpec) -> None:
        """Actual method calling the ops to do the computation"""
        raise NotImplementedError


def find_task(task_name: str) -> t.Optional[asyncio.Task]:
    """Retrieves all asyncio tasks and among them,"""
    task: t.Optional[asyncio.Task] = None
    all_tasks = asyncio.Task.all_tasks()
    for available_task in all_tasks:
        if available_task.get_name() == task_name:
            task = available_task
            break
    return task
