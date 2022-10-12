from __future__ import annotations

from .._measures.boolean_measure import BooleanMeasure
from ..measure_description import MeasureDescription


def conjunction(*measures: MeasureDescription) -> BooleanMeasure:
    """Return a measure equal to the logical conjunction of the passed measures."""
    return BooleanMeasure("and", measures)
