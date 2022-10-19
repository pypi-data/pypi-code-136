from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.invoice import Invoice

T = TypeVar("T", bound="ListInvoicesResponse")


@attr.s(auto_attribs=True)
class ListInvoicesResponse:
    """
    Attributes:
        invoices (List[Invoice]): Invoices are sorted by PeriodStart time.
    """

    invoices: List[Invoice]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoices = []
        for invoices_item_data in self.invoices:
            invoices_item = invoices_item_data.to_dict()

            invoices.append(invoices_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoices": invoices,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        invoices = []
        _invoices = d.pop("invoices")
        for invoices_item_data in _invoices:
            invoices_item = Invoice.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        list_invoices_response = cls(
            invoices=invoices,
        )

        list_invoices_response.additional_properties = d
        return list_invoices_response

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
