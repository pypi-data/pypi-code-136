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
        as_of_time (Union[Unset, datetime.datetime]):
        limit (Union[Unset, int]):
        page (Union[Unset, str]):
        sort_order (Union[Unset, SortOrder]):  - DESC: Sort in descending order. The default order is ascending.
    """

    as_of_time: Union[Unset, datetime.datetime] = UNSET
    limit: Union[Unset, int] = UNSET
    page: Union[Unset, str] = UNSET
    sort_order: Union[Unset, SortOrder] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        as_of_time: Union[Unset, str] = UNSET
        if not isinstance(self.as_of_time, Unset):
            as_of_time = self.as_of_time.isoformat()

        limit = self.limit
        page = self.page
        sort_order: Union[Unset, str] = UNSET
        if not isinstance(self.sort_order, Unset):
            sort_order = self.sort_order.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of_time is not UNSET:
            field_dict["as_of_time"] = as_of_time
        if limit is not UNSET:
            field_dict["limit"] = limit
        if page is not UNSET:
            field_dict["page"] = page
        if sort_order is not UNSET:
            field_dict["sort_order"] = sort_order

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _as_of_time = d.pop("as_of_time", UNSET)
        as_of_time: Union[Unset, datetime.datetime]
        if _as_of_time is None:
            as_of_time = None
        elif isinstance(_as_of_time, Unset):
            as_of_time = UNSET
        else:
            as_of_time = isoparse(_as_of_time)

        limit = d.pop("limit", UNSET)

        page = d.pop("page", UNSET)

        _sort_order = d.pop("sort_order", UNSET)
        sort_order: Union[Unset, SortOrder]
        if _sort_order is None:
            sort_order = None
        elif isinstance(_sort_order, Unset):
            sort_order = UNSET
        else:
            sort_order = SortOrder(_sort_order)

        keyset_pagination_request = cls(
            as_of_time=as_of_time,
            limit=limit,
            page=page,
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
