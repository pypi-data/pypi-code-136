'''
# `azurerm_virtual_machine_scale_set`

Refer to the Terraform Registory for docs: [`azurerm_virtual_machine_scale_set`](https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set).
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


class VirtualMachineScaleSet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set azurerm_virtual_machine_scale_set}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        network_profile: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetNetworkProfile", typing.Dict[str, typing.Any]]]],
        os_profile: typing.Union["VirtualMachineScaleSetOsProfile", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        sku: typing.Union["VirtualMachineScaleSetSku", typing.Dict[str, typing.Any]],
        storage_profile_os_disk: typing.Union["VirtualMachineScaleSetStorageProfileOsDisk", typing.Dict[str, typing.Any]],
        upgrade_policy_mode: builtins.str,
        automatic_os_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        boot_diagnostics: typing.Optional[typing.Union["VirtualMachineScaleSetBootDiagnostics", typing.Dict[str, typing.Any]]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetExtension", typing.Dict[str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["VirtualMachineScaleSetIdentity", typing.Dict[str, typing.Any]]] = None,
        license_type: typing.Optional[builtins.str] = None,
        os_profile_linux_config: typing.Optional[typing.Union["VirtualMachineScaleSetOsProfileLinuxConfig", typing.Dict[str, typing.Any]]] = None,
        os_profile_secrets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileSecrets", typing.Dict[str, typing.Any]]]]] = None,
        os_profile_windows_config: typing.Optional[typing.Union["VirtualMachineScaleSetOsProfileWindowsConfig", typing.Dict[str, typing.Any]]] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plan: typing.Optional[typing.Union["VirtualMachineScaleSetPlan", typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        proximity_placement_group_id: typing.Optional[builtins.str] = None,
        rolling_upgrade_policy: typing.Optional[typing.Union["VirtualMachineScaleSetRollingUpgradePolicy", typing.Dict[str, typing.Any]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_profile_data_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetStorageProfileDataDisk", typing.Dict[str, typing.Any]]]]] = None,
        storage_profile_image_reference: typing.Optional[typing.Union["VirtualMachineScaleSetStorageProfileImageReference", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineScaleSetTimeouts", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set azurerm_virtual_machine_scale_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#location VirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param network_profile: network_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#network_profile VirtualMachineScaleSet#network_profile}
        :param os_profile: os_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile VirtualMachineScaleSet#os_profile}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#resource_group_name VirtualMachineScaleSet#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#sku VirtualMachineScaleSet#sku}
        :param storage_profile_os_disk: storage_profile_os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_os_disk VirtualMachineScaleSet#storage_profile_os_disk}
        :param upgrade_policy_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#upgrade_policy_mode VirtualMachineScaleSet#upgrade_policy_mode}.
        :param automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#automatic_os_upgrade VirtualMachineScaleSet#automatic_os_upgrade}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#boot_diagnostics VirtualMachineScaleSet#boot_diagnostics}
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#eviction_policy VirtualMachineScaleSet#eviction_policy}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#extension VirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#health_probe_id VirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#id VirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#identity VirtualMachineScaleSet#identity}
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#license_type VirtualMachineScaleSet#license_type}.
        :param os_profile_linux_config: os_profile_linux_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_linux_config VirtualMachineScaleSet#os_profile_linux_config}
        :param os_profile_secrets: os_profile_secrets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_secrets VirtualMachineScaleSet#os_profile_secrets}
        :param os_profile_windows_config: os_profile_windows_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_windows_config VirtualMachineScaleSet#os_profile_windows_config}
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#overprovision VirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#plan VirtualMachineScaleSet#plan}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#priority VirtualMachineScaleSet#priority}.
        :param proximity_placement_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#proximity_placement_group_id VirtualMachineScaleSet#proximity_placement_group_id}.
        :param rolling_upgrade_policy: rolling_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#rolling_upgrade_policy VirtualMachineScaleSet#rolling_upgrade_policy}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#single_placement_group VirtualMachineScaleSet#single_placement_group}.
        :param storage_profile_data_disk: storage_profile_data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_data_disk VirtualMachineScaleSet#storage_profile_data_disk}
        :param storage_profile_image_reference: storage_profile_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_image_reference VirtualMachineScaleSet#storage_profile_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#tags VirtualMachineScaleSet#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#timeouts VirtualMachineScaleSet#timeouts}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#zones VirtualMachineScaleSet#zones}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualMachineScaleSetConfig(
            location=location,
            name=name,
            network_profile=network_profile,
            os_profile=os_profile,
            resource_group_name=resource_group_name,
            sku=sku,
            storage_profile_os_disk=storage_profile_os_disk,
            upgrade_policy_mode=upgrade_policy_mode,
            automatic_os_upgrade=automatic_os_upgrade,
            boot_diagnostics=boot_diagnostics,
            eviction_policy=eviction_policy,
            extension=extension,
            health_probe_id=health_probe_id,
            id=id,
            identity=identity,
            license_type=license_type,
            os_profile_linux_config=os_profile_linux_config,
            os_profile_secrets=os_profile_secrets,
            os_profile_windows_config=os_profile_windows_config,
            overprovision=overprovision,
            plan=plan,
            priority=priority,
            proximity_placement_group_id=proximity_placement_group_id,
            rolling_upgrade_policy=rolling_upgrade_policy,
            single_placement_group=single_placement_group,
            storage_profile_data_disk=storage_profile_data_disk,
            storage_profile_image_reference=storage_profile_image_reference,
            tags=tags,
            timeouts=timeouts,
            zones=zones,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(
        self,
        *,
        storage_uri: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param storage_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_uri VirtualMachineScaleSet#storage_uri}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#enabled VirtualMachineScaleSet#enabled}.
        '''
        value = VirtualMachineScaleSetBootDiagnostics(
            storage_uri=storage_uri, enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putExtension")
    def put_extension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetExtension", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSet.put_extension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtension", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#type VirtualMachineScaleSet#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#identity_ids VirtualMachineScaleSet#identity_ids}.
        '''
        value = VirtualMachineScaleSetIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putNetworkProfile")
    def put_network_profile(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetNetworkProfile", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSet.put_network_profile)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkProfile", [value]))

    @jsii.member(jsii_name="putOsProfile")
    def put_os_profile(
        self,
        *,
        admin_username: builtins.str,
        computer_name_prefix: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#admin_username VirtualMachineScaleSet#admin_username}.
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#computer_name_prefix VirtualMachineScaleSet#computer_name_prefix}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#admin_password VirtualMachineScaleSet#admin_password}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#custom_data VirtualMachineScaleSet#custom_data}.
        '''
        value = VirtualMachineScaleSetOsProfile(
            admin_username=admin_username,
            computer_name_prefix=computer_name_prefix,
            admin_password=admin_password,
            custom_data=custom_data,
        )

        return typing.cast(None, jsii.invoke(self, "putOsProfile", [value]))

    @jsii.member(jsii_name="putOsProfileLinuxConfig")
    def put_os_profile_linux_config(
        self,
        *,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssh_keys: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileLinuxConfigSshKeys", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#disable_password_authentication VirtualMachineScaleSet#disable_password_authentication}.
        :param ssh_keys: ssh_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#ssh_keys VirtualMachineScaleSet#ssh_keys}
        '''
        value = VirtualMachineScaleSetOsProfileLinuxConfig(
            disable_password_authentication=disable_password_authentication,
            ssh_keys=ssh_keys,
        )

        return typing.cast(None, jsii.invoke(self, "putOsProfileLinuxConfig", [value]))

    @jsii.member(jsii_name="putOsProfileSecrets")
    def put_os_profile_secrets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileSecrets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSet.put_os_profile_secrets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOsProfileSecrets", [value]))

    @jsii.member(jsii_name="putOsProfileWindowsConfig")
    def put_os_profile_windows_config(
        self,
        *,
        additional_unattend_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig", typing.Dict[str, typing.Any]]]]] = None,
        enable_automatic_upgrades: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileWindowsConfigWinrm", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param additional_unattend_config: additional_unattend_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#additional_unattend_config VirtualMachineScaleSet#additional_unattend_config}
        :param enable_automatic_upgrades: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#enable_automatic_upgrades VirtualMachineScaleSet#enable_automatic_upgrades}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#provision_vm_agent VirtualMachineScaleSet#provision_vm_agent}.
        :param winrm: winrm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#winrm VirtualMachineScaleSet#winrm}
        '''
        value = VirtualMachineScaleSetOsProfileWindowsConfig(
            additional_unattend_config=additional_unattend_config,
            enable_automatic_upgrades=enable_automatic_upgrades,
            provision_vm_agent=provision_vm_agent,
            winrm=winrm,
        )

        return typing.cast(None, jsii.invoke(self, "putOsProfileWindowsConfig", [value]))

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#product VirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.
        '''
        value = VirtualMachineScaleSetPlan(
            name=name, product=product, publisher=publisher
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putRollingUpgradePolicy")
    def put_rolling_upgrade_policy(
        self,
        *,
        max_batch_instance_percent: typing.Optional[jsii.Number] = None,
        max_unhealthy_instance_percent: typing.Optional[jsii.Number] = None,
        max_unhealthy_upgraded_instance_percent: typing.Optional[jsii.Number] = None,
        pause_time_between_batches: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_batch_instance_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_batch_instance_percent VirtualMachineScaleSet#max_batch_instance_percent}.
        :param max_unhealthy_instance_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_unhealthy_instance_percent VirtualMachineScaleSet#max_unhealthy_instance_percent}.
        :param max_unhealthy_upgraded_instance_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_unhealthy_upgraded_instance_percent VirtualMachineScaleSet#max_unhealthy_upgraded_instance_percent}.
        :param pause_time_between_batches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#pause_time_between_batches VirtualMachineScaleSet#pause_time_between_batches}.
        '''
        value = VirtualMachineScaleSetRollingUpgradePolicy(
            max_batch_instance_percent=max_batch_instance_percent,
            max_unhealthy_instance_percent=max_unhealthy_instance_percent,
            max_unhealthy_upgraded_instance_percent=max_unhealthy_upgraded_instance_percent,
            pause_time_between_batches=pause_time_between_batches,
        )

        return typing.cast(None, jsii.invoke(self, "putRollingUpgradePolicy", [value]))

    @jsii.member(jsii_name="putSku")
    def put_sku(
        self,
        *,
        capacity: jsii.Number,
        name: builtins.str,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#capacity VirtualMachineScaleSet#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#tier VirtualMachineScaleSet#tier}.
        '''
        value = VirtualMachineScaleSetSku(capacity=capacity, name=name, tier=tier)

        return typing.cast(None, jsii.invoke(self, "putSku", [value]))

    @jsii.member(jsii_name="putStorageProfileDataDisk")
    def put_storage_profile_data_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetStorageProfileDataDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSet.put_storage_profile_data_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageProfileDataDisk", [value]))

    @jsii.member(jsii_name="putStorageProfileImageReference")
    def put_storage_profile_image_reference(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        offer: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#id VirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#offer VirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#sku VirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#version VirtualMachineScaleSet#version}.
        '''
        value = VirtualMachineScaleSetStorageProfileImageReference(
            id=id, offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putStorageProfileImageReference", [value]))

    @jsii.member(jsii_name="putStorageProfileOsDisk")
    def put_storage_profile_os_disk(
        self,
        *,
        create_option: builtins.str,
        caching: typing.Optional[builtins.str] = None,
        image: typing.Optional[builtins.str] = None,
        managed_disk_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        vhd_containers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create_option VirtualMachineScaleSet#create_option}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#caching VirtualMachineScaleSet#caching}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#image VirtualMachineScaleSet#image}.
        :param managed_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#managed_disk_type VirtualMachineScaleSet#managed_disk_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_type VirtualMachineScaleSet#os_type}.
        :param vhd_containers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#vhd_containers VirtualMachineScaleSet#vhd_containers}.
        '''
        value = VirtualMachineScaleSetStorageProfileOsDisk(
            create_option=create_option,
            caching=caching,
            image=image,
            managed_disk_type=managed_disk_type,
            name=name,
            os_type=os_type,
            vhd_containers=vhd_containers,
        )

        return typing.cast(None, jsii.invoke(self, "putStorageProfileOsDisk", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create VirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#delete VirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#read VirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#update VirtualMachineScaleSet#update}.
        '''
        value = VirtualMachineScaleSetTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAutomaticOsUpgrade")
    def reset_automatic_os_upgrade(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticOsUpgrade", []))

    @jsii.member(jsii_name="resetBootDiagnostics")
    def reset_boot_diagnostics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiagnostics", []))

    @jsii.member(jsii_name="resetEvictionPolicy")
    def reset_eviction_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvictionPolicy", []))

    @jsii.member(jsii_name="resetExtension")
    def reset_extension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtension", []))

    @jsii.member(jsii_name="resetHealthProbeId")
    def reset_health_probe_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthProbeId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetOsProfileLinuxConfig")
    def reset_os_profile_linux_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsProfileLinuxConfig", []))

    @jsii.member(jsii_name="resetOsProfileSecrets")
    def reset_os_profile_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsProfileSecrets", []))

    @jsii.member(jsii_name="resetOsProfileWindowsConfig")
    def reset_os_profile_windows_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsProfileWindowsConfig", []))

    @jsii.member(jsii_name="resetOverprovision")
    def reset_overprovision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverprovision", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProximityPlacementGroupId")
    def reset_proximity_placement_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProximityPlacementGroupId", []))

    @jsii.member(jsii_name="resetRollingUpgradePolicy")
    def reset_rolling_upgrade_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollingUpgradePolicy", []))

    @jsii.member(jsii_name="resetSinglePlacementGroup")
    def reset_single_placement_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSinglePlacementGroup", []))

    @jsii.member(jsii_name="resetStorageProfileDataDisk")
    def reset_storage_profile_data_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageProfileDataDisk", []))

    @jsii.member(jsii_name="resetStorageProfileImageReference")
    def reset_storage_profile_image_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageProfileImageReference", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetZones")
    def reset_zones(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZones", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(
        self,
    ) -> "VirtualMachineScaleSetBootDiagnosticsOutputReference":
        return typing.cast("VirtualMachineScaleSetBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(self) -> "VirtualMachineScaleSetExtensionList":
        return typing.cast("VirtualMachineScaleSetExtensionList", jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "VirtualMachineScaleSetIdentityOutputReference":
        return typing.cast("VirtualMachineScaleSetIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="networkProfile")
    def network_profile(self) -> "VirtualMachineScaleSetNetworkProfileList":
        return typing.cast("VirtualMachineScaleSetNetworkProfileList", jsii.get(self, "networkProfile"))

    @builtins.property
    @jsii.member(jsii_name="osProfile")
    def os_profile(self) -> "VirtualMachineScaleSetOsProfileOutputReference":
        return typing.cast("VirtualMachineScaleSetOsProfileOutputReference", jsii.get(self, "osProfile"))

    @builtins.property
    @jsii.member(jsii_name="osProfileLinuxConfig")
    def os_profile_linux_config(
        self,
    ) -> "VirtualMachineScaleSetOsProfileLinuxConfigOutputReference":
        return typing.cast("VirtualMachineScaleSetOsProfileLinuxConfigOutputReference", jsii.get(self, "osProfileLinuxConfig"))

    @builtins.property
    @jsii.member(jsii_name="osProfileSecrets")
    def os_profile_secrets(self) -> "VirtualMachineScaleSetOsProfileSecretsList":
        return typing.cast("VirtualMachineScaleSetOsProfileSecretsList", jsii.get(self, "osProfileSecrets"))

    @builtins.property
    @jsii.member(jsii_name="osProfileWindowsConfig")
    def os_profile_windows_config(
        self,
    ) -> "VirtualMachineScaleSetOsProfileWindowsConfigOutputReference":
        return typing.cast("VirtualMachineScaleSetOsProfileWindowsConfigOutputReference", jsii.get(self, "osProfileWindowsConfig"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "VirtualMachineScaleSetPlanOutputReference":
        return typing.cast("VirtualMachineScaleSetPlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="rollingUpgradePolicy")
    def rolling_upgrade_policy(
        self,
    ) -> "VirtualMachineScaleSetRollingUpgradePolicyOutputReference":
        return typing.cast("VirtualMachineScaleSetRollingUpgradePolicyOutputReference", jsii.get(self, "rollingUpgradePolicy"))

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> "VirtualMachineScaleSetSkuOutputReference":
        return typing.cast("VirtualMachineScaleSetSkuOutputReference", jsii.get(self, "sku"))

    @builtins.property
    @jsii.member(jsii_name="storageProfileDataDisk")
    def storage_profile_data_disk(
        self,
    ) -> "VirtualMachineScaleSetStorageProfileDataDiskList":
        return typing.cast("VirtualMachineScaleSetStorageProfileDataDiskList", jsii.get(self, "storageProfileDataDisk"))

    @builtins.property
    @jsii.member(jsii_name="storageProfileImageReference")
    def storage_profile_image_reference(
        self,
    ) -> "VirtualMachineScaleSetStorageProfileImageReferenceOutputReference":
        return typing.cast("VirtualMachineScaleSetStorageProfileImageReferenceOutputReference", jsii.get(self, "storageProfileImageReference"))

    @builtins.property
    @jsii.member(jsii_name="storageProfileOsDisk")
    def storage_profile_os_disk(
        self,
    ) -> "VirtualMachineScaleSetStorageProfileOsDiskOutputReference":
        return typing.cast("VirtualMachineScaleSetStorageProfileOsDiskOutputReference", jsii.get(self, "storageProfileOsDisk"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualMachineScaleSetTimeoutsOutputReference":
        return typing.cast("VirtualMachineScaleSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgradeInput")
    def automatic_os_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticOsUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnosticsInput")
    def boot_diagnostics_input(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetBootDiagnostics"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="evictionPolicyInput")
    def eviction_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evictionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionInput")
    def extension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetExtension"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetExtension"]]], jsii.get(self, "extensionInput"))

    @builtins.property
    @jsii.member(jsii_name="healthProbeIdInput")
    def health_probe_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthProbeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["VirtualMachineScaleSetIdentity"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseTypeInput")
    def license_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkProfileInput")
    def network_profile_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetNetworkProfile"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetNetworkProfile"]]], jsii.get(self, "networkProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileInput")
    def os_profile_input(self) -> typing.Optional["VirtualMachineScaleSetOsProfile"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetOsProfile"], jsii.get(self, "osProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileLinuxConfigInput")
    def os_profile_linux_config_input(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetOsProfileLinuxConfig"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetOsProfileLinuxConfig"], jsii.get(self, "osProfileLinuxConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileSecretsInput")
    def os_profile_secrets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecrets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecrets"]]], jsii.get(self, "osProfileSecretsInput"))

    @builtins.property
    @jsii.member(jsii_name="osProfileWindowsConfigInput")
    def os_profile_windows_config_input(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetOsProfileWindowsConfig"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetOsProfileWindowsConfig"], jsii.get(self, "osProfileWindowsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="overprovisionInput")
    def overprovision_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overprovisionInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["VirtualMachineScaleSetPlan"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetPlan"], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="proximityPlacementGroupIdInput")
    def proximity_placement_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proximityPlacementGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="rollingUpgradePolicyInput")
    def rolling_upgrade_policy_input(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetRollingUpgradePolicy"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetRollingUpgradePolicy"], jsii.get(self, "rollingUpgradePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="singlePlacementGroupInput")
    def single_placement_group_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "singlePlacementGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional["VirtualMachineScaleSetSku"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetSku"], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="storageProfileDataDiskInput")
    def storage_profile_data_disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetStorageProfileDataDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetStorageProfileDataDisk"]]], jsii.get(self, "storageProfileDataDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="storageProfileImageReferenceInput")
    def storage_profile_image_reference_input(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetStorageProfileImageReference"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetStorageProfileImageReference"], jsii.get(self, "storageProfileImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageProfileOsDiskInput")
    def storage_profile_os_disk_input(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetStorageProfileOsDisk"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetStorageProfileOsDisk"], jsii.get(self, "storageProfileOsDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualMachineScaleSetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualMachineScaleSetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradePolicyModeInput")
    def upgrade_policy_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradePolicyModeInput"))

    @builtins.property
    @jsii.member(jsii_name="zonesInput")
    def zones_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "zonesInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgrade")
    def automatic_os_upgrade(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticOsUpgrade"))

    @automatic_os_upgrade.setter
    def automatic_os_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "automatic_os_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticOsUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="evictionPolicy")
    def eviction_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evictionPolicy"))

    @eviction_policy.setter
    def eviction_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "eviction_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evictionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="healthProbeId")
    def health_probe_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthProbeId"))

    @health_probe_id.setter
    def health_probe_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "health_probe_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthProbeId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "license_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="overprovision")
    def overprovision(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "overprovision"))

    @overprovision.setter
    def overprovision(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "overprovision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overprovision", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="proximityPlacementGroupId")
    def proximity_placement_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proximityPlacementGroupId"))

    @proximity_placement_group_id.setter
    def proximity_placement_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "proximity_placement_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proximityPlacementGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="singlePlacementGroup")
    def single_placement_group(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "singlePlacementGroup"))

    @single_placement_group.setter
    def single_placement_group(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "single_placement_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singlePlacementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="upgradePolicyMode")
    def upgrade_policy_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradePolicyMode"))

    @upgrade_policy_mode.setter
    def upgrade_policy_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "upgrade_policy_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradePolicyMode", value)

    @builtins.property
    @jsii.member(jsii_name="zones")
    def zones(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "zones"))

    @zones.setter
    def zones(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSet, "zones").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zones", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"storage_uri": "storageUri", "enabled": "enabled"},
)
class VirtualMachineScaleSetBootDiagnostics:
    def __init__(
        self,
        *,
        storage_uri: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param storage_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_uri VirtualMachineScaleSet#storage_uri}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#enabled VirtualMachineScaleSet#enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetBootDiagnostics.__init__)
            check_type(argname="argument storage_uri", value=storage_uri, expected_type=type_hints["storage_uri"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_uri": storage_uri,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def storage_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_uri VirtualMachineScaleSet#storage_uri}.'''
        result = self._values.get("storage_uri")
        assert result is not None, "Required property 'storage_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#enabled VirtualMachineScaleSet#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetBootDiagnosticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetBootDiagnosticsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="storageUriInput")
    def storage_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageUriInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetBootDiagnosticsOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="storageUri")
    def storage_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageUri"))

    @storage_uri.setter
    def storage_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetBootDiagnosticsOutputReference, "storage_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineScaleSetBootDiagnostics]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetBootDiagnosticsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "network_profile": "networkProfile",
        "os_profile": "osProfile",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "storage_profile_os_disk": "storageProfileOsDisk",
        "upgrade_policy_mode": "upgradePolicyMode",
        "automatic_os_upgrade": "automaticOsUpgrade",
        "boot_diagnostics": "bootDiagnostics",
        "eviction_policy": "evictionPolicy",
        "extension": "extension",
        "health_probe_id": "healthProbeId",
        "id": "id",
        "identity": "identity",
        "license_type": "licenseType",
        "os_profile_linux_config": "osProfileLinuxConfig",
        "os_profile_secrets": "osProfileSecrets",
        "os_profile_windows_config": "osProfileWindowsConfig",
        "overprovision": "overprovision",
        "plan": "plan",
        "priority": "priority",
        "proximity_placement_group_id": "proximityPlacementGroupId",
        "rolling_upgrade_policy": "rollingUpgradePolicy",
        "single_placement_group": "singlePlacementGroup",
        "storage_profile_data_disk": "storageProfileDataDisk",
        "storage_profile_image_reference": "storageProfileImageReference",
        "tags": "tags",
        "timeouts": "timeouts",
        "zones": "zones",
    },
)
class VirtualMachineScaleSetConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        network_profile: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetNetworkProfile", typing.Dict[str, typing.Any]]]],
        os_profile: typing.Union["VirtualMachineScaleSetOsProfile", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        sku: typing.Union["VirtualMachineScaleSetSku", typing.Dict[str, typing.Any]],
        storage_profile_os_disk: typing.Union["VirtualMachineScaleSetStorageProfileOsDisk", typing.Dict[str, typing.Any]],
        upgrade_policy_mode: builtins.str,
        automatic_os_upgrade: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        boot_diagnostics: typing.Optional[typing.Union[VirtualMachineScaleSetBootDiagnostics, typing.Dict[str, typing.Any]]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetExtension", typing.Dict[str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["VirtualMachineScaleSetIdentity", typing.Dict[str, typing.Any]]] = None,
        license_type: typing.Optional[builtins.str] = None,
        os_profile_linux_config: typing.Optional[typing.Union["VirtualMachineScaleSetOsProfileLinuxConfig", typing.Dict[str, typing.Any]]] = None,
        os_profile_secrets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileSecrets", typing.Dict[str, typing.Any]]]]] = None,
        os_profile_windows_config: typing.Optional[typing.Union["VirtualMachineScaleSetOsProfileWindowsConfig", typing.Dict[str, typing.Any]]] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plan: typing.Optional[typing.Union["VirtualMachineScaleSetPlan", typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        proximity_placement_group_id: typing.Optional[builtins.str] = None,
        rolling_upgrade_policy: typing.Optional[typing.Union["VirtualMachineScaleSetRollingUpgradePolicy", typing.Dict[str, typing.Any]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        storage_profile_data_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetStorageProfileDataDisk", typing.Dict[str, typing.Any]]]]] = None,
        storage_profile_image_reference: typing.Optional[typing.Union["VirtualMachineScaleSetStorageProfileImageReference", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualMachineScaleSetTimeouts", typing.Dict[str, typing.Any]]] = None,
        zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#location VirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param network_profile: network_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#network_profile VirtualMachineScaleSet#network_profile}
        :param os_profile: os_profile block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile VirtualMachineScaleSet#os_profile}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#resource_group_name VirtualMachineScaleSet#resource_group_name}.
        :param sku: sku block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#sku VirtualMachineScaleSet#sku}
        :param storage_profile_os_disk: storage_profile_os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_os_disk VirtualMachineScaleSet#storage_profile_os_disk}
        :param upgrade_policy_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#upgrade_policy_mode VirtualMachineScaleSet#upgrade_policy_mode}.
        :param automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#automatic_os_upgrade VirtualMachineScaleSet#automatic_os_upgrade}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#boot_diagnostics VirtualMachineScaleSet#boot_diagnostics}
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#eviction_policy VirtualMachineScaleSet#eviction_policy}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#extension VirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#health_probe_id VirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#id VirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#identity VirtualMachineScaleSet#identity}
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#license_type VirtualMachineScaleSet#license_type}.
        :param os_profile_linux_config: os_profile_linux_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_linux_config VirtualMachineScaleSet#os_profile_linux_config}
        :param os_profile_secrets: os_profile_secrets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_secrets VirtualMachineScaleSet#os_profile_secrets}
        :param os_profile_windows_config: os_profile_windows_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_windows_config VirtualMachineScaleSet#os_profile_windows_config}
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#overprovision VirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#plan VirtualMachineScaleSet#plan}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#priority VirtualMachineScaleSet#priority}.
        :param proximity_placement_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#proximity_placement_group_id VirtualMachineScaleSet#proximity_placement_group_id}.
        :param rolling_upgrade_policy: rolling_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#rolling_upgrade_policy VirtualMachineScaleSet#rolling_upgrade_policy}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#single_placement_group VirtualMachineScaleSet#single_placement_group}.
        :param storage_profile_data_disk: storage_profile_data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_data_disk VirtualMachineScaleSet#storage_profile_data_disk}
        :param storage_profile_image_reference: storage_profile_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_image_reference VirtualMachineScaleSet#storage_profile_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#tags VirtualMachineScaleSet#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#timeouts VirtualMachineScaleSet#timeouts}
        :param zones: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#zones VirtualMachineScaleSet#zones}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_profile, dict):
            os_profile = VirtualMachineScaleSetOsProfile(**os_profile)
        if isinstance(sku, dict):
            sku = VirtualMachineScaleSetSku(**sku)
        if isinstance(storage_profile_os_disk, dict):
            storage_profile_os_disk = VirtualMachineScaleSetStorageProfileOsDisk(**storage_profile_os_disk)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = VirtualMachineScaleSetBootDiagnostics(**boot_diagnostics)
        if isinstance(identity, dict):
            identity = VirtualMachineScaleSetIdentity(**identity)
        if isinstance(os_profile_linux_config, dict):
            os_profile_linux_config = VirtualMachineScaleSetOsProfileLinuxConfig(**os_profile_linux_config)
        if isinstance(os_profile_windows_config, dict):
            os_profile_windows_config = VirtualMachineScaleSetOsProfileWindowsConfig(**os_profile_windows_config)
        if isinstance(plan, dict):
            plan = VirtualMachineScaleSetPlan(**plan)
        if isinstance(rolling_upgrade_policy, dict):
            rolling_upgrade_policy = VirtualMachineScaleSetRollingUpgradePolicy(**rolling_upgrade_policy)
        if isinstance(storage_profile_image_reference, dict):
            storage_profile_image_reference = VirtualMachineScaleSetStorageProfileImageReference(**storage_profile_image_reference)
        if isinstance(timeouts, dict):
            timeouts = VirtualMachineScaleSetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_profile", value=network_profile, expected_type=type_hints["network_profile"])
            check_type(argname="argument os_profile", value=os_profile, expected_type=type_hints["os_profile"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument storage_profile_os_disk", value=storage_profile_os_disk, expected_type=type_hints["storage_profile_os_disk"])
            check_type(argname="argument upgrade_policy_mode", value=upgrade_policy_mode, expected_type=type_hints["upgrade_policy_mode"])
            check_type(argname="argument automatic_os_upgrade", value=automatic_os_upgrade, expected_type=type_hints["automatic_os_upgrade"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument eviction_policy", value=eviction_policy, expected_type=type_hints["eviction_policy"])
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument health_probe_id", value=health_probe_id, expected_type=type_hints["health_probe_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument os_profile_linux_config", value=os_profile_linux_config, expected_type=type_hints["os_profile_linux_config"])
            check_type(argname="argument os_profile_secrets", value=os_profile_secrets, expected_type=type_hints["os_profile_secrets"])
            check_type(argname="argument os_profile_windows_config", value=os_profile_windows_config, expected_type=type_hints["os_profile_windows_config"])
            check_type(argname="argument overprovision", value=overprovision, expected_type=type_hints["overprovision"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument proximity_placement_group_id", value=proximity_placement_group_id, expected_type=type_hints["proximity_placement_group_id"])
            check_type(argname="argument rolling_upgrade_policy", value=rolling_upgrade_policy, expected_type=type_hints["rolling_upgrade_policy"])
            check_type(argname="argument single_placement_group", value=single_placement_group, expected_type=type_hints["single_placement_group"])
            check_type(argname="argument storage_profile_data_disk", value=storage_profile_data_disk, expected_type=type_hints["storage_profile_data_disk"])
            check_type(argname="argument storage_profile_image_reference", value=storage_profile_image_reference, expected_type=type_hints["storage_profile_image_reference"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument zones", value=zones, expected_type=type_hints["zones"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "network_profile": network_profile,
            "os_profile": os_profile,
            "resource_group_name": resource_group_name,
            "sku": sku,
            "storage_profile_os_disk": storage_profile_os_disk,
            "upgrade_policy_mode": upgrade_policy_mode,
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
        if automatic_os_upgrade is not None:
            self._values["automatic_os_upgrade"] = automatic_os_upgrade
        if boot_diagnostics is not None:
            self._values["boot_diagnostics"] = boot_diagnostics
        if eviction_policy is not None:
            self._values["eviction_policy"] = eviction_policy
        if extension is not None:
            self._values["extension"] = extension
        if health_probe_id is not None:
            self._values["health_probe_id"] = health_probe_id
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if license_type is not None:
            self._values["license_type"] = license_type
        if os_profile_linux_config is not None:
            self._values["os_profile_linux_config"] = os_profile_linux_config
        if os_profile_secrets is not None:
            self._values["os_profile_secrets"] = os_profile_secrets
        if os_profile_windows_config is not None:
            self._values["os_profile_windows_config"] = os_profile_windows_config
        if overprovision is not None:
            self._values["overprovision"] = overprovision
        if plan is not None:
            self._values["plan"] = plan
        if priority is not None:
            self._values["priority"] = priority
        if proximity_placement_group_id is not None:
            self._values["proximity_placement_group_id"] = proximity_placement_group_id
        if rolling_upgrade_policy is not None:
            self._values["rolling_upgrade_policy"] = rolling_upgrade_policy
        if single_placement_group is not None:
            self._values["single_placement_group"] = single_placement_group
        if storage_profile_data_disk is not None:
            self._values["storage_profile_data_disk"] = storage_profile_data_disk
        if storage_profile_image_reference is not None:
            self._values["storage_profile_image_reference"] = storage_profile_image_reference
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if zones is not None:
            self._values["zones"] = zones

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#location VirtualMachineScaleSet#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_profile(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetNetworkProfile"]]:
        '''network_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#network_profile VirtualMachineScaleSet#network_profile}
        '''
        result = self._values.get("network_profile")
        assert result is not None, "Required property 'network_profile' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetNetworkProfile"]], result)

    @builtins.property
    def os_profile(self) -> "VirtualMachineScaleSetOsProfile":
        '''os_profile block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile VirtualMachineScaleSet#os_profile}
        '''
        result = self._values.get("os_profile")
        assert result is not None, "Required property 'os_profile' is missing"
        return typing.cast("VirtualMachineScaleSetOsProfile", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#resource_group_name VirtualMachineScaleSet#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> "VirtualMachineScaleSetSku":
        '''sku block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#sku VirtualMachineScaleSet#sku}
        '''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast("VirtualMachineScaleSetSku", result)

    @builtins.property
    def storage_profile_os_disk(self) -> "VirtualMachineScaleSetStorageProfileOsDisk":
        '''storage_profile_os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_os_disk VirtualMachineScaleSet#storage_profile_os_disk}
        '''
        result = self._values.get("storage_profile_os_disk")
        assert result is not None, "Required property 'storage_profile_os_disk' is missing"
        return typing.cast("VirtualMachineScaleSetStorageProfileOsDisk", result)

    @builtins.property
    def upgrade_policy_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#upgrade_policy_mode VirtualMachineScaleSet#upgrade_policy_mode}.'''
        result = self._values.get("upgrade_policy_mode")
        assert result is not None, "Required property 'upgrade_policy_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic_os_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#automatic_os_upgrade VirtualMachineScaleSet#automatic_os_upgrade}.'''
        result = self._values.get("automatic_os_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def boot_diagnostics(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#boot_diagnostics VirtualMachineScaleSet#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[VirtualMachineScaleSetBootDiagnostics], result)

    @builtins.property
    def eviction_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#eviction_policy VirtualMachineScaleSet#eviction_policy}.'''
        result = self._values.get("eviction_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extension(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetExtension"]]]:
        '''extension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#extension VirtualMachineScaleSet#extension}
        '''
        result = self._values.get("extension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetExtension"]]], result)

    @builtins.property
    def health_probe_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#health_probe_id VirtualMachineScaleSet#health_probe_id}.'''
        result = self._values.get("health_probe_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#id VirtualMachineScaleSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["VirtualMachineScaleSetIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#identity VirtualMachineScaleSet#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["VirtualMachineScaleSetIdentity"], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#license_type VirtualMachineScaleSet#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_profile_linux_config(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetOsProfileLinuxConfig"]:
        '''os_profile_linux_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_linux_config VirtualMachineScaleSet#os_profile_linux_config}
        '''
        result = self._values.get("os_profile_linux_config")
        return typing.cast(typing.Optional["VirtualMachineScaleSetOsProfileLinuxConfig"], result)

    @builtins.property
    def os_profile_secrets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecrets"]]]:
        '''os_profile_secrets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_secrets VirtualMachineScaleSet#os_profile_secrets}
        '''
        result = self._values.get("os_profile_secrets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecrets"]]], result)

    @builtins.property
    def os_profile_windows_config(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetOsProfileWindowsConfig"]:
        '''os_profile_windows_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_profile_windows_config VirtualMachineScaleSet#os_profile_windows_config}
        '''
        result = self._values.get("os_profile_windows_config")
        return typing.cast(typing.Optional["VirtualMachineScaleSetOsProfileWindowsConfig"], result)

    @builtins.property
    def overprovision(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#overprovision VirtualMachineScaleSet#overprovision}.'''
        result = self._values.get("overprovision")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def plan(self) -> typing.Optional["VirtualMachineScaleSetPlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#plan VirtualMachineScaleSet#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["VirtualMachineScaleSetPlan"], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#priority VirtualMachineScaleSet#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proximity_placement_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#proximity_placement_group_id VirtualMachineScaleSet#proximity_placement_group_id}.'''
        result = self._values.get("proximity_placement_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rolling_upgrade_policy(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetRollingUpgradePolicy"]:
        '''rolling_upgrade_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#rolling_upgrade_policy VirtualMachineScaleSet#rolling_upgrade_policy}
        '''
        result = self._values.get("rolling_upgrade_policy")
        return typing.cast(typing.Optional["VirtualMachineScaleSetRollingUpgradePolicy"], result)

    @builtins.property
    def single_placement_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#single_placement_group VirtualMachineScaleSet#single_placement_group}.'''
        result = self._values.get("single_placement_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def storage_profile_data_disk(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetStorageProfileDataDisk"]]]:
        '''storage_profile_data_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_data_disk VirtualMachineScaleSet#storage_profile_data_disk}
        '''
        result = self._values.get("storage_profile_data_disk")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetStorageProfileDataDisk"]]], result)

    @builtins.property
    def storage_profile_image_reference(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetStorageProfileImageReference"]:
        '''storage_profile_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#storage_profile_image_reference VirtualMachineScaleSet#storage_profile_image_reference}
        '''
        result = self._values.get("storage_profile_image_reference")
        return typing.cast(typing.Optional["VirtualMachineScaleSetStorageProfileImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#tags VirtualMachineScaleSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualMachineScaleSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#timeouts VirtualMachineScaleSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualMachineScaleSetTimeouts"], result)

    @builtins.property
    def zones(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#zones VirtualMachineScaleSet#zones}.'''
        result = self._values.get("zones")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetExtension",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "publisher": "publisher",
        "type": "type",
        "type_handler_version": "typeHandlerVersion",
        "auto_upgrade_minor_version": "autoUpgradeMinorVersion",
        "protected_settings": "protectedSettings",
        "provision_after_extensions": "provisionAfterExtensions",
        "settings": "settings",
    },
)
class VirtualMachineScaleSetExtension:
    def __init__(
        self,
        *,
        name: builtins.str,
        publisher: builtins.str,
        type: builtins.str,
        type_handler_version: builtins.str,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        provision_after_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        settings: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#type VirtualMachineScaleSet#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#type_handler_version VirtualMachineScaleSet#type_handler_version}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#auto_upgrade_minor_version VirtualMachineScaleSet#auto_upgrade_minor_version}.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#protected_settings VirtualMachineScaleSet#protected_settings}.
        :param provision_after_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#provision_after_extensions VirtualMachineScaleSet#provision_after_extensions}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#settings VirtualMachineScaleSet#settings}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetExtension.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument type_handler_version", value=type_handler_version, expected_type=type_hints["type_handler_version"])
            check_type(argname="argument auto_upgrade_minor_version", value=auto_upgrade_minor_version, expected_type=type_hints["auto_upgrade_minor_version"])
            check_type(argname="argument protected_settings", value=protected_settings, expected_type=type_hints["protected_settings"])
            check_type(argname="argument provision_after_extensions", value=provision_after_extensions, expected_type=type_hints["provision_after_extensions"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "publisher": publisher,
            "type": type,
            "type_handler_version": type_handler_version,
        }
        if auto_upgrade_minor_version is not None:
            self._values["auto_upgrade_minor_version"] = auto_upgrade_minor_version
        if protected_settings is not None:
            self._values["protected_settings"] = protected_settings
        if provision_after_extensions is not None:
            self._values["provision_after_extensions"] = provision_after_extensions
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#type VirtualMachineScaleSet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_handler_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#type_handler_version VirtualMachineScaleSet#type_handler_version}.'''
        result = self._values.get("type_handler_version")
        assert result is not None, "Required property 'type_handler_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#auto_upgrade_minor_version VirtualMachineScaleSet#auto_upgrade_minor_version}.'''
        result = self._values.get("auto_upgrade_minor_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def protected_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#protected_settings VirtualMachineScaleSet#protected_settings}.'''
        result = self._values.get("protected_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_after_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#provision_after_extensions VirtualMachineScaleSet#provision_after_extensions}.'''
        result = self._values.get("provision_after_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#settings VirtualMachineScaleSet#settings}.'''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetExtension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetExtensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetExtensionList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetExtensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetExtensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetExtensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetExtensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetExtension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetExtension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetExtension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetExtensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetExtensionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetExtensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAutoUpgradeMinorVersion")
    def reset_auto_upgrade_minor_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgradeMinorVersion", []))

    @jsii.member(jsii_name="resetProtectedSettings")
    def reset_protected_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectedSettings", []))

    @jsii.member(jsii_name="resetProvisionAfterExtensions")
    def reset_provision_after_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionAfterExtensions", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersionInput")
    def auto_upgrade_minor_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoUpgradeMinorVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedSettingsInput")
    def protected_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectedSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensionsInput")
    def provision_after_extensions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "provisionAfterExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersionInput")
    def type_handler_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeHandlerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoUpgradeMinorVersion"))

    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "auto_upgrade_minor_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgradeMinorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protectedSettings")
    def protected_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedSettings"))

    @protected_settings.setter
    def protected_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "protected_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedSettings", value)

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensions")
    def provision_after_extensions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "provisionAfterExtensions"))

    @provision_after_extensions.setter
    def provision_after_extensions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "provision_after_extensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionAfterExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersion")
    def type_handler_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeHandlerVersion"))

    @type_handler_version.setter
    def type_handler_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "type_handler_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeHandlerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetExtension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetExtension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetExtension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetExtensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class VirtualMachineScaleSetIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#type VirtualMachineScaleSet#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#identity_ids VirtualMachineScaleSet#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#type VirtualMachineScaleSet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#identity_ids VirtualMachineScaleSet#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetIdentityOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdentityIds")
    def reset_identity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityIds", []))

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineScaleSetIdentity]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfile",
    jsii_struct_bases=[],
    name_mapping={
        "ip_configuration": "ipConfiguration",
        "name": "name",
        "primary": "primary",
        "accelerated_networking": "acceleratedNetworking",
        "dns_settings": "dnsSettings",
        "ip_forwarding": "ipForwarding",
        "network_security_group_id": "networkSecurityGroupId",
    },
)
class VirtualMachineScaleSetNetworkProfile:
    def __init__(
        self,
        *,
        ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetNetworkProfileIpConfiguration", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        primary: typing.Union[builtins.bool, cdktf.IResolvable],
        accelerated_networking: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dns_settings: typing.Optional[typing.Union["VirtualMachineScaleSetNetworkProfileDnsSettings", typing.Dict[str, typing.Any]]] = None,
        ip_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_security_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#ip_configuration VirtualMachineScaleSet#ip_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#primary VirtualMachineScaleSet#primary}.
        :param accelerated_networking: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#accelerated_networking VirtualMachineScaleSet#accelerated_networking}.
        :param dns_settings: dns_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#dns_settings VirtualMachineScaleSet#dns_settings}
        :param ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#ip_forwarding VirtualMachineScaleSet#ip_forwarding}.
        :param network_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#network_security_group_id VirtualMachineScaleSet#network_security_group_id}.
        '''
        if isinstance(dns_settings, dict):
            dns_settings = VirtualMachineScaleSetNetworkProfileDnsSettings(**dns_settings)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfile.__init__)
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument accelerated_networking", value=accelerated_networking, expected_type=type_hints["accelerated_networking"])
            check_type(argname="argument dns_settings", value=dns_settings, expected_type=type_hints["dns_settings"])
            check_type(argname="argument ip_forwarding", value=ip_forwarding, expected_type=type_hints["ip_forwarding"])
            check_type(argname="argument network_security_group_id", value=network_security_group_id, expected_type=type_hints["network_security_group_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_configuration": ip_configuration,
            "name": name,
            "primary": primary,
        }
        if accelerated_networking is not None:
            self._values["accelerated_networking"] = accelerated_networking
        if dns_settings is not None:
            self._values["dns_settings"] = dns_settings
        if ip_forwarding is not None:
            self._values["ip_forwarding"] = ip_forwarding
        if network_security_group_id is not None:
            self._values["network_security_group_id"] = network_security_group_id

    @builtins.property
    def ip_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetNetworkProfileIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#ip_configuration VirtualMachineScaleSet#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetNetworkProfileIpConfiguration"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#primary VirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        assert result is not None, "Required property 'primary' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def accelerated_networking(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#accelerated_networking VirtualMachineScaleSet#accelerated_networking}.'''
        result = self._values.get("accelerated_networking")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dns_settings(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetNetworkProfileDnsSettings"]:
        '''dns_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#dns_settings VirtualMachineScaleSet#dns_settings}
        '''
        result = self._values.get("dns_settings")
        return typing.cast(typing.Optional["VirtualMachineScaleSetNetworkProfileDnsSettings"], result)

    @builtins.property
    def ip_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#ip_forwarding VirtualMachineScaleSet#ip_forwarding}.'''
        result = self._values.get("ip_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def network_security_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#network_security_group_id VirtualMachineScaleSet#network_security_group_id}.'''
        result = self._values.get("network_security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetNetworkProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileDnsSettings",
    jsii_struct_bases=[],
    name_mapping={"dns_servers": "dnsServers"},
)
class VirtualMachineScaleSetNetworkProfileDnsSettings:
    def __init__(self, *, dns_servers: typing.Sequence[builtins.str]) -> None:
        '''
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#dns_servers VirtualMachineScaleSet#dns_servers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileDnsSettings.__init__)
            check_type(argname="argument dns_servers", value=dns_servers, expected_type=type_hints["dns_servers"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns_servers": dns_servers,
        }

    @builtins.property
    def dns_servers(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#dns_servers VirtualMachineScaleSet#dns_servers}.'''
        result = self._values.get("dns_servers")
        assert result is not None, "Required property 'dns_servers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetNetworkProfileDnsSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dnsServersInput")
    def dns_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsServersInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsServers"))

    @dns_servers.setter
    def dns_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference, "dns_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetNetworkProfileDnsSettings]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetNetworkProfileDnsSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetNetworkProfileDnsSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "primary": "primary",
        "subnet_id": "subnetId",
        "application_gateway_backend_address_pool_ids": "applicationGatewayBackendAddressPoolIds",
        "application_security_group_ids": "applicationSecurityGroupIds",
        "load_balancer_backend_address_pool_ids": "loadBalancerBackendAddressPoolIds",
        "load_balancer_inbound_nat_rules_ids": "loadBalancerInboundNatRulesIds",
        "public_ip_address_configuration": "publicIpAddressConfiguration",
    },
)
class VirtualMachineScaleSetNetworkProfileIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        primary: typing.Union[builtins.bool, cdktf.IResolvable],
        subnet_id: builtins.str,
        application_gateway_backend_address_pool_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        application_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        load_balancer_backend_address_pool_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        load_balancer_inbound_nat_rules_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        public_ip_address_configuration: typing.Optional[typing.Union["VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#primary VirtualMachineScaleSet#primary}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#subnet_id VirtualMachineScaleSet#subnet_id}.
        :param application_gateway_backend_address_pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#application_gateway_backend_address_pool_ids VirtualMachineScaleSet#application_gateway_backend_address_pool_ids}.
        :param application_security_group_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#application_security_group_ids VirtualMachineScaleSet#application_security_group_ids}.
        :param load_balancer_backend_address_pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#load_balancer_backend_address_pool_ids VirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.
        :param load_balancer_inbound_nat_rules_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids VirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.
        :param public_ip_address_configuration: public_ip_address_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#public_ip_address_configuration VirtualMachineScaleSet#public_ip_address_configuration}
        '''
        if isinstance(public_ip_address_configuration, dict):
            public_ip_address_configuration = VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration(**public_ip_address_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument application_gateway_backend_address_pool_ids", value=application_gateway_backend_address_pool_ids, expected_type=type_hints["application_gateway_backend_address_pool_ids"])
            check_type(argname="argument application_security_group_ids", value=application_security_group_ids, expected_type=type_hints["application_security_group_ids"])
            check_type(argname="argument load_balancer_backend_address_pool_ids", value=load_balancer_backend_address_pool_ids, expected_type=type_hints["load_balancer_backend_address_pool_ids"])
            check_type(argname="argument load_balancer_inbound_nat_rules_ids", value=load_balancer_inbound_nat_rules_ids, expected_type=type_hints["load_balancer_inbound_nat_rules_ids"])
            check_type(argname="argument public_ip_address_configuration", value=public_ip_address_configuration, expected_type=type_hints["public_ip_address_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "primary": primary,
            "subnet_id": subnet_id,
        }
        if application_gateway_backend_address_pool_ids is not None:
            self._values["application_gateway_backend_address_pool_ids"] = application_gateway_backend_address_pool_ids
        if application_security_group_ids is not None:
            self._values["application_security_group_ids"] = application_security_group_ids
        if load_balancer_backend_address_pool_ids is not None:
            self._values["load_balancer_backend_address_pool_ids"] = load_balancer_backend_address_pool_ids
        if load_balancer_inbound_nat_rules_ids is not None:
            self._values["load_balancer_inbound_nat_rules_ids"] = load_balancer_inbound_nat_rules_ids
        if public_ip_address_configuration is not None:
            self._values["public_ip_address_configuration"] = public_ip_address_configuration

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#primary VirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        assert result is not None, "Required property 'primary' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#subnet_id VirtualMachineScaleSet#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_gateway_backend_address_pool_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#application_gateway_backend_address_pool_ids VirtualMachineScaleSet#application_gateway_backend_address_pool_ids}.'''
        result = self._values.get("application_gateway_backend_address_pool_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def application_security_group_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#application_security_group_ids VirtualMachineScaleSet#application_security_group_ids}.'''
        result = self._values.get("application_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def load_balancer_backend_address_pool_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#load_balancer_backend_address_pool_ids VirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.'''
        result = self._values.get("load_balancer_backend_address_pool_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def load_balancer_inbound_nat_rules_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids VirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.'''
        result = self._values.get("load_balancer_inbound_nat_rules_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def public_ip_address_configuration(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration"]:
        '''public_ip_address_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#public_ip_address_configuration VirtualMachineScaleSet#public_ip_address_configuration}
        '''
        result = self._values.get("public_ip_address_configuration")
        return typing.cast(typing.Optional["VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetNetworkProfileIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetNetworkProfileIpConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileIpConfigurationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileIpConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileIpConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfileIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfileIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfileIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPublicIpAddressConfiguration")
    def put_public_ip_address_configuration(
        self,
        *,
        domain_name_label: builtins.str,
        idle_timeout: jsii.Number,
        name: builtins.str,
    ) -> None:
        '''
        :param domain_name_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#domain_name_label VirtualMachineScaleSet#domain_name_label}.
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#idle_timeout VirtualMachineScaleSet#idle_timeout}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        '''
        value = VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration(
            domain_name_label=domain_name_label, idle_timeout=idle_timeout, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putPublicIpAddressConfiguration", [value]))

    @jsii.member(jsii_name="resetApplicationGatewayBackendAddressPoolIds")
    def reset_application_gateway_backend_address_pool_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationGatewayBackendAddressPoolIds", []))

    @jsii.member(jsii_name="resetApplicationSecurityGroupIds")
    def reset_application_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationSecurityGroupIds", []))

    @jsii.member(jsii_name="resetLoadBalancerBackendAddressPoolIds")
    def reset_load_balancer_backend_address_pool_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerBackendAddressPoolIds", []))

    @jsii.member(jsii_name="resetLoadBalancerInboundNatRulesIds")
    def reset_load_balancer_inbound_nat_rules_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerInboundNatRulesIds", []))

    @jsii.member(jsii_name="resetPublicIpAddressConfiguration")
    def reset_public_ip_address_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIpAddressConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressConfiguration")
    def public_ip_address_configuration(
        self,
    ) -> "VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference":
        return typing.cast("VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference", jsii.get(self, "publicIpAddressConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="applicationGatewayBackendAddressPoolIdsInput")
    def application_gateway_backend_address_pool_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "applicationGatewayBackendAddressPoolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationSecurityGroupIdsInput")
    def application_security_group_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "applicationSecurityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerBackendAddressPoolIdsInput")
    def load_balancer_backend_address_pool_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerBackendAddressPoolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInboundNatRulesIdsInput")
    def load_balancer_inbound_nat_rules_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerInboundNatRulesIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressConfigurationInput")
    def public_ip_address_configuration_input(
        self,
    ) -> typing.Optional["VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration"]:
        return typing.cast(typing.Optional["VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration"], jsii.get(self, "publicIpAddressConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationGatewayBackendAddressPoolIds")
    def application_gateway_backend_address_pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "applicationGatewayBackendAddressPoolIds"))

    @application_gateway_backend_address_pool_ids.setter
    def application_gateway_backend_address_pool_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "application_gateway_backend_address_pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationGatewayBackendAddressPoolIds", value)

    @builtins.property
    @jsii.member(jsii_name="applicationSecurityGroupIds")
    def application_security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "applicationSecurityGroupIds"))

    @application_security_group_ids.setter
    def application_security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "application_security_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationSecurityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerBackendAddressPoolIds")
    def load_balancer_backend_address_pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerBackendAddressPoolIds"))

    @load_balancer_backend_address_pool_ids.setter
    def load_balancer_backend_address_pool_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "load_balancer_backend_address_pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerBackendAddressPoolIds", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInboundNatRulesIds")
    def load_balancer_inbound_nat_rules_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerInboundNatRulesIds"))

    @load_balancer_inbound_nat_rules_ids.setter
    def load_balancer_inbound_nat_rules_ids(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "load_balancer_inbound_nat_rules_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerInboundNatRulesIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetNetworkProfileIpConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetNetworkProfileIpConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetNetworkProfileIpConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name_label": "domainNameLabel",
        "idle_timeout": "idleTimeout",
        "name": "name",
    },
)
class VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration:
    def __init__(
        self,
        *,
        domain_name_label: builtins.str,
        idle_timeout: jsii.Number,
        name: builtins.str,
    ) -> None:
        '''
        :param domain_name_label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#domain_name_label VirtualMachineScaleSet#domain_name_label}.
        :param idle_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#idle_timeout VirtualMachineScaleSet#idle_timeout}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration.__init__)
            check_type(argname="argument domain_name_label", value=domain_name_label, expected_type=type_hints["domain_name_label"])
            check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name_label": domain_name_label,
            "idle_timeout": idle_timeout,
            "name": name,
        }

    @builtins.property
    def domain_name_label(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#domain_name_label VirtualMachineScaleSet#domain_name_label}.'''
        result = self._values.get("domain_name_label")
        assert result is not None, "Required property 'domain_name_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def idle_timeout(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#idle_timeout VirtualMachineScaleSet#idle_timeout}.'''
        result = self._values.get("idle_timeout")
        assert result is not None, "Required property 'idle_timeout' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="domainNameLabelInput")
    def domain_name_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInput")
    def idle_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameLabel")
    def domain_name_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainNameLabel"))

    @domain_name_label.setter
    def domain_name_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference, "domain_name_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainNameLabel", value)

    @builtins.property
    @jsii.member(jsii_name="idleTimeout")
    def idle_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeout"))

    @idle_timeout.setter
    def idle_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference, "idle_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetNetworkProfileList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetNetworkProfileOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetNetworkProfileOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfile]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfile]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfile]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetNetworkProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetNetworkProfileOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDnsSettings")
    def put_dns_settings(self, *, dns_servers: typing.Sequence[builtins.str]) -> None:
        '''
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#dns_servers VirtualMachineScaleSet#dns_servers}.
        '''
        value = VirtualMachineScaleSetNetworkProfileDnsSettings(
            dns_servers=dns_servers
        )

        return typing.cast(None, jsii.invoke(self, "putDnsSettings", [value]))

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VirtualMachineScaleSetNetworkProfileIpConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetNetworkProfileOutputReference.put_ip_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

    @jsii.member(jsii_name="resetAcceleratedNetworking")
    def reset_accelerated_networking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAcceleratedNetworking", []))

    @jsii.member(jsii_name="resetDnsSettings")
    def reset_dns_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsSettings", []))

    @jsii.member(jsii_name="resetIpForwarding")
    def reset_ip_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpForwarding", []))

    @jsii.member(jsii_name="resetNetworkSecurityGroupId")
    def reset_network_security_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkSecurityGroupId", []))

    @builtins.property
    @jsii.member(jsii_name="dnsSettings")
    def dns_settings(
        self,
    ) -> VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference:
        return typing.cast(VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference, jsii.get(self, "dnsSettings"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(
        self,
    ) -> VirtualMachineScaleSetNetworkProfileIpConfigurationList:
        return typing.cast(VirtualMachineScaleSetNetworkProfileIpConfigurationList, jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="acceleratedNetworkingInput")
    def accelerated_networking_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "acceleratedNetworkingInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsSettingsInput")
    def dns_settings_input(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetNetworkProfileDnsSettings]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetNetworkProfileDnsSettings], jsii.get(self, "dnsSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfileIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetNetworkProfileIpConfiguration]]], jsii.get(self, "ipConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="ipForwardingInput")
    def ip_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ipForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupIdInput")
    def network_security_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkSecurityGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="acceleratedNetworking")
    def accelerated_networking(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "acceleratedNetworking"))

    @accelerated_networking.setter
    def accelerated_networking(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileOutputReference, "accelerated_networking").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceleratedNetworking", value)

    @builtins.property
    @jsii.member(jsii_name="ipForwarding")
    def ip_forwarding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ipForwarding"))

    @ip_forwarding.setter
    def ip_forwarding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileOutputReference, "ip_forwarding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupId")
    def network_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkSecurityGroupId"))

    @network_security_group_id.setter
    def network_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileOutputReference, "network_security_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetNetworkProfile, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetNetworkProfile, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetNetworkProfile, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetNetworkProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfile",
    jsii_struct_bases=[],
    name_mapping={
        "admin_username": "adminUsername",
        "computer_name_prefix": "computerNamePrefix",
        "admin_password": "adminPassword",
        "custom_data": "customData",
    },
)
class VirtualMachineScaleSetOsProfile:
    def __init__(
        self,
        *,
        admin_username: builtins.str,
        computer_name_prefix: builtins.str,
        admin_password: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#admin_username VirtualMachineScaleSet#admin_username}.
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#computer_name_prefix VirtualMachineScaleSet#computer_name_prefix}.
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#admin_password VirtualMachineScaleSet#admin_password}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#custom_data VirtualMachineScaleSet#custom_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfile.__init__)
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument computer_name_prefix", value=computer_name_prefix, expected_type=type_hints["computer_name_prefix"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "admin_username": admin_username,
            "computer_name_prefix": computer_name_prefix,
        }
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if custom_data is not None:
            self._values["custom_data"] = custom_data

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#admin_username VirtualMachineScaleSet#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def computer_name_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#computer_name_prefix VirtualMachineScaleSet#computer_name_prefix}.'''
        result = self._values.get("computer_name_prefix")
        assert result is not None, "Required property 'computer_name_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#admin_password VirtualMachineScaleSet#admin_password}.'''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#custom_data VirtualMachineScaleSet#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileLinuxConfig",
    jsii_struct_bases=[],
    name_mapping={
        "disable_password_authentication": "disablePasswordAuthentication",
        "ssh_keys": "sshKeys",
    },
)
class VirtualMachineScaleSetOsProfileLinuxConfig:
    def __init__(
        self,
        *,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssh_keys: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileLinuxConfigSshKeys", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#disable_password_authentication VirtualMachineScaleSet#disable_password_authentication}.
        :param ssh_keys: ssh_keys block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#ssh_keys VirtualMachineScaleSet#ssh_keys}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileLinuxConfig.__init__)
            check_type(argname="argument disable_password_authentication", value=disable_password_authentication, expected_type=type_hints["disable_password_authentication"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disable_password_authentication is not None:
            self._values["disable_password_authentication"] = disable_password_authentication
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys

    @builtins.property
    def disable_password_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#disable_password_authentication VirtualMachineScaleSet#disable_password_authentication}.'''
        result = self._values.get("disable_password_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssh_keys(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileLinuxConfigSshKeys"]]]:
        '''ssh_keys block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#ssh_keys VirtualMachineScaleSet#ssh_keys}
        '''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileLinuxConfigSshKeys"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfileLinuxConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetOsProfileLinuxConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileLinuxConfigOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileLinuxConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSshKeys")
    def put_ssh_keys(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileLinuxConfigSshKeys", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileLinuxConfigOutputReference.put_ssh_keys)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSshKeys", [value]))

    @jsii.member(jsii_name="resetDisablePasswordAuthentication")
    def reset_disable_password_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablePasswordAuthentication", []))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> "VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList":
        return typing.cast("VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList", jsii.get(self, "sshKeys"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordAuthenticationInput")
    def disable_password_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disablePasswordAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileLinuxConfigSshKeys"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileLinuxConfigSshKeys"]]], jsii.get(self, "sshKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordAuthentication")
    def disable_password_authentication(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disablePasswordAuthentication"))

    @disable_password_authentication.setter
    def disable_password_authentication(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigOutputReference, "disable_password_authentication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablePasswordAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetOsProfileLinuxConfig]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetOsProfileLinuxConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetOsProfileLinuxConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileLinuxConfigSshKeys",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "key_data": "keyData"},
)
class VirtualMachineScaleSetOsProfileLinuxConfigSshKeys:
    def __init__(
        self,
        *,
        path: builtins.str,
        key_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#path VirtualMachineScaleSet#path}.
        :param key_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#key_data VirtualMachineScaleSet#key_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileLinuxConfigSshKeys.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument key_data", value=key_data, expected_type=type_hints["key_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
        }
        if key_data is not None:
            self._values["key_data"] = key_data

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#path VirtualMachineScaleSet#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#key_data VirtualMachineScaleSet#key_data}.'''
        result = self._values.get("key_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfileLinuxConfigSshKeys(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileLinuxConfigSshKeys]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileLinuxConfigSshKeys]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileLinuxConfigSshKeys]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKeyData")
    def reset_key_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyData", []))

    @builtins.property
    @jsii.member(jsii_name="keyDataInput")
    def key_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyDataInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="keyData")
    def key_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyData"))

    @key_data.setter
    def key_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference, "key_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyData", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileLinuxConfigSshKeys, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileLinuxConfigSshKeys, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileLinuxConfigSshKeys, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetOsProfileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="computerNamePrefixInput")
    def computer_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computerNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileOutputReference, "admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileOutputReference, "admin_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="computerNamePrefix")
    def computer_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerNamePrefix"))

    @computer_name_prefix.setter
    def computer_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileOutputReference, "computer_name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileOutputReference, "custom_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineScaleSetOsProfile]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetOsProfile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetOsProfile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileSecrets",
    jsii_struct_bases=[],
    name_mapping={
        "source_vault_id": "sourceVaultId",
        "vault_certificates": "vaultCertificates",
    },
)
class VirtualMachineScaleSetOsProfileSecrets:
    def __init__(
        self,
        *,
        source_vault_id: builtins.str,
        vault_certificates: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileSecretsVaultCertificates", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param source_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#source_vault_id VirtualMachineScaleSet#source_vault_id}.
        :param vault_certificates: vault_certificates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#vault_certificates VirtualMachineScaleSet#vault_certificates}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecrets.__init__)
            check_type(argname="argument source_vault_id", value=source_vault_id, expected_type=type_hints["source_vault_id"])
            check_type(argname="argument vault_certificates", value=vault_certificates, expected_type=type_hints["vault_certificates"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_vault_id": source_vault_id,
        }
        if vault_certificates is not None:
            self._values["vault_certificates"] = vault_certificates

    @builtins.property
    def source_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#source_vault_id VirtualMachineScaleSet#source_vault_id}.'''
        result = self._values.get("source_vault_id")
        assert result is not None, "Required property 'source_vault_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vault_certificates(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecretsVaultCertificates"]]]:
        '''vault_certificates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#vault_certificates VirtualMachineScaleSet#vault_certificates}
        '''
        result = self._values.get("vault_certificates")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecretsVaultCertificates"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfileSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetOsProfileSecretsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileSecretsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetOsProfileSecretsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetOsProfileSecretsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileSecrets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileSecrets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileSecrets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetOsProfileSecretsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileSecretsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVaultCertificates")
    def put_vault_certificates(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileSecretsVaultCertificates", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsOutputReference.put_vault_certificates)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVaultCertificates", [value]))

    @jsii.member(jsii_name="resetVaultCertificates")
    def reset_vault_certificates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVaultCertificates", []))

    @builtins.property
    @jsii.member(jsii_name="vaultCertificates")
    def vault_certificates(
        self,
    ) -> "VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList":
        return typing.cast("VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList", jsii.get(self, "vaultCertificates"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultIdInput")
    def source_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultCertificatesInput")
    def vault_certificates_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecretsVaultCertificates"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileSecretsVaultCertificates"]]], jsii.get(self, "vaultCertificatesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVaultId")
    def source_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVaultId"))

    @source_vault_id.setter
    def source_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsOutputReference, "source_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileSecrets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileSecrets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileSecrets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileSecretsVaultCertificates",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_url": "certificateUrl",
        "certificate_store": "certificateStore",
    },
)
class VirtualMachineScaleSetOsProfileSecretsVaultCertificates:
    def __init__(
        self,
        *,
        certificate_url: builtins.str,
        certificate_store: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param certificate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#certificate_url VirtualMachineScaleSet#certificate_url}.
        :param certificate_store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#certificate_store VirtualMachineScaleSet#certificate_store}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsVaultCertificates.__init__)
            check_type(argname="argument certificate_url", value=certificate_url, expected_type=type_hints["certificate_url"])
            check_type(argname="argument certificate_store", value=certificate_store, expected_type=type_hints["certificate_store"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate_url": certificate_url,
        }
        if certificate_store is not None:
            self._values["certificate_store"] = certificate_store

    @builtins.property
    def certificate_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#certificate_url VirtualMachineScaleSet#certificate_url}.'''
        result = self._values.get("certificate_url")
        assert result is not None, "Required property 'certificate_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_store(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#certificate_store VirtualMachineScaleSet#certificate_store}.'''
        result = self._values.get("certificate_store")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfileSecretsVaultCertificates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileSecretsVaultCertificates]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileSecretsVaultCertificates]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileSecretsVaultCertificates]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificateStore")
    def reset_certificate_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateStore", []))

    @builtins.property
    @jsii.member(jsii_name="certificateStoreInput")
    def certificate_store_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateUrlInput")
    def certificate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateStore")
    def certificate_store(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateStore"))

    @certificate_store.setter
    def certificate_store(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference, "certificate_store").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateStore", value)

    @builtins.property
    @jsii.member(jsii_name="certificateUrl")
    def certificate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateUrl"))

    @certificate_url.setter
    def certificate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference, "certificate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileSecretsVaultCertificates, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileSecretsVaultCertificates, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileSecretsVaultCertificates, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "additional_unattend_config": "additionalUnattendConfig",
        "enable_automatic_upgrades": "enableAutomaticUpgrades",
        "provision_vm_agent": "provisionVmAgent",
        "winrm": "winrm",
    },
)
class VirtualMachineScaleSetOsProfileWindowsConfig:
    def __init__(
        self,
        *,
        additional_unattend_config: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig", typing.Dict[str, typing.Any]]]]] = None,
        enable_automatic_upgrades: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileWindowsConfigWinrm", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param additional_unattend_config: additional_unattend_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#additional_unattend_config VirtualMachineScaleSet#additional_unattend_config}
        :param enable_automatic_upgrades: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#enable_automatic_upgrades VirtualMachineScaleSet#enable_automatic_upgrades}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#provision_vm_agent VirtualMachineScaleSet#provision_vm_agent}.
        :param winrm: winrm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#winrm VirtualMachineScaleSet#winrm}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfig.__init__)
            check_type(argname="argument additional_unattend_config", value=additional_unattend_config, expected_type=type_hints["additional_unattend_config"])
            check_type(argname="argument enable_automatic_upgrades", value=enable_automatic_upgrades, expected_type=type_hints["enable_automatic_upgrades"])
            check_type(argname="argument provision_vm_agent", value=provision_vm_agent, expected_type=type_hints["provision_vm_agent"])
            check_type(argname="argument winrm", value=winrm, expected_type=type_hints["winrm"])
        self._values: typing.Dict[str, typing.Any] = {}
        if additional_unattend_config is not None:
            self._values["additional_unattend_config"] = additional_unattend_config
        if enable_automatic_upgrades is not None:
            self._values["enable_automatic_upgrades"] = enable_automatic_upgrades
        if provision_vm_agent is not None:
            self._values["provision_vm_agent"] = provision_vm_agent
        if winrm is not None:
            self._values["winrm"] = winrm

    @builtins.property
    def additional_unattend_config(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig"]]]:
        '''additional_unattend_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#additional_unattend_config VirtualMachineScaleSet#additional_unattend_config}
        '''
        result = self._values.get("additional_unattend_config")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig"]]], result)

    @builtins.property
    def enable_automatic_upgrades(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#enable_automatic_upgrades VirtualMachineScaleSet#enable_automatic_upgrades}.'''
        result = self._values.get("enable_automatic_upgrades")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#provision_vm_agent VirtualMachineScaleSet#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def winrm(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileWindowsConfigWinrm"]]]:
        '''winrm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#winrm VirtualMachineScaleSet#winrm}
        '''
        result = self._values.get("winrm")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileWindowsConfigWinrm"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfileWindowsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig",
    jsii_struct_bases=[],
    name_mapping={
        "component": "component",
        "content": "content",
        "pass_": "pass",
        "setting_name": "settingName",
    },
)
class VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig:
    def __init__(
        self,
        *,
        component: builtins.str,
        content: builtins.str,
        pass_: builtins.str,
        setting_name: builtins.str,
    ) -> None:
        '''
        :param component: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#component VirtualMachineScaleSet#component}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#content VirtualMachineScaleSet#content}.
        :param pass_: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#pass VirtualMachineScaleSet#pass}.
        :param setting_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#setting_name VirtualMachineScaleSet#setting_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig.__init__)
            check_type(argname="argument component", value=component, expected_type=type_hints["component"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument pass_", value=pass_, expected_type=type_hints["pass_"])
            check_type(argname="argument setting_name", value=setting_name, expected_type=type_hints["setting_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "component": component,
            "content": content,
            "pass_": pass_,
            "setting_name": setting_name,
        }

    @builtins.property
    def component(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#component VirtualMachineScaleSet#component}.'''
        result = self._values.get("component")
        assert result is not None, "Required property 'component' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#content VirtualMachineScaleSet#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pass_(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#pass VirtualMachineScaleSet#pass}.'''
        result = self._values.get("pass_")
        assert result is not None, "Required property 'pass_' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def setting_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#setting_name VirtualMachineScaleSet#setting_name}.'''
        result = self._values.get("setting_name")
        assert result is not None, "Required property 'setting_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="componentInput")
    def component_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "componentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="passInput")
    def pass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passInput"))

    @builtins.property
    @jsii.member(jsii_name="settingNameInput")
    def setting_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "component"))

    @component.setter
    def component(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference, "component").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "component", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="pass")
    def pass_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pass"))

    @pass_.setter
    def pass_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference, "pass_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pass", value)

    @builtins.property
    @jsii.member(jsii_name="settingName")
    def setting_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settingName"))

    @setting_name.setter
    def setting_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference, "setting_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetOsProfileWindowsConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfigOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAdditionalUnattendConfig")
    def put_additional_unattend_config(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigOutputReference.put_additional_unattend_config)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalUnattendConfig", [value]))

    @jsii.member(jsii_name="putWinrm")
    def put_winrm(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualMachineScaleSetOsProfileWindowsConfigWinrm", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigOutputReference.put_winrm)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWinrm", [value]))

    @jsii.member(jsii_name="resetAdditionalUnattendConfig")
    def reset_additional_unattend_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalUnattendConfig", []))

    @jsii.member(jsii_name="resetEnableAutomaticUpgrades")
    def reset_enable_automatic_upgrades(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticUpgrades", []))

    @jsii.member(jsii_name="resetProvisionVmAgent")
    def reset_provision_vm_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionVmAgent", []))

    @jsii.member(jsii_name="resetWinrm")
    def reset_winrm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrm", []))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendConfig")
    def additional_unattend_config(
        self,
    ) -> VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList:
        return typing.cast(VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList, jsii.get(self, "additionalUnattendConfig"))

    @builtins.property
    @jsii.member(jsii_name="winrm")
    def winrm(self) -> "VirtualMachineScaleSetOsProfileWindowsConfigWinrmList":
        return typing.cast("VirtualMachineScaleSetOsProfileWindowsConfigWinrmList", jsii.get(self, "winrm"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendConfigInput")
    def additional_unattend_config_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig]]], jsii.get(self, "additionalUnattendConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpgradesInput")
    def enable_automatic_upgrades_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutomaticUpgradesInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionVmAgentInput")
    def provision_vm_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "provisionVmAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmInput")
    def winrm_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileWindowsConfigWinrm"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualMachineScaleSetOsProfileWindowsConfigWinrm"]]], jsii.get(self, "winrmInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpgrades")
    def enable_automatic_upgrades(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutomaticUpgrades"))

    @enable_automatic_upgrades.setter
    def enable_automatic_upgrades(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigOutputReference, "enable_automatic_upgrades").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticUpgrades", value)

    @builtins.property
    @jsii.member(jsii_name="provisionVmAgent")
    def provision_vm_agent(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "provisionVmAgent"))

    @provision_vm_agent.setter
    def provision_vm_agent(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigOutputReference, "provision_vm_agent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetOsProfileWindowsConfig]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetOsProfileWindowsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetOsProfileWindowsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfigWinrm",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol", "certificate_url": "certificateUrl"},
)
class VirtualMachineScaleSetOsProfileWindowsConfigWinrm:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        certificate_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#protocol VirtualMachineScaleSet#protocol}.
        :param certificate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#certificate_url VirtualMachineScaleSet#certificate_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigWinrm.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument certificate_url", value=certificate_url, expected_type=type_hints["certificate_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
        }
        if certificate_url is not None:
            self._values["certificate_url"] = certificate_url

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#protocol VirtualMachineScaleSet#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#certificate_url VirtualMachineScaleSet#certificate_url}.'''
        result = self._values.get("certificate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetOsProfileWindowsConfigWinrm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetOsProfileWindowsConfigWinrmList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfigWinrmList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigWinrmList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigWinrmList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigWinrmList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigWinrmList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigWinrmList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigWinrm]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigWinrm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetOsProfileWindowsConfigWinrm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigWinrmList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificateUrl")
    def reset_certificate_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateUrl", []))

    @builtins.property
    @jsii.member(jsii_name="certificateUrlInput")
    def certificate_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateUrl")
    def certificate_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateUrl"))

    @certificate_url.setter
    def certificate_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference, "certificate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileWindowsConfigWinrm, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileWindowsConfigWinrm, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetOsProfileWindowsConfigWinrm, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetPlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class VirtualMachineScaleSetPlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#product VirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetPlan.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "product": product,
            "publisher": publisher,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#product VirtualMachineScaleSet#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetPlanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetPlanOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetPlanOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productInput")
    def product_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "productInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetPlanOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetPlanOutputReference, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetPlanOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineScaleSetPlan]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetPlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetPlan],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetPlanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetRollingUpgradePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "max_batch_instance_percent": "maxBatchInstancePercent",
        "max_unhealthy_instance_percent": "maxUnhealthyInstancePercent",
        "max_unhealthy_upgraded_instance_percent": "maxUnhealthyUpgradedInstancePercent",
        "pause_time_between_batches": "pauseTimeBetweenBatches",
    },
)
class VirtualMachineScaleSetRollingUpgradePolicy:
    def __init__(
        self,
        *,
        max_batch_instance_percent: typing.Optional[jsii.Number] = None,
        max_unhealthy_instance_percent: typing.Optional[jsii.Number] = None,
        max_unhealthy_upgraded_instance_percent: typing.Optional[jsii.Number] = None,
        pause_time_between_batches: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_batch_instance_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_batch_instance_percent VirtualMachineScaleSet#max_batch_instance_percent}.
        :param max_unhealthy_instance_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_unhealthy_instance_percent VirtualMachineScaleSet#max_unhealthy_instance_percent}.
        :param max_unhealthy_upgraded_instance_percent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_unhealthy_upgraded_instance_percent VirtualMachineScaleSet#max_unhealthy_upgraded_instance_percent}.
        :param pause_time_between_batches: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#pause_time_between_batches VirtualMachineScaleSet#pause_time_between_batches}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetRollingUpgradePolicy.__init__)
            check_type(argname="argument max_batch_instance_percent", value=max_batch_instance_percent, expected_type=type_hints["max_batch_instance_percent"])
            check_type(argname="argument max_unhealthy_instance_percent", value=max_unhealthy_instance_percent, expected_type=type_hints["max_unhealthy_instance_percent"])
            check_type(argname="argument max_unhealthy_upgraded_instance_percent", value=max_unhealthy_upgraded_instance_percent, expected_type=type_hints["max_unhealthy_upgraded_instance_percent"])
            check_type(argname="argument pause_time_between_batches", value=pause_time_between_batches, expected_type=type_hints["pause_time_between_batches"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_batch_instance_percent is not None:
            self._values["max_batch_instance_percent"] = max_batch_instance_percent
        if max_unhealthy_instance_percent is not None:
            self._values["max_unhealthy_instance_percent"] = max_unhealthy_instance_percent
        if max_unhealthy_upgraded_instance_percent is not None:
            self._values["max_unhealthy_upgraded_instance_percent"] = max_unhealthy_upgraded_instance_percent
        if pause_time_between_batches is not None:
            self._values["pause_time_between_batches"] = pause_time_between_batches

    @builtins.property
    def max_batch_instance_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_batch_instance_percent VirtualMachineScaleSet#max_batch_instance_percent}.'''
        result = self._values.get("max_batch_instance_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unhealthy_instance_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_unhealthy_instance_percent VirtualMachineScaleSet#max_unhealthy_instance_percent}.'''
        result = self._values.get("max_unhealthy_instance_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unhealthy_upgraded_instance_percent(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#max_unhealthy_upgraded_instance_percent VirtualMachineScaleSet#max_unhealthy_upgraded_instance_percent}.'''
        result = self._values.get("max_unhealthy_upgraded_instance_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pause_time_between_batches(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#pause_time_between_batches VirtualMachineScaleSet#pause_time_between_batches}.'''
        result = self._values.get("pause_time_between_batches")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetRollingUpgradePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetRollingUpgradePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetRollingUpgradePolicyOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetRollingUpgradePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxBatchInstancePercent")
    def reset_max_batch_instance_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBatchInstancePercent", []))

    @jsii.member(jsii_name="resetMaxUnhealthyInstancePercent")
    def reset_max_unhealthy_instance_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnhealthyInstancePercent", []))

    @jsii.member(jsii_name="resetMaxUnhealthyUpgradedInstancePercent")
    def reset_max_unhealthy_upgraded_instance_percent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnhealthyUpgradedInstancePercent", []))

    @jsii.member(jsii_name="resetPauseTimeBetweenBatches")
    def reset_pause_time_between_batches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPauseTimeBetweenBatches", []))

    @builtins.property
    @jsii.member(jsii_name="maxBatchInstancePercentInput")
    def max_batch_instance_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchInstancePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyInstancePercentInput")
    def max_unhealthy_instance_percent_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnhealthyInstancePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyUpgradedInstancePercentInput")
    def max_unhealthy_upgraded_instance_percent_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnhealthyUpgradedInstancePercentInput"))

    @builtins.property
    @jsii.member(jsii_name="pauseTimeBetweenBatchesInput")
    def pause_time_between_batches_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pauseTimeBetweenBatchesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBatchInstancePercent")
    def max_batch_instance_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBatchInstancePercent"))

    @max_batch_instance_percent.setter
    def max_batch_instance_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetRollingUpgradePolicyOutputReference, "max_batch_instance_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchInstancePercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyInstancePercent")
    def max_unhealthy_instance_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnhealthyInstancePercent"))

    @max_unhealthy_instance_percent.setter
    def max_unhealthy_instance_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetRollingUpgradePolicyOutputReference, "max_unhealthy_instance_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnhealthyInstancePercent", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnhealthyUpgradedInstancePercent")
    def max_unhealthy_upgraded_instance_percent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnhealthyUpgradedInstancePercent"))

    @max_unhealthy_upgraded_instance_percent.setter
    def max_unhealthy_upgraded_instance_percent(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetRollingUpgradePolicyOutputReference, "max_unhealthy_upgraded_instance_percent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnhealthyUpgradedInstancePercent", value)

    @builtins.property
    @jsii.member(jsii_name="pauseTimeBetweenBatches")
    def pause_time_between_batches(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pauseTimeBetweenBatches"))

    @pause_time_between_batches.setter
    def pause_time_between_batches(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetRollingUpgradePolicyOutputReference, "pause_time_between_batches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pauseTimeBetweenBatches", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetRollingUpgradePolicy]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetRollingUpgradePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetRollingUpgradePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetRollingUpgradePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetSku",
    jsii_struct_bases=[],
    name_mapping={"capacity": "capacity", "name": "name", "tier": "tier"},
)
class VirtualMachineScaleSetSku:
    def __init__(
        self,
        *,
        capacity: jsii.Number,
        name: builtins.str,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param capacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#capacity VirtualMachineScaleSet#capacity}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param tier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#tier VirtualMachineScaleSet#tier}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetSku.__init__)
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
        self._values: typing.Dict[str, typing.Any] = {
            "capacity": capacity,
            "name": name,
        }
        if tier is not None:
            self._values["tier"] = tier

    @builtins.property
    def capacity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#capacity VirtualMachineScaleSet#capacity}.'''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#tier VirtualMachineScaleSet#tier}.'''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetSku(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetSkuOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetSkuOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetSkuOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTier")
    def reset_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTier", []))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetSkuOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetSkuOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetSkuOutputReference, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualMachineScaleSetSku]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetSku], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VirtualMachineScaleSetSku]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetSkuOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetStorageProfileDataDisk",
    jsii_struct_bases=[],
    name_mapping={
        "create_option": "createOption",
        "lun": "lun",
        "caching": "caching",
        "disk_size_gb": "diskSizeGb",
        "managed_disk_type": "managedDiskType",
    },
)
class VirtualMachineScaleSetStorageProfileDataDisk:
    def __init__(
        self,
        *,
        create_option: builtins.str,
        lun: jsii.Number,
        caching: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        managed_disk_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create_option VirtualMachineScaleSet#create_option}.
        :param lun: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#lun VirtualMachineScaleSet#lun}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#caching VirtualMachineScaleSet#caching}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#disk_size_gb VirtualMachineScaleSet#disk_size_gb}.
        :param managed_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#managed_disk_type VirtualMachineScaleSet#managed_disk_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileDataDisk.__init__)
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument managed_disk_type", value=managed_disk_type, expected_type=type_hints["managed_disk_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "create_option": create_option,
            "lun": lun,
        }
        if caching is not None:
            self._values["caching"] = caching
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if managed_disk_type is not None:
            self._values["managed_disk_type"] = managed_disk_type

    @builtins.property
    def create_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create_option VirtualMachineScaleSet#create_option}.'''
        result = self._values.get("create_option")
        assert result is not None, "Required property 'create_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lun(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#lun VirtualMachineScaleSet#lun}.'''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def caching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#caching VirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#disk_size_gb VirtualMachineScaleSet#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def managed_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#managed_disk_type VirtualMachineScaleSet#managed_disk_type}.'''
        result = self._values.get("managed_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetStorageProfileDataDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetStorageProfileDataDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetStorageProfileDataDiskList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileDataDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualMachineScaleSetStorageProfileDataDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileDataDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualMachineScaleSetStorageProfileDataDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetStorageProfileDataDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetStorageProfileDataDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualMachineScaleSetStorageProfileDataDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualMachineScaleSetStorageProfileDataDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetStorageProfileDataDiskOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileDataDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCaching")
    def reset_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaching", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetManagedDiskType")
    def reset_managed_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskType", []))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="createOptionInput")
    def create_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskTypeInput")
    def managed_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskOutputReference, "caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskOutputReference, "create_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskOutputReference, "lun").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskType")
    def managed_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskType"))

    @managed_disk_type.setter
    def managed_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskOutputReference, "managed_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetStorageProfileDataDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetStorageProfileDataDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetStorageProfileDataDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileDataDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetStorageProfileImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class VirtualMachineScaleSetStorageProfileImageReference:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        offer: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#id VirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#offer VirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#sku VirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#version VirtualMachineScaleSet#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileImageReference.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if offer is not None:
            self._values["offer"] = offer
        if publisher is not None:
            self._values["publisher"] = publisher
        if sku is not None:
            self._values["sku"] = sku
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#id VirtualMachineScaleSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#offer VirtualMachineScaleSet#offer}.'''
        result = self._values.get("offer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#publisher VirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#sku VirtualMachineScaleSet#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#version VirtualMachineScaleSet#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetStorageProfileImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetStorageProfileImageReferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetStorageProfileImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileImageReferenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOffer")
    def reset_offer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffer", []))

    @jsii.member(jsii_name="resetPublisher")
    def reset_publisher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublisher", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="offerInput")
    def offer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offerInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileImageReferenceOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileImageReferenceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileImageReferenceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileImageReferenceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileImageReferenceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetStorageProfileImageReference]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetStorageProfileImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetStorageProfileImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileImageReferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetStorageProfileOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "create_option": "createOption",
        "caching": "caching",
        "image": "image",
        "managed_disk_type": "managedDiskType",
        "name": "name",
        "os_type": "osType",
        "vhd_containers": "vhdContainers",
    },
)
class VirtualMachineScaleSetStorageProfileOsDisk:
    def __init__(
        self,
        *,
        create_option: builtins.str,
        caching: typing.Optional[builtins.str] = None,
        image: typing.Optional[builtins.str] = None,
        managed_disk_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        os_type: typing.Optional[builtins.str] = None,
        vhd_containers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create_option VirtualMachineScaleSet#create_option}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#caching VirtualMachineScaleSet#caching}.
        :param image: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#image VirtualMachineScaleSet#image}.
        :param managed_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#managed_disk_type VirtualMachineScaleSet#managed_disk_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.
        :param os_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_type VirtualMachineScaleSet#os_type}.
        :param vhd_containers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#vhd_containers VirtualMachineScaleSet#vhd_containers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileOsDisk.__init__)
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument managed_disk_type", value=managed_disk_type, expected_type=type_hints["managed_disk_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument os_type", value=os_type, expected_type=type_hints["os_type"])
            check_type(argname="argument vhd_containers", value=vhd_containers, expected_type=type_hints["vhd_containers"])
        self._values: typing.Dict[str, typing.Any] = {
            "create_option": create_option,
        }
        if caching is not None:
            self._values["caching"] = caching
        if image is not None:
            self._values["image"] = image
        if managed_disk_type is not None:
            self._values["managed_disk_type"] = managed_disk_type
        if name is not None:
            self._values["name"] = name
        if os_type is not None:
            self._values["os_type"] = os_type
        if vhd_containers is not None:
            self._values["vhd_containers"] = vhd_containers

    @builtins.property
    def create_option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create_option VirtualMachineScaleSet#create_option}.'''
        result = self._values.get("create_option")
        assert result is not None, "Required property 'create_option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#caching VirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#image VirtualMachineScaleSet#image}.'''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#managed_disk_type VirtualMachineScaleSet#managed_disk_type}.'''
        result = self._values.get("managed_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#name VirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#os_type VirtualMachineScaleSet#os_type}.'''
        result = self._values.get("os_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vhd_containers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#vhd_containers VirtualMachineScaleSet#vhd_containers}.'''
        result = self._values.get("vhd_containers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetStorageProfileOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetStorageProfileOsDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetStorageProfileOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetStorageProfileOsDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaching")
    def reset_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaching", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetManagedDiskType")
    def reset_managed_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDiskType", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOsType")
    def reset_os_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsType", []))

    @jsii.member(jsii_name="resetVhdContainers")
    def reset_vhd_containers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVhdContainers", []))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="createOptionInput")
    def create_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskTypeInput")
    def managed_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managedDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypeInput")
    def os_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="vhdContainersInput")
    def vhd_containers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vhdContainersInput"))

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "create_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "image"))

    @image.setter
    def image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "image", value)

    @builtins.property
    @jsii.member(jsii_name="managedDiskType")
    def managed_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managedDiskType"))

    @managed_disk_type.setter
    def managed_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "managed_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osType"))

    @os_type.setter
    def os_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "os_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osType", value)

    @builtins.property
    @jsii.member(jsii_name="vhdContainers")
    def vhd_containers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vhdContainers"))

    @vhd_containers.setter
    def vhd_containers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "vhd_containers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vhdContainers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualMachineScaleSetStorageProfileOsDisk]:
        return typing.cast(typing.Optional[VirtualMachineScaleSetStorageProfileOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualMachineScaleSetStorageProfileOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetStorageProfileOsDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualMachineScaleSetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create VirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#delete VirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#read VirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#update VirtualMachineScaleSet#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualMachineScaleSetTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#create VirtualMachineScaleSet#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#delete VirtualMachineScaleSet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#read VirtualMachineScaleSet#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_machine_scale_set#update VirtualMachineScaleSet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMachineScaleSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualMachineScaleSetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualMachineScaleSet.VirtualMachineScaleSetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualMachineScaleSetTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualMachineScaleSetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualMachineScaleSetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualMachineScaleSetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualMachineScaleSetTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualMachineScaleSet",
    "VirtualMachineScaleSetBootDiagnostics",
    "VirtualMachineScaleSetBootDiagnosticsOutputReference",
    "VirtualMachineScaleSetConfig",
    "VirtualMachineScaleSetExtension",
    "VirtualMachineScaleSetExtensionList",
    "VirtualMachineScaleSetExtensionOutputReference",
    "VirtualMachineScaleSetIdentity",
    "VirtualMachineScaleSetIdentityOutputReference",
    "VirtualMachineScaleSetNetworkProfile",
    "VirtualMachineScaleSetNetworkProfileDnsSettings",
    "VirtualMachineScaleSetNetworkProfileDnsSettingsOutputReference",
    "VirtualMachineScaleSetNetworkProfileIpConfiguration",
    "VirtualMachineScaleSetNetworkProfileIpConfigurationList",
    "VirtualMachineScaleSetNetworkProfileIpConfigurationOutputReference",
    "VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfiguration",
    "VirtualMachineScaleSetNetworkProfileIpConfigurationPublicIpAddressConfigurationOutputReference",
    "VirtualMachineScaleSetNetworkProfileList",
    "VirtualMachineScaleSetNetworkProfileOutputReference",
    "VirtualMachineScaleSetOsProfile",
    "VirtualMachineScaleSetOsProfileLinuxConfig",
    "VirtualMachineScaleSetOsProfileLinuxConfigOutputReference",
    "VirtualMachineScaleSetOsProfileLinuxConfigSshKeys",
    "VirtualMachineScaleSetOsProfileLinuxConfigSshKeysList",
    "VirtualMachineScaleSetOsProfileLinuxConfigSshKeysOutputReference",
    "VirtualMachineScaleSetOsProfileOutputReference",
    "VirtualMachineScaleSetOsProfileSecrets",
    "VirtualMachineScaleSetOsProfileSecretsList",
    "VirtualMachineScaleSetOsProfileSecretsOutputReference",
    "VirtualMachineScaleSetOsProfileSecretsVaultCertificates",
    "VirtualMachineScaleSetOsProfileSecretsVaultCertificatesList",
    "VirtualMachineScaleSetOsProfileSecretsVaultCertificatesOutputReference",
    "VirtualMachineScaleSetOsProfileWindowsConfig",
    "VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfig",
    "VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigList",
    "VirtualMachineScaleSetOsProfileWindowsConfigAdditionalUnattendConfigOutputReference",
    "VirtualMachineScaleSetOsProfileWindowsConfigOutputReference",
    "VirtualMachineScaleSetOsProfileWindowsConfigWinrm",
    "VirtualMachineScaleSetOsProfileWindowsConfigWinrmList",
    "VirtualMachineScaleSetOsProfileWindowsConfigWinrmOutputReference",
    "VirtualMachineScaleSetPlan",
    "VirtualMachineScaleSetPlanOutputReference",
    "VirtualMachineScaleSetRollingUpgradePolicy",
    "VirtualMachineScaleSetRollingUpgradePolicyOutputReference",
    "VirtualMachineScaleSetSku",
    "VirtualMachineScaleSetSkuOutputReference",
    "VirtualMachineScaleSetStorageProfileDataDisk",
    "VirtualMachineScaleSetStorageProfileDataDiskList",
    "VirtualMachineScaleSetStorageProfileDataDiskOutputReference",
    "VirtualMachineScaleSetStorageProfileImageReference",
    "VirtualMachineScaleSetStorageProfileImageReferenceOutputReference",
    "VirtualMachineScaleSetStorageProfileOsDisk",
    "VirtualMachineScaleSetStorageProfileOsDiskOutputReference",
    "VirtualMachineScaleSetTimeouts",
    "VirtualMachineScaleSetTimeoutsOutputReference",
]

publication.publish()
