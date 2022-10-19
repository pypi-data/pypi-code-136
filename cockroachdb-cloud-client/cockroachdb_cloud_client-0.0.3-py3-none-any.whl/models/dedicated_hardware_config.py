from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DedicatedHardwareConfig")


@attr.s(auto_attribs=True)
class DedicatedHardwareConfig:
    """
    Attributes:
        disk_iops (int): DiskIOPs is the number of disk I/O operations per second that are
            permitted on each node in the cluster. Zero indicates the cloud
            provider-specific default.
        machine_type (str): MachineType is the machine type identifier within the given cloud
            provider, ex. m5.xlarge, n2-standard-4.
        memory_gib (float): MemoryGiB is the memory GiB per node in the cluster.
        num_virtual_cpus (int): NumVirtualCPUs is the number of virtual CPUs per node in the cluster.
        storage_gib (int): StorageGiB is the number of storage GiB per node in the cluster.
    """

    disk_iops: int
    machine_type: str
    memory_gib: float
    num_virtual_cpus: int
    storage_gib: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disk_iops = self.disk_iops
        machine_type = self.machine_type
        memory_gib = self.memory_gib
        num_virtual_cpus = self.num_virtual_cpus
        storage_gib = self.storage_gib

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disk_iops": disk_iops,
                "machine_type": machine_type,
                "memory_gib": memory_gib,
                "num_virtual_cpus": num_virtual_cpus,
                "storage_gib": storage_gib,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disk_iops = d.pop("disk_iops")

        machine_type = d.pop("machine_type")

        memory_gib = d.pop("memory_gib")

        num_virtual_cpus = d.pop("num_virtual_cpus")

        storage_gib = d.pop("storage_gib")

        dedicated_hardware_config = cls(
            disk_iops=disk_iops,
            machine_type=machine_type,
            memory_gib=memory_gib,
            num_virtual_cpus=num_virtual_cpus,
            storage_gib=storage_gib,
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
