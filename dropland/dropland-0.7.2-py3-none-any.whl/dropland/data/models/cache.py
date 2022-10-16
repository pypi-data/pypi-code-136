import asyncio
import contextlib
import operator
from datetime import timedelta
from functools import reduce
from typing import Dict, Any, Optional, Tuple, List

from dropland.util import calculate_digest
from ..cache import ModelCacheProtocol, ModelCacheData


class MethodCache:
    def __init__(self, cache_protocol: ModelCacheProtocol, ttl: Optional[timedelta] = None):
        self._cache_protocol = cache_protocol
        self._ttl = ttl

    @property
    def cache_protocol(self) -> ModelCacheProtocol:
        return self._cache_protocol

    def get_model_cache_key(self) -> str:
        return self._cache_protocol.get_model_cache_key()

    def get_cache_id(self, id_value: Any) -> str:
        return self._cache_protocol.get_cache_id(id_value)

    def get_cache_key(self, id_value: Any) -> str:
        return self._cache_protocol.get_cache_key(id_value)

    @contextlib.asynccontextmanager
    async def _async_session_context(self, session=None):
        ...

    @staticmethod
    def cache_key_for(method: str, args: Optional[Dict[str, Any]] = None) -> str:
        id_data = [method]

        if args:
            id_data.append(calculate_digest(args))
        else:
            id_data.append('_')

        return ':'.join(id_data)

    async def put(self, method: str, args: Optional[Dict[str, Any]] = None,
                  data: Optional[Any] = None, cache_key: Optional[str] = None,
                  ttl: Optional[timedelta] = None, **kwargs) -> bool:
        cache_key = cache_key or self.cache_key_for(method, args)
        async with self._async_session_context() as ctx:
            data = ModelCacheData(cache_id=cache_key, data=data)
            return await self._cache_protocol.cache_one(ctx, data, ttl=ttl or self._ttl, **kwargs)

    async def get(self, method: str, args: Optional[Dict[str, Any]] = None,
                  cache_key: Optional[str] = None, **kwargs) -> Tuple[bool, Optional[Any]]:
        cache_key = cache_key or self.cache_key_for(method, args)
        async with self._async_session_context() as ctx:
            exists, data = await self._cache_protocol.load_one(
                ctx, self._cache_protocol.get_cache_key(cache_key), **kwargs)
            return exists, data

    async def drop(self, method: str, args: Optional[Dict[str, Any]] = None,
                   cache_key: Optional[str] = None) -> bool:
        cache_key = cache_key or self.cache_key_for(method, args)
        async with self._async_session_context() as ctx:
            return await self._cache_protocol.drop_one(ctx, self._cache_protocol.get_cache_key(cache_key))

    async def drop_all(self, methods: List[str] = None) -> int:
        methods = methods if methods else list()
        async with self._async_session_context() as ctx:
            if not methods:
                return await self._cache_protocol.drop_all(ctx)
            results = await asyncio.gather(
                *(self._cache_protocol.drop_all(ctx, method) for method in methods)
            )
            return reduce(operator.add, results, 0)
