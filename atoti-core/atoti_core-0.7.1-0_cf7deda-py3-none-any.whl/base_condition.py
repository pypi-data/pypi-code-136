from __future__ import annotations

from abc import abstractmethod
from typing import NoReturn

from .bitwise_operators_only import BitwiseOperatorsOnly


class BaseCondition(BitwiseOperatorsOnly):
    @abstractmethod
    def __and__(self, other: BaseCondition) -> BaseCondition:
        ...

    def __xor__(self, other: BaseCondition) -> NoReturn:
        raise NotImplementedError("XOR conditions are not supported.")
