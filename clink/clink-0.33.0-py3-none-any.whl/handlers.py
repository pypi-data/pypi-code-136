import abc
import functools
import logging
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

import sentry_sdk

from . import backends, messaging, utils


__all__ = [
    "EventHandler",
    "Handler",
    "_parse_handler_references",
    "handler",
    "event_handler",
]


logger = logging.getLogger(__name__)


WrappedFunction = TypeVar("WrappedFunction", bound=Callable)


class Handler(metaclass=abc.ABCMeta):
    """Handler."""

    supports_dry_run: bool = False

    suppress_exceptions: bool = False

    def __call__(self, function: Callable) -> WrappedFunction:
        @functools.wraps(function)
        def wrapper(body: Any, *, metadata: Optional[dict] = None) -> Any:
            parsed_body = self.parse_body(body, metadata=metadata)
            dry_run = self.is_dry_run(parsed_body, metadata=metadata)

            if dry_run and not self.supports_dry_run:
                logger.warning(
                    "Dry-run is not supported by this handler. Skipping.",
                    extra={"function": function, "handler": self},
                )
                return None

            with sentry_sdk.configure_scope() as scope:
                self._configure_sentry_scope(
                    scope,
                    parsed_body,
                    function=function,
                    metadata=metadata,
                    dry_run=dry_run,
                )

                try:
                    result = function(
                        parsed_body, metadata=metadata, dry_run=dry_run
                    )

                except Exception as exception:
                    if self.suppress_exceptions:
                        logger.exception(
                            f'Unhandled exception "{exception}" was '
                            f'suppressed in "{function}".',
                            extra={
                                "dry_run": dry_run,
                                "function": utils.get_full_qualname(function),
                                "handler": self,
                                "metadata": metadata,
                                "parsed_body": parsed_body,
                                "supports_dry_run": self.supports_dry_run,
                                "suppress_exceptions": self.suppress_exceptions,  # noqa: E501
                            },
                        )
                    else:
                        raise

                else:
                    scope.clear()
                    return result

        setattr(wrapper, "_handler", self)
        return wrapper  # type: ignore[return-value]

    def __init__(
        self,
        *,
        dispatcher: Optional["backends.base.Dispatcher"] = None,
        suppress_exceptions: Optional[bool] = None,
        supports_dry_run: Optional[bool] = None,
    ) -> None:
        self.dispatcher = dispatcher or backends.Dispatcher()
        if suppress_exceptions is not None:
            self.suppress_exceptions = suppress_exceptions
        if supports_dry_run is not None:
            self.supports_dry_run = supports_dry_run

        setattr(self, "run", self(function=self.run))

    def _configure_sentry_scope(
        self,
        scope: sentry_sdk.Scope,
        parsed_body: Any,
        *,
        function: Callable,
        metadata: Optional[dict],
        dry_run: bool,
    ) -> None:
        scope.set_tag(
            "clink_handler_function", utils.get_full_qualname(function)
        )
        scope.set_tag("clink_dry_run", dry_run)

    def is_dry_run(self, body: Any, **kwargs: Any) -> bool:
        raise NotImplementedError()

    def parse_body(self, body: Any, **kwargs: Any) -> Any:
        return body

    def run(
        self,
        body: Any,
        *,
        metadata: Optional[dict] = None,
        dry_run: bool = False,
    ) -> None:
        raise NotImplementedError()


class EventHandler(Handler, metaclass=abc.ABCMeta):
    """Event handler."""

    def _configure_sentry_scope(
        self,
        scope: sentry_sdk.Scope,
        event: messaging.events.BaseEvent,
        *,
        function: Callable,
        metadata: Optional[dict],
        dry_run: bool,
    ) -> None:
        super()._configure_sentry_scope(
            scope,
            event,
            function=function,
            metadata=metadata,
            dry_run=dry_run,
        )
        scope.set_context("CLINK Event", event.to_dict())
        scope.set_tag("clink_event.source", str(event.source))
        scope.set_tag("clink_event.type", str(event.type))
        scope.set_tag("clink_trace_id", str(event.trace_parent.trace_id))
        if event.subject_urn:
            utils.set_scope_tags(
                scope,
                tags={
                    "clink_event.subject": str(event.subject_urn),
                    "clink_event.subject.partition": str(
                        event.subject_urn.partition
                    ),
                    "clink_event.subject.service": str(
                        event.subject_urn.service
                    ),
                    "clink_event.subject.region": str(
                        event.subject_urn.region
                    ),
                    "clink_event.subject.account": str(
                        event.subject_urn.account
                    ),
                    "clink_event.subject.resourcetype": str(
                        event.subject_urn.resource.type
                    ),
                    "clink_event.subject.resourceid": str(
                        event.subject_urn.resource.id
                    ),
                },
            )

    def is_dry_run(
        self, body: messaging.events.BaseEvent, **kwargs: Any
    ) -> bool:
        return body.dry_run

    def parse_body(
        self, body: Any, **kwargs: Any
    ) -> messaging.events.BaseEvent:
        metadata = kwargs.get("metadata", {})
        content_type = metadata.get("content_type")

        if not content_type == "application/cloudevents+json":
            raise ValueError(
                "Expected content type of "
                '"application/cloudevents+json", but received '
                f'"{content_type}".'
            )

        event = messaging.Event.from_json(body, metadata=metadata)
        logger.info(
            f'Received "{event.type}" event '
            f'from "{event.source}" for "{event.subject}" '
            f'[id: "{event.id}", trace_id: "{event.trace_parent.trace_id}", '
            f'parent_id: "{event.trace_parent.parent_id}"].',
            extra={"event": event},
        )
        logger.debug(event)

        return event

    def run(
        self,
        event: messaging.events.BaseEvent,
        *,
        metadata: Optional[dict] = None,
        dry_run: bool = False,
    ) -> None:
        raise NotImplementedError()


def handler(
    base: Type[Handler] = Handler,
    *,
    dispatcher: Optional["backends.base.Dispatcher"] = None,
    suppress_exceptions: Optional[bool] = None,
    supports_dry_run: Optional[bool] = None,
) -> Handler:
    return base(
        dispatcher=dispatcher,
        suppress_exceptions=suppress_exceptions,
        supports_dry_run=supports_dry_run,
    )


def event_handler(**kwargs: Any) -> Handler:
    return handler(base=EventHandler, **kwargs)


HandlerReferences = Union[
    WrappedFunction, str, Iterable[Union[WrappedFunction, str]]
]


def _parse_handler_references(
    handlers: HandlerReferences, *, context: Any
) -> List[WrappedFunction]:
    return [
        getattr(context, handler) if isinstance(handler, str) else handler
        for handler in utils.maybe_list(handlers)
    ]
