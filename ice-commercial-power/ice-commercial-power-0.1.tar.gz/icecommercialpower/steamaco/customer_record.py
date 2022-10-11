"""
Steamaco Customer and Tag
"""
# pylint: disable=too-few-public-methods
from typing import List, Optional
from pydantic import BaseModel


class Tag(BaseModel):
    """
    Tag for a customer.
    """

    id: int
    name: str
    url: Optional[str]


class CustomerRecord(BaseModel):
    """Steamaco Customer Record."""

    id: int
    url: str
    transactions_url: str
    utilities_url: str
    messages_url: str
    meters_url: str
    revenue_url: str
    balances_url: str
    audit_log_url: str
    telephone: str
    first_name: str
    last_name: str
    account_balance: float
    energy_price: float
    low_balance_warning: float
    low_balance_level: float
    control_type: str
    is_user: bool
    is_field_manager: bool
    is_demo: str
    language: str
    user_type: str
    payment_plan: Optional[str]
    utility_use_30_days: dict
    labels: dict
    tags_url: str
    created: str
    is_archived: Optional[bool]
    TOU_hours: str
    integration_id: Optional[str]
    tags: Optional[List[Tag]]
    site_manager: Optional[str]
    site_manager_name: Optional[str]
    site_manager_url: Optional[str]
    site_manager_telephone: Optional[str]
    site: Optional[int]
    site_url: Optional[str]
    site_name: Optional[str]
    bit_harvester: Optional[int]
    bit_harvester_name: Optional[str]
    bit_harvester_url: Optional[str]
    bit_harvester_telephone: Optional[str]
