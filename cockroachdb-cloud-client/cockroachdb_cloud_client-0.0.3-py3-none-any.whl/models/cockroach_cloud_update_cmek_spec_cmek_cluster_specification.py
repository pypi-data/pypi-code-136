from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.cmek_region_specification import CMEKRegionSpecification

T = TypeVar("T", bound="CockroachCloudUpdateCMEKSpecCMEKClusterSpecification")


@attr.s(auto_attribs=True)
class CockroachCloudUpdateCMEKSpecCMEKClusterSpecification:
    """
    Example:
        {'region_specs': [{'key_spec': {'auth_principal': 'arn:aws:iam::account:role/role-name-with-path', 'type':
            'AWS_KMS', 'uri': 'arn:aws:kms:us-west-2:111122223333:key/id-of-kms-key'}, 'region': 'us-central1'}]}

    Attributes:
        region_specs (List[CMEKRegionSpecification]):
    """

    region_specs: List[CMEKRegionSpecification]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_specs = []
        for region_specs_item_data in self.region_specs:
            region_specs_item = region_specs_item_data.to_dict()

            region_specs.append(region_specs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region_specs": region_specs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        region_specs = []
        _region_specs = d.pop("region_specs")
        for region_specs_item_data in _region_specs:
            region_specs_item = CMEKRegionSpecification.from_dict(region_specs_item_data)

            region_specs.append(region_specs_item)

        cockroach_cloud_update_cmek_spec_cmek_cluster_specification = cls(
            region_specs=region_specs,
        )

        cockroach_cloud_update_cmek_spec_cmek_cluster_specification.additional_properties = d
        return cockroach_cloud_update_cmek_spec_cmek_cluster_specification

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
