from __future__ import annotations

from contextvars import ContextVar
from types import TracebackType
from typing import Optional, Protocol, Type

_transaction_id_context: ContextVar[Optional[int]] = ContextVar(
    "_transaction_id_context", default=None
)
_transaction_id_context.set(None)


def is_inside_transaction() -> bool:
    return _transaction_id_context.get() is not None


class _Start(Protocol):
    def __call__(self, *, scenario_name: str, is_user_initiated: bool) -> int:
        ...


class _End(Protocol):
    def __call__(self, *, has_succeeded: bool, transaction_id: int) -> None:
        ...


class Transaction:

    _scenario_name: str
    _start: _Start
    _end: _End
    _is_user_initiated: bool = True
    _id: Optional[int] = None

    def __init__(
        self,
        scenario_name: str,
        *,
        start: _Start,
        end: _End,
        is_user_initiated: bool = True,
    ):
        self._scenario_name = scenario_name
        self._start = start
        self._end = end
        self._is_user_initiated = is_user_initiated

    def __enter__(self) -> None:
        self._id = self._start(
            scenario_name=self._scenario_name, is_user_initiated=self._is_user_initiated
        )
        _transaction_id_context.set(self._id)

    def __exit__(  # pylint: disable=too-many-positional-parameters
        self,
        exception_type: Optional[Type[BaseException]],
        exception_instance: Optional[BaseException],
        exception_traceback: Optional[TracebackType],
    ) -> None:
        if self._id is None:
            raise RuntimeError("Cannot end transaction without ID.")

        has_succeeded = exception_instance is None
        _transaction_id_context.set(None)
        self._end(has_succeeded=has_succeeded, transaction_id=self._id)
