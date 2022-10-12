import collections
import logging
from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    Optional,
    Union,
)

from . import handlers, utils


__all__ = ["Listener"]


logger = logging.getLogger(__name__)


@dataclass
class Listener:
    """Listener. Connects topics to handlers."""

    topics: Union[str, Collection[str]]

    handlers: Union[Callable, Collection[Callable]]

    name: Optional[str] = None

    def __post_init__(self) -> None:
        self.topics = list(utils.maybe_list(self.topics))
        self.handlers = list(utils.maybe_list(self.handlers))

    @property
    def durable(self) -> bool:
        return bool(self.name)

    @property
    def exclusive(self) -> bool:
        return not self.durable


ListenerReferences = Union[
    "Listener",
    Dict[str, "handlers.HandlerReferences"],
    Dict[str, Any],
    Iterable["Listener"],
    Iterable[Dict[str, Any]],
]


def _parse_listener_references(
    listeners: ListenerReferences, *, context: Any
) -> List[Listener]:
    """Parse various input formats of listener references in to a list of
    listener instances.

    Listener
    {"topic_1": handler_1, "topic_2": handler_2}
    {"topics": ["topic_1", "topic_2"], "handlers": [handler]}
    [Listener]
    [
        {"topics": ["topic_1", "topic_2"], "handlers": [handler_1]},
        {"topics": ["topic_3"], "handlers": [handler_2, handler_3]},
    ]

    """

    parsed_listeners: List[Listener] = []

    if isinstance(listeners, dict) and "handlers" not in listeners:
        # Assume key value pairs of one topic and one or more listeners
        for topics, value in listeners.items():
            parsed_handlers: List[
                Callable
            ] = handlers._parse_handler_references(value, context=context)
            parsed_listeners += [
                Listener(topics=topics, handlers=parsed_handlers)
            ]

    else:
        for item in utils.maybe_list(listeners):
            if isinstance(item, Listener):
                parsed_listeners += [item]
            else:
                parsed_handlers = handlers._parse_handler_references(
                    item.pop("handlers"), context=context
                )
                parsed_listeners += [
                    Listener(handlers=parsed_handlers, **item)
                ]

    return parsed_listeners


class ListenerList(collections.UserList):
    def __init__(
        self,
        initlist: Optional[Iterable] = None,
        *,
        context: Optional[Any] = None,
    ) -> None:
        self._context = context
        if initlist is not None:
            initlist = self._parse_listener_references(initlist)
        super().__init__(initlist)

    def __add__(self, other: ListenerReferences) -> "ListenerList":
        return super().__add__(self._parse_listener_references(other))

    def __iadd__(self, other: ListenerReferences) -> "ListenerList":
        return super().__iadd__(self._parse_listener_references(other))

    def _parse_listener_references(
        self, listeners: ListenerReferences
    ) -> List[Listener]:
        return _parse_listener_references(listeners, context=self._context)
