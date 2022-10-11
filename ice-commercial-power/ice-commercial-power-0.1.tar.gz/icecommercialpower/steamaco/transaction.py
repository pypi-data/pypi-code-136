"""
Defines a transaction in StemaCo.
"""

from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel


class TransactionCategory(str, Enum):
    """
    The category of the transaction.
    """

    # A payment made by the customer.
    # This is one of only three categories that may be created by API clients.
    PAY = "PAY"

    # A one-off charge issued for a financed asset's down payment.
    DWN = "DWN"

    # A periodic charge issued to pay off a financed asset.
    LN = "LN"

    # A periodic charge issued to pay for a subscription plan.
    SUB = "SUB"

    # A charge issued upon usage of utility.
    UCH = "UCH"

    # A charge issued to top-up an exceeded utility usage limit.
    LIM = "LIM"

    # Cancels a usage limit top-up charge.
    # This is issued when a usage limit top-up charge is unpaid at the end of a subscription period.
    LIC = "LIC"

    # A charge representing an initial connection fee.
    # This must be paid off before the customer begins receiving power.
    CON = "CON"

    # A zero-amount charge indicating the point in time when
    # the customer's connection fee was paid off.
    COF = "COF"

    # An update made to a customer's balance by a Steama user.
    # This is one of only three categories that may be created by API clients.
    UCU = "UCU"

    # An update made to a customer's balance in order to provide them
    # with a daily allotment of power.
    # This will set a customer's balance to zero if it was negative previously.
    # This category is only used in "Per-kWh" tiered tariffs.
    FPA = "FPA"

    # A reversal of the prior payment transaction.
    # This is one of only three categories that may be created by API clients.
    REV = "REV"

    # A record of a customer's negative balance before a payment was made.
    # This category is available for customers with Automatic/Cloud control and "Flat Rate" tariffs.
    NBA = "NBA"


class TransactionProvider(str, Enum):
    """
    Types of providers, responsible for carrying out transactions.
    """

    # The payment was made through the SteamaCo API.
    AP = "AP"

    # The payment was made through the Agent App.
    AA = "AA"

    # The payment was made through the Agent SMS interface.
    AS = "AS"

    # The payment was made by an Agent.
    AG = "AG"

    # The payment was made through Kopo Kopo.
    K2 = "K2"

    # The payment was made though a mobile money provider and was received over SMS.
    MS = "MS"

    # The payment was made through Wave Money.
    WM = "WM"

    # The payment was made through Vodacom.
    VC = "VC"


class Transaction(BaseModel):
    """
    A transaction in SteamaCo.
    """

    id: Optional[int]
    url: Optional[str]
    timestamp: Optional[datetime]
    amount: float
    category: TransactionCategory
    reference: Optional[str]
    raw_message: Optional[str]
    account_balance: Optional[float]
    provider: Optional[TransactionProvider]
    customer_url: Optional[str]
    customer_id: Optional[int]
    customer_first_name: Optional[str]
    customer_last_name: Optional[str]
    customer_telephone: Optional[str]
    currency: Optional[str]
    agent_url: Optional[str]
    agent_id: Optional[str]
    agent_first_name: Optional[str]
    agent_last_name: Optional[str]
    agent_telephone: Optional[str]
    reversed_by_id: Optional[int]
    reversed_by_url: Optional[str]
    reversed_by_reference: Optional[str]
    user: Optional[int]
    username: Optional[str]
    currency_display: Optional[str]
    synchronization_status: Optional[str]

    @classmethod
    def create(
        cls, reference: str, amount: float, raw_text: str = None
    ) -> "Transaction":
        """
        Creates a new transaction.

        Args:
            reference: The reference of the transaction.
            amount: The amount of the transaction.
            raw_text: The raw text of the message.
        """
        return cls(
            reference=reference,
            amount=amount,
            raw_message=raw_text,
            category=TransactionCategory.PAY,
        )
