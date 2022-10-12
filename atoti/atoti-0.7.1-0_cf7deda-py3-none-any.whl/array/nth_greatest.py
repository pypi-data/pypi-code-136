from __future__ import annotations

from typing import Union

from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription, _convert_to_measure_description
from ._utils import check_array_type, validate_n_argument


def nth_greatest(
    measure: MeasureDescription, /, n: Union[int, MeasureDescription]
) -> MeasureDescription:
    """Return a measure equal to the *n*-th greatest element of the passed array measure.

    Example:

            >>> pnl_table = session.read_csv(
            ...     f"{RESOURCES}/pnl.csv",
            ...     array_separator=";",
            ...     keys=["Continent", "Country"],
            ...     table_name="PnL",
            ... )
            >>> cube = session.create_cube(pnl_table)
            >>> l, m = cube.levels, cube.measures
            >>> m["3rd greatest"] = tt.array.nth_greatest(m["PnL.SUM"], n=3)
            >>> cube.query(m["PnL.SUM"], m["3rd greatest"])
                                      PnL.SUM 3rd greatest
            0  doubleVector[10]{-20.163, ...}         -.53

    """
    validate_n_argument(n)
    check_array_type(measure)
    return CalculatedMeasure(
        Operator("nth_greatest", [measure, _convert_to_measure_description(n)])
    )
