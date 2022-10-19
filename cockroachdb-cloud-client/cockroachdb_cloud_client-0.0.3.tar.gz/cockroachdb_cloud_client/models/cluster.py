import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_cloud_provider import ApiCloudProvider
from ..models.cluster_config import ClusterConfig
from ..models.cluster_state_type import ClusterStateType
from ..models.cluster_status_type import ClusterStatusType
from ..models.plan import Plan
from ..models.region import Region
from ..types import UNSET, Unset

T = TypeVar("T", bound="Cluster")


@attr.s(auto_attribs=True)
class Cluster:
    """
    Example:
        {'account_id': '', 'cloud_provider': 'GCP', 'cockroach_version': 'v21.2.4', 'config': {'serverless':
            {'routing_id': 'example-cluster-1533', 'spend_limit': 0}}, 'created_at': '2022-03-22T20:23:11.285067Z',
            'creator_id': '7cde0cd9-0d8a-4008-8f90-45092ce8afc1', 'deleted_at': None, 'id':
            '35c4abb2-bb66-46d7-afed-25ebef5ed2aa', 'name': 'example-cluster', 'operation_status':
            'CLUSTER_STATUS_UNSPECIFIED', 'plan': 'SERVERLESS', 'regions': [{'name': 'us-central1', 'node_count': 0,
            'sql_dns': 'free-tier7.gcp-us-central1.crdb.io', 'ui_dns': ''}], 'state': 'CREATED', 'updated_at':
            '2022-03-22T20:23:11.879593Z'}

    Attributes:
        cloud_provider (ApiCloudProvider):  - GCP: The Google Cloud Platform cloud provider.
             - AWS: The Amazon Web Services cloud provider.
        cockroach_version (str):
        config (ClusterConfig):
        creator_id (str):
        id (str):
        name (str):
        operation_status (ClusterStatusType):
        plan (Plan):  - DEDICATED: A paid plan that offers dedicated hardware in any location.
             - CUSTOM: A plan option that is used for clusters whose machine configs are not
            supported in self-service. All INVOICE clusters are under this plan option.
             - SERVERLESS: A paid plan that runs on shared hardware and caps the users'
            maximum monthly spending to a user-specified (possibly 0) amount.
        regions (List[Region]):
        state (ClusterStateType):  - LOCKED: An exclusive operation is being performed on this cluster.
            Other operations should not proceed if they did not set a cluster into the LOCKED state.
        account_id (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    cloud_provider: ApiCloudProvider
    cockroach_version: str
    config: ClusterConfig
    creator_id: str
    id: str
    name: str
    operation_status: ClusterStatusType
    plan: Plan
    regions: List[Region]
    state: ClusterStateType
    account_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_provider = self.cloud_provider.value

        cockroach_version = self.cockroach_version
        config = self.config.to_dict()

        creator_id = self.creator_id
        id = self.id
        name = self.name
        operation_status = self.operation_status.value

        plan = self.plan.value

        regions = []
        for regions_item_data in self.regions:
            regions_item = regions_item_data.to_dict()

            regions.append(regions_item)

        state = self.state.value

        account_id = self.account_id
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_provider": cloud_provider,
                "cockroach_version": cockroach_version,
                "config": config,
                "creator_id": creator_id,
                "id": id,
                "name": name,
                "operation_status": operation_status,
                "plan": plan,
                "regions": regions,
                "state": state,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_provider = ApiCloudProvider(d.pop("cloud_provider"))

        cockroach_version = d.pop("cockroach_version")

        config = ClusterConfig.from_dict(d.pop("config"))

        creator_id = d.pop("creator_id")

        id = d.pop("id")

        name = d.pop("name")

        operation_status = ClusterStatusType(d.pop("operation_status"))

        plan = Plan(d.pop("plan"))

        regions = []
        _regions = d.pop("regions")
        for regions_item_data in _regions:
            regions_item = Region.from_dict(regions_item_data)

            regions.append(regions_item)

        state = ClusterStateType(d.pop("state"))

        account_id = d.pop("account_id", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if _created_at is None:
            created_at = None
        elif isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _deleted_at = d.pop("deleted_at", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if _deleted_at is None:
            deleted_at = None
        elif isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if _updated_at is None:
            updated_at = None
        elif isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        cluster = cls(
            cloud_provider=cloud_provider,
            cockroach_version=cockroach_version,
            config=config,
            creator_id=creator_id,
            id=id,
            name=name,
            operation_status=operation_status,
            plan=plan,
            regions=regions,
            state=state,
            account_id=account_id,
            created_at=created_at,
            deleted_at=deleted_at,
            updated_at=updated_at,
        )

        cluster.additional_properties = d
        return cluster

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
