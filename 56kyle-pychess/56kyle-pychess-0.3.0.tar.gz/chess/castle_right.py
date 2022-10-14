
from dataclasses import dataclass

from chess.color import Color
from chess.position import Position
from chess.side import Side


@dataclass(frozen=True)
class CastleRight:
    color: Color
    rook_origin: Position
    rook_destination: Position
    king_origin: Position
    king_destination: Position



