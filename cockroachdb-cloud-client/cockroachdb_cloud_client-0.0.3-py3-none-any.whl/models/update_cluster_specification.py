from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dedicated_cluster_update_specification import DedicatedClusterUpdateSpecification
from ..models.serverless_cluster_update_specification import ServerlessClusterUpdateSpecification
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateClusterSpecification")


@attr.s(auto_attribs=True)
class UpdateClusterSpecification:
    """
    Example:
        {'dedicated': {'hardware': {'machine_type': 'n2-standard-8'}, 'region_nodes': {'us-central1': 5, 'us-west1':
            3}}}

    Attributes:
        dedicated (Union[Unset, DedicatedClusterUpdateSpecification]):
        serverless (Union[Unset, ServerlessClusterUpdateSpecification]):
    """

    dedicated: Union[Unset, DedicatedClusterUpdateSpecification] = UNSET
    serverless: Union[Unset, ServerlessClusterUpdateSpecification] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dedicated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dedicated, Unset):
            dedicated = self.dedicated.to_dict()

        serverless: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.serverless, Unset):
            serverless = self.serverless.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dedicated is not UNSET:
            field_dict["dedicated"] = dedicated
        if serverless is not UNSET:
            field_dict["serverless"] = serverless

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _dedicated = d.pop("dedicated", UNSET)
        dedicated: Union[Unset, DedicatedClusterUpdateSpecification]
        if _dedicated is None:
            dedicated = None
        elif isinstance(_dedicated, Unset):
            dedicated = UNSET
        else:
            dedicated = DedicatedClusterUpdateSpecification.from_dict(_dedicated)

        _serverless = d.pop("serverless", UNSET)
        serverless: Union[Unset, ServerlessClusterUpdateSpecification]
        if _serverless is None:
            serverless = None
        elif isinstance(_serverless, Unset):
            serverless = UNSET
        else:
            serverless = ServerlessClusterUpdateSpecification.from_dict(_serverless)

        update_cluster_specification = cls(
            dedicated=dedicated,
            serverless=serverless,
        )

        update_cluster_specification.additional_properties = d
        return update_cluster_specification

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
