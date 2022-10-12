from typing import Any, Callable, Optional

from . import backends, handlers, listeners, messaging, participants


__all__ = ["Event", "Participant", "SubjectURN", "TraceParent", "TraceState"]


Event = messaging.events.Event


SubjectURN = messaging.events.SubjectURN


TraceParent = messaging.events.TraceParent


TraceState = messaging.events.TraceState


class Participant(participants.Producer, participants.Consumer):
    """A clink Participant (can be a producer and/or a consumer)."""

    def __init__(
        self,
        name: str,
        *,
        dispatcher: Optional["backends.base.Dispatcher"] = None,
    ):
        super().__init__(dispatcher, source=name)

    def on_event(
        self, *topics: str, name: Optional[str] = None, **kwargs: Any
    ) -> Callable:
        """Decorator which combines the creation of an EventHandler and
        Listener."""
        kwargs["dispatcher"] = self.dispatcher

        def register(function: Callable) -> handlers.WrappedFunction:
            handler: handlers.WrappedFunction = handlers.EventHandler(
                **kwargs
            )(function)
            self.listeners += [  # type: ignore[operator]
                listeners.Listener(topics=topics, handlers=handler, name=name)
            ]
            return handler

        return register
