from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.private_endpoint_service import PrivateEndpointService

T = TypeVar("T", bound="PrivateEndpointServices")


@attr.s(auto_attribs=True)
class PrivateEndpointServices:
    """
    Attributes:
        services (List[PrivateEndpointService]): Services contains a list of all cluster related services.
    """

    services: List[PrivateEndpointService]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        services = []
        for services_item_data in self.services:
            services_item = services_item_data.to_dict()

            services.append(services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "services": services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        services = []
        _services = d.pop("services")
        for services_item_data in _services:
            services_item = PrivateEndpointService.from_dict(services_item_data)

            services.append(services_item)

        private_endpoint_services = cls(
            services=services,
        )

        private_endpoint_services.additional_properties = d
        return private_endpoint_services

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
