from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DedicatedClusterCreateSpecificationRegionNodes")


@attr.s(auto_attribs=True)
class DedicatedClusterCreateSpecificationRegionNodes:
    """Region keys should match the cloud provider's zone code.
    For example, for Oregon, set region_name to "us-west2" for
    GCP and "us-west-2" for AWS. Values represent the node count.

    """

    additional_properties: Dict[str, int] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dedicated_cluster_create_specification_region_nodes = cls()

        dedicated_cluster_create_specification_region_nodes.additional_properties = d
        return dedicated_cluster_create_specification_region_nodes

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
