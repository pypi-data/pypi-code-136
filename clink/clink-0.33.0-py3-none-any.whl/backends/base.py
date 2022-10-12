import abc
import logging
from typing import Any, Dict, Type

import clink

from .. import messaging, participants


__all__: list = []


logger = logging.getLogger(__name__)


class Backend(metaclass=abc.ABCMeta):
    """Base backend."""

    def __init__(self, dispatcher: "Dispatcher") -> None:
        self.dispatcher = dispatcher


class Dispatcher(metaclass=abc.ABCMeta):
    """Base dispatcher class."""

    backend_class: Type[Backend]

    def __init__(self) -> None:
        logger.info(
            f"{clink.__title__}, version {clink.__version__}. "
            f"{clink.__copyright__}.",
            extra={
                "author": clink.__author__,
                "copyright": clink.__copyright__,
                "license": clink.__license__,
                "title": clink.__title__,
                "url": clink.__url__,
                "version": clink.__version__,
            },
        )
        self.backend = self.backend_class(self)

    @abc.abstractmethod
    def consume(
        self, *, consumer: "participants.Consumer"
    ) -> None:  # pragma: no cover
        raise NotImplementedError()

    @abc.abstractmethod
    def emit_event(
        self,
        *,
        producer: "participants.Producer",
        event: messaging.events.BaseEvent,
    ) -> None:  # pragma: no cover
        raise NotImplementedError()

    @abc.abstractmethod
    def get_metadata(
        self, **kwargs: Any
    ) -> Dict[str, Any]:  # pragma: no cover
        raise NotImplementedError()

    @abc.abstractmethod
    def run_command(
        self,
        *,
        producer: "participants.Producer",
        command: messaging.commands.BaseCommand,
    ) -> None:  # pragma: no cover
        raise NotImplementedError()

    @abc.abstractmethod
    def send_message(
        self,
        *,
        producer: "participants.Producer",
        message: messaging.base.BaseMessage,
    ) -> None:  # pragma: no cover
        raise NotImplementedError()
