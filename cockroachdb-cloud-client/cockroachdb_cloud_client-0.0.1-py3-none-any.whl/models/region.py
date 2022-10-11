from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Region")


@attr.s(auto_attribs=True)
class Region:
    """
    Attributes:
        name (str):
        sql_dns (str):
        ui_dns (str):
        node_count (int): NodeCount will be 0 for serverless clusters.
    """

    name: str
    sql_dns: str
    ui_dns: str
    node_count: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        sql_dns = self.sql_dns
        ui_dns = self.ui_dns
        node_count = self.node_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "sql_dns": sql_dns,
                "ui_dns": ui_dns,
                "node_count": node_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        sql_dns = d.pop("sql_dns")

        ui_dns = d.pop("ui_dns")

        node_count = d.pop("node_count")

        region = cls(
            name=name,
            sql_dns=sql_dns,
            ui_dns=ui_dns,
            node_count=node_count,
        )

        region.additional_properties = d
        return region

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
