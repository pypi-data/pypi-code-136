from dataclasses import dataclass
from typing import Tuple

from .coordinates import Coordinates


@dataclass(frozen=True)
class ColumnCoordinates(Coordinates):  # pylint: disable=keyword-only-dataclass
    table_name: str
    column_name: str

    @property
    def key(self) -> Tuple[str, str]:
        return self.table_name, self.column_name
