from typing import Union, Optional
from pydigitalenergy.models import Extra


class Stats:
    def __init__(self, cpu: int, disksize: int, extips: int, exttraffic: int, gpu: int, ram: int, **kwargs):
        self.cpu = cpu
        self.disksize = disksize
        self.extips = extips
        self.exttraffic = exttraffic
        self.gpu = gpu
        self.ram = ram
        self.extra = Extra(kwargs)


class Resource:
    def __init__(self, Current: Union[Stats, dict], Reserved: Union[Stats, dict], **kwargs):
        self.current = Stats(**Current) if isinstance(Current, dict) else Current
        self.reserved = Stats(**Reserved) if isinstance(Reserved, dict) else Reserved
        self.extra = Extra(kwargs)


class Grid:
    def __init__(self, id: int, name: str, gid: int, Resources: Union[Resource, dict], flag: Optional[str] = '', guid: Optional[int] = None, locationCode: Optional[str] = '', **kwargs):
        self.id = id
        self.name = name
        self.data_center_id = gid
        self.resources = Resource(**Resources) if isinstance(Resources, dict) else Resources
        self.flag = flag
        self.guid = guid
        self.location_code = locationCode
        self.extra = Extra(kwargs)
