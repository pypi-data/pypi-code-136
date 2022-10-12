from dataclasses import dataclass
from typing import Tuple

from .coordinates import Coordinates


@dataclass(frozen=True)
class LevelCoordinates(Coordinates):  # pylint: disable=keyword-only-dataclass
    dimension_name: str
    hierarchy_name: str
    level_name: str

    @property
    def key(self) -> Tuple[str, str, str]:
        return self.dimension_name, self.hierarchy_name, self.level_name
