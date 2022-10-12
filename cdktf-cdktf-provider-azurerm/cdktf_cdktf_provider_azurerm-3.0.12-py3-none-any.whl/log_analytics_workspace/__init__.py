'''
# `azurerm_log_analytics_workspace`

Refer to the Terraform Registory for docs: [`azurerm_log_analytics_workspace`](https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace).
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


class LogAnalyticsWorkspace(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logAnalyticsWorkspace.LogAnalyticsWorkspace",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace azurerm_log_analytics_workspace}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        cmk_for_query_forced: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        daily_quota_gb: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        internet_ingestion_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        internet_query_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reservation_capacity_in_gb_per_day: typing.Optional[jsii.Number] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        sku: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LogAnalyticsWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace azurerm_log_analytics_workspace} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#location LogAnalyticsWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#name LogAnalyticsWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#resource_group_name LogAnalyticsWorkspace#resource_group_name}.
        :param cmk_for_query_forced: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#cmk_for_query_forced LogAnalyticsWorkspace#cmk_for_query_forced}.
        :param daily_quota_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#daily_quota_gb LogAnalyticsWorkspace#daily_quota_gb}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#id LogAnalyticsWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_ingestion_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#internet_ingestion_enabled LogAnalyticsWorkspace#internet_ingestion_enabled}.
        :param internet_query_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#internet_query_enabled LogAnalyticsWorkspace#internet_query_enabled}.
        :param reservation_capacity_in_gb_per_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#reservation_capacity_in_gb_per_day LogAnalyticsWorkspace#reservation_capacity_in_gb_per_day}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#retention_in_days LogAnalyticsWorkspace#retention_in_days}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#sku LogAnalyticsWorkspace#sku}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#tags LogAnalyticsWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#timeouts LogAnalyticsWorkspace#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogAnalyticsWorkspace.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LogAnalyticsWorkspaceConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            cmk_for_query_forced=cmk_for_query_forced,
            daily_quota_gb=daily_quota_gb,
            id=id,
            internet_ingestion_enabled=internet_ingestion_enabled,
            internet_query_enabled=internet_query_enabled,
            reservation_capacity_in_gb_per_day=reservation_capacity_in_gb_per_day,
            retention_in_days=retention_in_days,
            sku=sku,
            tags=tags,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#create LogAnalyticsWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#delete LogAnalyticsWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#read LogAnalyticsWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#update LogAnalyticsWorkspace#update}.
        '''
        value = LogAnalyticsWorkspaceTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCmkForQueryForced")
    def reset_cmk_for_query_forced(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCmkForQueryForced", []))

    @jsii.member(jsii_name="resetDailyQuotaGb")
    def reset_daily_quota_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailyQuotaGb", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInternetIngestionEnabled")
    def reset_internet_ingestion_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternetIngestionEnabled", []))

    @jsii.member(jsii_name="resetInternetQueryEnabled")
    def reset_internet_query_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternetQueryEnabled", []))

    @jsii.member(jsii_name="resetReservationCapacityInGbPerDay")
    def reset_reservation_capacity_in_gb_per_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReservationCapacityInGbPerDay", []))

    @jsii.member(jsii_name="resetRetentionInDays")
    def reset_retention_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionInDays", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="primarySharedKey")
    def primary_shared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primarySharedKey"))

    @builtins.property
    @jsii.member(jsii_name="secondarySharedKey")
    def secondary_shared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondarySharedKey"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LogAnalyticsWorkspaceTimeoutsOutputReference":
        return typing.cast("LogAnalyticsWorkspaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceId"))

    @builtins.property
    @jsii.member(jsii_name="cmkForQueryForcedInput")
    def cmk_for_query_forced_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cmkForQueryForcedInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyQuotaGbInput")
    def daily_quota_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dailyQuotaGbInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="internetIngestionEnabledInput")
    def internet_ingestion_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internetIngestionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="internetQueryEnabledInput")
    def internet_query_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internetQueryEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="reservationCapacityInGbPerDayInput")
    def reservation_capacity_in_gb_per_day_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "reservationCapacityInGbPerDayInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LogAnalyticsWorkspaceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LogAnalyticsWorkspaceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="cmkForQueryForced")
    def cmk_for_query_forced(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cmkForQueryForced"))

    @cmk_for_query_forced.setter
    def cmk_for_query_forced(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "cmk_for_query_forced").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cmkForQueryForced", value)

    @builtins.property
    @jsii.member(jsii_name="dailyQuotaGb")
    def daily_quota_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dailyQuotaGb"))

    @daily_quota_gb.setter
    def daily_quota_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "daily_quota_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailyQuotaGb", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internetIngestionEnabled")
    def internet_ingestion_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internetIngestionEnabled"))

    @internet_ingestion_enabled.setter
    def internet_ingestion_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "internet_ingestion_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetIngestionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internetQueryEnabled")
    def internet_query_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internetQueryEnabled"))

    @internet_query_enabled.setter
    def internet_query_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "internet_query_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetQueryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reservationCapacityInGbPerDay")
    def reservation_capacity_in_gb_per_day(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "reservationCapacityInGbPerDay"))

    @reservation_capacity_in_gb_per_day.setter
    def reservation_capacity_in_gb_per_day(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "reservation_capacity_in_gb_per_day").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reservationCapacityInGbPerDay", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspace, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logAnalyticsWorkspace.LogAnalyticsWorkspaceConfig",
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
        "resource_group_name": "resourceGroupName",
        "cmk_for_query_forced": "cmkForQueryForced",
        "daily_quota_gb": "dailyQuotaGb",
        "id": "id",
        "internet_ingestion_enabled": "internetIngestionEnabled",
        "internet_query_enabled": "internetQueryEnabled",
        "reservation_capacity_in_gb_per_day": "reservationCapacityInGbPerDay",
        "retention_in_days": "retentionInDays",
        "sku": "sku",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class LogAnalyticsWorkspaceConfig(cdktf.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        cmk_for_query_forced: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        daily_quota_gb: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        internet_ingestion_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        internet_query_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reservation_capacity_in_gb_per_day: typing.Optional[jsii.Number] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        sku: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["LogAnalyticsWorkspaceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#location LogAnalyticsWorkspace#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#name LogAnalyticsWorkspace#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#resource_group_name LogAnalyticsWorkspace#resource_group_name}.
        :param cmk_for_query_forced: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#cmk_for_query_forced LogAnalyticsWorkspace#cmk_for_query_forced}.
        :param daily_quota_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#daily_quota_gb LogAnalyticsWorkspace#daily_quota_gb}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#id LogAnalyticsWorkspace#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_ingestion_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#internet_ingestion_enabled LogAnalyticsWorkspace#internet_ingestion_enabled}.
        :param internet_query_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#internet_query_enabled LogAnalyticsWorkspace#internet_query_enabled}.
        :param reservation_capacity_in_gb_per_day: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#reservation_capacity_in_gb_per_day LogAnalyticsWorkspace#reservation_capacity_in_gb_per_day}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#retention_in_days LogAnalyticsWorkspace#retention_in_days}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#sku LogAnalyticsWorkspace#sku}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#tags LogAnalyticsWorkspace#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#timeouts LogAnalyticsWorkspace#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = LogAnalyticsWorkspaceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(LogAnalyticsWorkspaceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument cmk_for_query_forced", value=cmk_for_query_forced, expected_type=type_hints["cmk_for_query_forced"])
            check_type(argname="argument daily_quota_gb", value=daily_quota_gb, expected_type=type_hints["daily_quota_gb"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument internet_ingestion_enabled", value=internet_ingestion_enabled, expected_type=type_hints["internet_ingestion_enabled"])
            check_type(argname="argument internet_query_enabled", value=internet_query_enabled, expected_type=type_hints["internet_query_enabled"])
            check_type(argname="argument reservation_capacity_in_gb_per_day", value=reservation_capacity_in_gb_per_day, expected_type=type_hints["reservation_capacity_in_gb_per_day"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if cmk_for_query_forced is not None:
            self._values["cmk_for_query_forced"] = cmk_for_query_forced
        if daily_quota_gb is not None:
            self._values["daily_quota_gb"] = daily_quota_gb
        if id is not None:
            self._values["id"] = id
        if internet_ingestion_enabled is not None:
            self._values["internet_ingestion_enabled"] = internet_ingestion_enabled
        if internet_query_enabled is not None:
            self._values["internet_query_enabled"] = internet_query_enabled
        if reservation_capacity_in_gb_per_day is not None:
            self._values["reservation_capacity_in_gb_per_day"] = reservation_capacity_in_gb_per_day
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days
        if sku is not None:
            self._values["sku"] = sku
        if tags is not None:
            self._values["tags"] = tags
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#location LogAnalyticsWorkspace#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#name LogAnalyticsWorkspace#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#resource_group_name LogAnalyticsWorkspace#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cmk_for_query_forced(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#cmk_for_query_forced LogAnalyticsWorkspace#cmk_for_query_forced}.'''
        result = self._values.get("cmk_for_query_forced")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def daily_quota_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#daily_quota_gb LogAnalyticsWorkspace#daily_quota_gb}.'''
        result = self._values.get("daily_quota_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#id LogAnalyticsWorkspace#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internet_ingestion_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#internet_ingestion_enabled LogAnalyticsWorkspace#internet_ingestion_enabled}.'''
        result = self._values.get("internet_ingestion_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def internet_query_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#internet_query_enabled LogAnalyticsWorkspace#internet_query_enabled}.'''
        result = self._values.get("internet_query_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def reservation_capacity_in_gb_per_day(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#reservation_capacity_in_gb_per_day LogAnalyticsWorkspace#reservation_capacity_in_gb_per_day}.'''
        result = self._values.get("reservation_capacity_in_gb_per_day")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#retention_in_days LogAnalyticsWorkspace#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#sku LogAnalyticsWorkspace#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#tags LogAnalyticsWorkspace#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LogAnalyticsWorkspaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#timeouts LogAnalyticsWorkspace#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LogAnalyticsWorkspaceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogAnalyticsWorkspaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.logAnalyticsWorkspace.LogAnalyticsWorkspaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class LogAnalyticsWorkspaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#create LogAnalyticsWorkspace#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#delete LogAnalyticsWorkspace#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#read LogAnalyticsWorkspace#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#update LogAnalyticsWorkspace#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LogAnalyticsWorkspaceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#create LogAnalyticsWorkspace#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#delete LogAnalyticsWorkspace#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#read LogAnalyticsWorkspace#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/log_analytics_workspace#update LogAnalyticsWorkspace#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogAnalyticsWorkspaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LogAnalyticsWorkspaceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.logAnalyticsWorkspace.LogAnalyticsWorkspaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(LogAnalyticsWorkspaceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspaceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspaceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspaceTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspaceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LogAnalyticsWorkspaceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LogAnalyticsWorkspaceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LogAnalyticsWorkspaceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LogAnalyticsWorkspaceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LogAnalyticsWorkspace",
    "LogAnalyticsWorkspaceConfig",
    "LogAnalyticsWorkspaceTimeouts",
    "LogAnalyticsWorkspaceTimeoutsOutputReference",
]

publication.publish()
