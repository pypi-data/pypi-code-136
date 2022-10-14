from dataclasses import dataclass, field, replace, make_dataclass
from typing import Set, Type

from chess.color import Color
from chess.piece_meta import PieceMeta
from chess.position import Position


@dataclass(frozen=True)
class Piece:
    position: Position
    color: Color
    meta: PieceMeta = PieceMeta
    has_moved: bool = False

    def move(self, position: Position) -> 'Piece':
        return replace(self, position=position, has_moved=True)

    def promote(self, promotion: Type['Piece']) -> 'Piece':
        return replace(self, meta=promotion.meta)


