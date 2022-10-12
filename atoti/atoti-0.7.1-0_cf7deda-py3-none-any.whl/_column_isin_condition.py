from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Literal, Optional, Tuple

from atoti_core import ColumnCoordinates, Constant, DataType, keyword_only_dataclass

from ._base_column_condition import BaseColumnCondition, ColumnConditionCoordinates
from ._column_multi_condition import ColumnMultiCondition


@keyword_only_dataclass
@dataclass(frozen=True)
class ColumnIsinCondition(BaseColumnCondition):
    _column_coordinates: ColumnCoordinates
    _column_data_type: DataType
    _members: Tuple[Optional[Constant], ...]
    _comparison_operator: Literal["isin"] = field(default="isin", init=False)

    def __and__(self, other: BaseColumnCondition) -> ColumnMultiCondition:
        self._check_same_table(other)
        return ColumnMultiCondition(conditions=(self, other), operator="and")

    def __or__(self, other: BaseColumnCondition) -> ColumnMultiCondition:
        self._check_same_table(other)
        return ColumnMultiCondition(conditions=(self, other), operator="or")

    @property
    def _table_name(self) -> str:
        return self._column_coordinates.table_name

    def _to_coordinates(self) -> List[List[ColumnConditionCoordinates]]:
        return [
            [
                (
                    self._column_coordinates.column_name,
                    tuple(
                        None if member is None else member.value
                        for member in self._members
                    ),
                    self._comparison_operator,
                    self._column_data_type,
                )
            ]
        ]
