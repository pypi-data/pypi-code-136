'''
# `azurerm_site_recovery_replicated_vm`

Refer to the Terraform Registory for docs: [`azurerm_site_recovery_replicated_vm`](https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm).
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


class SiteRecoveryReplicatedVm(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVm",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm azurerm_site_recovery_replicated_vm}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        recovery_replication_policy_id: builtins.str,
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        source_recovery_fabric_name: builtins.str,
        source_recovery_protection_container_name: builtins.str,
        source_vm_id: builtins.str,
        target_recovery_fabric_id: builtins.str,
        target_recovery_protection_container_id: builtins.str,
        target_resource_group_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        managed_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmManagedDisk", typing.Dict[str, typing.Any]]]]] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        target_availability_set_id: typing.Optional[builtins.str] = None,
        target_network_id: typing.Optional[builtins.str] = None,
        target_zone: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SiteRecoveryReplicatedVmTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm azurerm_site_recovery_replicated_vm} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#name SiteRecoveryReplicatedVm#name}.
        :param recovery_replication_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_replication_policy_id SiteRecoveryReplicatedVm#recovery_replication_policy_id}.
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_vault_name SiteRecoveryReplicatedVm#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#resource_group_name SiteRecoveryReplicatedVm#resource_group_name}.
        :param source_recovery_fabric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_recovery_fabric_name SiteRecoveryReplicatedVm#source_recovery_fabric_name}.
        :param source_recovery_protection_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_recovery_protection_container_name SiteRecoveryReplicatedVm#source_recovery_protection_container_name}.
        :param source_vm_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_vm_id SiteRecoveryReplicatedVm#source_vm_id}.
        :param target_recovery_fabric_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_recovery_fabric_id SiteRecoveryReplicatedVm#target_recovery_fabric_id}.
        :param target_recovery_protection_container_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_recovery_protection_container_id SiteRecoveryReplicatedVm#target_recovery_protection_container_id}.
        :param target_resource_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_resource_group_id SiteRecoveryReplicatedVm#target_resource_group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#id SiteRecoveryReplicatedVm#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param managed_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#managed_disk SiteRecoveryReplicatedVm#managed_disk}.
        :param network_interface: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#network_interface SiteRecoveryReplicatedVm#network_interface}.
        :param target_availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_availability_set_id SiteRecoveryReplicatedVm#target_availability_set_id}.
        :param target_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_network_id SiteRecoveryReplicatedVm#target_network_id}.
        :param target_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_zone SiteRecoveryReplicatedVm#target_zone}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#timeouts SiteRecoveryReplicatedVm#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVm.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SiteRecoveryReplicatedVmConfig(
            name=name,
            recovery_replication_policy_id=recovery_replication_policy_id,
            recovery_vault_name=recovery_vault_name,
            resource_group_name=resource_group_name,
            source_recovery_fabric_name=source_recovery_fabric_name,
            source_recovery_protection_container_name=source_recovery_protection_container_name,
            source_vm_id=source_vm_id,
            target_recovery_fabric_id=target_recovery_fabric_id,
            target_recovery_protection_container_id=target_recovery_protection_container_id,
            target_resource_group_id=target_resource_group_id,
            id=id,
            managed_disk=managed_disk,
            network_interface=network_interface,
            target_availability_set_id=target_availability_set_id,
            target_network_id=target_network_id,
            target_zone=target_zone,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putManagedDisk")
    def put_managed_disk(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmManagedDisk", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVm.put_managed_disk)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedDisk", [value]))

    @jsii.member(jsii_name="putNetworkInterface")
    def put_network_interface(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmNetworkInterface", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVm.put_network_interface)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkInterface", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#create SiteRecoveryReplicatedVm#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#delete SiteRecoveryReplicatedVm#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#read SiteRecoveryReplicatedVm#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#update SiteRecoveryReplicatedVm#update}.
        '''
        value = SiteRecoveryReplicatedVmTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetManagedDisk")
    def reset_managed_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedDisk", []))

    @jsii.member(jsii_name="resetNetworkInterface")
    def reset_network_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkInterface", []))

    @jsii.member(jsii_name="resetTargetAvailabilitySetId")
    def reset_target_availability_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetAvailabilitySetId", []))

    @jsii.member(jsii_name="resetTargetNetworkId")
    def reset_target_network_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetNetworkId", []))

    @jsii.member(jsii_name="resetTargetZone")
    def reset_target_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetZone", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="managedDisk")
    def managed_disk(self) -> "SiteRecoveryReplicatedVmManagedDiskList":
        return typing.cast("SiteRecoveryReplicatedVmManagedDiskList", jsii.get(self, "managedDisk"))

    @builtins.property
    @jsii.member(jsii_name="networkInterface")
    def network_interface(self) -> "SiteRecoveryReplicatedVmNetworkInterfaceList":
        return typing.cast("SiteRecoveryReplicatedVmNetworkInterfaceList", jsii.get(self, "networkInterface"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SiteRecoveryReplicatedVmTimeoutsOutputReference":
        return typing.cast("SiteRecoveryReplicatedVmTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="managedDiskInput")
    def managed_disk_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDisk"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDisk"]]], jsii.get(self, "managedDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceInput")
    def network_interface_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmNetworkInterface"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmNetworkInterface"]]], jsii.get(self, "networkInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryReplicationPolicyIdInput")
    def recovery_replication_policy_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryReplicationPolicyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultNameInput")
    def recovery_vault_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryVaultNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceRecoveryFabricNameInput")
    def source_recovery_fabric_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceRecoveryFabricNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceRecoveryProtectionContainerNameInput")
    def source_recovery_protection_container_name_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceRecoveryProtectionContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceVmIdInput")
    def source_vm_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceVmIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetAvailabilitySetIdInput")
    def target_availability_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetAvailabilitySetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetNetworkIdInput")
    def target_network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetNetworkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetRecoveryFabricIdInput")
    def target_recovery_fabric_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetRecoveryFabricIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetRecoveryProtectionContainerIdInput")
    def target_recovery_protection_container_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetRecoveryProtectionContainerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceGroupIdInput")
    def target_resource_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetZoneInput")
    def target_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SiteRecoveryReplicatedVmTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SiteRecoveryReplicatedVmTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryReplicationPolicyId")
    def recovery_replication_policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryReplicationPolicyId"))

    @recovery_replication_policy_id.setter
    def recovery_replication_policy_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "recovery_replication_policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryReplicationPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultName")
    def recovery_vault_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryVaultName"))

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "recovery_vault_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryVaultName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceRecoveryFabricName")
    def source_recovery_fabric_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceRecoveryFabricName"))

    @source_recovery_fabric_name.setter
    def source_recovery_fabric_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "source_recovery_fabric_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceRecoveryFabricName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceRecoveryProtectionContainerName")
    def source_recovery_protection_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceRecoveryProtectionContainerName"))

    @source_recovery_protection_container_name.setter
    def source_recovery_protection_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "source_recovery_protection_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceRecoveryProtectionContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceVmId")
    def source_vm_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceVmId"))

    @source_vm_id.setter
    def source_vm_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "source_vm_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceVmId", value)

    @builtins.property
    @jsii.member(jsii_name="targetAvailabilitySetId")
    def target_availability_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetAvailabilitySetId"))

    @target_availability_set_id.setter
    def target_availability_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "target_availability_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetAvailabilitySetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetNetworkId")
    def target_network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetNetworkId"))

    @target_network_id.setter
    def target_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "target_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="targetRecoveryFabricId")
    def target_recovery_fabric_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetRecoveryFabricId"))

    @target_recovery_fabric_id.setter
    def target_recovery_fabric_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "target_recovery_fabric_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetRecoveryFabricId", value)

    @builtins.property
    @jsii.member(jsii_name="targetRecoveryProtectionContainerId")
    def target_recovery_protection_container_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetRecoveryProtectionContainerId"))

    @target_recovery_protection_container_id.setter
    def target_recovery_protection_container_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "target_recovery_protection_container_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetRecoveryProtectionContainerId", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceGroupId")
    def target_resource_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceGroupId"))

    @target_resource_group_id.setter
    def target_resource_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "target_resource_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="targetZone")
    def target_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetZone"))

    @target_zone.setter
    def target_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVm, "target_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetZone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmConfig",
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
        "recovery_replication_policy_id": "recoveryReplicationPolicyId",
        "recovery_vault_name": "recoveryVaultName",
        "resource_group_name": "resourceGroupName",
        "source_recovery_fabric_name": "sourceRecoveryFabricName",
        "source_recovery_protection_container_name": "sourceRecoveryProtectionContainerName",
        "source_vm_id": "sourceVmId",
        "target_recovery_fabric_id": "targetRecoveryFabricId",
        "target_recovery_protection_container_id": "targetRecoveryProtectionContainerId",
        "target_resource_group_id": "targetResourceGroupId",
        "id": "id",
        "managed_disk": "managedDisk",
        "network_interface": "networkInterface",
        "target_availability_set_id": "targetAvailabilitySetId",
        "target_network_id": "targetNetworkId",
        "target_zone": "targetZone",
        "timeouts": "timeouts",
    },
)
class SiteRecoveryReplicatedVmConfig(cdktf.TerraformMetaArguments):
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
        recovery_replication_policy_id: builtins.str,
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        source_recovery_fabric_name: builtins.str,
        source_recovery_protection_container_name: builtins.str,
        source_vm_id: builtins.str,
        target_recovery_fabric_id: builtins.str,
        target_recovery_protection_container_id: builtins.str,
        target_resource_group_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        managed_disk: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmManagedDisk", typing.Dict[str, typing.Any]]]]] = None,
        network_interface: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmNetworkInterface", typing.Dict[str, typing.Any]]]]] = None,
        target_availability_set_id: typing.Optional[builtins.str] = None,
        target_network_id: typing.Optional[builtins.str] = None,
        target_zone: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["SiteRecoveryReplicatedVmTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#name SiteRecoveryReplicatedVm#name}.
        :param recovery_replication_policy_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_replication_policy_id SiteRecoveryReplicatedVm#recovery_replication_policy_id}.
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_vault_name SiteRecoveryReplicatedVm#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#resource_group_name SiteRecoveryReplicatedVm#resource_group_name}.
        :param source_recovery_fabric_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_recovery_fabric_name SiteRecoveryReplicatedVm#source_recovery_fabric_name}.
        :param source_recovery_protection_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_recovery_protection_container_name SiteRecoveryReplicatedVm#source_recovery_protection_container_name}.
        :param source_vm_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_vm_id SiteRecoveryReplicatedVm#source_vm_id}.
        :param target_recovery_fabric_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_recovery_fabric_id SiteRecoveryReplicatedVm#target_recovery_fabric_id}.
        :param target_recovery_protection_container_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_recovery_protection_container_id SiteRecoveryReplicatedVm#target_recovery_protection_container_id}.
        :param target_resource_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_resource_group_id SiteRecoveryReplicatedVm#target_resource_group_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#id SiteRecoveryReplicatedVm#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param managed_disk: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#managed_disk SiteRecoveryReplicatedVm#managed_disk}.
        :param network_interface: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#network_interface SiteRecoveryReplicatedVm#network_interface}.
        :param target_availability_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_availability_set_id SiteRecoveryReplicatedVm#target_availability_set_id}.
        :param target_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_network_id SiteRecoveryReplicatedVm#target_network_id}.
        :param target_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_zone SiteRecoveryReplicatedVm#target_zone}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#timeouts SiteRecoveryReplicatedVm#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = SiteRecoveryReplicatedVmTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recovery_replication_policy_id", value=recovery_replication_policy_id, expected_type=type_hints["recovery_replication_policy_id"])
            check_type(argname="argument recovery_vault_name", value=recovery_vault_name, expected_type=type_hints["recovery_vault_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument source_recovery_fabric_name", value=source_recovery_fabric_name, expected_type=type_hints["source_recovery_fabric_name"])
            check_type(argname="argument source_recovery_protection_container_name", value=source_recovery_protection_container_name, expected_type=type_hints["source_recovery_protection_container_name"])
            check_type(argname="argument source_vm_id", value=source_vm_id, expected_type=type_hints["source_vm_id"])
            check_type(argname="argument target_recovery_fabric_id", value=target_recovery_fabric_id, expected_type=type_hints["target_recovery_fabric_id"])
            check_type(argname="argument target_recovery_protection_container_id", value=target_recovery_protection_container_id, expected_type=type_hints["target_recovery_protection_container_id"])
            check_type(argname="argument target_resource_group_id", value=target_resource_group_id, expected_type=type_hints["target_resource_group_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument managed_disk", value=managed_disk, expected_type=type_hints["managed_disk"])
            check_type(argname="argument network_interface", value=network_interface, expected_type=type_hints["network_interface"])
            check_type(argname="argument target_availability_set_id", value=target_availability_set_id, expected_type=type_hints["target_availability_set_id"])
            check_type(argname="argument target_network_id", value=target_network_id, expected_type=type_hints["target_network_id"])
            check_type(argname="argument target_zone", value=target_zone, expected_type=type_hints["target_zone"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "recovery_replication_policy_id": recovery_replication_policy_id,
            "recovery_vault_name": recovery_vault_name,
            "resource_group_name": resource_group_name,
            "source_recovery_fabric_name": source_recovery_fabric_name,
            "source_recovery_protection_container_name": source_recovery_protection_container_name,
            "source_vm_id": source_vm_id,
            "target_recovery_fabric_id": target_recovery_fabric_id,
            "target_recovery_protection_container_id": target_recovery_protection_container_id,
            "target_resource_group_id": target_resource_group_id,
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
        if id is not None:
            self._values["id"] = id
        if managed_disk is not None:
            self._values["managed_disk"] = managed_disk
        if network_interface is not None:
            self._values["network_interface"] = network_interface
        if target_availability_set_id is not None:
            self._values["target_availability_set_id"] = target_availability_set_id
        if target_network_id is not None:
            self._values["target_network_id"] = target_network_id
        if target_zone is not None:
            self._values["target_zone"] = target_zone
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#name SiteRecoveryReplicatedVm#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_replication_policy_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_replication_policy_id SiteRecoveryReplicatedVm#recovery_replication_policy_id}.'''
        result = self._values.get("recovery_replication_policy_id")
        assert result is not None, "Required property 'recovery_replication_policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_vault_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_vault_name SiteRecoveryReplicatedVm#recovery_vault_name}.'''
        result = self._values.get("recovery_vault_name")
        assert result is not None, "Required property 'recovery_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#resource_group_name SiteRecoveryReplicatedVm#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_recovery_fabric_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_recovery_fabric_name SiteRecoveryReplicatedVm#source_recovery_fabric_name}.'''
        result = self._values.get("source_recovery_fabric_name")
        assert result is not None, "Required property 'source_recovery_fabric_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_recovery_protection_container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_recovery_protection_container_name SiteRecoveryReplicatedVm#source_recovery_protection_container_name}.'''
        result = self._values.get("source_recovery_protection_container_name")
        assert result is not None, "Required property 'source_recovery_protection_container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_vm_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_vm_id SiteRecoveryReplicatedVm#source_vm_id}.'''
        result = self._values.get("source_vm_id")
        assert result is not None, "Required property 'source_vm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_recovery_fabric_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_recovery_fabric_id SiteRecoveryReplicatedVm#target_recovery_fabric_id}.'''
        result = self._values.get("target_recovery_fabric_id")
        assert result is not None, "Required property 'target_recovery_fabric_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_recovery_protection_container_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_recovery_protection_container_id SiteRecoveryReplicatedVm#target_recovery_protection_container_id}.'''
        result = self._values.get("target_recovery_protection_container_id")
        assert result is not None, "Required property 'target_recovery_protection_container_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_resource_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_resource_group_id SiteRecoveryReplicatedVm#target_resource_group_id}.'''
        result = self._values.get("target_resource_group_id")
        assert result is not None, "Required property 'target_resource_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#id SiteRecoveryReplicatedVm#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_disk(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDisk"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#managed_disk SiteRecoveryReplicatedVm#managed_disk}.'''
        result = self._values.get("managed_disk")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDisk"]]], result)

    @builtins.property
    def network_interface(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmNetworkInterface"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#network_interface SiteRecoveryReplicatedVm#network_interface}.'''
        result = self._values.get("network_interface")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmNetworkInterface"]]], result)

    @builtins.property
    def target_availability_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_availability_set_id SiteRecoveryReplicatedVm#target_availability_set_id}.'''
        result = self._values.get("target_availability_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_network_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_network_id SiteRecoveryReplicatedVm#target_network_id}.'''
        result = self._values.get("target_network_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_zone SiteRecoveryReplicatedVm#target_zone}.'''
        result = self._values.get("target_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SiteRecoveryReplicatedVmTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#timeouts SiteRecoveryReplicatedVm#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SiteRecoveryReplicatedVmTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryReplicatedVmConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDisk",
    jsii_struct_bases=[],
    name_mapping={
        "disk_id": "diskId",
        "staging_storage_account_id": "stagingStorageAccountId",
        "target_disk_encryption": "targetDiskEncryption",
        "target_disk_encryption_set_id": "targetDiskEncryptionSetId",
        "target_disk_type": "targetDiskType",
        "target_replica_disk_type": "targetReplicaDiskType",
        "target_resource_group_id": "targetResourceGroupId",
    },
)
class SiteRecoveryReplicatedVmManagedDisk:
    def __init__(
        self,
        *,
        disk_id: typing.Optional[builtins.str] = None,
        staging_storage_account_id: typing.Optional[builtins.str] = None,
        target_disk_encryption: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption", typing.Dict[str, typing.Any]]]]] = None,
        target_disk_encryption_set_id: typing.Optional[builtins.str] = None,
        target_disk_type: typing.Optional[builtins.str] = None,
        target_replica_disk_type: typing.Optional[builtins.str] = None,
        target_resource_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#disk_id SiteRecoveryReplicatedVm#disk_id}.
        :param staging_storage_account_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#staging_storage_account_id SiteRecoveryReplicatedVm#staging_storage_account_id}.
        :param target_disk_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_disk_encryption SiteRecoveryReplicatedVm#target_disk_encryption}.
        :param target_disk_encryption_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_disk_encryption_set_id SiteRecoveryReplicatedVm#target_disk_encryption_set_id}.
        :param target_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_disk_type SiteRecoveryReplicatedVm#target_disk_type}.
        :param target_replica_disk_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_replica_disk_type SiteRecoveryReplicatedVm#target_replica_disk_type}.
        :param target_resource_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_resource_group_id SiteRecoveryReplicatedVm#target_resource_group_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDisk.__init__)
            check_type(argname="argument disk_id", value=disk_id, expected_type=type_hints["disk_id"])
            check_type(argname="argument staging_storage_account_id", value=staging_storage_account_id, expected_type=type_hints["staging_storage_account_id"])
            check_type(argname="argument target_disk_encryption", value=target_disk_encryption, expected_type=type_hints["target_disk_encryption"])
            check_type(argname="argument target_disk_encryption_set_id", value=target_disk_encryption_set_id, expected_type=type_hints["target_disk_encryption_set_id"])
            check_type(argname="argument target_disk_type", value=target_disk_type, expected_type=type_hints["target_disk_type"])
            check_type(argname="argument target_replica_disk_type", value=target_replica_disk_type, expected_type=type_hints["target_replica_disk_type"])
            check_type(argname="argument target_resource_group_id", value=target_resource_group_id, expected_type=type_hints["target_resource_group_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disk_id is not None:
            self._values["disk_id"] = disk_id
        if staging_storage_account_id is not None:
            self._values["staging_storage_account_id"] = staging_storage_account_id
        if target_disk_encryption is not None:
            self._values["target_disk_encryption"] = target_disk_encryption
        if target_disk_encryption_set_id is not None:
            self._values["target_disk_encryption_set_id"] = target_disk_encryption_set_id
        if target_disk_type is not None:
            self._values["target_disk_type"] = target_disk_type
        if target_replica_disk_type is not None:
            self._values["target_replica_disk_type"] = target_replica_disk_type
        if target_resource_group_id is not None:
            self._values["target_resource_group_id"] = target_resource_group_id

    @builtins.property
    def disk_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#disk_id SiteRecoveryReplicatedVm#disk_id}.'''
        result = self._values.get("disk_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def staging_storage_account_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#staging_storage_account_id SiteRecoveryReplicatedVm#staging_storage_account_id}.'''
        result = self._values.get("staging_storage_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_disk_encryption SiteRecoveryReplicatedVm#target_disk_encryption}.'''
        result = self._values.get("target_disk_encryption")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption"]]], result)

    @builtins.property
    def target_disk_encryption_set_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_disk_encryption_set_id SiteRecoveryReplicatedVm#target_disk_encryption_set_id}.'''
        result = self._values.get("target_disk_encryption_set_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_disk_type SiteRecoveryReplicatedVm#target_disk_type}.'''
        result = self._values.get("target_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_replica_disk_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_replica_disk_type SiteRecoveryReplicatedVm#target_replica_disk_type}.'''
        result = self._values.get("target_replica_disk_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_resource_group_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_resource_group_id SiteRecoveryReplicatedVm#target_resource_group_id}.'''
        result = self._values.get("target_resource_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryReplicatedVmManagedDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SiteRecoveryReplicatedVmManagedDiskList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskList",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SiteRecoveryReplicatedVmManagedDiskOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SiteRecoveryReplicatedVmManagedDiskOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDisk]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDisk]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDisk]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SiteRecoveryReplicatedVmManagedDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskOutputReference",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTargetDiskEncryption")
    def put_target_disk_encryption(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskOutputReference.put_target_disk_encryption)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetDiskEncryption", [value]))

    @jsii.member(jsii_name="resetDiskId")
    def reset_disk_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskId", []))

    @jsii.member(jsii_name="resetStagingStorageAccountId")
    def reset_staging_storage_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStagingStorageAccountId", []))

    @jsii.member(jsii_name="resetTargetDiskEncryption")
    def reset_target_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDiskEncryption", []))

    @jsii.member(jsii_name="resetTargetDiskEncryptionSetId")
    def reset_target_disk_encryption_set_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDiskEncryptionSetId", []))

    @jsii.member(jsii_name="resetTargetDiskType")
    def reset_target_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDiskType", []))

    @jsii.member(jsii_name="resetTargetReplicaDiskType")
    def reset_target_replica_disk_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetReplicaDiskType", []))

    @jsii.member(jsii_name="resetTargetResourceGroupId")
    def reset_target_resource_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResourceGroupId", []))

    @builtins.property
    @jsii.member(jsii_name="targetDiskEncryption")
    def target_disk_encryption(
        self,
    ) -> "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList":
        return typing.cast("SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList", jsii.get(self, "targetDiskEncryption"))

    @builtins.property
    @jsii.member(jsii_name="diskIdInput")
    def disk_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskIdInput"))

    @builtins.property
    @jsii.member(jsii_name="stagingStorageAccountIdInput")
    def staging_storage_account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stagingStorageAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDiskEncryptionInput")
    def target_disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption"]]], jsii.get(self, "targetDiskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDiskEncryptionSetIdInput")
    def target_disk_encryption_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetDiskEncryptionSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDiskTypeInput")
    def target_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetReplicaDiskTypeInput")
    def target_replica_disk_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetReplicaDiskTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceGroupIdInput")
    def target_resource_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetResourceGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="diskId")
    def disk_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskId"))

    @disk_id.setter
    def disk_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskOutputReference, "disk_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskId", value)

    @builtins.property
    @jsii.member(jsii_name="stagingStorageAccountId")
    def staging_storage_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stagingStorageAccountId"))

    @staging_storage_account_id.setter
    def staging_storage_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskOutputReference, "staging_storage_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagingStorageAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="targetDiskEncryptionSetId")
    def target_disk_encryption_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDiskEncryptionSetId"))

    @target_disk_encryption_set_id.setter
    def target_disk_encryption_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskOutputReference, "target_disk_encryption_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDiskEncryptionSetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetDiskType")
    def target_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDiskType"))

    @target_disk_type.setter
    def target_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskOutputReference, "target_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="targetReplicaDiskType")
    def target_replica_disk_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetReplicaDiskType"))

    @target_replica_disk_type.setter
    def target_replica_disk_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskOutputReference, "target_replica_disk_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetReplicaDiskType", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceGroupId")
    def target_resource_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetResourceGroupId"))

    @target_resource_group_id.setter
    def target_resource_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskOutputReference, "target_resource_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDisk, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDisk, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDisk, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "disk_encryption_key": "diskEncryptionKey",
        "key_encryption_key": "keyEncryptionKey",
    },
)
class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption:
    def __init__(
        self,
        *,
        disk_encryption_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey", typing.Dict[str, typing.Any]]]]] = None,
        key_encryption_key: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param disk_encryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#disk_encryption_key SiteRecoveryReplicatedVm#disk_encryption_key}.
        :param key_encryption_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#key_encryption_key SiteRecoveryReplicatedVm#key_encryption_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption.__init__)
            check_type(argname="argument disk_encryption_key", value=disk_encryption_key, expected_type=type_hints["disk_encryption_key"])
            check_type(argname="argument key_encryption_key", value=key_encryption_key, expected_type=type_hints["key_encryption_key"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disk_encryption_key is not None:
            self._values["disk_encryption_key"] = disk_encryption_key
        if key_encryption_key is not None:
            self._values["key_encryption_key"] = key_encryption_key

    @builtins.property
    def disk_encryption_key(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#disk_encryption_key SiteRecoveryReplicatedVm#disk_encryption_key}.'''
        result = self._values.get("disk_encryption_key")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey"]]], result)

    @builtins.property
    def key_encryption_key(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#key_encryption_key SiteRecoveryReplicatedVm#key_encryption_key}.'''
        result = self._values.get("key_encryption_key")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"secret_url": "secretUrl", "vault_id": "vaultId"},
)
class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey:
    def __init__(
        self,
        *,
        secret_url: typing.Optional[builtins.str] = None,
        vault_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#secret_url SiteRecoveryReplicatedVm#secret_url}.
        :param vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#vault_id SiteRecoveryReplicatedVm#vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey.__init__)
            check_type(argname="argument secret_url", value=secret_url, expected_type=type_hints["secret_url"])
            check_type(argname="argument vault_id", value=vault_id, expected_type=type_hints["vault_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if secret_url is not None:
            self._values["secret_url"] = secret_url
        if vault_id is not None:
            self._values["vault_id"] = vault_id

    @builtins.property
    def secret_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#secret_url SiteRecoveryReplicatedVm#secret_url}.'''
        result = self._values.get("secret_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#vault_id SiteRecoveryReplicatedVm#vault_id}.'''
        result = self._values.get("vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSecretUrl")
    def reset_secret_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretUrl", []))

    @jsii.member(jsii_name="resetVaultId")
    def reset_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVaultId", []))

    @builtins.property
    @jsii.member(jsii_name="secretUrlInput")
    def secret_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultIdInput")
    def vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="secretUrl")
    def secret_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretUrl"))

    @secret_url.setter
    def secret_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference, "secret_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretUrl", value)

    @builtins.property
    @jsii.member(jsii_name="vaultId")
    def vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultId"))

    @vault_id.setter
    def vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference, "vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey",
    jsii_struct_bases=[],
    name_mapping={"key_url": "keyUrl", "vault_id": "vaultId"},
)
class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey:
    def __init__(
        self,
        *,
        key_url: typing.Optional[builtins.str] = None,
        vault_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#key_url SiteRecoveryReplicatedVm#key_url}.
        :param vault_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#vault_id SiteRecoveryReplicatedVm#vault_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey.__init__)
            check_type(argname="argument key_url", value=key_url, expected_type=type_hints["key_url"])
            check_type(argname="argument vault_id", value=vault_id, expected_type=type_hints["vault_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key_url is not None:
            self._values["key_url"] = key_url
        if vault_id is not None:
            self._values["vault_id"] = vault_id

    @builtins.property
    def key_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#key_url SiteRecoveryReplicatedVm#key_url}.'''
        result = self._values.get("key_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vault_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#vault_id SiteRecoveryReplicatedVm#vault_id}.'''
        result = self._values.get("vault_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKeyUrl")
    def reset_key_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyUrl", []))

    @jsii.member(jsii_name="resetVaultId")
    def reset_vault_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVaultId", []))

    @builtins.property
    @jsii.member(jsii_name="keyUrlInput")
    def key_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultIdInput")
    def vault_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyUrl")
    def key_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyUrl"))

    @key_url.setter
    def key_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference, "key_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="vaultId")
    def vault_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultId"))

    @vault_id.setter
    def vault_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference, "vault_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vaultId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDiskEncryptionKey")
    def put_disk_encryption_key(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference.put_disk_encryption_key)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDiskEncryptionKey", [value]))

    @jsii.member(jsii_name="putKeyEncryptionKey")
    def put_key_encryption_key(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference.put_key_encryption_key)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKeyEncryptionKey", [value]))

    @jsii.member(jsii_name="resetDiskEncryptionKey")
    def reset_disk_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryptionKey", []))

    @jsii.member(jsii_name="resetKeyEncryptionKey")
    def reset_key_encryption_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyEncryptionKey", []))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKey")
    def disk_encryption_key(
        self,
    ) -> SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList:
        return typing.cast(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList, jsii.get(self, "diskEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="keyEncryptionKey")
    def key_encryption_key(
        self,
    ) -> SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList:
        return typing.cast(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList, jsii.get(self, "keyEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionKeyInput")
    def disk_encryption_key_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey]]], jsii.get(self, "diskEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="keyEncryptionKeyInput")
    def key_encryption_key_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey]]], jsii.get(self, "keyEncryptionKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmNetworkInterface",
    jsii_struct_bases=[],
    name_mapping={
        "recovery_public_ip_address_id": "recoveryPublicIpAddressId",
        "source_network_interface_id": "sourceNetworkInterfaceId",
        "target_static_ip": "targetStaticIp",
        "target_subnet_name": "targetSubnetName",
    },
)
class SiteRecoveryReplicatedVmNetworkInterface:
    def __init__(
        self,
        *,
        recovery_public_ip_address_id: typing.Optional[builtins.str] = None,
        source_network_interface_id: typing.Optional[builtins.str] = None,
        target_static_ip: typing.Optional[builtins.str] = None,
        target_subnet_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param recovery_public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_public_ip_address_id SiteRecoveryReplicatedVm#recovery_public_ip_address_id}.
        :param source_network_interface_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_network_interface_id SiteRecoveryReplicatedVm#source_network_interface_id}.
        :param target_static_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_static_ip SiteRecoveryReplicatedVm#target_static_ip}.
        :param target_subnet_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_subnet_name SiteRecoveryReplicatedVm#target_subnet_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmNetworkInterface.__init__)
            check_type(argname="argument recovery_public_ip_address_id", value=recovery_public_ip_address_id, expected_type=type_hints["recovery_public_ip_address_id"])
            check_type(argname="argument source_network_interface_id", value=source_network_interface_id, expected_type=type_hints["source_network_interface_id"])
            check_type(argname="argument target_static_ip", value=target_static_ip, expected_type=type_hints["target_static_ip"])
            check_type(argname="argument target_subnet_name", value=target_subnet_name, expected_type=type_hints["target_subnet_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if recovery_public_ip_address_id is not None:
            self._values["recovery_public_ip_address_id"] = recovery_public_ip_address_id
        if source_network_interface_id is not None:
            self._values["source_network_interface_id"] = source_network_interface_id
        if target_static_ip is not None:
            self._values["target_static_ip"] = target_static_ip
        if target_subnet_name is not None:
            self._values["target_subnet_name"] = target_subnet_name

    @builtins.property
    def recovery_public_ip_address_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#recovery_public_ip_address_id SiteRecoveryReplicatedVm#recovery_public_ip_address_id}.'''
        result = self._values.get("recovery_public_ip_address_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_network_interface_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#source_network_interface_id SiteRecoveryReplicatedVm#source_network_interface_id}.'''
        result = self._values.get("source_network_interface_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_static_ip(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_static_ip SiteRecoveryReplicatedVm#target_static_ip}.'''
        result = self._values.get("target_static_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_subnet_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#target_subnet_name SiteRecoveryReplicatedVm#target_subnet_name}.'''
        result = self._values.get("target_subnet_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryReplicatedVmNetworkInterface(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SiteRecoveryReplicatedVmNetworkInterfaceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmNetworkInterfaceList",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmNetworkInterfaceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SiteRecoveryReplicatedVmNetworkInterfaceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmNetworkInterfaceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SiteRecoveryReplicatedVmNetworkInterfaceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmNetworkInterface]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmNetworkInterface]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SiteRecoveryReplicatedVmNetworkInterface]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SiteRecoveryReplicatedVmNetworkInterfaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmNetworkInterfaceOutputReference",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmNetworkInterfaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRecoveryPublicIpAddressId")
    def reset_recovery_public_ip_address_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecoveryPublicIpAddressId", []))

    @jsii.member(jsii_name="resetSourceNetworkInterfaceId")
    def reset_source_network_interface_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceNetworkInterfaceId", []))

    @jsii.member(jsii_name="resetTargetStaticIp")
    def reset_target_static_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetStaticIp", []))

    @jsii.member(jsii_name="resetTargetSubnetName")
    def reset_target_subnet_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetSubnetName", []))

    @builtins.property
    @jsii.member(jsii_name="recoveryPublicIpAddressIdInput")
    def recovery_public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryPublicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceNetworkInterfaceIdInput")
    def source_network_interface_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceNetworkInterfaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="targetStaticIpInput")
    def target_static_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetStaticIpInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSubnetNameInput")
    def target_subnet_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetSubnetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryPublicIpAddressId")
    def recovery_public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryPublicIpAddressId"))

    @recovery_public_ip_address_id.setter
    def recovery_public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceOutputReference, "recovery_public_ip_address_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryPublicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="sourceNetworkInterfaceId")
    def source_network_interface_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceNetworkInterfaceId"))

    @source_network_interface_id.setter
    def source_network_interface_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceOutputReference, "source_network_interface_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceNetworkInterfaceId", value)

    @builtins.property
    @jsii.member(jsii_name="targetStaticIp")
    def target_static_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetStaticIp"))

    @target_static_ip.setter
    def target_static_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceOutputReference, "target_static_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetStaticIp", value)

    @builtins.property
    @jsii.member(jsii_name="targetSubnetName")
    def target_subnet_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetSubnetName"))

    @target_subnet_name.setter
    def target_subnet_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceOutputReference, "target_subnet_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSubnetName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SiteRecoveryReplicatedVmNetworkInterface, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SiteRecoveryReplicatedVmNetworkInterface, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SiteRecoveryReplicatedVmNetworkInterface, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmNetworkInterfaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SiteRecoveryReplicatedVmTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#create SiteRecoveryReplicatedVm#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#delete SiteRecoveryReplicatedVm#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#read SiteRecoveryReplicatedVm#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#update SiteRecoveryReplicatedVm#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#create SiteRecoveryReplicatedVm#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#delete SiteRecoveryReplicatedVm#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#read SiteRecoveryReplicatedVm#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/site_recovery_replicated_vm#update SiteRecoveryReplicatedVm#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteRecoveryReplicatedVmTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SiteRecoveryReplicatedVmTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.siteRecoveryReplicatedVm.SiteRecoveryReplicatedVmTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SiteRecoveryReplicatedVmTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SiteRecoveryReplicatedVmTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SiteRecoveryReplicatedVmTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SiteRecoveryReplicatedVmTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SiteRecoveryReplicatedVmTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SiteRecoveryReplicatedVm",
    "SiteRecoveryReplicatedVmConfig",
    "SiteRecoveryReplicatedVmManagedDisk",
    "SiteRecoveryReplicatedVmManagedDiskList",
    "SiteRecoveryReplicatedVmManagedDiskOutputReference",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryption",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKey",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyList",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionDiskEncryptionKeyOutputReference",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKey",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyList",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionKeyEncryptionKeyOutputReference",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionList",
    "SiteRecoveryReplicatedVmManagedDiskTargetDiskEncryptionOutputReference",
    "SiteRecoveryReplicatedVmNetworkInterface",
    "SiteRecoveryReplicatedVmNetworkInterfaceList",
    "SiteRecoveryReplicatedVmNetworkInterfaceOutputReference",
    "SiteRecoveryReplicatedVmTimeouts",
    "SiteRecoveryReplicatedVmTimeoutsOutputReference",
]

publication.publish()
