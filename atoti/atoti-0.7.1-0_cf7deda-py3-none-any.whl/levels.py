from typing import Optional

from atoti_core import BaseLevels, LevelKey

from ._exceptions import AtotiJavaException
from .hierarchies import Hierarchies
from .level import Level


class Levels(BaseLevels[Hierarchies, Level]):
    """Flat representation of all the levels in the cube."""

    def __delitem__(self, key: LevelKey) -> None:
        """Delete a level.

        Args:
            key: The name of the level to delete, or a ``(hierarchy_name, level_name)`` tuple.
        """
        if key not in self:
            raise KeyError(f"{key} is not an existing level.")
        level = self[key]
        level._java_api.delete_level(level._coordinates, cube_name=level._cube_name)
        level._java_api.refresh()

    def _find_level(
        self,
        level_name: str,
        *,
        dimension_name: Optional[str] = None,
        hierarchy_name: Optional[str] = None,
    ) -> Level:
        """Get a level from the hierarchy name and level name."""
        try:
            hierarchy_argument = self._hierarchies._java_api.find_level_hierarchy(
                level_name,
                cube_name=self._hierarchies._cube_name,
                dimension_name=dimension_name,
                hierarchy_name=hierarchy_name,
            )
        except AtotiJavaException as exception:
            raise KeyError(str(exception)) from None
        hierarchy = self._hierarchies._create_hierarchy_from_arguments(
            hierarchy_argument
        )
        return hierarchy.levels[level_name]
