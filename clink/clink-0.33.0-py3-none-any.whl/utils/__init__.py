import asyncio
from typing import Any

from . import decorators, functional, participants, sentry


__all__ = ["maybe_list", "method_decorator"]


consumer_listeners_table = participants.consumer_listeners_table

maybe_list = functional.maybe_list

method_decorator = decorators.method_decorator

set_scope_tags = sentry.set_scope_tags


def get_running_loop() -> asyncio.AbstractEventLoop:  # pragma: no cover
    if hasattr(asyncio, "get_running_loop"):
        return asyncio.get_running_loop()  # type: ignore[attr-defined]
    else:  # Python 3.6
        return asyncio.get_event_loop()


def get_full_qualname(obj: Any) -> str:
    """Returns the module and qualified name of the class, function, method,
    descriptor, or generator instance."""
    qualname = getattr(obj, "__qualname__", obj.__class__.__qualname__)
    module = (
        obj.__module__
        if hasattr(obj, "__module__") and obj.__module__ is not None
        else getattr(obj, "__self__", obj.__class__).__module__
    )
    return f"{module}.{qualname}"
