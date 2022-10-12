from __future__ import annotations

from abc import ABC
from typing import Any, NoReturn, Optional
from uuid import uuid4


class BitwiseOperatorsOnly(ABC):
    """To avoid unexpected behavior, instances of this class cannot be auto cast to a boolean.

    Instead, they can be combined using `==`, `!=`, or other bitwise operators.
    """

    @property
    def _bool_auto_cast_error_message(self) -> str:
        message = f"A {self.__class__.__name__} cannot be cast to a boolean."
        alternative_message = self._bool_alternative_message

        if alternative_message is None:
            return message

        return f"{message} {alternative_message}"

    @property
    def _bool_alternative_message(self) -> Optional[str]:  # pylint: disable=no-self-use
        return None

    def __eq__(self, other: Any) -> Any:
        if not isinstance(other, self.__class__):
            return False
        raise TypeError("Instances of this class cannot be compared together.")

    def __ne__(self, other: Any) -> Any:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return hash(uuid4())

    def __bool__(self) -> NoReturn:
        raise TypeError(self._bool_auto_cast_error_message)
