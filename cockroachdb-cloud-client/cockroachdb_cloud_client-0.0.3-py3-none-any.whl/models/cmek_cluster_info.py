from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cmek_region_info import CMEKRegionInfo
from ..models.cmek_status import CMEKStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CMEKClusterInfo")


@attr.s(auto_attribs=True)
class CMEKClusterInfo:
    """CMEKClusterInfo contains the status of CMEK across an entire cluster,
    including within each one its regions.

        Attributes:
            region_infos (Union[Unset, List[CMEKRegionInfo]]):
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

    region_infos: Union[Unset, List[CMEKRegionInfo]] = UNSET
    status: Union[Unset, CMEKStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.region_infos, Unset):
            region_infos = []
            for region_infos_item_data in self.region_infos:
                region_infos_item = region_infos_item_data.to_dict()

                region_infos.append(region_infos_item)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_infos is not UNSET:
            field_dict["region_infos"] = region_infos
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_infos = []
        _region_infos = d.pop("region_infos", UNSET)
        for region_infos_item_data in _region_infos or []:
            region_infos_item = CMEKRegionInfo.from_dict(region_infos_item_data)

            region_infos.append(region_infos_item)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CMEKStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = CMEKStatus(_status)

        cmek_cluster_info = cls(
            region_infos=region_infos,
            status=status,
        )

        cmek_cluster_info.additional_properties = d
        return cmek_cluster_info

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
