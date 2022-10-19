from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cmek_key_type import CMEKKeyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CMEKKeySpecification")


@attr.s(auto_attribs=True)
class CMEKKeySpecification:
    """CMEKKeySpecification contains all the details necessary to use a customer-provided
    encryption key. This involves the type/location of the key and the principal
    to authenticate as when accessing it.

        Attributes:
            auth_principal (Union[Unset, str]):
            type (Union[Unset, CMEKKeyType]): CMEKKeyType enumerates types of customer-managed keys.

                 - UNKNOWN_KEY_TYPE: UNKNOWN should never be used; if it is used, it indicates a bug.
            uri (Union[Unset, str]):
    """

    auth_principal: Union[Unset, str] = UNSET
    type: Union[Unset, CMEKKeyType] = UNSET
    uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auth_principal = self.auth_principal
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        uri = self.uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_principal is not UNSET:
            field_dict["auth_principal"] = auth_principal
        if type is not UNSET:
            field_dict["type"] = type
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auth_principal = d.pop("auth_principal", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CMEKKeyType]
        if _type is None:
            type = None
        elif isinstance(_type, Unset):
            type = UNSET
        else:
            type = CMEKKeyType(_type)

        uri = d.pop("uri", UNSET)

        cmek_key_specification = cls(
            auth_principal=auth_principal,
            type=type,
            uri=uri,
        )

        cmek_key_specification.additional_properties = d
        return cmek_key_specification

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
