from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_cloud_provider import ApiCloudProvider
from ..models.aws_endpoint_connection_status import AWSEndpointConnectionStatus

T = TypeVar("T", bound="AwsEndpointConnection")


@attr.s(auto_attribs=True)
class AwsEndpointConnection:
    """
    Attributes:
        region_name (str): RegionName is the cloud provider region name (i.e. us-east-1).
        cloud_provider (ApiCloudProvider):  - GCP: The Google Cloud Platform cloud provider.
             - AWS: The Amazon Web Services cloud provider.
        status (AWSEndpointConnectionStatus): The statuses map to the statuses returned by the AWS API.
        endpoint_id (str): EndpointID is the client side of the PrivateLink connection.
        service_id (str): ServiceID is the server side of the PrivateLink
            connection. This is the same as AWSPrivateLinkEndpoint.service_id.
    """

    region_name: str
    cloud_provider: ApiCloudProvider
    status: AWSEndpointConnectionStatus
    endpoint_id: str
    service_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_name = self.region_name
        cloud_provider = self.cloud_provider.value

        status = self.status.value

        endpoint_id = self.endpoint_id
        service_id = self.service_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region_name": region_name,
                "cloud_provider": cloud_provider,
                "status": status,
                "endpoint_id": endpoint_id,
                "service_id": service_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_name = d.pop("region_name")

        cloud_provider = ApiCloudProvider(d.pop("cloud_provider"))

        status = AWSEndpointConnectionStatus(d.pop("status"))

        endpoint_id = d.pop("endpoint_id")

        service_id = d.pop("service_id")

        aws_endpoint_connection = cls(
            region_name=region_name,
            cloud_provider=cloud_provider,
            status=status,
            endpoint_id=endpoint_id,
            service_id=service_id,
        )

        aws_endpoint_connection.additional_properties = d
        return aws_endpoint_connection

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
