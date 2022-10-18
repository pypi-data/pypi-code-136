from abc import ABCMeta
from enum import Enum
from typing import Any, Dict, TypeVar, Generic, Type

from web_foundation.kernel.resource import Resource


class FilesResource(Resource, metaclass=ABCMeta):
    root: Any

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def open(self, path: Any, *args, **kwargs) -> Any:
        raise NotImplementedError

    async def remove(self, path: Any, *args, **kwargs):
        raise NotImplementedError

    async def list(self, path: Any, *args, **kwargs):
        raise NotImplementedError

    async def exists(self, path: Any) -> bool:
        raise NotImplementedError
