from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dedicated_machine_type_specification import DedicatedMachineTypeSpecification
from ..types import UNSET, Unset

T = TypeVar("T", bound="DedicatedHardwareCreateSpecification")


@attr.s(auto_attribs=True)
class DedicatedHardwareCreateSpecification:
    """
    Attributes:
        machine_spec (DedicatedMachineTypeSpecification):
        storage_gib (int): StorageGiB is the number of storage GiB per node in the cluster.
            Zero indicates default to the lowest storage GiB available given machine specs.
        disk_iops (Union[Unset, int]): DiskIOPs is the number of disk I/O operations per second that are
            permitted on each node in the cluster. Zero indicates the cloud
            provider-specific default. Only available for AWS clusters.
    """

    machine_spec: DedicatedMachineTypeSpecification
    storage_gib: int
    disk_iops: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        machine_spec = self.machine_spec.to_dict()

        storage_gib = self.storage_gib
        disk_iops = self.disk_iops

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "machine_spec": machine_spec,
                "storage_gib": storage_gib,
            }
        )
        if disk_iops is not UNSET:
            field_dict["disk_iops"] = disk_iops

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        machine_spec = DedicatedMachineTypeSpecification.from_dict(d.pop("machine_spec"))

        storage_gib = d.pop("storage_gib")

        disk_iops = d.pop("disk_iops", UNSET)

        dedicated_hardware_create_specification = cls(
            machine_spec=machine_spec,
            storage_gib=storage_gib,
            disk_iops=disk_iops,
        )

        dedicated_hardware_create_specification.additional_properties = d
        return dedicated_hardware_create_specification

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
