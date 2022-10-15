from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.branch_all_branches_item_modules_item import BranchAllBranchesItemModulesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="BranchAllBranchesItem")


@attr.s(auto_attribs=True)
class BranchAllBranchesItem:
    """ """

    modules: List[BranchAllBranchesItemModulesItem]
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modules = []
        for modules_item_data in self.modules:
            modules_item = modules_item_data.to_dict()

            modules.append(modules_item)

        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modules": modules,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        modules = []
        _modules = d.pop("modules")
        for modules_item_data in _modules:
            modules_item = BranchAllBranchesItemModulesItem.from_dict(modules_item_data)

            modules.append(modules_item)

        summary = d.pop("summary", UNSET)

        branch_all_branches_item = cls(
            modules=modules,
            summary=summary,
        )

        branch_all_branches_item.additional_properties = d
        return branch_all_branches_item

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
