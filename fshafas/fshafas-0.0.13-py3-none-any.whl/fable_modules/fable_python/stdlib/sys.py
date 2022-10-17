from __future__ import annotations
from abc import abstractmethod
from typing import Protocol
from ...fable_library.types import Array

class VersionInfo(Protocol):
    @property
    @abstractmethod
    def major(self) -> int:
        ...

    @property
    @abstractmethod
    def micro(self) -> int:
        ...

    @property
    @abstractmethod
    def minor(self) -> int:
        ...

    @property
    @abstractmethod
    def releaselevel(self) -> str:
        ...

    @property
    @abstractmethod
    def serial(self) -> int:
        ...


class IExports(Protocol):
    @property
    @abstractmethod
    def argv(self) -> Array[str]:
        ...

    @property
    @abstractmethod
    def byteorder(self) -> str:
        ...

    @property
    @abstractmethod
    def hexversion(self) -> int:
        ...

    @property
    @abstractmethod
    def maxsize(self) -> int:
        ...

    @property
    @abstractmethod
    def maxunicode(self) -> int:
        ...

    @property
    @abstractmethod
    def path(self) -> Array[str]:
        ...

    @property
    @abstractmethod
    def platform(self) -> str:
        ...

    @property
    @abstractmethod
    def prefix(self) -> str:
        ...

    @property
    @abstractmethod
    def version(self) -> str:
        ...

    @property
    @abstractmethod
    def version_info(self) -> VersionInfo:
        ...


