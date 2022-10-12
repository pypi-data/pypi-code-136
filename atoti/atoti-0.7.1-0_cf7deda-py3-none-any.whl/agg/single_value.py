from typing import Optional, Union, cast, overload

from atoti_core import doc

from ..column import Column
from ..measure_description import MeasureDescription
from ..scope._scope import Scope
from ._agg import agg
from ._utils import SCOPE_DOC


@overload
def single_value(operand: Column, /) -> MeasureDescription:
    ...


@overload
def single_value(operand: MeasureDescription, /, *, scope: Scope) -> MeasureDescription:
    ...


@doc(scope=SCOPE_DOC)
def single_value(
    operand: Union[Column, MeasureDescription],
    /,
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return a measure equal to the value aggregation of the operand across the specified scope.

    If the value is the same for all members of the level the operand is being aggregated on, it will be propagated to the next level.

    ``None`` values are ignored: they will not prevent the propagation.

    Args:
        operand: The measure or table column to aggregate.
        {scope}

    Example:
        >>> df = pd.DataFrame(
        ...     columns=["Continent", "Country", "City", "Price"],
        ...     data=[
        ...         ("Europe", "France", "Paris", 200.0),
        ...         ("Europe", "France", "Lyon", 200.0),
        ...         ("Europe", "UK", "London", 200.0),
        ...         ("Europe", "UK", "Manchester", 150.0),
        ...         ("Europe", "France", "Bordeaux", None),
        ...     ],
        ... )
        >>> table = session.read_pandas(
        ...     df, table_name="City price table", keys=["Continent", "Country", "City"]
        ... )
        >>> cube = session.create_cube(table)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> geography_level_names = ["Continent", "Country", "City"]
        >>> h["Geography"] = [table[name] for name in geography_level_names]
        >>> for name in geography_level_names:
        ...     del l[name, name]
        ...
        >>> m["Price.VALUE"] = tt.agg.single_value(table["Price"])
        >>> cube.query(
        ...     m["Price.VALUE"],
        ...     m["contributors.COUNT"],
        ...     levels=[l["City"]],
        ...     include_totals=True,
        ... )
                                     Price.VALUE contributors.COUNT
        Continent Country City
        Total                                                     5
        Europe                                                    5
                  France                  200.00                  3
                          Bordeaux                                1
                          Lyon            200.00                  1
                          Paris           200.00                  1
                  UK                                              2
                          London          200.00                  1
                          Manchester      150.00                  1

        * The :guilabel:`City` level is the most granular level so the members have the same value as in the input dataframe (including ``None`` for Bordeaux).
        * All the cities in France have the same price or ``None`` so the value is propagated to the :guilabel:`Country` level.
          The values in the UK cities are different so :guilabel:`Price.VALUE` is ``None``.
        * The cities in Europe have different values so the :guilabel:`Price.VALUE` is ``None`` at the :guilabel:`Continent` level.

    """
    # The type checkers cannot see that the `@overload` above ensure that this call is valid.
    return cast(MeasureDescription, agg(operand, plugin_key="SINGLE_VALUE_NULLABLE", scope=scope))  # type: ignore
