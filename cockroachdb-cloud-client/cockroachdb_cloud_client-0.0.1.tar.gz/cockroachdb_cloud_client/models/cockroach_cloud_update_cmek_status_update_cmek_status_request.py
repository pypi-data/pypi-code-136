from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.cmek_customer_action import CMEKCustomerAction

T = TypeVar("T", bound="CockroachCloudUpdateCMEKStatusUpdateCMEKStatusRequest")


@attr.s(auto_attribs=True)
class CockroachCloudUpdateCMEKStatusUpdateCMEKStatusRequest:
    """
    Example:
        {'action': 'REVOKE'}

    Attributes:
        action (CMEKCustomerAction): CMEKCustomerAction enumerates the actions a customer can take on a cluster
            that has been enabled for CMEK.
    """

    action: CMEKCustomerAction
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = CMEKCustomerAction(d.pop("action"))

        cockroach_cloud_update_cmek_status_update_cmek_status_request = cls(
            action=action,
        )

        cockroach_cloud_update_cmek_status_update_cmek_status_request.additional_properties = d
        return cockroach_cloud_update_cmek_status_update_cmek_status_request

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
