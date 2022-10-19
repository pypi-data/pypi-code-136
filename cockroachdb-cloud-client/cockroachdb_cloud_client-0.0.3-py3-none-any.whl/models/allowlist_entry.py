from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AllowlistEntry")


@attr.s(auto_attribs=True)
class AllowlistEntry:
    """
    Example:
        {'cidr_ip': '192.168.1.1', 'cidr_mask': 32, 'name': 'Example', 'sql': True, 'ui': True}

    Attributes:
        cidr_ip (str):
        cidr_mask (int):
        sql (bool):
        ui (bool):
        name (Union[Unset, str]):
    """

    cidr_ip: str
    cidr_mask: int
    sql: bool
    ui: bool
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cidr_ip = self.cidr_ip
        cidr_mask = self.cidr_mask
        sql = self.sql
        ui = self.ui
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cidr_ip": cidr_ip,
                "cidr_mask": cidr_mask,
                "sql": sql,
                "ui": ui,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cidr_ip = d.pop("cidr_ip")

        cidr_mask = d.pop("cidr_mask")

        sql = d.pop("sql")

        ui = d.pop("ui")

        name = d.pop("name", UNSET)

        allowlist_entry = cls(
            cidr_ip=cidr_ip,
            cidr_mask=cidr_mask,
            sql=sql,
            ui=ui,
            name=name,
        )

        allowlist_entry.additional_properties = d
        return allowlist_entry

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
