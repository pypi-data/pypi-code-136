from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_cloud_provider import ApiCloudProvider

T = TypeVar("T", bound="CloudProviderRegion")


@attr.s(auto_attribs=True)
class CloudProviderRegion:
    """
    Attributes:
        distance (float):
        location (str):
        name (str):
        provider (ApiCloudProvider):  - GCP: The Google Cloud Platform cloud provider.
             - AWS: The Amazon Web Services cloud provider.
        serverless (bool):
    """

    distance: float
    location: str
    name: str
    provider: ApiCloudProvider
    serverless: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        distance = self.distance
        location = self.location
        name = self.name
        provider = self.provider.value

        serverless = self.serverless

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "distance": distance,
                "location": location,
                "name": name,
                "provider": provider,
                "serverless": serverless,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        distance = d.pop("distance")

        location = d.pop("location")

        name = d.pop("name")

        provider = ApiCloudProvider(d.pop("provider"))

        serverless = d.pop("serverless")

        cloud_provider_region = cls(
            distance=distance,
            location=location,
            name=name,
            provider=provider,
            serverless=serverless,
        )

        cloud_provider_region.additional_properties = d
        return cloud_provider_region

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
