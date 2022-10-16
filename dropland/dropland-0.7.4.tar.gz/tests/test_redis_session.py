import pytest

from dropland.blocks.redis import USE_REDIS

pytestmark = pytest.mark.skipif(not USE_REDIS, reason='For Redis only')

if USE_REDIS:
    from dropland.blocks.redis.containers import RedisStorage, SingleRedisStorage, MultipleRedisStorage, RedisBlock
    from dropland.blocks.redis.engine import EngineConfig
    from tests import REDIS_URI


def test_session_connections(test_redis_storage, redis_engine, redis_session):
    assert not redis_session.get_session('_')

    session = redis_session.get_session('dropland')
    assert session
    assert session.engine is redis_engine
    assert session.connection

    created, session = redis_session.get_or_create_session('dropland')
    assert not created
    assert session
    assert session.engine is redis_engine
    assert session.connection

    assert not test_redis_storage.get_session('_')
    assert test_redis_storage.get_session('dropland') is session


@pytest.mark.asyncio
async def test_container_sessions():
    config = EngineConfig(url=REDIS_URI)

    cont = RedisStorage()
    engine = cont.create_engine('dropland', config)
    block = RedisBlock(cont)
    await block.startup()
    await block.session_begin()

    session = cont.get_session('dropland')
    assert session
    assert session.engine is engine
    assert session.connection
    assert not cont.get_session('_')
    await block.session_finish()
    await block.shutdown()
    cont.unwire()

    cont = SingleRedisStorage()
    cont.config.from_dict({
        'name': 'dropland1',
        'engine_config': config
    })
    engine = cont.create_engine()
    block = RedisBlock(cont)
    await block.startup()
    await block.session_begin()

    session = cont.get_session()
    assert session
    assert session.engine is engine
    assert session.connection
    await block.session_finish()
    await block.shutdown()
    cont.unwire()

    cont = MultipleRedisStorage()
    cont.config.from_dict({
        'one': {
            'name': 'dropland1',
            'engine_config': config
        },
        'two': {
            'name': 'dropland2',
            'engine_config': config
        },
    })
    engine1 = cont.create_engine('one')
    engine2 = cont.create_engine('two')
    block = RedisBlock(cont)
    await block.startup()
    await block.session_begin()

    for name, engine in zip(('one', 'two'), (engine1, engine2)):
        session = cont.get_session(name)
        assert session
        assert session.engine is engine
        assert session.connection

    assert not cont.get_session('_')
    await block.session_finish()
    await block.shutdown()
    cont.unwire()
