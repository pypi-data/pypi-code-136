from dataclasses import dataclass
from typing import Literal, Optional

from atoti_core import LevelCoordinates, keyword_only_dataclass

from .._java_api import JavaApi
from ..measure_description import MeasureDescription
from .utils import get_measure_name


@keyword_only_dataclass
@dataclass(eq=False)
class FirstLast(MeasureDescription):
    """Shift the value."""

    _underlying_measure: MeasureDescription
    _level_coordinates: LevelCoordinates
    _mode: Literal["FIRST", "LAST"]
    _partitioning: Optional[LevelCoordinates]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        underlying_name = get_measure_name(
            java_api=java_api, measure=self._underlying_measure, cube_name=cube_name
        )
        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "FIRST_LAST",
            underlying_name,
            self._level_coordinates.java_description,
            self._mode,
            self._partitioning.java_description
            if self._partitioning is not None
            else None,
        )
        return distilled_name
