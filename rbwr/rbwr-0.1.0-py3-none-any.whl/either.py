"""
The `Either` type and its components
"""

from typing import Generic, Tuple, TypeVar, Union

L = TypeVar("L")
R = TypeVar("R")


class Left:
    """
    The "left" variant containing a value
    """


class Right:
    """
    The "right" variant containing a value
    """


class Either(Generic[L, R]):
    """
    A type that is either a left or a right value, never both
    """

    def __init__(self, adt: Union[Tuple[Left, L], Tuple[Right, R]]) -> None:
        self.matchable = adt
        """
        Access this variable to get a type useful for `match` statements

        ## Examples

        ```python
        res = Either((Left(), 5))

        match res.matchable:
            case (Left(), x):
                assert x == 5
            case (Right(), _):
                raise AssertionError("unreachable")
        ```
        """

    def __repr__(self) -> str:
        match self.matchable:
            case (Left(), x):
                return f"Left({repr(x)})"
            case (Right(), x):
                return f"Right({repr(x)})"
