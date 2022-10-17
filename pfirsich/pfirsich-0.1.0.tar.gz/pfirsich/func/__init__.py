from __future__ import annotations

from collections.abc import Callable
from typing import Generic, TypeVar
import sys

if sys.version_info < (3, 10):
    from typing_extensions import ParamSpec
else:
    from typing import ParamSpec

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")

class Func(Generic[P, R]):
    def __init__(self, func: Callable[P, R]):
        self.func = func

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.func(*args, **kwargs)

    def __or__(self, rhs: Callable[[R], T]) -> Func[P, T]:
        @Func
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            return rhs(self.func(*args, **kwargs))
        
        return wrapper

__all__ = ["Func"]
