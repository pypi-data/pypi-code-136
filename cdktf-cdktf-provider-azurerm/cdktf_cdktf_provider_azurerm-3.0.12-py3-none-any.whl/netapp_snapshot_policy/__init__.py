'''
# `azurerm_netapp_snapshot_policy`

Refer to the Terraform Registory for docs: [`azurerm_netapp_snapshot_policy`](https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy).
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


class NetappSnapshotPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy azurerm_netapp_snapshot_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_name: builtins.str,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        daily_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyDailySchedule", typing.Dict[str, typing.Any]]] = None,
        hourly_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyHourlySchedule", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        monthly_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyMonthlySchedule", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetappSnapshotPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        weekly_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyWeeklySchedule", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy azurerm_netapp_snapshot_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#account_name NetappSnapshotPolicy#account_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#enabled NetappSnapshotPolicy#enabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#location NetappSnapshotPolicy#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#name NetappSnapshotPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#resource_group_name NetappSnapshotPolicy#resource_group_name}.
        :param daily_schedule: daily_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#daily_schedule NetappSnapshotPolicy#daily_schedule}
        :param hourly_schedule: hourly_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hourly_schedule NetappSnapshotPolicy#hourly_schedule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#id NetappSnapshotPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monthly_schedule: monthly_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#monthly_schedule NetappSnapshotPolicy#monthly_schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#tags NetappSnapshotPolicy#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#timeouts NetappSnapshotPolicy#timeouts}
        :param weekly_schedule: weekly_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#weekly_schedule NetappSnapshotPolicy#weekly_schedule}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetappSnapshotPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetappSnapshotPolicyConfig(
            account_name=account_name,
            enabled=enabled,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            daily_schedule=daily_schedule,
            hourly_schedule=hourly_schedule,
            id=id,
            monthly_schedule=monthly_schedule,
            tags=tags,
            timeouts=timeouts,
            weekly_schedule=weekly_schedule,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDailySchedule")
    def put_daily_schedule(
        self,
        *,
        hour: jsii.Number,
        minute: jsii.Number,
        snapshots_to_keep: jsii.Number,
    ) -> None:
        '''
        :param hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        value = NetappSnapshotPolicyDailySchedule(
            hour=hour, minute=minute, snapshots_to_keep=snapshots_to_keep
        )

        return typing.cast(None, jsii.invoke(self, "putDailySchedule", [value]))

    @jsii.member(jsii_name="putHourlySchedule")
    def put_hourly_schedule(
        self,
        *,
        minute: jsii.Number,
        snapshots_to_keep: jsii.Number,
    ) -> None:
        '''
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        value = NetappSnapshotPolicyHourlySchedule(
            minute=minute, snapshots_to_keep=snapshots_to_keep
        )

        return typing.cast(None, jsii.invoke(self, "putHourlySchedule", [value]))

    @jsii.member(jsii_name="putMonthlySchedule")
    def put_monthly_schedule(
        self,
        *,
        days_of_month: typing.Sequence[jsii.Number],
        hour: jsii.Number,
        minute: jsii.Number,
        snapshots_to_keep: jsii.Number,
    ) -> None:
        '''
        :param days_of_month: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#days_of_month NetappSnapshotPolicy#days_of_month}.
        :param hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        value = NetappSnapshotPolicyMonthlySchedule(
            days_of_month=days_of_month,
            hour=hour,
            minute=minute,
            snapshots_to_keep=snapshots_to_keep,
        )

        return typing.cast(None, jsii.invoke(self, "putMonthlySchedule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#create NetappSnapshotPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#delete NetappSnapshotPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#read NetappSnapshotPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#update NetappSnapshotPolicy#update}.
        '''
        value = NetappSnapshotPolicyTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWeeklySchedule")
    def put_weekly_schedule(
        self,
        *,
        days_of_week: typing.Sequence[builtins.str],
        hour: jsii.Number,
        minute: jsii.Number,
        snapshots_to_keep: jsii.Number,
    ) -> None:
        '''
        :param days_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#days_of_week NetappSnapshotPolicy#days_of_week}.
        :param hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        value = NetappSnapshotPolicyWeeklySchedule(
            days_of_week=days_of_week,
            hour=hour,
            minute=minute,
            snapshots_to_keep=snapshots_to_keep,
        )

        return typing.cast(None, jsii.invoke(self, "putWeeklySchedule", [value]))

    @jsii.member(jsii_name="resetDailySchedule")
    def reset_daily_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailySchedule", []))

    @jsii.member(jsii_name="resetHourlySchedule")
    def reset_hourly_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHourlySchedule", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMonthlySchedule")
    def reset_monthly_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthlySchedule", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWeeklySchedule")
    def reset_weekly_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklySchedule", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dailySchedule")
    def daily_schedule(self) -> "NetappSnapshotPolicyDailyScheduleOutputReference":
        return typing.cast("NetappSnapshotPolicyDailyScheduleOutputReference", jsii.get(self, "dailySchedule"))

    @builtins.property
    @jsii.member(jsii_name="hourlySchedule")
    def hourly_schedule(self) -> "NetappSnapshotPolicyHourlyScheduleOutputReference":
        return typing.cast("NetappSnapshotPolicyHourlyScheduleOutputReference", jsii.get(self, "hourlySchedule"))

    @builtins.property
    @jsii.member(jsii_name="monthlySchedule")
    def monthly_schedule(self) -> "NetappSnapshotPolicyMonthlyScheduleOutputReference":
        return typing.cast("NetappSnapshotPolicyMonthlyScheduleOutputReference", jsii.get(self, "monthlySchedule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetappSnapshotPolicyTimeoutsOutputReference":
        return typing.cast("NetappSnapshotPolicyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="weeklySchedule")
    def weekly_schedule(self) -> "NetappSnapshotPolicyWeeklyScheduleOutputReference":
        return typing.cast("NetappSnapshotPolicyWeeklyScheduleOutputReference", jsii.get(self, "weeklySchedule"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyScheduleInput")
    def daily_schedule_input(
        self,
    ) -> typing.Optional["NetappSnapshotPolicyDailySchedule"]:
        return typing.cast(typing.Optional["NetappSnapshotPolicyDailySchedule"], jsii.get(self, "dailyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="hourlyScheduleInput")
    def hourly_schedule_input(
        self,
    ) -> typing.Optional["NetappSnapshotPolicyHourlySchedule"]:
        return typing.cast(typing.Optional["NetappSnapshotPolicyHourlySchedule"], jsii.get(self, "hourlyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlyScheduleInput")
    def monthly_schedule_input(
        self,
    ) -> typing.Optional["NetappSnapshotPolicyMonthlySchedule"]:
        return typing.cast(typing.Optional["NetappSnapshotPolicyMonthlySchedule"], jsii.get(self, "monthlyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetappSnapshotPolicyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetappSnapshotPolicyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyScheduleInput")
    def weekly_schedule_input(
        self,
    ) -> typing.Optional["NetappSnapshotPolicyWeeklySchedule"]:
        return typing.cast(typing.Optional["NetappSnapshotPolicyWeeklySchedule"], jsii.get(self, "weeklyScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicy, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicy, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicy, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicy, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicy, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_name": "accountName",
        "enabled": "enabled",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "daily_schedule": "dailySchedule",
        "hourly_schedule": "hourlySchedule",
        "id": "id",
        "monthly_schedule": "monthlySchedule",
        "tags": "tags",
        "timeouts": "timeouts",
        "weekly_schedule": "weeklySchedule",
    },
)
class NetappSnapshotPolicyConfig(cdktf.TerraformMetaArguments):
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
        account_name: builtins.str,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        daily_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyDailySchedule", typing.Dict[str, typing.Any]]] = None,
        hourly_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyHourlySchedule", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        monthly_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyMonthlySchedule", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["NetappSnapshotPolicyTimeouts", typing.Dict[str, typing.Any]]] = None,
        weekly_schedule: typing.Optional[typing.Union["NetappSnapshotPolicyWeeklySchedule", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#account_name NetappSnapshotPolicy#account_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#enabled NetappSnapshotPolicy#enabled}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#location NetappSnapshotPolicy#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#name NetappSnapshotPolicy#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#resource_group_name NetappSnapshotPolicy#resource_group_name}.
        :param daily_schedule: daily_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#daily_schedule NetappSnapshotPolicy#daily_schedule}
        :param hourly_schedule: hourly_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hourly_schedule NetappSnapshotPolicy#hourly_schedule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#id NetappSnapshotPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param monthly_schedule: monthly_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#monthly_schedule NetappSnapshotPolicy#monthly_schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#tags NetappSnapshotPolicy#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#timeouts NetappSnapshotPolicy#timeouts}
        :param weekly_schedule: weekly_schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#weekly_schedule NetappSnapshotPolicy#weekly_schedule}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(daily_schedule, dict):
            daily_schedule = NetappSnapshotPolicyDailySchedule(**daily_schedule)
        if isinstance(hourly_schedule, dict):
            hourly_schedule = NetappSnapshotPolicyHourlySchedule(**hourly_schedule)
        if isinstance(monthly_schedule, dict):
            monthly_schedule = NetappSnapshotPolicyMonthlySchedule(**monthly_schedule)
        if isinstance(timeouts, dict):
            timeouts = NetappSnapshotPolicyTimeouts(**timeouts)
        if isinstance(weekly_schedule, dict):
            weekly_schedule = NetappSnapshotPolicyWeeklySchedule(**weekly_schedule)
        if __debug__:
            type_hints = typing.get_type_hints(NetappSnapshotPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument daily_schedule", value=daily_schedule, expected_type=type_hints["daily_schedule"])
            check_type(argname="argument hourly_schedule", value=hourly_schedule, expected_type=type_hints["hourly_schedule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument monthly_schedule", value=monthly_schedule, expected_type=type_hints["monthly_schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument weekly_schedule", value=weekly_schedule, expected_type=type_hints["weekly_schedule"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "enabled": enabled,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
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
        if daily_schedule is not None:
            self._values["daily_schedule"] = daily_schedule
        if hourly_schedule is not None:
            self._values["hourly_schedule"] = hourly_schedule
        if id is not None:
            self._values["id"] = id
        if monthly_schedule is not None:
            self._values["monthly_schedule"] = monthly_schedule
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if weekly_schedule is not None:
            self._values["weekly_schedule"] = weekly_schedule

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
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#account_name NetappSnapshotPolicy#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#enabled NetappSnapshotPolicy#enabled}.'''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#location NetappSnapshotPolicy#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#name NetappSnapshotPolicy#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#resource_group_name NetappSnapshotPolicy#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def daily_schedule(self) -> typing.Optional["NetappSnapshotPolicyDailySchedule"]:
        '''daily_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#daily_schedule NetappSnapshotPolicy#daily_schedule}
        '''
        result = self._values.get("daily_schedule")
        return typing.cast(typing.Optional["NetappSnapshotPolicyDailySchedule"], result)

    @builtins.property
    def hourly_schedule(self) -> typing.Optional["NetappSnapshotPolicyHourlySchedule"]:
        '''hourly_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hourly_schedule NetappSnapshotPolicy#hourly_schedule}
        '''
        result = self._values.get("hourly_schedule")
        return typing.cast(typing.Optional["NetappSnapshotPolicyHourlySchedule"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#id NetappSnapshotPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def monthly_schedule(
        self,
    ) -> typing.Optional["NetappSnapshotPolicyMonthlySchedule"]:
        '''monthly_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#monthly_schedule NetappSnapshotPolicy#monthly_schedule}
        '''
        result = self._values.get("monthly_schedule")
        return typing.cast(typing.Optional["NetappSnapshotPolicyMonthlySchedule"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#tags NetappSnapshotPolicy#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetappSnapshotPolicyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#timeouts NetappSnapshotPolicy#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetappSnapshotPolicyTimeouts"], result)

    @builtins.property
    def weekly_schedule(self) -> typing.Optional["NetappSnapshotPolicyWeeklySchedule"]:
        '''weekly_schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#weekly_schedule NetappSnapshotPolicy#weekly_schedule}
        '''
        result = self._values.get("weekly_schedule")
        return typing.cast(typing.Optional["NetappSnapshotPolicyWeeklySchedule"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetappSnapshotPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyDailySchedule",
    jsii_struct_bases=[],
    name_mapping={
        "hour": "hour",
        "minute": "minute",
        "snapshots_to_keep": "snapshotsToKeep",
    },
)
class NetappSnapshotPolicyDailySchedule:
    def __init__(
        self,
        *,
        hour: jsii.Number,
        minute: jsii.Number,
        snapshots_to_keep: jsii.Number,
    ) -> None:
        '''
        :param hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetappSnapshotPolicyDailySchedule.__init__)
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument snapshots_to_keep", value=snapshots_to_keep, expected_type=type_hints["snapshots_to_keep"])
        self._values: typing.Dict[str, typing.Any] = {
            "hour": hour,
            "minute": minute,
            "snapshots_to_keep": snapshots_to_keep,
        }

    @builtins.property
    def hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.'''
        result = self._values.get("hour")
        assert result is not None, "Required property 'hour' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minute(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.'''
        result = self._values.get("minute")
        assert result is not None, "Required property 'minute' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def snapshots_to_keep(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.'''
        result = self._values.get("snapshots_to_keep")
        assert result is not None, "Required property 'snapshots_to_keep' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetappSnapshotPolicyDailySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetappSnapshotPolicyDailyScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyDailyScheduleOutputReference",
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
            type_hints = typing.get_type_hints(NetappSnapshotPolicyDailyScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="hourInput")
    def hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hourInput"))

    @builtins.property
    @jsii.member(jsii_name="minuteInput")
    def minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minuteInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeepInput")
    def snapshots_to_keep_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotsToKeepInput"))

    @builtins.property
    @jsii.member(jsii_name="hour")
    def hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hour"))

    @hour.setter
    def hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyDailyScheduleOutputReference, "hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hour", value)

    @builtins.property
    @jsii.member(jsii_name="minute")
    def minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minute"))

    @minute.setter
    def minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyDailyScheduleOutputReference, "minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minute", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeep")
    def snapshots_to_keep(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "snapshotsToKeep"))

    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyDailyScheduleOutputReference, "snapshots_to_keep").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotsToKeep", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetappSnapshotPolicyDailySchedule]:
        return typing.cast(typing.Optional[NetappSnapshotPolicyDailySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetappSnapshotPolicyDailySchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyDailyScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyHourlySchedule",
    jsii_struct_bases=[],
    name_mapping={"minute": "minute", "snapshots_to_keep": "snapshotsToKeep"},
)
class NetappSnapshotPolicyHourlySchedule:
    def __init__(self, *, minute: jsii.Number, snapshots_to_keep: jsii.Number) -> None:
        '''
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetappSnapshotPolicyHourlySchedule.__init__)
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument snapshots_to_keep", value=snapshots_to_keep, expected_type=type_hints["snapshots_to_keep"])
        self._values: typing.Dict[str, typing.Any] = {
            "minute": minute,
            "snapshots_to_keep": snapshots_to_keep,
        }

    @builtins.property
    def minute(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.'''
        result = self._values.get("minute")
        assert result is not None, "Required property 'minute' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def snapshots_to_keep(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.'''
        result = self._values.get("snapshots_to_keep")
        assert result is not None, "Required property 'snapshots_to_keep' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetappSnapshotPolicyHourlySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetappSnapshotPolicyHourlyScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyHourlyScheduleOutputReference",
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
            type_hints = typing.get_type_hints(NetappSnapshotPolicyHourlyScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="minuteInput")
    def minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minuteInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeepInput")
    def snapshots_to_keep_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotsToKeepInput"))

    @builtins.property
    @jsii.member(jsii_name="minute")
    def minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minute"))

    @minute.setter
    def minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyHourlyScheduleOutputReference, "minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minute", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeep")
    def snapshots_to_keep(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "snapshotsToKeep"))

    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyHourlyScheduleOutputReference, "snapshots_to_keep").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotsToKeep", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetappSnapshotPolicyHourlySchedule]:
        return typing.cast(typing.Optional[NetappSnapshotPolicyHourlySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetappSnapshotPolicyHourlySchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyHourlyScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyMonthlySchedule",
    jsii_struct_bases=[],
    name_mapping={
        "days_of_month": "daysOfMonth",
        "hour": "hour",
        "minute": "minute",
        "snapshots_to_keep": "snapshotsToKeep",
    },
)
class NetappSnapshotPolicyMonthlySchedule:
    def __init__(
        self,
        *,
        days_of_month: typing.Sequence[jsii.Number],
        hour: jsii.Number,
        minute: jsii.Number,
        snapshots_to_keep: jsii.Number,
    ) -> None:
        '''
        :param days_of_month: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#days_of_month NetappSnapshotPolicy#days_of_month}.
        :param hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetappSnapshotPolicyMonthlySchedule.__init__)
            check_type(argname="argument days_of_month", value=days_of_month, expected_type=type_hints["days_of_month"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument snapshots_to_keep", value=snapshots_to_keep, expected_type=type_hints["snapshots_to_keep"])
        self._values: typing.Dict[str, typing.Any] = {
            "days_of_month": days_of_month,
            "hour": hour,
            "minute": minute,
            "snapshots_to_keep": snapshots_to_keep,
        }

    @builtins.property
    def days_of_month(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#days_of_month NetappSnapshotPolicy#days_of_month}.'''
        result = self._values.get("days_of_month")
        assert result is not None, "Required property 'days_of_month' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.'''
        result = self._values.get("hour")
        assert result is not None, "Required property 'hour' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minute(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.'''
        result = self._values.get("minute")
        assert result is not None, "Required property 'minute' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def snapshots_to_keep(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.'''
        result = self._values.get("snapshots_to_keep")
        assert result is not None, "Required property 'snapshots_to_keep' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetappSnapshotPolicyMonthlySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetappSnapshotPolicyMonthlyScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyMonthlyScheduleOutputReference",
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
            type_hints = typing.get_type_hints(NetappSnapshotPolicyMonthlyScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="daysOfMonthInput")
    def days_of_month_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "daysOfMonthInput"))

    @builtins.property
    @jsii.member(jsii_name="hourInput")
    def hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hourInput"))

    @builtins.property
    @jsii.member(jsii_name="minuteInput")
    def minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minuteInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeepInput")
    def snapshots_to_keep_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotsToKeepInput"))

    @builtins.property
    @jsii.member(jsii_name="daysOfMonth")
    def days_of_month(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "daysOfMonth"))

    @days_of_month.setter
    def days_of_month(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyMonthlyScheduleOutputReference, "days_of_month").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysOfMonth", value)

    @builtins.property
    @jsii.member(jsii_name="hour")
    def hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hour"))

    @hour.setter
    def hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyMonthlyScheduleOutputReference, "hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hour", value)

    @builtins.property
    @jsii.member(jsii_name="minute")
    def minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minute"))

    @minute.setter
    def minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyMonthlyScheduleOutputReference, "minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minute", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeep")
    def snapshots_to_keep(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "snapshotsToKeep"))

    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyMonthlyScheduleOutputReference, "snapshots_to_keep").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotsToKeep", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetappSnapshotPolicyMonthlySchedule]:
        return typing.cast(typing.Optional[NetappSnapshotPolicyMonthlySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetappSnapshotPolicyMonthlySchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyMonthlyScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class NetappSnapshotPolicyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#create NetappSnapshotPolicy#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#delete NetappSnapshotPolicy#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#read NetappSnapshotPolicy#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#update NetappSnapshotPolicy#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetappSnapshotPolicyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#create NetappSnapshotPolicy#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#delete NetappSnapshotPolicy#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#read NetappSnapshotPolicy#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#update NetappSnapshotPolicy#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetappSnapshotPolicyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetappSnapshotPolicyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(NetappSnapshotPolicyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetappSnapshotPolicyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetappSnapshotPolicyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetappSnapshotPolicyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyWeeklySchedule",
    jsii_struct_bases=[],
    name_mapping={
        "days_of_week": "daysOfWeek",
        "hour": "hour",
        "minute": "minute",
        "snapshots_to_keep": "snapshotsToKeep",
    },
)
class NetappSnapshotPolicyWeeklySchedule:
    def __init__(
        self,
        *,
        days_of_week: typing.Sequence[builtins.str],
        hour: jsii.Number,
        minute: jsii.Number,
        snapshots_to_keep: jsii.Number,
    ) -> None:
        '''
        :param days_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#days_of_week NetappSnapshotPolicy#days_of_week}.
        :param hour: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.
        :param minute: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.
        :param snapshots_to_keep: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetappSnapshotPolicyWeeklySchedule.__init__)
            check_type(argname="argument days_of_week", value=days_of_week, expected_type=type_hints["days_of_week"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument snapshots_to_keep", value=snapshots_to_keep, expected_type=type_hints["snapshots_to_keep"])
        self._values: typing.Dict[str, typing.Any] = {
            "days_of_week": days_of_week,
            "hour": hour,
            "minute": minute,
            "snapshots_to_keep": snapshots_to_keep,
        }

    @builtins.property
    def days_of_week(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#days_of_week NetappSnapshotPolicy#days_of_week}.'''
        result = self._values.get("days_of_week")
        assert result is not None, "Required property 'days_of_week' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def hour(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#hour NetappSnapshotPolicy#hour}.'''
        result = self._values.get("hour")
        assert result is not None, "Required property 'hour' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def minute(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#minute NetappSnapshotPolicy#minute}.'''
        result = self._values.get("minute")
        assert result is not None, "Required property 'minute' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def snapshots_to_keep(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/netapp_snapshot_policy#snapshots_to_keep NetappSnapshotPolicy#snapshots_to_keep}.'''
        result = self._values.get("snapshots_to_keep")
        assert result is not None, "Required property 'snapshots_to_keep' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetappSnapshotPolicyWeeklySchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetappSnapshotPolicyWeeklyScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.netappSnapshotPolicy.NetappSnapshotPolicyWeeklyScheduleOutputReference",
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
            type_hints = typing.get_type_hints(NetappSnapshotPolicyWeeklyScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="daysOfWeekInput")
    def days_of_week_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "daysOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="hourInput")
    def hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "hourInput"))

    @builtins.property
    @jsii.member(jsii_name="minuteInput")
    def minute_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minuteInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeepInput")
    def snapshots_to_keep_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snapshotsToKeepInput"))

    @builtins.property
    @jsii.member(jsii_name="daysOfWeek")
    def days_of_week(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "daysOfWeek"))

    @days_of_week.setter
    def days_of_week(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyWeeklyScheduleOutputReference, "days_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="hour")
    def hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hour"))

    @hour.setter
    def hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyWeeklyScheduleOutputReference, "hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hour", value)

    @builtins.property
    @jsii.member(jsii_name="minute")
    def minute(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minute"))

    @minute.setter
    def minute(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyWeeklyScheduleOutputReference, "minute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minute", value)

    @builtins.property
    @jsii.member(jsii_name="snapshotsToKeep")
    def snapshots_to_keep(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "snapshotsToKeep"))

    @snapshots_to_keep.setter
    def snapshots_to_keep(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyWeeklyScheduleOutputReference, "snapshots_to_keep").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapshotsToKeep", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetappSnapshotPolicyWeeklySchedule]:
        return typing.cast(typing.Optional[NetappSnapshotPolicyWeeklySchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetappSnapshotPolicyWeeklySchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetappSnapshotPolicyWeeklyScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetappSnapshotPolicy",
    "NetappSnapshotPolicyConfig",
    "NetappSnapshotPolicyDailySchedule",
    "NetappSnapshotPolicyDailyScheduleOutputReference",
    "NetappSnapshotPolicyHourlySchedule",
    "NetappSnapshotPolicyHourlyScheduleOutputReference",
    "NetappSnapshotPolicyMonthlySchedule",
    "NetappSnapshotPolicyMonthlyScheduleOutputReference",
    "NetappSnapshotPolicyTimeouts",
    "NetappSnapshotPolicyTimeoutsOutputReference",
    "NetappSnapshotPolicyWeeklySchedule",
    "NetappSnapshotPolicyWeeklyScheduleOutputReference",
]

publication.publish()
