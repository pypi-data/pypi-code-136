from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_cloud_provider import ApiCloudProvider
from ..models.create_cluster_specification import CreateClusterSpecification

T = TypeVar("T", bound="CreateClusterRequest")


@attr.s(auto_attribs=True)
class CreateClusterRequest:
    """
    Example:
        {'name': 'test-cluster', 'provider': 'GCP', 'spec': {'serverless': {'regions': ['us-central1'], 'spend_limit':
            0}}}

    Attributes:
        name (str): Name must be 6-20 characters in length and can include numbers,
            lowercase letters, and dashes (but no leading or trailing dashes).
        provider (ApiCloudProvider):  - GCP: The Google Cloud Platform cloud provider.
             - AWS: The Amazon Web Services cloud provider.
        spec (CreateClusterSpecification):
    """

    name: str
    provider: ApiCloudProvider
    spec: CreateClusterSpecification
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        provider = self.provider.value

        spec = self.spec.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "provider": provider,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        provider = ApiCloudProvider(d.pop("provider"))

        spec = CreateClusterSpecification.from_dict(d.pop("spec"))

        create_cluster_request = cls(
            name=name,
            provider=provider,
            spec=spec,
        )

        create_cluster_request.additional_properties = d
        return create_cluster_request

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
