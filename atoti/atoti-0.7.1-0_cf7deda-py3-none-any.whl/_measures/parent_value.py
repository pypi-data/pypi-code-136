from dataclasses import dataclass
from typing import Mapping, Optional, Union

from atoti_core import HierarchyCoordinates, keyword_only_dataclass

from .._java_api import JavaApi
from .._measures.utils import get_measure_name
from ..measure_description import MeasureDescription, MeasureLike


@keyword_only_dataclass
@dataclass(eq=False)
class ParentValue(MeasureDescription):
    """The value of the measure for the parent."""

    _underlying_measure: Union[MeasureDescription, str]
    _degrees: Mapping[HierarchyCoordinates, int]
    _total_value: Optional[MeasureLike]
    _apply_filters: bool

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        underlying_name = (
            self._underlying_measure
            if isinstance(self._underlying_measure, str)
            else get_measure_name(
                java_api=java_api, measure=self._underlying_measure, cube_name=cube_name
            )
        )
        total_measure_name = (
            self._total_value._distil(java_api=java_api, cube_name=cube_name)
            if isinstance(self._total_value, MeasureDescription)
            else None
        )
        total_literal = self._total_value if total_measure_name is None else None

        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "PARENT_VALUE",
            underlying_name,
            {
                coordinates.java_description: degree
                for coordinates, degree in self._degrees.items()
            },
            total_measure_name,
            total_literal,
            self._apply_filters,
        )
        return distilled_name
