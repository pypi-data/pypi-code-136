import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.currency_amount import CurrencyAmount
from ..models.invoice_item import InvoiceItem

T = TypeVar("T", bound="Invoice")


@attr.s(auto_attribs=True)
class Invoice:
    """Invoice message represents the details and the total charges associated with
    one billing period, which starts at the beginning of the month and ends at
    the beginning of the next month. The message also includes details about each
    invoice item.

        Attributes:
            invoice_id (str): InvoiceID is the unique ID representing the invoice.
            totals (List[CurrencyAmount]): Totals is a list of the total amounts per currency.
            period_start (datetime.datetime): PeriodStart is the start of the billing period (inclusive).
            period_end (datetime.datetime): PeriodEnd is the end of the billing period (exclusive).
            invoice_items (List[InvoiceItem]): InvoiceItems are sorted by the cluster name.
            balances (List[CurrencyAmount]): Balances are the amounts of currency left at the time of the invoice.
    """

    invoice_id: str
    totals: List[CurrencyAmount]
    period_start: datetime.datetime
    period_end: datetime.datetime
    invoice_items: List[InvoiceItem]
    balances: List[CurrencyAmount]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_id = self.invoice_id
        totals = []
        for totals_item_data in self.totals:
            totals_item = totals_item_data.to_dict()

            totals.append(totals_item)

        period_start = self.period_start.isoformat()

        period_end = self.period_end.isoformat()

        invoice_items = []
        for invoice_items_item_data in self.invoice_items:
            invoice_items_item = invoice_items_item_data.to_dict()

            invoice_items.append(invoice_items_item)

        balances = []
        for balances_item_data in self.balances:
            balances_item = balances_item_data.to_dict()

            balances.append(balances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoice_id": invoice_id,
                "totals": totals,
                "period_start": period_start,
                "period_end": period_end,
                "invoice_items": invoice_items,
                "balances": balances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoice_id = d.pop("invoice_id")

        totals = []
        _totals = d.pop("totals")
        for totals_item_data in _totals:
            totals_item = CurrencyAmount.from_dict(totals_item_data)

            totals.append(totals_item)

        period_start = isoparse(d.pop("period_start"))

        period_end = isoparse(d.pop("period_end"))

        invoice_items = []
        _invoice_items = d.pop("invoice_items")
        for invoice_items_item_data in _invoice_items:
            invoice_items_item = InvoiceItem.from_dict(invoice_items_item_data)

            invoice_items.append(invoice_items_item)

        balances = []
        _balances = d.pop("balances")
        for balances_item_data in _balances:
            balances_item = CurrencyAmount.from_dict(balances_item_data)

            balances.append(balances_item)

        invoice = cls(
            invoice_id=invoice_id,
            totals=totals,
            period_start=period_start,
            period_end=period_end,
            invoice_items=invoice_items,
            balances=balances,
        )

        invoice.additional_properties = d
        return invoice

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
