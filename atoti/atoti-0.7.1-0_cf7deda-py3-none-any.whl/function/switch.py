from __future__ import annotations

from functools import reduce
from typing import Dict, Mapping, Optional, Tuple, Union

from atoti_core import ConstantValue

from .._condition import Condition
from ..level import Level
from ..measure import Measure
from ..measure_description import MeasureConvertible, MeasureDescription, MeasureLike
from .where import where


def switch(
    subject: MeasureConvertible,
    cases: Mapping[
        Union[Optional[ConstantValue], Tuple[Optional[ConstantValue], ...]],
        MeasureLike,
    ],
    /,
    *,
    default: Optional[MeasureLike] = None,
) -> MeasureDescription:
    """Return a measure equal to the value of the first case for which *subject* is equal to the case's key.

    *cases*'s values and *default* must either be all numerical, all boolean or all objects.

    Args:
        subject: The measure or level to compare to *cases*' keys.
        cases: A mapping from keys to compare with *subject* to the values to return if the comparison is ``True``.
        default: The measure to use when none of the *cases* matched.

    Example:
        >>> df = pd.DataFrame(
        ...     columns=["Id", "City", "Value"],
        ...     data=[
        ...         (0, "Paris", 1.0),
        ...         (1, "Paris", 2.0),
        ...         (2, "London", 3.0),
        ...         (3, "London", 4.0),
        ...         (4, "Paris", 5.0),
        ...         (5, "Singapore", 7.0),
        ...         (6, "NYC", 2.0),
        ...     ],
        ... )
        >>> table = session.read_pandas(df, keys=["Id"], table_name="Switch example")
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Continent"] = tt.switch(
        ...     l["City"],
        ...     {
        ...         ("Paris", "London"): "Europe",
        ...         "Singapore": "Asia",
        ...         "NYC": "North America",
        ...     },
        ... )
        >>> cube.query(m["Continent"], levels=[l["City"]])
                       Continent
        City
        London            Europe
        NYC        North America
        Paris             Europe
        Singapore           Asia
        >>> m["Europe & Asia value"] = tt.agg.sum(
        ...     tt.switch(
        ...         m["Continent"], {("Europe", "Asia"): m["Value.SUM"]}, default=0.0
        ...     ),
        ...     scope=tt.OriginScope(l["Id"], l["City"]),
        ... )
        >>> cube.query(m["Europe & Asia value"], levels=[l["City"]])
                  Europe & Asia value
        City
        London                   7.00
        NYC                       .00
        Paris                    8.00
        Singapore                7.00
        >>> cube.query(m["Europe & Asia value"])
          Europe & Asia value
        0               22.00

    See also:
        :func:`atoti.where`.
    """
    condition_to_measure: Dict[
        Union[
            Condition,
            Measure,
        ],
        MeasureLike,
    ] = {}
    for values, measure in cases.items():
        if isinstance(values, tuple):
            condition_to_measure[
                reduce(
                    lambda a, b: a | b,
                    [
                        _create_eq_condition(subject=subject, value=value)
                        for value in values
                    ],
                )
            ] = measure
        else:
            condition_to_measure[
                _create_eq_condition(subject=subject, value=values)
            ] = measure
    return where(condition_to_measure, default=default)


def _create_eq_condition(
    *,
    subject: Union[MeasureDescription, MeasureConvertible],
    value: Optional[ConstantValue],
) -> Condition:
    return (
        subject.isnull()
        if isinstance(subject, (Level, MeasureDescription)) and value is None
        else subject == value
    )
