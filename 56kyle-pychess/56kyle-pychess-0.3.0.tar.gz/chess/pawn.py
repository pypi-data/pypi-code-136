from dataclasses import dataclass
from typing import Set

from chess.offset import VERTICAL, DIAGONAL
from chess.path import Path
from chess.piece import Piece
from chess.piece_meta import PieceMeta


class PawnMeta(PieceMeta):
    name: str = 'Pawn'
    letter: str = 'P'
    value: int = 1
    symbol: str = '\u2659'
    html_decimal: str = '&#9817;'
    html_hex: str = '&#x2659;'

    move_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in VERTICAL}
    capture_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in DIAGONAL}
    en_passant_paths: Set[Path] = {Path(offset=offset, max_steps=1) for offset in DIAGONAL}


@dataclass(frozen=True)
class Pawn(Piece):
    meta: PawnMeta = PawnMeta


