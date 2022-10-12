from dataclasses import dataclass
from typing import Tuple

from .coordinates import Coordinates


@dataclass(frozen=True)
class HierarchyCoordinates(Coordinates):  # pylint: disable=keyword-only-dataclass
    dimension_name: str
    hierarchy_name: str

    @property
    def key(self) -> Tuple[str, str]:
        return self.dimension_name, self.hierarchy_name
