import pytest

from tests.sql_models_data import USE_SQL

pytestmark = pytest.mark.skipif(not USE_SQL, reason='For SqlAlchemy only')

if USE_SQL:
    from dropland.blocks.sql.base import SqlStorageType
    from dropland.blocks.sql.containers import MultipleSqlStorage, SingleSqlStorage, SqlStorage
    from dropland.blocks.sql.engine import EngineConfig
    from tests import SQLITE_URI


def test_sync_session_connections(test_sql_storage, sql_sync_engine, sync_sql_session):
    assert sync_sql_session.get_session('dropland-test-sync')
    assert not sync_sql_session.get_session('_')

    for session in sync_sql_session.get_sessions_for_type(SqlStorageType.SQLITE, False):
        assert session.engine
        assert session.engine.db_type == SqlStorageType.SQLITE
        assert session.engine.is_async is False
        assert session.connection
        assert session.in_transaction

    created, session = sync_sql_session.get_or_create_session('dropland-test-sync')
    assert not created
    assert session
    assert session.engine is sql_sync_engine
    assert session.connection
    assert session.in_transaction

    assert not test_sql_storage.get_session('_')
    assert test_sql_storage.get_session('dropland-test-sync') is session


@pytest.mark.asyncio
async def test_async_session_connections(test_sql_storage, sql_async_engine, async_sql_session):
    assert async_sql_session.get_session('dropland-test-async')
    assert not async_sql_session.get_session('_')

    for session in async_sql_session.get_sessions_for_type(SqlStorageType.SQLITE, True):
        assert session.engine
        assert session.engine.db_type == SqlStorageType.SQLITE
        assert session.engine.is_async is True
        assert session.connection
        assert session.in_transaction

    created, session = async_sql_session.get_or_create_session('dropland-test-async')
    assert not created
    assert session
    assert session.engine is sql_async_engine
    assert session.connection
    assert session.in_transaction

    assert not test_sql_storage.get_session('_')
    assert test_sql_storage.get_session('dropland-test-async') is session


def test_sync_container_sessions():
    sqlite_config = EngineConfig(
        url=SQLITE_URI,
        pool_min_size=1, pool_max_size=2,
        pool_expire_seconds=15, pool_timeout_seconds=15,
    )

    cont = SqlStorage()
    engine = cont.create_engine('dropland', sqlite_config, SqlStorageType.SQLITE, use_async=False)
    cont.sync_session_context.init()

    session = cont.get_session('dropland')
    assert session
    assert session.engine is engine
    assert session.connection
    assert not cont.get_session('_')
    cont.unwire()

    cont = SingleSqlStorage()
    cont.config.from_dict({
        'name': 'dropland',
        'db_type': SqlStorageType.SQLITE,
        'engine_config': sqlite_config,
        'use_async': False,
    })
    engine = cont.create_engine()
    cont.sync_session_context.init()

    session = cont.get_session()
    assert session
    assert session.engine is engine
    assert session.connection
    cont.unwire()

    cont = MultipleSqlStorage()
    cont.config.from_dict({
        'one': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': False,
        },
        'two': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': False,
        },
    })
    engine1 = cont.create_engine('one')
    engine2 = cont.create_engine('two')
    cont.sync_session_context.init()

    for name, engine in zip(('one', 'two'), (engine1, engine2)):
        session = cont.get_session(name)
        assert session
        assert session.engine is engine
        assert session.connection

    assert not cont.get_session('_')
    cont.unwire()


@pytest.mark.asyncio
async def test_async_container_sessions():
    sqlite_config = EngineConfig(
        url=SQLITE_URI,
        pool_min_size=1, pool_max_size=2,
        pool_expire_seconds=15, pool_timeout_seconds=15,
    )

    cont = SqlStorage()
    engine = cont.create_engine('dropland', sqlite_config, SqlStorageType.SQLITE, use_async=True)
    await cont.session_context.init()

    session = cont.get_session('dropland')
    assert session
    assert session.engine is engine
    assert session.connection
    assert not cont.get_session('_')
    cont.unwire()

    cont = SingleSqlStorage()
    cont.config.from_dict({
        'name': 'dropland',
        'db_type': SqlStorageType.SQLITE,
        'engine_config': sqlite_config,
        'use_async': True,
    })
    engine = cont.create_engine()
    await cont.session_context.init()

    session = cont.get_session()
    assert session
    assert session.engine is engine
    assert session.connection
    cont.unwire()

    cont = MultipleSqlStorage()
    cont.config.from_dict({
        'one': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': True,
        },
        'two': {
            'db_type': SqlStorageType.SQLITE,
            'engine_config': sqlite_config,
            'use_async': True,
        },
    })
    engine1 = cont.create_engine('one')
    engine2 = cont.create_engine('two')
    await cont.session_context.init()

    for name, engine in zip(('one', 'two'), (engine1, engine2)):
        session = cont.get_session(name)
        assert session
        assert session.engine is engine
        assert session.connection

    assert not cont.get_session('_')
    cont.unwire()
