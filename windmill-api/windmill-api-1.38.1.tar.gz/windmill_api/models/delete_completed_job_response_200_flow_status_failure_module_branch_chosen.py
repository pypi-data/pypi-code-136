from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.delete_completed_job_response_200_flow_status_failure_module_branch_chosen_type import (
    DeleteCompletedJobResponse200FlowStatusFailureModuleBranchChosenType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteCompletedJobResponse200FlowStatusFailureModuleBranchChosen")


@attr.s(auto_attribs=True)
class DeleteCompletedJobResponse200FlowStatusFailureModuleBranchChosen:
    """ """

    type: Union[Unset, DeleteCompletedJobResponse200FlowStatusFailureModuleBranchChosenType] = UNSET
    branch: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        branch = self.branch

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if branch is not UNSET:
            field_dict["branch"] = branch

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type: Union[Unset, DeleteCompletedJobResponse200FlowStatusFailureModuleBranchChosenType] = UNSET
        _type = d.pop("type", UNSET)
        if not isinstance(_type, Unset):
            type = DeleteCompletedJobResponse200FlowStatusFailureModuleBranchChosenType(_type)

        branch = d.pop("branch", UNSET)

        delete_completed_job_response_200_flow_status_failure_module_branch_chosen = cls(
            type=type,
            branch=branch,
        )

        delete_completed_job_response_200_flow_status_failure_module_branch_chosen.additional_properties = d
        return delete_completed_job_response_200_flow_status_failure_module_branch_chosen

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
