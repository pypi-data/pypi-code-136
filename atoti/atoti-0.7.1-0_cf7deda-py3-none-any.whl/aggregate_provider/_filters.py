from typing import Dict, Mapping, Optional, Tuple

from atoti_core import BaseCondition, Constant, LevelCoordinates

from .._condition import Condition
from .._level_condition import LevelCondition
from .._level_isin_condition import LevelIsinCondition
from .._multi_condition import MultiCondition

FilterValues = Tuple[Constant, ...]
Filters = Mapping[LevelCoordinates, FilterValues]


def to_java_filters(condition: BaseCondition, /) -> Filters:
    if isinstance(condition, LevelCondition):
        if condition.operator != "eq":
            raise ValueError(
                f"Expected condition operator to be `eq` but got `{condition.operator}`."
            )
        return {condition.level_coordinates: (Constant(condition.value),)}
    if isinstance(condition, LevelIsinCondition):
        return {condition.level_coordinates: condition.members}
    if isinstance(condition, MultiCondition):
        result: Dict[LevelCoordinates, FilterValues] = {}
        for single_condition in condition.conditions:
            result.update(to_java_filters(single_condition))
        return result
    raise TypeError(f"Expected condition on level but got a `{type(condition)}`.")


def _to_python_condition(
    *, level_coordinates: LevelCoordinates, values: FilterValues
) -> Condition:
    if len(values) == 1:
        return LevelCondition(
            level_coordinates=level_coordinates,
            operator="eq",
            value=values[0].value,
        )
    return LevelIsinCondition(
        level_coordinates=level_coordinates,
        members=values,
    )


def to_python_condition(filters: Filters, /) -> Optional[Condition]:
    if not filters:
        return None

    filters = dict(filters)
    level_coordinates, values = filters.popitem()
    condition = _to_python_condition(level_coordinates=level_coordinates, values=values)
    for level_coordinates, values in filters.items():
        condition = condition & _to_python_condition(
            level_coordinates=level_coordinates, values=values
        )
    return condition
