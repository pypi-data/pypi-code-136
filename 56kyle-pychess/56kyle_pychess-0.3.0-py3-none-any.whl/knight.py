
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.move import Move
from chess.offset import Offset, UP, RIGHT, DOWN, LEFT, UP_RIGHT, DOWN_RIGHT, DOWN_LEFT, UP_LEFT
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta


class KnightMeta(PieceMeta):
    name: str = 'Knight'
    letter: str = 'N'
    value: int = 3
    symbol: str = '\u2658'
    html_decimal: str = '&#9822;'
    html_hex: str = '&#x2658;'
    offsets: Set[Offset] = {
        UP * 2 + RIGHT,
        UP * 2 + LEFT,
        DOWN * 2 + RIGHT,
        DOWN * 2 + LEFT,
        RIGHT * 2 + UP,
        RIGHT * 2 + DOWN,
        LEFT * 2 + UP,
        LEFT * 2 + DOWN,
    }
    move_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in offsets}
    capture_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in offsets}


@dataclass(frozen=True)
class Knight(Piece):
    meta: KnightMeta = KnightMeta


