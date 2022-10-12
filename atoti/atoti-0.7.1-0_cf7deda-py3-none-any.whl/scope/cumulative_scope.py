from dataclasses import dataclass
from typing import Optional, Tuple, Union

from atoti_core import LevelCoordinates, is_date_type

from .._measures.generic_measure import GenericMeasure
from ..level import Level
from ..measure_description import MeasureDescription

_TimePeriodWindow = Union[
    Tuple[str, str], Tuple[Optional[str], str], Tuple[str, Optional[str]]
]


@dataclass(frozen=True)
class CumulativeScope:  # pylint: disable=keyword-only-dataclass
    """Scope to perform a cumulative aggregation.

    Cumulative aggregations include cumulative sums (also called running sum or prefix sum), mean, min, max, etc.

    Example:
        >>> df = pd.DataFrame(
        ...     columns=["Year", "Month", "Day", "Quantity"],
        ...     data=[
        ...         (2019, 7, 1, 15),
        ...         (2019, 7, 2, 20),
        ...         (2019, 6, 1, 25),
        ...         (2019, 6, 2, 15),
        ...         (2018, 7, 1, 5),
        ...         (2018, 7, 2, 10),
        ...         (2018, 6, 1, 15),
        ...         (2018, 6, 2, 5),
        ...     ],
        ... )
        >>> table = session.read_pandas(
        ...     df,
        ...     table_name="Cumulative",
        ...     default_values={"Year": 0, "Month": 0, "Day": 0},
        ... )
        >>> cube = session.create_cube(table)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> h["Date"] = [table["Year"], table["Month"], table["Day"]]
        >>> m["Quantity.SUM"] = tt.agg.sum(table["Quantity"])
        >>> m["Cumulative quantity"] = tt.agg.sum(
        ...     m["Quantity.SUM"], scope=tt.CumulativeScope(level=l["Day"])
        ... )
        >>> m["Cumulative quantity partitioned by month"] = tt.agg.sum(
        ...     m["Quantity.SUM"],
        ...     scope=tt.CumulativeScope(level=l["Day"], partitioning=l["Month"]),
        ... )
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["Cumulative quantity"],
        ...     m["Cumulative quantity partitioned by month"],
        ...     levels=[l["Day"]],
        ...     include_totals=True,
        ... )
                        Quantity.SUM Cumulative quantity Cumulative quantity partitioned by month
        Year  Month Day
        Total                    110                 110
        2018                      35                  35
              6                   20                  20                                       20
                    1             15                  15                                       15
                    2              5                  20                                       20
              7                   15                  35                                       15
                    1              5                  25                                        5
                    2             10                  35                                       15
        2019                      75                 110
              6                   40                  75                                       40
                    1             25                  60                                       25
                    2             15                  75                                       40
              7                   35                 110                                       35
                    1             15                  90                                       15
                    2             20                 110                                       35
    """

    _level_coordinates: LevelCoordinates
    _dense: bool
    _partitioning: Optional[LevelCoordinates] = None
    _window: Union[_TimePeriodWindow, Optional[range]] = None

    def __init__(
        self,
        *,
        level: Level,
        dense: bool = False,
        partitioning: Optional[Level] = None,
        window: Union[Optional[range], _TimePeriodWindow] = None,
    ):
        """
        Args:
            level: The level along which the aggregation is performed.
            dense: When ``True``, all members of the level, even those with no value for the underlying measure, will be taken into account for the cumulative aggregation (resulting in repeating values).
            partitioning: The level in the hierarchy at which to start the aggregation over.
            window: The custom aggregation window.
                The window defines the set of members before and after a given member (using the level order) to be considered in the computation of the cumulative aggregation.

                The window can be a:

                * ``range`` starting with a <=0 value and ending with a >=0 value.

                   By default the window is ``range(-∞, 0)``, meaning that the value for a given member is computed using all of the members before it and none after it.

                   For instance, to compute the sliding mean on the 5 previous members of a level::

                      m2 = atoti.agg.mean(m1, scope=tt.CumulativeScope(level=l["date"], window=range(-5, 0)))

                * time period window as a two-element tuple of either ``None`` or a period as specified by `Java's Period.parse() <https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Period.html#parse(java.lang.CharSequence)>`__.

                  Example:

                    >>> from datetime import date
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
                    >>> table = session.read_pandas(
                    ...     df, table_name="CumulativeTimePeriod"
                    ... )
                    >>> cube = session.create_cube(table, mode="manual")
                    >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
                    >>> cube.create_date_hierarchy("Date", column=table["Date"])
                    >>> h["Date"] = {
                    ...     **h["Date"].levels,
                    ...     "Date": table["Date"],
                    ... }
                    >>> m["Quantity.SUM"] = tt.agg.sum(table["Quantity"])
                    >>> m["Cumulative quantity"] = tt.agg.sum(
                    ...     m["Quantity.SUM"], scope=tt.CumulativeScope(level=l["Date"])
                    ... )
                    >>> m["Cumulative quantity with 2 days window"] = tt.agg.sum(
                    ...     m["Quantity.SUM"],
                    ...     scope=tt.CumulativeScope(
                    ...         level=l["Date"], window=("-P2D", None)
                    ...     ),
                    ... )
                    >>> m[
                    ...     "Cumulative quantity with 2 days window partitioned by month"
                    ... ] = tt.agg.sum(
                    ...     m["Quantity.SUM"],
                    ...     scope=tt.CumulativeScope(
                    ...         level=l["Date"],
                    ...         window=("-P2D", None),
                    ...         partitioning=l["Month"],
                    ...     ),
                    ... )
                    >>> cube.query(
                    ...     m["Quantity.SUM"],
                    ...     m["Cumulative quantity"],
                    ...     m["Cumulative quantity with 2 days window"],
                    ...     m[
                    ...         "Cumulative quantity with 2 days window partitioned by month"
                    ...     ],
                    ...     levels=[l["Day"]],
                    ...     include_totals=True,
                    ... )
                                    Quantity.SUM Cumulative quantity Cumulative quantity with 2 days window Cumulative quantity with 2 days window partitioned by month
                    Year  Month Day
                    Total                     80                  80                                     35
                    2019                      80                  80                                     35
                          6                   45                  45                                      5                                                  5
                                1             25                  25                                     25                                                 25
                                2             15                  40                                     40                                                 40
                                30             5                  45                                      5                                                  5
                          7                   35                  80                                     35                                                 35
                                1             20                  65                                     25                                                 20
                                2             15                  80                                     35                                                 35

        """
        if isinstance(window, tuple) and not is_date_type(level.data_type):
            raise ValueError(
                "Time period window can only be used with hierarchy whose deepest level is temporal."
            )

        if isinstance(window, range) and window.step != 1:
            raise ValueError(
                "Running aggregation windows only support ranges with step of size 1."
            )

        self.__dict__["_level_coordinates"] = level._coordinates
        self.__dict__["_dense"] = dense
        self.__dict__["_window"] = window
        self.__dict__["_partitioning"] = (
            None if partitioning is None else partitioning._coordinates
        )

    def _create_aggregated_measure(
        self, measure: MeasureDescription, /, *, plugin_key: str
    ) -> MeasureDescription:
        return GenericMeasure(
            "WINDOW_AGG",
            measure,
            self._level_coordinates.java_description,
            self._partitioning.java_description
            if self._partitioning is not None
            else None,
            plugin_key,
            (self._window.start, self._window.stop)
            if isinstance(self._window, range)
            else self._window,
            self._dense,
        )
