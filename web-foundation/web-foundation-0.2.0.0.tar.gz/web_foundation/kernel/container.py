from __future__ import annotations

from typing import TypeVar

from pydantic import BaseSettings

from web_foundation.config import GenericConfig
from web_foundation.kernel.resource import Resource
from web_foundation.resources.files.interface import FilesResource
from web_foundation.kernel.dependency import Dependency
from web_foundation.resources.stores.interface import DataStore
from web_foundation.services.service import Service
from web_foundation.utils.helpers import in_obj_subclasses


class DependencyContainer:
    app_config: Dependency[GenericConfig] = Dependency(instance_of=BaseSettings)
    data_store: Dependency[DataStore] = Dependency(instance_of=DataStore)
    file_repository: Dependency[FilesResource] = Dependency(instance_of=FilesResource)

    async def init_resources(self):
        for resource, name in in_obj_subclasses(self, Resource):
            await resource.init(self.app_config())

    async def shutdown_resources(self):
        for resource, name in in_obj_subclasses(self, Resource):
            await getattr(self, name).shutdown()

    def services(self):
        return set(in_obj_subclasses(self, Service))


GenericDependencyContainer = TypeVar("GenericDependencyContainer", bound=DependencyContainer)
