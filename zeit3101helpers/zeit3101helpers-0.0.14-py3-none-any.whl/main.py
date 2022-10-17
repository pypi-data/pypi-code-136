import json
from time import sleep
import pika
from stix2 import Bundle, parse
from typing import Callable


class ChannelProvider:
    def __init__(
        self,
        hostname: str = "queue",
        port: int = 5672,
        username: str = "root",
        password: str = "root",
    ):
        credentials = pika.PlainCredentials(username, password)
        self._connection = None

        while self._connection is None:
            try:
                self._connection = pika.BlockingConnection(
                    pika.ConnectionParameters(hostname, port, "/", credentials)
                )
            except pika.exceptions.AMQPConnectionError:
                print("Polling AMQP channel...")
                sleep(3)

        self._stix_channel = None
        self._enrichment_channel = None

    def get_enrichment_channel(self):
        if self._enrichment_channel is None:
            new_channel = self._connection.channel()

            new_channel.exchange_declare(
                exchange="enrichment", exchange_type="fanout"
            )

            new_channel.queue_declare(queue="enrichment-queue")

            new_channel.queue_bind(
                exchange="enrichment", queue="enrichment_queue"
            )

            self._enrichment_channel = new_channel

        return self._enrichment_channel

    def get_stix_channel(self):

        new_channel = self._connection.channel()

        new_channel.exchange_declare(exchange="stix", exchange_type="fanout")

        result = new_channel.queue_declare(queue="", exclusive=True)
        queue_name = result.method.queue

        new_channel.queue_bind(exchange="stix", queue=queue_name)

        return new_channel, queue_name


class Helper:
    def __init__(
        self,
        hostname: str = "queue",
        port: int = 5672,
        username: str = "root",
        password: str = "root",
    ) -> None:
        self.channel_provider = ChannelProvider(
            hostname, port, username, password
        )

    def listen(self, callback: Callable) -> None:
        def consume_message(ch, method, properties, body):
            bundle = parse(str(body))
            return callback(bundle)

        channel = self.channel_provider.get_enrichment_channel()
        channel.basic_consume(
            queue="enrichment-queue",
            on_message_callback=consume_message,
            auto_ack=True,
        )
        channel.start_consuming()

    def send_stix_bundle(self, bundle: Bundle) -> None:
        channel, queue_name = self.channel_provider.get_stix_channel()
        channel.basic_publish(
            exchange="stix", routing_key=queue_name, body=bundle.serialize()
        )
        channel.close()

    def consume_stix(self, callback: Callable) -> None:
        def consume_message(ch, method, properties, body):
            json_bundle = json.loads(body)
            bundle = parse(json_bundle)
            return callback(bundle)

        channel, queue_name = self.channel_provider.get_stix_channel()
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=consume_message,
            auto_ack=True,
        )
        channel.start_consuming()
