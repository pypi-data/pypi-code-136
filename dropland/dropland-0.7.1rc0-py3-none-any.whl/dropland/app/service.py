from typing import Dict, List, Optional

from dependency_injector.containers import Container

from . import base, module


class Service(base.Service, module.Module):
    def __init__(self, container: Container, name: str):
        super().__init__(container, name)

        self._module_containers: Dict[str, Container] = dict()
        self._modules: Dict[str, module.Module] = dict()

        if hasattr(container, 'modules'):
            for name, provider in container.modules.providers.items():
                module_container = container.modules(name)
                self._module_containers[name] = module_container
                self._modules[name] = module_container.instance(module_container, name)

    @property
    def modules(self) -> List[base.Module]:
        return list(self._modules.values())

    def get_module(self, name) -> Optional[base.Module]:
        return self._modules.get(name)

    def sync_startup(self, application=None, *args, **kwargs):
        super().sync_startup(application=application, service=self, *args, **kwargs)

        for m in self._modules.values():
            m.sync_startup(application=application, service=self, *args, **kwargs)

    def sync_shutdown(self, application=None, *args, **kwargs):
        for m in self._modules.values():
            m.sync_shutdown(application=application, service=self, *args, **kwargs)

        super().sync_shutdown(application=application, service=self, *args, **kwargs)

    async def startup(self, application=None, *args, **kwargs):
        await super().startup(application=application, service=self, *args, **kwargs)

        for m in self._modules.values():
            await m.startup(application=application, service=self, *args, **kwargs)

    async def shutdown(self, application=None, *args, **kwargs):
        for m in self._modules.values():
            await m.shutdown(application=application, service=self, *args, **kwargs)

        await super().shutdown(application=application, service=self, *args, **kwargs)
