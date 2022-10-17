from uuid import UUID
from typing import Optional, Union, List, Any
from pydigitalenergy.cloudbroker.models.compute import Affinity, Boot, Disk, Interface, OSUser, SnapSet, AntiAffinityRule
from pydigitalenergy.cloudbroker.models.host import Host, Consumption, StorageConfig
from pydigitalenergy.cloudbroker.models.cluster import Cluster
from pydigitalenergy.cloudbroker.models.image import Image
from pydigitalenergy.models import Extra


class VM:
    def __init__(self, 
        # Required
        id: int, name: str, gid: int, accountId: int, accountName: str, rgId: int, rgName: str, status: str, techStatus: str, 
        hostId: int, hostGid: int, hostName: str, hostStatus: str, hostType: str, hostStackId: int, hostSepName: str, hostDesc: str, hostSepType: str, hostObjStatus: str, hostTechStatus: str, hostReferenceId: int,
        clusterId: int, clusterGid: int, clusterName: str, clusterStatus: str, clusterReferenceId: int, 
        # Optional
        affinityLabel: Optional[str] = '', affinityRules: Optional[List[Any]] = [], affinityWeight: Optional[int] = None, antiAffinityRules: Optional[List[Union[AntiAffinityRule, dict]]] = [], arch: Optional[str] = '', bootOrder: Optional[List[str]] = [], bootdiskSize: Optional[int] = None, cloneReference: Optional[int] = None, clones: Optional[List[Any]] = [], computeciId: Optional[int] = None, cpus: Optional[int] = None, createdBy: Optional[str] = '', createdTime: Optional[int] = None, customFields: Optional[Any] = None, deletedBy: Optional[str] = '', deletedTime: Optional[int] = None, desc: Optional[str] = '', devices: Optional[Any] = None, disks: Optional[List[Union[Disk, dict, int]]] = [], driver: Optional[str] = '', guid: Optional[int] = None, interfaces: Optional[List[Union[Interface, dict]]] = [], lockStatus: Optional[str] = '', managerId: Optional[int] = None, managerType: Optional[str] = '', migrationjob: Optional[int] = None, milestones: Optional[int] = None, osUsers: Optional[List[Union[OSUser, dict]]] = [], pinned: Optional[bool] = None, ram: Optional[int] = None, referenceId: Optional[UUID] = None, registered: Optional[bool] = None, resName: Optional[str] = '', snapSets: Optional[List[Union[SnapSet, dict]]] = [], statelessSepId: Optional[int] = None, statelessSepType: Optional[str] = '', tags: Optional[Any] = None, totalDisksSize: Optional[int] = None, updatedBy: Optional[str] = '', updatedTime: Optional[int] = None, userManaged: Optional[bool] = None, userdata: Optional[Any] = None, vgpus: Optional[List[Any]] = [], vinsConnected: Optional[int] = None, virtualImageId: Optional[int] = None,
        hostVersion: Optional[str] = '', hostApiUrl: Optional[str] = '', hostApikey: Optional[str] = '', hostDescr: Optional[str] = '', hostDrivers: Optional[List[str]] = '', hostError: Optional[int] = None, hostGuid: Optional[int] = None, hostIpaddr: Optional[List[str]] = [], hostConsumption: Union[Consumption, dict] = None, hostRoles: Optional[List[str]] = [], hostConfig: Optional[Union[StorageConfig, dict]] = None, hostConsumedBy: Optional[List[int]] = [], hostMilestones: Optional[int] = None, hostProvidedBy: Optional[List[Any]] = [],
        clusterDescr: Optional[str] = '', clusterError: Optional[int] = None, clusterGuid: Optional[int] = None, clusterConsumption: Union[Consumption, dict] = None, clusterRoles: Optional[List[str]] = [],
        imageHasImage: bool = True, imageId: int = None, imageName: str = '', imageType: str = '', imageVersion: str = '', imageStatus: str = '', imageTechStatus: str = '', imageUNCPath: Optional[str] = '', imageAccountId: Optional[int] = None, imageArchitecture: Optional[str] = '', imageBootType: Optional[str] = '', imageBootable: Optional[bool] = None, imageComputeciId: Optional[int] = None, imageDeletedTime: Optional[int] = None, imageDesc: Optional[str] = '', imageDrivers: Optional[List[str]] = [], imageEnabled: Optional[bool] = None, imageGid: Optional[int] = None, imageGuid: Optional[int] = None, imageHistory: Optional[List[Any]] = [], imageHotResize: Optional[bool] = None, imageLastModified: Optional[int] = None, imageLinkTo: Optional[int] = None, imageMilestones: Optional[int] = None, imageUsername: Optional[str] = '', imagePool: Optional[str] = '', imageProvidername: Optional[str] = '', imagePurgeAttempts: Optional[int] = None, imageReferenceId: Optional[str] = '', imageResId: Optional[int] = None, imageResName: Optional[str] = '', imageRescuecd: Optional[bool] = None, imageSepId: Optional[int] = None, imageSharedWith: Optional[List[Any]] = [], imageSize: Optional[int] = None, imageUrl: Optional[str] = '', imageVirtual: Optional[bool] = None,
     **kwargs):
        self.id = id
        self.data_center_id = gid
        self.account_id = accountId
        self.resource_group_id = rgId
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
        self.has_image = imageHasImage
        self.host = Host(hostId, hostGid, hostName, hostStatus, hostType, hostStackId, hostSepName, hostDesc, hostSepType, hostObjStatus, hostTechStatus, hostVersion, hostReferenceId, hostApiUrl, hostApikey, hostDescr, hostDrivers, hostError, hostGuid, hostIpaddr, hostConsumption, hostRoles, hostConfig, hostConsumedBy, hostMilestones, hostProvidedBy)
        self.cluster = Cluster(clusterId, clusterGid, clusterName, clusterStatus, clusterReferenceId, clusterDescr, clusterError, clusterGuid, clusterConsumption, clusterRoles)
        self.image = Image(imageId, imageName, imageType, imageVersion, imageStatus, imageTechStatus, imageUNCPath, imageAccountId, imageArchitecture, imageBootType, imageBootable, imageComputeciId, imageDeletedTime, imageDesc, imageDrivers, imageEnabled, imageGid, imageGuid, imageHistory, imageHotResize, imageLastModified, imageLinkTo, imageMilestones, imageUsername, imagePool, imageProvidername, imagePurgeAttempts, imageReferenceId, imageResId, imageResName, imageRescuecd, imageSepId, imageSharedWith, imageSize, imageUrl, imageVirtual)
        self.extra = Extra(kwargs)
