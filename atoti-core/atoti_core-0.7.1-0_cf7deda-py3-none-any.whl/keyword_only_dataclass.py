from dataclasses import is_dataclass
from functools import wraps
from typing import Any, Type, TypeVar

_T = TypeVar("_T")


def keyword_only_dataclass(cls: Type[_T]) -> Type[_T]:
    """Decorate a dataclass to force its construction to be done with keyword-only parameters.

    Replace with func:`dataclasses.dataclass`'s *kw_only* when bumping minimum supported version of Python to 3.10.
    """
    if not is_dataclass(cls):
        raise TypeError(f"Expected a dataclass but received {cls}.")

    init = cls.__init__

    @wraps(init)
    def init_enforcing_keyword_only_arguments(
        self: _T, *args: Any, **kwargs: Any
    ) -> None:
        if len(args) > 0:
            raise TypeError(
                f"{cls.__name__} expects keyword-only arguments but the following positional arguments were passed: {args}."
            )

        init(self, **kwargs)

    setattr(cls, "__init__", init_enforcing_keyword_only_arguments)

    return cls
