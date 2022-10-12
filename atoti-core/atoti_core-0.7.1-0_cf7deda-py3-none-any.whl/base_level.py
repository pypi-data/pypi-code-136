from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, NoReturn, Optional

from .base_level_condition import BaseLevelCondition
from .base_level_isin_condition import BaseLevelIsinCondition
from .bitwise_operators_only import BitwiseOperatorsOnly
from .constant import Constant, ConstantValue
from .keyword_only_dataclass import keyword_only_dataclass
from .level_coordinates import LevelCoordinates
from .repr_json import ReprJson, ReprJsonable


@keyword_only_dataclass
@dataclass(eq=False)
class BaseLevel(ReprJsonable, BitwiseOperatorsOnly):
    """Level of a base cube."""

    _name: str

    @property
    def name(self) -> str:
        """Name of the level."""
        return self._name

    @property
    @abstractmethod
    def dimension(self) -> str:
        """Name of the dimension holding the level."""

    @property
    @abstractmethod
    def hierarchy(self) -> str:
        """Name of the hierarchy holding the level."""

    @property
    def _coordinates(self) -> LevelCoordinates:
        return LevelCoordinates(self.dimension, self.hierarchy, self._name)

    def isin(self, *members: ConstantValue) -> BaseLevelIsinCondition:
        """Return a condition to check that the level is on one of the given members.

        ``level.isin(a, b)`` is equivalent to ``(level == a) | (level == b)``.

        Args:
            members: One or more members on which the level should be.

        Example:
            .. doctest:: Level.isin

                >>> df = pd.DataFrame(
                ...     columns=["City", "Price"],
                ...     data=[
                ...         ("Berlin", 150.0),
                ...         ("London", 240.0),
                ...         ("New York", 270.0),
                ...         ("Paris", 200.0),
                ...     ],
                ... )
                >>> table = session.read_pandas(
                ...     df, keys=["City"], table_name="isin example"
                ... )
                >>> cube = session.create_cube(table)
                >>> l, m = cube.levels, cube.measures
                >>> m["Price.SUM in London and Paris"] = tt.filter(
                ...     m["Price.SUM"], l["City"].isin("London", "Paris")
                ... )
                >>> cube.query(
                ...     m["Price.SUM"],
                ...     m["Price.SUM in London and Paris"],
                ...     levels=[l["City"]],
                ... )
                         Price.SUM Price.SUM in London and Paris
                City
                Berlin      150.00
                London      240.00                        240.00
                New York    270.00
                Paris       200.00                        200.00

            .. doctest:: Level.isin
                :hide:

                Clear the session to isolate the multiple methods sharing this docstring.
                >>> session._clear()

        """
        return BaseLevelIsinCondition(
            level_coordinates=self._coordinates,
            members=tuple(Constant(member) for member in members),
        )

    def isnull(self) -> BaseLevelCondition:
        """Return a condition evaluating to ``True`` when a level is not expressed in a query and ``False`` otherwise.

        Use `~level.isnull()` for the opposite behavior.

        Example:

            >>> df = pd.DataFrame(
            ...     columns=["Country", "City", "Price"],
            ...     data=[
            ...         ("France", "Paris", 200.0),
            ...         ("Germany", "Berlin", 120),
            ...     ],
            ... )
            >>> table = session.read_pandas(df, table_name="isnull example")
            >>> cube = session.create_cube(table)
            >>> l, m = cube.levels, cube.measures
            >>> m["City.isnull"] = l["City"].isnull()
            >>> m["City.notnull"] = ~l["City"].isnull()
            >>> cube.query(
            ...     m["City.isnull"],
            ...     m["City.notnull"],
            ...     levels=[l["Country"], l["City"]],
            ...     include_totals=True,
            ... )
                           City.isnull City.notnull
            Country City
            Total                 True        False
            France                True        False
                    Paris        False         True
            Germany               True        False
                    Berlin       False         True

        """
        return BaseLevelCondition(
            level_coordinates=self._coordinates, operator="eq", value=None
        )

    @abstractmethod
    def _repr_json_(self) -> ReprJson:
        """JSON representation of the level."""

    def __eq__(self, other: Any) -> BaseLevelCondition:  # type: ignore[override]
        return BaseLevelCondition(
            level_coordinates=self._coordinates, operator="eq", value=other
        )

    def __ne__(self, other: Any) -> NoReturn:
        # Explicitly implemented so that Python doesn't just silently return False.
        raise NotImplementedError(
            "Base level conditions can only be based on equality (==)."
        )

    # This is needed otherwise errors like "TypeError: unhashable type: 'QueryLevel'" are thrown.
    # This is a "eq=False" dataclass so hash method is generated "according to how eq" is set but
    # the desired behavior is to use BitwiseOperatorsOnly.__hash__().
    def __hash__(self) -> int:  # pylint: disable=useless-super-delegation, no-self-use
        return super().__hash__()

    @property
    def _bool_alternative_message(self) -> Optional[str]:  # pylint: disable=no-self-use
        return "For conditions on level members use `isin`, `where` or `filter` method."
