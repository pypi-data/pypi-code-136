from dataclasses import dataclass
from typing import Optional, Sequence

from atoti_core import is_array_type, keyword_only_dataclass

from .._java_api import JavaApi
from ..column import Column
from ..measure_description import MeasureDescription
from ..type import DOUBLE_ARRAY
from .utils import get_measure_name


@keyword_only_dataclass
@dataclass(eq=False)
class SumProductFieldsMeasure(MeasureDescription):
    """Sum of the product of factors for table fields."""

    _factors: Sequence[Column]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        # Checks fields are in the selection, otherwise use the other sum product implementation because UDAF needs fields in the selection.
        selection_fields = java_api.get_selection_fields(cube_name)
        if not all(
            factor._column_coordinates in selection_fields for factor in self._factors
        ):
            raise ValueError(
                f"The columns {[factor.name for factor in self._factors if not factor._column_coordinates in selection_fields]}"
                f" cannot be used in a sum product aggregation without first being converted into measures."
            )
        factors_and_type = {}
        for factor in self._factors:
            if is_array_type(factor.data_type) and factor.data_type != DOUBLE_ARRAY:
                raise TypeError(
                    f"Unsupported operation. Only array columns of type {DOUBLE_ARRAY} are supported and {factor} is not."
                )
            factors_and_type[factor._column_coordinates] = factor.data_type
        return java_api.create_measure(
            cube_name,
            measure_name,
            "SUM_PRODUCT_UDAF",
            [factor._column_coordinates for factor in self._factors],
            factors_and_type,
        )


@keyword_only_dataclass
@dataclass(eq=False)
class SumProductEncapsulationMeasure(MeasureDescription):
    """Create an intermediate measure needing to be aggregated with the key "SUM_PRODUCT"."""

    _factors: Sequence[MeasureDescription]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:

        return java_api.create_measure(
            cube_name,
            measure_name,
            "SUM_PRODUCT_ENCAPSULATION",
            [
                get_measure_name(java_api=java_api, measure=factor, cube_name=cube_name)
                for factor in self._factors
            ],
        )
