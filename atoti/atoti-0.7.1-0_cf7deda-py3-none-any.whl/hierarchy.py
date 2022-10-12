from dataclasses import dataclass, field
from typing import Mapping, Tuple

from atoti_core import (
    BaseHierarchy,
    Constant,
    ConstantValue,
    HierarchyCoordinates,
    keyword_only_dataclass,
)
from typeguard import typeguard_ignore

from ._hierarchy_isin_condition import HierarchyIsinCondition
from ._java_api import JavaApi
from ._level_arguments import LevelArguments
from .level import Level


@keyword_only_dataclass
@typeguard_ignore
@dataclass(eq=False)
class Hierarchy(BaseHierarchy[Level]):
    """Hierarchy of a :class:`atoti.Cube`.

    A hierarchy is a sub category of a :attr:`~dimension` and represents a precise type of data.

    For example, :guilabel:`Quarter` or :guilabel:`Week` could be hierarchies in the :guilabel:`Time` dimension.
    """

    _name: str
    _levels_arguments: Mapping[str, LevelArguments]
    _dimension: str
    _slicing: bool
    _cube_name: str
    _java_api: JavaApi = field(repr=False)
    _visible: bool
    _virtual: bool

    def __post_init__(self) -> None:
        self._levels: Mapping[str, Level] = {
            level_name: Level(
                _name=level_arguments[0],
                _hierarchy_coordinates=self._coordinates,
                _cube_name=self._cube_name,
                _java_api=self._java_api,
                _column_name=level_arguments[1].column_name,
                _table_name=level_arguments[1].table_name,
                _data_type=level_arguments[2],
                _order=level_arguments[3],
            )
            for level_name, level_arguments in self._levels_arguments.items()
        }

    @property
    def name(self) -> str:
        return self._name

    @property
    def levels(self) -> Mapping[str, Level]:
        return self._levels

    @property
    def virtual(self) -> bool:
        """
        Whether the hierarchy is virtual or not.

        A virtual hierarchy is a lightweight hierarchy which does not store in memory the list of its members.
        It is useful for hierarchies with large cardinality.
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual: bool, /) -> None:
        self._java_api.update_hierarchy_virtual(
            cube_name=self._cube_name,
            hierarchy_coordinates=self._coordinates,
            virtual=virtual,
        )
        self._java_api.refresh()
        self._virtual = virtual

    @property
    def dimension(self) -> str:
        return self._dimension

    @dimension.setter
    def dimension(self, value: str) -> None:
        """Dimension setter."""
        self._java_api.update_hierarchy_coordinate(
            cube_name=self._cube_name,
            hierarchy_coordinates=self._coordinates,
            new_dim=value,
            new_hierarchy=self._name,
        )
        self._java_api.refresh()
        self._dimension = value

    @property
    def slicing(self) -> bool:
        return self._slicing

    @slicing.setter
    def slicing(self, value: bool) -> None:
        """Slicing setter."""
        self._java_api.update_hierarchy_slicing(
            cube_name=self._cube_name,
            hierarchy_coordinates=self._coordinates,
            slicing=value,
        )
        self._java_api.refresh()
        self._slicing = value

    @property
    def visible(self) -> bool:
        """Whether the hierarchy is visible or not."""
        return self._visible

    @visible.setter
    def visible(self, value: bool) -> None:
        """Visibility setter."""
        self._java_api.set_hierarchy_visibility(
            cube_name=self._cube_name,
            dimension=self._dimension,
            name=self._name,
            visible=value,
        )
        self._java_api.refresh()
        self._visible = value

    def isin(self, *member_paths: Tuple[ConstantValue, ...]) -> HierarchyIsinCondition:
        return HierarchyIsinCondition(
            hierarchy_coordinates=HierarchyCoordinates(self.dimension, self.name),
            level_names=tuple(self.levels),
            member_paths=tuple(
                tuple(Constant(member) for member in member_path)
                for member_path in member_paths
            ),
        )
