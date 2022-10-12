import pytest

from dropland.blocks.rmq import USE_RMQ

pytestmark = pytest.mark.skipif(not USE_RMQ, reason='For RabbitMQ only')

if USE_RMQ:
    from dropland.blocks.rmq.containers import RmqStorage, SingleRmqStorage, MultipleRmqStorage
    from dropland.blocks.rmq.engine import EngineConfig
    from tests import RMQ_URI


def test_session_connections(test_rmq_storage, rmq_engine, rmq_session):
    assert not rmq_session.get_session('_')

    session = rmq_session.get_session('dropland')
    assert session
    assert session.engine is rmq_engine
    assert session.connection

    created, session = rmq_session.get_or_create_session('dropland')
    assert not created
    assert session
    assert session.engine is rmq_engine
    assert session.connection

    assert not test_rmq_storage.get_session('_')
    assert test_rmq_storage.get_session('dropland') is session


@pytest.mark.asyncio
async def test_container_sessions():
    config = EngineConfig(url=RMQ_URI)

    cont = RmqStorage()
    engine = cont.create_engine('dropland', config)
    await cont.session_context.init()

    session = cont.get_session('dropland')
    assert session
    assert session.engine is engine
    assert session.connection
    assert not cont.get_session('_')
    cont.unwire()

    cont = SingleRmqStorage()
    cont.config.from_dict({
        'name': 'dropland1',
        'engine_config': config
    })
    engine = cont.create_engine()
    await cont.session_context.init()

    session = cont.get_session()
    assert session
    assert session.engine is engine
    assert session.connection
    cont.unwire()

    cont = MultipleRmqStorage()
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
    await cont.session_context.init()

    for name, engine in zip(('one', 'two'), (engine1, engine2)):
        session = cont.get_session(name)
        assert session
        assert session.engine is engine
        assert session.connection

    assert not cont.get_session('_')
    cont.unwire()
