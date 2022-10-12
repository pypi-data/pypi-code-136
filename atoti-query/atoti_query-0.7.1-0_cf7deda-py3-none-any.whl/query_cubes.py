from atoti_core import BaseCubes, ImmutableMapping

from .query_cube import QueryCube


class QueryCubes(ImmutableMapping[str, QueryCube], BaseCubes[QueryCube]):
    """Manage the query cubes."""
