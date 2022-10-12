import logging
from typing import Any, Callable, Dict, Iterable, List, Optional, Type, Union

import kombu
import kombu.mixins
import kombu.transport.base

from .. import listeners, messaging, participants, settings
from . import base


__all__ = ["Dispatcher"]


logger = logging.getLogger(__name__)


class Backend(base.Backend):
    """Kombu backend."""

    def __init__(
        self,
        dispatcher: base.Dispatcher,
        *,
        transport_url: Optional[str] = None,
    ) -> None:
        super().__init__(dispatcher)
        self.connection = kombu.Connection(
            transport_url or settings.TRANSPORT_URL
        )
        self.exchange = kombu.Exchange(name="clink", type="topic")

    def get_consumerproducer(
        self, consumer_kwargs: Optional[List[Dict[str, Any]]] = None
    ) -> "KombuConsumerProducer":
        return KombuConsumerProducer(
            connection=self.connection,
            exchange=self.exchange,
            consumer_kwargs=consumer_kwargs,
        )

    def publish(
        self, *, body: Union[dict, str], content_type: str, routing_key: str
    ) -> None:
        if not hasattr(self, "_producer"):
            self._producer = self.get_consumerproducer().producer

        self._producer.publish(
            body=body,
            content_type=content_type,
            declare=[self.exchange],
            exchange=self.exchange,
            routing_key=routing_key,
        )


class Dispatcher(base.Dispatcher):
    """Kombu dispatcher."""

    backend_class = Backend

    def _wrap_handler(self, function_: Callable) -> Callable:
        def wrapper(body: Union[dict, str], message: kombu.Message) -> Any:
            metadata = self.get_metadata(body, message=message)
            return function_(body, metadata=metadata)

        return wrapper

    def get_metadata(  # type: ignore[override]
        self, body: Union[dict, str], *, message: kombu.Message
    ) -> Dict[str, Any]:
        return {
            "_message": message,
            "content_encoding": message.content_encoding,
            "content_type": message.content_type,
            "headers": message.headers,
        }

    def _get_kombu_consumer_kwargs(
        self,
        *,
        consumer: "participants.Consumer",
        listeners: Iterable[listeners.Listener],
    ) -> List[Dict[str, Any]]:
        return [
            {
                "queues": [
                    kombu.Queue(
                        auto_delete=not listener.durable,
                        durable=listener.durable,
                        exclusive=listener.exclusive,
                        name=listener.name,
                        bindings=[
                            kombu.binding(
                                exchange=self.backend.exchange,  # type: ignore[attr-defined]  # noqa: E501
                                routing_key=topic,
                            )
                            for topic in listener.topics
                        ],
                    )
                ],
                "callbacks": [
                    self._wrap_handler(handler)
                    for handler in listener.handlers  # type: ignore[union-attr]  # noqa: E501
                ],
                "auto_declare": True,
                "no_ack": True,
            }
            for listener in listeners
        ]

    def consume(self, *, consumer: "participants.Consumer") -> None:
        kombu_consumer_kwargs = self._get_kombu_consumer_kwargs(
            consumer=consumer, listeners=consumer.listeners
        )
        kombu_consumerproducer = self.backend.get_consumerproducer(  # type: ignore[attr-defined]  # noqa: E501
            consumer_kwargs=kombu_consumer_kwargs
        )

        try:
            kombu_consumerproducer.run()
        except KeyboardInterrupt:
            logger.warning("Keyboard interrupt.")

    def emit_event(
        self,
        *,
        producer: "participants.Producer",
        event: messaging.events.BaseEvent,
    ) -> None:
        self.backend.publish(  # type: ignore[attr-defined]
            body=event.to_json(),
            content_type="application/cloudevents+json",
            routing_key=event.type,
        )

    def run_command(
        self,
        *,
        producer: "participants.Producer",
        command: messaging.commands.BaseCommand,
    ) -> None:
        raise NotImplementedError()

    def send_message(
        self,
        *,
        producer: "participants.Producer",
        message: messaging.base.BaseMessage,
    ) -> None:
        raise NotImplementedError()


class KombuConsumerProducer(kombu.mixins.ConsumerProducerMixin):
    def __init__(
        self,
        *,
        connection: kombu.Connection,
        exchange: kombu.Exchange,
        consumer_kwargs: Optional[List[Dict[str, Any]]] = None,
    ) -> None:
        self.connection = connection
        self.exchange = exchange
        self.consumer_kwargs = (
            consumer_kwargs if consumer_kwargs is not None else []
        )

    def get_consumers(
        self,
        Consumer: Type[kombu.Consumer],
        channel: kombu.transport.base.StdChannel,
    ) -> List[kombu.Consumer]:
        return [Consumer(**kwargs) for kwargs in self.consumer_kwargs]
