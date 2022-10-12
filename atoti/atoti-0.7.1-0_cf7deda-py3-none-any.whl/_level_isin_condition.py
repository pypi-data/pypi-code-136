from __future__ import annotations

from dataclasses import dataclass

from atoti_core import BaseLevelIsinCondition, keyword_only_dataclass

from ._level_condition import LevelCondition
from ._measures.boolean_measure import BooleanMeasure
from ._single_condition import SingleCondition
from .measure_description import MeasureDescription


@keyword_only_dataclass
@dataclass(frozen=True)
class LevelIsinCondition(SingleCondition, BaseLevelIsinCondition):
    @property
    def _measure_description(self) -> MeasureDescription:

        if len(self.members) == 1:
            return LevelCondition(
                level_coordinates=self.level_coordinates,
                operator="eq",
                value=self.members[0].value,
            )._measure_description

        return BooleanMeasure(
            "or",
            tuple(
                LevelCondition(
                    level_coordinates=self.level_coordinates,
                    operator="eq",
                    value=member.value,
                )._measure_description
                for member in self.members
            ),
        )
