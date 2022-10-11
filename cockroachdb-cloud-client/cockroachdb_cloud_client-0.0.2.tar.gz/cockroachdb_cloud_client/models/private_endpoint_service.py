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
        region_name (str): RegionName is the cloud provider region name (i.e. us-east-1).
        cloud_provider (ApiCloudProvider):  - GCP: The Google Cloud Platform cloud provider.
             - AWS: The Amazon Web Services cloud provider.
        status (PrivateEndpoints): - ENDPOINT_SERVICE_STATUS_DELETE_FAILED: One note is that if the service is deleted,
            there is no longer
            a record, hence there is no "DELETED" status.
        aws (AWSPrivateLinkServiceDetail):
    """

    region_name: str
    cloud_provider: ApiCloudProvider
    status: PrivateEndpoints
    aws: AWSPrivateLinkServiceDetail
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_name = self.region_name
        cloud_provider = self.cloud_provider.value

        status = self.status.value

        aws = self.aws.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region_name": region_name,
                "cloud_provider": cloud_provider,
                "status": status,
                "aws": aws,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_name = d.pop("region_name")

        cloud_provider = ApiCloudProvider(d.pop("cloud_provider"))

        status = PrivateEndpoints(d.pop("status"))

        aws = AWSPrivateLinkServiceDetail.from_dict(d.pop("aws"))

        private_endpoint_service = cls(
            region_name=region_name,
            cloud_provider=cloud_provider,
            status=status,
            aws=aws,
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
