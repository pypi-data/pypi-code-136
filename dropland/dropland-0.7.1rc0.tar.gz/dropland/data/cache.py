from dataclasses import dataclass
from datetime import timedelta
from typing import Protocol, Any, List, Optional, Dict, Tuple, AsyncIterable

from .context import ContextData


@dataclass
class ModelCacheData:
    cache_id: str
    data: Optional[Any] = None


class ModelCacheProtocol(Protocol):
    def get_model_cache_key(self) -> str:
        ...

    def get_cache_id(self, id_value: Any) -> str:
        return str(id_value)

    def get_cache_key(self, id_value: Any) -> str:
        return f'{self.get_model_cache_key()}:{self.get_cache_id(id_value)}'

    async def cache_one(
            self, ctx: ContextData, data: ModelCacheData, ttl: Optional[timedelta] = None, **kwargs) -> bool:
        ...

    async def cache_many(
            self, ctx: ContextData, objects: List[ModelCacheData], ttl: Optional[timedelta] = None, **kwargs) -> bool:
        ...

    async def load_one(
            self, ctx: ContextData, cache_key: str, **kwargs) -> Tuple[bool, Optional[Any]]:
        ...

    async def load_many(
            self, ctx: ContextData, indices: List[Any], **kwargs) -> List[Optional[Dict[str, Any]]]:
        ...

    async def drop_one(self, ctx: ContextData, cache_key: str) -> bool:
        ...

    async def drop_many(self, ctx: ContextData, indices: List[Any] = None) -> int:
        ...

    async def drop_all(self, ctx: ContextData, prefix: Optional[str] = None) -> int:
        ...

    async def exists(self, ctx: ContextData, cache_key: str) -> bool:
        ...

    async def scan(self, ctx: ContextData, cache_key: str = None,
                   match: str = None, count: int = None) -> AsyncIterable[Tuple[str, Optional[Dict[str, Any]]]]:
        ...
