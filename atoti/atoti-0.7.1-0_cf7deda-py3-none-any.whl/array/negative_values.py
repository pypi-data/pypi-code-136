from __future__ import annotations

from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription
from ._utils import check_array_type


def negative_values(measure: MeasureDescription, /) -> MeasureDescription:
    """Return a measure where all the elements > 0 of the passed array measure are replaced by 0."""
    check_array_type(measure)
    return CalculatedMeasure(Operator("negative_vector", [measure]))
