from enum import Enum, auto
from inspect import _ParameterKind as ParameterKind


class NoValue(Enum):
    def __repr__(self) -> str:
        return f"<{type(self).__name__}.{self.name}>"


class ParameterType(NoValue):
    POSITIONAL_ONLY = auto()
    POSITIONAL_OR_KEYWORD = auto()
    VAR_POSITIONAL = auto()
    KEYWORD_ONLY = auto()
    VAR_KEYWORD = auto()

    @classmethod
    def from_kind(cls, kind: ParameterKind, /) -> "ParameterType":
        return getattr(cls, kind.name)
