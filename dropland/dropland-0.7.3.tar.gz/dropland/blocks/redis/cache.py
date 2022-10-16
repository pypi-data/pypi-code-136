from collections import OrderedDict
from datetime import timedelta
from typing import Optional, Dict, Any, List, Tuple, AsyncIterable

from dropland.blocks.redis import RedisStorageEngine
from dropland.data.cache import ModelCacheProtocol, ModelCacheData
from dropland.data.context import ContextData
from dropland.data.serializers import Serializer, Deserializer


class SimpleRedisModelCache(ModelCacheProtocol):
    def __init__(self, engine: RedisStorageEngine, class_key: str,
                 serializer: Serializer, deserializer: Deserializer, ttl_enabled: bool = True):
        self._redis_engine = engine
        self._class_key = class_key
        self._serializer = serializer
        self._deserializer = deserializer
        self._ttl_enabled = ttl_enabled
        self._null_data = self._serializer.serialize(None)

    def get_model_cache_key(self) -> str:
        return f'{self._redis_engine.name}.models.{self._class_key}'

    async def cache_one(
            self, ctx: ContextData, data: ModelCacheData, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        cache_kwargs = dict()

        if self._ttl_enabled:
            expiration = ttl or self._redis_engine.default_ttl
            total_seconds = expiration.total_seconds()

            if total_seconds > 1:
                cache_kwargs['expire'] = int(total_seconds)
            elif 0 < total_seconds < 1:
                cache_kwargs['pexpire'] = int(total_seconds * 1000)
            else:
                total_seconds = self._redis_engine.default_ttl.total_seconds()
                cache_kwargs['expire'] = int(total_seconds) if total_seconds > 1 else 60

        serialized = self._serializer.serialize(data.data)
        return bool(await ctx.redis.connection.set(self.get_cache_key(data.cache_id), serialized, **cache_kwargs))

    async def cache_many(
            self, ctx: ContextData, objects: List[ModelCacheData],
            ttl: Optional[timedelta] = None, **kwargs) -> bool:
        if not objects:
            return False
        res = False

        tx = ctx.redis.connection.multi_exec()

        for instance in objects:
            cache_kwargs = dict()

            if self._ttl_enabled:
                expiration = ttl or self._redis_engine.default_ttl
                total_seconds = expiration.total_seconds()

                if total_seconds > 1:
                    cache_kwargs['expire'] = int(total_seconds)
                elif 0 < total_seconds < 1:
                    cache_kwargs['pexpire'] = int(total_seconds * 1000)
                else:
                    total_seconds = self._redis_engine.default_ttl.total_seconds()
                    cache_kwargs['expire'] = int(total_seconds) if total_seconds > 1 else 60

            serialized = self._serializer.serialize(instance.data)
            tx.set(self.get_cache_key(instance.cache_id), serialized, **cache_kwargs)

        for r in await tx.execute():
            res |= r

        return bool(res)

    async def load_one(
            self, ctx: ContextData, cache_key: str, **kwargs) -> Tuple[bool, Optional[Any]]:
        if res := await ctx.redis.connection.get(cache_key):
            return True, self._deserializer.deserialize(res)
        return False, None

    async def load_many(
            self, ctx: ContextData, indices: List[Any], **kwargs) -> List[Optional[Dict[str, Any]]]:
        if not indices:
            return []

        cache_keys = [self.get_cache_key(id_value) for id_value in indices]
        res = await ctx.redis.connection.mget(*cache_keys)
        objects: Dict[Any, Any] = OrderedDict()

        for id_value, data in zip(indices, res):
            objects[id_value] = self._deserializer.deserialize(data) if data is not None else None

        return list(objects.values())

    async def drop_one(self, ctx: ContextData, cache_key: str) -> bool:
        return bool(await ctx.redis.connection.delete(cache_key))

    async def drop_many(self, ctx: ContextData, indices: List[Any] = None) -> int:
        if indices and len(indices) > 0:
            cache_keys = [self.get_cache_key(id_value) for id_value in indices]
        else:
            model_cache_key = self.get_model_cache_key()
            cache_keys = await ctx.redis.connection.keys(f'{model_cache_key}:*')

        return int(await ctx.redis.connection.delete(*cache_keys)) if cache_keys else 0

    async def drop_all(self, ctx: ContextData, prefix: Optional[str] = None) -> int:
        model_cache_key = self.get_model_cache_key()
        cache_key = f'{model_cache_key}:{prefix}*' if prefix else f'{model_cache_key}:*'
        keys_to_delete = await ctx.redis.connection.keys(cache_key)
        return int(await ctx.redis.connection.delete(*keys_to_delete)) if keys_to_delete else 0

    async def exists(self, ctx: ContextData, cache_key: str) -> bool:
        if await ctx.redis.connection.exists(cache_key):
            return await ctx.redis.connection.get(cache_key) != self._null_data
        return False

    async def scan(self, ctx: ContextData, cache_key: str = None,
                   match: str = None, count: int = None) -> AsyncIterable[Tuple[str, Optional[Dict[str, Any]]]]:
        match = f'{cache_key}:{match}' if cache_key and match else match
        async for k in ctx.redis.connection.iscan(match=match, count=count):
            cache_key = k.decode('utf-8')
            yield cache_key.split(':')[1] if ':' in cache_key else cache_key, (await self.load_one(ctx, cache_key))[1]


class HashRedisModelCache(ModelCacheProtocol):
    def __init__(self, engine: RedisStorageEngine, class_key: str,
                 serializer: Serializer, deserializer: Deserializer, ttl_enabled: bool = True):
        self._redis_engine = engine
        self._class_key = class_key
        self._serializer = serializer
        self._deserializer = deserializer
        self._ttl_enabled = ttl_enabled
        self._null_data = self._serializer.serialize(None)

    def get_model_cache_key(self) -> str:
        return f'{self._redis_engine.name}.models.{self._class_key}'

    async def cache_one(
            self, ctx: ContextData, data: ModelCacheData, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        model_cache_key, cache_id = self.get_model_cache_key(), self.get_cache_id(data.cache_id)
        serialized = self._serializer.serialize(data.data)

        if self._ttl_enabled:
            res = False
            tx = ctx.redis.connection.multi_exec()
            expiration = ttl or self._redis_engine.default_ttl
            tx.hset(model_cache_key, cache_id, serialized)
            tx.expire(model_cache_key, int(expiration.total_seconds()))

            for r in await tx.execute():
                res |= r

            return bool(res)

        return bool(await ctx.redis.connection.hset(model_cache_key, cache_id, serialized))

    async def cache_many(
            self, ctx: ContextData, objects: List[ModelCacheData],
            ttl: Optional[timedelta] = None, **kwargs) -> bool:
        if not objects:
            return False

        model_cache_key = self.get_model_cache_key()
        obj_dict = {
            self.get_cache_id(instance.cache_id): self._serializer.serialize(instance.data)
            for instance in objects
        }

        if self._ttl_enabled:
            res = False
            tx = ctx.redis.connection.multi_exec()
            expiration = ttl or self._redis_engine.default_ttl
            tx.hmset_dict(model_cache_key, obj_dict)
            tx.expire(model_cache_key, int(expiration.total_seconds()))

            for r in await tx.execute():
                res |= r

            return bool(res)

        return bool(await ctx.redis.connection.hmset_dict(model_cache_key, obj_dict))

    async def load_one(
            self, ctx: ContextData, cache_key: str, **kwargs) -> Tuple[bool, Optional[Any]]:
        if ':' in cache_key:
            model_cache_key, cache_id = cache_key.split(':', maxsplit=1)
            if res := await ctx.redis.connection.hget(model_cache_key, cache_id):
                return True, self._deserializer.deserialize(res)
            return False, None
        else:
            if res := await ctx.redis.connection.get(cache_key):
                return True, self._deserializer.deserialize(res)
            return False, None

    async def load_many(
            self, ctx: ContextData, indices: List[Any], **kwargs) -> List[Optional[Dict[str, Any]]]:
        if not indices:
            return []

        cache_keys = [self.get_cache_id(id_value) for id_value in indices]
        res = await ctx.redis.connection.hmget(self.get_model_cache_key(), *cache_keys)
        objects: Dict[Any, Any] = OrderedDict()

        for id_value, data in zip(indices, res):
            objects[id_value] = self._deserializer.deserialize(data) if data is not None else None

        return list(objects.values())

    async def drop_one(self, ctx: ContextData, cache_key: str) -> bool:
        if ':' in cache_key:
            model_cache_key, cache_id = cache_key.split(':', maxsplit=1)
            return bool(await ctx.redis.connection.hdel(model_cache_key, cache_id))
        else:
            return bool(await ctx.redis.connection.delete(cache_key))

    async def drop_many(self, ctx: ContextData, indices: List[Any] = None) -> int:
        model_cache_key = self.get_model_cache_key()

        if indices and len(indices) > 0:
            cache_keys = [self.get_cache_id(id_value) for id_value in indices]
        else:
            cache_keys = await ctx.redis.connection.hkeys(model_cache_key)

        return int(await ctx.redis.connection.hdel(model_cache_key, *cache_keys)) if cache_keys else 0

    async def drop_all(self, ctx: ContextData, prefix: Optional[str] = None) -> int:
        model_cache_key = self.get_model_cache_key()
        if not prefix:
            keys_to_delete = await ctx.redis.connection.hkeys(model_cache_key)
        else:
            keys_to_delete = list()
            for cache_key in await ctx.redis.connection.hkeys(model_cache_key, encoding='ascii'):
                if cache_key.startswith(prefix):
                    keys_to_delete.append(cache_key)

        return int(await ctx.redis.connection.hdel(model_cache_key, *keys_to_delete)) if keys_to_delete else 0

    async def exists(self, ctx: ContextData, cache_key: str) -> bool:
        if ':' in cache_key:
            model_cache_key, cache_id = cache_key.split(':', maxsplit=1)
            e = bool(await ctx.redis.connection.hexists(model_cache_key, cache_id))
        else:
            e = bool(await ctx.redis.connection.exists(cache_key))
        if e:
            return await ctx.redis.connection.get(cache_key) != self._null_data
        return False

    async def scan(self, ctx: ContextData, cache_key: str = None,
                   match: str = None, count: int = None) -> AsyncIterable[Tuple[str, Optional[Dict[str, Any]]]]:
        async for k, data in ctx.redis.connection.ihscan(cache_key, match=match, count=count):
            yield k.decode('utf-8'), self._deserializer.deserialize(data)
