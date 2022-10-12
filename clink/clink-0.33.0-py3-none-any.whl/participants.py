import abc
import asyncio
import concurrent.futures
import functools
import logging
from copy import copy
from typing import Any, List, Optional, Sequence

from . import backends
from . import listeners as listeners_
from . import messaging, utils


__all__ = ["Consumer", "Producer"]


logger = logging.getLogger(__name__)


class Participant(metaclass=abc.ABCMeta):
    """Base participant."""

    def __init__(
        self, dispatcher: Optional["backends.base.Dispatcher"] = None
    ):
        self.dispatcher: "backends.base.Dispatcher" = (
            dispatcher or backends.Dispatcher()
        )


class Consumer(Participant):
    """Consumer."""

    listeners: Sequence = []

    def __init__(
        self,
        dispatcher: Optional["backends.base.Dispatcher"] = None,
        *,
        listeners: Optional[listeners_.ListenerReferences] = None,
    ):
        super().__init__(dispatcher=dispatcher)
        self.listeners: List[listeners_.Listener] = listeners_.ListenerList(
            self.listeners, context=self
        )
        if listeners is not None:
            self.listeners += listeners

    def consume(self) -> None:
        logger.info(f"{utils.consumer_listeners_table(self)}")

        self.dispatcher.consume(consumer=self)

    async def async_consume(self) -> None:  # TODO - proper thread handling
        executor = concurrent.futures.ThreadPoolExecutor()
        loop = utils.get_running_loop()
        try:
            await loop.run_in_executor(executor, self.consume)
        except asyncio.CancelledError:  # pragma: no cover  # TODO
            executor.shutdown(wait=False)
            for thread in executor._threads:  # TODO - cleaner option
                thread._tstate_lock.release()  # type: ignore[attr-defined]


class Producer(Participant):
    """Producer."""

    source: Optional[str] = None

    def __init__(
        self,
        dispatcher: Optional["backends.base.Dispatcher"] = None,
        *,
        source: Optional[str] = None,
    ):
        super().__init__(dispatcher=dispatcher)
        if source is not None:
            self.source = source

    async def async_emit_event(
        self,
        event: Optional[messaging.events.BaseEvent] = None,
        *,
        preceding_event: Optional[messaging.events.BaseEvent] = None,
        **kwargs: Any,
    ) -> None:
        loop = utils.get_running_loop()
        emit_event = functools.partial(
            self.emit_event, event, preceding_event=preceding_event, **kwargs
        )
        # mypy partial issue 1484 https://github.com/python/mypy/issues/1484
        return await loop.run_in_executor(
            None, emit_event  # type: ignore[arg-type]
        )

    async def async_run_command(
        self,
        command: Optional[messaging.commands.BaseCommand] = None,
        **kwargs: Any,
    ) -> None:
        loop = utils.get_running_loop()
        run_command = functools.partial(self.run_command, command, **kwargs)
        # mypy partial issue 1484 https://github.com/python/mypy/issues/1484
        return await loop.run_in_executor(
            None, run_command  # type: ignore[arg-type]
        )

    async def async_send_message(
        self,
        message: Optional[messaging.base.BaseMessage] = None,
        **kwargs: Any,
    ) -> None:
        loop = utils.get_running_loop()
        send_message = functools.partial(self.send_message, message, **kwargs)
        # mypy partial issue 1484 https://github.com/python/mypy/issues/1484
        return await loop.run_in_executor(
            None, send_message  # type: ignore[arg-type]
        )

    def emit_event(
        self,
        event: Optional[messaging.events.BaseEvent] = None,
        *,
        preceding_event: Optional[messaging.events.BaseEvent] = None,
        **kwargs: Any,
    ) -> messaging.events.BaseEvent:
        if event is None:
            kwargs.setdefault("source", self.source)
            if preceding_event is not None:
                event = messaging.Event.from_preceding_event(
                    preceding_event, **kwargs
                )
            else:
                event = messaging.Event(**kwargs)
        else:
            event = copy(event)
            event.dry_run = kwargs.get("dry_run", False) or event.dry_run

        logger.debug(event)

        self.dispatcher.emit_event(producer=self, event=event)

        logger.info(
            f'Published "{event.type}" event from '
            f'"{event.source}" for "{event.subject}" '
            f'[id: "{event.id}", trace_id: "{event.trace_parent.trace_id}", '
            f'parent_id: "{event.trace_parent.parent_id}"].',
            extra={"event": event},
        )

        return event

    def run_command(
        self,
        command: Optional[messaging.commands.BaseCommand] = None,
        **kwargs: Any,
    ) -> messaging.commands.BaseCommand:
        if command is None:
            command = messaging.commands.Command(**kwargs)

        logger.debug(command)

        self.dispatcher.run_command(producer=self, command=command)

        return command

    def send_message(
        self,
        message: Optional[messaging.base.BaseMessage] = None,
        **kwargs: Any,
    ) -> messaging.base.BaseMessage:
        if message is None:
            message = messaging.base.BaseMessage(**kwargs)

        logger.debug(message)

        self.dispatcher.send_message(producer=self, message=message)

        return message
