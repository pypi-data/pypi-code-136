from dataclasses import dataclass

from atoti_core import HierarchyCoordinates

from .._measures.generic_measure import GenericMeasure
from ..hierarchy import Hierarchy
from ..measure_description import MeasureDescription


@dataclass(frozen=True)
class SiblingsScope:  # pylint: disable=keyword-only-dataclass
    """Scope to perform a "siblings" aggregation.

    With a siblings scope, the value for the member of a given level in the hierarchy is computed by taking the contribution of all of the members on the same level (its siblings).

    A siblings aggregation is an appropriate tool for operations such as marginal aggregations (marginal VaR, marginal mean) for non-linear aggregation functions.

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
        ...     df,
        ...     table_name="Siblings",
        ...     default_values={"Year": 0, "Month": 0, "Day": 0},
        ... )
        >>> cube = session.create_cube(table, mode="manual")
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> h["Date"] = [table["Year"], table["Month"], table["Day"]]
        >>> m["Quantity.SUM"] = tt.agg.sum(table["Quantity"])
        >>> m["Siblings quantity"] = tt.agg.sum(
        ...     m["Quantity.SUM"], scope=tt.SiblingsScope(hierarchy=h["Date"])
        ... )
        >>> m["Siblings quantity excluding self"] = tt.agg.sum(
        ...     m["Quantity.SUM"],
        ...     scope=tt.SiblingsScope(hierarchy=h["Date"], exclude_self=True),
        ... )
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["Siblings quantity"],
        ...     m["Siblings quantity excluding self"],
        ...     levels=[l["Day"]],
        ...     include_totals=True,
        ... )
                        Quantity.SUM Siblings quantity Siblings quantity excluding self
        Year  Month Day
        Total                    140               140                                0
        2018                      35               140                              105
              6                   20                35                               15
                    1             15                20                                5
                    2              5                20                               15
              7                   15                35                               20
                    1              5                15                               10
                    2             10                15                                5
        2019                     105               140                               35
              6                   40               105                               65
                    1             25                40                               15
                    2             15                40                               25
              7                   65               105                               40
                    1             15                65                               50
                    2             20                65                               45
                    3             30                65                               35
    """

    _hierarchy_coordinates: HierarchyCoordinates
    _exclude_self: bool

    def __init__(self, *, hierarchy: Hierarchy, exclude_self: bool = False):
        """
        Args:
            hierarchy: The hierarchy containing the levels along which the aggregation is performed.
            exclude_self: Whether to include the current member's contribution in its cumulative value.
        """
        self.__dict__["_hierarchy_coordinates"] = hierarchy._coordinates
        self.__dict__["_exclude_self"] = exclude_self

    def _create_aggregated_measure(
        self, measure: MeasureDescription, /, *, plugin_key: str
    ) -> MeasureDescription:
        return GenericMeasure(
            "SIBLINGS_AGG",
            measure,
            self._hierarchy_coordinates.java_description,
            plugin_key,
            self._exclude_self,
        )
