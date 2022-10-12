from typing import Dict, List, Optional

from dependency_injector.containers import Container

from . import base


class Module(base.Module, base.ContainerBlock):
    def __init__(self, container: Container, name: str):
        super().__init__(container)

        self._name = name
        self._resource_containers: Dict[str, Container] = dict()
        self._resources: Dict[str, base.ResourceBlock] = dict()

        if hasattr(container, 'blocks'):
            for name, provider in container.blocks.providers.items():
                block_container = container.blocks(name)
                self._resource_containers[name] = block_container
                self._resources[name] = block_container.instance(block_container)

    @property
    def name(self) -> str:
        return self._name

    @property
    def resources(self) -> List[base.ResourceBlock]:
        return list(self._resources.values())

    def get_resource(self, name) -> Optional[base.ResourceBlock]:
        return self._resources.get(name)

    def sync_startup(self, application=None, service=None, *args, **kwargs):
        for r in self.resources:
            r.sync_startup(application=application, service=service, module=self, *args, **kwargs)

    def sync_shutdown(self, application=None, service=None, *args, **kwargs):
        for r in self.resources:
            r.sync_shutdown(application=application, service=service, module=self, *args, **kwargs)

    async def startup(self, application=None, service=None, *args, **kwargs):
        for r in self.resources:
            await r.startup(application=application, service=service, module=self, *args, **kwargs)

    async def shutdown(self, application=None, service=None, *args, **kwargs):
        for r in self.resources:
            await r.shutdown(application=application, service=service, module=self, *args, **kwargs)
