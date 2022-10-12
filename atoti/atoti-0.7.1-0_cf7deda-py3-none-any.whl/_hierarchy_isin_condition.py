from __future__ import annotations

from dataclasses import dataclass

from atoti_core import (
    BaseHierarchyIsinCondition,
    LevelCoordinates,
    keyword_only_dataclass,
)

from ._level_condition import LevelCondition
from ._single_condition import SingleCondition
from .measure_description import MeasureDescription


@keyword_only_dataclass
@dataclass(frozen=True)
class HierarchyIsinCondition(SingleCondition, BaseHierarchyIsinCondition):
    @property
    def _measure_description(self) -> MeasureDescription:
        from ._measures.boolean_measure import (  # pylint:disable=nested-import
            BooleanMeasure,
        )

        operands = []

        for member_path in self.member_paths:
            condition = None
            for level_name, member in zip(self.level_names, member_path):
                level_coordinates = LevelCoordinates(
                    self.hierarchy_coordinates.dimension_name,
                    self.hierarchy_coordinates.hierarchy_name,
                    level_name,
                )

                if condition is not None:
                    condition = condition & LevelCondition(
                        level_coordinates=level_coordinates,
                        operator="eq",
                        value=member.value,
                    )
                else:
                    condition = LevelCondition(
                        level_coordinates=level_coordinates,
                        operator="eq",
                        value=member.value,
                    )

            if condition is not None:
                operands.append(condition._measure_description)

        if len(operands) == 1:
            return operands[0]

        return BooleanMeasure("or", (*operands,))
