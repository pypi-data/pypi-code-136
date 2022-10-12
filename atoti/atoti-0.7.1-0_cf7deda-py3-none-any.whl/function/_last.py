from typing import Optional

from .._measures.first_last import FirstLast
from ..level import Level
from ..measure_description import MeasureDescription


def last(
    measure: MeasureDescription, on: Level, /, *, partitioning: Optional[Level] = None
) -> MeasureDescription:
    """Return a measure equal to the last value of the passed measure on the level.

    Args:
        measure: The measure to shift.
        on: The level to shift on.
        partitioning: The level in the hierarchy at which to start the last over.

    Example:

        >>> from datetime import date
        >>> from atoti.function._last import last
        >>> df = pd.DataFrame(
        ...     columns=["Date", "Quantity"],
        ...     data=[
        ...         (date(2019, 7, 2), 15),
        ...         (date(2019, 7, 1), 20),
        ...         (date(2019, 6, 1), 25),
        ...         (date(2019, 6, 2), 15),
        ...         (date(2019, 6, 30), 5),
        ...     ],
        ... )
        >>> table = session.read_pandas(df, table_name="CumulativeTimePeriod")
        >>> cube = session.create_cube(table, mode="manual")
        >>> l, m = cube.levels, cube.measures
        >>> cube.create_date_hierarchy("Date", column=table["Date"])
        >>> m["Quantity.SUM"] = tt.agg.sum(table["Quantity"])
        >>> m["Quantity last day"] = last(m["Quantity.SUM"], l["Day"])
        >>> m["Quantity last day of month"] = last(
        ...     m["Quantity.SUM"], l["Day"], partitioning=l["Month"]
        ... )
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["Quantity last day"],
        ...     m["Quantity last day of month"],
        ...     levels=[l["Day"]],
        ...     include_totals=True,
        ... )
                        Quantity.SUM Quantity last day Quantity last day of month
        Total                     80                15
        2019                      80                15
              6                   45                15                          5
                    1             25                15                          5
                    2             15                15                          5
                    30             5                15                          5
              7                   35                15                         15
                    1             20                15                         15
                    2             15                15                         15

    """
    return FirstLast(
        _underlying_measure=measure,
        _level_coordinates=on._coordinates,
        _mode="LAST",
        _partitioning=partitioning._coordinates if partitioning is not None else None,
    )
