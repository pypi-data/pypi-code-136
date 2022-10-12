import asyncio
import contextlib
from dataclasses import dataclass
from typing import Any, Optional, List, Dict, Union, Set

from sqlalchemy.sql import ClauseElement, ColumnCollection

from dropland.blocks.sql.base import SqlStorageType
from .cache import MethodCache
from .model import Model, CreateSchemaType, UpdateSchemaType
from .serializable import SerializableModel


@dataclass
class SqlTableInfo:
    db_type: SqlStorageType
    is_async: bool


class SqlModel(Model):
    @classmethod
    def get_table_info(cls) -> SqlTableInfo:
        ...

    @classmethod
    @contextlib.contextmanager
    def _session_context(cls, begin_tx: bool = False, autocommit: bool = False, session=None):
        ...

    @classmethod
    @contextlib.asynccontextmanager
    async def _async_session_context(
            cls, begin_tx: bool = False, autocommit: bool = False, session=None):
        ...

    @classmethod
    def query_for_select(cls, include_rela: Optional[Set[str]] = None,
                         exclude_rela: Optional[Set[str]] = None, **kwargs):
        ...

    @classmethod
    def query_for_update(cls, **kwargs):
        ...

    @classmethod
    def query_for_delete(cls, **kwargs):
        ...

    @classmethod
    def get_columns(cls) -> ColumnCollection:
        ...

    @classmethod
    def get_relationships(cls) -> Dict[str, Any]:
        ...

    @classmethod
    def query_options(cls, include: Optional[Set[str]] = None, exclude: Optional[Set[str]] = None):
        ...

    @classmethod
    def prepare_for_create(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        return data

    @classmethod
    def prepare_for_update(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        return data

    @classmethod
    def prepare_for_delete(cls, obj: 'SqlModel') -> 'SqlModel':
        return obj

    #
    # Retrieve operations
    #

    @classmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['SqlModel']:
        ...

    @classmethod
    async def get_any(cls, indices: List[Any], **kwargs) -> List[Optional['SqlModel']]:
        ...

    @classmethod
    async def list(
        cls, filters: Optional[List[Any]] = None, sorting: Optional[List[Any]] = None,
            skip: int = 0, limit: int = 0, params: Dict[str, Any] = None, **kwargs) -> List['SqlModel']:
        ...

    @classmethod
    async def count(cls, filters: Optional[List[Any]] = None, params: Dict[str, Any] = None, **kwargs) -> int:
        ...

    @classmethod
    async def exists(cls, id_value: Any, **kwargs) -> bool:
        ...

    @classmethod
    async def exists_by(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs) -> bool:
        ...

    #
    # Modification operations
    #

    @classmethod
    async def create(cls, data: Union[CreateSchemaType, Dict[str, Any]], **kwargs) -> Optional['SqlModel']:
        ...

    async def update(self, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        ...

    @classmethod
    async def update_by_id(cls, id_value: Any, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        ...

    @classmethod
    async def update_by(cls, filters: List[Any],
                        data: Union[UpdateSchemaType, Dict[str, Any]],
                        /, params: Dict[str, Any] = None, **kwargs) -> int:
        ...

    async def save(self, updated_fields: List[str] = None, **kwargs) -> bool:
        ...

    async def load(self, field_names: List[str] = None) -> bool:
        ...

    @classmethod
    async def save_all(cls, objects: List['SqlModel'], *args, **kwargs) -> bool:
        ...

    async def delete(self) -> bool:
        ...

    @classmethod
    async def delete_all(cls, indices: List[Any] = None) -> bool:
        ...

    @classmethod
    async def delete_by_id(cls, id_value: Any) -> bool:
        ...

    @classmethod
    async def delete_by(cls, filters: List[Any], /, params: Dict[str, Any] = None, **kwargs) -> int:
        ...

    #
    # Query operations
    #

    @classmethod
    def query_get(cls, id_value: Any, query=None, **kwargs):
        ...

    @classmethod
    def query_any(cls, indices: List[Any], query=None, **kwargs):
        ...

    @classmethod
    def query_list(cls, filters: List[Any], sorting: List[Any],
                   skip: int = 0, limit: int = 0, params: Dict[str, Any] = None, **kwargs):
        ...

    @classmethod
    def query_count(cls, filters: Optional[List[Any]] = None, params: Dict[str, Any] = None, **kwargs):
        ...

    @classmethod
    def query_exists(cls, id_value: Any, **kwargs):
        ...

    @classmethod
    def query_exists_by(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        ...

    @classmethod
    def query_update(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        ...

    @classmethod
    def query_delete(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs):
        ...


# noinspection PyProtectedMember
class CachedSqlModel(SqlModel, SerializableModel):
    class Meta(SqlModel.Meta):
        caches: List[MethodCache]

    @classmethod
    def has_cache(cls):
        return len(cls.Meta.caches) > 0

    #
    # Retrieve operations
    #

    @classmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['CachedSqlModel']:
        if kwargs.get('no_cache', False):
            return await super().get(id_value, **kwargs)

        exists: bool = False
        instance: Optional[CachedSqlModel] = None
        method_cache_key = MethodCache.cache_key_for('get', {'id': id_value, 'kw': kwargs})

        for cache in cls.Meta.caches:
            exists, data = await cache.get('get', cache_key=method_cache_key)
            if exists:
                if instance := cls._construct(data, **kwargs):
                    break

        if exists:
            async with cls._async_session_context() as ctx:
                await cls._register_instances(ctx, [instance])
                return await cls._build_rela(ctx, instance, **kwargs)

        # noinspection PyTypeChecker
        result = await super().get(id_value, no_cache=True, **kwargs)  # type: Optional[CachedSqlModel]
        serializable = result.get_serializable_values() if result is not None else None

        for cache in cls.Meta.caches:
            await cache.put('get', cache_key=method_cache_key, data=serializable)
        return result

    @classmethod
    async def get_any(cls, indices: List[Any], **kwargs) -> List[Optional['CachedSqlModel']]:
        if kwargs.get('no_cache', False):
            return await super().get_any(indices, **kwargs)

        exists: bool = False
        objects: Optional[List[CachedSqlModel]] = None
        method_cache_key = MethodCache.cache_key_for('get_any', {'indices': indices, 'kw': kwargs})

        for cache in cls.Meta.caches:
            exists, data = await cache.get('get_any', cache_key=method_cache_key)
            if exists:
                # noinspection PyTypeChecker
                if objects := cls._construct_list(data, **kwargs):
                    break

        if exists:
            async with cls._async_session_context() as ctx:
                await cls._register_instances(ctx, objects)
                # noinspection PyTypeChecker
                return await cls._build_rela_list(ctx, objects, **kwargs)

        # noinspection PyTypeChecker
        result = await super().get_any(indices, no_cache=True, **kwargs)  # type: List[Optional[CachedSqlModel]]
        serializable = [i.get_serializable_values() if i is not None else None for i in result]

        for cache in cls.Meta.caches:
            await cache.put('get_any', cache_key=method_cache_key, data=serializable)
        return result

    @classmethod
    async def list(
        cls, filters: Optional[List[Any]] = None, sorting: Optional[List[Any]] = None,
            skip: int = 0, limit: int = 0, params: Dict[str, Any] = None, **kwargs) -> List['CachedSqlModel']:
        if kwargs.get('no_cache', False):
            # noinspection PyTypeChecker
            return await super().list(filters, sorting, skip, limit, params, **kwargs)

        exists: bool = False
        objects: Optional[List[CachedSqlModel]] = None
        method_cache_key = MethodCache.cache_key_for('list', {
            'filters': cls._expr2string(filters, params),
            'sorting': cls._expr2string(sorting),
            'skip': skip, 'limit': limit, 'kw': kwargs
        })

        for cache in cls.Meta.caches:
            exists, data = await cache.get('list', cache_key=method_cache_key)
            if exists:
                # noinspection PyTypeChecker
                if objects := cls._construct_list(data, **kwargs):
                    break

        if exists:
            async with cls._async_session_context() as ctx:
                await cls._register_instances(ctx, objects)
                # noinspection PyTypeChecker
                return await cls._build_rela_list(ctx, objects, **kwargs)

        # noinspection PyTypeChecker
        result = await super().list(filters, sorting, skip, limit, params, no_cache=True, **kwargs)  # type: List['CachedSqlModel']
        serializable = [i.get_serializable_values() for i in result]

        for cache in cls.Meta.caches:
            await cache.put('list', cache_key=method_cache_key, data=serializable)
        return result

    @classmethod
    async def count(cls, filters: Optional[List[Any]] = None, params: Dict[str, Any] = None, **kwargs) -> int:
        if kwargs.get('no_cache', False):
            return await super().count(filters, params, **kwargs)

        method_cache_key = MethodCache.cache_key_for('count', {
            'filters': cls._expr2string(filters, params), 'kw': kwargs
        })

        for cache in cls.Meta.caches:
            exists, data = await cache.get('count', cache_key=method_cache_key)
            if exists:
                return data

        result = await super().count(filters, params, no_cache=True, **kwargs)

        for cache in cls.Meta.caches:
            await cache.put('count', cache_key=method_cache_key, data=result)
        return result

    @classmethod
    async def exists(cls, id_value: Any, **kwargs) -> bool:
        if kwargs.get('no_cache', False):
            return await super().exists(id_value, **kwargs)

        method_cache_key = MethodCache.cache_key_for('exists', {'id': id_value, 'kw': kwargs})

        for cache in cls.Meta.caches:
            exists, data = await cache.get('exists', cache_key=method_cache_key)
            if exists:
                return data

        result = await super().exists(id_value, no_cache=True, **kwargs)

        for cache in cls.Meta.caches:
            await cache.put('exists', cache_key=method_cache_key, data=result)
        return result

    @classmethod
    async def exists_by(cls, filters: List[Any], params: Dict[str, Any] = None, **kwargs) -> bool:
        if kwargs.get('no_cache', False):
            return await super().exists_by(filters, params, **kwargs)

        method_cache_key = MethodCache.cache_key_for('exists_by', {
            'filters': cls._expr2string(filters, params), 'kw': kwargs
        })

        for cache in cls.Meta.caches:
            exists, data = await cache.get('exists_by', cache_key=method_cache_key)
            if exists:
                return data

        result = await super().exists_by(filters, params, no_cache=True, **kwargs)

        for cache in cls.Meta.caches:
            await cache.put('exists_by', cache_key=method_cache_key, data=result)
        return result

    #
    # Modification operations
    #

    @classmethod
    async def create(cls, data: Union[CreateSchemaType, Dict[str, Any]], **kwargs) -> Optional['SqlModel']:
        if result := await super().create(data, **kwargs):
            await cls._drop_methods()
        return result

    async def update(self, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        if result := await super().update(data):
            await self._drop_methods(['get', 'get_any', 'list'])
        return result

    @classmethod
    async def update_by_id(cls, id_value: Any, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        if result := await super().update_by_id(id_value, data):
            await cls._drop_methods(['get', 'get_any', 'list'])
        return result

    @classmethod
    async def update_by(cls, filters: List[Any],
                        data: Union[UpdateSchemaType, Dict[str, Any]],
                        /, params: Dict[str, Any] = None, **kwargs) -> int:
        if result := await super().update_by(filters, data, params=params, **kwargs):
            await cls._drop_methods(['get', 'get_any', 'list'])
        return result

    async def delete(self) -> bool:
        if result := await super().delete():
            await self._drop_methods()
        return result

    @classmethod
    async def delete_all(cls, indices: List[Any] = None) -> bool:
        if result := await super().delete_all(indices):
            await cls._drop_methods()
        return result

    @classmethod
    async def delete_by_id(cls, id_value: Any) -> bool:
        if result := await super().delete_by_id(id_value):
            await cls._drop_methods()
        return result

    @classmethod
    async def delete_by(cls, filters: List[Any], /, params: Dict[str, Any] = None, **kwargs) -> int:
        if result := await super().delete_by(filters, params=params, **kwargs):
            await cls._drop_methods()
        return result

    async def save(self, updated_fields: List[str] = None, **kwargs) -> bool:
        if result := await super().save(updated_fields, **kwargs):
            await self._drop_methods(['get', 'get_any', 'list'])
        return result

    async def load(self, field_names: List[str] = None) -> bool:
        if result := await super().load(field_names):
            await self._drop_methods(['get', 'get_any', 'list'])
        return result

    @classmethod
    async def save_all(cls, objects: List['SqlModel'], *args, **kwargs) -> bool:
        if result := await super().save_all(objects, *args, **kwargs):
            await cls._drop_methods()
        return result

    #
    # Private
    #

    @classmethod
    async def _drop_methods(cls, methods: List[str] = None):
        method_names = ('get', 'get_any', 'list', 'count', 'exists', 'exists_by')
        methods = set(methods) if methods else set(method_names)

        await asyncio.gather(
            *(cache.drop_all([m for m in method_names if m in methods]) for cache in cls.Meta.caches)
        )

    @classmethod
    def _expr2string(cls, expr, params: dict = None):
        if expr is None:
            return None
        elif isinstance(expr, list):
            res = [cls._expr2string(i, params) for i in expr]
            return ','.join(res)
        elif isinstance(expr, ClauseElement):
            if params:
                expr = expr.params(params)
            compiled = expr.compile(compile_kwargs={'render_postcompile': True})
            res = [compiled.string]
            for k, v in compiled.params.items():
                if params and k in params:
                    res.append(str(params[k]))
                else:
                    res.append(str(v))
            return '$'.join(res)

        return str(expr)
