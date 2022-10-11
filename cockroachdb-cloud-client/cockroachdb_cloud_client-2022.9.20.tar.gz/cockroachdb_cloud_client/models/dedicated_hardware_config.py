from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DedicatedHardwareConfig")


@attr.s(auto_attribs=True)
class DedicatedHardwareConfig:
    """
    Attributes:
        machine_type (str): MachineType is the machine type identifier within the given cloud
            provider, ex. m5.xlarge, n2-standard-4.
        num_virtual_cpus (int): NumVirtualCPUs is the number of virtual CPUs per node in the cluster.
        storage_gib (int): StorageGiB is the number of storage GiB per node in the cluster.
        memory_gib (float): MemoryGiB is the memory GiB per node in the cluster.
        disk_iops (int): DiskIOPs is the number of disk I/O operations per second that are
            permitted on each node in the cluster. Zero indicates the cloud
            provider-specific default.
    """

    machine_type: str
    num_virtual_cpus: int
    storage_gib: int
    memory_gib: float
    disk_iops: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        machine_type = self.machine_type
        num_virtual_cpus = self.num_virtual_cpus
        storage_gib = self.storage_gib
        memory_gib = self.memory_gib
        disk_iops = self.disk_iops

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "machine_type": machine_type,
                "num_virtual_cpus": num_virtual_cpus,
                "storage_gib": storage_gib,
                "memory_gib": memory_gib,
                "disk_iops": disk_iops,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        machine_type = d.pop("machine_type")

        num_virtual_cpus = d.pop("num_virtual_cpus")

        storage_gib = d.pop("storage_gib")

        memory_gib = d.pop("memory_gib")

        disk_iops = d.pop("disk_iops")

        dedicated_hardware_config = cls(
            machine_type=machine_type,
            num_virtual_cpus=num_virtual_cpus,
            storage_gib=storage_gib,
            memory_gib=memory_gib,
            disk_iops=disk_iops,
        )

        dedicated_hardware_config.additional_properties = d
        return dedicated_hardware_config

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
