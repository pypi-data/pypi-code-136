
from typing import Set

from chess.path import Path


class PieceMeta:
    name: str
    letter: str
    value: int
    symbol: str
    html_decimal: str
    html_hex: str

    move_paths: Set[Path] = set()
    capture_paths: Set[Path] = set()
    en_passant_paths: Set[Path] = set()
    castle_paths: Set[Path] = set()


