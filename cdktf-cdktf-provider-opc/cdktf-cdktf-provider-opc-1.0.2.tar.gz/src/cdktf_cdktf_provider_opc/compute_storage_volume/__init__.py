'''
# `opc_compute_storage_volume`

Refer to the Terraform Registory for docs: [`opc_compute_storage_volume`](https://www.terraform.io/docs/providers/opc/r/compute_storage_volume).
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


class ComputeStorageVolume(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeStorageVolume.ComputeStorageVolume",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume opc_compute_storage_volume}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        size: jsii.Number,
        bootable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        hypervisor: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_list: typing.Optional[builtins.str] = None,
        image_list_entry: typing.Optional[jsii.Number] = None,
        machine_image: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        platform: typing.Optional[builtins.str] = None,
        readonly: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot: typing.Optional[builtins.str] = None,
        snapshot_account: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        storage_pool: typing.Optional[builtins.str] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeStorageVolumeTimeouts", typing.Dict[str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume opc_compute_storage_volume} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#name ComputeStorageVolume#name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#size ComputeStorageVolume#size}.
        :param bootable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#bootable ComputeStorageVolume#bootable}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#description ComputeStorageVolume#description}.
        :param hypervisor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#hypervisor ComputeStorageVolume#hypervisor}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#id ComputeStorageVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#image_list ComputeStorageVolume#image_list}.
        :param image_list_entry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#image_list_entry ComputeStorageVolume#image_list_entry}.
        :param machine_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#machine_image ComputeStorageVolume#machine_image}.
        :param managed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#managed ComputeStorageVolume#managed}.
        :param platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#platform ComputeStorageVolume#platform}.
        :param readonly: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#readonly ComputeStorageVolume#readonly}.
        :param snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot ComputeStorageVolume#snapshot}.
        :param snapshot_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot_account ComputeStorageVolume#snapshot_account}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot_id ComputeStorageVolume#snapshot_id}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#status ComputeStorageVolume#status}.
        :param storage_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#storage_pool ComputeStorageVolume#storage_pool}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#storage_type ComputeStorageVolume#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#tags ComputeStorageVolume#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#timeouts ComputeStorageVolume#timeouts}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#uri ComputeStorageVolume#uri}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeStorageVolume.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeStorageVolumeConfig(
            name=name,
            size=size,
            bootable=bootable,
            description=description,
            hypervisor=hypervisor,
            id=id,
            image_list=image_list,
            image_list_entry=image_list_entry,
            machine_image=machine_image,
            managed=managed,
            platform=platform,
            readonly=readonly,
            snapshot=snapshot,
            snapshot_account=snapshot_account,
            snapshot_id=snapshot_id,
            status=status,
            storage_pool=storage_pool,
            storage_type=storage_type,
            tags=tags,
            timeouts=timeouts,
            uri=uri,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#create ComputeStorageVolume#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#delete ComputeStorageVolume#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#update ComputeStorageVolume#update}.
        '''
        value = ComputeStorageVolumeTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBootable")
    def reset_bootable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootable", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHypervisor")
    def reset_hypervisor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHypervisor", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageList")
    def reset_image_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageList", []))

    @jsii.member(jsii_name="resetImageListEntry")
    def reset_image_list_entry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageListEntry", []))

    @jsii.member(jsii_name="resetMachineImage")
    def reset_machine_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineImage", []))

    @jsii.member(jsii_name="resetManaged")
    def reset_managed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManaged", []))

    @jsii.member(jsii_name="resetPlatform")
    def reset_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatform", []))

    @jsii.member(jsii_name="resetReadonly")
    def reset_readonly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadonly", []))

    @jsii.member(jsii_name="resetSnapshot")
    def reset_snapshot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshot", []))

    @jsii.member(jsii_name="resetSnapshotAccount")
    def reset_snapshot_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotAccount", []))

    @jsii.member(jsii_name="resetSnapshotId")
    def reset_snapshot_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotId", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetStoragePool")
    def reset_storage_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoragePool", []))

    @jsii.member(jsii_name="resetStorageType")
    def reset_storage_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageType", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeStorageVolumeTimeoutsOutputReference":
        return typing.cast("ComputeStorageVolumeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bootableInput")
    def bootable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bootableInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="hypervisorInput")
    def hypervisor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hypervisorInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageListEntryInput")
    def image_list_entry_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageListEntryInput"))

    @builtins.property
    @jsii.member(jsii_name="imageListInput")
    def image_list_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageListInput"))

    @builtins.property
    @jsii.member(jsii_name="machineImageInput")
    def machine_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineImageInput"))

    @builtins.property
    @jsii.member(jsii_name="managedInput")
    def managed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "managedInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="platformInput")
    def platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformInput"))

    @builtins.property
    @jsii.member(jsii_name="readonlyInput")
    def readonly_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readonlyInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotAccountInput")
    def snapshot_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotIdInput")
    def snapshot_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotIdInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotInput")
    def snapshot_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapshotInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="storagePoolInput")
    def storage_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storagePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="storageTypeInput")
    def storage_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeStorageVolumeTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeStorageVolumeTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="bootable")
    def bootable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bootable"))

    @bootable.setter
    def bootable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "bootable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootable", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hypervisor")
    def hypervisor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hypervisor"))

    @hypervisor.setter
    def hypervisor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "hypervisor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hypervisor", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageList")
    def image_list(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageList"))

    @image_list.setter
    def image_list(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "image_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageList", value)

    @builtins.property
    @jsii.member(jsii_name="imageListEntry")
    def image_list_entry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageListEntry"))

    @image_list_entry.setter
    def image_list_entry(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "image_list_entry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageListEntry", value)

    @builtins.property
    @jsii.member(jsii_name="machineImage")
    def machine_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineImage"))

    @machine_image.setter
    def machine_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "machine_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineImage", value)

    @builtins.property
    @jsii.member(jsii_name="managed")
    def managed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "managed"))

    @managed.setter
    def managed(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "managed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managed", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="readonly")
    def readonly(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readonly"))

    @readonly.setter
    def readonly(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "readonly").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readonly", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="snapshot")
    def snapshot(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshot"))

    @snapshot.setter
    def snapshot(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "snapshot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshot", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotAccount")
    def snapshot_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotAccount"))

    @snapshot_account.setter
    def snapshot_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "snapshot_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotAccount", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotId")
    def snapshot_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapshotId"))

    @snapshot_id.setter
    def snapshot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "snapshot_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotId", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="storagePool")
    def storage_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storagePool"))

    @storage_pool.setter
    def storage_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "storage_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagePool", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "storage_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolume, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeStorageVolume.ComputeStorageVolumeConfig",
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
        "size": "size",
        "bootable": "bootable",
        "description": "description",
        "hypervisor": "hypervisor",
        "id": "id",
        "image_list": "imageList",
        "image_list_entry": "imageListEntry",
        "machine_image": "machineImage",
        "managed": "managed",
        "platform": "platform",
        "readonly": "readonly",
        "snapshot": "snapshot",
        "snapshot_account": "snapshotAccount",
        "snapshot_id": "snapshotId",
        "status": "status",
        "storage_pool": "storagePool",
        "storage_type": "storageType",
        "tags": "tags",
        "timeouts": "timeouts",
        "uri": "uri",
    },
)
class ComputeStorageVolumeConfig(cdktf.TerraformMetaArguments):
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
        size: jsii.Number,
        bootable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        hypervisor: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_list: typing.Optional[builtins.str] = None,
        image_list_entry: typing.Optional[jsii.Number] = None,
        machine_image: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        platform: typing.Optional[builtins.str] = None,
        readonly: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snapshot: typing.Optional[builtins.str] = None,
        snapshot_account: typing.Optional[builtins.str] = None,
        snapshot_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        storage_pool: typing.Optional[builtins.str] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeStorageVolumeTimeouts", typing.Dict[str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#name ComputeStorageVolume#name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#size ComputeStorageVolume#size}.
        :param bootable: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#bootable ComputeStorageVolume#bootable}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#description ComputeStorageVolume#description}.
        :param hypervisor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#hypervisor ComputeStorageVolume#hypervisor}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#id ComputeStorageVolume#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#image_list ComputeStorageVolume#image_list}.
        :param image_list_entry: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#image_list_entry ComputeStorageVolume#image_list_entry}.
        :param machine_image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#machine_image ComputeStorageVolume#machine_image}.
        :param managed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#managed ComputeStorageVolume#managed}.
        :param platform: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#platform ComputeStorageVolume#platform}.
        :param readonly: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#readonly ComputeStorageVolume#readonly}.
        :param snapshot: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot ComputeStorageVolume#snapshot}.
        :param snapshot_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot_account ComputeStorageVolume#snapshot_account}.
        :param snapshot_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot_id ComputeStorageVolume#snapshot_id}.
        :param status: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#status ComputeStorageVolume#status}.
        :param storage_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#storage_pool ComputeStorageVolume#storage_pool}.
        :param storage_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#storage_type ComputeStorageVolume#storage_type}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#tags ComputeStorageVolume#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#timeouts ComputeStorageVolume#timeouts}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#uri ComputeStorageVolume#uri}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ComputeStorageVolumeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeStorageVolumeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument bootable", value=bootable, expected_type=type_hints["bootable"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument hypervisor", value=hypervisor, expected_type=type_hints["hypervisor"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_list", value=image_list, expected_type=type_hints["image_list"])
            check_type(argname="argument image_list_entry", value=image_list_entry, expected_type=type_hints["image_list_entry"])
            check_type(argname="argument machine_image", value=machine_image, expected_type=type_hints["machine_image"])
            check_type(argname="argument managed", value=managed, expected_type=type_hints["managed"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument readonly", value=readonly, expected_type=type_hints["readonly"])
            check_type(argname="argument snapshot", value=snapshot, expected_type=type_hints["snapshot"])
            check_type(argname="argument snapshot_account", value=snapshot_account, expected_type=type_hints["snapshot_account"])
            check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument storage_pool", value=storage_pool, expected_type=type_hints["storage_pool"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "size": size,
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
        if bootable is not None:
            self._values["bootable"] = bootable
        if description is not None:
            self._values["description"] = description
        if hypervisor is not None:
            self._values["hypervisor"] = hypervisor
        if id is not None:
            self._values["id"] = id
        if image_list is not None:
            self._values["image_list"] = image_list
        if image_list_entry is not None:
            self._values["image_list_entry"] = image_list_entry
        if machine_image is not None:
            self._values["machine_image"] = machine_image
        if managed is not None:
            self._values["managed"] = managed
        if platform is not None:
            self._values["platform"] = platform
        if readonly is not None:
            self._values["readonly"] = readonly
        if snapshot is not None:
            self._values["snapshot"] = snapshot
        if snapshot_account is not None:
            self._values["snapshot_account"] = snapshot_account
        if snapshot_id is not None:
            self._values["snapshot_id"] = snapshot_id
        if status is not None:
            self._values["status"] = status
        if storage_pool is not None:
            self._values["storage_pool"] = storage_pool
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if uri is not None:
            self._values["uri"] = uri

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#name ComputeStorageVolume#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#size ComputeStorageVolume#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def bootable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#bootable ComputeStorageVolume#bootable}.'''
        result = self._values.get("bootable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#description ComputeStorageVolume#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hypervisor(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#hypervisor ComputeStorageVolume#hypervisor}.'''
        result = self._values.get("hypervisor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#id ComputeStorageVolume#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_list(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#image_list ComputeStorageVolume#image_list}.'''
        result = self._values.get("image_list")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_list_entry(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#image_list_entry ComputeStorageVolume#image_list_entry}.'''
        result = self._values.get("image_list_entry")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def machine_image(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#machine_image ComputeStorageVolume#machine_image}.'''
        result = self._values.get("machine_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#managed ComputeStorageVolume#managed}.'''
        result = self._values.get("managed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#platform ComputeStorageVolume#platform}.'''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readonly(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#readonly ComputeStorageVolume#readonly}.'''
        result = self._values.get("readonly")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def snapshot(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot ComputeStorageVolume#snapshot}.'''
        result = self._values.get("snapshot")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot_account ComputeStorageVolume#snapshot_account}.'''
        result = self._values.get("snapshot_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snapshot_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#snapshot_id ComputeStorageVolume#snapshot_id}.'''
        result = self._values.get("snapshot_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#status ComputeStorageVolume#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_pool(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#storage_pool ComputeStorageVolume#storage_pool}.'''
        result = self._values.get("storage_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#storage_type ComputeStorageVolume#storage_type}.'''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#tags ComputeStorageVolume#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeStorageVolumeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#timeouts ComputeStorageVolume#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeStorageVolumeTimeouts"], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#uri ComputeStorageVolume#uri}.'''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeStorageVolumeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeStorageVolume.ComputeStorageVolumeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComputeStorageVolumeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#create ComputeStorageVolume#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#delete ComputeStorageVolume#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#update ComputeStorageVolume#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeStorageVolumeTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#create ComputeStorageVolume#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#delete ComputeStorageVolume#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_storage_volume#update ComputeStorageVolume#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeStorageVolumeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeStorageVolumeTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeStorageVolume.ComputeStorageVolumeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeStorageVolumeTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolumeTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolumeTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolumeTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeStorageVolumeTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeStorageVolumeTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeStorageVolumeTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeStorageVolumeTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeStorageVolume",
    "ComputeStorageVolumeConfig",
    "ComputeStorageVolumeTimeouts",
    "ComputeStorageVolumeTimeoutsOutputReference",
]

publication.publish()
