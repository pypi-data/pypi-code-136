from __future__ import annotations

from typing import Union

from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription, _convert_to_measure_description
from ._utils import check_array_type, validate_n_argument


def n_greatest(
    measure: MeasureDescription, /, n: Union[int, MeasureDescription]
) -> MeasureDescription:
    """Return an array measure containing the *n* greatest elements of the passed array measure.

    The values in the returned array are not sorted, use :func:`atoti.array.sort` to sort them.

    Example:

        >>> pnl_table = session.read_csv(
        ...     f"{RESOURCES}/pnl.csv",
        ...     array_separator=";",
        ...     keys=["Continent", "Country"],
        ...     table_name="PnL",
        ... )
        >>> cube = session.create_cube(pnl_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Top 3"] = tt.array.n_greatest(m["PnL.SUM"], n=3)
        >>> cube.query(m["PnL.SUM"], m["Top 3"])
                                  PnL.SUM                                    Top 3
        0  doubleVector[10]{-20.163, ...}  doubleVector[3]{9.259999999999998, ...}

    """
    validate_n_argument(n)
    check_array_type(measure)
    return CalculatedMeasure(
        Operator("n_greatest", [measure, _convert_to_measure_description(n)])
    )
