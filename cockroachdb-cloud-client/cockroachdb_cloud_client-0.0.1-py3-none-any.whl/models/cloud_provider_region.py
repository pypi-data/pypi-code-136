from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_cloud_provider import ApiCloudProvider

T = TypeVar("T", bound="CloudProviderRegion")


@attr.s(auto_attribs=True)
class CloudProviderRegion:
    """
    Attributes:
        name (str):
        location (str):
        provider (ApiCloudProvider):  - GCP: The Google Cloud Platform cloud provider.
             - AWS: The Amazon Web Services cloud provider.
        serverless (bool):
        distance (float):
    """

    name: str
    location: str
    provider: ApiCloudProvider
    serverless: bool
    distance: float
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        location = self.location
        provider = self.provider.value

        serverless = self.serverless
        distance = self.distance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "location": location,
                "provider": provider,
                "serverless": serverless,
                "distance": distance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        location = d.pop("location")

        provider = ApiCloudProvider(d.pop("provider"))

        serverless = d.pop("serverless")

        distance = d.pop("distance")

        cloud_provider_region = cls(
            name=name,
            location=location,
            provider=provider,
            serverless=serverless,
            distance=distance,
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
