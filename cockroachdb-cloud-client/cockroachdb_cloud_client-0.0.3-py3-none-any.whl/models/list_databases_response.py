from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.database import Database
from ..models.keyset_pagination_response import KeysetPaginationResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListDatabasesResponse")


@attr.s(auto_attribs=True)
class ListDatabasesResponse:
    """
    Attributes:
        databases (List[Database]):
        pagination (Union[Unset, KeysetPaginationResponse]):
    """

    databases: List[Database]
    pagination: Union[Unset, KeysetPaginationResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        databases = []
        for databases_item_data in self.databases:
            databases_item = databases_item_data.to_dict()

            databases.append(databases_item)

        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "databases": databases,
            }
        )
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        databases = []
        _databases = d.pop("databases")
        for databases_item_data in _databases:
            databases_item = Database.from_dict(databases_item_data)

            databases.append(databases_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, KeysetPaginationResponse]
        if _pagination is None:
            pagination = None
        elif isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = KeysetPaginationResponse.from_dict(_pagination)

        list_databases_response = cls(
            databases=databases,
            pagination=pagination,
        )

        list_databases_response.additional_properties = d
        return list_databases_response

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
