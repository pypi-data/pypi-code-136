from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict

from minesweeper_sandbox.board import Board
from minesweeper_sandbox.cell import Position


@dataclass
class GameDifficultyPreset:
    width: int
    height: int
    bombs: int


class GameDifficulty(Enum):
    BEGINNER: GameDifficultyPreset = GameDifficultyPreset(width=9, height=9, bombs=10)
    INTERMEDIATE: GameDifficultyPreset = GameDifficultyPreset(width=16, height=16, bombs=40)
    EXPERT: GameDifficultyPreset = GameDifficultyPreset(width=16, height=30, bombs=99)


class GameAction(Enum):
    REVEAL = "reveal"
    FLAG = "flag"


class GameState(Enum):
    PLAYING = "playing"
    WIN = "win"
    LOOSE = "loose"


class Game:
    def __init__(self, difficulty: GameDifficulty):
        self.board: Board = Board(w=difficulty.value.width, h=difficulty.value.height, bombs=difficulty.value.bombs)
        self.first_move: bool = True
        self.state = GameState.PLAYING

    def action(self, action: GameAction, x, y) -> GameState:
        if x > self.board.w or y > self.board.h:
            raise ValueError(f"({x}, {y}) is not a valid position.")
        pos: Position = Position(y, x)

        if action == GameAction.REVEAL:
            self.reveal(first_move=self.first_move, pos=pos)
            self.first_move = False
        elif action == GameAction.FLAG:
            self.flag(pos=pos)

        return self.state

    def reveal(self, first_move: bool, pos: Position) -> None:
        if first_move:
            self.board.populate_board(pos)
            self.first_move = False
        if self.board.reveal(pos):
            self.state = GameState.LOOSE
        self.check_win()

    def flag(self, pos: Position) -> None:
        self.board.flag(pos)
        self.check_win()

    def check_win(self) -> None:
        if all([
            self.board.flagged_cells == self.board.bombs,
            self.board.revealed_cells + self.board.flagged_cells == self.board.w*self.board.h
        ]):
            self.state = GameState.WIN

    def state_data(self) -> Dict[str, Any]:
        return {
            "state": self.state.value,
            "board": [
                [
                    cell.value.value if cell.revealed else "F" if cell.flagged else '_'
                    for cell in row
                ]
                for row in self.board.board
            ],
            "width": self.board.w,
            "height": self.board.h,
            "num_flagged": self.board.flagged_cells,
            "num_revealed": self.board.revealed_cells,
            "total_bombs": self.board.bombs,
            "first_move": self.first_move
        }

    @staticmethod
    def display_state(game: Dict[str, Any]) -> None:
        print("  ", end="")
        for x in range(len(game["board"])):
            print(x, end=" ")
        print("")
        for i, row in enumerate(game["board"]):
            print(i, end=" ")
            for cell in row:
                print(cell, end=" ")
            print("")
        print(f"\n{game['state']} | Bombs: {game['total_bombs']} | Flags: {game['num_flagged']} | Revealed: {game['num_revealed']}")
