from __future__ import annotations

from typing import Optional

from atoti_core import ImmutableMapping

from ._discovery import Discovery, DiscoveryCube, DiscoveryHierarchy
from ._execute_gaq import _ExecuteGaq
from ._query_mdx import _QueryMdx
from .query_cube import QueryCube
from .query_cubes import QueryCubes
from .query_hierarchies import QueryHierarchies
from .query_hierarchy import QueryHierarchy
from .query_level import QueryLevel
from .query_measure import QueryMeasure
from .query_measures import QueryMeasures


def _create_hierarchy(
    dimension_name: str, discovery_hierarchy: DiscoveryHierarchy
) -> QueryHierarchy:
    levels = ImmutableMapping(
        {
            level["name"]: QueryLevel(
                _name=level["name"],
                _dimension=dimension_name,
                _hierarchy=discovery_hierarchy["name"],
            )
            for level in discovery_hierarchy["levels"]
            if level["type"] != "ALL"
        }
    )
    return QueryHierarchy(
        _name=discovery_hierarchy["name"],
        _dimension=dimension_name,
        _levels=levels,
        _slicing=discovery_hierarchy["slicing"],
    )


def _create_cube(
    discovery_cube: DiscoveryCube,
    *,
    execute_gaq: Optional[_ExecuteGaq] = None,
    query_mdx: _QueryMdx,
) -> QueryCube:
    hierarchies = QueryHierarchies(
        {
            (dimension["name"], hierarchy["name"]): _create_hierarchy(
                dimension["name"], hierarchy
            )
            for dimension in discovery_cube["dimensions"]
            if dimension["name"] != "Epoch"
            for hierarchy in dimension["hierarchies"]
        }
    )
    measures = QueryMeasures(
        {
            measure["name"]: QueryMeasure(
                _name=measure["name"],
                _visible=measure["visible"],
                _folder=measure.get("folder"),
                _formatter=measure.get("formatString"),
                _description=measure.get("description"),
            )
            for measure in discovery_cube["measures"]
        }
    )
    return QueryCube(
        _name=discovery_cube["name"],
        _hierarchies=hierarchies,
        _measures=measures,
        _execute_gaq=execute_gaq,
        _query_mdx=query_mdx,
    )


def create_query_cubes_from_discovery(
    discovery: Discovery,
    *,
    execute_gaq: Optional[_ExecuteGaq] = None,
    query_mdx: _QueryMdx,
) -> QueryCubes:
    return QueryCubes(
        {
            cube["name"]: _create_cube(
                cube, execute_gaq=execute_gaq, query_mdx=query_mdx
            )
            for catalog in discovery["catalogs"]
            for cube in catalog["cubes"]
        }
    )
