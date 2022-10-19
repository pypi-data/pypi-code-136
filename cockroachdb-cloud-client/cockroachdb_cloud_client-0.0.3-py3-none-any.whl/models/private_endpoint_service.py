from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.api_cloud_provider import ApiCloudProvider
from ..models.aws_private_link_service_detail import AWSPrivateLinkServiceDetail
from ..models.private_endpoints import PrivateEndpoints

T = TypeVar("T", bound="PrivateEndpointService")


@attr.s(auto_attribs=True)
class PrivateEndpointService:
    """
    Attributes:
        aws (AWSPrivateLinkServiceDetail):
        cloud_provider (ApiCloudProvider):  - GCP: The Google Cloud Platform cloud provider.
             - AWS: The Amazon Web Services cloud provider.
        region_name (str): RegionName is the cloud provider region name (i.e. us-east-1).
        status (PrivateEndpoints): - ENDPOINT_SERVICE_STATUS_DELETE_FAILED: One note is that if the service is deleted,
            there is no longer
            a record, hence there is no "DELETED" status.
    """

    aws: AWSPrivateLinkServiceDetail
    cloud_provider: ApiCloudProvider
    region_name: str
    status: PrivateEndpoints
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aws = self.aws.to_dict()

        cloud_provider = self.cloud_provider.value

        region_name = self.region_name
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aws": aws,
                "cloud_provider": cloud_provider,
                "region_name": region_name,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aws = AWSPrivateLinkServiceDetail.from_dict(d.pop("aws"))

        cloud_provider = ApiCloudProvider(d.pop("cloud_provider"))

        region_name = d.pop("region_name")

        status = PrivateEndpoints(d.pop("status"))

        private_endpoint_service = cls(
            aws=aws,
            cloud_provider=cloud_provider,
            region_name=region_name,
            status=status,
        )

        private_endpoint_service.additional_properties = d
        return private_endpoint_service

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
