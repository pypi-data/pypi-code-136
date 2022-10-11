from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.log_export_type import LogExportType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LogExportClusterSpecification")


@attr.s(auto_attribs=True)
class LogExportClusterSpecification:
    """LogExportClusterSpecification contains all the data necessary to
    configure log export for an individual cluster. Users would supply
    this data via the API and also receive it back when inspecting the
    state of their log export configuration.

        Attributes:
            type (Union[Unset, LogExportType]): LogExportType encodes the cloud selection that we're exporting to
                along with the cloud logging platform. Currently, each cloud has a
                single logging platform.
            log_name (Union[Unset, str]): log_name is an identifier for the logs in the customer's log sink.
            auth_principal (Union[Unset, str]): auth_principal is either the AWS Role ARN that identifies a role
                that the cluster account can assume to write to CloudWatch or the
                GCP Project ID that the cluster service account has permissions to
                write to for cloud logging.
    """

    type: Union[Unset, LogExportType] = UNSET
    log_name: Union[Unset, str] = UNSET
    auth_principal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        log_name = self.log_name
        auth_principal = self.auth_principal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if log_name is not UNSET:
            field_dict["log_name"] = log_name
        if auth_principal is not UNSET:
            field_dict["auth_principal"] = auth_principal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, LogExportType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = LogExportType(_type)

        log_name = d.pop("log_name", UNSET)

        auth_principal = d.pop("auth_principal", UNSET)

        log_export_cluster_specification = cls(
            type=type,
            log_name=log_name,
            auth_principal=auth_principal,
        )

        log_export_cluster_specification.additional_properties = d
        return log_export_cluster_specification

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
