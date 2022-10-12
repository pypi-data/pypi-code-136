from dataclasses import dataclass
from typing import Optional

from atoti_core import HierarchyCoordinates, keyword_only_dataclass

from ..._java_api import JavaApi
from ...measure_description import MeasureDescription


@keyword_only_dataclass
@dataclass(eq=False)
class IrrMeasure(MeasureDescription):
    """Internal Rate of Return measure."""

    _cash_flows_measure: MeasureDescription
    _market_value_measure: MeasureDescription
    _date_hierarchy_coordinates: HierarchyCoordinates
    _precision: float

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        # Distil the underlying measures
        cash_flows_name = self._cash_flows_measure._distil(
            java_api=java_api, cube_name=cube_name, measure_name=None
        )
        market_value_name = self._market_value_measure._distil(
            java_api=java_api, cube_name=cube_name, measure_name=None
        )

        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "IRR",
            market_value_name,  # market value first
            cash_flows_name,
            self._date_hierarchy_coordinates.java_description,
            self._precision,
        )
        return distilled_name
