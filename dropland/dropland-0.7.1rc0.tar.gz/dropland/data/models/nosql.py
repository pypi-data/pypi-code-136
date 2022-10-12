import contextlib
from datetime import timedelta
from typing import Optional, Any, Tuple, List, Union, Dict

from .model import Model, CreateSchemaType, UpdateSchemaType
from .serializable import SerializableModel
from ..cache import ModelCacheProtocol, ModelCacheData
from ..serializers import Serializer, Deserializer


class NoSqlModel(Model, SerializableModel):
    class Meta(Model.Meta):
        cache_protocol: ModelCacheProtocol

    def __init_subclass__(
            cls, cache_protocol: Optional[ModelCacheProtocol] = None,
            serializer: Optional[Serializer] = None,
            deserializer: Optional[Deserializer] = None,
            **kwargs):
        super().__init_subclass__(serializer, deserializer, **kwargs)
        cls.Meta.cache_protocol = cache_protocol

    @classmethod
    def get_model_cache_key(cls) -> str:
        return cls.Meta.cache_protocol.get_model_cache_key()

    @classmethod
    def get_cache_id(cls, id_value: Any) -> str:
        return cls.Meta.cache_protocol.get_cache_id(id_value)

    @classmethod
    def get_cache_key(cls, id_value: Any) -> str:
        return cls.Meta.cache_protocol.get_cache_key(id_value)

    @classmethod
    @contextlib.asynccontextmanager
    async def _async_session_context(cls, session=None):
        ...

    #
    # Retrieve operations
    #

    @classmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['NoSqlModel']:
        no_cache = kwargs.pop('no_cache', False)
        async with cls._async_session_context() as ctx:
            if not no_cache:
                if instance := cls._get_from_local_cache(ctx, [id_value])[0]:
                    return instance
            exists, data = await cls.Meta.cache_protocol.load_one(
                ctx, cls.get_cache_key(id_value), **kwargs)
            if exists:
                if instance := cls._construct(data, **kwargs):
                    await cls._register_instances(ctx, [instance])
                    return await cls._build_rela(ctx, instance, **kwargs)
        return None

    @classmethod
    async def get_any(cls, indices: List[Any], **kwargs) -> List[Optional['NoSqlModel']]:
        no_cache = kwargs.pop('no_cache', False)
        async with cls._async_session_context() as ctx:
            if not no_cache:
                objects = cls._get_from_local_cache(ctx, indices)
            else:
                objects = [None] * len(indices)
            non_cached_indices = [i for o, i in zip(objects, indices) if o is None]
            if non_cached_indices:
                data = await cls.Meta.cache_protocol.load_many(ctx, non_cached_indices, **kwargs)
                if non_cached := cls._construct_list(data, **kwargs):
                    await cls._register_instances(ctx, non_cached)
                    objects += await cls._build_rela_list(ctx, non_cached, **kwargs)

        objects = {obj.get_id_value(): obj for obj in objects if obj is not None}
        return [objects[id_value] if id_value in objects else None for id_value in indices]

    @classmethod
    async def exists(cls, id_value: Any, no_cache: bool = False) -> bool:
        async with cls._async_session_context() as ctx:
            if not no_cache and cls._has_in_local_cache(ctx, [id_value])[0]:
                return True
            return await cls.Meta.cache_protocol.exists(ctx, cls.get_cache_key(id_value))

    @classmethod
    async def scan(cls, match: str, count: int = None, **kwargs) -> Tuple[str, Optional['NoSqlModel']]:
        async with cls._async_session_context() as ctx:
            async for k, data in cls.Meta.cache_protocol.scan(ctx, cls.get_model_cache_key(), match, count):
                if data is None:
                    yield k, None
                elif instance := cls._construct(data, **kwargs):
                    await cls._register_instances(ctx, [instance])
                    yield k, await cls._build_rela(ctx, instance, **kwargs)
                else:
                    yield k, None

    #
    # Modification operations
    #

    @classmethod
    async def create(cls, data: Union[CreateSchemaType, Dict[str, Any]], **kwargs) -> Optional['NoSqlModel']:
        if isinstance(data, dict):
            create_data = data
        else:
            create_data = data.dict(exclude_unset=True)

        instance = cls._construct(create_data)
        await instance.save()
        return instance

    async def update(self, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        instance = self._construct(update_data, instance=self)
        return await instance.save()

    @classmethod
    async def update_by_id(cls, id_value: Any, data: Union[UpdateSchemaType, Dict[str, Any]]) -> bool:
        if isinstance(data, dict):
            update_data = data
        else:
            update_data = data.dict(exclude_unset=True)

        async with cls._async_session_context() as ctx:
            data = ModelCacheData(cache_id=cls.get_cache_id(id_value), data=update_data)
            return await cls.Meta.cache_protocol.cache_one(ctx, data)

    async def save(self, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        async with self.__class__._async_session_context() as ctx:
            if not ttl:
                await self._register_instances(ctx, [self])
            data = ModelCacheData(cache_id=self.get_cache_id(self.get_id_value()), data=self.get_serializable_values())
            return await self.Meta.cache_protocol.cache_one(ctx, data, ttl=ttl, **kwargs)

    async def load(self, field_names: List[str] = None) -> bool:
        field_names = set(field_names) if field_names else set()

        async with self.__class__._async_session_context() as ctx:
            exists, data = await self.Meta.cache_protocol.load_one(ctx, self.get_cache_key(self.get_id_value()))
            if exists:
                self._construct(data, self, field_names)
                await self._build_rela(ctx, self, load_fields=field_names)
                return True
        return False

    @classmethod
    async def save_all(cls, objects: List['NoSqlModel'],
                       ttl: Optional[timedelta] = None, **kwargs) -> bool:
        async with cls._async_session_context() as ctx:
            objects_data = [
                ModelCacheData(cache_id=cls.get_cache_id(o.get_id_value()), data=o.get_serializable_values())
                for o in objects
            ]
            if res := await cls.Meta.cache_protocol.cache_many(ctx, objects_data, ttl, **kwargs):
                if not ttl:
                    await cls._register_instances(ctx, objects)
            return res

    async def delete(self) -> bool:
        async with self.__class__._async_session_context() as ctx:
            id_value = self.get_id_value()
            await self._unregister_indices(ctx, [id_value])
            return await self.Meta.cache_protocol.drop_one(ctx, self.get_cache_key(id_value))

    @classmethod
    async def delete_all(cls, indices: List[Any] = None) -> bool:
        async with cls._async_session_context() as ctx:
            await cls._unregister_indices(ctx, indices)
            res = await cls.Meta.cache_protocol.drop_many(ctx, indices)
            return res > 0

    @classmethod
    async def delete_by_id(cls, id_value: Any) -> bool:
        async with cls._async_session_context() as ctx:
            await cls._unregister_indices(ctx, [id_value])
            return await cls.Meta.cache_protocol.drop_one(ctx, cls.get_cache_key(id_value))


class NoSqlProxyModel(NoSqlModel):
    class Meta(NoSqlModel.Meta):
        sql_model: Model
        ttl_enabled: bool = False

    @classmethod
    def _fields_cache_key(cls):
        return cls.Meta.sql_model._fields_cache_key()

    @classmethod
    def get_cache_key(cls, id_value: Any) -> str:
        return f'{cls.get_model_cache_key()}:{cls.get_cache_id(id_value)}'

    #
    # Retrieve operations
    #

    @classmethod
    async def get(cls, id_value: Any, **kwargs) -> Optional['NoSqlProxyModel']:
        if not kwargs.pop('no_cache', False):
            if instance := await super().get(id_value, **kwargs):
                return instance
        instance = await cls.Meta.sql_model.get(id_value, **kwargs)
        if instance:
            instance = cls._construct(instance.get_values())
            await super(NoSqlProxyModel, instance).save(**kwargs)
        return instance

    @classmethod
    async def get_any(cls, indices: List[Any], **kwargs) -> List[Optional['NoSqlProxyModel']]:
        if not kwargs.pop('no_cache', False):
            if objects := await super().get_any(indices, **kwargs):
                return objects
        objects = await cls.Meta.sql_model.get_any(indices, **kwargs)
        if objects:
            objects = [cls._construct(o.get_values()) for o in objects]
            await super().save_all(objects, **kwargs)
        return objects

    @classmethod
    async def exists(cls, id_value: Any, **kwargs) -> bool:
        if not kwargs.pop('no_cache', False):
            return await super().exists(id_value, **kwargs)
        return await cls.Meta.sql_model.exists(id_value, **kwargs)

    #
    # Modification operations
    #

    async def save(self, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        if res := await super().save(ttl, **kwargs):
            sql_instance = self.Meta.sql_model._construct(self.get_values())
            await sql_instance.save(**kwargs)
        return res

    async def load(self, field_names: List[str] = None) -> bool:
        if res := await super().load(field_names):
            return res
        sql_instance = self.Meta.sql_model._construct(self.get_values())
        if res := await sql_instance.load(field_names):
            self._construct(sql_instance.get_values(), instance=self)
        return res

    @classmethod
    async def save_all(cls, objects: List['NoSqlProxyModel'],
                       ttl: Optional[timedelta] = None, **kwargs) -> bool:
        if res := await super().save_all(objects):
            sql_objects = [cls.Meta.sql_model._construct(o.get_values()) for o in objects]
            return await cls.Meta.sql_model.save_all(sql_objects, ttl, **kwargs)
        return res

    async def delete(self) -> bool:
        if res := await super().delete():
            return await self.Meta.sql_model.delete_by_id(self.get_id_value())
        return res

    @classmethod
    async def delete_all(cls, indices: List[Any] = None) -> bool:
        if res := await super().delete_all(indices):
            return await cls.Meta.sql_model.delete_all(indices)
        return res
