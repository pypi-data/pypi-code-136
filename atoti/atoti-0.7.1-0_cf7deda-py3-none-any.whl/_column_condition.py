from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, List, Mapping

from atoti_core import (
    OPERATOR_TO_INVERSE_OPERATOR,
    ColumnCoordinates,
    ComparisonOperator,
    DataType,
    keyword_only_dataclass,
)

from ._base_column_condition import BaseColumnCondition, ColumnConditionCoordinates
from ._column_multi_condition import ColumnMultiCondition
from ._operation import ColumnOperation, ConditionOperation

_CONDITIONS: Mapping[
    ComparisonOperator, Callable[[ColumnOperation, Any], ConditionOperation]
] = {
    "eq": lambda column_operation, value: column_operation == value,  # type: ignore[no-any-return]
    "ge": lambda column_operation, value: column_operation >= value,  # type: ignore[no-any-return]
    "gt": lambda column_operation, value: column_operation > value,  # type: ignore[no-any-return]
    "le": lambda column_operation, value: column_operation <= value,  # type: ignore[no-any-return]
    "lt": lambda column_operation, value: column_operation < value,  # type: ignore[no-any-return]
    "ne": lambda column_operation, value: column_operation != value,  # type: ignore[no-any-return]
}


@keyword_only_dataclass
@dataclass(frozen=True)
class ColumnCondition(BaseColumnCondition):
    _column_coordinates: ColumnCoordinates
    _column_data_type: DataType
    _value: Any
    _comparison_operator: ComparisonOperator

    def __and__(self, other: BaseColumnCondition) -> ColumnMultiCondition:
        self._check_same_table(other)
        return ColumnMultiCondition(conditions=(self, other), operator="and")

    def __or__(self, other: BaseColumnCondition) -> ColumnMultiCondition:
        self._check_same_table(other)
        return ColumnMultiCondition(conditions=(self, other), operator="or")

    def _to_operation(self) -> ConditionOperation:
        return _CONDITIONS[self._comparison_operator](
            ColumnOperation(self._column_coordinates, self._column_data_type),
            self._value,
        )

    def __invert__(self) -> ColumnCondition:
        return ColumnCondition(
            _column_coordinates=self._column_coordinates,
            _column_data_type=self._column_data_type,
            _value=self._value,
            _comparison_operator=OPERATOR_TO_INVERSE_OPERATOR[
                self._comparison_operator
            ],
        )

    @property
    def _table_name(self) -> str:
        return self._column_coordinates.table_name

    def _to_coordinates(self) -> List[List[ColumnConditionCoordinates]]:
        return [
            [
                (
                    self._column_coordinates.column_name,
                    self._value,
                    self._comparison_operator,
                    self._column_data_type,
                )
            ]
        ]
