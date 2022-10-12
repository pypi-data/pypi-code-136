from dataclasses import dataclass
from typing import Dict, Iterable, Optional, Tuple, Union

from atoti_core import HierarchyKey, keyword_only_dataclass
from atoti_query import QueryHierarchy
from typeguard import typechecked, typeguard_ignore

from atoti._exceptions import AtotiJavaException

from ..._local_hierarchies import LocalHierarchies
from ...column import Column
from ...level import Level

LevelOrColumn = Union[Level, Column]


@keyword_only_dataclass
@typeguard_ignore
@dataclass(frozen=True)
class DistributedHierarchies(
    LocalHierarchies[QueryHierarchy],
):
    """Manage the hierarchies."""

    _cube_name: str

    def _get_underlying(self) -> Dict[Tuple[str, str], QueryHierarchy]:
        hierarchies = {
            coordinates: self._create_hierarchy_from_arguments(description)
            for coordinates, description in self._java_api.get_hierarchies(
                cube_name=self._cube_name,
            ).items()
        }
        return {
            hierarchyCoordinate: hierarchies[hierarchyCoordinate]  # type: ignore
            for hierarchyCoordinate in hierarchies
        }

    @typechecked
    def __getitem__(self, key: HierarchyKey) -> QueryHierarchy:
        (dimension_name, hierarchy_name) = self._convert_key(key)
        try:
            hierarchy_argument = self._java_api.get_hierarchy(
                hierarchy_name,
                cube_name=self._cube_name,
                dimension_name=dimension_name,
            )
        except AtotiJavaException as exception:
            raise KeyError(str(exception)) from None
        return self._create_hierarchy_from_arguments(hierarchy_argument)

    def _delete_keys(self, keys: Optional[Iterable[Tuple[str, str]]] = None, /) -> None:
        raise NotImplementedError("Distributed cube hierarchies cannot be changed")
