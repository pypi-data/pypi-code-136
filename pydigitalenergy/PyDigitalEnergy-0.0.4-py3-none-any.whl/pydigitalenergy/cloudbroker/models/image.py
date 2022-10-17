from typing import Optional, List, Union, Any
from pydigitalenergy.models import Extra


class Image:
    def __init__(self, id: int, name: str, type: str, version: str, status: str, techStatus: str, UNCPath: Optional[str] = '', accountId: Optional[int] = None, architecture: Optional[str] = '', bootType: Optional[str] = '', bootable: Optional[bool] = None, computeciId: Optional[int] = None, deletedTime: Optional[int] = None, desc: Optional[str] = '', drivers: Optional[List[str]] = [], enabled: Optional[bool] = None, gid: Optional[int] = None, guid: Optional[int] = None, history: Optional[List[Any]] = [], hotResize: Optional[bool] = None, lastModified: Optional[int] = None, linkTo: Optional[int] = None, milestones: Optional[int] = None, username: Optional[str] = '', pool: Optional[str] = '', providername: Optional[str] = '', purgeAttempts: Optional[int] = None, referenceId: Optional[str] = '', resId: Optional[int] = None, resName: Optional[str] = '', rescuecd: Optional[bool] = None, sepId: Optional[int] = None, sharedWith: Optional[List[Any]] = [], size: Optional[int] = None, url: Optional[str] = '', virtual: Optional[bool] = None, **kwargs):
        self.id = id
        self.name = name
        self.type = type
        self.version = version
        self.status = status
        self.tech_status = techStatus
        self.unc_patch = UNCPath
        self.account_id = accountId
        self.architecture = architecture
        self.boot_type = bootType
        self.bootable = bootable
        self.compute_ci_id = computeciId
        self.deleted_time = deletedTime
        self.description = desc
        self.drivers = drivers
        self.enabled = enabled
        self.grid_id = gid
        self.guid = guid
        self.history = history
        self.hot_resize = hotResize
        self.last_modified = lastModified
        self.link_to = linkTo
        self.milestones = milestones
        self.pool = pool
        self.provider_name = providername
        self.purge_attempts = purgeAttempts
        self.reference_id = referenceId
        self.res_id = resId
        self.res_name = resName
        self.rescuecd = rescuecd
        self.sep_id = sepId
        self.shared_with = sharedWith
        self.size = size
        self.url = url
        self.username = username
        self.virtual = virtual
        self.extra = Extra(kwargs)
