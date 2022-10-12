'''
# `azurestack_linux_virtual_machine_scale_set`

Refer to the Terraform Registory for docs: [`azurestack_linux_virtual_machine_scale_set`](https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set).
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


class LinuxVirtualMachineScaleSet(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSet",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set azurestack_linux_virtual_machine_scale_set}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        admin_username: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        network_interface: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterface", typing.Dict[str, typing.Any]]]],
        os_disk: typing.Union["LinuxVirtualMachineScaleSetOsDisk", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        sku: builtins.str,
        additional_capabilities: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetAdditionalCapabilities", typing.Dict[str, typing.Any]]] = None,
        admin_password: typing.Optional[builtins.str] = None,
        admin_ssh_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetAdminSshKey", typing.Dict[str, typing.Any]]]]] = None,
        automatic_instance_repair: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetAutomaticInstanceRepair", typing.Dict[str, typing.Any]]] = None,
        automatic_os_upgrade_policy: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy", typing.Dict[str, typing.Any]]] = None,
        boot_diagnostics: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetBootDiagnostics", typing.Dict[str, typing.Any]]] = None,
        computer_name_prefix: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        data_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetDataDisk", typing.Dict[str, typing.Any]]]]] = None,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetExtension", typing.Dict[str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plan: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetPlan", typing.Dict[str, typing.Any]]] = None,
        platform_fault_domain_count: typing.Optional[jsii.Number] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scale_in_policy: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecret", typing.Dict[str, typing.Any]]]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetSourceImageReference", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_notification: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTerminateNotification", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", typing.Dict[str, typing.Any]]] = None,
        upgrade_mode: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set azurestack_linux_virtual_machine_scale_set} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_username LinuxVirtualMachineScaleSet#admin_username}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#instances LinuxVirtualMachineScaleSet#instances}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#location LinuxVirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_interface LinuxVirtualMachineScaleSet#network_interface}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#os_disk LinuxVirtualMachineScaleSet#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#resource_group_name LinuxVirtualMachineScaleSet#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#additional_capabilities LinuxVirtualMachineScaleSet#additional_capabilities}
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_password LinuxVirtualMachineScaleSet#admin_password}.
        :param admin_ssh_key: admin_ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_ssh_key LinuxVirtualMachineScaleSet#admin_ssh_key}
        :param automatic_instance_repair: automatic_instance_repair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_instance_repair LinuxVirtualMachineScaleSet#automatic_instance_repair}
        :param automatic_os_upgrade_policy: automatic_os_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_os_upgrade_policy LinuxVirtualMachineScaleSet#automatic_os_upgrade_policy}
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#boot_diagnostics LinuxVirtualMachineScaleSet#boot_diagnostics}
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#computer_name_prefix LinuxVirtualMachineScaleSet#computer_name_prefix}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#custom_data LinuxVirtualMachineScaleSet#custom_data}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#data_disk LinuxVirtualMachineScaleSet#data_disk}
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_password_authentication LinuxVirtualMachineScaleSet#disable_password_authentication}.
        :param do_not_run_extensions_on_overprovisioned_machines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines LinuxVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#encryption_at_host_enabled LinuxVirtualMachineScaleSet#encryption_at_host_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#extension LinuxVirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#health_probe_id LinuxVirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#id LinuxVirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#overprovision LinuxVirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#plan LinuxVirtualMachineScaleSet#plan}
        :param platform_fault_domain_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#platform_fault_domain_count LinuxVirtualMachineScaleSet#platform_fault_domain_count}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_vm_agent LinuxVirtualMachineScaleSet#provision_vm_agent}.
        :param scale_in_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#scale_in_policy LinuxVirtualMachineScaleSet#scale_in_policy}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#secret LinuxVirtualMachineScaleSet#secret}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#single_placement_group LinuxVirtualMachineScaleSet#single_placement_group}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_id LinuxVirtualMachineScaleSet#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_reference LinuxVirtualMachineScaleSet#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#tags LinuxVirtualMachineScaleSet#tags}.
        :param terminate_notification: terminate_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#terminate_notification LinuxVirtualMachineScaleSet#terminate_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeouts LinuxVirtualMachineScaleSet#timeouts}
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#upgrade_mode LinuxVirtualMachineScaleSet#upgrade_mode}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSet.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LinuxVirtualMachineScaleSetConfig(
            admin_username=admin_username,
            instances=instances,
            location=location,
            name=name,
            network_interface=network_interface,
            os_disk=os_disk,
            resource_group_name=resource_group_name,
            sku=sku,
            additional_capabilities=additional_capabilities,
            admin_password=admin_password,
            admin_ssh_key=admin_ssh_key,
            automatic_instance_repair=automatic_instance_repair,
            automatic_os_upgrade_policy=automatic_os_upgrade_policy,
            boot_diagnostics=boot_diagnostics,
            computer_name_prefix=computer_name_prefix,
            custom_data=custom_data,
            data_disk=data_disk,
            disable_password_authentication=disable_password_authentication,
            do_not_run_extensions_on_overprovisioned_machines=do_not_run_extensions_on_overprovisioned_machines,
            encryption_at_host_enabled=encryption_at_host_enabled,
            extension=extension,
            health_probe_id=health_probe_id,
            id=id,
            overprovision=overprovision,
            plan=plan,
            platform_fault_domain_count=platform_fault_domain_count,
            provision_vm_agent=provision_vm_agent,
            scale_in_policy=scale_in_policy,
            secret=secret,
            single_placement_group=single_placement_group,
            source_image_id=source_image_id,
            source_image_reference=source_image_reference,
            tags=tags,
            terminate_notification=terminate_notification,
            timeouts=timeouts,
            upgrade_mode=upgrade_mode,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdditionalCapabilities")
    def put_additional_capabilities(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ultra_ssd_enabled LinuxVirtualMachineScaleSet#ultra_ssd_enabled}.
        '''
        value = LinuxVirtualMachineScaleSetAdditionalCapabilities(
            ultra_ssd_enabled=ultra_ssd_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdditionalCapabilities", [value]))

    @jsii.member(jsii_name="putAdminSshKey")
    def put_admin_ssh_key(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetAdminSshKey", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSet.put_admin_ssh_key)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdminSshKey", [value]))

    @jsii.member(jsii_name="putAutomaticInstanceRepair")
    def put_automatic_instance_repair(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        grace_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#grace_period LinuxVirtualMachineScaleSet#grace_period}.
        '''
        value = LinuxVirtualMachineScaleSetAutomaticInstanceRepair(
            enabled=enabled, grace_period=grace_period
        )

        return typing.cast(None, jsii.invoke(self, "putAutomaticInstanceRepair", [value]))

    @jsii.member(jsii_name="putAutomaticOsUpgradePolicy")
    def put_automatic_os_upgrade_policy(
        self,
        *,
        disable_automatic_rollback: typing.Union[builtins.bool, cdktf.IResolvable],
        enable_automatic_os_upgrade: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disable_automatic_rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_automatic_rollback LinuxVirtualMachineScaleSet#disable_automatic_rollback}.
        :param enable_automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_automatic_os_upgrade LinuxVirtualMachineScaleSet#enable_automatic_os_upgrade}.
        '''
        value = LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy(
            disable_automatic_rollback=disable_automatic_rollback,
            enable_automatic_os_upgrade=enable_automatic_os_upgrade,
        )

        return typing.cast(None, jsii.invoke(self, "putAutomaticOsUpgradePolicy", [value]))

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_uri LinuxVirtualMachineScaleSet#storage_account_uri}.
        '''
        value = LinuxVirtualMachineScaleSetBootDiagnostics(
            storage_account_uri=storage_account_uri
        )

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putDataDisk")
    def put_data_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetDataDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSet.put_data_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataDisk", [value]))

    @jsii.member(jsii_name="putExtension")
    def put_extension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetExtension", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSet.put_extension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtension", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterface", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSet.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings", typing.Dict[str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#diff_disk_settings LinuxVirtualMachineScaleSet#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        value = LinuxVirtualMachineScaleSetOsDisk(
            caching=caching,
            storage_account_type=storage_account_type,
            diff_disk_settings=diff_disk_settings,
            disk_encryption_set_id=disk_encryption_set_id,
            disk_size_gb=disk_size_gb,
            write_accelerator_enabled=write_accelerator_enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putOsDisk", [value]))

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#product LinuxVirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        '''
        value = LinuxVirtualMachineScaleSetPlan(
            name=name, product=product, publisher=publisher
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putSecret")
    def put_secret(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecret", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSet.put_secret)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecret", [value]))

    @jsii.member(jsii_name="putSourceImageReference")
    def put_source_image_reference(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#offer LinuxVirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.
        '''
        value = LinuxVirtualMachineScaleSetSourceImageReference(
            offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putSourceImageReference", [value]))

    @jsii.member(jsii_name="putTerminateNotification")
    def put_terminate_notification(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeout LinuxVirtualMachineScaleSet#timeout}.
        '''
        value = LinuxVirtualMachineScaleSetTerminateNotification(
            enabled=enabled, timeout=timeout
        )

        return typing.cast(None, jsii.invoke(self, "putTerminateNotification", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create LinuxVirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#delete LinuxVirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#read LinuxVirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#update LinuxVirtualMachineScaleSet#update}.
        '''
        value = LinuxVirtualMachineScaleSetTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdditionalCapabilities")
    def reset_additional_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalCapabilities", []))

    @jsii.member(jsii_name="resetAdminPassword")
    def reset_admin_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminPassword", []))

    @jsii.member(jsii_name="resetAdminSshKey")
    def reset_admin_ssh_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminSshKey", []))

    @jsii.member(jsii_name="resetAutomaticInstanceRepair")
    def reset_automatic_instance_repair(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticInstanceRepair", []))

    @jsii.member(jsii_name="resetAutomaticOsUpgradePolicy")
    def reset_automatic_os_upgrade_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticOsUpgradePolicy", []))

    @jsii.member(jsii_name="resetBootDiagnostics")
    def reset_boot_diagnostics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiagnostics", []))

    @jsii.member(jsii_name="resetComputerNamePrefix")
    def reset_computer_name_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputerNamePrefix", []))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @jsii.member(jsii_name="resetDataDisk")
    def reset_data_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataDisk", []))

    @jsii.member(jsii_name="resetDisablePasswordAuthentication")
    def reset_disable_password_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablePasswordAuthentication", []))

    @jsii.member(jsii_name="resetDoNotRunExtensionsOnOverprovisionedMachines")
    def reset_do_not_run_extensions_on_overprovisioned_machines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDoNotRunExtensionsOnOverprovisionedMachines", []))

    @jsii.member(jsii_name="resetEncryptionAtHostEnabled")
    def reset_encryption_at_host_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAtHostEnabled", []))

    @jsii.member(jsii_name="resetExtension")
    def reset_extension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtension", []))

    @jsii.member(jsii_name="resetHealthProbeId")
    def reset_health_probe_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthProbeId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOverprovision")
    def reset_overprovision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverprovision", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetPlatformFaultDomainCount")
    def reset_platform_fault_domain_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformFaultDomainCount", []))

    @jsii.member(jsii_name="resetProvisionVmAgent")
    def reset_provision_vm_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionVmAgent", []))

    @jsii.member(jsii_name="resetScaleInPolicy")
    def reset_scale_in_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleInPolicy", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetSinglePlacementGroup")
    def reset_single_placement_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSinglePlacementGroup", []))

    @jsii.member(jsii_name="resetSourceImageId")
    def reset_source_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageId", []))

    @jsii.member(jsii_name="resetSourceImageReference")
    def reset_source_image_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageReference", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTerminateNotification")
    def reset_terminate_notification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminateNotification", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUpgradeMode")
    def reset_upgrade_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpgradeMode", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> "LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference", jsii.get(self, "additionalCapabilities"))

    @builtins.property
    @jsii.member(jsii_name="adminSshKey")
    def admin_ssh_key(self) -> "LinuxVirtualMachineScaleSetAdminSshKeyList":
        return typing.cast("LinuxVirtualMachineScaleSetAdminSshKeyList", jsii.get(self, "adminSshKey"))

    @builtins.property
    @jsii.member(jsii_name="automaticInstanceRepair")
    def automatic_instance_repair(
        self,
    ) -> "LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference", jsii.get(self, "automaticInstanceRepair"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgradePolicy")
    def automatic_os_upgrade_policy(
        self,
    ) -> "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference", jsii.get(self, "automaticOsUpgradePolicy"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(
        self,
    ) -> "LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="dataDisk")
    def data_disk(self) -> "LinuxVirtualMachineScaleSetDataDiskList":
        return typing.cast("LinuxVirtualMachineScaleSetDataDiskList", jsii.get(self, "dataDisk"))

    @builtins.property
    @jsii.member(jsii_name="extension")
    def extension(self) -> "LinuxVirtualMachineScaleSetExtensionList":
        return typing.cast("LinuxVirtualMachineScaleSetExtensionList", jsii.get(self, "extension"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "LinuxVirtualMachineScaleSetNetworkInterfaceList":
        return typing.cast("LinuxVirtualMachineScaleSetNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "LinuxVirtualMachineScaleSetOsDiskOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "LinuxVirtualMachineScaleSetPlanOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetPlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> "LinuxVirtualMachineScaleSetSecretList":
        return typing.cast("LinuxVirtualMachineScaleSetSecretList", jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReference")
    def source_image_reference(
        self,
    ) -> "LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference", jsii.get(self, "sourceImageReference"))

    @builtins.property
    @jsii.member(jsii_name="terminateNotification")
    def terminate_notification(
        self,
    ) -> "LinuxVirtualMachineScaleSetTerminateNotificationOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetTerminateNotificationOutputReference", jsii.get(self, "terminateNotification"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LinuxVirtualMachineScaleSetTimeoutsOutputReference":
        return typing.cast("LinuxVirtualMachineScaleSetTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uniqueId")
    def unique_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uniqueId"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilitiesInput")
    def additional_capabilities_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetAdditionalCapabilities"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetAdditionalCapabilities"], jsii.get(self, "additionalCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminSshKeyInput")
    def admin_ssh_key_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetAdminSshKey"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetAdminSshKey"]]], jsii.get(self, "adminSshKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticInstanceRepairInput")
    def automatic_instance_repair_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetAutomaticInstanceRepair"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetAutomaticInstanceRepair"], jsii.get(self, "automaticInstanceRepairInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticOsUpgradePolicyInput")
    def automatic_os_upgrade_policy_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy"], jsii.get(self, "automaticOsUpgradePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnosticsInput")
    def boot_diagnostics_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetBootDiagnostics"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="computerNamePrefixInput")
    def computer_name_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computerNamePrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskInput")
    def data_disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]], jsii.get(self, "dataDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="disablePasswordAuthenticationInput")
    def disable_password_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disablePasswordAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="doNotRunExtensionsOnOverprovisionedMachinesInput")
    def do_not_run_extensions_on_overprovisioned_machines_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "doNotRunExtensionsOnOverprovisionedMachinesInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtHostEnabledInput")
    def encryption_at_host_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionAtHostEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionInput")
    def extension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]], jsii.get(self, "extensionInput"))

    @builtins.property
    @jsii.member(jsii_name="healthProbeIdInput")
    def health_probe_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthProbeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instancesInput")
    def instances_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instancesInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(self) -> typing.Optional["LinuxVirtualMachineScaleSetOsDisk"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="overprovisionInput")
    def overprovision_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "overprovisionInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["LinuxVirtualMachineScaleSetPlan"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetPlan"], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="platformFaultDomainCountInput")
    def platform_fault_domain_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "platformFaultDomainCountInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionVmAgentInput")
    def provision_vm_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "provisionVmAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicyInput")
    def scale_in_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scaleInPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="singlePlacementGroupInput")
    def single_placement_group_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "singlePlacementGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageIdInput")
    def source_image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceImageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReferenceInput")
    def source_image_reference_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"], jsii.get(self, "sourceImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateNotificationInput")
    def terminate_notification_input(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"]:
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"], jsii.get(self, "terminateNotificationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="upgradeModeInput")
    def upgrade_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "upgradeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "admin_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="computerNamePrefix")
    def computer_name_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerNamePrefix"))

    @computer_name_prefix.setter
    def computer_name_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "computer_name_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerNamePrefix", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "custom_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "disable_password_authentication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablePasswordAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="doNotRunExtensionsOnOverprovisionedMachines")
    def do_not_run_extensions_on_overprovisioned_machines(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "doNotRunExtensionsOnOverprovisionedMachines"))

    @do_not_run_extensions_on_overprovisioned_machines.setter
    def do_not_run_extensions_on_overprovisioned_machines(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "do_not_run_extensions_on_overprovisioned_machines").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "doNotRunExtensionsOnOverprovisionedMachines", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionAtHostEnabled")
    def encryption_at_host_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "encryptionAtHostEnabled"))

    @encryption_at_host_enabled.setter
    def encryption_at_host_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "encryption_at_host_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtHostEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="healthProbeId")
    def health_probe_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthProbeId"))

    @health_probe_id.setter
    def health_probe_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "health_probe_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthProbeId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="instances")
    def instances(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instances"))

    @instances.setter
    def instances(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "instances").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instances", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "name").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "overprovision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overprovision", value)

    @builtins.property
    @jsii.member(jsii_name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "platformFaultDomainCount"))

    @platform_fault_domain_count.setter
    def platform_fault_domain_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "platform_fault_domain_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformFaultDomainCount", value)

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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "provision_vm_agent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="scaleInPolicy")
    def scale_in_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scaleInPolicy"))

    @scale_in_policy.setter
    def scale_in_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "scale_in_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleInPolicy", value)

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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "single_placement_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singlePlacementGroup", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImageId")
    def source_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImageId"))

    @source_image_id.setter
    def source_image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "source_image_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImageId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="upgradeMode")
    def upgrade_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "upgradeMode"))

    @upgrade_mode.setter
    def upgrade_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSet, "upgrade_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upgradeMode", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdditionalCapabilities",
    jsii_struct_bases=[],
    name_mapping={"ultra_ssd_enabled": "ultraSsdEnabled"},
)
class LinuxVirtualMachineScaleSetAdditionalCapabilities:
    def __init__(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ultra_ssd_enabled LinuxVirtualMachineScaleSet#ultra_ssd_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAdditionalCapabilities.__init__)
            check_type(argname="argument ultra_ssd_enabled", value=ultra_ssd_enabled, expected_type=type_hints["ultra_ssd_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ultra_ssd_enabled is not None:
            self._values["ultra_ssd_enabled"] = ultra_ssd_enabled

    @builtins.property
    def ultra_ssd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ultra_ssd_enabled LinuxVirtualMachineScaleSet#ultra_ssd_enabled}.'''
        result = self._values.get("ultra_ssd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAdditionalCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUltraSsdEnabled")
    def reset_ultra_ssd_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUltraSsdEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="ultraSsdEnabledInput")
    def ultra_ssd_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ultraSsdEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ultraSsdEnabled")
    def ultra_ssd_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ultraSsdEnabled"))

    @ultra_ssd_enabled.setter
    def ultra_ssd_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference, "ultra_ssd_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ultraSsdEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdminSshKey",
    jsii_struct_bases=[],
    name_mapping={"public_key": "publicKey", "username": "username"},
)
class LinuxVirtualMachineScaleSetAdminSshKey:
    def __init__(self, *, public_key: builtins.str, username: builtins.str) -> None:
        '''
        :param public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#public_key LinuxVirtualMachineScaleSet#public_key}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#username LinuxVirtualMachineScaleSet#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAdminSshKey.__init__)
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "public_key": public_key,
            "username": username,
        }

    @builtins.property
    def public_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#public_key LinuxVirtualMachineScaleSet#public_key}.'''
        result = self._values.get("public_key")
        assert result is not None, "Required property 'public_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#username LinuxVirtualMachineScaleSet#username}.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAdminSshKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAdminSshKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdminSshKeyList",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAdminSshKeyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetAdminSshKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAdminSshKeyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetAdminSshKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdminSshKeyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdminSshKeyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdminSshKeyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdminSshKeyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetAdminSshKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAdminSshKeyOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAdminSshKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="publicKeyInput")
    def public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdminSshKeyOutputReference, "public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdminSshKeyOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAdminSshKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticInstanceRepair",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "grace_period": "gracePeriod"},
)
class LinuxVirtualMachineScaleSetAutomaticInstanceRepair:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        grace_period: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param grace_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#grace_period LinuxVirtualMachineScaleSet#grace_period}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAutomaticInstanceRepair.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument grace_period", value=grace_period, expected_type=type_hints["grace_period"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if grace_period is not None:
            self._values["grace_period"] = grace_period

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def grace_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#grace_period LinuxVirtualMachineScaleSet#grace_period}.'''
        result = self._values.get("grace_period")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAutomaticInstanceRepair(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGracePeriod")
    def reset_grace_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGracePeriod", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="gracePeriodInput")
    def grace_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gracePeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="gracePeriod")
    def grace_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gracePeriod"))

    @grace_period.setter
    def grace_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference, "grace_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gracePeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "disable_automatic_rollback": "disableAutomaticRollback",
        "enable_automatic_os_upgrade": "enableAutomaticOsUpgrade",
    },
)
class LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy:
    def __init__(
        self,
        *,
        disable_automatic_rollback: typing.Union[builtins.bool, cdktf.IResolvable],
        enable_automatic_os_upgrade: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param disable_automatic_rollback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_automatic_rollback LinuxVirtualMachineScaleSet#disable_automatic_rollback}.
        :param enable_automatic_os_upgrade: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_automatic_os_upgrade LinuxVirtualMachineScaleSet#enable_automatic_os_upgrade}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy.__init__)
            check_type(argname="argument disable_automatic_rollback", value=disable_automatic_rollback, expected_type=type_hints["disable_automatic_rollback"])
            check_type(argname="argument enable_automatic_os_upgrade", value=enable_automatic_os_upgrade, expected_type=type_hints["enable_automatic_os_upgrade"])
        self._values: typing.Dict[str, typing.Any] = {
            "disable_automatic_rollback": disable_automatic_rollback,
            "enable_automatic_os_upgrade": enable_automatic_os_upgrade,
        }

    @builtins.property
    def disable_automatic_rollback(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_automatic_rollback LinuxVirtualMachineScaleSet#disable_automatic_rollback}.'''
        result = self._values.get("disable_automatic_rollback")
        assert result is not None, "Required property 'disable_automatic_rollback' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def enable_automatic_os_upgrade(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_automatic_os_upgrade LinuxVirtualMachineScaleSet#enable_automatic_os_upgrade}.'''
        result = self._values.get("enable_automatic_os_upgrade")
        assert result is not None, "Required property 'enable_automatic_os_upgrade' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="disableAutomaticRollbackInput")
    def disable_automatic_rollback_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableAutomaticRollbackInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticOsUpgradeInput")
    def enable_automatic_os_upgrade_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutomaticOsUpgradeInput"))

    @builtins.property
    @jsii.member(jsii_name="disableAutomaticRollback")
    def disable_automatic_rollback(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableAutomaticRollback"))

    @disable_automatic_rollback.setter
    def disable_automatic_rollback(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference, "disable_automatic_rollback").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableAutomaticRollback", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticOsUpgrade")
    def enable_automatic_os_upgrade(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutomaticOsUpgrade"))

    @enable_automatic_os_upgrade.setter
    def enable_automatic_os_upgrade(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference, "enable_automatic_os_upgrade").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticOsUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"storage_account_uri": "storageAccountUri"},
)
class LinuxVirtualMachineScaleSetBootDiagnostics:
    def __init__(self, *, storage_account_uri: builtins.str) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_uri LinuxVirtualMachineScaleSet#storage_account_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetBootDiagnostics.__init__)
            check_type(argname="argument storage_account_uri", value=storage_account_uri, expected_type=type_hints["storage_account_uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "storage_account_uri": storage_account_uri,
        }

    @builtins.property
    def storage_account_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_uri LinuxVirtualMachineScaleSet#storage_account_uri}.'''
        result = self._values.get("storage_account_uri")
        assert result is not None, "Required property 'storage_account_uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="storageAccountUriInput")
    def storage_account_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountUriInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountUri")
    def storage_account_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountUri"))

    @storage_account_uri.setter
    def storage_account_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference, "storage_account_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "admin_username": "adminUsername",
        "instances": "instances",
        "location": "location",
        "name": "name",
        "network_interface": "networkInterface",
        "os_disk": "osDisk",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "additional_capabilities": "additionalCapabilities",
        "admin_password": "adminPassword",
        "admin_ssh_key": "adminSshKey",
        "automatic_instance_repair": "automaticInstanceRepair",
        "automatic_os_upgrade_policy": "automaticOsUpgradePolicy",
        "boot_diagnostics": "bootDiagnostics",
        "computer_name_prefix": "computerNamePrefix",
        "custom_data": "customData",
        "data_disk": "dataDisk",
        "disable_password_authentication": "disablePasswordAuthentication",
        "do_not_run_extensions_on_overprovisioned_machines": "doNotRunExtensionsOnOverprovisionedMachines",
        "encryption_at_host_enabled": "encryptionAtHostEnabled",
        "extension": "extension",
        "health_probe_id": "healthProbeId",
        "id": "id",
        "overprovision": "overprovision",
        "plan": "plan",
        "platform_fault_domain_count": "platformFaultDomainCount",
        "provision_vm_agent": "provisionVmAgent",
        "scale_in_policy": "scaleInPolicy",
        "secret": "secret",
        "single_placement_group": "singlePlacementGroup",
        "source_image_id": "sourceImageId",
        "source_image_reference": "sourceImageReference",
        "tags": "tags",
        "terminate_notification": "terminateNotification",
        "timeouts": "timeouts",
        "upgrade_mode": "upgradeMode",
    },
)
class LinuxVirtualMachineScaleSetConfig(cdktf.TerraformMetaArguments):
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
        admin_username: builtins.str,
        instances: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        network_interface: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterface", typing.Dict[str, typing.Any]]]],
        os_disk: typing.Union["LinuxVirtualMachineScaleSetOsDisk", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        sku: builtins.str,
        additional_capabilities: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAdditionalCapabilities, typing.Dict[str, typing.Any]]] = None,
        admin_password: typing.Optional[builtins.str] = None,
        admin_ssh_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetAdminSshKey, typing.Dict[str, typing.Any]]]]] = None,
        automatic_instance_repair: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticInstanceRepair, typing.Dict[str, typing.Any]]] = None,
        automatic_os_upgrade_policy: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy, typing.Dict[str, typing.Any]]] = None,
        boot_diagnostics: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetBootDiagnostics, typing.Dict[str, typing.Any]]] = None,
        computer_name_prefix: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        data_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetDataDisk", typing.Dict[str, typing.Any]]]]] = None,
        disable_password_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        do_not_run_extensions_on_overprovisioned_machines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        extension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetExtension", typing.Dict[str, typing.Any]]]]] = None,
        health_probe_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overprovision: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plan: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetPlan", typing.Dict[str, typing.Any]]] = None,
        platform_fault_domain_count: typing.Optional[jsii.Number] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scale_in_policy: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecret", typing.Dict[str, typing.Any]]]]] = None,
        single_placement_group: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetSourceImageReference", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_notification: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTerminateNotification", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetTimeouts", typing.Dict[str, typing.Any]]] = None,
        upgrade_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_username LinuxVirtualMachineScaleSet#admin_username}.
        :param instances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#instances LinuxVirtualMachineScaleSet#instances}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#location LinuxVirtualMachineScaleSet#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param network_interface: network_interface block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_interface LinuxVirtualMachineScaleSet#network_interface}
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#os_disk LinuxVirtualMachineScaleSet#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#resource_group_name LinuxVirtualMachineScaleSet#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#additional_capabilities LinuxVirtualMachineScaleSet#additional_capabilities}
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_password LinuxVirtualMachineScaleSet#admin_password}.
        :param admin_ssh_key: admin_ssh_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_ssh_key LinuxVirtualMachineScaleSet#admin_ssh_key}
        :param automatic_instance_repair: automatic_instance_repair block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_instance_repair LinuxVirtualMachineScaleSet#automatic_instance_repair}
        :param automatic_os_upgrade_policy: automatic_os_upgrade_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_os_upgrade_policy LinuxVirtualMachineScaleSet#automatic_os_upgrade_policy}
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#boot_diagnostics LinuxVirtualMachineScaleSet#boot_diagnostics}
        :param computer_name_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#computer_name_prefix LinuxVirtualMachineScaleSet#computer_name_prefix}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#custom_data LinuxVirtualMachineScaleSet#custom_data}.
        :param data_disk: data_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#data_disk LinuxVirtualMachineScaleSet#data_disk}
        :param disable_password_authentication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_password_authentication LinuxVirtualMachineScaleSet#disable_password_authentication}.
        :param do_not_run_extensions_on_overprovisioned_machines: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines LinuxVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#encryption_at_host_enabled LinuxVirtualMachineScaleSet#encryption_at_host_enabled}.
        :param extension: extension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#extension LinuxVirtualMachineScaleSet#extension}
        :param health_probe_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#health_probe_id LinuxVirtualMachineScaleSet#health_probe_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#id LinuxVirtualMachineScaleSet#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overprovision: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#overprovision LinuxVirtualMachineScaleSet#overprovision}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#plan LinuxVirtualMachineScaleSet#plan}
        :param platform_fault_domain_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#platform_fault_domain_count LinuxVirtualMachineScaleSet#platform_fault_domain_count}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_vm_agent LinuxVirtualMachineScaleSet#provision_vm_agent}.
        :param scale_in_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#scale_in_policy LinuxVirtualMachineScaleSet#scale_in_policy}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#secret LinuxVirtualMachineScaleSet#secret}
        :param single_placement_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#single_placement_group LinuxVirtualMachineScaleSet#single_placement_group}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_id LinuxVirtualMachineScaleSet#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_reference LinuxVirtualMachineScaleSet#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#tags LinuxVirtualMachineScaleSet#tags}.
        :param terminate_notification: terminate_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#terminate_notification LinuxVirtualMachineScaleSet#terminate_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeouts LinuxVirtualMachineScaleSet#timeouts}
        :param upgrade_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#upgrade_mode LinuxVirtualMachineScaleSet#upgrade_mode}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_disk, dict):
            os_disk = LinuxVirtualMachineScaleSetOsDisk(**os_disk)
        if isinstance(additional_capabilities, dict):
            additional_capabilities = LinuxVirtualMachineScaleSetAdditionalCapabilities(**additional_capabilities)
        if isinstance(automatic_instance_repair, dict):
            automatic_instance_repair = LinuxVirtualMachineScaleSetAutomaticInstanceRepair(**automatic_instance_repair)
        if isinstance(automatic_os_upgrade_policy, dict):
            automatic_os_upgrade_policy = LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy(**automatic_os_upgrade_policy)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = LinuxVirtualMachineScaleSetBootDiagnostics(**boot_diagnostics)
        if isinstance(plan, dict):
            plan = LinuxVirtualMachineScaleSetPlan(**plan)
        if isinstance(source_image_reference, dict):
            source_image_reference = LinuxVirtualMachineScaleSetSourceImageReference(**source_image_reference)
        if isinstance(terminate_notification, dict):
            terminate_notification = LinuxVirtualMachineScaleSetTerminateNotification(**terminate_notification)
        if isinstance(timeouts, dict):
            timeouts = LinuxVirtualMachineScaleSetTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument additional_capabilities", value=additional_capabilities, expected_type=type_hints["additional_capabilities"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_ssh_key", value=admin_ssh_key, expected_type=type_hints["admin_ssh_key"])
            check_type(argname="argument automatic_instance_repair", value=automatic_instance_repair, expected_type=type_hints["automatic_instance_repair"])
            check_type(argname="argument automatic_os_upgrade_policy", value=automatic_os_upgrade_policy, expected_type=type_hints["automatic_os_upgrade_policy"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument computer_name_prefix", value=computer_name_prefix, expected_type=type_hints["computer_name_prefix"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument data_disk", value=data_disk, expected_type=type_hints["data_disk"])
            check_type(argname="argument disable_password_authentication", value=disable_password_authentication, expected_type=type_hints["disable_password_authentication"])
            check_type(argname="argument do_not_run_extensions_on_overprovisioned_machines", value=do_not_run_extensions_on_overprovisioned_machines, expected_type=type_hints["do_not_run_extensions_on_overprovisioned_machines"])
            check_type(argname="argument encryption_at_host_enabled", value=encryption_at_host_enabled, expected_type=type_hints["encryption_at_host_enabled"])
            check_type(argname="argument extension", value=extension, expected_type=type_hints["extension"])
            check_type(argname="argument health_probe_id", value=health_probe_id, expected_type=type_hints["health_probe_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument overprovision", value=overprovision, expected_type=type_hints["overprovision"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument platform_fault_domain_count", value=platform_fault_domain_count, expected_type=type_hints["platform_fault_domain_count"])
            check_type(argname="argument provision_vm_agent", value=provision_vm_agent, expected_type=type_hints["provision_vm_agent"])
            check_type(argname="argument scale_in_policy", value=scale_in_policy, expected_type=type_hints["scale_in_policy"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument single_placement_group", value=single_placement_group, expected_type=type_hints["single_placement_group"])
            check_type(argname="argument source_image_id", value=source_image_id, expected_type=type_hints["source_image_id"])
            check_type(argname="argument source_image_reference", value=source_image_reference, expected_type=type_hints["source_image_reference"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument terminate_notification", value=terminate_notification, expected_type=type_hints["terminate_notification"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument upgrade_mode", value=upgrade_mode, expected_type=type_hints["upgrade_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "admin_username": admin_username,
            "instances": instances,
            "location": location,
            "name": name,
            "network_interface": network_interface,
            "os_disk": os_disk,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if additional_capabilities is not None:
            self._values["additional_capabilities"] = additional_capabilities
        if admin_password is not None:
            self._values["admin_password"] = admin_password
        if admin_ssh_key is not None:
            self._values["admin_ssh_key"] = admin_ssh_key
        if automatic_instance_repair is not None:
            self._values["automatic_instance_repair"] = automatic_instance_repair
        if automatic_os_upgrade_policy is not None:
            self._values["automatic_os_upgrade_policy"] = automatic_os_upgrade_policy
        if boot_diagnostics is not None:
            self._values["boot_diagnostics"] = boot_diagnostics
        if computer_name_prefix is not None:
            self._values["computer_name_prefix"] = computer_name_prefix
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if data_disk is not None:
            self._values["data_disk"] = data_disk
        if disable_password_authentication is not None:
            self._values["disable_password_authentication"] = disable_password_authentication
        if do_not_run_extensions_on_overprovisioned_machines is not None:
            self._values["do_not_run_extensions_on_overprovisioned_machines"] = do_not_run_extensions_on_overprovisioned_machines
        if encryption_at_host_enabled is not None:
            self._values["encryption_at_host_enabled"] = encryption_at_host_enabled
        if extension is not None:
            self._values["extension"] = extension
        if health_probe_id is not None:
            self._values["health_probe_id"] = health_probe_id
        if id is not None:
            self._values["id"] = id
        if overprovision is not None:
            self._values["overprovision"] = overprovision
        if plan is not None:
            self._values["plan"] = plan
        if platform_fault_domain_count is not None:
            self._values["platform_fault_domain_count"] = platform_fault_domain_count
        if provision_vm_agent is not None:
            self._values["provision_vm_agent"] = provision_vm_agent
        if scale_in_policy is not None:
            self._values["scale_in_policy"] = scale_in_policy
        if secret is not None:
            self._values["secret"] = secret
        if single_placement_group is not None:
            self._values["single_placement_group"] = single_placement_group
        if source_image_id is not None:
            self._values["source_image_id"] = source_image_id
        if source_image_reference is not None:
            self._values["source_image_reference"] = source_image_reference
        if tags is not None:
            self._values["tags"] = tags
        if terminate_notification is not None:
            self._values["terminate_notification"] = terminate_notification
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if upgrade_mode is not None:
            self._values["upgrade_mode"] = upgrade_mode

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
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_username LinuxVirtualMachineScaleSet#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instances(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#instances LinuxVirtualMachineScaleSet#instances}.'''
        result = self._values.get("instances")
        assert result is not None, "Required property 'instances' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#location LinuxVirtualMachineScaleSet#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]]:
        '''network_interface block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_interface LinuxVirtualMachineScaleSet#network_interface}
        '''
        result = self._values.get("network_interface")
        assert result is not None, "Required property 'network_interface' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterface"]], result)

    @builtins.property
    def os_disk(self) -> "LinuxVirtualMachineScaleSetOsDisk":
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#os_disk LinuxVirtualMachineScaleSet#os_disk}
        '''
        result = self._values.get("os_disk")
        assert result is not None, "Required property 'os_disk' is missing"
        return typing.cast("LinuxVirtualMachineScaleSetOsDisk", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#resource_group_name LinuxVirtualMachineScaleSet#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_capabilities(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities]:
        '''additional_capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#additional_capabilities LinuxVirtualMachineScaleSet#additional_capabilities}
        '''
        result = self._values.get("additional_capabilities")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAdditionalCapabilities], result)

    @builtins.property
    def admin_password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_password LinuxVirtualMachineScaleSet#admin_password}.'''
        result = self._values.get("admin_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def admin_ssh_key(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]]:
        '''admin_ssh_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#admin_ssh_key LinuxVirtualMachineScaleSet#admin_ssh_key}
        '''
        result = self._values.get("admin_ssh_key")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetAdminSshKey]]], result)

    @builtins.property
    def automatic_instance_repair(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair]:
        '''automatic_instance_repair block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_instance_repair LinuxVirtualMachineScaleSet#automatic_instance_repair}
        '''
        result = self._values.get("automatic_instance_repair")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticInstanceRepair], result)

    @builtins.property
    def automatic_os_upgrade_policy(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy]:
        '''automatic_os_upgrade_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_os_upgrade_policy LinuxVirtualMachineScaleSet#automatic_os_upgrade_policy}
        '''
        result = self._values.get("automatic_os_upgrade_policy")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy], result)

    @builtins.property
    def boot_diagnostics(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#boot_diagnostics LinuxVirtualMachineScaleSet#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetBootDiagnostics], result)

    @builtins.property
    def computer_name_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#computer_name_prefix LinuxVirtualMachineScaleSet#computer_name_prefix}.'''
        result = self._values.get("computer_name_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#custom_data LinuxVirtualMachineScaleSet#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_disk(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]]:
        '''data_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#data_disk LinuxVirtualMachineScaleSet#data_disk}
        '''
        result = self._values.get("data_disk")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetDataDisk"]]], result)

    @builtins.property
    def disable_password_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disable_password_authentication LinuxVirtualMachineScaleSet#disable_password_authentication}.'''
        result = self._values.get("disable_password_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def do_not_run_extensions_on_overprovisioned_machines(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#do_not_run_extensions_on_overprovisioned_machines LinuxVirtualMachineScaleSet#do_not_run_extensions_on_overprovisioned_machines}.'''
        result = self._values.get("do_not_run_extensions_on_overprovisioned_machines")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_at_host_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#encryption_at_host_enabled LinuxVirtualMachineScaleSet#encryption_at_host_enabled}.'''
        result = self._values.get("encryption_at_host_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def extension(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]]:
        '''extension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#extension LinuxVirtualMachineScaleSet#extension}
        '''
        result = self._values.get("extension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetExtension"]]], result)

    @builtins.property
    def health_probe_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#health_probe_id LinuxVirtualMachineScaleSet#health_probe_id}.'''
        result = self._values.get("health_probe_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#id LinuxVirtualMachineScaleSet#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overprovision(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#overprovision LinuxVirtualMachineScaleSet#overprovision}.'''
        result = self._values.get("overprovision")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def plan(self) -> typing.Optional["LinuxVirtualMachineScaleSetPlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#plan LinuxVirtualMachineScaleSet#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetPlan"], result)

    @builtins.property
    def platform_fault_domain_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#platform_fault_domain_count LinuxVirtualMachineScaleSet#platform_fault_domain_count}.'''
        result = self._values.get("platform_fault_domain_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_vm_agent LinuxVirtualMachineScaleSet#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scale_in_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#scale_in_policy LinuxVirtualMachineScaleSet#scale_in_policy}.'''
        result = self._values.get("scale_in_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]]:
        '''secret block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#secret LinuxVirtualMachineScaleSet#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecret"]]], result)

    @builtins.property
    def single_placement_group(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#single_placement_group LinuxVirtualMachineScaleSet#single_placement_group}.'''
        result = self._values.get("single_placement_group")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source_image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_id LinuxVirtualMachineScaleSet#source_image_id}.'''
        result = self._values.get("source_image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image_reference(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"]:
        '''source_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#source_image_reference LinuxVirtualMachineScaleSet#source_image_reference}
        '''
        result = self._values.get("source_image_reference")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetSourceImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#tags LinuxVirtualMachineScaleSet#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def terminate_notification(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"]:
        '''terminate_notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#terminate_notification LinuxVirtualMachineScaleSet#terminate_notification}
        '''
        result = self._values.get("terminate_notification")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetTerminateNotification"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LinuxVirtualMachineScaleSetTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeouts LinuxVirtualMachineScaleSet#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetTimeouts"], result)

    @builtins.property
    def upgrade_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#upgrade_mode LinuxVirtualMachineScaleSet#upgrade_mode}.'''
        result = self._values.get("upgrade_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetDataDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching": "caching",
        "disk_size_gb": "diskSizeGb",
        "lun": "lun",
        "storage_account_type": "storageAccountType",
        "create_option": "createOption",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class LinuxVirtualMachineScaleSetDataDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        disk_size_gb: jsii.Number,
        lun: jsii.Number,
        storage_account_type: builtins.str,
        create_option: typing.Optional[builtins.str] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.
        :param lun: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#lun LinuxVirtualMachineScaleSet#lun}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.
        :param create_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create_option LinuxVirtualMachineScaleSet#create_option}.
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetDataDisk.__init__)
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument create_option", value=create_option, expected_type=type_hints["create_option"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument write_accelerator_enabled", value=write_accelerator_enabled, expected_type=type_hints["write_accelerator_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "caching": caching,
            "disk_size_gb": disk_size_gb,
            "lun": lun,
            "storage_account_type": storage_account_type,
        }
        if create_option is not None:
            self._values["create_option"] = create_option
        if disk_encryption_set_id is not None:
            self._values["disk_encryption_set_id"] = disk_encryption_set_id
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def caching(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_size_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        assert result is not None, "Required property 'disk_size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lun(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#lun LinuxVirtualMachineScaleSet#lun}.'''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def create_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create_option LinuxVirtualMachineScaleSet#create_option}.'''
        result = self._values.get("create_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetDataDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetDataDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetDataDiskList",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetDataDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetDataDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetDataDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetDataDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetDataDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetDataDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetDataDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetDataDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetDataDiskOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetDataDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCreateOption")
    def reset_create_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateOption", []))

    @jsii.member(jsii_name="resetDiskEncryptionSetId")
    def reset_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetWriteAcceleratorEnabled")
    def reset_write_accelerator_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcceleratorEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="createOptionInput")
    def create_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabledInput")
    def write_accelerator_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "writeAcceleratorEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="createOption")
    def create_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createOption"))

    @create_option.setter
    def create_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "create_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createOption", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "lun").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabled")
    def write_accelerator_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "writeAcceleratorEnabled"))

    @write_accelerator_enabled.setter
    def write_accelerator_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "write_accelerator_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetDataDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetDataDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetDataDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetDataDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetExtension",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "publisher": "publisher",
        "type": "type",
        "type_handler_version": "typeHandlerVersion",
        "automatic_upgrade_enabled": "automaticUpgradeEnabled",
        "auto_upgrade_minor_version": "autoUpgradeMinorVersion",
        "force_update_tag": "forceUpdateTag",
        "protected_settings": "protectedSettings",
        "provision_after_extensions": "provisionAfterExtensions",
        "settings": "settings",
    },
)
class LinuxVirtualMachineScaleSetExtension:
    def __init__(
        self,
        *,
        name: builtins.str,
        publisher: builtins.str,
        type: builtins.str,
        type_handler_version: builtins.str,
        automatic_upgrade_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_update_tag: typing.Optional[builtins.str] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        provision_after_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        settings: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type LinuxVirtualMachineScaleSet#type}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type_handler_version LinuxVirtualMachineScaleSet#type_handler_version}.
        :param automatic_upgrade_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_upgrade_enabled LinuxVirtualMachineScaleSet#automatic_upgrade_enabled}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#auto_upgrade_minor_version LinuxVirtualMachineScaleSet#auto_upgrade_minor_version}.
        :param force_update_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#force_update_tag LinuxVirtualMachineScaleSet#force_update_tag}.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#protected_settings LinuxVirtualMachineScaleSet#protected_settings}.
        :param provision_after_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_after_extensions LinuxVirtualMachineScaleSet#provision_after_extensions}.
        :param settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#settings LinuxVirtualMachineScaleSet#settings}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetExtension.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument type_handler_version", value=type_handler_version, expected_type=type_hints["type_handler_version"])
            check_type(argname="argument automatic_upgrade_enabled", value=automatic_upgrade_enabled, expected_type=type_hints["automatic_upgrade_enabled"])
            check_type(argname="argument auto_upgrade_minor_version", value=auto_upgrade_minor_version, expected_type=type_hints["auto_upgrade_minor_version"])
            check_type(argname="argument force_update_tag", value=force_update_tag, expected_type=type_hints["force_update_tag"])
            check_type(argname="argument protected_settings", value=protected_settings, expected_type=type_hints["protected_settings"])
            check_type(argname="argument provision_after_extensions", value=provision_after_extensions, expected_type=type_hints["provision_after_extensions"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "publisher": publisher,
            "type": type,
            "type_handler_version": type_handler_version,
        }
        if automatic_upgrade_enabled is not None:
            self._values["automatic_upgrade_enabled"] = automatic_upgrade_enabled
        if auto_upgrade_minor_version is not None:
            self._values["auto_upgrade_minor_version"] = auto_upgrade_minor_version
        if force_update_tag is not None:
            self._values["force_update_tag"] = force_update_tag
        if protected_settings is not None:
            self._values["protected_settings"] = protected_settings
        if provision_after_extensions is not None:
            self._values["provision_after_extensions"] = provision_after_extensions
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type LinuxVirtualMachineScaleSet#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_handler_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#type_handler_version LinuxVirtualMachineScaleSet#type_handler_version}.'''
        result = self._values.get("type_handler_version")
        assert result is not None, "Required property 'type_handler_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic_upgrade_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#automatic_upgrade_enabled LinuxVirtualMachineScaleSet#automatic_upgrade_enabled}.'''
        result = self._values.get("automatic_upgrade_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#auto_upgrade_minor_version LinuxVirtualMachineScaleSet#auto_upgrade_minor_version}.'''
        result = self._values.get("auto_upgrade_minor_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_update_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#force_update_tag LinuxVirtualMachineScaleSet#force_update_tag}.'''
        result = self._values.get("force_update_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protected_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#protected_settings LinuxVirtualMachineScaleSet#protected_settings}.'''
        result = self._values.get("protected_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_after_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#provision_after_extensions LinuxVirtualMachineScaleSet#provision_after_extensions}.'''
        result = self._values.get("provision_after_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#settings LinuxVirtualMachineScaleSet#settings}.'''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetExtension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetExtensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetExtensionList",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetExtensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetExtensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetExtensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetExtensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetExtension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetExtension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetExtension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetExtensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetExtensionOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetExtensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAutomaticUpgradeEnabled")
    def reset_automatic_upgrade_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticUpgradeEnabled", []))

    @jsii.member(jsii_name="resetAutoUpgradeMinorVersion")
    def reset_auto_upgrade_minor_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgradeMinorVersion", []))

    @jsii.member(jsii_name="resetForceUpdateTag")
    def reset_force_update_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceUpdateTag", []))

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
    @jsii.member(jsii_name="automaticUpgradeEnabledInput")
    def automatic_upgrade_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticUpgradeEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersionInput")
    def auto_upgrade_minor_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoUpgradeMinorVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="forceUpdateTagInput")
    def force_update_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forceUpdateTagInput"))

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
    @jsii.member(jsii_name="automaticUpgradeEnabled")
    def automatic_upgrade_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticUpgradeEnabled"))

    @automatic_upgrade_enabled.setter
    def automatic_upgrade_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "automatic_upgrade_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticUpgradeEnabled", value)

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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "auto_upgrade_minor_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgradeMinorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="forceUpdateTag")
    def force_update_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forceUpdateTag"))

    @force_update_tag.setter
    def force_update_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "force_update_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceUpdateTag", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protectedSettings")
    def protected_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedSettings"))

    @protected_settings.setter
    def protected_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "protected_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedSettings", value)

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensions")
    def provision_after_extensions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "provisionAfterExtensions"))

    @provision_after_extensions.setter
    def provision_after_extensions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "provision_after_extensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionAfterExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersion")
    def type_handler_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeHandlerVersion"))

    @type_handler_version.setter
    def type_handler_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "type_handler_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeHandlerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetExtension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetExtension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetExtension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetExtensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "ip_configuration": "ipConfiguration",
        "name": "name",
        "dns_servers": "dnsServers",
        "enable_ip_forwarding": "enableIpForwarding",
        "network_security_group_id": "networkSecurityGroupId",
        "primary": "primary",
    },
)
class LinuxVirtualMachineScaleSetNetworkInterface:
    def __init__(
        self,
        *,
        ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_ip_forwarding: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        network_security_group_id: typing.Optional[builtins.str] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ip_configuration LinuxVirtualMachineScaleSet#ip_configuration}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#dns_servers LinuxVirtualMachineScaleSet#dns_servers}.
        :param enable_ip_forwarding: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_ip_forwarding LinuxVirtualMachineScaleSet#enable_ip_forwarding}.
        :param network_security_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_security_group_id LinuxVirtualMachineScaleSet#network_security_group_id}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterface.__init__)
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument dns_servers", value=dns_servers, expected_type=type_hints["dns_servers"])
            check_type(argname="argument enable_ip_forwarding", value=enable_ip_forwarding, expected_type=type_hints["enable_ip_forwarding"])
            check_type(argname="argument network_security_group_id", value=network_security_group_id, expected_type=type_hints["network_security_group_id"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_configuration": ip_configuration,
            "name": name,
        }
        if dns_servers is not None:
            self._values["dns_servers"] = dns_servers
        if enable_ip_forwarding is not None:
            self._values["enable_ip_forwarding"] = enable_ip_forwarding
        if network_security_group_id is not None:
            self._values["network_security_group_id"] = network_security_group_id
        if primary is not None:
            self._values["primary"] = primary

    @builtins.property
    def ip_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#ip_configuration LinuxVirtualMachineScaleSet#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#dns_servers LinuxVirtualMachineScaleSet#dns_servers}.'''
        result = self._values.get("dns_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_ip_forwarding(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enable_ip_forwarding LinuxVirtualMachineScaleSet#enable_ip_forwarding}.'''
        result = self._values.get("enable_ip_forwarding")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def network_security_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#network_security_group_id LinuxVirtualMachineScaleSet#network_security_group_id}.'''
        result = self._values.get("network_security_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "load_balancer_backend_address_pool_ids": "loadBalancerBackendAddressPoolIds",
        "load_balancer_inbound_nat_rules_ids": "loadBalancerInboundNatRulesIds",
        "primary": "primary",
        "subnet_id": "subnetId",
        "version": "version",
    },
)
class LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        load_balancer_backend_address_pool_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        load_balancer_inbound_nat_rules_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        primary: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param load_balancer_backend_address_pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_backend_address_pool_ids LinuxVirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.
        :param load_balancer_inbound_nat_rules_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids LinuxVirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#subnet_id LinuxVirtualMachineScaleSet#subnet_id}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument load_balancer_backend_address_pool_ids", value=load_balancer_backend_address_pool_ids, expected_type=type_hints["load_balancer_backend_address_pool_ids"])
            check_type(argname="argument load_balancer_inbound_nat_rules_ids", value=load_balancer_inbound_nat_rules_ids, expected_type=type_hints["load_balancer_inbound_nat_rules_ids"])
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if load_balancer_backend_address_pool_ids is not None:
            self._values["load_balancer_backend_address_pool_ids"] = load_balancer_backend_address_pool_ids
        if load_balancer_inbound_nat_rules_ids is not None:
            self._values["load_balancer_inbound_nat_rules_ids"] = load_balancer_inbound_nat_rules_ids
        if primary is not None:
            self._values["primary"] = primary
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_backend_address_pool_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_backend_address_pool_ids LinuxVirtualMachineScaleSet#load_balancer_backend_address_pool_ids}.'''
        result = self._values.get("load_balancer_backend_address_pool_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def load_balancer_inbound_nat_rules_ids(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#load_balancer_inbound_nat_rules_ids LinuxVirtualMachineScaleSet#load_balancer_inbound_nat_rules_ids}.'''
        result = self._values.get("load_balancer_inbound_nat_rules_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def primary(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#primary LinuxVirtualMachineScaleSet#primary}.'''
        result = self._values.get("primary")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#subnet_id LinuxVirtualMachineScaleSet#subnet_id}.'''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetLoadBalancerBackendAddressPoolIds")
    def reset_load_balancer_backend_address_pool_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerBackendAddressPoolIds", []))

    @jsii.member(jsii_name="resetLoadBalancerInboundNatRulesIds")
    def reset_load_balancer_inbound_nat_rules_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerInboundNatRulesIds", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @jsii.member(jsii_name="resetSubnetId")
    def reset_subnet_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubnetId", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

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
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference, "load_balancer_backend_address_pool_ids").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference, "load_balancer_inbound_nat_rules_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerInboundNatRulesIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference.put_ip_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

    @jsii.member(jsii_name="resetDnsServers")
    def reset_dns_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServers", []))

    @jsii.member(jsii_name="resetEnableIpForwarding")
    def reset_enable_ip_forwarding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableIpForwarding", []))

    @jsii.member(jsii_name="resetNetworkSecurityGroupId")
    def reset_network_security_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkSecurityGroupId", []))

    @jsii.member(jsii_name="resetPrimary")
    def reset_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimary", []))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(
        self,
    ) -> LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList:
        return typing.cast(LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList, jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dnsServersInput")
    def dns_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsServersInput"))

    @builtins.property
    @jsii.member(jsii_name="enableIpForwardingInput")
    def enable_ip_forwarding_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableIpForwardingInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration]]], jsii.get(self, "ipConfigurationInput"))

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
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsServers"))

    @dns_servers.setter
    def dns_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference, "dns_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServers", value)

    @builtins.property
    @jsii.member(jsii_name="enableIpForwarding")
    def enable_ip_forwarding(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableIpForwarding"))

    @enable_ip_forwarding.setter
    def enable_ip_forwarding(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference, "enable_ip_forwarding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIpForwarding", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupId")
    def network_security_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkSecurityGroupId"))

    @network_security_group_id.setter
    def network_security_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference, "network_security_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSecurityGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching": "caching",
        "storage_account_type": "storageAccountType",
        "diff_disk_settings": "diffDiskSettings",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "disk_size_gb": "diskSizeGb",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class LinuxVirtualMachineScaleSetOsDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings", typing.Dict[str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#diff_disk_settings LinuxVirtualMachineScaleSet#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.
        '''
        if isinstance(diff_disk_settings, dict):
            diff_disk_settings = LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings(**diff_disk_settings)
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetOsDisk.__init__)
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument diff_disk_settings", value=diff_disk_settings, expected_type=type_hints["diff_disk_settings"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument write_accelerator_enabled", value=write_accelerator_enabled, expected_type=type_hints["write_accelerator_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "caching": caching,
            "storage_account_type": storage_account_type,
        }
        if diff_disk_settings is not None:
            self._values["diff_disk_settings"] = diff_disk_settings
        if disk_encryption_set_id is not None:
            self._values["disk_encryption_set_id"] = disk_encryption_set_id
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def caching(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#caching LinuxVirtualMachineScaleSet#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#storage_account_type LinuxVirtualMachineScaleSet#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def diff_disk_settings(
        self,
    ) -> typing.Optional["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings"]:
        '''diff_disk_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#diff_disk_settings LinuxVirtualMachineScaleSet#diff_disk_settings}
        '''
        result = self._values.get("diff_disk_settings")
        return typing.cast(typing.Optional["LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings"], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_encryption_set_id LinuxVirtualMachineScaleSet#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#disk_size_gb LinuxVirtualMachineScaleSet#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#write_accelerator_enabled LinuxVirtualMachineScaleSet#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings",
    jsii_struct_bases=[],
    name_mapping={"option": "option"},
)
class LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings:
    def __init__(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#option LinuxVirtualMachineScaleSet#option}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings.__init__)
            check_type(argname="argument option", value=option, expected_type=type_hints["option"])
        self._values: typing.Dict[str, typing.Any] = {
            "option": option,
        }

    @builtins.property
    def option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#option LinuxVirtualMachineScaleSet#option}.'''
        result = self._values.get("option")
        assert result is not None, "Required property 'option' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="optionInput")
    def option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optionInput"))

    @builtins.property
    @jsii.member(jsii_name="option")
    def option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "option"))

    @option.setter
    def option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference, "option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "option", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetOsDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetOsDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiffDiskSettings")
    def put_diff_disk_settings(self, *, option: builtins.str) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#option LinuxVirtualMachineScaleSet#option}.
        '''
        value = LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings(option=option)

        return typing.cast(None, jsii.invoke(self, "putDiffDiskSettings", [value]))

    @jsii.member(jsii_name="resetDiffDiskSettings")
    def reset_diff_disk_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiffDiskSettings", []))

    @jsii.member(jsii_name="resetDiskEncryptionSetId")
    def reset_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetWriteAcceleratorEnabled")
    def reset_write_accelerator_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcceleratorEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettings")
    def diff_disk_settings(
        self,
    ) -> LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference:
        return typing.cast(LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference, jsii.get(self, "diffDiskSettings"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettingsInput")
    def diff_disk_settings_input(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings], jsii.get(self, "diffDiskSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabledInput")
    def write_accelerator_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "writeAcceleratorEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskOutputReference, "caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskOutputReference, "disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskOutputReference, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="writeAcceleratorEnabled")
    def write_accelerator_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "writeAcceleratorEnabled"))

    @write_accelerator_enabled.setter
    def write_accelerator_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskOutputReference, "write_accelerator_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxVirtualMachineScaleSetOsDisk]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetOsDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetPlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class LinuxVirtualMachineScaleSetPlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#product LinuxVirtualMachineScaleSet#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetPlan.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#name LinuxVirtualMachineScaleSet#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#product LinuxVirtualMachineScaleSet#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetPlanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetPlanOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetPlanOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetPlanOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetPlanOutputReference, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetPlanOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LinuxVirtualMachineScaleSetPlan]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetPlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetPlan],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetPlanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecret",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "key_vault_id": "keyVaultId"},
)
class LinuxVirtualMachineScaleSetSecret:
    def __init__(
        self,
        *,
        certificate: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LinuxVirtualMachineScaleSetSecretCertificate", typing.Dict[str, typing.Any]]]],
        key_vault_id: builtins.str,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#certificate LinuxVirtualMachineScaleSet#certificate}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#key_vault_id LinuxVirtualMachineScaleSet#key_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecret.__init__)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate": certificate,
            "key_vault_id": key_vault_id,
        }

    @builtins.property
    def certificate(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecretCertificate"]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#certificate LinuxVirtualMachineScaleSet#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LinuxVirtualMachineScaleSetSecretCertificate"]], result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#key_vault_id LinuxVirtualMachineScaleSet#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretCertificate",
    jsii_struct_bases=[],
    name_mapping={},
)
class LinuxVirtualMachineScaleSetSecretCertificate:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetSecretCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetSecretCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretCertificateList",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecretCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetSecretCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecretCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetSecretCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetSecretCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretCertificateOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecretCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetSecretList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretList",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecretList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LinuxVirtualMachineScaleSetSecretOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecretList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LinuxVirtualMachineScaleSetSecretOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecret]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecret]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecret]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LinuxVirtualMachineScaleSetSecretOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSecretOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecretOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LinuxVirtualMachineScaleSetSecretCertificate, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSecretOutputReference.put_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> LinuxVirtualMachineScaleSetSecretCertificateList:
        return typing.cast(LinuxVirtualMachineScaleSetSecretCertificateList, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LinuxVirtualMachineScaleSetSecretCertificate]]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultIdInput")
    def key_vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyVaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultId")
    def key_vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyVaultId"))

    @key_vault_id.setter
    def key_vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecret, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecret, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetSecret, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSecretOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSourceImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class LinuxVirtualMachineScaleSetSourceImageReference:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#offer LinuxVirtualMachineScaleSet#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSourceImageReference.__init__)
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "offer": offer,
            "publisher": publisher,
            "sku": sku,
            "version": version,
        }

    @builtins.property
    def offer(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#offer LinuxVirtualMachineScaleSet#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#publisher LinuxVirtualMachineScaleSet#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#sku LinuxVirtualMachineScaleSet#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#version LinuxVirtualMachineScaleSet#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetSourceImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetSourceImageReference]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetSourceImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetSourceImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTerminateNotification",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "timeout": "timeout"},
)
class LinuxVirtualMachineScaleSetTerminateNotification:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeout LinuxVirtualMachineScaleSet#timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetTerminateNotification.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#enabled LinuxVirtualMachineScaleSet#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#timeout LinuxVirtualMachineScaleSet#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetTerminateNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetTerminateNotificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTerminateNotificationOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetTerminateNotificationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTerminateNotificationOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTerminateNotificationOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LinuxVirtualMachineScaleSetTerminateNotification]:
        return typing.cast(typing.Optional[LinuxVirtualMachineScaleSetTerminateNotification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LinuxVirtualMachineScaleSetTerminateNotification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTerminateNotificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LinuxVirtualMachineScaleSetTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create LinuxVirtualMachineScaleSet#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#delete LinuxVirtualMachineScaleSet#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#read LinuxVirtualMachineScaleSet#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#update LinuxVirtualMachineScaleSet#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#create LinuxVirtualMachineScaleSet#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#delete LinuxVirtualMachineScaleSet#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#read LinuxVirtualMachineScaleSet#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurestack/r/linux_virtual_machine_scale_set#update LinuxVirtualMachineScaleSet#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinuxVirtualMachineScaleSetTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LinuxVirtualMachineScaleSetTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurestack.linuxVirtualMachineScaleSet.LinuxVirtualMachineScaleSetTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LinuxVirtualMachineScaleSetTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LinuxVirtualMachineScaleSetTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LinuxVirtualMachineScaleSetTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LinuxVirtualMachineScaleSet",
    "LinuxVirtualMachineScaleSetAdditionalCapabilities",
    "LinuxVirtualMachineScaleSetAdditionalCapabilitiesOutputReference",
    "LinuxVirtualMachineScaleSetAdminSshKey",
    "LinuxVirtualMachineScaleSetAdminSshKeyList",
    "LinuxVirtualMachineScaleSetAdminSshKeyOutputReference",
    "LinuxVirtualMachineScaleSetAutomaticInstanceRepair",
    "LinuxVirtualMachineScaleSetAutomaticInstanceRepairOutputReference",
    "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicy",
    "LinuxVirtualMachineScaleSetAutomaticOsUpgradePolicyOutputReference",
    "LinuxVirtualMachineScaleSetBootDiagnostics",
    "LinuxVirtualMachineScaleSetBootDiagnosticsOutputReference",
    "LinuxVirtualMachineScaleSetConfig",
    "LinuxVirtualMachineScaleSetDataDisk",
    "LinuxVirtualMachineScaleSetDataDiskList",
    "LinuxVirtualMachineScaleSetDataDiskOutputReference",
    "LinuxVirtualMachineScaleSetExtension",
    "LinuxVirtualMachineScaleSetExtensionList",
    "LinuxVirtualMachineScaleSetExtensionOutputReference",
    "LinuxVirtualMachineScaleSetNetworkInterface",
    "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfiguration",
    "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationList",
    "LinuxVirtualMachineScaleSetNetworkInterfaceIpConfigurationOutputReference",
    "LinuxVirtualMachineScaleSetNetworkInterfaceList",
    "LinuxVirtualMachineScaleSetNetworkInterfaceOutputReference",
    "LinuxVirtualMachineScaleSetOsDisk",
    "LinuxVirtualMachineScaleSetOsDiskDiffDiskSettings",
    "LinuxVirtualMachineScaleSetOsDiskDiffDiskSettingsOutputReference",
    "LinuxVirtualMachineScaleSetOsDiskOutputReference",
    "LinuxVirtualMachineScaleSetPlan",
    "LinuxVirtualMachineScaleSetPlanOutputReference",
    "LinuxVirtualMachineScaleSetSecret",
    "LinuxVirtualMachineScaleSetSecretCertificate",
    "LinuxVirtualMachineScaleSetSecretCertificateList",
    "LinuxVirtualMachineScaleSetSecretCertificateOutputReference",
    "LinuxVirtualMachineScaleSetSecretList",
    "LinuxVirtualMachineScaleSetSecretOutputReference",
    "LinuxVirtualMachineScaleSetSourceImageReference",
    "LinuxVirtualMachineScaleSetSourceImageReferenceOutputReference",
    "LinuxVirtualMachineScaleSetTerminateNotification",
    "LinuxVirtualMachineScaleSetTerminateNotificationOutputReference",
    "LinuxVirtualMachineScaleSetTimeouts",
    "LinuxVirtualMachineScaleSetTimeoutsOutputReference",
]

publication.publish()
