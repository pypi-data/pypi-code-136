from __future__ import annotations

from typing import Union, overload

from .._measures.calculated_measure import CalculatedMeasure, Operator
from .._operation import JavaFunctionOperation, Operation, _to_operation
from .._udaf_utils import array_mean
from ..column import Column
from ..measure_description import MeasureDescription
from ._utils import ArrayType, check_array_type


@overload
def mean(value: ArrayType, /) -> JavaFunctionOperation:
    ...


@overload
def mean(value: MeasureDescription, /) -> MeasureDescription:
    ...


def mean(
    value: Union[ArrayType, MeasureDescription], /
) -> Union[MeasureDescription, JavaFunctionOperation]:
    """Return a measure equal to the mean of all the elements of the passed array measure.

    Example:

        >>> pnl_table = session.read_csv(
        ...     f"{RESOURCES}/pnl.csv",
        ...     array_separator=";",
        ...     keys=["Continent", "Country"],
        ...     table_name="PnL",
        ... )
        >>> cube = session.create_cube(pnl_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Mean"] = tt.array.mean(m["PnL.SUM"])
        >>> m["Empty mean"] = tt.array.mean(m["PnL.SUM"][0:0])
        >>> cube.query(m["PnL.SUM"], m["Mean"], m["Empty mean"])
                                  PnL.SUM    Mean Empty mean
        0  doubleVector[10]{-20.163, ...}  -30.83        .00

    """
    if isinstance(value, (Operation, Column)):
        return array_mean(_to_operation(value))
    check_array_type(value)
    return CalculatedMeasure(Operator("mean_vector", [value]))
