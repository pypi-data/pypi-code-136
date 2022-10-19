from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.node_status import NodeStatus

T = TypeVar("T", bound="Node")


@attr.s(auto_attribs=True)
class Node:
    """
    Attributes:
        name (str):
        region_name (str):
        status (NodeStatus):
    """

    name: str
    region_name: str
    status: NodeStatus
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        region_name = self.region_name
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "region_name": region_name,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        region_name = d.pop("region_name")

        status = NodeStatus(d.pop("status"))

        node = cls(
            name=name,
            region_name=region_name,
            status=status,
        )

        node.additional_properties = d
        return node

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
