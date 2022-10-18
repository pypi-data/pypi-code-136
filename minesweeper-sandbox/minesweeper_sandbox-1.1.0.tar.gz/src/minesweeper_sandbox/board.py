import random as rand
from typing import Generator, List, Optional

from minesweeper_sandbox.cell import Cell, CellValue, Position


class Board:
    def __init__(self, w: int, h: int, bombs: int):
        self.w: int = w
        self.h: int = h
        self.bombs: int = bombs
        self.board: List[List[Cell]]
        self.flagged_cells = 0
        self.revealed_cells = 0

        self.create_empty_board()

    def create_empty_board(self) -> List[List[Cell]]:
        self.board = [
            [Cell() for _ in range(self.w)]for _ in range(self.h)
        ].copy()
        for x in range(self.w):
            for y in range(self.h):
                self.board[y][x].set_position(pos=Position(y, x))
        return self.board

    def populate_board(self, move: Position) -> None:
        # Bombs
        bombs_placed = 0
        while bombs_placed < self.bombs:
            x, y = rand.randint(0, self.w-1), rand.randint(0, self.h-1)
            if x == move.x and y == move.y:
                continue
            cell = self.board[y][x]
            if cell.is_bomb():
                continue
            cell.set_bomb()
            bombs_placed += 1

        # Adjacency List
        for x in range(self.w):
            for y in range(self.h):
                cell = self.board[y][x]
                if not cell.is_bomb():
                    self.board[y][x].set_adjacent([
                        self.board[pos.y][pos.x] for pos in Board.get_adj_coords(self.w, self.h, Position(x=x, y=y))
                    ])

    def reveal(self, pos: Optional[Position]) -> bool:
        """ returns true if a bomb is revealed """
        if not pos:
            return False

        cell = self.board[pos.x][pos.y]
        if cell.revealed:
            return False

        self.revealed_cells += 1

        if cell.reveal():
            return True

        if cell.get_value() == CellValue.ZERO:
            for adj in cell.adj_cells():
                self.reveal(adj.pos)

        return False

    def flag(self, pos: Position) -> None:
        self.flagged_cells += self.board[pos.x][pos.y].flag()

    @staticmethod
    def get_adj_coords(board_w: int, board_h: int, pos: Position) -> Generator[Position, None, None]:
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == c == 0:
                    continue
                if 0 <= pos.x+r < board_w and 0 <= pos.y+c < board_h:
                    yield (Position(x=pos.x+r, y=pos.y+c))
