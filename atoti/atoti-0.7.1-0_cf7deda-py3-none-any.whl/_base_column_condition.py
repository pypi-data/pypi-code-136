from __future__ import annotations

from abc import abstractmethod
from typing import Any, List, Literal, NoReturn, Tuple

from atoti_core import BitwiseOperatorsOnly, ComparisonOperator, DataType

ColumnName = str
Value = Any
ColumnConditionCoordinates = Tuple[
    ColumnName, Value, Literal[ComparisonOperator, "isin"], DataType
]


class BaseColumnCondition(BitwiseOperatorsOnly):
    @abstractmethod
    def __and__(self, other: BaseColumnCondition) -> BaseColumnCondition:
        ...

    @abstractmethod
    def __or__(self, other: BaseColumnCondition) -> BaseColumnCondition:
        ...

    def __xor__(self, other: BaseColumnCondition) -> NoReturn:
        raise NotImplementedError("XOR conditions are not supported.")

    @property
    @abstractmethod
    def _table_name(self) -> str:
        ...

    def _check_same_table(self, other: BaseColumnCondition) -> None:
        if self._table_name != other._table_name:
            raise ValueError(
                f"Cannot mix conditions on different tables. This one is on `{self._table_name}` but the other is on `{other._table_name}`."
            )

    @abstractmethod
    def _to_coordinates(self) -> List[List[ColumnConditionCoordinates]]:
        """Return flattened conditions.

        `(c_1 & c_2) | c_3` is equivalent to `[[c_1, c_2], [c_3]]`.
        """
