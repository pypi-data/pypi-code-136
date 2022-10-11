"""Payments module"""
from __future__ import annotations
import os
from enum import Enum
from datetime import datetime
from typing import Optional

from azure.cosmos import CosmosClient
from pydantic import BaseModel, Field
from ..db.base_repository import BaseRepository


class PaymentStatus(str, Enum):
    """Statuses for payments"""

    PENDING = "PENDING"
    PAID = "PAID"
    SYNCED = "SYNCED"
    FAILED = "FAILED"


class NotificationStatus(str, Enum):
    """Status for notifications"""

    NOT_STARTED = "NOT_STARTED"
    NOTIFYING = "NOTIFYING"
    NOTIFIED = "NOTIFIED"


class Payment(BaseModel):
    """Describes a payment"""

    id: str  # tx_ref in FlutterWave
    date_created: datetime  # date it was created
    customer_phone_number: str
    customer_email: str
    customer_name: str
    customer_id: int
    integration_id: Optional[str]
    site_name: Optional[str]
    status: PaymentStatus
    notification: NotificationStatus
    notification_date: Optional[datetime]  # date the notification was sent
    amount: float  # Amount chosen by the customer to pay
    subscription_plan: Optional[str] = None # plan selected by the customer
    charged_amount: Optional[float]  # Amount charged by Flutterwave (amount + fees)
    """
    amount_settled: Depends on Flutterwave fee settings (charged to customer or to ICE).
    If charged to customer fees are not included, else fees are.
    """
    amount_settled: Optional[float] = None
    app_fee: Optional[float] = None  # Fee charged by Flutterwave
    merchant_fee: Optional[
        float
    ] = None  # Uncertain what this is. Awaiting clarification from Flutterwave
    currency: str
    external_id: str  # payment id in external system
    external_ref: str  # payment reference in external system
    steamaco_id: Optional[int]
    steamaco_synced_at: Optional[datetime]
    etag: str = Field(default=None, alias="_etag")  # tag for optimistic concurrency:
    # https://docs.microsoft.com/en-us/azure/cosmos-db/sql/database-transactions-optimistic-concurrency


class PaymentRepository(BaseRepository):
    """Repository for payments"""

    _cosmos_client: CosmosClient = None

    # pylint: disable=too-few-public-methods
    class Config:
        """Repository configuration"""

        ContainerName = "payments"
        Model = Payment

    def create_or_update(self, item: Payment) -> None:
        """Not allowed: Either create or update a payment"""
        raise NotImplementedError("Should not update or create a payment")

    def get_payment(self, payment_id: str, customer_id: int) -> Payment:
        """Get a payment"""
        return self.get(item_id=payment_id, partition_key=customer_id)

    @classmethod
    def from_env(cls) -> PaymentRepository:
        """
        Creates a new PaymentRepository instance from the environment.
        Args:
            None.
        Returns:
            The new PaymentRepository instance.
        """
        cls._cosmos_client = (
            cls._cosmos_client
            if cls._cosmos_client
            else CosmosClient.from_connection_string(
                os.environ["COSMOSDB_CONNECTION_STRING"]
            )
        )

        return cls(cls._cosmos_client, os.getenv("COSMOSDB_DATABASE_ID", "payments"))
