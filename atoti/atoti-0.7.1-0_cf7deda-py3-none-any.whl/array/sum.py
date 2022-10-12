from __future__ import annotations

from typing import Union, overload

from .._measures.calculated_measure import CalculatedMeasure, Operator
from .._operation import JavaFunctionOperation, Operation, _to_operation
from .._udaf_utils import array_sum
from ..column import Column
from ..measure_description import MeasureDescription, _convert_to_measure_description
from ._utils import ArrayType, check_array_type


@overload
def sum(  # pylint: disable=redefined-builtin
    value: ArrayType, /
) -> JavaFunctionOperation:
    ...


@overload
def sum(  # pylint: disable=redefined-builtin
    value: MeasureDescription, /
) -> MeasureDescription:
    ...


def sum(  # pylint: disable=redefined-builtin
    value: Union[ArrayType, MeasureDescription], /
) -> Union[JavaFunctionOperation, MeasureDescription]:
    """Return a measure equal to the sum of all the elements of the passed array measure.

    Example:

        >>> pnl_table = session.read_csv(
        ...     f"{RESOURCES}/pnl.csv",
        ...     array_separator=";",
        ...     keys=["Continent", "Country"],
        ...     table_name="PnL",
        ... )
        >>> cube = session.create_cube(pnl_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Sum"] = tt.array.sum(m["PnL.SUM"])
        >>> m["Empty sum"] = tt.array.sum(m["PnL.SUM"][0:0])
        >>> cube.query(m["PnL.SUM"], m["Sum"], m["Empty sum"])
                                  PnL.SUM      Sum Empty sum
        0  doubleVector[10]{-20.163, ...}  -308.29       .00

    """
    if isinstance(value, (Operation, Column)):
        return array_sum(_to_operation(value))

    measure = _convert_to_measure_description(value)
    check_array_type(measure)
    return CalculatedMeasure(Operator("sum_vector", [measure]))
