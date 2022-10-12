from functools import wraps
from textwrap import dedent
from typing import Any, Callable, List, TypeVar, Union, cast

from typing_extensions import ParamSpec

_P = ParamSpec("_P")
_R = TypeVar("_R")


# Taken from Pandas:
# https://github.com/pandas-dev/pandas/blame/8aa707298428801199280b2b994632080591700a/pandas/util/_decorators.py#L332
def doc(
    *args: Union[str, Callable[..., Any]], **kwargs: str
) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]:
    """Take docstring templates, concatenate them and perform string substitution."""

    def decorator(function: Callable[_P, _R]) -> Callable[_P, _R]:
        @wraps(function)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> Any:
            return function(*args, **kwargs)

        # Collecting docstring and docstring templates
        docstring_components: List[Union[str, Callable[..., Any]]] = []

        if function.__doc__:
            docstring_components.append(dedent(function.__doc__))

        for arg in cast(Any, args):
            if hasattr(arg, "_docstring_components"):
                docstring_components.extend(
                    cast(
                        Any,
                        arg,
                    )._docstring_components
                )
            elif isinstance(arg, str) or arg.__doc__:
                docstring_components.append(arg)

        # Formatting templates and concatenating docstring
        wrapper.__doc__ = "".join(
            [
                arg.format(**kwargs)
                if isinstance(arg, str)
                else dedent(arg.__doc__ or "")
                for arg in docstring_components
            ]
        )

        wrapper._docstring_components = docstring_components  # type: ignore

        return wrapper

    return decorator
