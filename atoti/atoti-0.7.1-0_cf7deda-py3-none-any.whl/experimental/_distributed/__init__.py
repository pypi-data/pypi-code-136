"""
atoti supports distributed clusters with several data cubes and one query cube.

This is not the same as a query session: in a query session, the query cube connects to a remote data cube and query its content, while in a distributed setup, multiple data cubes can join a distributed cluster where a distributed cube can be queried to retrieve the union of their data.
"""

from __future__ import annotations

from ...cube import Cube
from .cube import *
from .session import *


def join_distributed_cluster(
    *,
    cube: Cube,
    distributed_session_url: str,
    distributed_cube_name: str,
) -> None:
    """Join the distributed cluster at the given address for the given distributed cube."""
    cube._join_distributed_cluster(distributed_session_url, distributed_cube_name)
