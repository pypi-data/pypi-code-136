from typing import Iterable, Mapping, Protocol

from atoti_core import DataType, LevelCoordinates


class GetLevelDataTypes(Protocol):
    def __call__(
        self, levels_coordinates: Iterable[LevelCoordinates], /, *, cube_name: str
    ) -> Mapping[LevelCoordinates, DataType]:
        ...
