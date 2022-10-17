from abc import abstractmethod
from typing import (Any, Protocol)

class IExports(Protocol):
    @abstractmethod
    def dumps(self, obj: Any) -> str:
        ...

    @abstractmethod
    def loads(self, __arg0: str) -> Any:
        ...


