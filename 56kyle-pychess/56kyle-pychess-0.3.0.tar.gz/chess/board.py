
from typing import Set, Dict, Type

from chess.bishop import Bishop
from chess.castle_right import CastleRight
from chess.color import Color
from chess.knight import Knight
from chess.move import Move
from chess.offset import Offset
from chess.path import Path
from chess.pawn import Pawn
from chess.piece import Piece
from chess.position import Position
from chess.queen import Queen
from chess.rook import Rook
from chess.size import Size


class Board:
    size: Size = Size(width=8, height=8)
    color_promotion_positions: Dict[Color, Set[Position]] = {
        Color.WHITE: {Position(file=file, rank=8) for file in range(1, 9)},
        Color.BLACK: {Position(file=file, rank=1) for file in range(1, 9)},
    }
    allowed_promotions: Set[Type[Piece]] = {
        Knight,
        Bishop,
        Rook,
        Queen,
    }

    def __init__(self,
                 pieces: Set[Piece],
                 castling_rights: Set[CastleRight],
                 en_passant_target_position: Position = None,
                 half_move_draw_clock: int = 0,
                 full_move_number: int = 0):
        self.pieces: Set[Piece] = pieces
        self.castling_rights: Set[CastleRight] = castling_rights
        self.en_passant_target_position: Position = en_passant_target_position
        self.half_move_draw_clock: int = half_move_draw_clock
        self.full_move_number: int = full_move_number

    def move(self, piece: Piece, destination: Position):
        self._validate_destination_is_empty(destination=destination)
        self._validate_in_bounds(position=destination)

        self.pieces.remove(piece)
        self.pieces.add(piece.move(destination))

    def _validate_destination_is_empty(self, destination: Position):
        if self.get_piece(destination) is not None:
            raise ValueError(f'Piece already at {destination}')

    def _validate_in_bounds(self, position: Position):
        if not self.in_bounds(position):
            raise ValueError(f'Position {position} is out of bounds')

    def promote(self, piece: Piece, promotion: Type[Piece]):
        self._validate_is_allowed_promotion(promotion=promotion)
        self.pieces.remove(piece)
        self.pieces.add(piece.promote(promotion=promotion))

    def _validate_is_allowed_promotion(self, promotion: Type[Piece]):
        if promotion not in self.allowed_promotions:
            raise ValueError(f'Invalid promotion: {promotion}')

    def get_colored_pieces(self, color: Color) -> Set[Piece]:
        return {piece for piece in self.pieces if piece.color == color}

    def get_piece(self, position: Position) -> Piece | None:
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def get_max_steps(self, position: Position, offset: Offset) -> int:
        max_dx = max(self.size.width - position.file, position.file) // offset.dx
        max_dy = max(self.size.height - position.rank, position.rank) // offset.dy
        return min(max_dx, max_dy)

    def is_promotion_position(self, color: Color, position: Position) -> bool:
        return position in self.color_promotion_positions[color]

    def in_bounds(self, position: Position) -> bool:
        return self._in_width_bounds(position) and self._in_height_bounds(position)

    def _in_width_bounds(self, position: Position) -> bool:
        return 1 <= position.file <= self.size.width

    def _in_height_bounds(self, position: Position) -> bool:
        return 1 <= position.rank <= self.size.height













