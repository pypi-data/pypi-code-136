from typing import Optional, Union, List, Any
from pydigitalenergy.cloudbroker.models.node import Consumption
from pydigitalenergy.cloudbroker.models.sep import StorageConfig
from pydigitalenergy.models import Extra


class Hardware:
    def __init__(self, sepName: str, desc: str, sepType: str, objStatus: str, techStatus: str, config: Optional[Union[StorageConfig, dict]] = None, consumedBy: Optional[List[int]] = [], milestones: Optional[int] = None, providedBy: Optional[List[Any]] = []):
        self.name = sepName
        self.description = desc
        self.type = sepType
        self.obj_status = objStatus
        self.tech_status = techStatus
        self.config = StorageConfig(**config) if isinstance(config, dict) else config
        self.consumed_by = consumedBy
        self.milestones = milestones
        self.provided_by = providedBy


class Host:
    def __init__(self, id: int, gid: int, name: str, status: str, type: str, stackId: int, sepName: str, desc: str, sepType: str, objStatus: str, techStatus: str, version: Optional[str], referenceId: int, apiUrl: Optional[str] = '', apikey: Optional[str] = '', descr: Optional[str] = '', drivers: Optional[List[str]] = '', error: Optional[int] = None, guid: Optional[int] = None, ipaddr: Optional[List[str]] = [], consumption: Union[Consumption, dict] = None, roles: Optional[List[str]] = [], config: Optional[Union[StorageConfig, dict]] = None, consumedBy: Optional[List[int]] = [], milestones: Optional[int] = None, providedBy: Optional[List[Any]] = [], **kwargs):
        self.id = id
        self.data_center_id = gid
        self.name = name
        self.status = status
        self.version = version
        self.ip_address = ipaddr
        self.consumption = Consumption(**consumption) if isinstance(consumption, dict) else consumption
        self.roles = roles
        self.hardware = Hardware(sepName, desc, sepType, objStatus, techStatus, config, consumedBy, milestones, providedBy)
        self.cluster_id = stackId
        self.type = type
        self.node_id = int(referenceId) if referenceId.isdigit() else referenceId
        self.description = descr
        self.drivers = drivers
        self.api_url = apiUrl
        self.api_key = apikey
        self.error = error
        self.guid = guid
        self.extra = Extra(kwargs)
