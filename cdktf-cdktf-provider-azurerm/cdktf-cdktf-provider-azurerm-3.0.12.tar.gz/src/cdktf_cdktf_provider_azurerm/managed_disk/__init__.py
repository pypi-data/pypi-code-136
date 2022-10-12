'''
# `azurerm_managed_disk`

Refer to the Terraform Registory for docs: [`azurerm_managed_disk`](https://www.terraform.io/docs/providers/azurerm/r/managed_disk).
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


class ManagedDisk(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDisk",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk azurerm_managed_disk}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        create_option: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        storage_account_type: builtins.str,
        disk_access_id: typing.Optional[builtins.str] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_iops_read_only: typing.Optional[jsii.Number] = None,
        disk_iops_read_write: typing.Optional[jsii.Number] = None,
        disk_mbps_read_only: typing.Optional[jsii.Number] = None,
        disk_mbps_read_write: typing.Optional[jsii.Number] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        encryption_settings: typing.Optional[typing.Union["ManagedDiskEncryptionSettings", typing.Dict[str, typing.Any]]] = None,
        gallery_image_reference_id: typing.Optional[builtins.str] = None,
        hyper_v_generation: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_reference_id: typing.Optional[builtins.str] = None,
        logical_sector_size: typing.Optional[jsii.Number] = None,
        max_shares: typing.Optional[jsii.Number] = None,
        network_access_policy: typing.Optional[builtins.str] = None,
        on_demand_bursting_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        os_type: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secure_vm_disk_encryption_set_id: typing.Optional[builtins.str] = None,
        security_type: typing.Optional[builtins.str] = None,
        source_resource_id: typing.Optional[builtins.str] = None,
        source_uri: typing.Optional[builtins.str] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tier: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ManagedDiskTimeouts", typing.Dict[str, typing.Any]]] = None,
        trusted_launch_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk azurerm_managed_disk} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#create_option ManagedDisk#create_option}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#location ManagedDisk#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#name ManagedDisk#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#resource_group_name ManagedDisk#resource_group_name}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#storage_account_type ManagedDisk#storage_account_type}.
        :param disk_access_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_access_id ManagedDisk#disk_access_id}.
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_encryption_set_id ManagedDisk#disk_encryption_set_id}.
        :param disk_iops_read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_iops_read_only ManagedDisk#disk_iops_read_only}.
        :param disk_iops_read_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_iops_read_write ManagedDisk#disk_iops_read_write}.
        :param disk_mbps_read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_mbps_read_only ManagedDisk#disk_mbps_read_only}.
        :param disk_mbps_read_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_mbps_read_write ManagedDisk#disk_mbps_read_write}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_size_gb ManagedDisk#disk_size_gb}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#edge_zone ManagedDisk#edge_zone}.
        :param encryption_settings: encryption_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#encryption_settings ManagedDisk#encryption_settings}
        :param gallery_image_reference_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#gallery_image_reference_id ManagedDisk#gallery_image_reference_id}.
        :param hyper_v_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#hyper_v_generation ManagedDisk#hyper_v_generation}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#id ManagedDisk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_reference_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#image_reference_id ManagedDisk#image_reference_id}.
        :param logical_sector_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#logical_sector_size ManagedDisk#logical_sector_size}.
        :param max_shares: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#max_shares ManagedDisk#max_shares}.
        :param network_access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#network_access_policy ManagedDisk#network_access_policy}.
        :param on_demand_bursting_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#on_demand_bursting_enabled ManagedDisk#on_demand_bursting_enabled}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#os_type ManagedDisk#os_type}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#public_network_access_enabled ManagedDisk#public_network_access_enabled}.
        :param secure_vm_disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#secure_vm_disk_encryption_set_id ManagedDisk#secure_vm_disk_encryption_set_id}.
        :param security_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#security_type ManagedDisk#security_type}.
        :param source_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_resource_id ManagedDisk#source_resource_id}.
        :param source_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_uri ManagedDisk#source_uri}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#storage_account_id ManagedDisk#storage_account_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#tags ManagedDisk#tags}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#tier ManagedDisk#tier}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#timeouts ManagedDisk#timeouts}
        :param trusted_launch_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#trusted_launch_enabled ManagedDisk#trusted_launch_enabled}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#zone ManagedDisk#zone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDisk.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManagedDiskConfig(
            create_option=create_option,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            storage_account_type=storage_account_type,
            disk_access_id=disk_access_id,
            disk_encryption_set_id=disk_encryption_set_id,
            disk_iops_read_only=disk_iops_read_only,
            disk_iops_read_write=disk_iops_read_write,
            disk_mbps_read_only=disk_mbps_read_only,
            disk_mbps_read_write=disk_mbps_read_write,
            disk_size_gb=disk_size_gb,
            edge_zone=edge_zone,
            encryption_settings=encryption_settings,
            gallery_image_reference_id=gallery_image_reference_id,
            hyper_v_generation=hyper_v_generation,
            id=id,
            image_reference_id=image_reference_id,
            logical_sector_size=logical_sector_size,
            max_shares=max_shares,
            network_access_policy=network_access_policy,
            on_demand_bursting_enabled=on_demand_bursting_enabled,
            os_type=os_type,
            public_network_access_enabled=public_network_access_enabled,
            secure_vm_disk_encryption_set_id=secure_vm_disk_encryption_set_id,
            security_type=security_type,
            source_resource_id=source_resource_id,
            source_uri=source_uri,
            storage_account_id=storage_account_id,
            tags=tags,
            tier=tier,
            timeouts=timeouts,
            trusted_launch_enabled=trusted_launch_enabled,
            zone=zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEncryptionSettings")
    def put_encryption_settings(
        self,
        *,
        disk_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionSettingsDiskEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionSettingsKeyEncryptionKey", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_encryption_key: disk_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_encryption_key ManagedDisk#disk_encryption_key}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#enabled ManagedDisk#enabled}.
        :param key_encryption_key: key_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#key_encryption_key ManagedDisk#key_encryption_key}
        '''
        value = ManagedDiskEncryptionSettings(
            disk_encryption_key=disk_encryption_key,
            enabled=enabled,
            key_encryption_key=key_encryption_key,
        )

        return typing.cast(None, jsii.invoke(self, "putEncryptionSettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#create ManagedDisk#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#delete ManagedDisk#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#read ManagedDisk#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#update ManagedDisk#update}.
        '''
        value = ManagedDiskTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDiskAccessId")
    def reset_disk_access_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskAccessId", []))

    @jsii.member(jsii_name="resetDiskEncryptionSetId")
    def reset_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetDiskIopsReadOnly")
    def reset_disk_iops_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskIopsReadOnly", []))

    @jsii.member(jsii_name="resetDiskIopsReadWrite")
    def reset_disk_iops_read_write(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskIopsReadWrite", []))

    @jsii.member(jsii_name="resetDiskMbpsReadOnly")
    def reset_disk_mbps_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskMbpsReadOnly", []))

    @jsii.member(jsii_name="resetDiskMbpsReadWrite")
    def reset_disk_mbps_read_write(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskMbpsReadWrite", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetEdgeZone")
    def reset_edge_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeZone", []))

    @jsii.member(jsii_name="resetEncryptionSettings")
    def reset_encryption_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionSettings", []))

    @jsii.member(jsii_name="resetGalleryImageReferenceId")
    def reset_gallery_image_reference_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGalleryImageReferenceId", []))

    @jsii.member(jsii_name="resetHyperVGeneration")
    def reset_hyper_v_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHyperVGeneration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImageReferenceId")
    def reset_image_reference_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageReferenceId", []))

    @jsii.member(jsii_name="resetLogicalSectorSize")
    def reset_logical_sector_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogicalSectorSize", []))

    @jsii.member(jsii_name="resetMaxShares")
    def reset_max_shares(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxShares", []))

    @jsii.member(jsii_name="resetNetworkAccessPolicy")
    def reset_network_access_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkAccessPolicy", []))

    @jsii.member(jsii_name="resetOnDemandBurstingEnabled")
    def reset_on_demand_bursting_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemandBurstingEnabled", []))

    @jsii.member(jsii_name="resetOsType")
    def reset_os_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsType", []))

    @jsii.member(jsii_name="resetPublicNetworkAccessEnabled")
    def reset_public_network_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicNetworkAccessEnabled", []))

    @jsii.member(jsii_name="resetSecureVmDiskEncryptionSetId")
    def reset_secure_vm_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureVmDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetSecurityType")
    def reset_security_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityType", []))

    @jsii.member(jsii_name="resetSourceResourceId")
    def reset_source_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceResourceId", []))

    @jsii.member(jsii_name="resetSourceUri")
    def reset_source_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceUri", []))

    @jsii.member(jsii_name="resetStorageAccountId")
    def reset_storage_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTier")
    def reset_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTier", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrustedLaunchEnabled")
    def reset_trusted_launch_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedLaunchEnabled", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="encryptionSettings")
    def encryption_settings(self) -> "ManagedDiskEncryptionSettingsOutputReference":
        return typing.cast("ManagedDiskEncryptionSettingsOutputReference", jsii.get(self, "encryptionSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ManagedDiskTimeoutsOutputReference":
        return typing.cast("ManagedDiskTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="createOptionInput")
    def create_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskAccessIdInput")
    def disk_access_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskAccessIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskIopsReadOnlyInput")
    def disk_iops_read_only_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskIopsReadOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="diskIopsReadWriteInput")
    def disk_iops_read_write_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskIopsReadWriteInput"))

    @builtins.property
    @jsii.member(jsii_name="diskMbpsReadOnlyInput")
    def disk_mbps_read_only_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskMbpsReadOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="diskMbpsReadWriteInput")
    def disk_mbps_read_write_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskMbpsReadWriteInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeZoneInput")
    def edge_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionSettingsInput")
    def encryption_settings_input(
        self,
    ) -> typing.Optional["ManagedDiskEncryptionSettings"]:
        return typing.cast(typing.Optional["ManagedDiskEncryptionSettings"], jsii.get(self, "encryptionSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="galleryImageReferenceIdInput")
    def gallery_image_reference_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "galleryImageReferenceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hyperVGenerationInput")
    def hyper_v_generation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hyperVGenerationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="imageReferenceIdInput")
    def image_reference_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageReferenceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="logicalSectorSizeInput")
    def logical_sector_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logicalSectorSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSharesInput")
    def max_shares_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSharesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkAccessPolicyInput")
    def network_access_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkAccessPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandBurstingEnabledInput")
    def on_demand_bursting_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onDemandBurstingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypeInput")
    def os_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabledInput")
    def public_network_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicNetworkAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secureVmDiskEncryptionSetIdInput")
    def secure_vm_disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secureVmDiskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityTypeInput")
    def security_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceResourceIdInput")
    def source_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUriInput")
    def source_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceUriInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountIdInput")
    def storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ManagedDiskTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ManagedDiskTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedLaunchEnabledInput")
    def trusted_launch_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "trustedLaunchEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "create_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskAccessId")
    def disk_access_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskAccessId"))

    @disk_access_id.setter
    def disk_access_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_access_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskAccessId", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskIopsReadOnly")
    def disk_iops_read_only(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskIopsReadOnly"))

    @disk_iops_read_only.setter
    def disk_iops_read_only(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_iops_read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskIopsReadOnly", value)

    @builtins.property
    @jsii.member(jsii_name="diskIopsReadWrite")
    def disk_iops_read_write(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskIopsReadWrite"))

    @disk_iops_read_write.setter
    def disk_iops_read_write(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_iops_read_write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskIopsReadWrite", value)

    @builtins.property
    @jsii.member(jsii_name="diskMbpsReadOnly")
    def disk_mbps_read_only(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskMbpsReadOnly"))

    @disk_mbps_read_only.setter
    def disk_mbps_read_only(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_mbps_read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskMbpsReadOnly", value)

    @builtins.property
    @jsii.member(jsii_name="diskMbpsReadWrite")
    def disk_mbps_read_write(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskMbpsReadWrite"))

    @disk_mbps_read_write.setter
    def disk_mbps_read_write(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_mbps_read_write").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskMbpsReadWrite", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="edgeZone")
    def edge_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeZone"))

    @edge_zone.setter
    def edge_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "edge_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeZone", value)

    @builtins.property
    @jsii.member(jsii_name="galleryImageReferenceId")
    def gallery_image_reference_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "galleryImageReferenceId"))

    @gallery_image_reference_id.setter
    def gallery_image_reference_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "gallery_image_reference_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "galleryImageReferenceId", value)

    @builtins.property
    @jsii.member(jsii_name="hyperVGeneration")
    def hyper_v_generation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hyperVGeneration"))

    @hyper_v_generation.setter
    def hyper_v_generation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "hyper_v_generation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hyperVGeneration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="imageReferenceId")
    def image_reference_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageReferenceId"))

    @image_reference_id.setter
    def image_reference_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "image_reference_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageReferenceId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="logicalSectorSize")
    def logical_sector_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logicalSectorSize"))

    @logical_sector_size.setter
    def logical_sector_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "logical_sector_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logicalSectorSize", value)

    @builtins.property
    @jsii.member(jsii_name="maxShares")
    def max_shares(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxShares"))

    @max_shares.setter
    def max_shares(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "max_shares").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxShares", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkAccessPolicy")
    def network_access_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkAccessPolicy"))

    @network_access_policy.setter
    def network_access_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "network_access_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkAccessPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="onDemandBurstingEnabled")
    def on_demand_bursting_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onDemandBurstingEnabled"))

    @on_demand_bursting_enabled.setter
    def on_demand_bursting_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "on_demand_bursting_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemandBurstingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osType"))

    @os_type.setter
    def os_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "os_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osType", value)

    @builtins.property
    @jsii.member(jsii_name="publicNetworkAccessEnabled")
    def public_network_access_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicNetworkAccessEnabled"))

    @public_network_access_enabled.setter
    def public_network_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "public_network_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicNetworkAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="secureVmDiskEncryptionSetId")
    def secure_vm_disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secureVmDiskEncryptionSetId"))

    @secure_vm_disk_encryption_set_id.setter
    def secure_vm_disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "secure_vm_disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureVmDiskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="securityType")
    def security_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityType"))

    @security_type.setter
    def security_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "security_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityType", value)

    @builtins.property
    @jsii.member(jsii_name="sourceResourceId")
    def source_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceResourceId"))

    @source_resource_id.setter
    def source_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "source_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUri")
    def source_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceUri"))

    @source_uri.setter
    def source_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "source_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUri", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountId")
    def storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountId"))

    @storage_account_id.setter
    def storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="trustedLaunchEnabled")
    def trusted_launch_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "trustedLaunchEnabled"))

    @trusted_launch_enabled.setter
    def trusted_launch_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "trusted_launch_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustedLaunchEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDisk, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "create_option": "createOption",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "storage_account_type": "storageAccountType",
        "disk_access_id": "diskAccessId",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "disk_iops_read_only": "diskIopsReadOnly",
        "disk_iops_read_write": "diskIopsReadWrite",
        "disk_mbps_read_only": "diskMbpsReadOnly",
        "disk_mbps_read_write": "diskMbpsReadWrite",
        "disk_size_gb": "diskSizeGb",
        "edge_zone": "edgeZone",
        "encryption_settings": "encryptionSettings",
        "gallery_image_reference_id": "galleryImageReferenceId",
        "hyper_v_generation": "hyperVGeneration",
        "id": "id",
        "image_reference_id": "imageReferenceId",
        "logical_sector_size": "logicalSectorSize",
        "max_shares": "maxShares",
        "network_access_policy": "networkAccessPolicy",
        "on_demand_bursting_enabled": "onDemandBurstingEnabled",
        "os_type": "osType",
        "public_network_access_enabled": "publicNetworkAccessEnabled",
        "secure_vm_disk_encryption_set_id": "secureVmDiskEncryptionSetId",
        "security_type": "securityType",
        "source_resource_id": "sourceResourceId",
        "source_uri": "sourceUri",
        "storage_account_id": "storageAccountId",
        "tags": "tags",
        "tier": "tier",
        "timeouts": "timeouts",
        "trusted_launch_enabled": "trustedLaunchEnabled",
        "zone": "zone",
    },
)
class ManagedDiskConfig(cdktf.TerraformMetaArguments):
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
        create_option: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        storage_account_type: builtins.str,
        disk_access_id: typing.Optional[builtins.str] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_iops_read_only: typing.Optional[jsii.Number] = None,
        disk_iops_read_write: typing.Optional[jsii.Number] = None,
        disk_mbps_read_only: typing.Optional[jsii.Number] = None,
        disk_mbps_read_write: typing.Optional[jsii.Number] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        encryption_settings: typing.Optional[typing.Union["ManagedDiskEncryptionSettings", typing.Dict[str, typing.Any]]] = None,
        gallery_image_reference_id: typing.Optional[builtins.str] = None,
        hyper_v_generation: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        image_reference_id: typing.Optional[builtins.str] = None,
        logical_sector_size: typing.Optional[jsii.Number] = None,
        max_shares: typing.Optional[jsii.Number] = None,
        network_access_policy: typing.Optional[builtins.str] = None,
        on_demand_bursting_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        os_type: typing.Optional[builtins.str] = None,
        public_network_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secure_vm_disk_encryption_set_id: typing.Optional[builtins.str] = None,
        security_type: typing.Optional[builtins.str] = None,
        source_resource_id: typing.Optional[builtins.str] = None,
        source_uri: typing.Optional[builtins.str] = None,
        storage_account_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tier: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["ManagedDiskTimeouts", typing.Dict[str, typing.Any]]] = None,
        trusted_launch_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#create_option ManagedDisk#create_option}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#location ManagedDisk#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#name ManagedDisk#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#resource_group_name ManagedDisk#resource_group_name}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#storage_account_type ManagedDisk#storage_account_type}.
        :param disk_access_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_access_id ManagedDisk#disk_access_id}.
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_encryption_set_id ManagedDisk#disk_encryption_set_id}.
        :param disk_iops_read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_iops_read_only ManagedDisk#disk_iops_read_only}.
        :param disk_iops_read_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_iops_read_write ManagedDisk#disk_iops_read_write}.
        :param disk_mbps_read_only: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_mbps_read_only ManagedDisk#disk_mbps_read_only}.
        :param disk_mbps_read_write: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_mbps_read_write ManagedDisk#disk_mbps_read_write}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_size_gb ManagedDisk#disk_size_gb}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#edge_zone ManagedDisk#edge_zone}.
        :param encryption_settings: encryption_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#encryption_settings ManagedDisk#encryption_settings}
        :param gallery_image_reference_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#gallery_image_reference_id ManagedDisk#gallery_image_reference_id}.
        :param hyper_v_generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#hyper_v_generation ManagedDisk#hyper_v_generation}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#id ManagedDisk#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param image_reference_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#image_reference_id ManagedDisk#image_reference_id}.
        :param logical_sector_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#logical_sector_size ManagedDisk#logical_sector_size}.
        :param max_shares: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#max_shares ManagedDisk#max_shares}.
        :param network_access_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#network_access_policy ManagedDisk#network_access_policy}.
        :param on_demand_bursting_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#on_demand_bursting_enabled ManagedDisk#on_demand_bursting_enabled}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#os_type ManagedDisk#os_type}.
        :param public_network_access_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#public_network_access_enabled ManagedDisk#public_network_access_enabled}.
        :param secure_vm_disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#secure_vm_disk_encryption_set_id ManagedDisk#secure_vm_disk_encryption_set_id}.
        :param security_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#security_type ManagedDisk#security_type}.
        :param source_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_resource_id ManagedDisk#source_resource_id}.
        :param source_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_uri ManagedDisk#source_uri}.
        :param storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#storage_account_id ManagedDisk#storage_account_id}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#tags ManagedDisk#tags}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#tier ManagedDisk#tier}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#timeouts ManagedDisk#timeouts}
        :param trusted_launch_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#trusted_launch_enabled ManagedDisk#trusted_launch_enabled}.
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#zone ManagedDisk#zone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(encryption_settings, dict):
            encryption_settings = ManagedDiskEncryptionSettings(**encryption_settings)
        if isinstance(timeouts, dict):
            timeouts = ManagedDiskTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument disk_access_id", value=disk_access_id, expected_type=type_hints["disk_access_id"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument disk_iops_read_only", value=disk_iops_read_only, expected_type=type_hints["disk_iops_read_only"])
            check_type(argname="argument disk_iops_read_write", value=disk_iops_read_write, expected_type=type_hints["disk_iops_read_write"])
            check_type(argname="argument disk_mbps_read_only", value=disk_mbps_read_only, expected_type=type_hints["disk_mbps_read_only"])
            check_type(argname="argument disk_mbps_read_write", value=disk_mbps_read_write, expected_type=type_hints["disk_mbps_read_write"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument edge_zone", value=edge_zone, expected_type=type_hints["edge_zone"])
            check_type(argname="argument encryption_settings", value=encryption_settings, expected_type=type_hints["encryption_settings"])
            check_type(argname="argument gallery_image_reference_id", value=gallery_image_reference_id, expected_type=type_hints["gallery_image_reference_id"])
            check_type(argname="argument hyper_v_generation", value=hyper_v_generation, expected_type=type_hints["hyper_v_generation"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image_reference_id", value=image_reference_id, expected_type=type_hints["image_reference_id"])
            check_type(argname="argument logical_sector_size", value=logical_sector_size, expected_type=type_hints["logical_sector_size"])
            check_type(argname="argument max_shares", value=max_shares, expected_type=type_hints["max_shares"])
            check_type(argname="argument network_access_policy", value=network_access_policy, expected_type=type_hints["network_access_policy"])
            check_type(argname="argument on_demand_bursting_enabled", value=on_demand_bursting_enabled, expected_type=type_hints["on_demand_bursting_enabled"])
            check_type(argname="argument os_type", value=os_type, expected_type=type_hints["os_type"])
            check_type(argname="argument public_network_access_enabled", value=public_network_access_enabled, expected_type=type_hints["public_network_access_enabled"])
            check_type(argname="argument secure_vm_disk_encryption_set_id", value=secure_vm_disk_encryption_set_id, expected_type=type_hints["secure_vm_disk_encryption_set_id"])
            check_type(argname="argument security_type", value=security_type, expected_type=type_hints["security_type"])
            check_type(argname="argument source_resource_id", value=source_resource_id, expected_type=type_hints["source_resource_id"])
            check_type(argname="argument source_uri", value=source_uri, expected_type=type_hints["source_uri"])
            check_type(argname="argument storage_account_id", value=storage_account_id, expected_type=type_hints["storage_account_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument trusted_launch_enabled", value=trusted_launch_enabled, expected_type=type_hints["trusted_launch_enabled"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "create_option": create_option,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "storage_account_type": storage_account_type,
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
        if disk_access_id is not None:
            self._values["disk_access_id"] = disk_access_id
        if disk_encryption_set_id is not None:
            self._values["disk_encryption_set_id"] = disk_encryption_set_id
        if disk_iops_read_only is not None:
            self._values["disk_iops_read_only"] = disk_iops_read_only
        if disk_iops_read_write is not None:
            self._values["disk_iops_read_write"] = disk_iops_read_write
        if disk_mbps_read_only is not None:
            self._values["disk_mbps_read_only"] = disk_mbps_read_only
        if disk_mbps_read_write is not None:
            self._values["disk_mbps_read_write"] = disk_mbps_read_write
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if edge_zone is not None:
            self._values["edge_zone"] = edge_zone
        if encryption_settings is not None:
            self._values["encryption_settings"] = encryption_settings
        if gallery_image_reference_id is not None:
            self._values["gallery_image_reference_id"] = gallery_image_reference_id
        if hyper_v_generation is not None:
            self._values["hyper_v_generation"] = hyper_v_generation
        if id is not None:
            self._values["id"] = id
        if image_reference_id is not None:
            self._values["image_reference_id"] = image_reference_id
        if logical_sector_size is not None:
            self._values["logical_sector_size"] = logical_sector_size
        if max_shares is not None:
            self._values["max_shares"] = max_shares
        if network_access_policy is not None:
            self._values["network_access_policy"] = network_access_policy
        if on_demand_bursting_enabled is not None:
            self._values["on_demand_bursting_enabled"] = on_demand_bursting_enabled
        if os_type is not None:
            self._values["os_type"] = os_type
        if public_network_access_enabled is not None:
            self._values["public_network_access_enabled"] = public_network_access_enabled
        if secure_vm_disk_encryption_set_id is not None:
            self._values["secure_vm_disk_encryption_set_id"] = secure_vm_disk_encryption_set_id
        if security_type is not None:
            self._values["security_type"] = security_type
        if source_resource_id is not None:
            self._values["source_resource_id"] = source_resource_id
        if source_uri is not None:
            self._values["source_uri"] = source_uri
        if storage_account_id is not None:
            self._values["storage_account_id"] = storage_account_id
        if tags is not None:
            self._values["tags"] = tags
        if tier is not None:
            self._values["tier"] = tier
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if trusted_launch_enabled is not None:
            self._values["trusted_launch_enabled"] = trusted_launch_enabled
        if zone is not None:
            self._values["zone"] = zone

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
    def create_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#create_option ManagedDisk#create_option}.'''
        result = self._values.get("create_option")
        assert result is not None, "Required property 'create_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#location ManagedDisk#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#name ManagedDisk#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#resource_group_name ManagedDisk#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#storage_account_type ManagedDisk#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_access_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_access_id ManagedDisk#disk_access_id}.'''
        result = self._values.get("disk_access_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_encryption_set_id ManagedDisk#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_iops_read_only(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_iops_read_only ManagedDisk#disk_iops_read_only}.'''
        result = self._values.get("disk_iops_read_only")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_iops_read_write(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_iops_read_write ManagedDisk#disk_iops_read_write}.'''
        result = self._values.get("disk_iops_read_write")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_mbps_read_only(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_mbps_read_only ManagedDisk#disk_mbps_read_only}.'''
        result = self._values.get("disk_mbps_read_only")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_mbps_read_write(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_mbps_read_write ManagedDisk#disk_mbps_read_write}.'''
        result = self._values.get("disk_mbps_read_write")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_size_gb ManagedDisk#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def edge_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#edge_zone ManagedDisk#edge_zone}.'''
        result = self._values.get("edge_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_settings(self) -> typing.Optional["ManagedDiskEncryptionSettings"]:
        '''encryption_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#encryption_settings ManagedDisk#encryption_settings}
        '''
        result = self._values.get("encryption_settings")
        return typing.cast(typing.Optional["ManagedDiskEncryptionSettings"], result)

    @builtins.property
    def gallery_image_reference_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#gallery_image_reference_id ManagedDisk#gallery_image_reference_id}.'''
        result = self._values.get("gallery_image_reference_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hyper_v_generation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#hyper_v_generation ManagedDisk#hyper_v_generation}.'''
        result = self._values.get("hyper_v_generation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#id ManagedDisk#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_reference_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#image_reference_id ManagedDisk#image_reference_id}.'''
        result = self._values.get("image_reference_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logical_sector_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#logical_sector_size ManagedDisk#logical_sector_size}.'''
        result = self._values.get("logical_sector_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_shares(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#max_shares ManagedDisk#max_shares}.'''
        result = self._values.get("max_shares")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_access_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#network_access_policy ManagedDisk#network_access_policy}.'''
        result = self._values.get("network_access_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_demand_bursting_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#on_demand_bursting_enabled ManagedDisk#on_demand_bursting_enabled}.'''
        result = self._values.get("on_demand_bursting_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def os_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#os_type ManagedDisk#os_type}.'''
        result = self._values.get("os_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_network_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#public_network_access_enabled ManagedDisk#public_network_access_enabled}.'''
        result = self._values.get("public_network_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secure_vm_disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#secure_vm_disk_encryption_set_id ManagedDisk#secure_vm_disk_encryption_set_id}.'''
        result = self._values.get("secure_vm_disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#security_type ManagedDisk#security_type}.'''
        result = self._values.get("security_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_resource_id ManagedDisk#source_resource_id}.'''
        result = self._values.get("source_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_uri ManagedDisk#source_uri}.'''
        result = self._values.get("source_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#storage_account_id ManagedDisk#storage_account_id}.'''
        result = self._values.get("storage_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#tags ManagedDisk#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#tier ManagedDisk#tier}.'''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ManagedDiskTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#timeouts ManagedDisk#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ManagedDiskTimeouts"], result)

    @builtins.property
    def trusted_launch_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#trusted_launch_enabled ManagedDisk#trusted_launch_enabled}.'''
        result = self._values.get("trusted_launch_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#zone ManagedDisk#zone}.'''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskEncryptionSettings",
    jsii_struct_bases=[],
    name_mapping={
        "disk_encryption_key": "diskEncryptionKey",
        "enabled": "enabled",
        "key_encryption_key": "keyEncryptionKey",
    },
)
class ManagedDiskEncryptionSettings:
    def __init__(
        self,
        *,
        disk_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionSettingsDiskEncryptionKey", typing.Dict[str, typing.Any]]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        key_encryption_key: typing.Optional[typing.Union["ManagedDiskEncryptionSettingsKeyEncryptionKey", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param disk_encryption_key: disk_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_encryption_key ManagedDisk#disk_encryption_key}
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#enabled ManagedDisk#enabled}.
        :param key_encryption_key: key_encryption_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#key_encryption_key ManagedDisk#key_encryption_key}
        '''
        if isinstance(disk_encryption_key, dict):
            disk_encryption_key = ManagedDiskEncryptionSettingsDiskEncryptionKey(**disk_encryption_key)
        if isinstance(key_encryption_key, dict):
            key_encryption_key = ManagedDiskEncryptionSettingsKeyEncryptionKey(**key_encryption_key)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskEncryptionSettings.__init__)
            check_type(argname="argument disk_encryption_key", value=disk_encryption_key, expected_type=type_hints["disk_encryption_key"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument key_encryption_key", value=key_encryption_key, expected_type=type_hints["key_encryption_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disk_encryption_key is not None:
            self._values["disk_encryption_key"] = disk_encryption_key
        if enabled is not None:
            self._values["enabled"] = enabled
        if key_encryption_key is not None:
            self._values["key_encryption_key"] = key_encryption_key

    @builtins.property
    def disk_encryption_key(
        self,
    ) -> typing.Optional["ManagedDiskEncryptionSettingsDiskEncryptionKey"]:
        '''disk_encryption_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#disk_encryption_key ManagedDisk#disk_encryption_key}
        '''
        result = self._values.get("disk_encryption_key")
        return typing.cast(typing.Optional["ManagedDiskEncryptionSettingsDiskEncryptionKey"], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#enabled ManagedDisk#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def key_encryption_key(
        self,
    ) -> typing.Optional["ManagedDiskEncryptionSettingsKeyEncryptionKey"]:
        '''key_encryption_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#key_encryption_key ManagedDisk#key_encryption_key}
        '''
        result = self._values.get("key_encryption_key")
        return typing.cast(typing.Optional["ManagedDiskEncryptionSettingsKeyEncryptionKey"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskEncryptionSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskEncryptionSettingsDiskEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"secret_url": "secretUrl", "source_vault_id": "sourceVaultId"},
)
class ManagedDiskEncryptionSettingsDiskEncryptionKey:
    def __init__(
        self,
        *,
        secret_url: builtins.str,
        source_vault_id: builtins.str,
    ) -> None:
        '''
        :param secret_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#secret_url ManagedDisk#secret_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskEncryptionSettingsDiskEncryptionKey.__init__)
            check_type(argname="argument secret_url", value=secret_url, expected_type=type_hints["secret_url"])
            check_type(argname="argument source_vault_id", value=source_vault_id, expected_type=type_hints["source_vault_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_url": secret_url,
            "source_vault_id": source_vault_id,
        }

    @builtins.property
    def secret_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#secret_url ManagedDisk#secret_url}.'''
        result = self._values.get("secret_url")
        assert result is not None, "Required property 'secret_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.'''
        result = self._values.get("source_vault_id")
        assert result is not None, "Required property 'source_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskEncryptionSettingsDiskEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="secretUrlInput")
    def secret_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultIdInput")
    def source_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretUrl")
    def secret_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretUrl"))

    @secret_url.setter
    def secret_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference, "secret_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretUrl", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVaultId")
    def source_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVaultId"))

    @source_vault_id.setter
    def source_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference, "source_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedDiskEncryptionSettingsDiskEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionSettingsDiskEncryptionKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDiskEncryptionSettingsDiskEncryptionKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskEncryptionSettingsKeyEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"key_url": "keyUrl", "source_vault_id": "sourceVaultId"},
)
class ManagedDiskEncryptionSettingsKeyEncryptionKey:
    def __init__(self, *, key_url: builtins.str, source_vault_id: builtins.str) -> None:
        '''
        :param key_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#key_url ManagedDisk#key_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskEncryptionSettingsKeyEncryptionKey.__init__)
            check_type(argname="argument key_url", value=key_url, expected_type=type_hints["key_url"])
            check_type(argname="argument source_vault_id", value=source_vault_id, expected_type=type_hints["source_vault_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_url": key_url,
            "source_vault_id": source_vault_id,
        }

    @builtins.property
    def key_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#key_url ManagedDisk#key_url}.'''
        result = self._values.get("key_url")
        assert result is not None, "Required property 'key_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.'''
        result = self._values.get("source_vault_id")
        assert result is not None, "Required property 'source_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskEncryptionSettingsKeyEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="keyUrlInput")
    def key_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultIdInput")
    def source_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUrl")
    def key_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyUrl"))

    @key_url.setter
    def key_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference, "key_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVaultId")
    def source_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVaultId"))

    @source_vault_id.setter
    def source_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference, "source_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ManagedDiskEncryptionSettingsKeyEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionSettingsKeyEncryptionKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDiskEncryptionSettingsKeyEncryptionKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedDiskEncryptionSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskEncryptionSettingsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskEncryptionSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiskEncryptionKey")
    def put_disk_encryption_key(
        self,
        *,
        secret_url: builtins.str,
        source_vault_id: builtins.str,
    ) -> None:
        '''
        :param secret_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#secret_url ManagedDisk#secret_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        value = ManagedDiskEncryptionSettingsDiskEncryptionKey(
            secret_url=secret_url, source_vault_id=source_vault_id
        )

        return typing.cast(None, jsii.invoke(self, "putDiskEncryptionKey", [value]))

    @jsii.member(jsii_name="putKeyEncryptionKey")
    def put_key_encryption_key(
        self,
        *,
        key_url: builtins.str,
        source_vault_id: builtins.str,
    ) -> None:
        '''
        :param key_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#key_url ManagedDisk#key_url}.
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#source_vault_id ManagedDisk#source_vault_id}.
        '''
        value = ManagedDiskEncryptionSettingsKeyEncryptionKey(
            key_url=key_url, source_vault_id=source_vault_id
        )

        return typing.cast(None, jsii.invoke(self, "putKeyEncryptionKey", [value]))

    @jsii.member(jsii_name="resetDiskEncryptionKey")
    def reset_disk_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKey", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetKeyEncryptionKey")
    def reset_key_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyEncryptionKey", []))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKey")
    def disk_encryption_key(
        self,
    ) -> ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference:
        return typing.cast(ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference, jsii.get(self, "diskEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="keyEncryptionKey")
    def key_encryption_key(
        self,
    ) -> ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference:
        return typing.cast(ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference, jsii.get(self, "keyEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyInput")
    def disk_encryption_key_input(
        self,
    ) -> typing.Optional[ManagedDiskEncryptionSettingsDiskEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionSettingsDiskEncryptionKey], jsii.get(self, "diskEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="keyEncryptionKeyInput")
    def key_encryption_key_input(
        self,
    ) -> typing.Optional[ManagedDiskEncryptionSettingsKeyEncryptionKey]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionSettingsKeyEncryptionKey], jsii.get(self, "keyEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ManagedDiskEncryptionSettings]:
        return typing.cast(typing.Optional[ManagedDiskEncryptionSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ManagedDiskEncryptionSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskEncryptionSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ManagedDiskTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#create ManagedDisk#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#delete ManagedDisk#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#read ManagedDisk#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#update ManagedDisk#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedDiskTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#create ManagedDisk#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#delete ManagedDisk#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#read ManagedDisk#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/managed_disk#update ManagedDisk#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedDiskTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedDiskTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.managedDisk.ManagedDiskTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedDiskTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedDiskTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedDiskTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedDiskTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedDiskTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ManagedDisk",
    "ManagedDiskConfig",
    "ManagedDiskEncryptionSettings",
    "ManagedDiskEncryptionSettingsDiskEncryptionKey",
    "ManagedDiskEncryptionSettingsDiskEncryptionKeyOutputReference",
    "ManagedDiskEncryptionSettingsKeyEncryptionKey",
    "ManagedDiskEncryptionSettingsKeyEncryptionKeyOutputReference",
    "ManagedDiskEncryptionSettingsOutputReference",
    "ManagedDiskTimeouts",
    "ManagedDiskTimeoutsOutputReference",
]

publication.publish()
