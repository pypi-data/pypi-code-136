from abc import abstractmethod
from typing import Protocol

class IExports(Protocol):
    @abstractmethod
    def unescape(self, __arg0: str) -> str:
        ...


