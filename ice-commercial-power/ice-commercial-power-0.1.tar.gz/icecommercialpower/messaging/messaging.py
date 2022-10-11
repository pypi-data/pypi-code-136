"""
Schemas for Service Bus queue messages.
"""
import os
from pydantic import BaseModel


def get_flutterwave_checks_queue_name() -> str:
    """Gets the Flutterwave queue name"""
    return os.getenv("FLUTTERWAVE_QUEUE_NAME", "flutterwave_checks")


def get_paid_payments_queue_name() -> str:
    """Gets the paid payments queue name"""
    return os.getenv("PAID_PAYMENTS_QUEUE_NAME", "paid_payments")


def get_synced_payments_topic_name() -> str:
    """Gets the synced payments topic name"""
    return os.getenv("SYNCED_PAYMENTS_TOPIC_NAME", "synced_payments")


class FwChecksMessage(BaseModel):
    """Message from the flutterwave_checks queue"""

    tx_id: int
    tx_ref: str
    customer_id: int
    retry_count: int = 0


class PaidPaymentsMessage(BaseModel):
    """
    Message from the paid_payments queue.
    Informs about a payment that has been paid in FlutterWave.
    """

    tx_id: int
    tx_ref: str
    customer_id: int


class SyncedPaymentsMessage(BaseModel):
    """
    Message from the synced_payments topic.
    Informs about a payment that has been synced to SteamaCo.
    """

    tx_ref: str
    customer_id: int
