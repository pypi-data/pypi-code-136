from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="Region")


@attr.s(auto_attribs=True)
class Region:
    """
    Attributes:
        internal_dns (str): InternalDns is the internal DNS name of the cluster within the cloud provider's network. It
            is used to connect to the cluster with PrivateLink or VPC peering.
        name (str):
        node_count (int): NodeCount will be 0 for serverless clusters.
        sql_dns (str): SqlDns is the DNS name of SQL interface of the cluster. It is used to connect to the cluster with
            IP allowlisting.
        ui_dns (str): UiDns is the DNS name used when connecting to the DB Console for the cluster.
    """

    internal_dns: str
    name: str
    node_count: int
    sql_dns: str
    ui_dns: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        internal_dns = self.internal_dns
        name = self.name
        node_count = self.node_count
        sql_dns = self.sql_dns
        ui_dns = self.ui_dns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "internal_dns": internal_dns,
                "name": name,
                "node_count": node_count,
                "sql_dns": sql_dns,
                "ui_dns": ui_dns,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        internal_dns = d.pop("internal_dns")

        name = d.pop("name")

        node_count = d.pop("node_count")

        sql_dns = d.pop("sql_dns")

        ui_dns = d.pop("ui_dns")

        region = cls(
            internal_dns=internal_dns,
            name=name,
            node_count=node_count,
            sql_dns=sql_dns,
            ui_dns=ui_dns,
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
