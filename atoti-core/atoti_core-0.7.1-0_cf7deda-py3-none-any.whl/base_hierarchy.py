from abc import abstractmethod
from dataclasses import dataclass
from typing import Generic, Mapping, Optional, Tuple, TypeVar

from .base_hierarchy_isin_condition import BaseHierarchyIsinCondition
from .base_level import BaseLevel
from .bitwise_operators_only import BitwiseOperatorsOnly
from .constant import Constant, ConstantValue
from .hierarchy_coordinates import HierarchyCoordinates
from .keyword_only_dataclass import keyword_only_dataclass
from .repr_json import ReprJson, ReprJsonable

LevelT = TypeVar("LevelT", bound=BaseLevel, covariant=True)


@keyword_only_dataclass
@dataclass(eq=False)
class BaseHierarchy(Generic[LevelT], ReprJsonable, BitwiseOperatorsOnly):
    """Hierarchy of a base cube."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the hierarchy."""

    @property
    @abstractmethod
    def dimension(self) -> str:
        """Name of the dimension of the hierarchy.

        A dimension is a logical group of attributes (e.g. :guilabel:`Geography`).
        It can be thought of as a folder containing hierarchies.
        """

    @property
    @abstractmethod
    def levels(self) -> Mapping[str, LevelT]:
        """Levels of the hierarchy."""

    @property
    @abstractmethod
    def slicing(self) -> bool:
        """Whether the hierarchy is slicing or not.

        * A regular (or non-slicing) hierarchy is considered aggregatable, meaning that it makes sense to aggregate data across all members of the hierarchy.

          For instance, for a :guilabel:`Geography` hierarchy, it is useful to see the worldwide aggregated :guilabel:`Turnover` across all countries.

        * A slicing hierarchy is not aggregatable at the top level, meaning that it does not make sense to aggregate data across all members of the hierarchy.

          For instance, for an :guilabel:`As of date` hierarchy giving the current bank account :guilabel:`Balance` for a given date, it does provide any meaningful information to aggregate the :guilabel:`Balance` across all the dates.
        """

    def isin(
        self, *member_paths: Tuple[ConstantValue, ...]
    ) -> BaseHierarchyIsinCondition:
        """Return a condition to check that the hierarchy is on one of the given members.

        Considering ``hierarchy_1`` containing ``level_1`` and ``level_2``, ``hierarchy_1.isin((a,), (b, x))`` is equivalent to ``(level_1 == a) | ((level_1 == b) & (level_2 == x))``.

        Args:
            members: One or more members expressed as tuples on which the hierarchy should be.
                Each element in a tuple corresponds to a level of the hierarchy, from the shallowest to the deepest.

        Example:
            .. doctest:: Hierarchy.isin

                >>> df = pd.DataFrame(
                ...     columns=["Country", "City", "Price"],
                ...     data=[
                ...         ("Germany", "Berlin", 150.0),
                ...         ("Germany", "Hamburg", 120.0),
                ...         ("United Kingdom", "London", 240.0),
                ...         ("United States", "New York", 270.0),
                ...         ("France", "Paris", 200.0),
                ...     ],
                ... )
                >>> table = session.read_pandas(
                ...     df, keys=["Country", "City"], table_name="isin example"
                ... )
                >>> cube = session.create_cube(table)
                >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
                >>> h["Geography"] = [l["Country"], l["City"]]
                >>> m["Price.SUM in Germany and Paris"] = tt.filter(
                ...     m["Price.SUM"],
                ...     h["Geography"].isin(("Germany",), ("France", "Paris")),
                ... )
                >>> cube.query(
                ...     m["Price.SUM"],
                ...     m["Price.SUM in Germany and Paris"],
                ...     levels=[l["Geography", "City"]],
                ... )
                                        Price.SUM Price.SUM in Germany and Paris
                Country        City
                France         Paris       200.00                         200.00
                Germany        Berlin      150.00                         150.00
                               Hamburg     120.00                         120.00
                United Kingdom London      240.00
                United States  New York    270.00

            .. doctest:: Hierarchy.isin
                :hide:

                Clear the session to isolate the multiple methods sharing this docstring.
                >>> session._clear()
        """
        return BaseHierarchyIsinCondition(
            hierarchy_coordinates=HierarchyCoordinates(self.dimension, self.name),
            level_names=(*self.levels,),
            member_paths=tuple(
                tuple(Constant(member) for member in member_path)
                for member_path in member_paths
            ),
        )

    def _repr_json_(self) -> ReprJson:
        """Return the JSON representation of a hierarchy."""
        root = f"{self.name}{' (slicing)' if self.slicing else ''}"
        return (
            [level.name for level in self.levels.values()],
            {
                "root": root,
                "expanded": False,
            },
        )

    @property
    def _coordinates(self) -> HierarchyCoordinates:
        return HierarchyCoordinates(self.dimension, self.name)

    @property
    def _bool_alternative_message(self) -> Optional[str]:  # pylint: disable=no-self-use
        return "For conditions on hierarchy members use the `isin` method."

    # This is needed otherwise errors like "TypeError: unhashable type: 'Hierarchy'" are thrown.
    # This is a "eq=False" dataclass so hash method is generated "according to how eq" is set but
    # the desired behavior is to use BitwiseOperatorsOnly.__hash__().
    def __hash__(self) -> int:  # pylint: disable=useless-super-delegation, no-self-use
        return super().__hash__()


BaseHierarchyBound = BaseHierarchy[BaseLevel]
