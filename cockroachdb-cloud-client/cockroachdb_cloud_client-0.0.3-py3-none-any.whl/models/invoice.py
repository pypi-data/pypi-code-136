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
            balances (List[CurrencyAmount]): Balances are the amounts of currency left at the time of the invoice.
            invoice_id (str): InvoiceID is the unique ID representing the invoice.
            invoice_items (List[InvoiceItem]): InvoiceItems are sorted by the cluster name.
            period_end (datetime.datetime): PeriodEnd is the end of the billing period (exclusive).
            period_start (datetime.datetime): PeriodStart is the start of the billing period (inclusive).
            totals (List[CurrencyAmount]): Totals is a list of the total amounts per currency.
    """

    balances: List[CurrencyAmount]
    invoice_id: str
    invoice_items: List[InvoiceItem]
    period_end: datetime.datetime
    period_start: datetime.datetime
    totals: List[CurrencyAmount]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        balances = []
        for balances_item_data in self.balances:
            balances_item = balances_item_data.to_dict()

            balances.append(balances_item)

        invoice_id = self.invoice_id
        invoice_items = []
        for invoice_items_item_data in self.invoice_items:
            invoice_items_item = invoice_items_item_data.to_dict()

            invoice_items.append(invoice_items_item)

        period_end = self.period_end.isoformat()

        period_start = self.period_start.isoformat()

        totals = []
        for totals_item_data in self.totals:
            totals_item = totals_item_data.to_dict()

            totals.append(totals_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "balances": balances,
                "invoice_id": invoice_id,
                "invoice_items": invoice_items,
                "period_end": period_end,
                "period_start": period_start,
                "totals": totals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        balances = []
        _balances = d.pop("balances")
        for balances_item_data in _balances:
            balances_item = CurrencyAmount.from_dict(balances_item_data)

            balances.append(balances_item)

        invoice_id = d.pop("invoice_id")

        invoice_items = []
        _invoice_items = d.pop("invoice_items")
        for invoice_items_item_data in _invoice_items:
            invoice_items_item = InvoiceItem.from_dict(invoice_items_item_data)

            invoice_items.append(invoice_items_item)

        period_end = isoparse(d.pop("period_end"))

        period_start = isoparse(d.pop("period_start"))

        totals = []
        _totals = d.pop("totals")
        for totals_item_data in _totals:
            totals_item = CurrencyAmount.from_dict(totals_item_data)

            totals.append(totals_item)

        invoice = cls(
            balances=balances,
            invoice_id=invoice_id,
            invoice_items=invoice_items,
            period_end=period_end,
            period_start=period_start,
            totals=totals,
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
