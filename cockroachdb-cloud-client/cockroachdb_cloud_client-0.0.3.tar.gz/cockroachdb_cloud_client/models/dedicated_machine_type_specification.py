from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DedicatedMachineTypeSpecification")


@attr.s(auto_attribs=True)
class DedicatedMachineTypeSpecification:
    """
    Attributes:
        machine_type (Union[Unset, str]): MachineType is the machine type identifier within the given cloud
            provider, ex. m5.xlarge, n2-standard-4.
        num_virtual_cpus (Union[Unset, int]): NumVirtualCPUs may be used to automatically select a machine type
            according to the desired number of vCPUs.
    """

    machine_type: Union[Unset, str] = UNSET
    num_virtual_cpus: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        machine_type = self.machine_type
        num_virtual_cpus = self.num_virtual_cpus

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if machine_type is not UNSET:
            field_dict["machine_type"] = machine_type
        if num_virtual_cpus is not UNSET:
            field_dict["num_virtual_cpus"] = num_virtual_cpus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        machine_type = d.pop("machine_type", UNSET)

        num_virtual_cpus = d.pop("num_virtual_cpus", UNSET)

        dedicated_machine_type_specification = cls(
            machine_type=machine_type,
            num_virtual_cpus=num_virtual_cpus,
        )

        dedicated_machine_type_specification.additional_properties = d
        return dedicated_machine_type_specification

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
