import asyncio
import logging
import typing as t

import pyarrow as pa

from sarus_data_spec.manager.asyncio.base import BaseComputation, T
from sarus_data_spec.manager.typing import DelegatedComputation, Manager
import sarus_data_spec.status as stt
import sarus_data_spec.typing as st

logger = logging.getLogger(__name__)


class TypedDelegatingManager(Manager, t.Protocol):
    async def async_to_arrow_op(
        self, dataset: st.Dataset, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        ...

    def delegate_manager_status(
        self, dataspec: st.DataSpec, task_name: str
    ) -> t.Optional[st.Status]:
        ...


class RemoteComputation(BaseComputation[T], DelegatedComputation):
    """For now, this is actually almost a copy/paste of the ApiCompuation.

    One difference is that the `delegate_manager_status` is a method of
    the manager. This makes sense since the way to communicate with the remote
    server is better centralized in the manager instead of being repeated in
    the Computations.

    Another difference is that we added a `fetch_result` method to potentially
    download the result from the remote worker before setting the local status.
    """

    def __init__(self, manager: TypedDelegatingManager):
        self._manager: TypedDelegatingManager = manager

    def manager(self) -> TypedDelegatingManager:
        return self._manager

    def launch_task(self, dataspec: st.DataSpec) -> None:
        raise NotImplementedError

    async def task_result(self, dataspec: st.DataSpec, **kwargs: t.Any) -> T:
        raise NotImplementedError

    def delegate_manager_status(
        self, dataspec: st.DataSpec
    ) -> t.Optional[st.Status]:
        return self.manager().delegate_manager_status(dataspec, self.task_name)

    async def fetch_result(self, dataspec: st.DataSpec) -> t.Dict[str, str]:
        """Optionally fetch the result from the remote worker before setting
        the ready status."""
        return dict()

    async def pending(self, dataspec: st.DataSpec) -> st.Status:
        """if the status of a task is pending, delegation has been
        already done, so the manager just waits for the task to
        be completed"""

        for i in range(100):
            logger.debug('POLLING ', self.task_name, dataspec.uuid())
            status = self.delegate_manager_status(dataspec=dataspec)
            if status is None:
                await asyncio.sleep(1)
            else:
                stage = status.task(self.task_name)
                assert stage
                if stage.ready():
                    properties = await self.fetch_result(dataspec)
                    stt.ready(
                        dataspec=dataspec,
                        manager=self.manager(),
                        task=self.task_name,
                        properties=properties,
                    )
                elif stage.processing():
                    stt.processing(
                        dataspec=dataspec,
                        manager=self.manager(),
                        task=self.task_name,
                    )
                elif stage.error():
                    stt.error(
                        dataspec=dataspec,
                        manager=self.manager(),
                        task=self.task_name,
                        properties=stage.properties(),
                    )
                else:
                    raise ValueError(f'stage {stage} not accepted')
                break

        status = stt.last_status(
            dataspec, task=self.task_name, manager=self.manager()
        )
        assert status
        stage = status.task(self.task_name)
        assert stage
        if stage.pending():
            stt.error(
                dataspec=dataspec,
                manager=dataspec.manager(),
                task=self.task_name,
                properties={
                    "message": f'Timeout exceeded in Pending task {self.task_name}'  # noqa: E501
                },
            )
        return await self.complete_task(dataspec)

    async def processing(self, dataspec: st.DataSpec) -> st.Status:
        """If processing, wait for the task to be ready.
        Such a case can happen if another manager has taken the computation
        of the task. After a given timeout, an error is raised.
        """

        for i in range(100):
            logger.debug('POLLING ', self.task_name, dataspec.uuid())
            status = self.delegate_manager_status(dataspec=dataspec)
            assert status
            stage = status.task(self.task_name)
            assert stage
            if stage.processing():
                await asyncio.sleep(1)
                continue
            else:
                break

        assert stage
        if stage.ready():
            properties = await self.fetch_result(dataspec)
            stt.ready(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
                properties=properties,
            )
        elif stage.error():
            stt.error(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
                properties=stage.properties(),
            )

        else:
            stt.error(
                dataspec=dataspec,
                manager=dataspec.manager(),
                task=self.task_name,
                properties={
                    "message": f'Timeout exceeded in Processing task {self.task_name}'  # noqa: E501
                },
            )
        return await self.complete_task(dataspec)

    def synchronize_status(
        self, dataspec: st.DataSpec, stage: st.Stage
    ) -> None:
        class StatusSynchronizer(st.StageVisitor):
            def __init__(
                self, task_name: str, manager: Manager, properties: t.Mapping
            ):
                self.task_name = task_name
                self.manager = manager
                self.properties = properties

            def ready(self) -> None:
                stt.ready(
                    dataspec=dataspec,
                    task=self.task_name,
                    manager=self.manager,
                    properties=self.properties,
                )

            def processing(self) -> None:
                stt.processing(
                    dataspec=dataspec,
                    task=self.task_name,
                    manager=self.manager,
                    properties=self.properties,
                )

            def pending(self) -> None:
                raise ValueError('Worker statuses must not be pending')

            def error(self) -> None:
                stt.error(
                    dataspec=dataspec,
                    task=self.task_name,
                    manager=self.manager,
                    properties=self.properties,
                )

        visitor = StatusSynchronizer(
            task_name=self.task_name,
            manager=self.manager(),
            properties=stage.properties(),
        )
        stage.accept(visitor)
        return
