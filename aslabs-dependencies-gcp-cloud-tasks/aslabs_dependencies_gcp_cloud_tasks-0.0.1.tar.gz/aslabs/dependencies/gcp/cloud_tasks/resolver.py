from __future__ import annotations
from typing import Optional, TypeVar, Type
from aslabs.dependencies import DependenciesABC, ResolverABC
from .cloud_tasks import CloudTaskConfig, cloud_task_client_factory, CloudTasks


T = TypeVar("T")


class CloudTasksResolver(ResolverABC):
    def __init__(self):
        self._client = None

    def __call__(self, deps: DependenciesABC) -> T:
        config = deps.get(CloudTaskConfig)
        if self._client is None:
            self._client = cloud_task_client_factory(config)
        return CloudTasks(config, self._client)

    @property
    def resolved_type(self) -> Type[T]:
        return CloudTasks
