from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.aws_endpoint_connection import AwsEndpointConnection

T = TypeVar("T", bound="AwsEndpointConnections")


@attr.s(auto_attribs=True)
class AwsEndpointConnections:
    """
    Attributes:
        connections (List[AwsEndpointConnection]): Connections is a list of private endpoints.
    """

    connections: List[AwsEndpointConnection]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()

            connections.append(connections_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connections": connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connections = []
        _connections = d.pop("connections")
        for connections_item_data in _connections:
            connections_item = AwsEndpointConnection.from_dict(connections_item_data)

            connections.append(connections_item)

        aws_endpoint_connections = cls(
            connections=connections,
        )

        aws_endpoint_connections.additional_properties = d
        return aws_endpoint_connections

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
