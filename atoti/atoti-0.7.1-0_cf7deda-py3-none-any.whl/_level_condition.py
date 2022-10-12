from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from atoti_core import (
    OPERATOR_TO_INVERSE_OPERATOR,
    BaseLevelCondition,
    ComparisonOperator,
    keyword_only_dataclass,
)

from ._measures.boolean_measure import BooleanMeasure
from ._measures.level_measure import LevelMeasure
from ._single_condition import SingleCondition
from ._warn_about_required_levels import warn_about_required_levels
from .measure_description import MeasureDescription, _convert_to_measure_description


@keyword_only_dataclass
@dataclass(frozen=True)
class LevelCondition(SingleCondition, BaseLevelCondition):
    def __invert__(self) -> LevelCondition:
        return LevelCondition(
            level_coordinates=self.level_coordinates,
            operator=OPERATOR_TO_INVERSE_OPERATOR[self.operator],
            value=self.value,
        )

    @property
    def _measure_description(self) -> MeasureDescription:

        lvl_measure = LevelMeasure(self.level_coordinates)

        # Handle comparing to None
        if self.value is None:
            if self.operator not in ["eq", "ne"]:
                raise ValueError(f"Cannot use operation {self.operator} on None.")

            return BooleanMeasure(
                _operator="isNull" if self.operator == "eq" else "notNull",
                _operands=(lvl_measure,),
            )

        warn_about_required_levels(
            origin_scope_levels=f"the level {self.level_coordinates}"
        )

        value_measure = _convert_to_measure_description(self.value)
        switcher: Mapping[ComparisonOperator, MeasureDescription] = {
            "eq": lvl_measure == value_measure,
            "ne": lvl_measure != value_measure,
            "lt": lvl_measure < value_measure,
            "le": lvl_measure <= value_measure,
            "gt": lvl_measure > value_measure,
            "ge": lvl_measure >= value_measure,
        }
        return switcher[self.operator]
