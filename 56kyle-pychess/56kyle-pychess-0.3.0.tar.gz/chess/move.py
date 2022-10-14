

from dataclasses import dataclass, field
from typing import Set, Type

from chess.position import Position
from chess.piece import Piece


@dataclass(frozen=True)
class Move:
    piece: Piece
    origin: Position
    destination: Position
    captures: Set[Piece] = field(default_factory=set)
    promotion: Type[Piece] | None = None

