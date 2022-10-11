from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.currency_amount import CurrencyAmount
from ..models.quantity_unit_type import QuantityUnitType

T = TypeVar("T", bound="LineItem")


@attr.s(auto_attribs=True)
class LineItem:
    """
    Attributes:
        description (str): Description contains the details of the line item (i.e t3 micro).
        quantity (float): Quantity is the number of the specific line items used.
        unit_cost (float): UnitCost is the cost per unit of line item.
        total (CurrencyAmount):
        quantity_unit (QuantityUnitType): Billing
            QuantityUnitType is the unit type for a quantity of billing line item.
    """

    description: str
    quantity: float
    unit_cost: float
    total: CurrencyAmount
    quantity_unit: QuantityUnitType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        quantity = self.quantity
        unit_cost = self.unit_cost
        total = self.total.to_dict()

        quantity_unit = self.quantity_unit.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "quantity": quantity,
                "unit_cost": unit_cost,
                "total": total,
                "quantity_unit": quantity_unit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        quantity = d.pop("quantity")

        unit_cost = d.pop("unit_cost")

        total = CurrencyAmount.from_dict(d.pop("total"))

        quantity_unit = QuantityUnitType(d.pop("quantity_unit"))

        line_item = cls(
            description=description,
            quantity=quantity,
            unit_cost=unit_cost,
            total=total,
            quantity_unit=quantity_unit,
        )

        line_item.additional_properties = d
        return line_item

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
