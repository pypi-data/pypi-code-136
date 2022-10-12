from typing import Dict, Iterable, Optional

from atoti_core import DataType, LevelCoordinates
from atoti_query import QueryHierarchy, QueryLevel, _ExecuteGaq, _QueryMdx
from typeguard import typeguard_ignore

from ..._hierarchy_arguments import HierarchyArguments
from ..._java_api import JavaApi
from ..._local_cube import LocalCube
from ...aggregates_cache import AggregatesCache
from .hierarchies import DistributedHierarchies
from .levels import DistributedLevels
from .measures import DistributedMeasures


class DistributedCube(
    LocalCube[DistributedHierarchies, DistributedLevels, DistributedMeasures]
):
    """Cube of a distributed session."""

    @typeguard_ignore
    def __init__(
        self,
        name: str,
        *,
        java_api: JavaApi,
        session_name: Optional[str],
        query_mdx: _QueryMdx,
        execute_gaq: _ExecuteGaq
    ):
        super().__init__(
            name=name,
            java_api=java_api,
            session_name=session_name,
            hierarchies=DistributedHierarchies(
                _java_api=java_api,
                _cube_name=name,
                _create_hierarchy_from_arguments=self._create_hierarchy_from_arguments,
            ),
            level_function=lambda hierarchies: DistributedLevels(hierarchies),
            measures=DistributedMeasures(_java_api=java_api, _cube_name=name),
            agg_cache=AggregatesCache(
                _cube_name=name,
                _set_capacity=java_api.set_aggregates_cache_capacity,
                _get_capacity=java_api.get_aggregates_cache_capacity,
            ),
            query_mdx=query_mdx,
            execute_gaq=execute_gaq,
        )

    def _get_level_data_types(  # pylint: disable=no-self-use
        self, levels_coordinates: Iterable[LevelCoordinates]
    ) -> Dict[LevelCoordinates, DataType]:
        return {level_coordinates: "Object" for level_coordinates in levels_coordinates}

    def _create_hierarchy_from_arguments(
        self, arguments: HierarchyArguments
    ) -> QueryHierarchy:
        hierarchy = QueryHierarchy(
            _name=arguments.name,
            _levels={
                level_name: QueryLevel(
                    _name=level_name,
                    _dimension=arguments.dimension,
                    _hierarchy=arguments.name,
                )
                for level_name in arguments.levels_arguments
                if level_name != "ALL"
            },
            _dimension=arguments.dimension,
            _slicing=arguments.slicing,
        )
        return hierarchy
