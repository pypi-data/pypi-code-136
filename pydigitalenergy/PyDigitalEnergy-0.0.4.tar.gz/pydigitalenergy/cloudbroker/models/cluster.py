from typing import Optional, List, Union
from pydigitalenergy.cloudbroker.models.node import Consumption
from pydigitalenergy.models import Extra


class Cluster:
    def __init__(self, id: int, gid: int, name: str, status: str, referenceId: int, descr: Optional[str] = '', error: Optional[int] = None, guid: Optional[int] = None, consumption: Union[Consumption, dict] = None, roles: Optional[List[str]] = [], **kwargs):
        self.id = id
        self.node_id = int(referenceId) if referenceId.isdigit() else referenceId
        self.data_center_id = gid
        self.guid = guid
        self.name = name
        self.status = status
        self.roles = roles
        self.description = descr
        self.error = error
        self.consumption = Consumption(**consumption) if isinstance(consumption, dict) else consumption
        self.extra = Extra(kwargs)
