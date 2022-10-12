import asyncio
from dataclasses import dataclass
from typing import Dict, List, Mapping, Optional

import aio_pika
from aio_pika.pool import Pool

from dropland.log import logger, tr
from ..base import StorageBackend, StorageEngine


@dataclass
class EngineConfig:
    url: str
    virtualhost: str = '/'
    timeout_seconds: int = 5
    pool_max_connections: int = 4
    pool_max_channels_per_connection: int = 100


class RmqStorageBackend(StorageBackend):
    def __init__(self):
        self._engines: Dict[str, 'RmqStorageEngine'] = dict()

    @property
    def name(self) -> str:
        return 'rabbitmq'

    def create_engine(self, name: str, config: EngineConfig) -> Optional['RmqStorageEngine']:
        if engine := self._engines.get(name):
            return engine

        engine = RmqStorageEngine(self, name, config)
        self._engines[name] = engine
        logger.info(tr('dropland.blocks.rmq.engine.created').format(name=name))
        return engine

    def get_engine(self, name: str) -> Optional['RmqStorageEngine']:
        return self._engines.get(name)

    def get_engine_names(self) -> List[str]:
        return list(self._engines.keys())

    def get_engines(self, names: List[str]) -> Mapping[str, 'RmqStorageEngine']:
        engines = dict()

        if not names:
            names = self.get_engine_names()

        for name in names:
            if engine := self.get_engine(name):
                engines[name] = engine

        return engines


class RmqStorageEngine(StorageEngine):
    def __init__(self, backend: RmqStorageBackend, name: str, config: EngineConfig):
        super().__init__(backend)
        self._name = name
        self._config = config
        self._lock = asyncio.Lock()
        self._conn_pool: Optional[Pool] = None
        self._chan_pool: Optional[Pool] = None
        self._counter = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_async(self):
        return True

    def new_connection(self):
        return self._chan_pool.acquire()

    def start(self):
        raise RuntimeError('Use async_start method')

    def stop(self):
        raise RuntimeError('Use async_stop method')

    async def async_start(self):
        async with self._lock:
            if 0 == self._counter:
                assert not self._conn_pool
                assert not self._chan_pool

                loop = asyncio.get_event_loop()
                self._conn_pool = Pool(self._get_connection, max_size=self._config.pool_max_connections, loop=loop)
                self._chan_pool = Pool(self._get_channel, max_size=self._config.pool_max_channels_per_connection, loop=loop)
                logger.info(tr('dropland.blocks.rmq.engine.started'))

            self._counter += 1

    async def async_stop(self):
        async with self._lock:
            if 1 == self._counter:
                assert self._conn_pool
                assert self._chan_pool

                await self._chan_pool.close()
                await self._conn_pool.close()

                self._conn_pool = self._chan_pool = None
                logger.info(tr('dropland.blocks.rmq.engine.stopped'))

            self._counter = max(self._counter - 1, 0)

    async def _get_connection(self) -> aio_pika.abc.AbstractRobustConnection:
        return await aio_pika.connect_robust(
            self._config.url, virtualhost=self._config.virtualhost,
            timeout=self._config.timeout_seconds
        )

    async def _get_channel(self) -> aio_pika.Channel:
        async with self._conn_pool.acquire() as connection:
            return await connection.channel()
