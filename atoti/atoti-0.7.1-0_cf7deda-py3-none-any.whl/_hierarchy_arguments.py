from dataclasses import dataclass
from typing import Mapping

from atoti_core import HierarchyCoordinates, keyword_only_dataclass

from ._level_arguments import LevelArguments


@keyword_only_dataclass
@dataclass(frozen=True)
class HierarchyArguments:
    name: str
    levels_arguments: Mapping[str, LevelArguments]
    dimension: str
    slicing: bool
    visible: bool
    virtual: bool

    def get_coordinates(self) -> HierarchyCoordinates:
        return HierarchyCoordinates(self.dimension, self.name)
