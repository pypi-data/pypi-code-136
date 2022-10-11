import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.log_export_cluster_specification import LogExportClusterSpecification
from ..models.log_export_status import LogExportStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LogExportClusterInfo")


@attr.s(auto_attribs=True)
class LogExportClusterInfo:
    """LogExportClusterInfo contains a package of information that fully
    describes both the intended state of the log export configuration for
    a specific cluster but also some metadata around its deployment
    status, any error messages, and some timestamps.

        Attributes:
            cluster_id (Union[Unset, str]):
            status (Union[Unset, LogExportStatus]): LogExportStatus encodes the possible states that a configuration can
                be in as it is created, deployed, and disabled.
            user_message (Union[Unset, str]):
            spec (Union[Unset, LogExportClusterSpecification]): LogExportClusterSpecification contains all the data
                necessary to
                configure log export for an individual cluster. Users would supply
                this data via the API and also receive it back when inspecting the
                state of their log export configuration.
            created_at (Union[Unset, datetime.datetime]):
            updated_at (Union[Unset, datetime.datetime]):
    """

    cluster_id: Union[Unset, str] = UNSET
    status: Union[Unset, LogExportStatus] = UNSET
    user_message: Union[Unset, str] = UNSET
    spec: Union[Unset, LogExportClusterSpecification] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
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
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
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
        cluster_id = d.pop("cluster_id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, LogExportStatus]
        if _status is None:
            status = None
        elif isinstance(_status, Unset):
            status = UNSET
        else:
            status = LogExportStatus(_status)

        user_message = d.pop("user_message", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, LogExportClusterSpecification]
        if _spec is None:
            spec = None
        elif isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = LogExportClusterSpecification.from_dict(_spec)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if _created_at is None:
            created_at = None
        elif isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if _updated_at is None:
            updated_at = None
        elif isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        log_export_cluster_info = cls(
            cluster_id=cluster_id,
            status=status,
            user_message=user_message,
            spec=spec,
            created_at=created_at,
            updated_at=updated_at,
        )

        log_export_cluster_info.additional_properties = d
        return log_export_cluster_info

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
