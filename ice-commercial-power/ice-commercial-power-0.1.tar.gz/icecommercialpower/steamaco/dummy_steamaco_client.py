"""
Dummy SteamaCoClient.
"""
# pylint: disable=too-few-public-methods,too-many-instance-attributes,missing-function-docstring

from typing import List, Optional, Sequence

from .customer_record import CustomerRecord
from .meter_record import MeterRecord
from .transaction import Transaction


class DummySteamaCoClient:
    """
    Dummy that emulates a SteamaCo REST API client.
    Exposes the same interface, but instead of querying SteamaCo,
    stores all data in-memory.
    """

    def __init__(
        self,
        customers: Sequence[CustomerRecord] = (),
        transactions: Sequence[Transaction] = (),
        meters: Sequence[MeterRecord] = (),
    ):
        self.customers = list(customers)
        self.transactions = list(transactions)
        self.meters = list(meters)

    def get_customer_by_phone_number(self, phone_number) -> Optional[CustomerRecord]:
        for customer in self.customers:
            if customer.telephone == phone_number:
                return customer
        return None

    def get_meters(self) -> List[MeterRecord]:
        return list(self.meters)

    def get_customers(self) -> List[CustomerRecord]:
        return list(self.customers)

    def get_customer_by_id(self, customer_id: int) -> Optional[CustomerRecord]:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def get_customer_transactions(
        self, customer_id: int, reference: str = None
    ) -> List[Transaction]:
        return [
            t
            for t in self.transactions
            if t.customer_id == customer_id and t.reference == reference
        ]

    def create_customer_transaction(
        self, customer_id: int, transaction: Transaction
    ) -> Transaction:
        created_transaction = transaction.copy(deep=True)
        created_transaction.customer_id = customer_id
        created_transaction.id = max([t.id for t in self.transactions], default=0) + 1
        self.transactions.append(created_transaction)
        return created_transaction
