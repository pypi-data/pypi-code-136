"""Subscription module"""
from __future__ import annotations
import os
from enum import Enum
from datetime import datetime, timedelta
from typing import List, Optional, Union

from azure.cosmos import CosmosClient
from pydantic import BaseModel, Field
from ..db.base_repository import BaseRepository


class SubscriptionPlan(str, Enum):
    """Subscription plans"""

    BI_WEEKLY = "Bi-Weekly"
    MONTHLY = "Monthly"


class Subscription(BaseModel):
    """Describes a subscription"""

    id: str  # subscription id in cosmosdb
    customer_id: int
    customer_name: str
    customer_email: str
    customer_phone_number: str
    account_balance: float  # Total amount in subscription
    currency: str
    plan: SubscriptionPlan
    subscription_started: datetime
    subscription_ends: datetime
    is_active: bool # indicates if subscription has expired
    etag: str = Field(default=None, alias="_etag")  # tag for optimistic concurrency:
    # https://docs.microsoft.com/en-us/azure/cosmos-db/sql/database-transactions-optimistic-concurrency


class SubscriptionRepository(BaseRepository):
    """Subscription repository"""

    _cosmos_client: CosmosClient = None

    # pylint: disable=too-few-public-methods
    class Config:
        """Subscription repository config"""

        ContainerName = "subscriptions"
        Model = Subscription

    def create_or_update(self, item: Subscription) -> Union[BaseModel, dict]:
        """update or create a subscription for a customer"""
        subscription = self.get_subscription_by_customer_id(item.customer_id)

        if subscription:
            item.id = subscription.id
            return self.update(item)
        return self.create(item)

    def get_subscription(self, subscription_id: str, customer_id: int) -> Subscription:
        """Get customer's subscription"""
        return self.get(subscription_id, customer_id)

    def get_subscription_by_customer_id(self, customer_id: int) -> Optional[Subscription]:
        """Get a subscription by customer id"""
        queryset: List[Subscription] = self.query(f"SELECT * FROM s \
            WHERE s.customer_id = {customer_id}")
        if queryset:
            return queryset[0]
        return None

    def get_due_subscriptions(self) -> List[Subscription]:
        """Get all subscriptions that are due"""
        queryset: List[Subscription] = self.query(
            f'SELECT * FROM s WHERE (s["subscription_ends"] <= "{datetime.utcnow().isoformat()}") AND s.is_active = true',
            enable_cross_partition_query=True
        )
        return queryset

    def get_due_expirations(self) -> List[Subscription]:
        """Get all subscriptions that are due in 2 days"""
        l_datetime = datetime.utcnow() + timedelta(days=2)
        g_datetime = l_datetime + timedelta(minutes=15)
        queryset: List[Subscription] = self.query(
            f'SELECT * FROM s WHERE (s["subscription_ends"] >= "{l_datetime.isoformat()}") and \
                (s["subscription_ends"] <= "{g_datetime.isoformat()}") AND s.is_active = true',
            enable_cross_partition_query=True
        )
        return queryset

    @classmethod
    def from_env(cls) -> SubscriptionRepository:
        """
        Creates a new SubscriptionRepository instance from the environment.
        Args:
            None.
        Returns:
            The new SubscriptionRepository instance.
        """
        cls._cosmos_client = (
            cls._cosmos_client
            if cls._cosmos_client
            else CosmosClient.from_connection_string(
                os.environ["COSMOSDB_CONNECTION_STRING"]
            )
        )

        return cls(cls._cosmos_client, os.getenv("COSMOSDB_DATABASE_ID", "payments"))
