import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.sort_order import SortOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeysetPaginationRequest")


@attr.s(auto_attribs=True)
class KeysetPaginationRequest:
    """
    Attributes:
        page (Union[Unset, str]):
        limit (Union[Unset, int]):
        as_of_time (Union[Unset, datetime.datetime]):
        sort_order (Union[Unset, SortOrder]):  - DESC: Sort in descending order. The default order is ascending.
    """

    page: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET
    as_of_time: Union[Unset, datetime.datetime] = UNSET
    sort_order: Union[Unset, SortOrder] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        page = self.page
        limit = self.limit
        as_of_time: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_time, Unset):
            as_of_time = self.as_of_time.isoformat()

        sort_order: Union[Unset, str] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if limit is not UNSET:
            field_dict["limit"] = limit
        if as_of_time is not UNSET:
            field_dict["as_of_time"] = as_of_time
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        page = d.pop("page", UNSET)

        limit = d.pop("limit", UNSET)

        _as_of_time = d.pop("as_of_time", UNSET)
        as_of_time: Union[Unset, datetime.datetime]
        if isinstance(_as_of_time, Unset):
            as_of_time = UNSET
        else:
            as_of_time = isoparse(_as_of_time)

        _sort_order = d.pop("sort_order", UNSET)
        sort_order: Union[Unset, SortOrder]
        if isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortOrder(_sort_order)

        keyset_pagination_request = cls(
            page=page,
            limit=limit,
            as_of_time=as_of_time,
            sort_order=sort_order,
        )

        keyset_pagination_request.additional_properties = d
        return keyset_pagination_request

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
