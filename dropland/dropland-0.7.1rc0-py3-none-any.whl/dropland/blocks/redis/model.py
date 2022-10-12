import asyncio
import contextlib
import enum
from datetime import timedelta
from typing import Any, Optional

from dependency_injector.wiring import Provide

from dropland.data.context import get_context
from dropland.data.models.cache import MethodCache
from dropland.data.models.nosql import NoSqlModel, NoSqlProxyModel
from dropland.data.serializers import Serializer, Deserializer
from dropland.data.serializers.pickle import PickleSerializer, PickleDeserializer
from .engine import RedisStorageEngine


class RedisCacheType(int, enum.Enum):
    SIMPLE = 0
    HASH = 1


class RedisModel(NoSqlModel):
    class Meta(NoSqlModel.Meta):
        _redis_engine = None

    def __init_subclass__(
            cls, redis_engine: RedisStorageEngine = None,
            cache_type: RedisCacheType = RedisCacheType.SIMPLE,
            serializer: Optional[Serializer] = None,
            deserializer: Optional[Deserializer] = None,
            ttl_enabled: bool = True,
            **kwargs):
        from .cache import SimpleRedisModelCache, HashRedisModelCache

        if not redis_engine:
            return super().__init_subclass__(**kwargs)

        serializer = serializer or PickleSerializer()
        deserializer = deserializer or PickleDeserializer()

        protocol_class = SimpleRedisModelCache \
            if cache_type == RedisCacheType.SIMPLE \
            else HashRedisModelCache

        cache_protocol = protocol_class(
            redis_engine, cls.__name__,
            serializer, deserializer,
            ttl_enabled=ttl_enabled
        )

        cls.Meta._redis_engine = redis_engine

        super().__init_subclass__(
            cache_protocol=cache_protocol,
            serializer=serializer,
            deserializer=deserializer,
            **kwargs
        )

    def get_id_value(self) -> Any:
        raise NotImplementedError

    # noinspection PyProtectedMember
    @classmethod
    def get_engine(cls) -> 'RedisStorageEngine':
        return cls.Meta._redis_engine

    @classmethod
    @contextlib.asynccontextmanager
    async def _async_session_context(cls, session_context=Provide['session_context']):
        ctx = get_context()
        if not hasattr(ctx, '_redis_cond'):
            ctx._redis_cond = asyncio.Condition()

        async with ctx._redis_cond:
            if hasattr(ctx, 'redis'):
                ctx._redis_cnt += 1
                ctx._redis_cond.release()
                try:
                    yield ctx
                finally:
                    await ctx._redis_cond.acquire()
                    ctx._redis_cnt -= 1
                    if 0 == ctx._redis_cnt:
                        ctx._redis_cond.notify()
            else:
                engine = cls.get_engine()
                session_context = await session_context
                ctx.redis = session_context.get_session(engine.name)
                ctx._redis_cnt = 1 if not hasattr(ctx, '_redis_cnt') else ctx._redis_cnt + 1
                ctx._redis_cond.release()
                try:
                    yield ctx
                finally:
                    await ctx._redis_cond.acquire()
                    ctx._redis_cnt -= 1
                    if 0 == ctx._redis_cnt:
                        del ctx.redis
                    else:
                        await ctx._redis_cond.wait_for(lambda: 0 == ctx._redis_cnt)
                        del ctx.redis


class RedisProxyModel(NoSqlProxyModel, RedisModel):
    class Meta(NoSqlProxyModel.Meta, RedisModel.Meta):
        pass

    def __init_subclass__(cls, redis_engine: RedisStorageEngine = None, **kwargs):
        super().__init_subclass__(redis_engine=redis_engine, **kwargs)
        cls.Meta._redis_engine = redis_engine

    def get_id_value(self) -> Any:
        raise NotImplementedError


class RedisMethodCache(MethodCache):
    def __init__(
            self, redis_engine: RedisStorageEngine, model_name: str,
            cache_type: RedisCacheType = RedisCacheType.SIMPLE,
            serializer: Optional[Serializer] = None,
            deserializer: Optional[Deserializer] = None,
            ttl: Optional[timedelta] = None):
        from .cache import SimpleRedisModelCache, HashRedisModelCache

        serializer = serializer or PickleSerializer()
        deserializer = deserializer or PickleDeserializer()

        protocol_class = SimpleRedisModelCache \
            if cache_type == RedisCacheType.SIMPLE \
            else HashRedisModelCache

        cache_protocol = protocol_class(
            redis_engine, model_name,
            serializer, deserializer,
            ttl_enabled=True
        )

        super().__init__(cache_protocol, ttl)
        self._redis_engine = redis_engine
        self._cache_type = cache_type
        self._engine_name = redis_engine.name

    @contextlib.asynccontextmanager
    async def _async_session_context(self, session_context=Provide['session_context']):
        ctx = get_context()
        if not hasattr(ctx, '_redis_cond'):
            ctx._redis_cond = asyncio.Condition()

        async with ctx._redis_cond:
            if hasattr(ctx, 'redis'):
                ctx._redis_cnt += 1
                ctx._redis_cond.release()
                try:
                    yield ctx
                finally:
                    await ctx._redis_cond.acquire()
                    ctx._redis_cnt -= 1
                    if 0 == ctx._redis_cnt:
                        ctx._redis_cond.notify()
            else:
                session_context = await session_context
                ctx.redis = session_context.get_session(self._engine_name)
                ctx._redis_cnt = 1 if not hasattr(ctx, '_redis_cnt') else ctx._redis_cnt + 1
                ctx._redis_cond.release()
                try:
                    yield ctx
                finally:
                    await ctx._redis_cond.acquire()
                    ctx._redis_cnt -= 1
                    if 0 == ctx._redis_cnt:
                        del ctx.redis
                    else:
                        await ctx._redis_cond.wait_for(lambda: 0 == ctx._redis_cnt)
                        del ctx.redis
