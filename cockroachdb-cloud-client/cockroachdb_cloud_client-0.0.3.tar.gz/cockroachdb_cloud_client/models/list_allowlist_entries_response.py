from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.allowlist_entry import AllowlistEntry
from ..models.keyset_pagination_response import KeysetPaginationResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAllowlistEntriesResponse")


@attr.s(auto_attribs=True)
class ListAllowlistEntriesResponse:
    """
    Attributes:
        allowlist (List[AllowlistEntry]):
        propagating (bool):
        pagination (Union[Unset, KeysetPaginationResponse]):
    """

    allowlist: List[AllowlistEntry]
    propagating: bool
    pagination: Union[Unset, KeysetPaginationResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowlist = []
        for allowlist_item_data in self.allowlist:
            allowlist_item = allowlist_item_data.to_dict()

            allowlist.append(allowlist_item)

        propagating = self.propagating
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowlist": allowlist,
                "propagating": propagating,
            }
        )
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowlist = []
        _allowlist = d.pop("allowlist")
        for allowlist_item_data in _allowlist:
            allowlist_item = AllowlistEntry.from_dict(allowlist_item_data)

            allowlist.append(allowlist_item)

        propagating = d.pop("propagating")

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, KeysetPaginationResponse]
        if _pagination is None:
            pagination = None
        elif isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = KeysetPaginationResponse.from_dict(_pagination)

        list_allowlist_entries_response = cls(
            allowlist=allowlist,
            propagating=propagating,
            pagination=pagination,
        )

        list_allowlist_entries_response.additional_properties = d
        return list_allowlist_entries_response

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
