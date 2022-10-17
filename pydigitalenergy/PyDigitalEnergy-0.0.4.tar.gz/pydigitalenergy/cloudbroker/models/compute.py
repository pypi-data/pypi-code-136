from uuid import UUID
from typing import Union, Optional, List, Any
from pydigitalenergy.cloudbroker.models.disk import Disk
from pydigitalenergy.models import Extra


class AntiAffinityRule:
    def __init__(self, key: str, guid: Optional[str] = '', mode: Optional[str] = '', value: Optional[bool] = None, **kwargs):
        self.key = key
        self.guid = guid
        self.mode = mode
        self.value = value
        self.extra = Extra(kwargs)


class Interface:
    def __init__(self, connId: int, connType: str, defGw: Optional[str] = '', flipgroupId: Optional[int] = None, guid: Optional[str] = '', ipAddress: Optional[str] = '', listenSsh: Optional[bool] = None, mac: Optional[str] = '', name: Optional[str] = '', netId: Optional[int] = None, netMask: Optional[int] = None, netType: Optional[str] = '', pciSlot: Optional[int] = None, target: Optional[str] = '', type: Optional[str] = '', vnfs: Optional[List[Any]] = [], **kwargs):
        self.conn_id = connId
        self.conn_type = connType
        self.def_gw = defGw
        self.flipgroup_id = flipgroupId
        self.guid = guid
        self.ip_address = ipAddress
        self.listen_ssh = listenSsh
        self.mac = mac
        self.name = name
        self.net_id = netId
        self.net_mask = netMask
        self.net_type = netType
        self.pci_slot = pciSlot
        self.target = target
        self.type = type
        self.vnfs = vnfs
        self.extra = Extra(kwargs)


class OSUser:
    def __init__(self, guid: Optional[str] = '', login: Optional[str] = '', password: Optional[str] = '', pubkey: Optional[str] = '', **kwargs):
        self.guid = guid
        self.login = login
        self.password = password
        self.pubkey = pubkey
        self.extra = Extra(kwargs)


class SnapSet:
    def __init__(self, guid: Optional[UUID] = '', disks: Optional[List[int]] = [], label: Optional[str] = '', timestamp: Optional[int] = None, **kwargs):
        self.guid = guid
        self.disks = disks
        self.label = label
        self.timestamp = timestamp
        self.extra = Extra(kwargs)


class Affinity:
    def __init__(self, affinityLabel: Optional[str] = '', affinityRules: Optional[List[Any]] = [], affinityWeight: Optional[int] = None, antiAffinityRules: Optional[List[Union[AntiAffinityRule, dict]]] = []):
        self.affinity_label = affinityLabel
        self.affinity_rules = affinityRules
        self.affinity_weight = affinityWeight
        self.anti_affinity_rules = [] if not antiAffinityRules else [AntiAffinityRule(**rules) for rules in antiAffinityRules]


class Boot:
    def __init__(self, bootOrder: Optional[List[str]] = [], bootdiskSize: Optional[int] = None):
        self.boot_order = bootOrder
        self.boot_disk_size = bootdiskSize


class Compute:
    def __init__(self, id: int, name: str, gid: int, accountId: int, accountName: str, rgId: int, rgName: str, stackId: int, status: str, techStatus: str, affinityLabel: Optional[str] = '', affinityRules: Optional[List[Any]] = [], affinityWeight: Optional[int] = None, antiAffinityRules: Optional[List[Union[AntiAffinityRule, dict]]] = [], arch: Optional[str] = '', bootOrder: Optional[List[str]] = [], bootdiskSize: Optional[int] = None, cloneReference: Optional[int] = None, clones: Optional[List[Any]] = [], computeciId: Optional[int] = None, cpus: Optional[int] = None, createdBy: Optional[str] = '', createdTime: Optional[int] = None, customFields: Optional[Any] = None, deletedBy: Optional[str] = '', deletedTime: Optional[int] = None, desc: Optional[str] = '', devices: Optional[Any] = None, disks: Optional[List[Union[Disk, dict, int]]] = [], driver: Optional[str] = '', guid: Optional[int] = None, imageId: Optional[int] = None, interfaces: Optional[List[Union[Interface, dict]]] = [], lockStatus: Optional[str] = '', managerId: Optional[int] = None, managerType: Optional[str] = '', migrationjob: Optional[int] = None, milestones: Optional[int] = None, osUsers: Optional[List[Union[OSUser, dict]]] = [], pinned: Optional[bool] = None, ram: Optional[int] = None, referenceId: Optional[UUID] = None, registered: Optional[bool] = None, resName: Optional[str] = '', snapSets: Optional[List[Union[SnapSet, dict]]] = [], statelessSepId: Optional[int] = None, statelessSepType: Optional[str] = '', tags: Optional[Any] = None, totalDisksSize: Optional[int] = None, updatedBy: Optional[str] = '', updatedTime: Optional[int] = None, userManaged: Optional[bool] = None, userdata: Optional[Any] = None, vgpus: Optional[List[Any]] = [], vinsConnected: Optional[int] = None, virtualImageId: Optional[int] = None, **kwargs):
        self.id = id
        self.grid_id = gid
        self.stack_id = stackId
        self.account_id = accountId
        self.resource_group_id = rgId
        self.image_id = imageId
        self.name = name
        self.account_name = accountName
        self.resource_group_name = rgName
        self.status = status
        self.tech_status = techStatus
        self.affinity = Affinity(affinityLabel, affinityRules, affinityWeight, antiAffinityRules)
        self.architecture = arch
        self.boot = Boot(bootOrder, bootdiskSize)
        self.clone_reference = cloneReference
        self.clones = clones
        self.compute_ci_id = computeciId
        self.cpus = cpus
        self.created_by = createdBy
        self.created_time = createdTime
        self.deleted_by = deletedBy
        self.deleted_time = deletedTime
        self.custom_fields = customFields
        self.description = desc
        self.devices = devices
        self.disks = [] if not disks else [Disk(**disk) if isinstance(disk, dict) else disk for disk in disks]
        self.driver = driver
        self.guid = guid
        self.interfaces = [] if not interfaces else [Interface(**interface) if isinstance(interface, dict) else interface for interface in interfaces]
        self.lock_status = lockStatus
        self.manager_id = managerId
        self.manager_type = managerType
        self.migration_job = migrationjob
        self.milestones = milestones
        self.os_users = [] if not osUsers else [OSUser(**user) if isinstance(user, dict) else user for user in osUsers]
        self.pinned = pinned
        self.ram = ram
        self.reference_id = referenceId
        self.registered = registered
        self.res_name = resName
        self.snap_sets = [] if not snapSets else [SnapSet(**snap_set) if isinstance(snap_set, dict) else snap_set for snap_set in snapSets]
        self.stateless_sep_id = statelessSepId
        self.stateless_sep_type = statelessSepType
        self.tags = tags
        self.total_disks_size = totalDisksSize
        self.updated_by = updatedBy
        self.updated_time = updatedTime
        self.user_managed = userManaged
        self.user_data = userdata
        self.vgpus = vgpus
        self.vins_connected = vinsConnected
        self.virtual_image_id = virtualImageId
        self.extra = Extra(kwargs)
