from abc import ABC, abstractmethod
from functools import cached_property
from typing import Tuple


class Coordinates(ABC):
    @property
    @abstractmethod
    def key(self) -> Tuple[str, ...]:
        ...

    @cached_property
    def java_description(self) -> str:
        return "@".join(reversed(self.key))

    def __str__(self) -> str:
        return str(self.key)
