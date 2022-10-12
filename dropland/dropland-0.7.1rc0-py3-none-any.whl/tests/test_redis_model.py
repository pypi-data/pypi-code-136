import asyncio
from datetime import timedelta

import pytest

from dropland.blocks.redis import USE_REDIS

pytestmark = pytest.mark.skipif(not USE_REDIS, reason='For Redis only')

if USE_REDIS:
    from dropland.blocks.redis.model import RedisCacheType, RedisModel
    from .redis_models_data import redis_engine

    class TestModel(RedisModel, redis_engine=redis_engine, cache_type=RedisCacheType.SIMPLE):
        a: int = 1
        b: str = '123'

        def __init__(self):
            self.a = 1
            self.b = '123'

        def get_id_value(self):
            return self.a


@pytest.mark.asyncio
async def test_model_fields(redis_session):
    assert TestModel.get_model_cache_key() == 'dropland.models.TestModel'
    assert TestModel.get_cache_key(1) == 'dropland.models.TestModel:1'
    assert TestModel.get_cache_id(123) == '123'
    assert TestModel.get_engine() is redis_engine


@pytest.mark.asyncio
async def test_model_serde(redis_session):
    m = TestModel()
    assert m.a == 1
    assert m.b == '123'

    assert TestModel.get_fields() == {'a', 'b'}
    assert m.get_values() == {'a': 1, 'b': '123'}

    ser = m.serialize()
    assert isinstance(ser, bytes)
    res = TestModel.deserialize(ser)
    assert isinstance(res, TestModel)

    assert res.a == 1
    assert res.b == '123'


@pytest.mark.asyncio
async def test_exists_save_and_get(redis_session):
    m = TestModel()

    assert not await TestModel.exists(1)
    assert not await TestModel.get(1)

    assert await m.save()
    assert await TestModel.exists(1)

    m2 = await TestModel.get(1)
    assert m2.a == 1
    assert m2.b == '123'

    await m.save(timedelta(milliseconds=10))
    assert await TestModel.exists(1, no_cache=True)
    assert await TestModel.get(1, no_cache=True)
    await asyncio.sleep(0.02)
    assert not await TestModel.exists(1, no_cache=True)
    assert not await TestModel.get(1, no_cache=True)


@pytest.mark.asyncio
async def test_load(redis_session):
    m = TestModel()

    assert not await m.load()
    assert await m.save()
    assert await m.load()

    assert m.a == 1
    assert m.b == '123'

    m.b = None
    assert m.a == 1
    assert m.b is None

    assert await m.load()
    assert m.a == 1
    assert m.b == '123'


@pytest.mark.asyncio
async def test_delete(redis_session):
    m = TestModel()
    await m.save()

    m2 = await TestModel.get(1)
    assert m2.a == 1
    assert m2.b == '123'

    assert await m.load()
    assert m.a == 1
    assert m.b == '123'

    assert await TestModel.exists(1)
    assert await m.delete()
    assert not await m.delete()

    assert not await TestModel.exists(1)
    assert not await TestModel.get(1)
    assert not await m.load()


@pytest.mark.asyncio
async def test_save_all_get_any_and_scan(redis_session):
    m, m2 = TestModel(), TestModel()
    m2.a = 2

    assert await TestModel.save_all([m, m2])

    objects = await TestModel.get_any([])
    assert len(objects) == 0

    objects = await TestModel.get_any([1, 2])
    assert len(objects) == 2
    assert objects[0].a == 1
    assert objects[1].a == 2

    objects = await TestModel.get_any([-1, 1, 999999, 2, 0])
    assert len(objects) == 5
    assert objects[0] is None
    assert objects[1].a == 1
    assert objects[2] is None
    assert objects[3].a == 2
    assert objects[4] is None

    objects = {k: v async for k, v in TestModel.scan('*')}
    assert len(objects) == 2
    assert objects['1'].a == 1
    assert objects['2'].a == 2

    assert await TestModel.save_all([m, m2], timedelta(milliseconds=10))
    objects = await TestModel.get_any([1, 2], no_cache=True)
    assert len(objects) == 2
    assert objects[0].a == 1
    assert objects[1].a == 2

    await asyncio.sleep(0.02)
    objects = await TestModel.get_any([1, 2], no_cache=True)
    assert objects == [None, None]


@pytest.mark.asyncio
async def test_delete_all(redis_session):
    m, m2 = TestModel(), TestModel()
    m2.a = 2

    assert await TestModel.save_all([m, m2])
    objects = await TestModel.get_any([1, 2])
    assert len(objects) == 2
    assert objects[0].a == 1
    assert objects[1].a == 2

    assert await TestModel.delete_all([1, 2])
    assert not await TestModel.delete_all([1, 2])

    assert await TestModel.save_all([m, m2])
    assert await TestModel.delete_all()
    assert not await TestModel.delete_all()

    objects = await TestModel.get_any([1, 2])
    assert objects == [None, None]
