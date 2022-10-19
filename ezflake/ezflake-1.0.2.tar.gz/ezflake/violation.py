from __future__ import annotations

from dataclasses import dataclass
from functools import partial
from typing import Type, Dict, Any, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from .plugin import Plugin


@dataclass
class Violation:
    code: int
    message: str
    line: int
    col: int
    kwargs: Dict[str, Any]

    @property
    def full_message(self):
        return f'{str(self.code).zfill(3)} {self.formatted_message}'

    @property
    def formatted_message(self):
        return self.message.format(**self.kwargs)

    def as_tuple(self, type_: Type[Plugin]):
        return self.line, self.col, self.full_message, type_


create_violation = partial(partial, Violation)
ViolationFactory = Callable[[int, int, Dict[str, Any]], Violation]
