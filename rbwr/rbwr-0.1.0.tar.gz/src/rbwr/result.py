"""
The `Result` type and its components
"""

from typing import Generic, Tuple, TypeVar, Union

T = TypeVar("T")
E = TypeVar("E")


class Ok:
    """
    The variant containing a success value
    """


class Err:
    """
    The variant containing an error value
    """


class Result(Generic[T, E]):
    """
    A type that is either a success value or an error value, never both
    """

    def __init__(self, adt: Union[Tuple[Ok, T], Tuple[Err, E]]) -> None:
        self.matchable = adt
        """
        Access this variable to get a type useful for `match` statements

        ## Examples

        ```python
        res = Result((Ok(), 5))

        match res.matchable:
            case (Ok(), x):
                assert x == 5
            case (Err(), _):
                raise AssertionError("unreachable")
        ```
        """

    def __repr__(self) -> str:
        match self.matchable:
            case (Ok(), x):
                return f"Ok({repr(x)})"
            case (Err(), x):
                return f"Err({repr(x)})"
