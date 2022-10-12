from __future__ import annotations

from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
)

from atoti_core import (
    DataType,
    LevelCoordinates,
    is_boolean_type,
    is_numeric_type,
    is_primitive_type,
    keyword_only_dataclass,
)

from .._condition import Condition
from .._data_type_error import DataTypeError
from .._hierarchy_isin_condition import HierarchyIsinCondition
from .._java_api import JavaApi
from .._level_condition import LevelCondition
from .._level_isin_condition import LevelIsinCondition
from .._py4j_utils import as_java_object, to_java_object_list
from ..level import Level
from ..measure_description import MeasureDescription
from ..type import DataType


def is_object_type(data_type: DataType, /) -> bool:
    return not is_primitive_type(data_type)


TYPE_TO_PREDICATE: Dict[str, Callable[[DataType], bool]] = {
    "numeric": is_numeric_type,
    "boolean": is_boolean_type,
    "object": is_object_type,
}


def _validate_type_compatibility(data_types: Iterable[DataType], /) -> None:
    """
    Ensures that a switch/where measure defining multiple measures selects a measure that is compatible type-wise.
    Two types are compatible if they both have the same type among the following: numeric, boolean or object.
    """
    for data_type_to_validate, predicate in TYPE_TO_PREDICATE.items():
        first_data_type_matched = predicate(next(iter(data_types)))
        for data_type in data_types:
            if first_data_type_matched and not predicate(data_type):
                raise DataTypeError(
                    "The given measures have incompatible types. "
                    + "Ensure that all measures are returning "
                    + data_type_to_validate
                    + " values."
                )


@keyword_only_dataclass
@dataclass(eq=False)
class WhereMeasure(MeasureDescription):
    """A measure that returns the value of other measures based on conditions."""

    _measure_to_conditions: Mapping[MeasureDescription, Tuple[MeasureDescription, ...]]
    _default_measure: Optional[MeasureDescription]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        underlying_measure_to_conditions = {
            measure._distil(
                java_api=java_api, cube_name=cube_name, measure_name=None
            ): conditions
            for measure, conditions in self._measure_to_conditions.items()
        }
        underlying_default_measure = (
            self._default_measure._distil(java_api=java_api, cube_name=cube_name)
            if self._default_measure is not None
            else None
        )
        java_api.publish_measures(cube_name)

        data_types: List[DataType] = [
            java_api.get_measure(underlying_name, cube_name=cube_name).underlying_type
            for underlying_name in underlying_measure_to_conditions
        ]
        if underlying_default_measure is not None:
            data_types.append(
                java_api.get_measure(
                    underlying_default_measure, cube_name=cube_name
                ).underlying_type
            )
        _validate_type_compatibility(data_types)

        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "WHERE",
            {
                measure: [
                    condition._distil(java_api=java_api, cube_name=cube_name)
                    for condition in conditions
                ]
                for measure, conditions in underlying_measure_to_conditions.items()
            },
            underlying_default_measure,
        )
        return distilled_name


@keyword_only_dataclass
@dataclass(eq=False)
class LevelValueFilteredMeasure(MeasureDescription):
    """A measure on a part of the cube filtered on a level value."""

    _underlying_measure: MeasureDescription
    _conditions: Collection[Condition] = ()

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:

        # Distil the underlying measure
        underlying_name = self._underlying_measure._distil(
            java_api=java_api, cube_name=cube_name, measure_name=None
        )

        conditions: List[Dict[str, Any]] = []

        for condition in self._conditions:
            if isinstance(condition, LevelCondition):
                conditions.append(
                    {
                        "level": condition.level_coordinates.java_description,
                        "type": "other",
                        "operation": condition.operator,
                        "value": condition.value.name,
                    }
                    if isinstance(condition.value, Level)
                    else {
                        "level": condition.level_coordinates.java_description,
                        "type": "constant",
                        "operation": condition.operator,
                        "value": as_java_object(
                            condition.value, gateway=java_api.gateway
                        ),
                    }
                )
            if isinstance(condition, LevelIsinCondition):
                conditions.append(
                    {
                        "level": condition.level_coordinates.java_description,
                        "type": "constant",
                        "operation": condition.operator,
                        "value": to_java_object_list(
                            tuple(member.value for member in condition.members),
                            gateway=java_api.gateway,
                        ),
                    }
                )
            if isinstance(condition, HierarchyIsinCondition):
                conditions.append(
                    {
                        "level": LevelCoordinates(
                            condition.hierarchy_coordinates.dimension_name,
                            condition.hierarchy_coordinates.hierarchy_name,
                            condition.level_names[0],
                        ).java_description,
                        "type": "constant",
                        "operation": condition.operator,
                        "value": [
                            {
                                LevelCoordinates(
                                    condition.hierarchy_coordinates.dimension_name,
                                    condition.hierarchy_coordinates.hierarchy_name,
                                    level_name,
                                ).java_description: member.value
                                for level_name, member in zip(
                                    condition.level_names, member_path
                                )
                            }
                            for member_path in condition.member_paths
                        ],
                    }
                )

        # Create the filtered measure and return its name.
        distilled_name = java_api.create_measure(
            cube_name, measure_name, "FILTER", underlying_name, conditions
        )
        return distilled_name
