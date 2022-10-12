from __future__ import annotations

from dataclasses import dataclass
from itertools import chain, product
from typing import List, Tuple

from atoti_core import BooleanOperator, keyword_only_dataclass

from ._base_column_condition import BaseColumnCondition, ColumnConditionCoordinates


def _flatten_condition(
    column_condition: BaseColumnCondition,
    output: List[List[ColumnConditionCoordinates]],
    /,
) -> List[List[ColumnConditionCoordinates]]:
    """Flatten multicondition in a list of list of column condition coordinates.

    `(c_1 & c_2) | c_3` is equivalent to `[[c_1, c_2], [c_3]]`.
    """
    if isinstance(column_condition, ColumnMultiCondition):
        if column_condition.operator == "and":
            output = [
                list(chain(*t))
                for t in product(
                    _flatten_condition(column_condition.conditions[0], output),
                    _flatten_condition(column_condition.conditions[1], output),
                )
            ]
            return output
        output = _flatten_condition(
            column_condition.conditions[0], output
        ) + _flatten_condition(column_condition.conditions[1], output)
        return output
    return column_condition._to_coordinates()


@keyword_only_dataclass
@dataclass(frozen=True)
class ColumnMultiCondition(BaseColumnCondition):

    conditions: Tuple[BaseColumnCondition, BaseColumnCondition]
    operator: BooleanOperator

    def __and__(self, other: BaseColumnCondition) -> ColumnMultiCondition:
        self._check_same_table(other)
        return ColumnMultiCondition(conditions=(self, other), operator="and")

    def __or__(self, other: BaseColumnCondition) -> ColumnMultiCondition:
        self._check_same_table(other)
        return ColumnMultiCondition(conditions=(self, other), operator="or")

    @property
    def _table_name(self) -> str:
        return next(iter(self.conditions))._table_name

    def _to_coordinates(self) -> List[List[ColumnConditionCoordinates]]:
        return _flatten_condition(self, [])
