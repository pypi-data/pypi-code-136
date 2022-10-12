import asyncio
import contextlib
import sys
import threading
from collections import defaultdict
from dataclasses import dataclass, replace
from datetime import timedelta
from typing import Dict, List, Mapping, Optional, Set

import ujson
from sqlalchemy import create_engine as create_sync_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.schema import MetaData

from dropland.blocks.sql.base import SqlStorageType
from dropland.log import logger, tr
from .base import NAMING_CONVENTION
from ..base import StorageBackend, StorageEngine


@dataclass
class EngineConfig:
    url: str
    echo: bool = False
    pool_min_size: int = 1
    pool_max_size: int = 8
    pool_expire_seconds: int = 60
    pool_timeout_seconds: int = 15


@dataclass
class EngineKey:
    db_type: SqlStorageType
    is_async: bool

    def __eq__(self, other: 'EngineKey'):
        return (self.db_type, self.is_async) == (other.db_type, other.is_async)

    def __hash__(self):
        return hash((self.db_type, self.is_async))


@dataclass
class EngineWithDbType:
    db_type: SqlStorageType
    engine: 'SqlStorageEngine'


class SqlStorageBackend(StorageBackend):
    def __init__(self):
        self._engines: Dict[str, 'SqlStorageEngine'] = dict()
        self._engines_by_key: Dict[EngineKey, Set[str]] = defaultdict(set)
        self._engines_by_type: Dict[SqlStorageType, Set[str]] = defaultdict(set)

    @property
    def name(self) -> str:
        return 'sqla'

    def create_engine(self, name: str, config: EngineConfig, db_type: SqlStorageType, use_async: bool) \
            -> Optional['SqlStorageEngine']:
        if engine := self._engines.get(name):
            return engine

        uri = config.url

        if use_async:
            if db_type == SqlStorageType.SQLITE:
                uri = uri.replace('sqlite', 'sqlite+aiosqlite', 1)
            elif db_type == SqlStorageType.POSTGRES:
                uri = uri.replace('postgresql', 'postgresql+asyncpg', 1)
            elif db_type == SqlStorageType.MYSQL:
                uri = uri.replace('mysql', 'mysql+aiomysql', 1)
        else:
            if db_type == SqlStorageType.MYSQL:
                uri = uri.replace('mysql', 'mysql+pymysql', 1)

        config = replace(config, url=uri)

        params = dict(
            echo=config.echo,
            pool_recycle=config.pool_expire_seconds,
            json_serializer=ujson.dumps,
            json_deserializer=ujson.loads,
        )

        if db_type in (SqlStorageType.POSTGRES, SqlStorageType.MYSQL):
            params.update(dict(
                pool_size=config.pool_min_size,
                max_overflow=config.pool_max_size - config.pool_min_size,
                pool_timeout=config.pool_timeout_seconds
            ))

        if use_async:
            engine = create_async_engine(config.url, **params)
            session_class = sessionmaker(engine, autoflush=False, expire_on_commit=False, class_=AsyncSession)
        else:
            engine = create_sync_engine(config.url, **params)
            session_class = sessionmaker(engine, autoflush=False)

        logger.info(tr('dropland.blocks.sql.engine.created').format(db_type=db_type, async_=f'async={use_async}'))
        metadata = MetaData(bind=engine, naming_convention=NAMING_CONVENTION)
        engine_class = SqlAlchemyAsyncEngine if use_async else SqlAlchemySyncEngine
        engine = engine_class(self, name, engine, metadata, db_type, session_class,
                              timedelta(seconds=config.pool_timeout_seconds))

        self._engines[name] = engine
        self._engines_by_key[EngineKey(db_type=db_type, is_async=use_async)].add(name)
        self._engines_by_type[db_type].add(name)
        return engine

    def get_engine(self, name: str) -> Optional['SqlStorageEngine']:
        return self._engines.get(name)

    def get_engine_names(self) -> List[str]:
        return list(self._engines.keys())

    def get_engines_for_type(self, db_type: SqlStorageType, is_async: bool) -> List['SqlStorageEngine']:
        engine_names = self._engines_by_key[EngineKey(db_type=db_type, is_async=is_async)]
        return [self.get_engine(name) for name in engine_names]

    def get_engines(self, names: List[str]) -> Mapping[str, 'SqlStorageEngine']:
        engines = dict()

        if not names:
            names = self.get_engine_names()

        for name in names:
            if engine := self.get_engine(name):
                engines[name] = engine

        return engines


class SqlStorageEngine(StorageEngine):
    def __init__(self, backend: SqlStorageBackend, name: str, raw_engine, metadata,
                 db_type: SqlStorageType, timeout: timedelta):
        super().__init__(backend)
        self._name = name
        self._engine = raw_engine
        self._db_type = db_type
        self._timeout = timeout
        self._metadata = metadata

    @property
    def name(self) -> str:
        return self._name

    @property
    def raw_engine(self):
        return self._engine

    @property
    def db_type(self):
        return self._db_type

    @property
    def timeout(self) -> timedelta:
        return self._timeout

    @property
    def metadata(self):
        return self._metadata

    @property
    def is_async(self):
        raise NotImplementedError

    @property
    def connection_class(self):
        raise NotImplementedError

    def new_connection(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    async def async_start(self):
        raise NotImplementedError

    async def async_stop(self):
        raise NotImplementedError

    @contextlib.contextmanager
    def transaction_context(self, connection, autocommit: bool = True):
        raise NotImplementedError

    @contextlib.asynccontextmanager
    async def async_transaction_context(self, connection, autocommit: bool = True):
        raise NotImplementedError


# noinspection PyPep8Naming
class SqlAlchemySyncEngine(SqlStorageEngine):
    def __init__(self, backend: SqlStorageBackend, name: str, engine, metadata,
                 db_type: SqlStorageType, session_class, timeout: timedelta):
        super().__init__(backend, name, engine, metadata, db_type, timeout)
        self._session_class = session_class
        self._lock = threading.Lock()
        self._counter = 0

    @property
    def is_async(self):
        return False

    @property
    def connection_class(self):
        return Session

    def new_connection(self):
        return self._session_class()

    def start(self):
        with self._lock:
            if 0 == self._counter:
                logger.info(tr('dropland.blocks.sql.engine.started')
                            .format(db_type=self.db_type, async_=f'async=False'))
            self._counter += 1

    def stop(self):
        with self._lock:
            if 1 == self._counter:
                self.raw_engine.dispose()
                logger.info(tr('dropland.blocks.sql.engine.stopped')
                            .format(db_type=self.db_type, async_=f'async=False'))
            self._counter = max(self._counter - 1, 0)

    async def async_start(self):
        raise RuntimeError('Use start method')

    async def async_stop(self):
        raise RuntimeError('Use stop method')

    @contextlib.contextmanager
    def transaction_context(self, connection: Session, autocommit: bool = True):
        tx = connection

        yield tx

        if sys.exc_info()[0]:
            tx.rollback()
        else:
            if autocommit:
                tx.commit()
            else:
                tx.rollback()

    @contextlib.asynccontextmanager
    async def async_transaction_context(self, connection, autocommit: bool = True):
        raise RuntimeError('Use transaction_context method')


# noinspection PyPep8Naming
class SqlAlchemyAsyncEngine(SqlStorageEngine):
    def __init__(self, backend: SqlStorageBackend, name: str, engine, metadata,
                 db_type: SqlStorageType, session_class, timeout: timedelta):
        super().__init__(backend, name, engine, metadata, db_type, timeout)
        self._session_class = session_class
        self._lock = asyncio.Lock()
        self._counter = 0

    @property
    def is_async(self):
        return True

    @property
    def connection_class(self):
        return AsyncSession

    def new_connection(self):
        return self._session_class()

    def start(self):
        raise RuntimeError('Use async_start method')

    def stop(self):
        raise RuntimeError('Use async_stop method')

    async def async_start(self):
        async with self._lock:
            if 0 == self._counter:
                logger.info(tr('dropland.blocks.sql.engine.started')
                            .format(db_type=self.db_type, async_=f'async=True'))
            self._counter += 1

    async def async_stop(self):
        async with self._lock:
            if 1 == self._counter:
                await self.raw_engine.dispose()
                logger.info(tr('dropland.blocks.sql.engine.stopped')
                            .format(db_type=self.db_type, async_=f'async=True'))
            self._counter = max(self._counter - 1, 0)

    @contextlib.contextmanager
    def transaction_context(self, connection: Session, autocommit: bool = True):
        raise RuntimeError('Use async_transaction_context method')

    @contextlib.asynccontextmanager
    async def async_transaction_context(self, connection: AsyncSession, autocommit: bool = True):
        tx = connection

        yield tx

        if sys.exc_info()[0]:
            await tx.rollback()
        else:
            if autocommit:
                await tx.commit()
            else:
                await tx.rollback()
