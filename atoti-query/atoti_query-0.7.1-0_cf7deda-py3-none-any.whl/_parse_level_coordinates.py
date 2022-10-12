import re
from typing import Optional

from atoti_core import LevelCoordinates

_LEVEL_UNIQUE_NAME_PATTERN = re.compile(
    r"^\[(?P<dimension>.*)\]\.\[(?P<hierarchy>.*)\]\.\[(?P<level>.*)\]$"
)


def parse_level_coordinates(
    level_unique_name: str,
) -> Optional[LevelCoordinates]:
    match = _LEVEL_UNIQUE_NAME_PATTERN.match(level_unique_name)

    return (
        LevelCoordinates(
            match.group("dimension"),
            match.group("hierarchy"),
            match.group("level"),
        )
        if match
        else None
    )
