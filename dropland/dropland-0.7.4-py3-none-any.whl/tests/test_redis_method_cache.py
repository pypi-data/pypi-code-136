from datetime import datetime

import pytest

from dropland.blocks.redis import USE_REDIS

pytestmark = pytest.mark.skipif(not USE_REDIS, reason='For Redis only')

if USE_REDIS:
    from dropland.blocks.redis.model import RedisCacheType, RedisMethodCache
    from .redis_models_data import redis_engine


@pytest.mark.asyncio
@pytest.mark.parametrize('cache_type', (RedisCacheType.SIMPLE, RedisCacheType.HASH), ids=['simple', 'hash'])
async def test_method_cache(cache_type, redis_session):
    method_cache = RedisMethodCache(redis_engine, 'test', cache_type)

    assert method_cache.get_model_cache_key() == 'dropland.models.test'
    assert method_cache.get_cache_id(123) == '123'
    assert method_cache.get_cache_key(1) == 'dropland.models.test:1'

    args = {'a': 1, 'b': 12.34, 'c': 'asdf', 'd': datetime.now()}
    exists, data = await method_cache.get('method', args)
    assert not exists
    assert not data

    assert await method_cache.put('method', None, None)
    exists, data = await method_cache.get('method', args)
    assert not exists
    assert not data
    exists, data = await method_cache.get('method', None)
    assert exists
    assert data is None

    assert await method_cache.put('method', args, None)
    exists, data = await method_cache.get('method', args)
    assert exists
    assert data is None
    exists, data = await method_cache.get('method', None)
    assert exists
    assert data is None

    assert await method_cache.put('method', args, 123)
    exists, data = await method_cache.get('method', args)
    assert exists
    assert data is 123
    exists, data = await method_cache.get('method', None)
    assert exists
    assert data is None

    assert await method_cache.put('method', None, '456')
    exists, data = await method_cache.get('method', args)
    assert exists
    assert data is 123
    exists, data = await method_cache.get('method', None)
    assert exists
    assert data == '456'

    assert await method_cache.drop('method', args)
    assert not await method_cache.drop('method', args)
    exists, data = await method_cache.get('method', args)
    assert not exists
    assert not data
    exists, data = await method_cache.get('method', None)
    assert exists
    assert data == '456'

    assert await method_cache.drop('method', None)
    assert not await method_cache.drop('method', None)
    exists, data = await method_cache.get('method', args)
    assert not exists
    assert not data
    exists, data = await method_cache.get('method', None)
    assert not exists
    assert not data
