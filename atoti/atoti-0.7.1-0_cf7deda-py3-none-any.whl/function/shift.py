from typing import Optional, Union

from atoti_core import deprecated

from atoti.hierarchy import Hierarchy
from atoti.level import Level

from .._measures.generic_measure import GenericMeasure
from ..hierarchy import Hierarchy
from ..measure_description import MeasureDescription


def shift(
    measure: MeasureDescription,
    on: Union[Hierarchy, Level],
    /,
    *,
    offset: int = 1,
    partitioning: Optional[Level] = None,
) -> MeasureDescription:
    """Return a measure equal to the passed measure shifted to another member of the hierarchy.

    Args:
        measure: The measure to shift.
        on: The hierarchy to shift on.
        offset: The amount of members to shift by.
        partitioning: The level in the hierarchy at which to start the shift over.

    Example:
        >>> df = pd.DataFrame(
        ...     columns=["Country", "City", "Price"],
        ...     data=[
        ...         ("France", "Bordeaux", 1),
        ...         ("France", "Lyon", 2),
        ...         ("France", "Paris", 3),
        ...         ("Germany", "Berlin", 4),
        ...         ("Germany", "Frankfurt", 5),
        ...         ("Germany", "Munich", 6),
        ...     ],
        ... )
        >>> table = session.read_pandas(
        ...     df,
        ...     table_name="Shift example",
        ... )
        >>> cube = session.create_cube(table)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> m["Shifted Price.SUM"] = tt.shift(m["Price.SUM"], h["City"], offset=2)
        >>> cube.query(
        ...     m["Price.SUM"],
        ...     m["Shifted Price.SUM"],
        ...     levels=[l["City"]],
        ...     include_totals=True,
        ... )
                  Price.SUM Shifted Price.SUM
        City
        Total            21
        Berlin            4                 5
        Bordeaux          1                 2
        Frankfurt         5                 6
        Lyon              2                 3
        Munich            6
        Paris             3

        >>> h["Location"] = [l["Country"], l["City"]]
        >>> m["Shifted Price.SUM"] = tt.shift(m["Price.SUM"], h["Location"], offset=1)
        >>> m["Shifted Price.SUM partitioned by Country"] = tt.shift(
        ...     m["Price.SUM"],
        ...     h["Location"],
        ...     offset=1,
        ...     partitioning=l["Location", "Country"],
        ... )
        >>> cube.query(
        ...     m["Price.SUM"],
        ...     m["Shifted Price.SUM"],
        ...     m["Shifted Price.SUM partitioned by Country"],
        ...     levels=[
        ...         l["Shift example", "Location", "Country"],
        ...         l["Shift example", "Location", "City"],
        ...     ],
        ...     include_totals=True,
        ... )
                          Price.SUM Shifted Price.SUM Shifted Price.SUM partitioned by Country
        Country City
        Total                    21
        France                    6                15
                Bordeaux          1                 2                                        2
                Lyon              2                 3                                        3
                Paris             3                 4
        Germany                  15
                Berlin            4                 5                                        5
                Frankfurt         5                 6                                        6
                Munich            6
    """
    if isinstance(on, Level):
        deprecated(
            "Passing a `Level` to the *on* parameter is deprecated, use a `Hierarchy` instead."
        )

    return GenericMeasure(
        "LEAD_LAG",
        measure,
        (
            on._coordinates if isinstance(on, Hierarchy) else on._hierarchy_coordinates
        ).java_description,
        offset,
        partitioning._coordinates.java_description
        if partitioning is not None
        else None,
    )
