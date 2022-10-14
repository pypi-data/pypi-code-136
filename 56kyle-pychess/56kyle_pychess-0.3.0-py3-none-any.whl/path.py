
from dataclasses import dataclass
from typing import Set

from chess.offset import Offset
from chess.size import Size


@dataclass(frozen=True)
class Path:
    offset: Offset
    max_steps: int | None = None



