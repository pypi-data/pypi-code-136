from dataclasses import dataclass
from typing import Optional

from atoti_core import LevelCoordinates

from .._java_api import JavaApi
from ..measure_description import MeasureDescription


@dataclass(eq=False)
class LevelMeasure(MeasureDescription):  # pylint: disable=keyword-only-dataclass
    """Measure based on a cube level."""

    _level_coordinates: LevelCoordinates

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "LEVEL",
            self._level_coordinates.java_description,
        )
        return distilled_name
