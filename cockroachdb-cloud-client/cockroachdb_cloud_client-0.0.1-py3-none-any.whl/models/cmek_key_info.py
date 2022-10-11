import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cmek_key_specification import CMEKKeySpecification
from ..models.cmek_status import CMEKStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CMEKKeyInfo")


@attr.s(auto_attribs=True)
class CMEKKeyInfo:
    """CMEKKeyInfo contains the status of a customer-provided key alongside the
    specification.

        Attributes:
            status (Union[Unset, CMEKStatus]): CMEKStatus describes the current status of CMEK for an entire CRDB cluster
                or a CMEK key within a region.

                 - UNKNOWN_STATUS: UNKNOWN should never be used; if it is used, it indicates a bug.
                 - DISABLED: DISABLED corresponds to the state of a cluster or region-level key when
                CMEK has finished being disabled. By default, CMEK will be disabled for
                new clusters.
                 - DISABLING: DISABLING corresponds to the state of a cluster or region-level key when
                CMEK is in the process of being disabled.
                 - DISABLE_FAILED: DISABLE_FAILED corresponds to the state of a cluster or region-level key
                when CMEK has failed to be disabled.
                 - ENABLED: ENABLED corresponds to the state of a cluster or region-level key when
                CMEK is enabled.
                 - ENABLING: ENABLING corresponds to the state of a cluster or region-level key when
                CMEK is in the process of being enabled.
                 - ENABLE_FAILED: ENABLE_FAILED corresponds to the state of a cluster or region-level key
                when CMEK has failed to be enabled.
                 - ROTATING: ROTATING corresponds to the state of a cluster or region when the a new
                spec is in the process of being enabled while an existing spec is being
                disabled.
                 - ROTATE_FAILED: ROTATE_FAILED corresponds to the state of a cluster or region if there was
                a failure to update from one CMEK spec to another.
                 - REVOKED: REVOKED corresponds to the state of a cluster or region-level key when the
                customer has revoked CockroachLab's permissions for their key.
                 - REVOKING: REVOKING corresponds to the state of a cluster or region-level key when
                CMEK is in the process of being revoked.
                 - REVOKE_FAILED: REVOKE_FAILED corresponds to the state of a cluster or region-level key
                when CMEK has failed to be revoked.
            user_message (Union[Unset, str]):
            spec (Union[Unset, CMEKKeySpecification]): CMEKKeySpecification contains all the details necessary to use a
                customer-provided
                encryption key. This involves the type/location of the key and the principal
                to authenticate as when accessing it.
            created_at (Union[Unset, datetime.datetime]):
            updated_at (Union[Unset, datetime.datetime]):
    """

    status: Union[Unset, CMEKStatus] = UNSET
    user_message: Union[Unset, str] = UNSET
    spec: Union[Unset, CMEKKeySpecification] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        user_message = self.user_message
        spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if user_message is not UNSET:
            field_dict["user_message"] = user_message
        if spec is not UNSET:
            field_dict["spec"] = spec
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, CMEKStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CMEKStatus(_status)

        user_message = d.pop("user_message", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, CMEKKeySpecification]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = CMEKKeySpecification.from_dict(_spec)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        cmek_key_info = cls(
            status=status,
            user_message=user_message,
            spec=spec,
            created_at=created_at,
            updated_at=updated_at,
        )

        cmek_key_info.additional_properties = d
        return cmek_key_info

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
