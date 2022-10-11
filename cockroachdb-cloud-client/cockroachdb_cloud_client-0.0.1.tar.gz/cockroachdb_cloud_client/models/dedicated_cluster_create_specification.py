from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dedicated_cluster_create_specification_region_nodes import DedicatedClusterCreateSpecificationRegionNodes
from ..models.dedicated_hardware_create_specification import DedicatedHardwareCreateSpecification
from ..types import UNSET, Unset

T = TypeVar("T", bound="DedicatedClusterCreateSpecification")


@attr.s(auto_attribs=True)
class DedicatedClusterCreateSpecification:
    """
    Attributes:
        region_nodes (DedicatedClusterCreateSpecificationRegionNodes): Region keys should match the cloud provider's
            zone code.
            For example, for Oregon, set region_name to "us-west2" for
            GCP and "us-west-2" for AWS. Values represent the node count.
        hardware (DedicatedHardwareCreateSpecification):
        cockroach_version (Union[Unset, str]): The CockroachDB version for the cluster. The current version
            is used if omitted.
    """

    region_nodes: DedicatedClusterCreateSpecificationRegionNodes
    hardware: DedicatedHardwareCreateSpecification
    cockroach_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_nodes = self.region_nodes.to_dict()

        hardware = self.hardware.to_dict()

        cockroach_version = self.cockroach_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region_nodes": region_nodes,
                "hardware": hardware,
            }
        )
        if cockroach_version is not UNSET:
            field_dict["cockroach_version"] = cockroach_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_nodes = DedicatedClusterCreateSpecificationRegionNodes.from_dict(d.pop("region_nodes"))

        hardware = DedicatedHardwareCreateSpecification.from_dict(d.pop("hardware"))

        cockroach_version = d.pop("cockroach_version", UNSET)

        dedicated_cluster_create_specification = cls(
            region_nodes=region_nodes,
            hardware=hardware,
            cockroach_version=cockroach_version,
        )

        dedicated_cluster_create_specification.additional_properties = d
        return dedicated_cluster_create_specification

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
