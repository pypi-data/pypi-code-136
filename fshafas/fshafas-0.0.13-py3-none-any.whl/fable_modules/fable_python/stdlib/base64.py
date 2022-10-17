from abc import abstractmethod
from typing import (ByteString, Protocol)
from ...fable_library.types import uint8

class IExports(Protocol):
    @abstractmethod
    def b16encode(self, __arg0: ByteString) -> uint8:
        ...

    @abstractmethod
    def b32encode(self, __arg0: ByteString) -> ByteString:
        ...

    @abstractmethod
    def standard_b64encode(self, __arg0: ByteString) -> ByteString:
        ...

    @abstractmethod
    def urlsafe_b64encode(self, __arg0: ByteString) -> ByteString:
        ...


