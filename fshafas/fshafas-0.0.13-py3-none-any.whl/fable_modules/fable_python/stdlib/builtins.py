from __future__ import annotations
from abc import abstractmethod
import builtins
from typing import (Protocol, Any, TypeVar, Optional)
from ...fable_library.list import FSharpList
from ...fable_library.util import (IEnumerable_1, IDisposable)

__A = TypeVar("__A")

class TextIOBase(Protocol):
    @abstractmethod
    def readline(self, __size: int) -> str:
        ...

    @abstractmethod
    def readlines(self, __hint: int) -> FSharpList[str]:
        ...

    @abstractmethod
    def tell(self) -> int:
        ...

    @abstractmethod
    def write(self, __s: str) -> int:
        ...

    @abstractmethod
    def writelines(self, __lines: IEnumerable_1[str]) -> None:
        ...


class TextIOWrapper(TextIOBase, IDisposable):
    pass

class IExports(Protocol):
    @abstractmethod
    def chr(self, __arg0: int) -> str:
        ...

    @abstractmethod
    def float(self, __arg0: Any) -> float:
        ...

    @abstractmethod
    def id(self, __arg0: Any) -> int:
        ...

    @abstractmethod
    def int(self, __arg0: Any) -> int:
        ...

    @abstractmethod
    def len(self, __arg0: Any) -> int:
        ...

    @abstractmethod
    def ord(self, __arg0: str) -> int:
        ...

    @abstractmethod
    def print(self, obj: Any) -> None:
        ...

    @abstractmethod
    def str(self, __arg0: Any) -> str:
        ...


def print(obj: Optional[Any]=None) -> None:
    builtins.print(obj)


__all__ = ["print"]

