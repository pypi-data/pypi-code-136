from __future__ import annotations

from .._condition import Condition
from .._level_condition import LevelCondition
from .._measures.boolean_measure import BooleanMeasure
from .._measures.filtered_measure import LevelValueFilteredMeasure
from .._multi_condition import MultiCondition
from .._single_condition import SingleCondition
from ..level import Level
from ..measure_description import (
    MeasureDescription,
    MeasureLike,
    _convert_to_measure_description,
)


def filter(  # pylint: disable=redefined-builtin
    measure: MeasureLike, condition: Condition, /
) -> MeasureDescription:
    """Return a filtered measure.

    The new measure is equal to the passed one where the condition is ``True`` and to ``None`` elsewhere.

    Args:
        measure: The measure to filter.
        condition: The condition to evaluate.

    Example:

        >>> from datetime import date
        >>> data = pd.DataFrame(
        ...     {
        ...         "Date": [date(2021, 1, 13), date(2021, 7, 5), date(2021, 7, 6)],
        ...         "City": ["Paris", "Paris", "London"],
        ...         "Age": [18, 25, 8],
        ...         "Quantity": [200, 500, 100],
        ...     }
        ... )
        >>> table = session.read_pandas(
        ...     data, table_name="City date table", default_values={"Age": 0}
        ... )
        >>> table.head()
                Date    City  Age  Quantity
        0 2021-01-13   Paris   18       200
        1 2021-07-05   Paris   25       500
        2 2021-07-06  London    8       100
        >>> cube = session.create_cube(table)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> h.update({name: {name: table[name]} for name in ["Date", "City", "Age"]})
        >>> # Levels compared to constants of the same type:
        >>> m["London Quantity.SUM"] = tt.filter(
        ...     m["Quantity.SUM"], l["City"] == "London"
        ... )
        >>> m["Quantity.SUM before July"] = tt.filter(
        ...     m["Quantity.SUM"], l["Date"] < date(2021, 7, 1)
        ... )
        >>> m["Quantity.SUM for age under 18"] = tt.filter(
        ...     m["Quantity.SUM"], l["Age"] <= 18
        ... )
        >>> # A conjunction of conditions using the ``&`` operator:
        >>> m["July Quantity.SUM in Paris"] = tt.filter(
        ...     m["Quantity.SUM"],
        ...     (
        ...         (l["City"] == "Paris")
        ...         & ((l["Date"]) >= date(2021, 7, 1))
        ...         & (l["Date"] <= date(2021, 7, 31))
        ...     ),
        ... )
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["London Quantity.SUM"],
        ...     m["Quantity.SUM before July"],
        ...     m["Quantity.SUM for age under 18"],
        ...     m["July Quantity.SUM in Paris"],
        ... )
          Quantity.SUM London Quantity.SUM Quantity.SUM before July Quantity.SUM for age under 18 July Quantity.SUM in Paris
        0          800                 100                      200                           300                        500
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["London Quantity.SUM"],
        ...     m["Quantity.SUM before July"],
        ...     m["Quantity.SUM for age under 18"],
        ...     m["July Quantity.SUM in Paris"],
        ...     levels=[l["Date"], l["Age"], l["City"]],
        ... )
                              Quantity.SUM London Quantity.SUM Quantity.SUM before July Quantity.SUM for age under 18 July Quantity.SUM in Paris
        Date       Age City
        2021-01-13 18  Paris           200                                          200                           200
        2021-07-05 25  Paris           500                                                                                                   500
        2021-07-06 8   London          100                 100                                                    100

    """

    measure = _convert_to_measure_description(measure)

    if isinstance(condition, BooleanMeasure):
        raise ValueError("Use atoti.where() for conditions with measures.")

    if isinstance(condition, LevelCondition):
        if isinstance(condition.value, Level):
            raise ValueError("Conditions between two levels are not supported.")

        return LevelValueFilteredMeasure(
            _underlying_measure=measure, _conditions=[condition]
        )

    if isinstance(condition, SingleCondition):
        return LevelValueFilteredMeasure(
            _underlying_measure=measure, _conditions=[condition]
        )

    if not isinstance(condition, MultiCondition):
        raise TypeError(f"Unsupported condition type: {type(condition)}.")

    if any(
        isinstance(single_condition, BooleanMeasure)
        for single_condition in condition.conditions
    ):
        raise ValueError("Use atoti.where() for conditions with measures.")

    return LevelValueFilteredMeasure(
        _underlying_measure=measure,
        _conditions=condition.conditions,
    )
