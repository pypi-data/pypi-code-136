"""Service Bus helpers"""

import os
import logging
from datetime import datetime
from functools import cache
from azure.servicebus import (
    ServiceBusClient,
    ServiceBusMessage,
    ServiceBusSender,
    parse_connection_string,
)
from azure.identity import DefaultAzureCredential


MANAGED_IDENTITY_SETTING_NAME = "MANAGED_IDENTITY_FOR_SERVICE_BUS_ENABLED"


def send_queue_message(
    connection_string: str, queue_name: str, message: ServiceBusMessage
) -> None:

    """Sends a message to the queue."""

    if not connection_string:
        raise ValueError("connection_string cannot be empty")

    if not queue_name:
        raise ValueError("queue_name cannot be empty")

    sender = _get_queue_sender(
        connection_string=connection_string, queue_name=queue_name
    )
    sender.send_messages(message)


def schedule_queue_message(
    connection_string: str,
    queue_name: str,
    message: ServiceBusMessage,
    schedule_time_utc: datetime,
):
    """Schedules a message to be sent to the queue."""
    if not connection_string:
        raise ValueError("connection_string cannot be empty")

    if not queue_name:
        raise ValueError("queue_name cannot be empty")

    sender = _get_queue_sender(
        connection_string=connection_string, queue_name=queue_name
    )
    sender.schedule_messages(message, schedule_time_utc)


def send_topic_message(
    connection_string: str, topic_name: str, message: ServiceBusMessage
):
    """Sends a message to the topic."""

    if not connection_string:
        raise ValueError("connection_string cannot be empty")

    if not topic_name:
        raise ValueError("topic_name cannot be empty")

    sender = _get_topic_sender(
        connection_string=connection_string, topic_name=topic_name
    )
    sender.send_messages(message)


@cache
def _get_service_bus_client(connection_string: str) -> ServiceBusClient:
    """Returns a Service Bus client."""
    if os.getenv(MANAGED_IDENTITY_SETTING_NAME) in ["true", "1", "True", "TRUE"]:
        logging.info("Using managed identity for Service Bus")
        if connection_string.startswith("Endpoint=sb://"):
            connection_string = parse_connection_string(
                connection_string
            ).fully_qualified_namespace
        return ServiceBusClient(
            fully_qualified_namespace=connection_string,
            credential=DefaultAzureCredential(),
        )

    logging.info("Using connection string based authentication for Service Bus")
    return ServiceBusClient.from_connection_string(connection_string)


@cache
def _get_queue_sender(connection_string: str, queue_name: str) -> ServiceBusSender:
    """Gets a queue sender."""
    sb_client = _get_service_bus_client(connection_string=connection_string)
    return sb_client.get_queue_sender(queue_name)


@cache
def _get_topic_sender(connection_string: str, topic_name: str) -> ServiceBusSender:
    """Gets a topic sender."""
    sb_client = _get_service_bus_client(connection_string=connection_string)
    return sb_client.get_topic_sender(topic_name)
