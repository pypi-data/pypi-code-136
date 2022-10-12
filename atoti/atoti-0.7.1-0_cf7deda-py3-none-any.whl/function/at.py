from typing import Any, List, Mapping, Optional, Tuple, Union

from atoti_core import BaseCondition, deprecated

from .._condition import Condition
from .._level_condition import LevelCondition
from .._level_isin_condition import LevelIsinCondition
from .._measures.generic_measure import GenericMeasure
from .._multi_condition import MultiCondition
from ..level import Level
from ..measure_description import MeasureDescription


def _add_value(
    value: Any, /, *, target_levels: List[Optional[str]], target_values: List[Any]
) -> None:
    if isinstance(value, Level):
        target_levels.append(value._coordinates.java_description)
        target_values.append(None)
    else:
        target_levels.append(None)
        target_values.append(value)


def _unwrap_conditions_from_coordinates(
    coordinates: Mapping[Level, Any], /
) -> Tuple[List[str], List[Any], List[Optional[str]]]:
    """Transform a map of coordinates into its corresponding list of levels, target values, and target levels."""
    levels: List[str] = []
    target_levels: List[Optional[str]] = []
    target_values: List[Any] = []
    for level, value in coordinates.items():
        levels.append(level._coordinates.java_description)
        _add_value(value, target_values=target_values, target_levels=target_levels)
    return levels, target_values, target_levels


def _unwrap_and_check_conditions(
    condition: BaseCondition,
    *,
    levels: List[str],
    target_levels: List[Optional[str]],
    target_values: List[Any],
) -> Tuple[List[str], List[Any], List[Optional[str]]]:
    """Transform a condition into its corresponding list of level coordinates, target values, and target level coordinates."""
    if isinstance(condition, LevelCondition):
        if condition.operator != "eq":
            raise ValueError(
                f"Only the `eq` operator is supported for the `at` function, got `{condition.operator}`."
            )
        levels.append(condition.level_coordinates.java_description)
        _add_value(
            condition.value, target_levels=target_levels, target_values=target_values
        )
    if isinstance(condition, LevelIsinCondition):
        raise ValueError("The condition must be an equality test with a single value.")
    if isinstance(condition, MultiCondition):
        for single_condition in condition.conditions:
            levels, target_values, target_levels = _unwrap_and_check_conditions(
                single_condition,
                levels=levels,
                target_levels=target_levels,
                target_values=target_values,
            )
    if len(levels) != len(list(set(levels))):
        raise ValueError(
            "The condition cannot contain two conditions on the same level."
        )
    return levels, target_values, target_levels


def at(
    measure: MeasureDescription,
    coordinates: Union[Condition, Mapping[Level, Any]],
    /,
) -> MeasureDescription:
    """Return a measure equal to the passed measure at some other coordinates of the cube.

    Args:
        measure: The measure to take at other coordinates.
        coordinates: The condition specifying the coordinates at which to fetch the measure's value.
            It can only be a condition made of an equality test of a level with a single value or a combination of such conditions.

    Example:

        >>> df = pd.DataFrame(
        ...     columns=[
        ...         "Country",
        ...         "City",
        ...         "Target Country",
        ...         "Target City",
        ...         "Quantity",
        ...     ],
        ...     data=[
        ...         ("Germany", "Berlin", "UK", "London", 15),
        ...         ("UK", "London", "Germany", "Berlin", 24),
        ...         ("USA", "New York", "UK", "London", 10),
        ...         ("USA", "New York", "France", "Paris", 3),
        ...         ("USA", "Seattle", "Germany", "Berlin", 3),
        ...     ],
        ... )
        >>> table = session.read_pandas(df, table_name="At")
        >>> cube = session.create_cube(table, mode="manual")
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> h["Geography"] = [table["Country"], table["City"]]
        >>> h["Target Geography"] = [
        ...     table["Target Country"],
        ...     table["Target City"],
        ... ]
        >>> m["Quantity.SUM"] = tt.agg.sum(table["Quantity"])
        >>> # Using a constant matching an existing member of the level:
        >>> m["USA quantity"] = tt.at(m["Quantity.SUM"], l["Country"] == "USA")
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["USA quantity"],
        ...     levels=[l["Country"]],
        ... )
                Quantity.SUM USA quantity
        Country
        Germany           15           16
        UK                24           16
        USA               16           16
        >>> # Using another level whose current member the level on the left of the condition will be shifted to:
        >>> m["Target quantity"] = tt.at(
        ...     m["Quantity.SUM"],
        ...     (l["Country"] == l["Target Country"]) & (l["City"] == l["Target City"]),
        ... )
        >>> cube.query(
        ...     m["Quantity.SUM"],
        ...     m["Target quantity"],
        ...     levels=[l["City"], l["Target City"]],
        ... )
                                                    Quantity.SUM Target quantity
        Country City     Target Country Target City
        Germany Berlin   UK             London                15              24
        UK      London   Germany        Berlin                24              15
        USA     New York France         Paris                  3
                         UK             London                10              24
                Seattle  Germany        Berlin                 3              15

        Note that if the level on the right is not expressed, the shifting will not occur.

    """
    if isinstance(coordinates, Mapping):
        deprecated(
            "Passing a `Mapping` to `coordinates` is deprecated, pass a `Condition` instead."
        )
        (
            levels,
            values,
            target_levels,
        ) = _unwrap_conditions_from_coordinates(coordinates)
    else:
        (levels, values, target_levels,) = _unwrap_and_check_conditions(
            coordinates, levels=[], target_levels=[], target_values=[]
        )
    return GenericMeasure(
        "LEVEL_AT",
        measure,
        levels,
        values,
        target_levels,
    )
