'''
# `azurerm_backup_policy_vm_workload`

Refer to the Terraform Registory for docs: [`azurerm_backup_policy_vm_workload`](https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload).
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


class BackupPolicyVmWorkload(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkload",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload azurerm_backup_policy_vm_workload}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        protection_policy: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BackupPolicyVmWorkloadProtectionPolicy", typing.Dict[str, typing.Any]]]],
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        settings: typing.Union["BackupPolicyVmWorkloadSettings", typing.Dict[str, typing.Any]],
        workload_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["BackupPolicyVmWorkloadTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload azurerm_backup_policy_vm_workload} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#name BackupPolicyVmWorkload#name}.
        :param protection_policy: protection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#protection_policy BackupPolicyVmWorkload#protection_policy}
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#recovery_vault_name BackupPolicyVmWorkload#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#resource_group_name BackupPolicyVmWorkload#resource_group_name}.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#settings BackupPolicyVmWorkload#settings}
        :param workload_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#workload_type BackupPolicyVmWorkload#workload_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#id BackupPolicyVmWorkload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#timeouts BackupPolicyVmWorkload#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkload.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BackupPolicyVmWorkloadConfig(
            name=name,
            protection_policy=protection_policy,
            recovery_vault_name=recovery_vault_name,
            resource_group_name=resource_group_name,
            settings=settings,
            workload_type=workload_type,
            id=id,
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

    @jsii.member(jsii_name="putProtectionPolicy")
    def put_protection_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BackupPolicyVmWorkloadProtectionPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkload.put_protection_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putProtectionPolicy", [value]))

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        *,
        time_zone: builtins.str,
        compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#time_zone BackupPolicyVmWorkload#time_zone}.
        :param compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#compression_enabled BackupPolicyVmWorkload#compression_enabled}.
        '''
        value = BackupPolicyVmWorkloadSettings(
            time_zone=time_zone, compression_enabled=compression_enabled
        )

        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#create BackupPolicyVmWorkload#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#delete BackupPolicyVmWorkload#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#read BackupPolicyVmWorkload#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#update BackupPolicyVmWorkload#update}.
        '''
        value = BackupPolicyVmWorkloadTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="protectionPolicy")
    def protection_policy(self) -> "BackupPolicyVmWorkloadProtectionPolicyList":
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicyList", jsii.get(self, "protectionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "BackupPolicyVmWorkloadSettingsOutputReference":
        return typing.cast("BackupPolicyVmWorkloadSettingsOutputReference", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "BackupPolicyVmWorkloadTimeoutsOutputReference":
        return typing.cast("BackupPolicyVmWorkloadTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protectionPolicyInput")
    def protection_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BackupPolicyVmWorkloadProtectionPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BackupPolicyVmWorkloadProtectionPolicy"]]], jsii.get(self, "protectionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultNameInput")
    def recovery_vault_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryVaultNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional["BackupPolicyVmWorkloadSettings"]:
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadSettings"], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["BackupPolicyVmWorkloadTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["BackupPolicyVmWorkloadTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadTypeInput")
    def workload_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workloadTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkload, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkload, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultName")
    def recovery_vault_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryVaultName"))

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkload, "recovery_vault_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryVaultName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkload, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="workloadType")
    def workload_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workloadType"))

    @workload_type.setter
    def workload_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkload, "workload_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadConfig",
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
        "protection_policy": "protectionPolicy",
        "recovery_vault_name": "recoveryVaultName",
        "resource_group_name": "resourceGroupName",
        "settings": "settings",
        "workload_type": "workloadType",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class BackupPolicyVmWorkloadConfig(cdktf.TerraformMetaArguments):
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
        protection_policy: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BackupPolicyVmWorkloadProtectionPolicy", typing.Dict[str, typing.Any]]]],
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        settings: typing.Union["BackupPolicyVmWorkloadSettings", typing.Dict[str, typing.Any]],
        workload_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["BackupPolicyVmWorkloadTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#name BackupPolicyVmWorkload#name}.
        :param protection_policy: protection_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#protection_policy BackupPolicyVmWorkload#protection_policy}
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#recovery_vault_name BackupPolicyVmWorkload#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#resource_group_name BackupPolicyVmWorkload#resource_group_name}.
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#settings BackupPolicyVmWorkload#settings}
        :param workload_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#workload_type BackupPolicyVmWorkload#workload_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#id BackupPolicyVmWorkload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#timeouts BackupPolicyVmWorkload#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(settings, dict):
            settings = BackupPolicyVmWorkloadSettings(**settings)
        if isinstance(timeouts, dict):
            timeouts = BackupPolicyVmWorkloadTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protection_policy", value=protection_policy, expected_type=type_hints["protection_policy"])
            check_type(argname="argument recovery_vault_name", value=recovery_vault_name, expected_type=type_hints["recovery_vault_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument workload_type", value=workload_type, expected_type=type_hints["workload_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "protection_policy": protection_policy,
            "recovery_vault_name": recovery_vault_name,
            "resource_group_name": resource_group_name,
            "settings": settings,
            "workload_type": workload_type,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#name BackupPolicyVmWorkload#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protection_policy(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["BackupPolicyVmWorkloadProtectionPolicy"]]:
        '''protection_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#protection_policy BackupPolicyVmWorkload#protection_policy}
        '''
        result = self._values.get("protection_policy")
        assert result is not None, "Required property 'protection_policy' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["BackupPolicyVmWorkloadProtectionPolicy"]], result)

    @builtins.property
    def recovery_vault_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#recovery_vault_name BackupPolicyVmWorkload#recovery_vault_name}.'''
        result = self._values.get("recovery_vault_name")
        assert result is not None, "Required property 'recovery_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#resource_group_name BackupPolicyVmWorkload#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def settings(self) -> "BackupPolicyVmWorkloadSettings":
        '''settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#settings BackupPolicyVmWorkload#settings}
        '''
        result = self._values.get("settings")
        assert result is not None, "Required property 'settings' is missing"
        return typing.cast("BackupPolicyVmWorkloadSettings", result)

    @builtins.property
    def workload_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#workload_type BackupPolicyVmWorkload#workload_type}.'''
        result = self._values.get("workload_type")
        assert result is not None, "Required property 'workload_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#id BackupPolicyVmWorkload#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["BackupPolicyVmWorkloadTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#timeouts BackupPolicyVmWorkload#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "backup": "backup",
        "policy_type": "policyType",
        "retention_daily": "retentionDaily",
        "retention_monthly": "retentionMonthly",
        "retention_weekly": "retentionWeekly",
        "retention_yearly": "retentionYearly",
        "simple_retention": "simpleRetention",
    },
)
class BackupPolicyVmWorkloadProtectionPolicy:
    def __init__(
        self,
        *,
        backup: typing.Union["BackupPolicyVmWorkloadProtectionPolicyBackup", typing.Dict[str, typing.Any]],
        policy_type: builtins.str,
        retention_daily: typing.Optional[typing.Union["BackupPolicyVmWorkloadProtectionPolicyRetentionDaily", typing.Dict[str, typing.Any]]] = None,
        retention_monthly: typing.Optional[typing.Union["BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly", typing.Dict[str, typing.Any]]] = None,
        retention_weekly: typing.Optional[typing.Union["BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly", typing.Dict[str, typing.Any]]] = None,
        retention_yearly: typing.Optional[typing.Union["BackupPolicyVmWorkloadProtectionPolicyRetentionYearly", typing.Dict[str, typing.Any]]] = None,
        simple_retention: typing.Optional[typing.Union["BackupPolicyVmWorkloadProtectionPolicySimpleRetention", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#backup BackupPolicyVmWorkload#backup}
        :param policy_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#policy_type BackupPolicyVmWorkload#policy_type}.
        :param retention_daily: retention_daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_daily BackupPolicyVmWorkload#retention_daily}
        :param retention_monthly: retention_monthly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_monthly BackupPolicyVmWorkload#retention_monthly}
        :param retention_weekly: retention_weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_weekly BackupPolicyVmWorkload#retention_weekly}
        :param retention_yearly: retention_yearly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_yearly BackupPolicyVmWorkload#retention_yearly}
        :param simple_retention: simple_retention block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#simple_retention BackupPolicyVmWorkload#simple_retention}
        '''
        if isinstance(backup, dict):
            backup = BackupPolicyVmWorkloadProtectionPolicyBackup(**backup)
        if isinstance(retention_daily, dict):
            retention_daily = BackupPolicyVmWorkloadProtectionPolicyRetentionDaily(**retention_daily)
        if isinstance(retention_monthly, dict):
            retention_monthly = BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly(**retention_monthly)
        if isinstance(retention_weekly, dict):
            retention_weekly = BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly(**retention_weekly)
        if isinstance(retention_yearly, dict):
            retention_yearly = BackupPolicyVmWorkloadProtectionPolicyRetentionYearly(**retention_yearly)
        if isinstance(simple_retention, dict):
            simple_retention = BackupPolicyVmWorkloadProtectionPolicySimpleRetention(**simple_retention)
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicy.__init__)
            check_type(argname="argument backup", value=backup, expected_type=type_hints["backup"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            check_type(argname="argument retention_daily", value=retention_daily, expected_type=type_hints["retention_daily"])
            check_type(argname="argument retention_monthly", value=retention_monthly, expected_type=type_hints["retention_monthly"])
            check_type(argname="argument retention_weekly", value=retention_weekly, expected_type=type_hints["retention_weekly"])
            check_type(argname="argument retention_yearly", value=retention_yearly, expected_type=type_hints["retention_yearly"])
            check_type(argname="argument simple_retention", value=simple_retention, expected_type=type_hints["simple_retention"])
        self._values: typing.Dict[str, typing.Any] = {
            "backup": backup,
            "policy_type": policy_type,
        }
        if retention_daily is not None:
            self._values["retention_daily"] = retention_daily
        if retention_monthly is not None:
            self._values["retention_monthly"] = retention_monthly
        if retention_weekly is not None:
            self._values["retention_weekly"] = retention_weekly
        if retention_yearly is not None:
            self._values["retention_yearly"] = retention_yearly
        if simple_retention is not None:
            self._values["simple_retention"] = simple_retention

    @builtins.property
    def backup(self) -> "BackupPolicyVmWorkloadProtectionPolicyBackup":
        '''backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#backup BackupPolicyVmWorkload#backup}
        '''
        result = self._values.get("backup")
        assert result is not None, "Required property 'backup' is missing"
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicyBackup", result)

    @builtins.property
    def policy_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#policy_type BackupPolicyVmWorkload#policy_type}.'''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_daily(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionDaily"]:
        '''retention_daily block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_daily BackupPolicyVmWorkload#retention_daily}
        '''
        result = self._values.get("retention_daily")
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionDaily"], result)

    @builtins.property
    def retention_monthly(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly"]:
        '''retention_monthly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_monthly BackupPolicyVmWorkload#retention_monthly}
        '''
        result = self._values.get("retention_monthly")
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly"], result)

    @builtins.property
    def retention_weekly(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly"]:
        '''retention_weekly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_weekly BackupPolicyVmWorkload#retention_weekly}
        '''
        result = self._values.get("retention_weekly")
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly"], result)

    @builtins.property
    def retention_yearly(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionYearly"]:
        '''retention_yearly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#retention_yearly BackupPolicyVmWorkload#retention_yearly}
        '''
        result = self._values.get("retention_yearly")
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionYearly"], result)

    @builtins.property
    def simple_retention(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicySimpleRetention"]:
        '''simple_retention block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#simple_retention BackupPolicyVmWorkload#simple_retention}
        '''
        result = self._values.get("simple_retention")
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicySimpleRetention"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadProtectionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyBackup",
    jsii_struct_bases=[],
    name_mapping={
        "frequency": "frequency",
        "frequency_in_minutes": "frequencyInMinutes",
        "time": "time",
        "weekdays": "weekdays",
    },
)
class BackupPolicyVmWorkloadProtectionPolicyBackup:
    def __init__(
        self,
        *,
        frequency: typing.Optional[builtins.str] = None,
        frequency_in_minutes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
        weekdays: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#frequency BackupPolicyVmWorkload#frequency}.
        :param frequency_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#frequency_in_minutes BackupPolicyVmWorkload#frequency_in_minutes}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#time BackupPolicyVmWorkload#time}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyBackup.__init__)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument frequency_in_minutes", value=frequency_in_minutes, expected_type=type_hints["frequency_in_minutes"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
        self._values: typing.Dict[str, typing.Any] = {}
        if frequency is not None:
            self._values["frequency"] = frequency
        if frequency_in_minutes is not None:
            self._values["frequency_in_minutes"] = frequency_in_minutes
        if time is not None:
            self._values["time"] = time
        if weekdays is not None:
            self._values["weekdays"] = weekdays

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#frequency BackupPolicyVmWorkload#frequency}.'''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frequency_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#frequency_in_minutes BackupPolicyVmWorkload#frequency_in_minutes}.'''
        result = self._values.get("frequency_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#time BackupPolicyVmWorkload#time}.'''
        result = self._values.get("time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekdays(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.'''
        result = self._values.get("weekdays")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadProtectionPolicyBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetFrequencyInMinutes")
    def reset_frequency_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequencyInMinutes", []))

    @jsii.member(jsii_name="resetTime")
    def reset_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTime", []))

    @jsii.member(jsii_name="resetWeekdays")
    def reset_weekdays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekdays", []))

    @builtins.property
    @jsii.member(jsii_name="frequencyInMinutesInput")
    def frequency_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frequencyInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="weekdaysInput")
    def weekdays_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "weekdaysInput"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="frequencyInMinutes")
    def frequency_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequencyInMinutes"))

    @frequency_in_minutes.setter
    def frequency_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference, "frequency_in_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequencyInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BackupPolicyVmWorkloadProtectionPolicyBackup]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadProtectionPolicyBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyVmWorkloadProtectionPolicyBackup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BackupPolicyVmWorkloadProtectionPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyList",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BackupPolicyVmWorkloadProtectionPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BackupPolicyVmWorkloadProtectionPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BackupPolicyVmWorkloadProtectionPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BackupPolicyVmWorkloadProtectionPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BackupPolicyVmWorkloadProtectionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackup")
    def put_backup(
        self,
        *,
        frequency: typing.Optional[builtins.str] = None,
        frequency_in_minutes: typing.Optional[jsii.Number] = None,
        time: typing.Optional[builtins.str] = None,
        weekdays: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#frequency BackupPolicyVmWorkload#frequency}.
        :param frequency_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#frequency_in_minutes BackupPolicyVmWorkload#frequency_in_minutes}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#time BackupPolicyVmWorkload#time}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        '''
        value = BackupPolicyVmWorkloadProtectionPolicyBackup(
            frequency=frequency,
            frequency_in_minutes=frequency_in_minutes,
            time=time,
            weekdays=weekdays,
        )

        return typing.cast(None, jsii.invoke(self, "putBackup", [value]))

    @jsii.member(jsii_name="putRetentionDaily")
    def put_retention_daily(self, *, count: jsii.Number) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        '''
        value = BackupPolicyVmWorkloadProtectionPolicyRetentionDaily(count=count)

        return typing.cast(None, jsii.invoke(self, "putRetentionDaily", [value]))

    @jsii.member(jsii_name="putRetentionMonthly")
    def put_retention_monthly(
        self,
        *,
        count: jsii.Number,
        format_type: builtins.str,
        monthdays: typing.Optional[typing.Sequence[jsii.Number]] = None,
        weekdays: typing.Optional[typing.Sequence[builtins.str]] = None,
        weeks: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        :param format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#format_type BackupPolicyVmWorkload#format_type}.
        :param monthdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#monthdays BackupPolicyVmWorkload#monthdays}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weeks BackupPolicyVmWorkload#weeks}.
        '''
        value = BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly(
            count=count,
            format_type=format_type,
            monthdays=monthdays,
            weekdays=weekdays,
            weeks=weeks,
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionMonthly", [value]))

    @jsii.member(jsii_name="putRetentionWeekly")
    def put_retention_weekly(
        self,
        *,
        count: jsii.Number,
        weekdays: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        '''
        value = BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly(
            count=count, weekdays=weekdays
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionWeekly", [value]))

    @jsii.member(jsii_name="putRetentionYearly")
    def put_retention_yearly(
        self,
        *,
        count: jsii.Number,
        format_type: builtins.str,
        months: typing.Sequence[builtins.str],
        monthdays: typing.Optional[typing.Sequence[jsii.Number]] = None,
        weekdays: typing.Optional[typing.Sequence[builtins.str]] = None,
        weeks: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        :param format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#format_type BackupPolicyVmWorkload#format_type}.
        :param months: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#months BackupPolicyVmWorkload#months}.
        :param monthdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#monthdays BackupPolicyVmWorkload#monthdays}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weeks BackupPolicyVmWorkload#weeks}.
        '''
        value = BackupPolicyVmWorkloadProtectionPolicyRetentionYearly(
            count=count,
            format_type=format_type,
            months=months,
            monthdays=monthdays,
            weekdays=weekdays,
            weeks=weeks,
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionYearly", [value]))

    @jsii.member(jsii_name="putSimpleRetention")
    def put_simple_retention(self, *, count: jsii.Number) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        '''
        value = BackupPolicyVmWorkloadProtectionPolicySimpleRetention(count=count)

        return typing.cast(None, jsii.invoke(self, "putSimpleRetention", [value]))

    @jsii.member(jsii_name="resetRetentionDaily")
    def reset_retention_daily(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionDaily", []))

    @jsii.member(jsii_name="resetRetentionMonthly")
    def reset_retention_monthly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionMonthly", []))

    @jsii.member(jsii_name="resetRetentionWeekly")
    def reset_retention_weekly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionWeekly", []))

    @jsii.member(jsii_name="resetRetentionYearly")
    def reset_retention_yearly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionYearly", []))

    @jsii.member(jsii_name="resetSimpleRetention")
    def reset_simple_retention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSimpleRetention", []))

    @builtins.property
    @jsii.member(jsii_name="backup")
    def backup(self) -> BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference:
        return typing.cast(BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference, jsii.get(self, "backup"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaily")
    def retention_daily(
        self,
    ) -> "BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference":
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference", jsii.get(self, "retentionDaily"))

    @builtins.property
    @jsii.member(jsii_name="retentionMonthly")
    def retention_monthly(
        self,
    ) -> "BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference":
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference", jsii.get(self, "retentionMonthly"))

    @builtins.property
    @jsii.member(jsii_name="retentionWeekly")
    def retention_weekly(
        self,
    ) -> "BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference":
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference", jsii.get(self, "retentionWeekly"))

    @builtins.property
    @jsii.member(jsii_name="retentionYearly")
    def retention_yearly(
        self,
    ) -> "BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference":
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference", jsii.get(self, "retentionYearly"))

    @builtins.property
    @jsii.member(jsii_name="simpleRetention")
    def simple_retention(
        self,
    ) -> "BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference":
        return typing.cast("BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference", jsii.get(self, "simpleRetention"))

    @builtins.property
    @jsii.member(jsii_name="backupInput")
    def backup_input(
        self,
    ) -> typing.Optional[BackupPolicyVmWorkloadProtectionPolicyBackup]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadProtectionPolicyBackup], jsii.get(self, "backupInput"))

    @builtins.property
    @jsii.member(jsii_name="policyTypeInput")
    def policy_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDailyInput")
    def retention_daily_input(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionDaily"]:
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionDaily"], jsii.get(self, "retentionDailyInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionMonthlyInput")
    def retention_monthly_input(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly"]:
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly"], jsii.get(self, "retentionMonthlyInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionWeeklyInput")
    def retention_weekly_input(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly"]:
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly"], jsii.get(self, "retentionWeeklyInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionYearlyInput")
    def retention_yearly_input(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionYearly"]:
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicyRetentionYearly"], jsii.get(self, "retentionYearlyInput"))

    @builtins.property
    @jsii.member(jsii_name="simpleRetentionInput")
    def simple_retention_input(
        self,
    ) -> typing.Optional["BackupPolicyVmWorkloadProtectionPolicySimpleRetention"]:
        return typing.cast(typing.Optional["BackupPolicyVmWorkloadProtectionPolicySimpleRetention"], jsii.get(self, "simpleRetentionInput"))

    @builtins.property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyType"))

    @policy_type.setter
    def policy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyOutputReference, "policy_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BackupPolicyVmWorkloadProtectionPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BackupPolicyVmWorkloadProtectionPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BackupPolicyVmWorkloadProtectionPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionDaily",
    jsii_struct_bases=[],
    name_mapping={"count": "count"},
)
class BackupPolicyVmWorkloadProtectionPolicyRetentionDaily:
    def __init__(self, *, count: jsii.Number) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionDaily.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadProtectionPolicyRetentionDaily(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionDaily]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionDaily], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionDaily],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "format_type": "formatType",
        "monthdays": "monthdays",
        "weekdays": "weekdays",
        "weeks": "weeks",
    },
)
class BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly:
    def __init__(
        self,
        *,
        count: jsii.Number,
        format_type: builtins.str,
        monthdays: typing.Optional[typing.Sequence[jsii.Number]] = None,
        weekdays: typing.Optional[typing.Sequence[builtins.str]] = None,
        weeks: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        :param format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#format_type BackupPolicyVmWorkload#format_type}.
        :param monthdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#monthdays BackupPolicyVmWorkload#monthdays}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weeks BackupPolicyVmWorkload#weeks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument format_type", value=format_type, expected_type=type_hints["format_type"])
            check_type(argname="argument monthdays", value=monthdays, expected_type=type_hints["monthdays"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
            check_type(argname="argument weeks", value=weeks, expected_type=type_hints["weeks"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "format_type": format_type,
        }
        if monthdays is not None:
            self._values["monthdays"] = monthdays
        if weekdays is not None:
            self._values["weekdays"] = weekdays
        if weeks is not None:
            self._values["weeks"] = weeks

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def format_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#format_type BackupPolicyVmWorkload#format_type}.'''
        result = self._values.get("format_type")
        assert result is not None, "Required property 'format_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monthdays(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#monthdays BackupPolicyVmWorkload#monthdays}.'''
        result = self._values.get("monthdays")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def weekdays(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.'''
        result = self._values.get("weekdays")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def weeks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weeks BackupPolicyVmWorkload#weeks}.'''
        result = self._values.get("weeks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMonthdays")
    def reset_monthdays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthdays", []))

    @jsii.member(jsii_name="resetWeekdays")
    def reset_weekdays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekdays", []))

    @jsii.member(jsii_name="resetWeeks")
    def reset_weeks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeks", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="formatTypeInput")
    def format_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="monthdaysInput")
    def monthdays_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "monthdaysInput"))

    @builtins.property
    @jsii.member(jsii_name="weekdaysInput")
    def weekdays_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "weekdaysInput"))

    @builtins.property
    @jsii.member(jsii_name="weeksInput")
    def weeks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "weeksInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="formatType")
    def format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "formatType"))

    @format_type.setter
    def format_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference, "format_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formatType", value)

    @builtins.property
    @jsii.member(jsii_name="monthdays")
    def monthdays(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "monthdays"))

    @monthdays.setter
    def monthdays(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference, "monthdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthdays", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="weeks")
    def weeks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weeks"))

    @weeks.setter
    def weeks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference, "weeks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "weekdays": "weekdays"},
)
class BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly:
    def __init__(
        self,
        *,
        count: jsii.Number,
        weekdays: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "weekdays": weekdays,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def weekdays(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.'''
        result = self._values.get("weekdays")
        assert result is not None, "Required property 'weekdays' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="weekdaysInput")
    def weekdays_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "weekdaysInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionYearly",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "format_type": "formatType",
        "months": "months",
        "monthdays": "monthdays",
        "weekdays": "weekdays",
        "weeks": "weeks",
    },
)
class BackupPolicyVmWorkloadProtectionPolicyRetentionYearly:
    def __init__(
        self,
        *,
        count: jsii.Number,
        format_type: builtins.str,
        months: typing.Sequence[builtins.str],
        monthdays: typing.Optional[typing.Sequence[jsii.Number]] = None,
        weekdays: typing.Optional[typing.Sequence[builtins.str]] = None,
        weeks: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        :param format_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#format_type BackupPolicyVmWorkload#format_type}.
        :param months: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#months BackupPolicyVmWorkload#months}.
        :param monthdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#monthdays BackupPolicyVmWorkload#monthdays}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weeks BackupPolicyVmWorkload#weeks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionYearly.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument format_type", value=format_type, expected_type=type_hints["format_type"])
            check_type(argname="argument months", value=months, expected_type=type_hints["months"])
            check_type(argname="argument monthdays", value=monthdays, expected_type=type_hints["monthdays"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
            check_type(argname="argument weeks", value=weeks, expected_type=type_hints["weeks"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "format_type": format_type,
            "months": months,
        }
        if monthdays is not None:
            self._values["monthdays"] = monthdays
        if weekdays is not None:
            self._values["weekdays"] = weekdays
        if weeks is not None:
            self._values["weeks"] = weeks

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def format_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#format_type BackupPolicyVmWorkload#format_type}.'''
        result = self._values.get("format_type")
        assert result is not None, "Required property 'format_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def months(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#months BackupPolicyVmWorkload#months}.'''
        result = self._values.get("months")
        assert result is not None, "Required property 'months' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def monthdays(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#monthdays BackupPolicyVmWorkload#monthdays}.'''
        result = self._values.get("monthdays")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def weekdays(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weekdays BackupPolicyVmWorkload#weekdays}.'''
        result = self._values.get("weekdays")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def weeks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#weeks BackupPolicyVmWorkload#weeks}.'''
        result = self._values.get("weeks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadProtectionPolicyRetentionYearly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMonthdays")
    def reset_monthdays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthdays", []))

    @jsii.member(jsii_name="resetWeekdays")
    def reset_weekdays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekdays", []))

    @jsii.member(jsii_name="resetWeeks")
    def reset_weeks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeks", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="formatTypeInput")
    def format_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="monthdaysInput")
    def monthdays_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "monthdaysInput"))

    @builtins.property
    @jsii.member(jsii_name="monthsInput")
    def months_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "monthsInput"))

    @builtins.property
    @jsii.member(jsii_name="weekdaysInput")
    def weekdays_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "weekdaysInput"))

    @builtins.property
    @jsii.member(jsii_name="weeksInput")
    def weeks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "weeksInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="formatType")
    def format_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "formatType"))

    @format_type.setter
    def format_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference, "format_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formatType", value)

    @builtins.property
    @jsii.member(jsii_name="monthdays")
    def monthdays(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "monthdays"))

    @monthdays.setter
    def monthdays(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference, "monthdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthdays", value)

    @builtins.property
    @jsii.member(jsii_name="months")
    def months(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "months"))

    @months.setter
    def months(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference, "months").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "months", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="weeks")
    def weeks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weeks"))

    @weeks.setter
    def weeks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference, "weeks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionYearly]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionYearly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyVmWorkloadProtectionPolicyRetentionYearly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicySimpleRetention",
    jsii_struct_bases=[],
    name_mapping={"count": "count"},
)
class BackupPolicyVmWorkloadProtectionPolicySimpleRetention:
    def __init__(self, *, count: jsii.Number) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicySimpleRetention.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#count BackupPolicyVmWorkload#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadProtectionPolicySimpleRetention(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[BackupPolicyVmWorkloadProtectionPolicySimpleRetention]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadProtectionPolicySimpleRetention], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyVmWorkloadProtectionPolicySimpleRetention],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadSettings",
    jsii_struct_bases=[],
    name_mapping={
        "time_zone": "timeZone",
        "compression_enabled": "compressionEnabled",
    },
)
class BackupPolicyVmWorkloadSettings:
    def __init__(
        self,
        *,
        time_zone: builtins.str,
        compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#time_zone BackupPolicyVmWorkload#time_zone}.
        :param compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#compression_enabled BackupPolicyVmWorkload#compression_enabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadSettings.__init__)
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument compression_enabled", value=compression_enabled, expected_type=type_hints["compression_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "time_zone": time_zone,
        }
        if compression_enabled is not None:
            self._values["compression_enabled"] = compression_enabled

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#time_zone BackupPolicyVmWorkload#time_zone}.'''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compression_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#compression_enabled BackupPolicyVmWorkload#compression_enabled}.'''
        result = self._values.get("compression_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadSettingsOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCompressionEnabled")
    def reset_compression_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="compressionEnabledInput")
    def compression_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "compressionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionEnabled")
    def compression_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "compressionEnabled"))

    @compression_enabled.setter
    def compression_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadSettingsOutputReference, "compression_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadSettingsOutputReference, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPolicyVmWorkloadSettings]:
        return typing.cast(typing.Optional[BackupPolicyVmWorkloadSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyVmWorkloadSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class BackupPolicyVmWorkloadTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#create BackupPolicyVmWorkload#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#delete BackupPolicyVmWorkload#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#read BackupPolicyVmWorkload#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#update BackupPolicyVmWorkload#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#create BackupPolicyVmWorkload#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#delete BackupPolicyVmWorkload#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#read BackupPolicyVmWorkload#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_vm_workload#update BackupPolicyVmWorkload#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyVmWorkloadTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyVmWorkloadTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyVmWorkload.BackupPolicyVmWorkloadTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyVmWorkloadTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BackupPolicyVmWorkloadTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BackupPolicyVmWorkloadTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BackupPolicyVmWorkloadTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyVmWorkloadTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BackupPolicyVmWorkload",
    "BackupPolicyVmWorkloadConfig",
    "BackupPolicyVmWorkloadProtectionPolicy",
    "BackupPolicyVmWorkloadProtectionPolicyBackup",
    "BackupPolicyVmWorkloadProtectionPolicyBackupOutputReference",
    "BackupPolicyVmWorkloadProtectionPolicyList",
    "BackupPolicyVmWorkloadProtectionPolicyOutputReference",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionDaily",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionDailyOutputReference",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionMonthly",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionMonthlyOutputReference",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionWeekly",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionWeeklyOutputReference",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionYearly",
    "BackupPolicyVmWorkloadProtectionPolicyRetentionYearlyOutputReference",
    "BackupPolicyVmWorkloadProtectionPolicySimpleRetention",
    "BackupPolicyVmWorkloadProtectionPolicySimpleRetentionOutputReference",
    "BackupPolicyVmWorkloadSettings",
    "BackupPolicyVmWorkloadSettingsOutputReference",
    "BackupPolicyVmWorkloadTimeouts",
    "BackupPolicyVmWorkloadTimeoutsOutputReference",
]

publication.publish()
