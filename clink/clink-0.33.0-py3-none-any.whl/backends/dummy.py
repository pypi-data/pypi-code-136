import logging
from typing import Any, Dict

from .. import messaging, participants
from . import base


__all__ = ["Dispatcher"]


logger = logging.getLogger(__name__)


class Backend(base.Backend):
    """Dummy backend."""

    pass


class Dispatcher(base.Dispatcher):
    """Dummy dispatcher."""

    backend_class = Backend

    def consume(self, *, consumer: "participants.Consumer") -> None:
        pass

    def emit_event(
        self,
        *,
        producer: "participants.Producer",
        event: messaging.events.BaseEvent,
    ) -> None:
        pass

    def get_metadata(self, **kwargs: Any) -> Dict[str, Any]:
        return {}

    def run_command(
        self,
        *,
        producer: "participants.Producer",
        command: messaging.commands.BaseCommand,
    ) -> None:
        pass

    def send_message(
        self,
        *,
        producer: "participants.Producer",
        message: messaging.base.BaseMessage,
    ) -> None:
        pass
