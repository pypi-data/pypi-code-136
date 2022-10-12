'''
# `google_compute_region_disk`

Refer to the Terraform Registory for docs: [`google_compute_region_disk`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class GoogleComputeRegionDisk(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDisk",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk google_compute_region_disk}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        replica_zones: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        disk_encryption_key: typing.Optional[typing.Union["GoogleComputeRegionDiskDiskEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        interface: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        physical_block_size_bytes: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        snapshot: typing.Optional[builtins.str] = None,
        source_snapshot_encryption_key: typing.Optional[typing.Union["GoogleComputeRegionDiskSourceSnapshotEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionDiskTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk google_compute_region_disk} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#name GoogleComputeRegionDisk#name}
        :param replica_zones: URLs of the zones where the disk should be replicated to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#replica_zones GoogleComputeRegionDisk#replica_zones}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#description GoogleComputeRegionDisk#description}
        :param disk_encryption_key: disk_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#disk_encryption_key GoogleComputeRegionDisk#disk_encryption_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#id GoogleComputeRegionDisk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interface: Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#interface GoogleComputeRegionDisk#interface}
        :param labels: Labels to apply to this disk. A list of key->value pairs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#labels GoogleComputeRegionDisk#labels}
        :param physical_block_size_bytes: Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently supported sizes are 4096 and 16384, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#physical_block_size_bytes GoogleComputeRegionDisk#physical_block_size_bytes}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#project GoogleComputeRegionDisk#project}.
        :param region: A reference to the region where the disk resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#region GoogleComputeRegionDisk#region}
        :param size: Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk. If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less than the size of the sourceImage or the size of the snapshot. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#size GoogleComputeRegionDisk#size}
        :param snapshot: The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 'https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot' 'projects/project/global/snapshots/snapshot' 'global/snapshots/snapshot' 'snapshot' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#snapshot GoogleComputeRegionDisk#snapshot}
        :param source_snapshot_encryption_key: source_snapshot_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#source_snapshot_encryption_key GoogleComputeRegionDisk#source_snapshot_encryption_key}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#timeouts GoogleComputeRegionDisk#timeouts}
        :param type: URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#type GoogleComputeRegionDisk#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDisk.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRegionDiskConfig(
            name=name,
            replica_zones=replica_zones,
            description=description,
            disk_encryption_key=disk_encryption_key,
            id=id,
            interface=interface,
            labels=labels,
            physical_block_size_bytes=physical_block_size_bytes,
            project=project,
            region=region,
            size=size,
            snapshot=snapshot,
            source_snapshot_encryption_key=source_snapshot_encryption_key,
            timeouts=timeouts,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDiskEncryptionKey")
    def put_disk_encryption_key(
        self,
        *,
        kms_key_name: typing.Optional[builtins.str] = None,
        raw_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_name: The name of the encryption key that is stored in Google Cloud KMS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#kms_key_name GoogleComputeRegionDisk#kms_key_name}
        :param raw_key: Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#raw_key GoogleComputeRegionDisk#raw_key}
        '''
        value = GoogleComputeRegionDiskDiskEncryptionKey(
            kms_key_name=kms_key_name, raw_key=raw_key
        )

        return typing.cast(None, jsii.invoke(self, "putDiskEncryptionKey", [value]))

    @jsii.member(jsii_name="putSourceSnapshotEncryptionKey")
    def put_source_snapshot_encryption_key(
        self,
        *,
        kms_key_name: typing.Optional[builtins.str] = None,
        raw_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_name: The name of the encryption key that is stored in Google Cloud KMS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#kms_key_name GoogleComputeRegionDisk#kms_key_name}
        :param raw_key: Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#raw_key GoogleComputeRegionDisk#raw_key}
        '''
        value = GoogleComputeRegionDiskSourceSnapshotEncryptionKey(
            kms_key_name=kms_key_name, raw_key=raw_key
        )

        return typing.cast(None, jsii.invoke(self, "putSourceSnapshotEncryptionKey", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#create GoogleComputeRegionDisk#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#delete GoogleComputeRegionDisk#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#update GoogleComputeRegionDisk#update}.
        '''
        value = GoogleComputeRegionDiskTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDiskEncryptionKey")
    def reset_disk_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKey", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInterface")
    def reset_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterface", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetPhysicalBlockSizeBytes")
    def reset_physical_block_size_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhysicalBlockSizeBytes", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetSnapshot")
    def reset_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshot", []))

    @jsii.member(jsii_name="resetSourceSnapshotEncryptionKey")
    def reset_source_snapshot_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceSnapshotEncryptionKey", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKey")
    def disk_encryption_key(
        self,
    ) -> "GoogleComputeRegionDiskDiskEncryptionKeyOutputReference":
        return typing.cast("GoogleComputeRegionDiskDiskEncryptionKeyOutputReference", jsii.get(self, "diskEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="labelFingerprint")
    def label_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="lastAttachTimestamp")
    def last_attach_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastAttachTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="lastDetachTimestamp")
    def last_detach_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastDetachTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="sourceSnapshotEncryptionKey")
    def source_snapshot_encryption_key(
        self,
    ) -> "GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference":
        return typing.cast("GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference", jsii.get(self, "sourceSnapshotEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="sourceSnapshotId")
    def source_snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceSnapshotId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeRegionDiskTimeoutsOutputReference":
        return typing.cast("GoogleComputeRegionDiskTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "users"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyInput")
    def disk_encryption_key_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionDiskDiskEncryptionKey"]:
        return typing.cast(typing.Optional["GoogleComputeRegionDiskDiskEncryptionKey"], jsii.get(self, "diskEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceInput")
    def interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="physicalBlockSizeBytesInput")
    def physical_block_size_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "physicalBlockSizeBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="replicaZonesInput")
    def replica_zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "replicaZonesInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotInput")
    def snapshot_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceSnapshotEncryptionKeyInput")
    def source_snapshot_encryption_key_input(
        self,
    ) -> typing.Optional["GoogleComputeRegionDiskSourceSnapshotEncryptionKey"]:
        return typing.cast(typing.Optional["GoogleComputeRegionDiskSourceSnapshotEncryptionKey"], jsii.get(self, "sourceSnapshotEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeRegionDiskTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRegionDiskTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="interface")
    def interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interface"))

    @interface.setter
    def interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interface", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="physicalBlockSizeBytes")
    def physical_block_size_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "physicalBlockSizeBytes"))

    @physical_block_size_bytes.setter
    def physical_block_size_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "physical_block_size_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "physicalBlockSizeBytes", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="replicaZones")
    def replica_zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "replicaZones"))

    @replica_zones.setter
    def replica_zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "replica_zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicaZones", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="snapshot")
    def snapshot(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshot"))

    @snapshot.setter
    def snapshot(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "snapshot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshot", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDisk, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDiskConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "replica_zones": "replicaZones",
        "description": "description",
        "disk_encryption_key": "diskEncryptionKey",
        "id": "id",
        "interface": "interface",
        "labels": "labels",
        "physical_block_size_bytes": "physicalBlockSizeBytes",
        "project": "project",
        "region": "region",
        "size": "size",
        "snapshot": "snapshot",
        "source_snapshot_encryption_key": "sourceSnapshotEncryptionKey",
        "timeouts": "timeouts",
        "type": "type",
    },
)
class GoogleComputeRegionDiskConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        name: builtins.str,
        replica_zones: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        disk_encryption_key: typing.Optional[typing.Union["GoogleComputeRegionDiskDiskEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        interface: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        physical_block_size_bytes: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        snapshot: typing.Optional[builtins.str] = None,
        source_snapshot_encryption_key: typing.Optional[typing.Union["GoogleComputeRegionDiskSourceSnapshotEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRegionDiskTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#name GoogleComputeRegionDisk#name}
        :param replica_zones: URLs of the zones where the disk should be replicated to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#replica_zones GoogleComputeRegionDisk#replica_zones}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#description GoogleComputeRegionDisk#description}
        :param disk_encryption_key: disk_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#disk_encryption_key GoogleComputeRegionDisk#disk_encryption_key}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#id GoogleComputeRegionDisk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interface: Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME. The default is SCSI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#interface GoogleComputeRegionDisk#interface}
        :param labels: Labels to apply to this disk. A list of key->value pairs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#labels GoogleComputeRegionDisk#labels}
        :param physical_block_size_bytes: Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. Currently supported sizes are 4096 and 16384, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#physical_block_size_bytes GoogleComputeRegionDisk#physical_block_size_bytes}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#project GoogleComputeRegionDisk#project}.
        :param region: A reference to the region where the disk resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#region GoogleComputeRegionDisk#region}
        :param size: Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk. If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less than the size of the sourceImage or the size of the snapshot. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#size GoogleComputeRegionDisk#size}
        :param snapshot: The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: 'https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot' 'projects/project/global/snapshots/snapshot' 'global/snapshots/snapshot' 'snapshot' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#snapshot GoogleComputeRegionDisk#snapshot}
        :param source_snapshot_encryption_key: source_snapshot_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#source_snapshot_encryption_key GoogleComputeRegionDisk#source_snapshot_encryption_key}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#timeouts GoogleComputeRegionDisk#timeouts}
        :param type: URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#type GoogleComputeRegionDisk#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(disk_encryption_key, dict):
            disk_encryption_key = GoogleComputeRegionDiskDiskEncryptionKey(**disk_encryption_key)
        if isinstance(source_snapshot_encryption_key, dict):
            source_snapshot_encryption_key = GoogleComputeRegionDiskSourceSnapshotEncryptionKey(**source_snapshot_encryption_key)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRegionDiskTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDiskConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument replica_zones", value=replica_zones, expected_type=type_hints["replica_zones"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disk_encryption_key", value=disk_encryption_key, expected_type=type_hints["disk_encryption_key"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument physical_block_size_bytes", value=physical_block_size_bytes, expected_type=type_hints["physical_block_size_bytes"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument snapshot", value=snapshot, expected_type=type_hints["snapshot"])
            check_type(argname="argument source_snapshot_encryption_key", value=source_snapshot_encryption_key, expected_type=type_hints["source_snapshot_encryption_key"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "replica_zones": replica_zones,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if disk_encryption_key is not None:
            self._values["disk_encryption_key"] = disk_encryption_key
        if id is not None:
            self._values["id"] = id
        if interface is not None:
            self._values["interface"] = interface
        if labels is not None:
            self._values["labels"] = labels
        if physical_block_size_bytes is not None:
            self._values["physical_block_size_bytes"] = physical_block_size_bytes
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if size is not None:
            self._values["size"] = size
        if snapshot is not None:
            self._values["snapshot"] = snapshot
        if source_snapshot_encryption_key is not None:
            self._values["source_snapshot_encryption_key"] = source_snapshot_encryption_key
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#name GoogleComputeRegionDisk#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replica_zones(self) -> typing.List[builtins.str]:
        '''URLs of the zones where the disk should be replicated to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#replica_zones GoogleComputeRegionDisk#replica_zones}
        '''
        result = self._values.get("replica_zones")
        assert result is not None, "Required property 'replica_zones' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#description GoogleComputeRegionDisk#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_key(
        self,
    ) -> typing.Optional["GoogleComputeRegionDiskDiskEncryptionKey"]:
        '''disk_encryption_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#disk_encryption_key GoogleComputeRegionDisk#disk_encryption_key}
        '''
        result = self._values.get("disk_encryption_key")
        return typing.cast(typing.Optional["GoogleComputeRegionDiskDiskEncryptionKey"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#id GoogleComputeRegionDisk#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interface(self) -> typing.Optional[builtins.str]:
        '''Specifies the disk interface to use for attaching this disk, which is either SCSI or NVME.

        The default is SCSI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#interface GoogleComputeRegionDisk#interface}
        '''
        result = self._values.get("interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to this disk.  A list of key->value pairs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#labels GoogleComputeRegionDisk#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def physical_block_size_bytes(self) -> typing.Optional[jsii.Number]:
        '''Physical block size of the persistent disk, in bytes.

        If not present
        in a request, a default value is used. Currently supported sizes
        are 4096 and 16384, other sizes may be added in the future.
        If an unsupported value is requested, the error message will list
        the supported values for the caller's project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#physical_block_size_bytes GoogleComputeRegionDisk#physical_block_size_bytes}
        '''
        result = self._values.get("physical_block_size_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#project GoogleComputeRegionDisk#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''A reference to the region where the disk resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#region GoogleComputeRegionDisk#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''Size of the persistent disk, specified in GB.

        You can specify this
        field when creating a persistent disk using the sourceImage or
        sourceSnapshot parameter, or specify it alone to create an empty
        persistent disk.

        If you specify this field along with sourceImage or sourceSnapshot,
        the value of sizeGb must not be less than the size of the sourceImage
        or the size of the snapshot.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#size GoogleComputeRegionDisk#size}
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapshot(self) -> typing.Optional[builtins.str]:
        '''The source snapshot used to create this disk.

        You can provide this as
        a partial or full URL to the resource. For example, the following are
        valid values:

        'https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot'
        'projects/project/global/snapshots/snapshot'
        'global/snapshots/snapshot'
        'snapshot'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#snapshot GoogleComputeRegionDisk#snapshot}
        '''
        result = self._values.get("snapshot")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_snapshot_encryption_key(
        self,
    ) -> typing.Optional["GoogleComputeRegionDiskSourceSnapshotEncryptionKey"]:
        '''source_snapshot_encryption_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#source_snapshot_encryption_key GoogleComputeRegionDisk#source_snapshot_encryption_key}
        '''
        result = self._values.get("source_snapshot_encryption_key")
        return typing.cast(typing.Optional["GoogleComputeRegionDiskSourceSnapshotEncryptionKey"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeRegionDiskTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#timeouts GoogleComputeRegionDisk#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRegionDiskTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''URL of the disk type resource describing which disk type to use to create the disk.

        Provide this when creating the disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#type GoogleComputeRegionDisk#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDiskDiskEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName", "raw_key": "rawKey"},
)
class GoogleComputeRegionDiskDiskEncryptionKey:
    def __init__(
        self,
        *,
        kms_key_name: typing.Optional[builtins.str] = None,
        raw_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_name: The name of the encryption key that is stored in Google Cloud KMS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#kms_key_name GoogleComputeRegionDisk#kms_key_name}
        :param raw_key: Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#raw_key GoogleComputeRegionDisk#raw_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDiskDiskEncryptionKey.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
            check_type(argname="argument raw_key", value=raw_key, expected_type=type_hints["raw_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kms_key_name is not None:
            self._values["kms_key_name"] = kms_key_name
        if raw_key is not None:
            self._values["raw_key"] = raw_key

    @builtins.property
    def kms_key_name(self) -> typing.Optional[builtins.str]:
        '''The name of the encryption key that is stored in Google Cloud KMS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#kms_key_name GoogleComputeRegionDisk#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def raw_key(self) -> typing.Optional[builtins.str]:
        '''Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#raw_key GoogleComputeRegionDisk#raw_key}
        '''
        result = self._values.get("raw_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionDiskDiskEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionDiskDiskEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDiskDiskEncryptionKeyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDiskDiskEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyName")
    def reset_kms_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyName", []))

    @jsii.member(jsii_name="resetRawKey")
    def reset_raw_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRawKey", []))

    @builtins.property
    @jsii.member(jsii_name="sha256")
    def sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha256"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rawKeyInput")
    def raw_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rawKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskDiskEncryptionKeyOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="rawKey")
    def raw_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rawKey"))

    @raw_key.setter
    def raw_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskDiskEncryptionKeyOutputReference, "raw_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rawKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionDiskDiskEncryptionKey]:
        return typing.cast(typing.Optional[GoogleComputeRegionDiskDiskEncryptionKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionDiskDiskEncryptionKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskDiskEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDiskSourceSnapshotEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName", "raw_key": "rawKey"},
)
class GoogleComputeRegionDiskSourceSnapshotEncryptionKey:
    def __init__(
        self,
        *,
        kms_key_name: typing.Optional[builtins.str] = None,
        raw_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kms_key_name: The name of the encryption key that is stored in Google Cloud KMS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#kms_key_name GoogleComputeRegionDisk#kms_key_name}
        :param raw_key: Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#raw_key GoogleComputeRegionDisk#raw_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDiskSourceSnapshotEncryptionKey.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
            check_type(argname="argument raw_key", value=raw_key, expected_type=type_hints["raw_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if kms_key_name is not None:
            self._values["kms_key_name"] = kms_key_name
        if raw_key is not None:
            self._values["raw_key"] = raw_key

    @builtins.property
    def kms_key_name(self) -> typing.Optional[builtins.str]:
        '''The name of the encryption key that is stored in Google Cloud KMS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#kms_key_name GoogleComputeRegionDisk#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def raw_key(self) -> typing.Optional[builtins.str]:
        '''Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648 base64 to either encrypt or decrypt this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#raw_key GoogleComputeRegionDisk#raw_key}
        '''
        result = self._values.get("raw_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionDiskSourceSnapshotEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKmsKeyName")
    def reset_kms_key_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyName", []))

    @jsii.member(jsii_name="resetRawKey")
    def reset_raw_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRawKey", []))

    @builtins.property
    @jsii.member(jsii_name="sha256")
    def sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha256"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rawKeyInput")
    def raw_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rawKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="rawKey")
    def raw_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rawKey"))

    @raw_key.setter
    def raw_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference, "raw_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rawKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeRegionDiskSourceSnapshotEncryptionKey]:
        return typing.cast(typing.Optional[GoogleComputeRegionDiskSourceSnapshotEncryptionKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRegionDiskSourceSnapshotEncryptionKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDiskTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeRegionDiskTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#create GoogleComputeRegionDisk#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#delete GoogleComputeRegionDisk#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#update GoogleComputeRegionDisk#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDiskTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#create GoogleComputeRegionDisk#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#delete GoogleComputeRegionDisk#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_region_disk#update GoogleComputeRegionDisk#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRegionDiskTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRegionDiskTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRegionDisk.GoogleComputeRegionDiskTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRegionDiskTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRegionDiskTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRegionDiskTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRegionDiskTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRegionDiskTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRegionDisk",
    "GoogleComputeRegionDiskConfig",
    "GoogleComputeRegionDiskDiskEncryptionKey",
    "GoogleComputeRegionDiskDiskEncryptionKeyOutputReference",
    "GoogleComputeRegionDiskSourceSnapshotEncryptionKey",
    "GoogleComputeRegionDiskSourceSnapshotEncryptionKeyOutputReference",
    "GoogleComputeRegionDiskTimeouts",
    "GoogleComputeRegionDiskTimeoutsOutputReference",
]

publication.publish()
