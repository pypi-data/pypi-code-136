'''
# `azurerm_backup_policy_file_share`

Refer to the Terraform Registory for docs: [`azurerm_backup_policy_file_share`](https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share).
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


class BackupPolicyFileShare(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShare",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share azurerm_backup_policy_file_share}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backup: typing.Union["BackupPolicyFileShareBackup", typing.Dict[str, typing.Any]],
        name: builtins.str,
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        retention_daily: typing.Union["BackupPolicyFileShareRetentionDaily", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        retention_monthly: typing.Optional[typing.Union["BackupPolicyFileShareRetentionMonthly", typing.Dict[str, typing.Any]]] = None,
        retention_weekly: typing.Optional[typing.Union["BackupPolicyFileShareRetentionWeekly", typing.Dict[str, typing.Any]]] = None,
        retention_yearly: typing.Optional[typing.Union["BackupPolicyFileShareRetentionYearly", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["BackupPolicyFileShareTimeouts", typing.Dict[str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share azurerm_backup_policy_file_share} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#backup BackupPolicyFileShare#backup}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#name BackupPolicyFileShare#name}.
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#recovery_vault_name BackupPolicyFileShare#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#resource_group_name BackupPolicyFileShare#resource_group_name}.
        :param retention_daily: retention_daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_daily BackupPolicyFileShare#retention_daily}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#id BackupPolicyFileShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param retention_monthly: retention_monthly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_monthly BackupPolicyFileShare#retention_monthly}
        :param retention_weekly: retention_weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_weekly BackupPolicyFileShare#retention_weekly}
        :param retention_yearly: retention_yearly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_yearly BackupPolicyFileShare#retention_yearly}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#timeouts BackupPolicyFileShare#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#timezone BackupPolicyFileShare#timezone}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShare.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BackupPolicyFileShareConfig(
            backup=backup,
            name=name,
            recovery_vault_name=recovery_vault_name,
            resource_group_name=resource_group_name,
            retention_daily=retention_daily,
            id=id,
            retention_monthly=retention_monthly,
            retention_weekly=retention_weekly,
            retention_yearly=retention_yearly,
            timeouts=timeouts,
            timezone=timezone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBackup")
    def put_backup(self, *, frequency: builtins.str, time: builtins.str) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#frequency BackupPolicyFileShare#frequency}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#time BackupPolicyFileShare#time}.
        '''
        value = BackupPolicyFileShareBackup(frequency=frequency, time=time)

        return typing.cast(None, jsii.invoke(self, "putBackup", [value]))

    @jsii.member(jsii_name="putRetentionDaily")
    def put_retention_daily(self, *, count: jsii.Number) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        '''
        value = BackupPolicyFileShareRetentionDaily(count=count)

        return typing.cast(None, jsii.invoke(self, "putRetentionDaily", [value]))

    @jsii.member(jsii_name="putRetentionMonthly")
    def put_retention_monthly(
        self,
        *,
        count: jsii.Number,
        weekdays: typing.Sequence[builtins.str],
        weeks: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weeks BackupPolicyFileShare#weeks}.
        '''
        value = BackupPolicyFileShareRetentionMonthly(
            count=count, weekdays=weekdays, weeks=weeks
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
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.
        '''
        value = BackupPolicyFileShareRetentionWeekly(count=count, weekdays=weekdays)

        return typing.cast(None, jsii.invoke(self, "putRetentionWeekly", [value]))

    @jsii.member(jsii_name="putRetentionYearly")
    def put_retention_yearly(
        self,
        *,
        count: jsii.Number,
        months: typing.Sequence[builtins.str],
        weekdays: typing.Sequence[builtins.str],
        weeks: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        :param months: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#months BackupPolicyFileShare#months}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weeks BackupPolicyFileShare#weeks}.
        '''
        value = BackupPolicyFileShareRetentionYearly(
            count=count, months=months, weekdays=weekdays, weeks=weeks
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionYearly", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#create BackupPolicyFileShare#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#delete BackupPolicyFileShare#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#read BackupPolicyFileShare#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#update BackupPolicyFileShare#update}.
        '''
        value = BackupPolicyFileShareTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRetentionMonthly")
    def reset_retention_monthly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionMonthly", []))

    @jsii.member(jsii_name="resetRetentionWeekly")
    def reset_retention_weekly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionWeekly", []))

    @jsii.member(jsii_name="resetRetentionYearly")
    def reset_retention_yearly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionYearly", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backup")
    def backup(self) -> "BackupPolicyFileShareBackupOutputReference":
        return typing.cast("BackupPolicyFileShareBackupOutputReference", jsii.get(self, "backup"))

    @builtins.property
    @jsii.member(jsii_name="retentionDaily")
    def retention_daily(self) -> "BackupPolicyFileShareRetentionDailyOutputReference":
        return typing.cast("BackupPolicyFileShareRetentionDailyOutputReference", jsii.get(self, "retentionDaily"))

    @builtins.property
    @jsii.member(jsii_name="retentionMonthly")
    def retention_monthly(
        self,
    ) -> "BackupPolicyFileShareRetentionMonthlyOutputReference":
        return typing.cast("BackupPolicyFileShareRetentionMonthlyOutputReference", jsii.get(self, "retentionMonthly"))

    @builtins.property
    @jsii.member(jsii_name="retentionWeekly")
    def retention_weekly(self) -> "BackupPolicyFileShareRetentionWeeklyOutputReference":
        return typing.cast("BackupPolicyFileShareRetentionWeeklyOutputReference", jsii.get(self, "retentionWeekly"))

    @builtins.property
    @jsii.member(jsii_name="retentionYearly")
    def retention_yearly(self) -> "BackupPolicyFileShareRetentionYearlyOutputReference":
        return typing.cast("BackupPolicyFileShareRetentionYearlyOutputReference", jsii.get(self, "retentionYearly"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "BackupPolicyFileShareTimeoutsOutputReference":
        return typing.cast("BackupPolicyFileShareTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backupInput")
    def backup_input(self) -> typing.Optional["BackupPolicyFileShareBackup"]:
        return typing.cast(typing.Optional["BackupPolicyFileShareBackup"], jsii.get(self, "backupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultNameInput")
    def recovery_vault_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recoveryVaultNameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionDailyInput")
    def retention_daily_input(
        self,
    ) -> typing.Optional["BackupPolicyFileShareRetentionDaily"]:
        return typing.cast(typing.Optional["BackupPolicyFileShareRetentionDaily"], jsii.get(self, "retentionDailyInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionMonthlyInput")
    def retention_monthly_input(
        self,
    ) -> typing.Optional["BackupPolicyFileShareRetentionMonthly"]:
        return typing.cast(typing.Optional["BackupPolicyFileShareRetentionMonthly"], jsii.get(self, "retentionMonthlyInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionWeeklyInput")
    def retention_weekly_input(
        self,
    ) -> typing.Optional["BackupPolicyFileShareRetentionWeekly"]:
        return typing.cast(typing.Optional["BackupPolicyFileShareRetentionWeekly"], jsii.get(self, "retentionWeeklyInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionYearlyInput")
    def retention_yearly_input(
        self,
    ) -> typing.Optional["BackupPolicyFileShareRetentionYearly"]:
        return typing.cast(typing.Optional["BackupPolicyFileShareRetentionYearly"], jsii.get(self, "retentionYearlyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["BackupPolicyFileShareTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["BackupPolicyFileShareTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShare, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShare, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recoveryVaultName")
    def recovery_vault_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recoveryVaultName"))

    @recovery_vault_name.setter
    def recovery_vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShare, "recovery_vault_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recoveryVaultName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShare, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShare, "timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareBackup",
    jsii_struct_bases=[],
    name_mapping={"frequency": "frequency", "time": "time"},
)
class BackupPolicyFileShareBackup:
    def __init__(self, *, frequency: builtins.str, time: builtins.str) -> None:
        '''
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#frequency BackupPolicyFileShare#frequency}.
        :param time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#time BackupPolicyFileShare#time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShareBackup.__init__)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "frequency": frequency,
            "time": time,
        }

    @builtins.property
    def frequency(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#frequency BackupPolicyFileShare#frequency}.'''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#time BackupPolicyFileShare#time}.'''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyFileShareBackup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyFileShareBackupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareBackupOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyFileShareBackupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareBackupOutputReference, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareBackupOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPolicyFileShareBackup]:
        return typing.cast(typing.Optional[BackupPolicyFileShareBackup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyFileShareBackup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareBackupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backup": "backup",
        "name": "name",
        "recovery_vault_name": "recoveryVaultName",
        "resource_group_name": "resourceGroupName",
        "retention_daily": "retentionDaily",
        "id": "id",
        "retention_monthly": "retentionMonthly",
        "retention_weekly": "retentionWeekly",
        "retention_yearly": "retentionYearly",
        "timeouts": "timeouts",
        "timezone": "timezone",
    },
)
class BackupPolicyFileShareConfig(cdktf.TerraformMetaArguments):
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
        backup: typing.Union[BackupPolicyFileShareBackup, typing.Dict[str, typing.Any]],
        name: builtins.str,
        recovery_vault_name: builtins.str,
        resource_group_name: builtins.str,
        retention_daily: typing.Union["BackupPolicyFileShareRetentionDaily", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        retention_monthly: typing.Optional[typing.Union["BackupPolicyFileShareRetentionMonthly", typing.Dict[str, typing.Any]]] = None,
        retention_weekly: typing.Optional[typing.Union["BackupPolicyFileShareRetentionWeekly", typing.Dict[str, typing.Any]]] = None,
        retention_yearly: typing.Optional[typing.Union["BackupPolicyFileShareRetentionYearly", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["BackupPolicyFileShareTimeouts", typing.Dict[str, typing.Any]]] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backup: backup block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#backup BackupPolicyFileShare#backup}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#name BackupPolicyFileShare#name}.
        :param recovery_vault_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#recovery_vault_name BackupPolicyFileShare#recovery_vault_name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#resource_group_name BackupPolicyFileShare#resource_group_name}.
        :param retention_daily: retention_daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_daily BackupPolicyFileShare#retention_daily}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#id BackupPolicyFileShare#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param retention_monthly: retention_monthly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_monthly BackupPolicyFileShare#retention_monthly}
        :param retention_weekly: retention_weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_weekly BackupPolicyFileShare#retention_weekly}
        :param retention_yearly: retention_yearly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_yearly BackupPolicyFileShare#retention_yearly}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#timeouts BackupPolicyFileShare#timeouts}
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#timezone BackupPolicyFileShare#timezone}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(backup, dict):
            backup = BackupPolicyFileShareBackup(**backup)
        if isinstance(retention_daily, dict):
            retention_daily = BackupPolicyFileShareRetentionDaily(**retention_daily)
        if isinstance(retention_monthly, dict):
            retention_monthly = BackupPolicyFileShareRetentionMonthly(**retention_monthly)
        if isinstance(retention_weekly, dict):
            retention_weekly = BackupPolicyFileShareRetentionWeekly(**retention_weekly)
        if isinstance(retention_yearly, dict):
            retention_yearly = BackupPolicyFileShareRetentionYearly(**retention_yearly)
        if isinstance(timeouts, dict):
            timeouts = BackupPolicyFileShareTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShareConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backup", value=backup, expected_type=type_hints["backup"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recovery_vault_name", value=recovery_vault_name, expected_type=type_hints["recovery_vault_name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument retention_daily", value=retention_daily, expected_type=type_hints["retention_daily"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument retention_monthly", value=retention_monthly, expected_type=type_hints["retention_monthly"])
            check_type(argname="argument retention_weekly", value=retention_weekly, expected_type=type_hints["retention_weekly"])
            check_type(argname="argument retention_yearly", value=retention_yearly, expected_type=type_hints["retention_yearly"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[str, typing.Any] = {
            "backup": backup,
            "name": name,
            "recovery_vault_name": recovery_vault_name,
            "resource_group_name": resource_group_name,
            "retention_daily": retention_daily,
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
        if retention_monthly is not None:
            self._values["retention_monthly"] = retention_monthly
        if retention_weekly is not None:
            self._values["retention_weekly"] = retention_weekly
        if retention_yearly is not None:
            self._values["retention_yearly"] = retention_yearly
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timezone is not None:
            self._values["timezone"] = timezone

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
    def backup(self) -> BackupPolicyFileShareBackup:
        '''backup block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#backup BackupPolicyFileShare#backup}
        '''
        result = self._values.get("backup")
        assert result is not None, "Required property 'backup' is missing"
        return typing.cast(BackupPolicyFileShareBackup, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#name BackupPolicyFileShare#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_vault_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#recovery_vault_name BackupPolicyFileShare#recovery_vault_name}.'''
        result = self._values.get("recovery_vault_name")
        assert result is not None, "Required property 'recovery_vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#resource_group_name BackupPolicyFileShare#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention_daily(self) -> "BackupPolicyFileShareRetentionDaily":
        '''retention_daily block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_daily BackupPolicyFileShare#retention_daily}
        '''
        result = self._values.get("retention_daily")
        assert result is not None, "Required property 'retention_daily' is missing"
        return typing.cast("BackupPolicyFileShareRetentionDaily", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#id BackupPolicyFileShare#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_monthly(
        self,
    ) -> typing.Optional["BackupPolicyFileShareRetentionMonthly"]:
        '''retention_monthly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_monthly BackupPolicyFileShare#retention_monthly}
        '''
        result = self._values.get("retention_monthly")
        return typing.cast(typing.Optional["BackupPolicyFileShareRetentionMonthly"], result)

    @builtins.property
    def retention_weekly(
        self,
    ) -> typing.Optional["BackupPolicyFileShareRetentionWeekly"]:
        '''retention_weekly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_weekly BackupPolicyFileShare#retention_weekly}
        '''
        result = self._values.get("retention_weekly")
        return typing.cast(typing.Optional["BackupPolicyFileShareRetentionWeekly"], result)

    @builtins.property
    def retention_yearly(
        self,
    ) -> typing.Optional["BackupPolicyFileShareRetentionYearly"]:
        '''retention_yearly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#retention_yearly BackupPolicyFileShare#retention_yearly}
        '''
        result = self._values.get("retention_yearly")
        return typing.cast(typing.Optional["BackupPolicyFileShareRetentionYearly"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["BackupPolicyFileShareTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#timeouts BackupPolicyFileShare#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["BackupPolicyFileShareTimeouts"], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#timezone BackupPolicyFileShare#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyFileShareConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionDaily",
    jsii_struct_bases=[],
    name_mapping={"count": "count"},
)
class BackupPolicyFileShareRetentionDaily:
    def __init__(self, *, count: jsii.Number) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionDaily.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyFileShareRetentionDaily(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyFileShareRetentionDailyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionDailyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionDailyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionDailyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPolicyFileShareRetentionDaily]:
        return typing.cast(typing.Optional[BackupPolicyFileShareRetentionDaily], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyFileShareRetentionDaily],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionDailyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionMonthly",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "weekdays": "weekdays", "weeks": "weeks"},
)
class BackupPolicyFileShareRetentionMonthly:
    def __init__(
        self,
        *,
        count: jsii.Number,
        weekdays: typing.Sequence[builtins.str],
        weeks: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weeks BackupPolicyFileShare#weeks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionMonthly.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
            check_type(argname="argument weeks", value=weeks, expected_type=type_hints["weeks"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "weekdays": weekdays,
            "weeks": weeks,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def weekdays(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.'''
        result = self._values.get("weekdays")
        assert result is not None, "Required property 'weekdays' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def weeks(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weeks BackupPolicyFileShare#weeks}.'''
        result = self._values.get("weeks")
        assert result is not None, "Required property 'weeks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyFileShareRetentionMonthly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyFileShareRetentionMonthlyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionMonthlyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionMonthlyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionMonthlyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionMonthlyOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="weeks")
    def weeks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weeks"))

    @weeks.setter
    def weeks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionMonthlyOutputReference, "weeks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPolicyFileShareRetentionMonthly]:
        return typing.cast(typing.Optional[BackupPolicyFileShareRetentionMonthly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyFileShareRetentionMonthly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionMonthlyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionWeekly",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "weekdays": "weekdays"},
)
class BackupPolicyFileShareRetentionWeekly:
    def __init__(
        self,
        *,
        count: jsii.Number,
        weekdays: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionWeekly.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "weekdays": weekdays,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def weekdays(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.'''
        result = self._values.get("weekdays")
        assert result is not None, "Required property 'weekdays' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyFileShareRetentionWeekly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyFileShareRetentionWeeklyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionWeeklyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionWeeklyOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionWeeklyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionWeeklyOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPolicyFileShareRetentionWeekly]:
        return typing.cast(typing.Optional[BackupPolicyFileShareRetentionWeekly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyFileShareRetentionWeekly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionWeeklyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionYearly",
    jsii_struct_bases=[],
    name_mapping={
        "count": "count",
        "months": "months",
        "weekdays": "weekdays",
        "weeks": "weeks",
    },
)
class BackupPolicyFileShareRetentionYearly:
    def __init__(
        self,
        *,
        count: jsii.Number,
        months: typing.Sequence[builtins.str],
        weekdays: typing.Sequence[builtins.str],
        weeks: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.
        :param months: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#months BackupPolicyFileShare#months}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.
        :param weeks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weeks BackupPolicyFileShare#weeks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionYearly.__init__)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument months", value=months, expected_type=type_hints["months"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
            check_type(argname="argument weeks", value=weeks, expected_type=type_hints["weeks"])
        self._values: typing.Dict[str, typing.Any] = {
            "count": count,
            "months": months,
            "weekdays": weekdays,
            "weeks": weeks,
        }

    @builtins.property
    def count(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#count BackupPolicyFileShare#count}.'''
        result = self._values.get("count")
        assert result is not None, "Required property 'count' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def months(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#months BackupPolicyFileShare#months}.'''
        result = self._values.get("months")
        assert result is not None, "Required property 'months' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def weekdays(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weekdays BackupPolicyFileShare#weekdays}.'''
        result = self._values.get("weekdays")
        assert result is not None, "Required property 'weekdays' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def weeks(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#weeks BackupPolicyFileShare#weeks}.'''
        result = self._values.get("weeks")
        assert result is not None, "Required property 'weeks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyFileShareRetentionYearly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyFileShareRetentionYearlyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareRetentionYearlyOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyFileShareRetentionYearlyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

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
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionYearlyOutputReference, "count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="months")
    def months(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "months"))

    @months.setter
    def months(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionYearlyOutputReference, "months").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "months", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionYearlyOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="weeks")
    def weeks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weeks"))

    @weeks.setter
    def weeks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionYearlyOutputReference, "weeks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BackupPolicyFileShareRetentionYearly]:
        return typing.cast(typing.Optional[BackupPolicyFileShareRetentionYearly], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BackupPolicyFileShareRetentionYearly],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareRetentionYearlyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class BackupPolicyFileShareTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#create BackupPolicyFileShare#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#delete BackupPolicyFileShare#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#read BackupPolicyFileShare#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#update BackupPolicyFileShare#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BackupPolicyFileShareTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#create BackupPolicyFileShare#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#delete BackupPolicyFileShare#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#read BackupPolicyFileShare#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/backup_policy_file_share#update BackupPolicyFileShare#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPolicyFileShareTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BackupPolicyFileShareTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.backupPolicyFileShare.BackupPolicyFileShareTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(BackupPolicyFileShareTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BackupPolicyFileShareTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BackupPolicyFileShareTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BackupPolicyFileShareTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BackupPolicyFileShareTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BackupPolicyFileShare",
    "BackupPolicyFileShareBackup",
    "BackupPolicyFileShareBackupOutputReference",
    "BackupPolicyFileShareConfig",
    "BackupPolicyFileShareRetentionDaily",
    "BackupPolicyFileShareRetentionDailyOutputReference",
    "BackupPolicyFileShareRetentionMonthly",
    "BackupPolicyFileShareRetentionMonthlyOutputReference",
    "BackupPolicyFileShareRetentionWeekly",
    "BackupPolicyFileShareRetentionWeeklyOutputReference",
    "BackupPolicyFileShareRetentionYearly",
    "BackupPolicyFileShareRetentionYearlyOutputReference",
    "BackupPolicyFileShareTimeouts",
    "BackupPolicyFileShareTimeoutsOutputReference",
]

publication.publish()
