import asyncio
import contextlib
from dataclasses import dataclass
from datetime import timedelta
from typing import Dict, List, Mapping, Optional

from aioredis import ConnectionsPool, Redis, create_pool

from dropland.log import logger, tr
from ..base import StorageBackend, StorageEngine


@dataclass
class EngineConfig:
    url: str
    max_connections: int = 4
    pool_timeout_seconds: int = 5


class RedisStorageBackend(StorageBackend):
    def __init__(self):
        self._engines: Dict[str, 'RedisStorageEngine'] = dict()

    @property
    def name(self) -> str:
        return 'redis'

    def create_engine(self, name: str, config: EngineConfig,
                      default_ttl: timedelta = timedelta(seconds=60)) -> Optional['RedisStorageEngine']:
        if engine := self._engines.get(name):
            return engine

        engine = RedisStorageEngine(self, name, config, default_ttl)
        self._engines[name] = engine
        logger.info(tr('dropland.blocks.redis.engine.created').format(name=name))
        return engine

    def get_engine(self, name: str) -> Optional['RedisStorageEngine']:
        return self._engines.get(name)

    def get_engine_names(self) -> List[str]:
        return list(self._engines.keys())

    def get_engines(self, names: List[str]) -> Mapping[str, 'RedisStorageEngine']:
        engines = dict()

        if not names:
            names = self.get_engine_names()

        for name in names:
            if engine := self.get_engine(name):
                engines[name] = engine

        return engines


class RedisStorageEngine(StorageEngine):
    def __init__(self, backend: RedisStorageBackend, name: str, config: EngineConfig, default_ttl: timedelta):
        super().__init__(backend)
        self._name = name
        self._config = config
        self._default_ttl = default_ttl
        self._lock = asyncio.Lock()
        self._pool: Optional[ConnectionsPool] = None
        self._counter = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_async(self):
        return True

    @property
    def default_ttl(self) -> timedelta:
        return self._default_ttl

    def new_connection(self):
        @contextlib.asynccontextmanager
        async def inner(self):
            yield Redis(self._pool)
        return inner(self)

    def start(self):
        raise RuntimeError('Use async_start method')

    def stop(self):
        raise RuntimeError('Use async_stop method')

    async def async_start(self):
        async with self._lock:
            if 0 == self._counter:
                assert not self._pool
                self._pool = await create_pool(
                    self._config.url, create_connection_timeout=self._config.pool_timeout_seconds,
                    minsize=1, maxsize=self._config.max_connections
                )
                logger.info(tr('dropland.blocks.redis.engine.started'))
            self._counter += 1

    async def async_stop(self):
        async with self._lock:
            if 1 == self._counter:
                assert self._pool
                self._pool.close()
                await self._pool.wait_closed()
                self._pool = None
                logger.info(tr('dropland.blocks.redis.engine.stopped'))

            self._counter = max(self._counter - 1, 0)
