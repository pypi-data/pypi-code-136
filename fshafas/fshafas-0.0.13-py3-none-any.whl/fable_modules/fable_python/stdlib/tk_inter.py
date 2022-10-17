from __future__ import annotations
from abc import abstractmethod
from typing import (Protocol, Callable, Optional)

class Event(Protocol):
    @property
    @abstractmethod
    def x(self) -> int:
        ...

    @property
    @abstractmethod
    def y(self) -> int:
        ...


class Misc(Protocol):
    @abstractmethod
    def bind(self, sequence: str, func: Callable[[Event], None]) -> Optional[str]:
        ...


class Wm(Protocol):
    pass

