from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Optional, Protocol

from dependency_injector.containers import Container


class Block(Protocol):
    pass


class ResourceBlock(Block):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initialized: bool = False

    @property
    def initialized(self) -> bool:
        return self._initialized

    def sync_startup(self, application=None, service=None, module=None, *args, **kwargs):
        pass

    def sync_shutdown(self, application=None, service=None, module=None, *args, **kwargs):
        pass

    async def startup(self, application=None, service=None, module=None, *args, **kwargs):
        pass

    async def shutdown(self, application=None, service=None, module=None, *args, **kwargs):
        pass


class ContainerBlock(Block):
    def __init__(self, container: Container, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._container = container

    @property
    def container(self) -> Container:
        return self._container


class Module(ResourceBlock, ABC):
    name: str
    resources: List[ResourceBlock]

    @abstractmethod
    def get_resource(self, name) -> Optional[ResourceBlock]:
        ...


class Service(Module, ABC):
    modules: List[Module]

    @abstractmethod
    def get_module(self, name) -> Optional[Module]:
        ...


class Application(Service, ABC):
    services: List[Service]

    @abstractmethod
    def get_service(self, name) -> Optional[Service]:
        ...

    @property
    @abstractmethod
    def version(self) -> str:
        ...

    @property
    @abstractmethod
    def debug(self) -> bool:
        ...

    @abstractmethod
    def get_cwd(self) -> Path:
        ...

    @abstractmethod
    def sync_load_modules(self, *args, **kwargs):
        ...

    @abstractmethod
    async def load_modules(self, *args, **kwargs):
        ...
