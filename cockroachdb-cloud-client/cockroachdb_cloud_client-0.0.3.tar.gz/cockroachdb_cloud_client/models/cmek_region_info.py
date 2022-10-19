from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cmek_key_info import CMEKKeyInfo
from ..models.cmek_status import CMEKStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CMEKRegionInfo")


@attr.s(auto_attribs=True)
class CMEKRegionInfo:
    """CMEKRegionInfo contains the status of CMEK within a region. This includes
    current and past key specifications used within the region, as well as the
    status of those specifications.

        Attributes:
            key_infos (Union[Unset, List[CMEKKeyInfo]]):
            region (Union[Unset, str]):
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
    """

    key_infos: Union[Unset, List[CMEKKeyInfo]] = UNSET
    region: Union[Unset, str] = UNSET
    status: Union[Unset, CMEKStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.key_infos, Unset):
            key_infos = []
            for key_infos_item_data in self.key_infos:
                key_infos_item = key_infos_item_data.to_dict()

                key_infos.append(key_infos_item)

        region = self.region
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key_infos is not UNSET:
            field_dict["key_infos"] = key_infos
        if region is not UNSET:
            field_dict["region"] = region
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_infos = []
        _key_infos = d.pop("key_infos", UNSET)
        for key_infos_item_data in _key_infos or []:
            key_infos_item = CMEKKeyInfo.from_dict(key_infos_item_data)

            key_infos.append(key_infos_item)

        region = d.pop("region", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CMEKStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = CMEKStatus(_status)

        cmek_region_info = cls(
            key_infos=key_infos,
            region=region,
            status=status,
        )

        cmek_region_info.additional_properties = d
        return cmek_region_info

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
