from dataclasses import dataclass
from typing import Any

from atoti_core import (
    BaseLevel,
    ColumnCoordinates,
    Constant,
    ConstantValue,
    HierarchyCoordinates,
    ReprJson,
    deprecated,
    keyword_only_dataclass,
)
from typeguard import typeguard_ignore

from ._java_api import JavaApi
from ._level_condition import LevelCondition
from ._level_isin_condition import LevelIsinCondition
from ._measures.level_measure import LevelMeasure
from ._warn_about_required_levels import warn_about_required_levels
from .measure_description import MeasureConvertible, MeasureDescription
from .order import NaturalOrder
from .order._order import Order
from .type import DataType


@keyword_only_dataclass
@typeguard_ignore
@dataclass(eq=False)
class Level(BaseLevel, MeasureConvertible):
    """Level of a :class:`atoti.Hierarchy`.

    A level is a sub category of a hierarchy.
    Levels have a specific order with a parent-child relationship.

    In a :guilabel:`Pivot Table`, a single-level hierarchy will be displayed as a flat attribute while a multi-level hierarchy will display the first level and allow users to expand each member against the next level and display sub totals.

    For example, a :guilabel:`Geography` hierarchy can have a :guilabel:`Continent` as the top level where :guilabel:`Continent` expands to :guilabel:`Country` which in turns expands to the leaf level: :guilabel:`City`.
    """

    _table_name: str
    _column_name: str
    _data_type: DataType
    _hierarchy_coordinates: HierarchyCoordinates
    _cube_name: str
    _java_api: JavaApi
    _order: Order = NaturalOrder()

    @property
    def dimension(self) -> str:
        """Name of the dimension holding the level."""
        return self._hierarchy_coordinates.dimension_name

    @property
    def hierarchy(self) -> str:
        """Name of the hierarchy holding the level."""
        return self._hierarchy_coordinates.hierarchy_name

    @property
    def data_type(self) -> DataType:
        """Type of the level members."""
        return self._data_type

    @property
    def _column_coordinates(self) -> ColumnCoordinates:
        return ColumnCoordinates(
            table_name=self._table_name, column_name=self._column_name
        )

    @property
    def order(self) -> Order:
        """Order in which to sort the level's members.

        Defaults to ascending :class:`atoti.NaturalOrder`.
        """
        return self._order

    @order.setter
    def order(self, value: Order) -> None:
        self._java_api.update_level_order(
            value,
            cube_name=self._cube_name,
            level_coordinates=self._coordinates,
        )
        self._java_api.refresh()
        self._order = value

    @property
    def _measure_description(self) -> MeasureDescription:

        warn_about_required_levels(origin_scope_levels=f"the level {self._coordinates}")

        return LevelMeasure(self._coordinates)

    def _repr_json_(self) -> ReprJson:
        data = {
            "dimension": self.dimension,
            "hierarchy": self.hierarchy,
            "type": str(self.data_type),
            "order": self.order._key,
        }
        return (data, {"expanded": True, "root": self.name})

    def isin(self, *members: ConstantValue) -> LevelIsinCondition:
        return LevelIsinCondition(
            level_coordinates=self._coordinates,
            members=tuple(Constant(member) for member in members),
        )

    def isnull(self) -> LevelCondition:
        return LevelCondition(
            level_coordinates=self._coordinates, operator="eq", value=None
        )

    def __eq__(self, other: Any) -> LevelCondition:  # type: ignore[override]
        if isinstance(other, MeasureDescription):
            return NotImplemented
        if other is None:
            deprecated(
                "Comparison with `None` is deprecated, use `level.isnull()` instead."
            )
        return LevelCondition(
            level_coordinates=self._coordinates, operator="eq", value=other
        )

    def __ne__(self, other: Any) -> LevelCondition:  # type: ignore[override]
        if isinstance(other, MeasureDescription):
            return NotImplemented
        if other is None:
            deprecated(
                "Comparison with `None` is deprecated, use `~level.isnull()` instead."
            )
        return LevelCondition(
            level_coordinates=self._coordinates, operator="ne", value=other
        )

    def __lt__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="lt", value=other
        )

    def __le__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="le", value=other
        )

    def __gt__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="gt", value=other
        )

    def __ge__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="ge", value=other
        )

    # This is needed otherwise errors like "TypeError: unhashable type: 'Level'" are thrown.
    # This is a "eq=False" dataclass so hash method is generated "according to how eq" is set but
    # the desired behavior is to use BitwiseOperatorsOnly.__hash__().
    def __hash__(self) -> int:  # pylint: disable=useless-super-delegation, no-self-use
        return super().__hash__()
