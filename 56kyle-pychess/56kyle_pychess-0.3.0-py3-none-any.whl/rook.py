
from dataclasses import dataclass, field
from typing import TypeVar, Set

from chess.offset import LINEAR
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta


class RookMeta(PieceMeta):
    name: str = 'Rook'
    letter: str = 'R'
    value: int = 5
    symbol: str = '♜'
    html_decimal: str = '&#9820;'
    html_hex: str = '&#x265C;'

    move_paths: Set[Path] = {Path(offset=offset, max_steps=None) for offset in LINEAR}
    capture_paths: Set[Path] = {Path(offset=offset, max_steps=None) for offset in LINEAR}


@dataclass(frozen=True)
class Rook(Piece):
    meta: RookMeta = RookMeta



