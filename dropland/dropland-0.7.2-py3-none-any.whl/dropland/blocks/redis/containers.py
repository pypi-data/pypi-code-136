import contextlib
from datetime import timedelta

from dependency_injector import containers, providers
from pytimeparse.timeparse import timeparse

from dropland.app.base import ContainerBlock, SessionResourceBlock
from dropland.data.context import get_context
from dropland.util import default_value
from .engine import EngineConfig, RedisStorageBackend
from .session import SessionManager


class RedisBlock(ContainerBlock, SessionResourceBlock):
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
        if not self.initialized or '_redis_block' in ctx:
            return

        ctx._redis_block = await contextlib.AsyncExitStack().__aenter__()
        for engine_name in self.container.engine_factory().get_engine_names():
            await ctx._redis_block.enter_async_context(
                self.container.manager().session_context(engine_name)
            )

    async def session_finish(self, *args, **kwargs):
        ctx = get_context()
        if not self.initialized or '_redis_block' not in ctx:
            return

        await ctx._redis_block.__aexit__(None, None, None)
        del ctx._redis_block

    def get_engine(self, *args, **kwargs):
        if isinstance(self.container, SingleRedisStorage) or 'SingleRedisStorage' == self.container.parent_name:
            return self.container.create_engine()
        return self.container.create_engine(*args, **kwargs)

    def get_session(self, *args, **kwargs):
        if isinstance(self.container, SingleRedisStorage) or 'SingleRedisStorage' == self.container.parent_name:
            return self.container.get_session()
        return self.container.get_session(*args, **kwargs)


class RedisStorage(containers.DeclarativeContainer):
    __self__ = providers.Self()
    engine_factory = providers.Singleton(RedisStorageBackend)
    manager = providers.Singleton(SessionManager, engine_factory)
    default_ttl = providers.Object(timedelta(seconds=timeparse('1 min')))

    def _create_engine(self, *args, **kwargs):
        return self.engine_factory().create_engine(*args, **kwargs)

    async def _init_session(self):
        async with self.manager().init_engines():
            yield self.manager()

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(_init_session, __self__)
    get_session = providers.Factory(manager.provided.get_session.call())
    block = providers.Singleton(RedisBlock, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=['.model']
    )


class SingleRedisStorage(RedisStorage):
    __self__ = providers.Self()
    config = providers.Configuration()
    # noinspection PyArgumentList
    default_ttl = providers.Object(timedelta(
        seconds=timeparse(config.get('default_cache_ttl', required=False) or '1 min')))

    def _create_engine(self):
        if isinstance(self.config.engine_config(), EngineConfig):
            engine_config = self.config.engine_config()
        else:
            engine_config = EngineConfig(
                url=self.config.engine_config.url(),
                max_connections=self.config.engine_config.
                    max_connections.as_(default_value(int))(default=4),
                pool_timeout_seconds=self.config.engine_config.
                    pool_timeout_seconds.as_(default_value(int))(default=5)
            )
        return RedisStorage._create_engine(self, self.config.name(), engine_config, self.default_ttl())

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(RedisStorage._init_session, __self__)
    get_session = providers.Factory(RedisStorage.get_session, config.name)
    block = providers.Singleton(RedisBlock, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=['.model']
    )


class MultipleRedisStorage(RedisStorage):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self, name: str):
        if conf := self.config.get(name):
            if isinstance(conf['engine_config'], EngineConfig):
                engine_config = conf['engine_config']
            else:
                engine_config = EngineConfig(
                    url=conf['engine_config']['url'],
                    max_connections=int(conf['engine_config'].get('max_connections', 4)),
                    pool_timeout_seconds=int(conf['engine_config'].get('pool_timeout_seconds', 5))
                )
            return RedisStorage._create_engine(
                self, name, engine_config,
                timedelta(seconds=timeparse(conf.get('default_cache_ttl', '1 min'))))
        return None

    def _get_session(self, name: str):
        return self.manager().get_session(name)

    create_engine = providers.Factory(_create_engine, __self__)
    session_context = providers.Resource(RedisStorage._init_session, __self__)
    get_session = providers.Factory(_get_session, __self__)
    block = providers.Singleton(RedisBlock, __self__)

    wiring_config = containers.WiringConfiguration(
        modules=['.model']
    )
