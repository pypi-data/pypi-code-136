'''
# `azurerm_windows_virtual_machine`

Refer to the Terraform Registory for docs: [`azurerm_windows_virtual_machine`](https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine).
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


class WindowsVirtualMachine(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachine",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine azurerm_windows_virtual_machine}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        admin_password: builtins.str,
        admin_username: builtins.str,
        location: builtins.str,
        name: builtins.str,
        network_interface_ids: typing.Sequence[builtins.str],
        os_disk: typing.Union["WindowsVirtualMachineOsDisk", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        size: builtins.str,
        additional_capabilities: typing.Optional[typing.Union["WindowsVirtualMachineAdditionalCapabilities", typing.Dict[str, typing.Any]]] = None,
        additional_unattend_content: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineAdditionalUnattendContent", typing.Dict[str, typing.Any]]]]] = None,
        allow_extension_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union["WindowsVirtualMachineBootDiagnostics", typing.Dict[str, typing.Any]]] = None,
        capacity_reservation_group_id: typing.Optional[builtins.str] = None,
        computer_name: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        dedicated_host_group_id: typing.Optional[builtins.str] = None,
        dedicated_host_id: typing.Optional[builtins.str] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extensions_time_budget: typing.Optional[builtins.str] = None,
        gallery_application: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineGalleryApplication", typing.Dict[str, typing.Any]]]]] = None,
        hotpatching_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["WindowsVirtualMachineIdentity", typing.Dict[str, typing.Any]]] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_bid_price: typing.Optional[jsii.Number] = None,
        patch_assessment_mode: typing.Optional[builtins.str] = None,
        patch_mode: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union["WindowsVirtualMachinePlan", typing.Dict[str, typing.Any]]] = None,
        platform_fault_domain: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[builtins.str] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        proximity_placement_group_id: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecret", typing.Dict[str, typing.Any]]]]] = None,
        secure_boot_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["WindowsVirtualMachineSourceImageReference", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_notification: typing.Optional[typing.Union["WindowsVirtualMachineTerminationNotification", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", typing.Dict[str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
        virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
        vtpm_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm_listener: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineWinrmListener", typing.Dict[str, typing.Any]]]]] = None,
        zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine azurerm_windows_virtual_machine} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#admin_password WindowsVirtualMachine#admin_password}.
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#admin_username WindowsVirtualMachine#admin_username}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#location WindowsVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#network_interface_ids WindowsVirtualMachine#network_interface_ids}.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#os_disk WindowsVirtualMachine#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#resource_group_name WindowsVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#size WindowsVirtualMachine#size}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#additional_capabilities WindowsVirtualMachine#additional_capabilities}
        :param additional_unattend_content: additional_unattend_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#additional_unattend_content WindowsVirtualMachine#additional_unattend_content}
        :param allow_extension_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#allow_extension_operations WindowsVirtualMachine#allow_extension_operations}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#availability_set_id WindowsVirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#boot_diagnostics WindowsVirtualMachine#boot_diagnostics}
        :param capacity_reservation_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#capacity_reservation_group_id WindowsVirtualMachine#capacity_reservation_group_id}.
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#computer_name WindowsVirtualMachine#computer_name}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#custom_data WindowsVirtualMachine#custom_data}.
        :param dedicated_host_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#dedicated_host_group_id WindowsVirtualMachine#dedicated_host_group_id}.
        :param dedicated_host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#dedicated_host_id WindowsVirtualMachine#dedicated_host_id}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#edge_zone WindowsVirtualMachine#edge_zone}.
        :param enable_automatic_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#enable_automatic_updates WindowsVirtualMachine#enable_automatic_updates}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#encryption_at_host_enabled WindowsVirtualMachine#encryption_at_host_enabled}.
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#eviction_policy WindowsVirtualMachine#eviction_policy}.
        :param extensions_time_budget: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#extensions_time_budget WindowsVirtualMachine#extensions_time_budget}.
        :param gallery_application: gallery_application block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#gallery_application WindowsVirtualMachine#gallery_application}
        :param hotpatching_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#hotpatching_enabled WindowsVirtualMachine#hotpatching_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#id WindowsVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#identity WindowsVirtualMachine#identity}
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#license_type WindowsVirtualMachine#license_type}.
        :param max_bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#max_bid_price WindowsVirtualMachine#max_bid_price}.
        :param patch_assessment_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#patch_assessment_mode WindowsVirtualMachine#patch_assessment_mode}.
        :param patch_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#patch_mode WindowsVirtualMachine#patch_mode}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#plan WindowsVirtualMachine#plan}
        :param platform_fault_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#platform_fault_domain WindowsVirtualMachine#platform_fault_domain}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#priority WindowsVirtualMachine#priority}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#provision_vm_agent WindowsVirtualMachine#provision_vm_agent}.
        :param proximity_placement_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#proximity_placement_group_id WindowsVirtualMachine#proximity_placement_group_id}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secret WindowsVirtualMachine#secret}
        :param secure_boot_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secure_boot_enabled WindowsVirtualMachine#secure_boot_enabled}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#source_image_id WindowsVirtualMachine#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#source_image_reference WindowsVirtualMachine#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#tags WindowsVirtualMachine#tags}.
        :param termination_notification: termination_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#termination_notification WindowsVirtualMachine#termination_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timeouts WindowsVirtualMachine#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timezone WindowsVirtualMachine#timezone}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#user_data WindowsVirtualMachine#user_data}.
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#virtual_machine_scale_set_id WindowsVirtualMachine#virtual_machine_scale_set_id}.
        :param vtpm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#vtpm_enabled WindowsVirtualMachine#vtpm_enabled}.
        :param winrm_listener: winrm_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#winrm_listener WindowsVirtualMachine#winrm_listener}
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#zone WindowsVirtualMachine#zone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachine.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WindowsVirtualMachineConfig(
            admin_password=admin_password,
            admin_username=admin_username,
            location=location,
            name=name,
            network_interface_ids=network_interface_ids,
            os_disk=os_disk,
            resource_group_name=resource_group_name,
            size=size,
            additional_capabilities=additional_capabilities,
            additional_unattend_content=additional_unattend_content,
            allow_extension_operations=allow_extension_operations,
            availability_set_id=availability_set_id,
            boot_diagnostics=boot_diagnostics,
            capacity_reservation_group_id=capacity_reservation_group_id,
            computer_name=computer_name,
            custom_data=custom_data,
            dedicated_host_group_id=dedicated_host_group_id,
            dedicated_host_id=dedicated_host_id,
            edge_zone=edge_zone,
            enable_automatic_updates=enable_automatic_updates,
            encryption_at_host_enabled=encryption_at_host_enabled,
            eviction_policy=eviction_policy,
            extensions_time_budget=extensions_time_budget,
            gallery_application=gallery_application,
            hotpatching_enabled=hotpatching_enabled,
            id=id,
            identity=identity,
            license_type=license_type,
            max_bid_price=max_bid_price,
            patch_assessment_mode=patch_assessment_mode,
            patch_mode=patch_mode,
            plan=plan,
            platform_fault_domain=platform_fault_domain,
            priority=priority,
            provision_vm_agent=provision_vm_agent,
            proximity_placement_group_id=proximity_placement_group_id,
            secret=secret,
            secure_boot_enabled=secure_boot_enabled,
            source_image_id=source_image_id,
            source_image_reference=source_image_reference,
            tags=tags,
            termination_notification=termination_notification,
            timeouts=timeouts,
            timezone=timezone,
            user_data=user_data,
            virtual_machine_scale_set_id=virtual_machine_scale_set_id,
            vtpm_enabled=vtpm_enabled,
            winrm_listener=winrm_listener,
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

    @jsii.member(jsii_name="putAdditionalCapabilities")
    def put_additional_capabilities(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#ultra_ssd_enabled WindowsVirtualMachine#ultra_ssd_enabled}.
        '''
        value = WindowsVirtualMachineAdditionalCapabilities(
            ultra_ssd_enabled=ultra_ssd_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putAdditionalCapabilities", [value]))

    @jsii.member(jsii_name="putAdditionalUnattendContent")
    def put_additional_unattend_content(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineAdditionalUnattendContent", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachine.put_additional_unattend_content)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdditionalUnattendContent", [value]))

    @jsii.member(jsii_name="putBootDiagnostics")
    def put_boot_diagnostics(
        self,
        *,
        storage_account_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#storage_account_uri WindowsVirtualMachine#storage_account_uri}.
        '''
        value = WindowsVirtualMachineBootDiagnostics(
            storage_account_uri=storage_account_uri
        )

        return typing.cast(None, jsii.invoke(self, "putBootDiagnostics", [value]))

    @jsii.member(jsii_name="putGalleryApplication")
    def put_gallery_application(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineGalleryApplication", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachine.put_gallery_application)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGalleryApplication", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#type WindowsVirtualMachine#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#identity_ids WindowsVirtualMachine#identity_ids}.
        '''
        value = WindowsVirtualMachineIdentity(type=type, identity_ids=identity_ids)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putOsDisk")
    def put_os_disk(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["WindowsVirtualMachineOsDiskDiffDiskSettings", typing.Dict[str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        secure_vm_disk_encryption_set_id: typing.Optional[builtins.str] = None,
        security_encryption_type: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#caching WindowsVirtualMachine#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#storage_account_type WindowsVirtualMachine#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#diff_disk_settings WindowsVirtualMachine#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#disk_encryption_set_id WindowsVirtualMachine#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#disk_size_gb WindowsVirtualMachine#disk_size_gb}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param secure_vm_disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secure_vm_disk_encryption_set_id WindowsVirtualMachine#secure_vm_disk_encryption_set_id}.
        :param security_encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#security_encryption_type WindowsVirtualMachine#security_encryption_type}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#write_accelerator_enabled WindowsVirtualMachine#write_accelerator_enabled}.
        '''
        value = WindowsVirtualMachineOsDisk(
            caching=caching,
            storage_account_type=storage_account_type,
            diff_disk_settings=diff_disk_settings,
            disk_encryption_set_id=disk_encryption_set_id,
            disk_size_gb=disk_size_gb,
            name=name,
            secure_vm_disk_encryption_set_id=secure_vm_disk_encryption_set_id,
            security_encryption_type=security_encryption_type,
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
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#product WindowsVirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        '''
        value = WindowsVirtualMachinePlan(
            name=name, product=product, publisher=publisher
        )

        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putSecret")
    def put_secret(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecret", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachine.put_secret)
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
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#offer WindowsVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#sku WindowsVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#version WindowsVirtualMachine#version}.
        '''
        value = WindowsVirtualMachineSourceImageReference(
            offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putSourceImageReference", [value]))

    @jsii.member(jsii_name="putTerminationNotification")
    def put_termination_notification(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#enabled WindowsVirtualMachine#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timeout WindowsVirtualMachine#timeout}.
        '''
        value = WindowsVirtualMachineTerminationNotification(
            enabled=enabled, timeout=timeout
        )

        return typing.cast(None, jsii.invoke(self, "putTerminationNotification", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#create WindowsVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#delete WindowsVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#read WindowsVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#update WindowsVirtualMachine#update}.
        '''
        value = WindowsVirtualMachineTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWinrmListener")
    def put_winrm_listener(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineWinrmListener", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachine.put_winrm_listener)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWinrmListener", [value]))

    @jsii.member(jsii_name="resetAdditionalCapabilities")
    def reset_additional_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalCapabilities", []))

    @jsii.member(jsii_name="resetAdditionalUnattendContent")
    def reset_additional_unattend_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalUnattendContent", []))

    @jsii.member(jsii_name="resetAllowExtensionOperations")
    def reset_allow_extension_operations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowExtensionOperations", []))

    @jsii.member(jsii_name="resetAvailabilitySetId")
    def reset_availability_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailabilitySetId", []))

    @jsii.member(jsii_name="resetBootDiagnostics")
    def reset_boot_diagnostics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootDiagnostics", []))

    @jsii.member(jsii_name="resetCapacityReservationGroupId")
    def reset_capacity_reservation_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCapacityReservationGroupId", []))

    @jsii.member(jsii_name="resetComputerName")
    def reset_computer_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComputerName", []))

    @jsii.member(jsii_name="resetCustomData")
    def reset_custom_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomData", []))

    @jsii.member(jsii_name="resetDedicatedHostGroupId")
    def reset_dedicated_host_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedHostGroupId", []))

    @jsii.member(jsii_name="resetDedicatedHostId")
    def reset_dedicated_host_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDedicatedHostId", []))

    @jsii.member(jsii_name="resetEdgeZone")
    def reset_edge_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeZone", []))

    @jsii.member(jsii_name="resetEnableAutomaticUpdates")
    def reset_enable_automatic_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticUpdates", []))

    @jsii.member(jsii_name="resetEncryptionAtHostEnabled")
    def reset_encryption_at_host_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionAtHostEnabled", []))

    @jsii.member(jsii_name="resetEvictionPolicy")
    def reset_eviction_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvictionPolicy", []))

    @jsii.member(jsii_name="resetExtensionsTimeBudget")
    def reset_extensions_time_budget(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtensionsTimeBudget", []))

    @jsii.member(jsii_name="resetGalleryApplication")
    def reset_gallery_application(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGalleryApplication", []))

    @jsii.member(jsii_name="resetHotpatchingEnabled")
    def reset_hotpatching_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHotpatchingEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetMaxBidPrice")
    def reset_max_bid_price(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBidPrice", []))

    @jsii.member(jsii_name="resetPatchAssessmentMode")
    def reset_patch_assessment_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPatchAssessmentMode", []))

    @jsii.member(jsii_name="resetPatchMode")
    def reset_patch_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPatchMode", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetPlatformFaultDomain")
    def reset_platform_fault_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatformFaultDomain", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProvisionVmAgent")
    def reset_provision_vm_agent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionVmAgent", []))

    @jsii.member(jsii_name="resetProximityPlacementGroupId")
    def reset_proximity_placement_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProximityPlacementGroupId", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetSecureBootEnabled")
    def reset_secure_boot_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureBootEnabled", []))

    @jsii.member(jsii_name="resetSourceImageId")
    def reset_source_image_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageId", []))

    @jsii.member(jsii_name="resetSourceImageReference")
    def reset_source_image_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceImageReference", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTerminationNotification")
    def reset_termination_notification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationNotification", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetUserData")
    def reset_user_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserData", []))

    @jsii.member(jsii_name="resetVirtualMachineScaleSetId")
    def reset_virtual_machine_scale_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVirtualMachineScaleSetId", []))

    @jsii.member(jsii_name="resetVtpmEnabled")
    def reset_vtpm_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVtpmEnabled", []))

    @jsii.member(jsii_name="resetWinrmListener")
    def reset_winrm_listener(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWinrmListener", []))

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
    @jsii.member(jsii_name="additionalCapabilities")
    def additional_capabilities(
        self,
    ) -> "WindowsVirtualMachineAdditionalCapabilitiesOutputReference":
        return typing.cast("WindowsVirtualMachineAdditionalCapabilitiesOutputReference", jsii.get(self, "additionalCapabilities"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendContent")
    def additional_unattend_content(
        self,
    ) -> "WindowsVirtualMachineAdditionalUnattendContentList":
        return typing.cast("WindowsVirtualMachineAdditionalUnattendContentList", jsii.get(self, "additionalUnattendContent"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnostics")
    def boot_diagnostics(self) -> "WindowsVirtualMachineBootDiagnosticsOutputReference":
        return typing.cast("WindowsVirtualMachineBootDiagnosticsOutputReference", jsii.get(self, "bootDiagnostics"))

    @builtins.property
    @jsii.member(jsii_name="galleryApplication")
    def gallery_application(self) -> "WindowsVirtualMachineGalleryApplicationList":
        return typing.cast("WindowsVirtualMachineGalleryApplicationList", jsii.get(self, "galleryApplication"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "WindowsVirtualMachineIdentityOutputReference":
        return typing.cast("WindowsVirtualMachineIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="osDisk")
    def os_disk(self) -> "WindowsVirtualMachineOsDiskOutputReference":
        return typing.cast("WindowsVirtualMachineOsDiskOutputReference", jsii.get(self, "osDisk"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "WindowsVirtualMachinePlanOutputReference":
        return typing.cast("WindowsVirtualMachinePlanOutputReference", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddress")
    def private_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddresses")
    def private_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "privateIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddress")
    def public_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddresses")
    def public_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publicIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> "WindowsVirtualMachineSecretList":
        return typing.cast("WindowsVirtualMachineSecretList", jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReference")
    def source_image_reference(
        self,
    ) -> "WindowsVirtualMachineSourceImageReferenceOutputReference":
        return typing.cast("WindowsVirtualMachineSourceImageReferenceOutputReference", jsii.get(self, "sourceImageReference"))

    @builtins.property
    @jsii.member(jsii_name="terminationNotification")
    def termination_notification(
        self,
    ) -> "WindowsVirtualMachineTerminationNotificationOutputReference":
        return typing.cast("WindowsVirtualMachineTerminationNotificationOutputReference", jsii.get(self, "terminationNotification"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "WindowsVirtualMachineTimeoutsOutputReference":
        return typing.cast("WindowsVirtualMachineTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineId")
    def virtual_machine_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineId"))

    @builtins.property
    @jsii.member(jsii_name="winrmListener")
    def winrm_listener(self) -> "WindowsVirtualMachineWinrmListenerList":
        return typing.cast("WindowsVirtualMachineWinrmListenerList", jsii.get(self, "winrmListener"))

    @builtins.property
    @jsii.member(jsii_name="additionalCapabilitiesInput")
    def additional_capabilities_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineAdditionalCapabilities"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineAdditionalCapabilities"], jsii.get(self, "additionalCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalUnattendContentInput")
    def additional_unattend_content_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineAdditionalUnattendContent"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineAdditionalUnattendContent"]]], jsii.get(self, "additionalUnattendContentInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPasswordInput")
    def admin_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUsernameInput")
    def admin_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="allowExtensionOperationsInput")
    def allow_extension_operations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowExtensionOperationsInput"))

    @builtins.property
    @jsii.member(jsii_name="availabilitySetIdInput")
    def availability_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilitySetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bootDiagnosticsInput")
    def boot_diagnostics_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineBootDiagnostics"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineBootDiagnostics"], jsii.get(self, "bootDiagnosticsInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityReservationGroupIdInput")
    def capacity_reservation_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "capacityReservationGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="computerNameInput")
    def computer_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="customDataInput")
    def custom_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customDataInput"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedHostGroupIdInput")
    def dedicated_host_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dedicatedHostGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dedicatedHostIdInput")
    def dedicated_host_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dedicatedHostIdInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeZoneInput")
    def edge_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpdatesInput")
    def enable_automatic_updates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutomaticUpdatesInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAtHostEnabledInput")
    def encryption_at_host_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "encryptionAtHostEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="evictionPolicyInput")
    def eviction_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evictionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionsTimeBudgetInput")
    def extensions_time_budget_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extensionsTimeBudgetInput"))

    @builtins.property
    @jsii.member(jsii_name="galleryApplicationInput")
    def gallery_application_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineGalleryApplication"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineGalleryApplication"]]], jsii.get(self, "galleryApplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="hotpatchingEnabledInput")
    def hotpatching_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hotpatchingEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["WindowsVirtualMachineIdentity"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineIdentity"], jsii.get(self, "identityInput"))

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
    @jsii.member(jsii_name="maxBidPriceInput")
    def max_bid_price_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBidPriceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIdsInput")
    def network_interface_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "networkInterfaceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskInput")
    def os_disk_input(self) -> typing.Optional["WindowsVirtualMachineOsDisk"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineOsDisk"], jsii.get(self, "osDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="patchAssessmentModeInput")
    def patch_assessment_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patchAssessmentModeInput"))

    @builtins.property
    @jsii.member(jsii_name="patchModeInput")
    def patch_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patchModeInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(self) -> typing.Optional["WindowsVirtualMachinePlan"]:
        return typing.cast(typing.Optional["WindowsVirtualMachinePlan"], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="platformFaultDomainInput")
    def platform_fault_domain_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "platformFaultDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionVmAgentInput")
    def provision_vm_agent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "provisionVmAgentInput"))

    @builtins.property
    @jsii.member(jsii_name="proximityPlacementGroupIdInput")
    def proximity_placement_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proximityPlacementGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineSecret"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineSecret"]]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="secureBootEnabledInput")
    def secure_boot_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "secureBootEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageIdInput")
    def source_image_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceImageIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceImageReferenceInput")
    def source_image_reference_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineSourceImageReference"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineSourceImageReference"], jsii.get(self, "sourceImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationNotificationInput")
    def termination_notification_input(
        self,
    ) -> typing.Optional["WindowsVirtualMachineTerminationNotification"]:
        return typing.cast(typing.Optional["WindowsVirtualMachineTerminationNotification"], jsii.get(self, "terminationNotificationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="userDataInput")
    def user_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userDataInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetIdInput")
    def virtual_machine_scale_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualMachineScaleSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vtpmEnabledInput")
    def vtpm_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "vtpmEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="winrmListenerInput")
    def winrm_listener_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]], jsii.get(self, "winrmListenerInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="adminPassword")
    def admin_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminPassword"))

    @admin_password.setter
    def admin_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "admin_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminPassword", value)

    @builtins.property
    @jsii.member(jsii_name="adminUsername")
    def admin_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUsername"))

    @admin_username.setter
    def admin_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "admin_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUsername", value)

    @builtins.property
    @jsii.member(jsii_name="allowExtensionOperations")
    def allow_extension_operations(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowExtensionOperations"))

    @allow_extension_operations.setter
    def allow_extension_operations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "allow_extension_operations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowExtensionOperations", value)

    @builtins.property
    @jsii.member(jsii_name="availabilitySetId")
    def availability_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilitySetId"))

    @availability_set_id.setter
    def availability_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "availability_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilitySetId", value)

    @builtins.property
    @jsii.member(jsii_name="capacityReservationGroupId")
    def capacity_reservation_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "capacityReservationGroupId"))

    @capacity_reservation_group_id.setter
    def capacity_reservation_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "capacity_reservation_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacityReservationGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="computerName")
    def computer_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computerName"))

    @computer_name.setter
    def computer_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "computer_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computerName", value)

    @builtins.property
    @jsii.member(jsii_name="customData")
    def custom_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customData"))

    @custom_data.setter
    def custom_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "custom_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customData", value)

    @builtins.property
    @jsii.member(jsii_name="dedicatedHostGroupId")
    def dedicated_host_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dedicatedHostGroupId"))

    @dedicated_host_group_id.setter
    def dedicated_host_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "dedicated_host_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedHostGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="dedicatedHostId")
    def dedicated_host_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dedicatedHostId"))

    @dedicated_host_id.setter
    def dedicated_host_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "dedicated_host_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dedicatedHostId", value)

    @builtins.property
    @jsii.member(jsii_name="edgeZone")
    def edge_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeZone"))

    @edge_zone.setter
    def edge_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "edge_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeZone", value)

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpdates")
    def enable_automatic_updates(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutomaticUpdates"))

    @enable_automatic_updates.setter
    def enable_automatic_updates(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "enable_automatic_updates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticUpdates", value)

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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "encryption_at_host_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAtHostEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="evictionPolicy")
    def eviction_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evictionPolicy"))

    @eviction_policy.setter
    def eviction_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "eviction_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evictionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="extensionsTimeBudget")
    def extensions_time_budget(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extensionsTimeBudget"))

    @extensions_time_budget.setter
    def extensions_time_budget(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "extensions_time_budget").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extensionsTimeBudget", value)

    @builtins.property
    @jsii.member(jsii_name="hotpatchingEnabled")
    def hotpatching_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hotpatchingEnabled"))

    @hotpatching_enabled.setter
    def hotpatching_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "hotpatching_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hotpatchingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "license_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="maxBidPrice")
    def max_bid_price(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBidPrice"))

    @max_bid_price.setter
    def max_bid_price(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "max_bid_price").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBidPrice", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceIds")
    def network_interface_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "networkInterfaceIds"))

    @network_interface_ids.setter
    def network_interface_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "network_interface_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaceIds", value)

    @builtins.property
    @jsii.member(jsii_name="patchAssessmentMode")
    def patch_assessment_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "patchAssessmentMode"))

    @patch_assessment_mode.setter
    def patch_assessment_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "patch_assessment_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patchAssessmentMode", value)

    @builtins.property
    @jsii.member(jsii_name="patchMode")
    def patch_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "patchMode"))

    @patch_mode.setter
    def patch_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "patch_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patchMode", value)

    @builtins.property
    @jsii.member(jsii_name="platformFaultDomain")
    def platform_fault_domain(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "platformFaultDomain"))

    @platform_fault_domain.setter
    def platform_fault_domain(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "platform_fault_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformFaultDomain", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "provision_vm_agent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionVmAgent", value)

    @builtins.property
    @jsii.member(jsii_name="proximityPlacementGroupId")
    def proximity_placement_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proximityPlacementGroupId"))

    @proximity_placement_group_id.setter
    def proximity_placement_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "proximity_placement_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proximityPlacementGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="secureBootEnabled")
    def secure_boot_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "secureBootEnabled"))

    @secure_boot_enabled.setter
    def secure_boot_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "secure_boot_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureBootEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sourceImageId")
    def source_image_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceImageId"))

    @source_image_id.setter
    def source_image_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "source_image_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceImageId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userData"))

    @user_data.setter
    def user_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "user_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userData", value)

    @builtins.property
    @jsii.member(jsii_name="virtualMachineScaleSetId")
    def virtual_machine_scale_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualMachineScaleSetId"))

    @virtual_machine_scale_set_id.setter
    def virtual_machine_scale_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "virtual_machine_scale_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualMachineScaleSetId", value)

    @builtins.property
    @jsii.member(jsii_name="vtpmEnabled")
    def vtpm_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "vtpmEnabled"))

    @vtpm_enabled.setter
    def vtpm_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "vtpm_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vtpmEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachine, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineAdditionalCapabilities",
    jsii_struct_bases=[],
    name_mapping={"ultra_ssd_enabled": "ultraSsdEnabled"},
)
class WindowsVirtualMachineAdditionalCapabilities:
    def __init__(
        self,
        *,
        ultra_ssd_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param ultra_ssd_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#ultra_ssd_enabled WindowsVirtualMachine#ultra_ssd_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineAdditionalCapabilities.__init__)
            check_type(argname="argument ultra_ssd_enabled", value=ultra_ssd_enabled, expected_type=type_hints["ultra_ssd_enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ultra_ssd_enabled is not None:
            self._values["ultra_ssd_enabled"] = ultra_ssd_enabled

    @builtins.property
    def ultra_ssd_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#ultra_ssd_enabled WindowsVirtualMachine#ultra_ssd_enabled}.'''
        result = self._values.get("ultra_ssd_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineAdditionalCapabilities(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineAdditionalCapabilitiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineAdditionalCapabilitiesOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineAdditionalCapabilitiesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalCapabilitiesOutputReference, "ultra_ssd_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ultraSsdEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineAdditionalCapabilities]:
        return typing.cast(typing.Optional[WindowsVirtualMachineAdditionalCapabilities], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineAdditionalCapabilities],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalCapabilitiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineAdditionalUnattendContent",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "setting": "setting"},
)
class WindowsVirtualMachineAdditionalUnattendContent:
    def __init__(self, *, content: builtins.str, setting: builtins.str) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#content WindowsVirtualMachine#content}.
        :param setting: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#setting WindowsVirtualMachine#setting}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineAdditionalUnattendContent.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument setting", value=setting, expected_type=type_hints["setting"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "setting": setting,
        }

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#content WindowsVirtualMachine#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def setting(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#setting WindowsVirtualMachine#setting}.'''
        result = self._values.get("setting")
        assert result is not None, "Required property 'setting' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineAdditionalUnattendContent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineAdditionalUnattendContentList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineAdditionalUnattendContentList",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineAdditionalUnattendContentList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineAdditionalUnattendContentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineAdditionalUnattendContentList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineAdditionalUnattendContentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalUnattendContentList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalUnattendContentList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalUnattendContentList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalUnattendContentList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineAdditionalUnattendContentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineAdditionalUnattendContentOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineAdditionalUnattendContentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="settingInput")
    def setting_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalUnattendContentOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="setting")
    def setting(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setting"))

    @setting.setter
    def setting(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalUnattendContentOutputReference, "setting").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setting", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineAdditionalUnattendContentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineBootDiagnostics",
    jsii_struct_bases=[],
    name_mapping={"storage_account_uri": "storageAccountUri"},
)
class WindowsVirtualMachineBootDiagnostics:
    def __init__(
        self,
        *,
        storage_account_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storage_account_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#storage_account_uri WindowsVirtualMachine#storage_account_uri}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineBootDiagnostics.__init__)
            check_type(argname="argument storage_account_uri", value=storage_account_uri, expected_type=type_hints["storage_account_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if storage_account_uri is not None:
            self._values["storage_account_uri"] = storage_account_uri

    @builtins.property
    def storage_account_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#storage_account_uri WindowsVirtualMachine#storage_account_uri}.'''
        result = self._values.get("storage_account_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineBootDiagnostics(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineBootDiagnosticsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineBootDiagnosticsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineBootDiagnosticsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStorageAccountUri")
    def reset_storage_account_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountUri", []))

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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineBootDiagnosticsOutputReference, "storage_account_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachineBootDiagnostics]:
        return typing.cast(typing.Optional[WindowsVirtualMachineBootDiagnostics], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineBootDiagnostics],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineBootDiagnosticsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "admin_password": "adminPassword",
        "admin_username": "adminUsername",
        "location": "location",
        "name": "name",
        "network_interface_ids": "networkInterfaceIds",
        "os_disk": "osDisk",
        "resource_group_name": "resourceGroupName",
        "size": "size",
        "additional_capabilities": "additionalCapabilities",
        "additional_unattend_content": "additionalUnattendContent",
        "allow_extension_operations": "allowExtensionOperations",
        "availability_set_id": "availabilitySetId",
        "boot_diagnostics": "bootDiagnostics",
        "capacity_reservation_group_id": "capacityReservationGroupId",
        "computer_name": "computerName",
        "custom_data": "customData",
        "dedicated_host_group_id": "dedicatedHostGroupId",
        "dedicated_host_id": "dedicatedHostId",
        "edge_zone": "edgeZone",
        "enable_automatic_updates": "enableAutomaticUpdates",
        "encryption_at_host_enabled": "encryptionAtHostEnabled",
        "eviction_policy": "evictionPolicy",
        "extensions_time_budget": "extensionsTimeBudget",
        "gallery_application": "galleryApplication",
        "hotpatching_enabled": "hotpatchingEnabled",
        "id": "id",
        "identity": "identity",
        "license_type": "licenseType",
        "max_bid_price": "maxBidPrice",
        "patch_assessment_mode": "patchAssessmentMode",
        "patch_mode": "patchMode",
        "plan": "plan",
        "platform_fault_domain": "platformFaultDomain",
        "priority": "priority",
        "provision_vm_agent": "provisionVmAgent",
        "proximity_placement_group_id": "proximityPlacementGroupId",
        "secret": "secret",
        "secure_boot_enabled": "secureBootEnabled",
        "source_image_id": "sourceImageId",
        "source_image_reference": "sourceImageReference",
        "tags": "tags",
        "termination_notification": "terminationNotification",
        "timeouts": "timeouts",
        "timezone": "timezone",
        "user_data": "userData",
        "virtual_machine_scale_set_id": "virtualMachineScaleSetId",
        "vtpm_enabled": "vtpmEnabled",
        "winrm_listener": "winrmListener",
        "zone": "zone",
    },
)
class WindowsVirtualMachineConfig(cdktf.TerraformMetaArguments):
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
        admin_password: builtins.str,
        admin_username: builtins.str,
        location: builtins.str,
        name: builtins.str,
        network_interface_ids: typing.Sequence[builtins.str],
        os_disk: typing.Union["WindowsVirtualMachineOsDisk", typing.Dict[str, typing.Any]],
        resource_group_name: builtins.str,
        size: builtins.str,
        additional_capabilities: typing.Optional[typing.Union[WindowsVirtualMachineAdditionalCapabilities, typing.Dict[str, typing.Any]]] = None,
        additional_unattend_content: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineAdditionalUnattendContent, typing.Dict[str, typing.Any]]]]] = None,
        allow_extension_operations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        availability_set_id: typing.Optional[builtins.str] = None,
        boot_diagnostics: typing.Optional[typing.Union[WindowsVirtualMachineBootDiagnostics, typing.Dict[str, typing.Any]]] = None,
        capacity_reservation_group_id: typing.Optional[builtins.str] = None,
        computer_name: typing.Optional[builtins.str] = None,
        custom_data: typing.Optional[builtins.str] = None,
        dedicated_host_group_id: typing.Optional[builtins.str] = None,
        dedicated_host_id: typing.Optional[builtins.str] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption_at_host_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        eviction_policy: typing.Optional[builtins.str] = None,
        extensions_time_budget: typing.Optional[builtins.str] = None,
        gallery_application: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineGalleryApplication", typing.Dict[str, typing.Any]]]]] = None,
        hotpatching_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["WindowsVirtualMachineIdentity", typing.Dict[str, typing.Any]]] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_bid_price: typing.Optional[jsii.Number] = None,
        patch_assessment_mode: typing.Optional[builtins.str] = None,
        patch_mode: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union["WindowsVirtualMachinePlan", typing.Dict[str, typing.Any]]] = None,
        platform_fault_domain: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[builtins.str] = None,
        provision_vm_agent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        proximity_placement_group_id: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecret", typing.Dict[str, typing.Any]]]]] = None,
        secure_boot_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_image_id: typing.Optional[builtins.str] = None,
        source_image_reference: typing.Optional[typing.Union["WindowsVirtualMachineSourceImageReference", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        termination_notification: typing.Optional[typing.Union["WindowsVirtualMachineTerminationNotification", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["WindowsVirtualMachineTimeouts", typing.Dict[str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        user_data: typing.Optional[builtins.str] = None,
        virtual_machine_scale_set_id: typing.Optional[builtins.str] = None,
        vtpm_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        winrm_listener: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineWinrmListener", typing.Dict[str, typing.Any]]]]] = None,
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
        :param admin_password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#admin_password WindowsVirtualMachine#admin_password}.
        :param admin_username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#admin_username WindowsVirtualMachine#admin_username}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#location WindowsVirtualMachine#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param network_interface_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#network_interface_ids WindowsVirtualMachine#network_interface_ids}.
        :param os_disk: os_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#os_disk WindowsVirtualMachine#os_disk}
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#resource_group_name WindowsVirtualMachine#resource_group_name}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#size WindowsVirtualMachine#size}.
        :param additional_capabilities: additional_capabilities block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#additional_capabilities WindowsVirtualMachine#additional_capabilities}
        :param additional_unattend_content: additional_unattend_content block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#additional_unattend_content WindowsVirtualMachine#additional_unattend_content}
        :param allow_extension_operations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#allow_extension_operations WindowsVirtualMachine#allow_extension_operations}.
        :param availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#availability_set_id WindowsVirtualMachine#availability_set_id}.
        :param boot_diagnostics: boot_diagnostics block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#boot_diagnostics WindowsVirtualMachine#boot_diagnostics}
        :param capacity_reservation_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#capacity_reservation_group_id WindowsVirtualMachine#capacity_reservation_group_id}.
        :param computer_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#computer_name WindowsVirtualMachine#computer_name}.
        :param custom_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#custom_data WindowsVirtualMachine#custom_data}.
        :param dedicated_host_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#dedicated_host_group_id WindowsVirtualMachine#dedicated_host_group_id}.
        :param dedicated_host_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#dedicated_host_id WindowsVirtualMachine#dedicated_host_id}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#edge_zone WindowsVirtualMachine#edge_zone}.
        :param enable_automatic_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#enable_automatic_updates WindowsVirtualMachine#enable_automatic_updates}.
        :param encryption_at_host_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#encryption_at_host_enabled WindowsVirtualMachine#encryption_at_host_enabled}.
        :param eviction_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#eviction_policy WindowsVirtualMachine#eviction_policy}.
        :param extensions_time_budget: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#extensions_time_budget WindowsVirtualMachine#extensions_time_budget}.
        :param gallery_application: gallery_application block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#gallery_application WindowsVirtualMachine#gallery_application}
        :param hotpatching_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#hotpatching_enabled WindowsVirtualMachine#hotpatching_enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#id WindowsVirtualMachine#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#identity WindowsVirtualMachine#identity}
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#license_type WindowsVirtualMachine#license_type}.
        :param max_bid_price: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#max_bid_price WindowsVirtualMachine#max_bid_price}.
        :param patch_assessment_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#patch_assessment_mode WindowsVirtualMachine#patch_assessment_mode}.
        :param patch_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#patch_mode WindowsVirtualMachine#patch_mode}.
        :param plan: plan block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#plan WindowsVirtualMachine#plan}
        :param platform_fault_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#platform_fault_domain WindowsVirtualMachine#platform_fault_domain}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#priority WindowsVirtualMachine#priority}.
        :param provision_vm_agent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#provision_vm_agent WindowsVirtualMachine#provision_vm_agent}.
        :param proximity_placement_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#proximity_placement_group_id WindowsVirtualMachine#proximity_placement_group_id}.
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secret WindowsVirtualMachine#secret}
        :param secure_boot_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secure_boot_enabled WindowsVirtualMachine#secure_boot_enabled}.
        :param source_image_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#source_image_id WindowsVirtualMachine#source_image_id}.
        :param source_image_reference: source_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#source_image_reference WindowsVirtualMachine#source_image_reference}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#tags WindowsVirtualMachine#tags}.
        :param termination_notification: termination_notification block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#termination_notification WindowsVirtualMachine#termination_notification}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timeouts WindowsVirtualMachine#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timezone WindowsVirtualMachine#timezone}.
        :param user_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#user_data WindowsVirtualMachine#user_data}.
        :param virtual_machine_scale_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#virtual_machine_scale_set_id WindowsVirtualMachine#virtual_machine_scale_set_id}.
        :param vtpm_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#vtpm_enabled WindowsVirtualMachine#vtpm_enabled}.
        :param winrm_listener: winrm_listener block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#winrm_listener WindowsVirtualMachine#winrm_listener}
        :param zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#zone WindowsVirtualMachine#zone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(os_disk, dict):
            os_disk = WindowsVirtualMachineOsDisk(**os_disk)
        if isinstance(additional_capabilities, dict):
            additional_capabilities = WindowsVirtualMachineAdditionalCapabilities(**additional_capabilities)
        if isinstance(boot_diagnostics, dict):
            boot_diagnostics = WindowsVirtualMachineBootDiagnostics(**boot_diagnostics)
        if isinstance(identity, dict):
            identity = WindowsVirtualMachineIdentity(**identity)
        if isinstance(plan, dict):
            plan = WindowsVirtualMachinePlan(**plan)
        if isinstance(source_image_reference, dict):
            source_image_reference = WindowsVirtualMachineSourceImageReference(**source_image_reference)
        if isinstance(termination_notification, dict):
            termination_notification = WindowsVirtualMachineTerminationNotification(**termination_notification)
        if isinstance(timeouts, dict):
            timeouts = WindowsVirtualMachineTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument admin_password", value=admin_password, expected_type=type_hints["admin_password"])
            check_type(argname="argument admin_username", value=admin_username, expected_type=type_hints["admin_username"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_interface_ids", value=network_interface_ids, expected_type=type_hints["network_interface_ids"])
            check_type(argname="argument os_disk", value=os_disk, expected_type=type_hints["os_disk"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument additional_capabilities", value=additional_capabilities, expected_type=type_hints["additional_capabilities"])
            check_type(argname="argument additional_unattend_content", value=additional_unattend_content, expected_type=type_hints["additional_unattend_content"])
            check_type(argname="argument allow_extension_operations", value=allow_extension_operations, expected_type=type_hints["allow_extension_operations"])
            check_type(argname="argument availability_set_id", value=availability_set_id, expected_type=type_hints["availability_set_id"])
            check_type(argname="argument boot_diagnostics", value=boot_diagnostics, expected_type=type_hints["boot_diagnostics"])
            check_type(argname="argument capacity_reservation_group_id", value=capacity_reservation_group_id, expected_type=type_hints["capacity_reservation_group_id"])
            check_type(argname="argument computer_name", value=computer_name, expected_type=type_hints["computer_name"])
            check_type(argname="argument custom_data", value=custom_data, expected_type=type_hints["custom_data"])
            check_type(argname="argument dedicated_host_group_id", value=dedicated_host_group_id, expected_type=type_hints["dedicated_host_group_id"])
            check_type(argname="argument dedicated_host_id", value=dedicated_host_id, expected_type=type_hints["dedicated_host_id"])
            check_type(argname="argument edge_zone", value=edge_zone, expected_type=type_hints["edge_zone"])
            check_type(argname="argument enable_automatic_updates", value=enable_automatic_updates, expected_type=type_hints["enable_automatic_updates"])
            check_type(argname="argument encryption_at_host_enabled", value=encryption_at_host_enabled, expected_type=type_hints["encryption_at_host_enabled"])
            check_type(argname="argument eviction_policy", value=eviction_policy, expected_type=type_hints["eviction_policy"])
            check_type(argname="argument extensions_time_budget", value=extensions_time_budget, expected_type=type_hints["extensions_time_budget"])
            check_type(argname="argument gallery_application", value=gallery_application, expected_type=type_hints["gallery_application"])
            check_type(argname="argument hotpatching_enabled", value=hotpatching_enabled, expected_type=type_hints["hotpatching_enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument max_bid_price", value=max_bid_price, expected_type=type_hints["max_bid_price"])
            check_type(argname="argument patch_assessment_mode", value=patch_assessment_mode, expected_type=type_hints["patch_assessment_mode"])
            check_type(argname="argument patch_mode", value=patch_mode, expected_type=type_hints["patch_mode"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument platform_fault_domain", value=platform_fault_domain, expected_type=type_hints["platform_fault_domain"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument provision_vm_agent", value=provision_vm_agent, expected_type=type_hints["provision_vm_agent"])
            check_type(argname="argument proximity_placement_group_id", value=proximity_placement_group_id, expected_type=type_hints["proximity_placement_group_id"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument secure_boot_enabled", value=secure_boot_enabled, expected_type=type_hints["secure_boot_enabled"])
            check_type(argname="argument source_image_id", value=source_image_id, expected_type=type_hints["source_image_id"])
            check_type(argname="argument source_image_reference", value=source_image_reference, expected_type=type_hints["source_image_reference"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument termination_notification", value=termination_notification, expected_type=type_hints["termination_notification"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument user_data", value=user_data, expected_type=type_hints["user_data"])
            check_type(argname="argument virtual_machine_scale_set_id", value=virtual_machine_scale_set_id, expected_type=type_hints["virtual_machine_scale_set_id"])
            check_type(argname="argument vtpm_enabled", value=vtpm_enabled, expected_type=type_hints["vtpm_enabled"])
            check_type(argname="argument winrm_listener", value=winrm_listener, expected_type=type_hints["winrm_listener"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "admin_password": admin_password,
            "admin_username": admin_username,
            "location": location,
            "name": name,
            "network_interface_ids": network_interface_ids,
            "os_disk": os_disk,
            "resource_group_name": resource_group_name,
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
        if additional_capabilities is not None:
            self._values["additional_capabilities"] = additional_capabilities
        if additional_unattend_content is not None:
            self._values["additional_unattend_content"] = additional_unattend_content
        if allow_extension_operations is not None:
            self._values["allow_extension_operations"] = allow_extension_operations
        if availability_set_id is not None:
            self._values["availability_set_id"] = availability_set_id
        if boot_diagnostics is not None:
            self._values["boot_diagnostics"] = boot_diagnostics
        if capacity_reservation_group_id is not None:
            self._values["capacity_reservation_group_id"] = capacity_reservation_group_id
        if computer_name is not None:
            self._values["computer_name"] = computer_name
        if custom_data is not None:
            self._values["custom_data"] = custom_data
        if dedicated_host_group_id is not None:
            self._values["dedicated_host_group_id"] = dedicated_host_group_id
        if dedicated_host_id is not None:
            self._values["dedicated_host_id"] = dedicated_host_id
        if edge_zone is not None:
            self._values["edge_zone"] = edge_zone
        if enable_automatic_updates is not None:
            self._values["enable_automatic_updates"] = enable_automatic_updates
        if encryption_at_host_enabled is not None:
            self._values["encryption_at_host_enabled"] = encryption_at_host_enabled
        if eviction_policy is not None:
            self._values["eviction_policy"] = eviction_policy
        if extensions_time_budget is not None:
            self._values["extensions_time_budget"] = extensions_time_budget
        if gallery_application is not None:
            self._values["gallery_application"] = gallery_application
        if hotpatching_enabled is not None:
            self._values["hotpatching_enabled"] = hotpatching_enabled
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if license_type is not None:
            self._values["license_type"] = license_type
        if max_bid_price is not None:
            self._values["max_bid_price"] = max_bid_price
        if patch_assessment_mode is not None:
            self._values["patch_assessment_mode"] = patch_assessment_mode
        if patch_mode is not None:
            self._values["patch_mode"] = patch_mode
        if plan is not None:
            self._values["plan"] = plan
        if platform_fault_domain is not None:
            self._values["platform_fault_domain"] = platform_fault_domain
        if priority is not None:
            self._values["priority"] = priority
        if provision_vm_agent is not None:
            self._values["provision_vm_agent"] = provision_vm_agent
        if proximity_placement_group_id is not None:
            self._values["proximity_placement_group_id"] = proximity_placement_group_id
        if secret is not None:
            self._values["secret"] = secret
        if secure_boot_enabled is not None:
            self._values["secure_boot_enabled"] = secure_boot_enabled
        if source_image_id is not None:
            self._values["source_image_id"] = source_image_id
        if source_image_reference is not None:
            self._values["source_image_reference"] = source_image_reference
        if tags is not None:
            self._values["tags"] = tags
        if termination_notification is not None:
            self._values["termination_notification"] = termination_notification
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timezone is not None:
            self._values["timezone"] = timezone
        if user_data is not None:
            self._values["user_data"] = user_data
        if virtual_machine_scale_set_id is not None:
            self._values["virtual_machine_scale_set_id"] = virtual_machine_scale_set_id
        if vtpm_enabled is not None:
            self._values["vtpm_enabled"] = vtpm_enabled
        if winrm_listener is not None:
            self._values["winrm_listener"] = winrm_listener
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
    def admin_password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#admin_password WindowsVirtualMachine#admin_password}.'''
        result = self._values.get("admin_password")
        assert result is not None, "Required property 'admin_password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_username(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#admin_username WindowsVirtualMachine#admin_username}.'''
        result = self._values.get("admin_username")
        assert result is not None, "Required property 'admin_username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#location WindowsVirtualMachine#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#network_interface_ids WindowsVirtualMachine#network_interface_ids}.'''
        result = self._values.get("network_interface_ids")
        assert result is not None, "Required property 'network_interface_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def os_disk(self) -> "WindowsVirtualMachineOsDisk":
        '''os_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#os_disk WindowsVirtualMachine#os_disk}
        '''
        result = self._values.get("os_disk")
        assert result is not None, "Required property 'os_disk' is missing"
        return typing.cast("WindowsVirtualMachineOsDisk", result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#resource_group_name WindowsVirtualMachine#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#size WindowsVirtualMachine#size}.'''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_capabilities(
        self,
    ) -> typing.Optional[WindowsVirtualMachineAdditionalCapabilities]:
        '''additional_capabilities block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#additional_capabilities WindowsVirtualMachine#additional_capabilities}
        '''
        result = self._values.get("additional_capabilities")
        return typing.cast(typing.Optional[WindowsVirtualMachineAdditionalCapabilities], result)

    @builtins.property
    def additional_unattend_content(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]]:
        '''additional_unattend_content block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#additional_unattend_content WindowsVirtualMachine#additional_unattend_content}
        '''
        result = self._values.get("additional_unattend_content")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineAdditionalUnattendContent]]], result)

    @builtins.property
    def allow_extension_operations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#allow_extension_operations WindowsVirtualMachine#allow_extension_operations}.'''
        result = self._values.get("allow_extension_operations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def availability_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#availability_set_id WindowsVirtualMachine#availability_set_id}.'''
        result = self._values.get("availability_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def boot_diagnostics(self) -> typing.Optional[WindowsVirtualMachineBootDiagnostics]:
        '''boot_diagnostics block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#boot_diagnostics WindowsVirtualMachine#boot_diagnostics}
        '''
        result = self._values.get("boot_diagnostics")
        return typing.cast(typing.Optional[WindowsVirtualMachineBootDiagnostics], result)

    @builtins.property
    def capacity_reservation_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#capacity_reservation_group_id WindowsVirtualMachine#capacity_reservation_group_id}.'''
        result = self._values.get("capacity_reservation_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def computer_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#computer_name WindowsVirtualMachine#computer_name}.'''
        result = self._values.get("computer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#custom_data WindowsVirtualMachine#custom_data}.'''
        result = self._values.get("custom_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dedicated_host_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#dedicated_host_group_id WindowsVirtualMachine#dedicated_host_group_id}.'''
        result = self._values.get("dedicated_host_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dedicated_host_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#dedicated_host_id WindowsVirtualMachine#dedicated_host_id}.'''
        result = self._values.get("dedicated_host_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edge_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#edge_zone WindowsVirtualMachine#edge_zone}.'''
        result = self._values.get("edge_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_automatic_updates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#enable_automatic_updates WindowsVirtualMachine#enable_automatic_updates}.'''
        result = self._values.get("enable_automatic_updates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption_at_host_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#encryption_at_host_enabled WindowsVirtualMachine#encryption_at_host_enabled}.'''
        result = self._values.get("encryption_at_host_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def eviction_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#eviction_policy WindowsVirtualMachine#eviction_policy}.'''
        result = self._values.get("eviction_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extensions_time_budget(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#extensions_time_budget WindowsVirtualMachine#extensions_time_budget}.'''
        result = self._values.get("extensions_time_budget")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gallery_application(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineGalleryApplication"]]]:
        '''gallery_application block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#gallery_application WindowsVirtualMachine#gallery_application}
        '''
        result = self._values.get("gallery_application")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineGalleryApplication"]]], result)

    @builtins.property
    def hotpatching_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#hotpatching_enabled WindowsVirtualMachine#hotpatching_enabled}.'''
        result = self._values.get("hotpatching_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#id WindowsVirtualMachine#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["WindowsVirtualMachineIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#identity WindowsVirtualMachine#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["WindowsVirtualMachineIdentity"], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#license_type WindowsVirtualMachine#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_bid_price(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#max_bid_price WindowsVirtualMachine#max_bid_price}.'''
        result = self._values.get("max_bid_price")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def patch_assessment_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#patch_assessment_mode WindowsVirtualMachine#patch_assessment_mode}.'''
        result = self._values.get("patch_assessment_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def patch_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#patch_mode WindowsVirtualMachine#patch_mode}.'''
        result = self._values.get("patch_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan(self) -> typing.Optional["WindowsVirtualMachinePlan"]:
        '''plan block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#plan WindowsVirtualMachine#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional["WindowsVirtualMachinePlan"], result)

    @builtins.property
    def platform_fault_domain(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#platform_fault_domain WindowsVirtualMachine#platform_fault_domain}.'''
        result = self._values.get("platform_fault_domain")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#priority WindowsVirtualMachine#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_vm_agent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#provision_vm_agent WindowsVirtualMachine#provision_vm_agent}.'''
        result = self._values.get("provision_vm_agent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def proximity_placement_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#proximity_placement_group_id WindowsVirtualMachine#proximity_placement_group_id}.'''
        result = self._values.get("proximity_placement_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineSecret"]]]:
        '''secret block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secret WindowsVirtualMachine#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineSecret"]]], result)

    @builtins.property
    def secure_boot_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secure_boot_enabled WindowsVirtualMachine#secure_boot_enabled}.'''
        result = self._values.get("secure_boot_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source_image_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#source_image_id WindowsVirtualMachine#source_image_id}.'''
        result = self._values.get("source_image_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_image_reference(
        self,
    ) -> typing.Optional["WindowsVirtualMachineSourceImageReference"]:
        '''source_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#source_image_reference WindowsVirtualMachine#source_image_reference}
        '''
        result = self._values.get("source_image_reference")
        return typing.cast(typing.Optional["WindowsVirtualMachineSourceImageReference"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#tags WindowsVirtualMachine#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def termination_notification(
        self,
    ) -> typing.Optional["WindowsVirtualMachineTerminationNotification"]:
        '''termination_notification block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#termination_notification WindowsVirtualMachine#termination_notification}
        '''
        result = self._values.get("termination_notification")
        return typing.cast(typing.Optional["WindowsVirtualMachineTerminationNotification"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["WindowsVirtualMachineTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timeouts WindowsVirtualMachine#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["WindowsVirtualMachineTimeouts"], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timezone WindowsVirtualMachine#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_data(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#user_data WindowsVirtualMachine#user_data}.'''
        result = self._values.get("user_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def virtual_machine_scale_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#virtual_machine_scale_set_id WindowsVirtualMachine#virtual_machine_scale_set_id}.'''
        result = self._values.get("virtual_machine_scale_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vtpm_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#vtpm_enabled WindowsVirtualMachine#vtpm_enabled}.'''
        result = self._values.get("vtpm_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def winrm_listener(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]]:
        '''winrm_listener block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#winrm_listener WindowsVirtualMachine#winrm_listener}
        '''
        result = self._values.get("winrm_listener")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineWinrmListener"]]], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#zone WindowsVirtualMachine#zone}.'''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineGalleryApplication",
    jsii_struct_bases=[],
    name_mapping={
        "version_id": "versionId",
        "configuration_blob_uri": "configurationBlobUri",
        "order": "order",
        "tag": "tag",
    },
)
class WindowsVirtualMachineGalleryApplication:
    def __init__(
        self,
        *,
        version_id: builtins.str,
        configuration_blob_uri: typing.Optional[builtins.str] = None,
        order: typing.Optional[jsii.Number] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param version_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#version_id WindowsVirtualMachine#version_id}.
        :param configuration_blob_uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#configuration_blob_uri WindowsVirtualMachine#configuration_blob_uri}.
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#order WindowsVirtualMachine#order}.
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#tag WindowsVirtualMachine#tag}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineGalleryApplication.__init__)
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
            check_type(argname="argument configuration_blob_uri", value=configuration_blob_uri, expected_type=type_hints["configuration_blob_uri"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "version_id": version_id,
        }
        if configuration_blob_uri is not None:
            self._values["configuration_blob_uri"] = configuration_blob_uri
        if order is not None:
            self._values["order"] = order
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def version_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#version_id WindowsVirtualMachine#version_id}.'''
        result = self._values.get("version_id")
        assert result is not None, "Required property 'version_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_blob_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#configuration_blob_uri WindowsVirtualMachine#configuration_blob_uri}.'''
        result = self._values.get("configuration_blob_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def order(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#order WindowsVirtualMachine#order}.'''
        result = self._values.get("order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#tag WindowsVirtualMachine#tag}.'''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineGalleryApplication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineGalleryApplicationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineGalleryApplicationList",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineGalleryApplicationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineGalleryApplicationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineGalleryApplicationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineGalleryApplicationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineGalleryApplication]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineGalleryApplication]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineGalleryApplication]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineGalleryApplicationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineGalleryApplicationOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineGalleryApplicationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConfigurationBlobUri")
    def reset_configuration_blob_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationBlobUri", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="configurationBlobUriInput")
    def configuration_blob_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationBlobUriInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="versionIdInput")
    def version_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationBlobUri")
    def configuration_blob_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationBlobUri"))

    @configuration_blob_uri.setter
    def configuration_blob_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationOutputReference, "configuration_blob_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationBlobUri", value)

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "order"))

    @order.setter
    def order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationOutputReference, "order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="versionId")
    def version_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionId"))

    @version_id.setter
    def version_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationOutputReference, "version_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineGalleryApplication, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineGalleryApplication, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineGalleryApplication, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineGalleryApplicationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineIdentity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "identity_ids": "identityIds"},
)
class WindowsVirtualMachineIdentity:
    def __init__(
        self,
        *,
        type: builtins.str,
        identity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#type WindowsVirtualMachine#type}.
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#identity_ids WindowsVirtualMachine#identity_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineIdentity.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if identity_ids is not None:
            self._values["identity_ids"] = identity_ids

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#type WindowsVirtualMachine#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#identity_ids WindowsVirtualMachine#identity_ids}.'''
        result = self._values.get("identity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineIdentityOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineIdentityOutputReference.__init__)
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
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachineIdentity]:
        return typing.cast(typing.Optional[WindowsVirtualMachineIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineOsDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching": "caching",
        "storage_account_type": "storageAccountType",
        "diff_disk_settings": "diffDiskSettings",
        "disk_encryption_set_id": "diskEncryptionSetId",
        "disk_size_gb": "diskSizeGb",
        "name": "name",
        "secure_vm_disk_encryption_set_id": "secureVmDiskEncryptionSetId",
        "security_encryption_type": "securityEncryptionType",
        "write_accelerator_enabled": "writeAcceleratorEnabled",
    },
)
class WindowsVirtualMachineOsDisk:
    def __init__(
        self,
        *,
        caching: builtins.str,
        storage_account_type: builtins.str,
        diff_disk_settings: typing.Optional[typing.Union["WindowsVirtualMachineOsDiskDiffDiskSettings", typing.Dict[str, typing.Any]]] = None,
        disk_encryption_set_id: typing.Optional[builtins.str] = None,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        secure_vm_disk_encryption_set_id: typing.Optional[builtins.str] = None,
        security_encryption_type: typing.Optional[builtins.str] = None,
        write_accelerator_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#caching WindowsVirtualMachine#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#storage_account_type WindowsVirtualMachine#storage_account_type}.
        :param diff_disk_settings: diff_disk_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#diff_disk_settings WindowsVirtualMachine#diff_disk_settings}
        :param disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#disk_encryption_set_id WindowsVirtualMachine#disk_encryption_set_id}.
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#disk_size_gb WindowsVirtualMachine#disk_size_gb}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param secure_vm_disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secure_vm_disk_encryption_set_id WindowsVirtualMachine#secure_vm_disk_encryption_set_id}.
        :param security_encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#security_encryption_type WindowsVirtualMachine#security_encryption_type}.
        :param write_accelerator_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#write_accelerator_enabled WindowsVirtualMachine#write_accelerator_enabled}.
        '''
        if isinstance(diff_disk_settings, dict):
            diff_disk_settings = WindowsVirtualMachineOsDiskDiffDiskSettings(**diff_disk_settings)
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineOsDisk.__init__)
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
            check_type(argname="argument diff_disk_settings", value=diff_disk_settings, expected_type=type_hints["diff_disk_settings"])
            check_type(argname="argument disk_encryption_set_id", value=disk_encryption_set_id, expected_type=type_hints["disk_encryption_set_id"])
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument secure_vm_disk_encryption_set_id", value=secure_vm_disk_encryption_set_id, expected_type=type_hints["secure_vm_disk_encryption_set_id"])
            check_type(argname="argument security_encryption_type", value=security_encryption_type, expected_type=type_hints["security_encryption_type"])
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
        if name is not None:
            self._values["name"] = name
        if secure_vm_disk_encryption_set_id is not None:
            self._values["secure_vm_disk_encryption_set_id"] = secure_vm_disk_encryption_set_id
        if security_encryption_type is not None:
            self._values["security_encryption_type"] = security_encryption_type
        if write_accelerator_enabled is not None:
            self._values["write_accelerator_enabled"] = write_accelerator_enabled

    @builtins.property
    def caching(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#caching WindowsVirtualMachine#caching}.'''
        result = self._values.get("caching")
        assert result is not None, "Required property 'caching' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_account_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#storage_account_type WindowsVirtualMachine#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        assert result is not None, "Required property 'storage_account_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def diff_disk_settings(
        self,
    ) -> typing.Optional["WindowsVirtualMachineOsDiskDiffDiskSettings"]:
        '''diff_disk_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#diff_disk_settings WindowsVirtualMachine#diff_disk_settings}
        '''
        result = self._values.get("diff_disk_settings")
        return typing.cast(typing.Optional["WindowsVirtualMachineOsDiskDiffDiskSettings"], result)

    @builtins.property
    def disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#disk_encryption_set_id WindowsVirtualMachine#disk_encryption_set_id}.'''
        result = self._values.get("disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#disk_size_gb WindowsVirtualMachine#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secure_vm_disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#secure_vm_disk_encryption_set_id WindowsVirtualMachine#secure_vm_disk_encryption_set_id}.'''
        result = self._values.get("secure_vm_disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#security_encryption_type WindowsVirtualMachine#security_encryption_type}.'''
        result = self._values.get("security_encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def write_accelerator_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#write_accelerator_enabled WindowsVirtualMachine#write_accelerator_enabled}.'''
        result = self._values.get("write_accelerator_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineOsDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineOsDiskDiffDiskSettings",
    jsii_struct_bases=[],
    name_mapping={"option": "option", "placement": "placement"},
)
class WindowsVirtualMachineOsDiskDiffDiskSettings:
    def __init__(
        self,
        *,
        option: builtins.str,
        placement: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#option WindowsVirtualMachine#option}.
        :param placement: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#placement WindowsVirtualMachine#placement}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineOsDiskDiffDiskSettings.__init__)
            check_type(argname="argument option", value=option, expected_type=type_hints["option"])
            check_type(argname="argument placement", value=placement, expected_type=type_hints["placement"])
        self._values: typing.Dict[str, typing.Any] = {
            "option": option,
        }
        if placement is not None:
            self._values["placement"] = placement

    @builtins.property
    def option(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#option WindowsVirtualMachine#option}.'''
        result = self._values.get("option")
        assert result is not None, "Required property 'option' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def placement(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#placement WindowsVirtualMachine#placement}.'''
        result = self._values.get("placement")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineOsDiskDiffDiskSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPlacement")
    def reset_placement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlacement", []))

    @builtins.property
    @jsii.member(jsii_name="optionInput")
    def option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optionInput"))

    @builtins.property
    @jsii.member(jsii_name="placementInput")
    def placement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "placementInput"))

    @builtins.property
    @jsii.member(jsii_name="option")
    def option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "option"))

    @option.setter
    def option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference, "option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "option", value)

    @builtins.property
    @jsii.member(jsii_name="placement")
    def placement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "placement"))

    @placement.setter
    def placement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference, "placement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placement", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineOsDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineOsDiskOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineOsDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDiffDiskSettings")
    def put_diff_disk_settings(
        self,
        *,
        option: builtins.str,
        placement: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#option WindowsVirtualMachine#option}.
        :param placement: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#placement WindowsVirtualMachine#placement}.
        '''
        value = WindowsVirtualMachineOsDiskDiffDiskSettings(
            option=option, placement=placement
        )

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

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSecureVmDiskEncryptionSetId")
    def reset_secure_vm_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureVmDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetSecurityEncryptionType")
    def reset_security_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityEncryptionType", []))

    @jsii.member(jsii_name="resetWriteAcceleratorEnabled")
    def reset_write_accelerator_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteAcceleratorEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettings")
    def diff_disk_settings(
        self,
    ) -> WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference:
        return typing.cast(WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference, jsii.get(self, "diffDiskSettings"))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="diffDiskSettingsInput")
    def diff_disk_settings_input(
        self,
    ) -> typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings]:
        return typing.cast(typing.Optional[WindowsVirtualMachineOsDiskDiffDiskSettings], jsii.get(self, "diffDiskSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetIdInput")
    def disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="secureVmDiskEncryptionSetIdInput")
    def secure_vm_disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secureVmDiskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="securityEncryptionTypeInput")
    def security_encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityEncryptionTypeInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionSetId")
    def disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionSetId"))

    @disk_encryption_set_id.setter
    def disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="secureVmDiskEncryptionSetId")
    def secure_vm_disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secureVmDiskEncryptionSetId"))

    @secure_vm_disk_encryption_set_id.setter
    def secure_vm_disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "secure_vm_disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureVmDiskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="securityEncryptionType")
    def security_encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityEncryptionType"))

    @security_encryption_type.setter
    def security_encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "security_encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityEncryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "storage_account_type").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "write_accelerator_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeAcceleratorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachineOsDisk]:
        return typing.cast(typing.Optional[WindowsVirtualMachineOsDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineOsDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineOsDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachinePlan",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "product": "product", "publisher": "publisher"},
)
class WindowsVirtualMachinePlan:
    def __init__(
        self,
        *,
        name: builtins.str,
        product: builtins.str,
        publisher: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.
        :param product: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#product WindowsVirtualMachine#product}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachinePlan.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#name WindowsVirtualMachine#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#product WindowsVirtualMachine#product}.'''
        result = self._values.get("product")
        assert result is not None, "Required property 'product' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachinePlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachinePlanOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachinePlanOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachinePlanOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachinePlanOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="product")
    def product(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "product"))

    @product.setter
    def product(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachinePlanOutputReference, "product").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "product", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachinePlanOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[WindowsVirtualMachinePlan]:
        return typing.cast(typing.Optional[WindowsVirtualMachinePlan], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[WindowsVirtualMachinePlan]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachinePlanOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSecret",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "key_vault_id": "keyVaultId"},
)
class WindowsVirtualMachineSecret:
    def __init__(
        self,
        *,
        certificate: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WindowsVirtualMachineSecretCertificate", typing.Dict[str, typing.Any]]]],
        key_vault_id: builtins.str,
    ) -> None:
        '''
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#certificate WindowsVirtualMachine#certificate}
        :param key_vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#key_vault_id WindowsVirtualMachine#key_vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecret.__init__)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument key_vault_id", value=key_vault_id, expected_type=type_hints["key_vault_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "certificate": certificate,
            "key_vault_id": key_vault_id,
        }

    @builtins.property
    def certificate(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineSecretCertificate"]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#certificate WindowsVirtualMachine#certificate}
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["WindowsVirtualMachineSecretCertificate"]], result)

    @builtins.property
    def key_vault_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#key_vault_id WindowsVirtualMachine#key_vault_id}.'''
        result = self._values.get("key_vault_id")
        assert result is not None, "Required property 'key_vault_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSecretCertificate",
    jsii_struct_bases=[],
    name_mapping={"store": "store", "url": "url"},
)
class WindowsVirtualMachineSecretCertificate:
    def __init__(self, *, store: builtins.str, url: builtins.str) -> None:
        '''
        :param store: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#store WindowsVirtualMachine#store}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#url WindowsVirtualMachine#url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretCertificate.__init__)
            check_type(argname="argument store", value=store, expected_type=type_hints["store"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "store": store,
            "url": url,
        }

    @builtins.property
    def store(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#store WindowsVirtualMachine#store}.'''
        result = self._values.get("store")
        assert result is not None, "Required property 'store' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#url WindowsVirtualMachine#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineSecretCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineSecretCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSecretCertificateList",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineSecretCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineSecretCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineSecretCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSecretCertificateOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="storeInput")
    def store_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "store"))

    @store.setter
    def store(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretCertificateOutputReference, "store").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "store", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretCertificateOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineSecretCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineSecretCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineSecretCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineSecretList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSecretList",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WindowsVirtualMachineSecretOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineSecretOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecret]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecret]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecret]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineSecretOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSecretOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[WindowsVirtualMachineSecretCertificate, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineSecretOutputReference.put_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> WindowsVirtualMachineSecretCertificateList:
        return typing.cast(WindowsVirtualMachineSecretCertificateList, jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineSecretCertificate]]], jsii.get(self, "certificateInput"))

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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretOutputReference, "key_vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyVaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineSecret, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineSecret, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineSecret, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSecretOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSourceImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class WindowsVirtualMachineSourceImageReference:
    def __init__(
        self,
        *,
        offer: builtins.str,
        publisher: builtins.str,
        sku: builtins.str,
        version: builtins.str,
    ) -> None:
        '''
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#offer WindowsVirtualMachine#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#sku WindowsVirtualMachine#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#version WindowsVirtualMachine#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineSourceImageReference.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#offer WindowsVirtualMachine#offer}.'''
        result = self._values.get("offer")
        assert result is not None, "Required property 'offer' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#publisher WindowsVirtualMachine#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#sku WindowsVirtualMachine#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#version WindowsVirtualMachine#version}.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineSourceImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineSourceImageReferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineSourceImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineSourceImageReferenceOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSourceImageReferenceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSourceImageReferenceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSourceImageReferenceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSourceImageReferenceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineSourceImageReference]:
        return typing.cast(typing.Optional[WindowsVirtualMachineSourceImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineSourceImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineSourceImageReferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineTerminationNotification",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "timeout": "timeout"},
)
class WindowsVirtualMachineTerminationNotification:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#enabled WindowsVirtualMachine#enabled}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timeout WindowsVirtualMachine#timeout}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineTerminationNotification.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#enabled WindowsVirtualMachine#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#timeout WindowsVirtualMachine#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineTerminationNotification(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineTerminationNotificationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineTerminationNotificationOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineTerminationNotificationOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTerminationNotificationOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTerminationNotificationOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[WindowsVirtualMachineTerminationNotification]:
        return typing.cast(typing.Optional[WindowsVirtualMachineTerminationNotification], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[WindowsVirtualMachineTerminationNotification],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTerminationNotificationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class WindowsVirtualMachineTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#create WindowsVirtualMachine#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#delete WindowsVirtualMachine#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#read WindowsVirtualMachine#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#update WindowsVirtualMachine#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#create WindowsVirtualMachine#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#delete WindowsVirtualMachine#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#read WindowsVirtualMachine#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#update WindowsVirtualMachine#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineWinrmListener",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol", "certificate_url": "certificateUrl"},
)
class WindowsVirtualMachineWinrmListener:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        certificate_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#protocol WindowsVirtualMachine#protocol}.
        :param certificate_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#certificate_url WindowsVirtualMachine#certificate_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineWinrmListener.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument certificate_url", value=certificate_url, expected_type=type_hints["certificate_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
        }
        if certificate_url is not None:
            self._values["certificate_url"] = certificate_url

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#protocol WindowsVirtualMachine#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/windows_virtual_machine#certificate_url WindowsVirtualMachine#certificate_url}.'''
        result = self._values.get("certificate_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WindowsVirtualMachineWinrmListener(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WindowsVirtualMachineWinrmListenerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineWinrmListenerList",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineWinrmListenerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WindowsVirtualMachineWinrmListenerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WindowsVirtualMachineWinrmListenerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WindowsVirtualMachineWinrmListenerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineWinrmListenerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineWinrmListenerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineWinrmListenerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineWinrmListener]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineWinrmListener]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WindowsVirtualMachineWinrmListener]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineWinrmListenerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WindowsVirtualMachineWinrmListenerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.windowsVirtualMachine.WindowsVirtualMachineWinrmListenerOutputReference",
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
            type_hints = typing.get_type_hints(WindowsVirtualMachineWinrmListenerOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineWinrmListenerOutputReference, "certificate_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateUrl", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineWinrmListenerOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WindowsVirtualMachineWinrmListener, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WindowsVirtualMachineWinrmListener, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WindowsVirtualMachineWinrmListener, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WindowsVirtualMachineWinrmListenerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WindowsVirtualMachine",
    "WindowsVirtualMachineAdditionalCapabilities",
    "WindowsVirtualMachineAdditionalCapabilitiesOutputReference",
    "WindowsVirtualMachineAdditionalUnattendContent",
    "WindowsVirtualMachineAdditionalUnattendContentList",
    "WindowsVirtualMachineAdditionalUnattendContentOutputReference",
    "WindowsVirtualMachineBootDiagnostics",
    "WindowsVirtualMachineBootDiagnosticsOutputReference",
    "WindowsVirtualMachineConfig",
    "WindowsVirtualMachineGalleryApplication",
    "WindowsVirtualMachineGalleryApplicationList",
    "WindowsVirtualMachineGalleryApplicationOutputReference",
    "WindowsVirtualMachineIdentity",
    "WindowsVirtualMachineIdentityOutputReference",
    "WindowsVirtualMachineOsDisk",
    "WindowsVirtualMachineOsDiskDiffDiskSettings",
    "WindowsVirtualMachineOsDiskDiffDiskSettingsOutputReference",
    "WindowsVirtualMachineOsDiskOutputReference",
    "WindowsVirtualMachinePlan",
    "WindowsVirtualMachinePlanOutputReference",
    "WindowsVirtualMachineSecret",
    "WindowsVirtualMachineSecretCertificate",
    "WindowsVirtualMachineSecretCertificateList",
    "WindowsVirtualMachineSecretCertificateOutputReference",
    "WindowsVirtualMachineSecretList",
    "WindowsVirtualMachineSecretOutputReference",
    "WindowsVirtualMachineSourceImageReference",
    "WindowsVirtualMachineSourceImageReferenceOutputReference",
    "WindowsVirtualMachineTerminationNotification",
    "WindowsVirtualMachineTerminationNotificationOutputReference",
    "WindowsVirtualMachineTimeouts",
    "WindowsVirtualMachineTimeoutsOutputReference",
    "WindowsVirtualMachineWinrmListener",
    "WindowsVirtualMachineWinrmListenerList",
    "WindowsVirtualMachineWinrmListenerOutputReference",
]

publication.publish()
