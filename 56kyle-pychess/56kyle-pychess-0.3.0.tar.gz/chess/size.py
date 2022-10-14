
from dataclasses import dataclass, field

from chess.position import Position


@dataclass(frozen=True)
class Size:
    width: int
    height: int



