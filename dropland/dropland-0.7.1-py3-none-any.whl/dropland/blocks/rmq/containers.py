import contextlib

from dependency_injector import containers, providers

from dropland.app.base import ContainerBlock, SessionResourceBlock
from dropland.data.context import get_context
from dropland.util import default_value
from .engine import EngineConfig, RmqStorageBackend
from .session import SessionManager


class RmqBlock(ContainerBlock, SessionResourceBlock):
    async def startup(self, *args, **kwargs):
        if self.initialized:
            return
        await self.container.init_resources()
        self._initialized = True

    async def shutdown(self, *args, **kwargs):
        if not self.initialized:
            return
        await self.container.shutdown_resources()
        self._initialized = False

    async def session_begin(self, *args, **kwargs):
        ctx = get_context()
        if not self.initialized or '_rmq_block' in ctx:
            return

        ctx._rmq_block = await contextlib.AsyncExitStack().__aenter__()
        for engine_name in self.container.engine_factory().get_engine_names():
            await ctx._rmq_block.enter_async_context(
                self.container.manager().session_context(engine_name)
            )

    async def session_finish(self, *args, **kwargs):
        ctx = get_context()
        if not self.initialized or '_rmq_block' not in ctx:
            return

        await ctx._rmq_block.__aexit__(None, None, None)
        del ctx._rmq_block

    def get_engine(self, *args, **kwargs):
        if isinstance(self.container, SingleRmqStorage) or 'SingleRmqStorage' == self.container.parent_name:
            return self.container.create_engine()
        return self.container.create_engine(*args, **kwargs)

    def get_session(self, *args, **kwargs):
        if isinstance(self.container, SingleRmqStorage) or 'SingleRmqStorage' == self.container.parent_name:
            return self.container.get_session()
        return self.container.get_session(*args, **kwargs)


class RmqStorage(containers.DeclarativeContainer):
    __self__ = providers.Self()
    engine_factory = providers.Singleton(RmqStorageBackend)
    manager = providers.Singleton(SessionManager, engine_factory)

    def _create_engine(self, *args, **kwargs):
        return self.engine_factory().create_engine(*args, **kwargs)

    async def _init_session(self):
        async with self.manager().init_engines():
            yield self.manager()

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(_init_session, __self__)
    get_session = providers.Factory(manager.provided.get_session.call())
    block = providers.Singleton(RmqBlock, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=[__name__]
    )


class SingleRmqStorage(RmqStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self):
        if isinstance(self.config.engine_config(), EngineConfig):
            engine_config = self.config.engine_config()
        else:
            engine_config = EngineConfig(
                url=self.config.engine_config.url(),
                virtualhost=self.config.engine_config.virtualhost(),
                timeout_seconds=self.config.engine_config.
                    timeout_seconds.as_(default_value(int))(default=5),
                pool_max_connections=self.config.engine_config.
                    pool_max_connections.as_(default_value(int))(default=4),
                pool_max_channels_per_connection=self.config.engine_config.
                    pool_max_channels_per_connection.as_(default_value(int))(default=100)
            )
        return RmqStorage._create_engine(self, self.config.name(), engine_config)

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(RmqStorage._init_session, __self__)
    get_session = providers.Factory(RmqStorage.get_session, config.name)
    block = providers.Singleton(RmqBlock, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=[__name__]
    )


class MultipleRmqStorage(RmqStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self, name: str):
        if conf := self.config.get(name):
            if isinstance(conf['engine_config'], EngineConfig):
                engine_config = conf['engine_config']
            else:
                engine_config = EngineConfig(
                    url=conf['engine_config']['url'],
                    virtualhost=conf['engine_config']['virtualhost'],
                    timeout_seconds=int(conf['engine_config'].get('timeout_seconds', 5)),
                    pool_max_connections=int(conf['engine_config'].get('pool_max_connections', 4)),
                    pool_max_channels_per_connection=int(conf['engine_config'].get(
                        'pool_max_channels_per_connection', 100))
                )
            return RmqStorage._create_engine(self, name, engine_config)
        return None

    def _get_session(self, name: str):
        return self.manager().get_session(name)

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(RmqStorage._init_session, __self__)
    get_session = providers.Factory(_get_session, __self__)
    block = providers.Singleton(RmqBlock, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=[__name__]
    )
