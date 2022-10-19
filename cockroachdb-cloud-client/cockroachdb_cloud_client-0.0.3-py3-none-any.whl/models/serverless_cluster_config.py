from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ServerlessClusterConfig")


@attr.s(auto_attribs=True)
class ServerlessClusterConfig:
    """
    Attributes:
        routing_id (str): Used to build a connection string.
        spend_limit (int): Spend limit in US cents.
    """

    routing_id: str
    spend_limit: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        routing_id = self.routing_id
        spend_limit = self.spend_limit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "routing_id": routing_id,
                "spend_limit": spend_limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        routing_id = d.pop("routing_id")

        spend_limit = d.pop("spend_limit")

        serverless_cluster_config = cls(
            routing_id=routing_id,
            spend_limit=spend_limit,
        )

        serverless_cluster_config.additional_properties = d
        return serverless_cluster_config

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
