from dataclasses import dataclass
from typing import Sequence

from atoti_core import LevelCoordinates

from ..level import Level


@dataclass(frozen=True)
class OriginScope:  # pylint: disable=keyword-only-dataclass
    """Scope to perform an aggregation starting from the specified levels.

    The passed levels define a boundary above and under which the aggregation is performed differently.
    When those levels are not expressed in a query, the queried measure will drill down until finding the value for all members of these levels, and then aggregate those values using the defined aggregation function.

    This allows to compute measures that show the yearly mean when looking at the grand total, but the sum of each month's value when looking at each year individually.

    Example:
      >>> df = pd.DataFrame(
      ...     columns=["Year", "Month", "Day", "Quantity"],
      ...     data=[
      ...         (2019, 7, 1, 15),
      ...         (2019, 7, 2, 20),
      ...         (2019, 7, 3, 30),
      ...         (2019, 6, 1, 25),
      ...         (2019, 6, 2, 15),
      ...         (2018, 7, 1, 5),
      ...         (2018, 7, 2, 10),
      ...         (2018, 6, 1, 15),
      ...         (2018, 6, 2, 5),
      ...     ],
      ... )
      >>> table = session.read_pandas(
      ...     df, table_name="Origin", default_values={"Year": 0, "Month": 0, "Day": 0}
      ... )
      >>> cube = session.create_cube(table, mode="manual")
      >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
      >>> h["Date"] = [table["Year"], table["Month"], table["Day"]]
      >>> m["Quantity.SUM"] = tt.agg.sum(table["Quantity"])
      >>> m["Average of monthly quantities"] = tt.agg.mean(
      ...     m["Quantity.SUM"], scope=tt.OriginScope(l["Month"])
      ... )
      >>> cube.query(
      ...     m["Quantity.SUM"],
      ...     m["Average of monthly quantities"],
      ...     levels=[l["Day"]],
      ...     include_totals=True,
      ... )
                      Quantity.SUM Average of monthly quantities
      Year  Month Day
      Total                    140                         35.00
      2018                      35                         17.50
            6                   20                         20.00
                  1             15                         15.00
                  2              5                          5.00
            7                   15                         15.00
                  1              5                          5.00
                  2             10                         10.00
      2019                     105                         52.50
            6                   40                         40.00
                  1             25                         25.00
                  2             15                         15.00
            7                   65                         65.00
                  1             15                         15.00
                  2             20                         20.00
                  3             30                         30.00
    """

    _levels_coordinates: Sequence[LevelCoordinates]

    def __init__(self, *levels: Level):
        """
        Args:
            levels: The levels defining the dynamic aggregation domain.
        """
        if len(levels) == 1 and isinstance(levels[0], list):
            raise TypeError("Expected variadic levels but received a list of levels.")

        self.__dict__["_levels_coordinates"] = [level._coordinates for level in levels]
