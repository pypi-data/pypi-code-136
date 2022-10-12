from __future__ import annotations

from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription
from ._utils import check_array_type


def sort(
    measure: MeasureDescription, /, *, ascending: bool = True
) -> MeasureDescription:
    """Return an array measure with the elements of the passed array measure sorted.

    Example:

        >>> pnl_table = session.read_csv(
        ...     f"{RESOURCES}/pnl.csv",
        ...     array_separator=";",
        ...     keys=["Continent", "Country"],
        ...     table_name="PnL",
        ... )
        >>> cube = session.create_cube(pnl_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Ascending sort"] = tt.array.sort(m["PnL.SUM"])
        >>> m["Descending sort"] = tt.array.sort(m["PnL.SUM"], ascending=False)
        >>> cube.query(m["PnL.SUM"], m["Ascending sort"], m["Descending sort"])
                                  PnL.SUM                              Ascending sort                           Descending sort
        0  doubleVector[10]{-20.163, ...}  doubleVector[10]{-110.09900000000002, ...}  doubleVector[10]{9.259999999999998, ...}

    """
    check_array_type(measure)
    return CalculatedMeasure(Operator("sort", [measure, str(ascending)]))
