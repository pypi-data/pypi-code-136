from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeysetPaginationResponse")


@attr.s(auto_attribs=True)
class KeysetPaginationResponse:
    """
    Attributes:
        next_page (Union[Unset, str]):
        previous_page (Union[Unset, str]):
    """

    next_page: Union[Unset, str] = UNSET
    previous_page: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        next_page = self.next_page
        previous_page = self.previous_page

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page is not UNSET:
            field_dict["next_page"] = next_page
        if previous_page is not UNSET:
            field_dict["previous_page"] = previous_page

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        next_page = d.pop("next_page", UNSET)

        previous_page = d.pop("previous_page", UNSET)

        keyset_pagination_response = cls(
            next_page=next_page,
            previous_page=previous_page,
        )

        keyset_pagination_response.additional_properties = d
        return keyset_pagination_response

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
