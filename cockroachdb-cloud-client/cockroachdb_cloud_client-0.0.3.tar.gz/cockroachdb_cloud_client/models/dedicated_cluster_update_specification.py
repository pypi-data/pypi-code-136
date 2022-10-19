from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cmek_region_specification import CMEKRegionSpecification
from ..models.dedicated_cluster_update_specification_region_nodes import DedicatedClusterUpdateSpecificationRegionNodes
from ..models.dedicated_hardware_update_specification import DedicatedHardwareUpdateSpecification
from ..types import UNSET, Unset

T = TypeVar("T", bound="DedicatedClusterUpdateSpecification")


@attr.s(auto_attribs=True)
class DedicatedClusterUpdateSpecification:
    """
    Attributes:
        cmek_region_specs (Union[Unset, List[CMEKRegionSpecification]]): This field should contain the CMEK specs for
            newly added regions. If a
            CMEK spec is provided for an existing region, the request is invalid and
            will fail.
        hardware (Union[Unset, DedicatedHardwareUpdateSpecification]):
        region_nodes (Union[Unset, DedicatedClusterUpdateSpecificationRegionNodes]): Region keys should match the cloud
            provider's zone code.
            For example, for Oregon, set region_name to "us-west2" for
            GCP and "us-west-2" for AWS. Values represent the node count.
    """

    cmek_region_specs: Union[Unset, List[CMEKRegionSpecification]] = UNSET
    hardware: Union[Unset, DedicatedHardwareUpdateSpecification] = UNSET
    region_nodes: Union[Unset, DedicatedClusterUpdateSpecificationRegionNodes] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cmek_region_specs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cmek_region_specs, Unset):
            cmek_region_specs = []
            for cmek_region_specs_item_data in self.cmek_region_specs:
                cmek_region_specs_item = cmek_region_specs_item_data.to_dict()

                cmek_region_specs.append(cmek_region_specs_item)

        hardware: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hardware, Unset):
            hardware = self.hardware.to_dict()

        region_nodes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.region_nodes, Unset):
            region_nodes = self.region_nodes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cmek_region_specs is not UNSET:
            field_dict["cmek_region_specs"] = cmek_region_specs
        if hardware is not UNSET:
            field_dict["hardware"] = hardware
        if region_nodes is not UNSET:
            field_dict["region_nodes"] = region_nodes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cmek_region_specs = []
        _cmek_region_specs = d.pop("cmek_region_specs", UNSET)
        for cmek_region_specs_item_data in _cmek_region_specs or []:
            cmek_region_specs_item = CMEKRegionSpecification.from_dict(cmek_region_specs_item_data)

            cmek_region_specs.append(cmek_region_specs_item)

        _hardware = d.pop("hardware", UNSET)
        hardware: Union[Unset, DedicatedHardwareUpdateSpecification]
        if _hardware is None:
            hardware = None
        elif isinstance(_hardware, Unset):
            hardware = UNSET
        else:
            hardware = DedicatedHardwareUpdateSpecification.from_dict(_hardware)

        _region_nodes = d.pop("region_nodes", UNSET)
        region_nodes: Union[Unset, DedicatedClusterUpdateSpecificationRegionNodes]
        if _region_nodes is None:
            region_nodes = None
        elif isinstance(_region_nodes, Unset):
            region_nodes = UNSET
        else:
            region_nodes = DedicatedClusterUpdateSpecificationRegionNodes.from_dict(_region_nodes)

        dedicated_cluster_update_specification = cls(
            cmek_region_specs=cmek_region_specs,
            hardware=hardware,
            region_nodes=region_nodes,
        )

        dedicated_cluster_update_specification.additional_properties = d
        return dedicated_cluster_update_specification

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
