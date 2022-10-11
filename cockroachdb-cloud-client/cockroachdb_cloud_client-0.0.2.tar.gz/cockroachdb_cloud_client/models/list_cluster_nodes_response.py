from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keyset_pagination_response import KeysetPaginationResponse
from ..models.node import Node
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListClusterNodesResponse")


@attr.s(auto_attribs=True)
class ListClusterNodesResponse:
    """
    Attributes:
        nodes (List[Node]):
        pagination (Union[Unset, KeysetPaginationResponse]):
    """

    nodes: List[Node]
    pagination: Union[Unset, KeysetPaginationResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()

            nodes.append(nodes_item)

        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nodes": nodes,
            }
        )
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = Node.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, KeysetPaginationResponse]
        if _pagination is None:
            pagination = None
        elif isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = KeysetPaginationResponse.from_dict(_pagination)

        list_cluster_nodes_response = cls(
            nodes=nodes,
            pagination=pagination,
        )

        list_cluster_nodes_response.additional_properties = d
        return list_cluster_nodes_response

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
