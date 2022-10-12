from collections import defaultdict
from typing import Protocol, List, Any, Optional

from .base import ModelProtocol
from ..context import ContextData


class ModelLocalCacheMixin(Protocol):
    @classmethod
    def _add_to_local_cache(cls, ctx: ContextData, instances: List[ModelProtocol]):
        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))
        for instance in instances:
            if instance is not None:
                ctx.cache[cls][instance.get_id_value()] = instance

    @classmethod
    def _get_from_local_cache(cls, ctx: ContextData, indices: List[Any]) -> List[Optional[ModelProtocol]]:
        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))

        return [ctx.cache[cls].get(id_value) for id_value in indices]

    @classmethod
    def _drop_from_local_cache(cls, ctx: ContextData, indices: List[Any] = None) -> List[bool]:
        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))

        if indices is None:
            ctx.cache[cls] = defaultdict(dict)
            return [True]

        return [ctx.cache[cls].pop(id_value, None) is None for id_value in indices]

    @classmethod
    def _has_in_local_cache(cls, ctx: ContextData, indices: List[Any]) -> List[bool]:
        if not hasattr(ctx, 'cache'):
            ctx.cache = defaultdict(lambda: defaultdict(dict))

        return [id_value in ctx.cache[cls] for id_value in indices]

    # noinspection PyProtectedMember
    @classmethod
    async def _register_instances(cls, ctx: ContextData, objects: List[ModelProtocol]):
        await super()._register_instances(ctx, objects)
        cls._add_to_local_cache(ctx, objects)

    # noinspection PyProtectedMember
    @classmethod
    async def _unregister_indices(cls, ctx: ContextData, indices: List[Any] = None):
        cls._drop_from_local_cache(ctx, indices)
        await super()._unregister_indices(ctx, indices)
