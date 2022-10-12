from __future__ import annotations

from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription
from ._utils import check_array_type


def min(  # pylint: disable=redefined-builtin
    measure: MeasureDescription, /
) -> MeasureDescription:
    """Return a measure equal to the minimum element of the passed array measure.

    Example:

        >>> pnl_table = session.read_csv(
        ...     f"{RESOURCES}/pnl.csv",
        ...     array_separator=";",
        ...     keys=["Continent", "Country"],
        ...     table_name="PnL",
        ... )
        >>> cube = session.create_cube(pnl_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Min"] = tt.array.min(m["PnL.SUM"])
        >>> m["Empty min"] = tt.array.min(m["PnL.SUM"][0:0])
        >>> cube.query(m["PnL.SUM"], m["Min"], m["Empty min"])
                                  PnL.SUM      Min Empty min
        0  doubleVector[10]{-20.163, ...}  -110.10

    """
    check_array_type(measure)
    return CalculatedMeasure(Operator("min_vector", [measure]))
