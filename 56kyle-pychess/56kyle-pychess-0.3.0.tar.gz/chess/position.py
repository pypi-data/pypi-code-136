
from dataclasses import dataclass

from .offset import Offset


@dataclass(frozen=True)
class Position:
    file: int  # 1-indexed
    rank: int  # 1-indexed

    def __post_init__(self):
        if self.file <= 0:
            raise ValueError(f'File must be a positive integer: {self.file}')
        if self.rank <= 0:
            raise ValueError(f'Rank must be a positive integer: {self.rank}')

    def offset(self, offset: Offset) -> 'Position':
        return Position(file=self.file + offset.dx, rank=self.rank + offset.dy)



