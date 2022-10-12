from __future__ import annotations

from typing import Dict, Optional

from ..._local_session import LocalSession
from ...config._session_config import SessionConfig
from .cube import DistributedCube
from .cubes import DistributedCubes


class DistributedSession(LocalSession[DistributedCubes]):
    """Holds a connection to the Java gateway."""

    def __init__(
        self,
        *,
        config: Optional[SessionConfig] = None,
    ):
        """Create the session and the Java gateway."""
        super().__init__(config=config or SessionConfig(), distributed=True)
        self._cubes = DistributedCubes(
            _delete_cube=self._java_api.delete_cube,
            _get_cube=self._get_cube,
            _get_cubes=self._get_cubes,
        )

    def __enter__(self) -> DistributedSession:
        return self

    @property
    def cubes(self) -> DistributedCubes:
        """Cubes of the session."""
        return self._cubes

    def create_cube(self, name: str) -> DistributedCube:
        """Create a distributed cube.

        Args:
            name: The name of the created cube.
        """
        self._java_api.create_distributed_cube(name)
        self._java_api.java_api.refresh()
        return DistributedCube(
            java_api=self._java_api,
            name=name,
            session_name=self.name,
            query_mdx=self.query_mdx,
            execute_gaq=self._create_query_session()._execute_gaq,
        )

    def _get_cube(self, cube_name: str) -> DistributedCube:
        java_cube = self._java_api.get_cube(cube_name)
        return DistributedCube(
            java_api=self._java_api,
            name=java_cube.name(),
            session_name=self.name,
            query_mdx=self.query_mdx,
            execute_gaq=self._create_query_session()._execute_gaq,
        )

    def _get_cubes(self) -> Dict[str, DistributedCube]:
        return {
            java_cube.name(): DistributedCube(
                java_api=self._java_api,
                name=java_cube.name(),
                session_name=self.name,
                query_mdx=self.query_mdx,
                execute_gaq=self._create_query_session()._execute_gaq,
            )
            for java_cube in self._java_api.get_cubes()
        }
