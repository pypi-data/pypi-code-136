from __future__ import annotations

from typing import Union

from .._measures.calculated_measure import CalculatedMeasure, Operator
from ..measure_description import MeasureDescription, _convert_to_measure_description
from ._utils import check_array_type, validate_n_argument


def n_lowest_indices(
    measure: MeasureDescription, /, n: Union[int, MeasureDescription]
) -> MeasureDescription:
    """Return an array measure containing the indices of the *n* lowest elements of the passed array measure.

    The indices in the returned array are sorted, so the first index corresponds to the lowest value and the last index to to the n-th lowest value.

    Example:

        >>> pnl_table = session.read_csv(
        ...     f"{RESOURCES}/pnl.csv",
        ...     array_separator=";",
        ...     keys=["Continent", "Country"],
        ...     table_name="PnL",
        ... )
        >>> cube = session.create_cube(pnl_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Bottom 3 indices"] = tt.array.n_lowest_indices(m["PnL.SUM"], n=3)
        >>> cube.query(m["PnL.SUM"], m["Bottom 3 indices"])
                                  PnL.SUM      Bottom 3 indices
        0  doubleVector[10]{-20.163, ...}  intVector[3]{2, ...}

    """
    validate_n_argument(n)
    check_array_type(measure)
    return CalculatedMeasure(
        Operator("n_lowest_indices", [measure, _convert_to_measure_description(n)])
    )
