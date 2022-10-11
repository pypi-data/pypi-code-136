from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.any_ import Any
from ..types import UNSET, Unset

T = TypeVar("T", bound="Status")


@attr.s(auto_attribs=True)
class Status:
    """
    Attributes:
        code (Union[Unset, int]):
        message (Union[Unset, str]):
        details (Union[Unset, List[Any]]):
    """

    code: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    details: Union[Unset, List[Any]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        message = self.message
        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()

                details.append(details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = Any.from_dict(details_item_data)

            details.append(details_item)

        status = cls(
            code=code,
            message=message,
            details=details,
        )

        status.additional_properties = d
        return status

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
