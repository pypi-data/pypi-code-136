from __future__ import annotations

from typing import List, Mapping, Optional, Tuple, Union, overload

from atoti_core import ConstantValue

from .._column_condition import ColumnCondition
from .._condition import Condition
from .._data_type_error import DataTypeError
from .._measures.filtered_measure import WhereMeasure
from .._multi_condition import MultiCondition
from .._operation import Operation, TernaryOperation, _to_operation
from .._single_condition import SingleCondition
from ..column import Column
from ..measure import Measure
from ..measure_description import (
    MeasureDescription,
    MeasureLike,
    _convert_to_measure_description,
)
from ..type import BOOLEAN

_OperationLike = Union[ConstantValue, Column, Operation]


@overload
def where(  # pylint: disable=too-many-positional-parameters
    condition: ColumnCondition,
    true_value: _OperationLike,
    false_value: Optional[_OperationLike] = None,
    /,
) -> TernaryOperation:
    ...


@overload
def where(  # pylint: disable=too-many-positional-parameters
    condition: Union[
        Condition,
        Measure,
    ],
    true_value: MeasureLike,
    # Not keyword-only to be symmetrical with true_value and because
    # there probably will not be more optional parameters.
    false_value: Optional[MeasureLike] = None,
    /,
) -> MeasureDescription:
    ...


@overload
def where(
    condition_to_value: Mapping[
        Union[
            Condition,
            Measure,
        ],
        MeasureLike,
    ],
    /,
    *,
    default: Optional[MeasureLike] = None,
) -> MeasureDescription:
    ...


def where(  # pylint: disable=too-many-positional-parameters
    where_condition: Union[
        ColumnCondition,
        Condition,
        Measure,
        Mapping[
            Union[
                Condition,
                Measure,
            ],
            MeasureLike,
        ],
    ],
    # Optional to support the where overload above
    true_value: Optional[Union[MeasureLike, _OperationLike]] = None,
    false_value: Optional[Union[MeasureLike, _OperationLike]] = None,
    /,
    *,
    default: Optional[MeasureLike] = None,
) -> Union[MeasureDescription, TernaryOperation]:
    """Return a conditional measure.

    This function is like an *if-then-else* statement:

    * Where the condition is ``True``, the new measure will be equal to *true_value*.
    * Where the condition is ``False``, the new measure will be equal to *false_value*.

    If *false_value* is not ``None``, *true_value* and *false_value* must either be both numerical, both boolean or both objects.

    If one of the values compared in the condition is ``None``, the condition will be considered ``False``.

    Different types of conditions are supported:

    * Measures compared to anything measure-like::

        m["Test"] == 20

    * Levels compared to levels, (if the level is not expressed, it is considered ``None``)::

        l["source"] == l["destination"]

    * Levels compared to constants of the same type::

        l["city"] == "Paris"
        l["date"] > datetime.date(2020,1,1)
        l["age"] <= 18

    * A conjunction or disjunction of conditions using the ``&`` operator or ``|`` operator::

        (m["Test"] == 20) & (l["city"] == "Paris")
        (l["Country"] == "USA") | (l["Currency"] == "USD")


    Example:
        >>> df = pd.DataFrame(
        ...     columns=["Id", "City", "Value"],
        ...     data=[
        ...         (0, "Paris", 1.0),
        ...         (1, "Paris", 2.0),
        ...         (2, "London", 3.0),
        ...         (3, "London", 4.0),
        ...         (4, "Paris", 5.0),
        ...     ],
        ... )
        >>> table = session.read_pandas(df, keys=["Id"], table_name="filter example")
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Paris value"] = tt.where(l["City"] == "Paris", m["Value.SUM"], 0)
        >>> cube.query(m["Paris value"], levels=[l["City"]])
               Paris value
        City
        London         .00
        Paris         8.00

        When a mapping of condition to value is passed, the resulting value is the one of the first condition evaluating to ``True``:

        >>> m["Value.RECAP"] = tt.where(
        ...     {
        ...         m["Value.SUM"] < 3: "less than 3",
        ...         m["Value.SUM"] <= 3: "less than or equal to 3",
        ...         m["Value.SUM"]
        ...         == 3: "equal to 3",  # never used because of the broader condition before
        ...     },
        ...     default="more than 3",
        ... )
        >>> cube.query(m["Value.SUM"], m["Value.RECAP"], levels=[l["Id"]])
           Value.SUM              Value.RECAP
        Id
        0       1.00              less than 3
        1       2.00              less than 3
        2       3.00  less than or equal to 3
        3       4.00              more than 3
        4       5.00              more than 3

    See also:
        :func:`atoti.switch`.
    """
    if isinstance(where_condition, ColumnCondition):
        true_operation = _to_operation(true_value)
        false_operation = (
            _to_operation(false_value) if false_value is not None else None
        )
        return TernaryOperation(
            condition=where_condition._to_operation(),
            true_operation=true_operation,
            false_operation=false_operation,
        )
    if isinstance(true_value, (Column, Operation)) or isinstance(
        false_value, (Column, Operation)
    ):
        raise ValueError(
            "Cannot use tt.where on operations if the condition is not also an operation. Please convert the true (and false) value(s) to a measure(s)."
        )

    if isinstance(where_condition, Mapping):
        false_value = default
        measures_to_conditions = {
            _convert_to_measure_description(
                value
            ): _convert_condition_to_measure_description(condition)
            for condition, value in where_condition.items()
        }

    else:
        if true_value is None:
            raise TypeError("Missing `true_value`.")
        measures_to_conditions = {
            _convert_to_measure_description(
                true_value
            ): _convert_condition_to_measure_description(where_condition)
        }

    return WhereMeasure(
        _measure_to_conditions=measures_to_conditions,
        _default_measure=_convert_to_measure_description(false_value)
        if false_value is not None
        else None,
    )


def _convert_condition_to_measure_description(
    condition: Union[
        ColumnCondition,
        Condition,
        Measure,
    ],
    /,
) -> Tuple[MeasureDescription, ...]:
    conditions: List[MeasureDescription] = []

    if isinstance(condition, SingleCondition):
        conditions.append(condition._measure_description)

    elif isinstance(condition, Measure):
        if condition.data_type != BOOLEAN:
            message = (
                "Incorrect measure type."
                f" Expected measure {condition.name} to be of type boolean but got {condition.data_type}."
            )
            raise DataTypeError(message)
        conditions.append(condition)

    elif isinstance(condition, MultiCondition):
        for _condition in condition.conditions:
            conditions.append(_condition._measure_description)

    return (*conditions,)
