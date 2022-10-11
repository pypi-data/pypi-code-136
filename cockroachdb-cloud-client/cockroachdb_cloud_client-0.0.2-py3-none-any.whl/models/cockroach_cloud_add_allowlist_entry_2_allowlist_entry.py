from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CockroachCloudAddAllowlistEntry2AllowlistEntry")


@attr.s(auto_attribs=True)
class CockroachCloudAddAllowlistEntry2AllowlistEntry:
    """
    Example:
        {'cidr_ip': '192.168.1.1', 'cidr_mask': 32, 'ui': True, 'sql': True, 'name': 'Example'}

    Attributes:
        ui (bool):
        sql (bool):
        name (Union[Unset, str]):
    """

    ui: bool
    sql: bool
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ui = self.ui
        sql = self.sql
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ui": ui,
                "sql": sql,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ui = d.pop("ui")

        sql = d.pop("sql")

        name = d.pop("name", UNSET)

        cockroach_cloud_add_allowlist_entry_2_allowlist_entry = cls(
            ui=ui,
            sql=sql,
            name=name,
        )

        cockroach_cloud_add_allowlist_entry_2_allowlist_entry.additional_properties = d
        return cockroach_cloud_add_allowlist_entry_2_allowlist_entry

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
