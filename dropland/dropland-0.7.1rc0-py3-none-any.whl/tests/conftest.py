import asyncio

import pytest

from dropland.blocks.redis import USE_REDIS
from dropland.blocks.rmq import USE_RMQ
from dropland.blocks.sql import USE_SQL
from dropland.blocks.sql.base import SqlStorageType

if USE_REDIS:
    from dropland.blocks.redis.containers import RedisStorage
    from dropland.blocks.redis.engine import EngineConfig as RedisEngineConfig

if USE_RMQ:
    from dropland.blocks.rmq.containers import RmqStorage
    from dropland.blocks.rmq.engine import EngineConfig as RmqEngineConfig

if USE_SQL:
    from dropland.blocks.sql.containers import MultipleSqlStorage, SqlStorage
    from dropland.blocks.sql import EngineConfig as SqlEngineConfig

from tests import MYSQL_URI, POSTGRES_URI, REDIS_URI, RMQ_URI, SQLITE_URI


if USE_SQL:
    sql_storage = MultipleSqlStorage()

    sql_storage.config.from_dict({
        'sqlite': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': SqlEngineConfig(
                url=SQLITE_URI,
                pool_min_size=1, pool_max_size=2,
                pool_expire_seconds=15, pool_timeout_seconds=15,
            ),
            'use_async': False
        },
        'asqlite': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': SqlEngineConfig(
                url=SQLITE_URI,
                pool_min_size=1, pool_max_size=2,
                pool_expire_seconds=15, pool_timeout_seconds=15,
            ),
            'use_async': True
        },
        'pg': {
            'db_type': SqlStorageType.POSTGRES,
            'engine_config': SqlEngineConfig(
                url=POSTGRES_URI,
                pool_min_size=1, pool_max_size=2,
                pool_expire_seconds=15, pool_timeout_seconds=15,
            ),
            'use_async': False
        },
        'apg': {
            'db_type': SqlStorageType.POSTGRES,
            'engine_config': SqlEngineConfig(
                url=POSTGRES_URI,
                pool_min_size=1, pool_max_size=2,
                pool_expire_seconds=15, pool_timeout_seconds=15,
            ),
            'use_async': True
        },
        'ms': {
            'db_type': SqlStorageType.MYSQL,
            'engine_config': SqlEngineConfig(
                url=MYSQL_URI,
                pool_min_size=1, pool_max_size=2,
                pool_expire_seconds=15, pool_timeout_seconds=15,
            ),
            'use_async': False
        },
        'ams': {
            'db_type': SqlStorageType.MYSQL,
            'engine_config': SqlEngineConfig(
                url=MYSQL_URI,
                pool_min_size=1, pool_max_size=2,
                pool_expire_seconds=15, pool_timeout_seconds=15,
            ),
            'use_async': True
        },
    })


@pytest.fixture(scope='session')
def test_sql_storage():
    if USE_SQL:
        return SqlStorage()
    else:
        return None


@pytest.fixture(scope='session')
def test_redis_storage():
    if USE_REDIS:
        return RedisStorage()
    else:
        return None


@pytest.fixture(scope='session')
def test_rmq_storage():
    if USE_RMQ:
        return RmqStorage()
    else:
        return None


@pytest.fixture(scope='session')
def sql_sync_engine(test_sql_storage):
    conf = sql_storage.config.get('sqlite')
    return test_sql_storage.create_engine(
        'dropland-test-sync', conf['engine_config'], conf['db_type'], conf.get('use_async')
    )


@pytest.fixture(scope='session')
def sql_async_engine(test_sql_storage):
    conf = sql_storage.config.get('asqlite')
    return test_sql_storage.create_engine(
        'dropland-test-async', conf['engine_config'], conf['db_type'], conf.get('use_async')
    )


@pytest.fixture(scope='session')
def sqlite_engine():
    return sql_storage.create_engine('sqlite')


@pytest.fixture(scope='session')
def sqlite_async_engine():
    return sql_storage.create_engine('asqlite')


@pytest.fixture(scope='session')
def pg_engine():
    return sql_storage.create_engine('pg')


@pytest.fixture(scope='session')
def pg_async_engine():
    return sql_storage.create_engine('apg')


@pytest.fixture(scope='session')
def mysql_engine():
    return sql_storage.create_engine('ms')


@pytest.fixture(scope='session')
def mysql_async_engine():
    return sql_storage.create_engine('ams')


@pytest.fixture(scope='session')
def redis_engine(test_redis_storage):
    engine_config = RedisEngineConfig(url=REDIS_URI)
    return test_redis_storage.create_engine('dropland', engine_config)


@pytest.fixture(scope='session')
def rmq_engine(test_rmq_storage):
    engine_config = RmqEngineConfig(url=RMQ_URI)
    return test_rmq_storage.create_engine('dropland', engine_config)


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


if USE_SQL:
    @pytest.fixture(scope='function')
    def sync_sql_session(event_loop, test_sql_storage):
        session = test_sql_storage.sync_session_context(autocommit=False)
        yield session
        test_sql_storage.sync_session_context.shutdown()

    @pytest.fixture(scope='function')
    async def async_sql_session(event_loop, test_sql_storage):
        session = await test_sql_storage.session_context(autocommit=False)
        yield session
        await test_sql_storage.session_context.shutdown()


if USE_REDIS:
    @pytest.fixture(scope='module')
    def wire_redis_storage(test_redis_storage):
        test_redis_storage.wire()
        yield
        test_redis_storage.unwire()

    @pytest.fixture(scope='function')
    async def redis_session(event_loop, wire_redis_storage, test_redis_storage, redis_engine):
        session = await test_redis_storage.session_context.init()
        yield session
        await test_redis_storage.session_context.shutdown()


if USE_RMQ:
    @pytest.fixture(scope='module')
    def wire_rmq_storage(test_rmq_storage):
        test_rmq_storage.wire()
        yield
        test_rmq_storage.unwire()

    @pytest.fixture(scope='function')
    async def rmq_session(event_loop, wire_rmq_storage, test_rmq_storage, rmq_engine):
        session = await test_rmq_storage.session_context.init()
        yield session
        await test_rmq_storage.session_context.shutdown()
