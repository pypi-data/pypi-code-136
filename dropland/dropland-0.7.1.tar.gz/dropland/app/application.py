import contextlib
from pathlib import Path
from typing import Dict, List, Optional

from dependency_injector import providers
from dependency_injector.containers import Container
from dependency_injector.wiring import Provide, inject

from dropland.data.context import with_context
from dropland.log import logger
from dropland.util import import_path, invoke_async, invoke_sync
from . import base, service


class Application(base.Application, service.SessionService):
    def __init__(self, container: Container, name: str, debug: bool = False, version: str = ''):
        super().__init__(container, name)

        self._version = version
        self._debug = debug
        self._path = self._inspect_cwd()

        self._imported_modules = None
        self._service_containers: Dict[str, Container] = dict()
        self._services: Dict[str, service.Service] = dict()

        if hasattr(container, 'services'):
            for name, provider in container.services.providers.items():
                service_container = container.services(name)
                self._service_containers[name] = service_container
                self._services[name] = service_container.instance(service_container, name)

        container.instance = providers.Object(self)
        container.wire(modules=[__name__])

    @property
    def services(self) -> List[base.Service]:
        return list(self._services.values())

    def get_service(self, name) -> Optional[base.Service]:
        return self._services.get(name)

    @staticmethod
    def _inspect_cwd():
        import inspect
        return Path(inspect.stack()[3].filename).parent.absolute()

    @property
    def version(self) -> str:
        return self._version

    @property
    def debug(self) -> bool:
        return self._debug

    def get_cwd(self) -> Path:
        return self._path.absolute()

    def sync_startup(self, *args, **kwargs):
        super().sync_startup(application=self, *args, **kwargs)

        for s in self.services:
            s.sync_startup(application=self, *args, **kwargs)

    def sync_shutdown(self, *args, **kwargs):
        for s in self.services:
            s.sync_shutdown(application=self, *args, **kwargs)

        super().sync_shutdown(application=self, *args, **kwargs)

    async def startup(self, *args, **kwargs):
        await super().startup(application=self, *args, **kwargs)

        for s in self.services:
            await s.startup(application=self, *args, **kwargs)

    async def shutdown(self, *args, **kwargs):
        for s in self.services:
            await s.shutdown(application=self, *args, **kwargs)

        await super().shutdown(application=self, *args, **kwargs)

    def sync_session_begin(self, application=None, service=None, module=None, *args, **kwargs):
        super().sync_session_begin(application=self, *args, **kwargs)

        for s in self.services:
            if not isinstance(s, base.SessionResourceBlock):
                continue
            s.sync_session_begin(application=self, *args, **kwargs)

    def sync_session_finish(self, application=None, service=None, module=None, *args, **kwargs):
        for s in self.services:
            if not isinstance(s, base.SessionResourceBlock):
                continue
            s.sync_session_finish(application=self, *args, **kwargs)

        super().sync_session_finish(application=self, *args, **kwargs)

    async def session_begin(self, application=None, service=None, module=None, *args, **kwargs):
        await super().session_begin(application=self, *args, **kwargs)

        for s in self.services:
            if not isinstance(s, base.SessionResourceBlock):
                continue
            await s.session_begin(application=self, *args, **kwargs)

    async def session_finish(self, application=None, service=None, module=None, *args, **kwargs):
        for s in self.services:
            if not isinstance(s, base.SessionResourceBlock):
                continue
            await s.session_finish(application=self, *args, **kwargs)

        await super().session_finish(application=self, *args, **kwargs)

    def _import_modules(self, app_name: Optional[str] = None):
        from tomlkit import parse

        modules, result = dict(), dict()
        pyproject_toml_path = self.get_cwd() / 'pyproject.toml'

        if pyproject_toml_path.exists():
            with open(str(pyproject_toml_path)) as f:
                pyproject_toml = parse(string=f.read())

            if project := pyproject_toml.get('project'):
                if app_name:
                    if section := project.get(app_name):
                        modules = section.get('modules', dict())
                else:
                    modules = project.get('modules', dict())

        app_name = app_name or 'module'

        for name, dotted_path in modules.items():
            logger.info(f'Import module: {name}')
            dotted_path = dotted_path if ':' in dotted_path else f'{dotted_path}:{app_name}_init'

            if entrypoint := import_path(dotted_path):
                result[name] = entrypoint

        return result

    def sync_load_modules(self, *args, **kwargs):
        if not self._imported_modules:
            self._imported_modules = self._import_modules(self.name)

        with self.sync_with_app_sessions():
            for name, entrypoint in self._imported_modules.items():
                if name not in self._modules:
                    logger.warn(f'Application "{self.name}" does not contains module "{name}"')
                    continue

                logger.info(f'Application "{self.name}": load module "{name}"')

                module_args = (self, self._modules[name], *args)
                entrypoint(*module_args, **kwargs)

    async def load_modules(self, *args, **kwargs):
        if not self._imported_modules:
            self._imported_modules = self._import_modules(self.name)

        async with self.with_app_sessions():
            for name, entrypoint in self._imported_modules.items():
                if name not in self._modules:
                    logger.warn(f'Application "{self.name}" does not contains module "{name}"')
                    continue

                logger.info(f'Application "{self.name}": load module "{name}"')

                module_args = (self, self._modules[name], *args)
                await entrypoint(*module_args, **kwargs)

    @contextlib.contextmanager
    def sync_with_app_resources(self):
        with with_context(False):
            with contextlib.ExitStack() as stack:
                invoke_sync(self.startup)
                self.sync_startup()
                stack.callback(self.sync_shutdown)
                stack.callback(invoke_sync, self.shutdown)
                yield

    @contextlib.asynccontextmanager
    async def with_app_resources(self):
        with with_context(False):
            async with contextlib.AsyncExitStack() as stack:
                await self.startup()
                await invoke_async(self.sync_startup)
                stack.push_async_callback(invoke_async, self.sync_shutdown)
                stack.push_async_callback(self.shutdown)
                yield

    @contextlib.contextmanager
    def sync_with_app_sessions(self):
        with with_context(False):
            with contextlib.ExitStack() as stack:
                invoke_sync(self.session_begin)
                self.sync_session_begin()
                stack.callback(self.sync_session_finish)
                stack.callback(invoke_sync, self.session_finish)
                yield

    @contextlib.asynccontextmanager
    async def with_app_sessions(self):
        with with_context(False):
            async with contextlib.AsyncExitStack() as stack:
                await self.session_begin()
                await invoke_async(self.sync_session_begin)
                stack.push_async_callback(invoke_async, self.sync_session_finish)
                stack.push_async_callback(self.session_finish)
                yield


@inject
def current_application(_app: Application = Provide['instance']):
    return _app
