'''
# `azurerm_application_insights`

Refer to the Terraform Registory for docs: [`azurerm_application_insights`](https://www.terraform.io/docs/providers/azurerm/r/application_insights).
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


class ApplicationInsights(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationInsights.ApplicationInsights",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights azurerm_application_insights}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        application_type: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        daily_data_cap_in_gb: typing.Optional[jsii.Number] = None,
        daily_data_cap_notifications_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_ip_masking: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_customer_storage_for_profiler: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        internet_ingestion_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        internet_query_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        local_authentication_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ApplicationInsightsTimeouts", typing.Dict[str, typing.Any]]] = None,
        workspace_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights azurerm_application_insights} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param application_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#application_type ApplicationInsights#application_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#location ApplicationInsights#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#name ApplicationInsights#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#resource_group_name ApplicationInsights#resource_group_name}.
        :param daily_data_cap_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#daily_data_cap_in_gb ApplicationInsights#daily_data_cap_in_gb}.
        :param daily_data_cap_notifications_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#daily_data_cap_notifications_disabled ApplicationInsights#daily_data_cap_notifications_disabled}.
        :param disable_ip_masking: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#disable_ip_masking ApplicationInsights#disable_ip_masking}.
        :param force_customer_storage_for_profiler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#force_customer_storage_for_profiler ApplicationInsights#force_customer_storage_for_profiler}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#id ApplicationInsights#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_ingestion_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#internet_ingestion_enabled ApplicationInsights#internet_ingestion_enabled}.
        :param internet_query_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#internet_query_enabled ApplicationInsights#internet_query_enabled}.
        :param local_authentication_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#local_authentication_disabled ApplicationInsights#local_authentication_disabled}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#retention_in_days ApplicationInsights#retention_in_days}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#sampling_percentage ApplicationInsights#sampling_percentage}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#tags ApplicationInsights#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#timeouts ApplicationInsights#timeouts}
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#workspace_id ApplicationInsights#workspace_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationInsights.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApplicationInsightsConfig(
            application_type=application_type,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            daily_data_cap_in_gb=daily_data_cap_in_gb,
            daily_data_cap_notifications_disabled=daily_data_cap_notifications_disabled,
            disable_ip_masking=disable_ip_masking,
            force_customer_storage_for_profiler=force_customer_storage_for_profiler,
            id=id,
            internet_ingestion_enabled=internet_ingestion_enabled,
            internet_query_enabled=internet_query_enabled,
            local_authentication_disabled=local_authentication_disabled,
            retention_in_days=retention_in_days,
            sampling_percentage=sampling_percentage,
            tags=tags,
            timeouts=timeouts,
            workspace_id=workspace_id,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#create ApplicationInsights#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#delete ApplicationInsights#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#read ApplicationInsights#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#update ApplicationInsights#update}.
        '''
        value = ApplicationInsightsTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDailyDataCapInGb")
    def reset_daily_data_cap_in_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailyDataCapInGb", []))

    @jsii.member(jsii_name="resetDailyDataCapNotificationsDisabled")
    def reset_daily_data_cap_notifications_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDailyDataCapNotificationsDisabled", []))

    @jsii.member(jsii_name="resetDisableIpMasking")
    def reset_disable_ip_masking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableIpMasking", []))

    @jsii.member(jsii_name="resetForceCustomerStorageForProfiler")
    def reset_force_customer_storage_for_profiler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceCustomerStorageForProfiler", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInternetIngestionEnabled")
    def reset_internet_ingestion_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternetIngestionEnabled", []))

    @jsii.member(jsii_name="resetInternetQueryEnabled")
    def reset_internet_query_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternetQueryEnabled", []))

    @jsii.member(jsii_name="resetLocalAuthenticationDisabled")
    def reset_local_authentication_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAuthenticationDisabled", []))

    @jsii.member(jsii_name="resetRetentionInDays")
    def reset_retention_in_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionInDays", []))

    @jsii.member(jsii_name="resetSamplingPercentage")
    def reset_sampling_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamplingPercentage", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkspaceId")
    def reset_workspace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @builtins.property
    @jsii.member(jsii_name="connectionString")
    def connection_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionString"))

    @builtins.property
    @jsii.member(jsii_name="instrumentationKey")
    def instrumentation_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instrumentationKey"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApplicationInsightsTimeoutsOutputReference":
        return typing.cast("ApplicationInsightsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="applicationTypeInput")
    def application_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyDataCapInGbInput")
    def daily_data_cap_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dailyDataCapInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="dailyDataCapNotificationsDisabledInput")
    def daily_data_cap_notifications_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dailyDataCapNotificationsDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="disableIpMaskingInput")
    def disable_ip_masking_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableIpMaskingInput"))

    @builtins.property
    @jsii.member(jsii_name="forceCustomerStorageForProfilerInput")
    def force_customer_storage_for_profiler_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceCustomerStorageForProfilerInput"))

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
    @jsii.member(jsii_name="localAuthenticationDisabledInput")
    def local_authentication_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAuthenticationDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInDaysInput")
    def retention_in_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingPercentageInput")
    def sampling_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApplicationInsightsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApplicationInsightsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceIdInput")
    def workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationType")
    def application_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationType"))

    @application_type.setter
    def application_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "application_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationType", value)

    @builtins.property
    @jsii.member(jsii_name="dailyDataCapInGb")
    def daily_data_cap_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dailyDataCapInGb"))

    @daily_data_cap_in_gb.setter
    def daily_data_cap_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "daily_data_cap_in_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailyDataCapInGb", value)

    @builtins.property
    @jsii.member(jsii_name="dailyDataCapNotificationsDisabled")
    def daily_data_cap_notifications_disabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dailyDataCapNotificationsDisabled"))

    @daily_data_cap_notifications_disabled.setter
    def daily_data_cap_notifications_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "daily_data_cap_notifications_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dailyDataCapNotificationsDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="disableIpMasking")
    def disable_ip_masking(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableIpMasking"))

    @disable_ip_masking.setter
    def disable_ip_masking(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "disable_ip_masking").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableIpMasking", value)

    @builtins.property
    @jsii.member(jsii_name="forceCustomerStorageForProfiler")
    def force_customer_storage_for_profiler(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceCustomerStorageForProfiler"))

    @force_customer_storage_for_profiler.setter
    def force_customer_storage_for_profiler(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "force_customer_storage_for_profiler").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceCustomerStorageForProfiler", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "id").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "internet_ingestion_enabled").fset)
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
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "internet_query_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetQueryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="localAuthenticationDisabled")
    def local_authentication_disabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localAuthenticationDisabled"))

    @local_authentication_disabled.setter
    def local_authentication_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "local_authentication_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAuthenticationDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionInDays"))

    @retention_in_days.setter
    def retention_in_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "retention_in_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionInDays", value)

    @builtins.property
    @jsii.member(jsii_name="samplingPercentage")
    def sampling_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingPercentage"))

    @sampling_percentage.setter
    def sampling_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "sampling_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceId")
    def workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workspaceId"))

    @workspace_id.setter
    def workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsights, "workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationInsights.ApplicationInsightsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "application_type": "applicationType",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "daily_data_cap_in_gb": "dailyDataCapInGb",
        "daily_data_cap_notifications_disabled": "dailyDataCapNotificationsDisabled",
        "disable_ip_masking": "disableIpMasking",
        "force_customer_storage_for_profiler": "forceCustomerStorageForProfiler",
        "id": "id",
        "internet_ingestion_enabled": "internetIngestionEnabled",
        "internet_query_enabled": "internetQueryEnabled",
        "local_authentication_disabled": "localAuthenticationDisabled",
        "retention_in_days": "retentionInDays",
        "sampling_percentage": "samplingPercentage",
        "tags": "tags",
        "timeouts": "timeouts",
        "workspace_id": "workspaceId",
    },
)
class ApplicationInsightsConfig(cdktf.TerraformMetaArguments):
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
        application_type: builtins.str,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        daily_data_cap_in_gb: typing.Optional[jsii.Number] = None,
        daily_data_cap_notifications_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_ip_masking: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        force_customer_storage_for_profiler: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        internet_ingestion_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        internet_query_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        local_authentication_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_in_days: typing.Optional[jsii.Number] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ApplicationInsightsTimeouts", typing.Dict[str, typing.Any]]] = None,
        workspace_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param application_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#application_type ApplicationInsights#application_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#location ApplicationInsights#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#name ApplicationInsights#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#resource_group_name ApplicationInsights#resource_group_name}.
        :param daily_data_cap_in_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#daily_data_cap_in_gb ApplicationInsights#daily_data_cap_in_gb}.
        :param daily_data_cap_notifications_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#daily_data_cap_notifications_disabled ApplicationInsights#daily_data_cap_notifications_disabled}.
        :param disable_ip_masking: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#disable_ip_masking ApplicationInsights#disable_ip_masking}.
        :param force_customer_storage_for_profiler: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#force_customer_storage_for_profiler ApplicationInsights#force_customer_storage_for_profiler}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#id ApplicationInsights#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_ingestion_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#internet_ingestion_enabled ApplicationInsights#internet_ingestion_enabled}.
        :param internet_query_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#internet_query_enabled ApplicationInsights#internet_query_enabled}.
        :param local_authentication_disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#local_authentication_disabled ApplicationInsights#local_authentication_disabled}.
        :param retention_in_days: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#retention_in_days ApplicationInsights#retention_in_days}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#sampling_percentage ApplicationInsights#sampling_percentage}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#tags ApplicationInsights#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#timeouts ApplicationInsights#timeouts}
        :param workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#workspace_id ApplicationInsights#workspace_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ApplicationInsightsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationInsightsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument application_type", value=application_type, expected_type=type_hints["application_type"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument daily_data_cap_in_gb", value=daily_data_cap_in_gb, expected_type=type_hints["daily_data_cap_in_gb"])
            check_type(argname="argument daily_data_cap_notifications_disabled", value=daily_data_cap_notifications_disabled, expected_type=type_hints["daily_data_cap_notifications_disabled"])
            check_type(argname="argument disable_ip_masking", value=disable_ip_masking, expected_type=type_hints["disable_ip_masking"])
            check_type(argname="argument force_customer_storage_for_profiler", value=force_customer_storage_for_profiler, expected_type=type_hints["force_customer_storage_for_profiler"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument internet_ingestion_enabled", value=internet_ingestion_enabled, expected_type=type_hints["internet_ingestion_enabled"])
            check_type(argname="argument internet_query_enabled", value=internet_query_enabled, expected_type=type_hints["internet_query_enabled"])
            check_type(argname="argument local_authentication_disabled", value=local_authentication_disabled, expected_type=type_hints["local_authentication_disabled"])
            check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
            check_type(argname="argument sampling_percentage", value=sampling_percentage, expected_type=type_hints["sampling_percentage"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_type": application_type,
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
        if daily_data_cap_in_gb is not None:
            self._values["daily_data_cap_in_gb"] = daily_data_cap_in_gb
        if daily_data_cap_notifications_disabled is not None:
            self._values["daily_data_cap_notifications_disabled"] = daily_data_cap_notifications_disabled
        if disable_ip_masking is not None:
            self._values["disable_ip_masking"] = disable_ip_masking
        if force_customer_storage_for_profiler is not None:
            self._values["force_customer_storage_for_profiler"] = force_customer_storage_for_profiler
        if id is not None:
            self._values["id"] = id
        if internet_ingestion_enabled is not None:
            self._values["internet_ingestion_enabled"] = internet_ingestion_enabled
        if internet_query_enabled is not None:
            self._values["internet_query_enabled"] = internet_query_enabled
        if local_authentication_disabled is not None:
            self._values["local_authentication_disabled"] = local_authentication_disabled
        if retention_in_days is not None:
            self._values["retention_in_days"] = retention_in_days
        if sampling_percentage is not None:
            self._values["sampling_percentage"] = sampling_percentage
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if workspace_id is not None:
            self._values["workspace_id"] = workspace_id

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
    def application_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#application_type ApplicationInsights#application_type}.'''
        result = self._values.get("application_type")
        assert result is not None, "Required property 'application_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#location ApplicationInsights#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#name ApplicationInsights#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#resource_group_name ApplicationInsights#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def daily_data_cap_in_gb(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#daily_data_cap_in_gb ApplicationInsights#daily_data_cap_in_gb}.'''
        result = self._values.get("daily_data_cap_in_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def daily_data_cap_notifications_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#daily_data_cap_notifications_disabled ApplicationInsights#daily_data_cap_notifications_disabled}.'''
        result = self._values.get("daily_data_cap_notifications_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_ip_masking(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#disable_ip_masking ApplicationInsights#disable_ip_masking}.'''
        result = self._values.get("disable_ip_masking")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def force_customer_storage_for_profiler(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#force_customer_storage_for_profiler ApplicationInsights#force_customer_storage_for_profiler}.'''
        result = self._values.get("force_customer_storage_for_profiler")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#id ApplicationInsights#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internet_ingestion_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#internet_ingestion_enabled ApplicationInsights#internet_ingestion_enabled}.'''
        result = self._values.get("internet_ingestion_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def internet_query_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#internet_query_enabled ApplicationInsights#internet_query_enabled}.'''
        result = self._values.get("internet_query_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def local_authentication_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#local_authentication_disabled ApplicationInsights#local_authentication_disabled}.'''
        result = self._values.get("local_authentication_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#retention_in_days ApplicationInsights#retention_in_days}.'''
        result = self._values.get("retention_in_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sampling_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#sampling_percentage ApplicationInsights#sampling_percentage}.'''
        result = self._values.get("sampling_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#tags ApplicationInsights#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApplicationInsightsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#timeouts ApplicationInsights#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApplicationInsightsTimeouts"], result)

    @builtins.property
    def workspace_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#workspace_id ApplicationInsights#workspace_id}.'''
        result = self._values.get("workspace_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationInsightsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.applicationInsights.ApplicationInsightsTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApplicationInsightsTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#create ApplicationInsights#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#delete ApplicationInsights#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#read ApplicationInsights#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#update ApplicationInsights#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApplicationInsightsTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#create ApplicationInsights#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#delete ApplicationInsights#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#read ApplicationInsights#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/application_insights#update ApplicationInsights#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationInsightsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApplicationInsightsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.applicationInsights.ApplicationInsightsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApplicationInsightsTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApplicationInsightsTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsightsTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsightsTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsightsTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApplicationInsightsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApplicationInsightsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApplicationInsightsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApplicationInsightsTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApplicationInsights",
    "ApplicationInsightsConfig",
    "ApplicationInsightsTimeouts",
    "ApplicationInsightsTimeoutsOutputReference",
]

publication.publish()
