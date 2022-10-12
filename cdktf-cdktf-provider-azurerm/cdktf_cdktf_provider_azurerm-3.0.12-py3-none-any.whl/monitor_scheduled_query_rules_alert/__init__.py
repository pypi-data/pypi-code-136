'''
# `azurerm_monitor_scheduled_query_rules_alert`

Refer to the Terraform Registory for docs: [`azurerm_monitor_scheduled_query_rules_alert`](https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert).
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


class MonitorScheduledQueryRulesAlert(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlert",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert azurerm_monitor_scheduled_query_rules_alert}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        action: typing.Union["MonitorScheduledQueryRulesAlertAction", typing.Dict[str, typing.Any]],
        data_source_id: builtins.str,
        frequency: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        query: builtins.str,
        resource_group_name: builtins.str,
        time_window: jsii.Number,
        trigger: typing.Union["MonitorScheduledQueryRulesAlertTrigger", typing.Dict[str, typing.Any]],
        authorized_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_mitigation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        query_type: typing.Optional[builtins.str] = None,
        severity: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        throttling: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert azurerm_monitor_scheduled_query_rules_alert} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#action MonitorScheduledQueryRulesAlert#action}
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#data_source_id MonitorScheduledQueryRulesAlert#data_source_id}.
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#frequency MonitorScheduledQueryRulesAlert#frequency}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#location MonitorScheduledQueryRulesAlert#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#name MonitorScheduledQueryRulesAlert#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#query MonitorScheduledQueryRulesAlert#query}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#resource_group_name MonitorScheduledQueryRulesAlert#resource_group_name}.
        :param time_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#time_window MonitorScheduledQueryRulesAlert#time_window}.
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#trigger MonitorScheduledQueryRulesAlert#trigger}
        :param authorized_resource_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#authorized_resource_ids MonitorScheduledQueryRulesAlert#authorized_resource_ids}.
        :param auto_mitigation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#auto_mitigation_enabled MonitorScheduledQueryRulesAlert#auto_mitigation_enabled}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#description MonitorScheduledQueryRulesAlert#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#enabled MonitorScheduledQueryRulesAlert#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#id MonitorScheduledQueryRulesAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param query_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#query_type MonitorScheduledQueryRulesAlert#query_type}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#severity MonitorScheduledQueryRulesAlert#severity}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#tags MonitorScheduledQueryRulesAlert#tags}.
        :param throttling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#throttling MonitorScheduledQueryRulesAlert#throttling}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#timeouts MonitorScheduledQueryRulesAlert#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlert.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorScheduledQueryRulesAlertConfig(
            action=action,
            data_source_id=data_source_id,
            frequency=frequency,
            location=location,
            name=name,
            query=query,
            resource_group_name=resource_group_name,
            time_window=time_window,
            trigger=trigger,
            authorized_resource_ids=authorized_resource_ids,
            auto_mitigation_enabled=auto_mitigation_enabled,
            description=description,
            enabled=enabled,
            id=id,
            query_type=query_type,
            severity=severity,
            tags=tags,
            throttling=throttling,
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

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        action_group: typing.Sequence[builtins.str],
        custom_webhook_payload: typing.Optional[builtins.str] = None,
        email_subject: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#action_group MonitorScheduledQueryRulesAlert#action_group}.
        :param custom_webhook_payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#custom_webhook_payload MonitorScheduledQueryRulesAlert#custom_webhook_payload}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#email_subject MonitorScheduledQueryRulesAlert#email_subject}.
        '''
        value = MonitorScheduledQueryRulesAlertAction(
            action_group=action_group,
            custom_webhook_payload=custom_webhook_payload,
            email_subject=email_subject,
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#create MonitorScheduledQueryRulesAlert#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#delete MonitorScheduledQueryRulesAlert#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#read MonitorScheduledQueryRulesAlert#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#update MonitorScheduledQueryRulesAlert#update}.
        '''
        value = MonitorScheduledQueryRulesAlertTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTrigger")
    def put_trigger(
        self,
        *,
        operator: builtins.str,
        threshold: jsii.Number,
        metric_trigger: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertTriggerMetricTrigger", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#operator MonitorScheduledQueryRulesAlert#operator}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#threshold MonitorScheduledQueryRulesAlert#threshold}.
        :param metric_trigger: metric_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_trigger MonitorScheduledQueryRulesAlert#metric_trigger}
        '''
        value = MonitorScheduledQueryRulesAlertTrigger(
            operator=operator, threshold=threshold, metric_trigger=metric_trigger
        )

        return typing.cast(None, jsii.invoke(self, "putTrigger", [value]))

    @jsii.member(jsii_name="resetAuthorizedResourceIds")
    def reset_authorized_resource_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizedResourceIds", []))

    @jsii.member(jsii_name="resetAutoMitigationEnabled")
    def reset_auto_mitigation_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMitigationEnabled", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetQueryType")
    def reset_query_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryType", []))

    @jsii.member(jsii_name="resetSeverity")
    def reset_severity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverity", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetThrottling")
    def reset_throttling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThrottling", []))

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
    @jsii.member(jsii_name="action")
    def action(self) -> "MonitorScheduledQueryRulesAlertActionOutputReference":
        return typing.cast("MonitorScheduledQueryRulesAlertActionOutputReference", jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MonitorScheduledQueryRulesAlertTimeoutsOutputReference":
        return typing.cast("MonitorScheduledQueryRulesAlertTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="trigger")
    def trigger(self) -> "MonitorScheduledQueryRulesAlertTriggerOutputReference":
        return typing.cast("MonitorScheduledQueryRulesAlertTriggerOutputReference", jsii.get(self, "trigger"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional["MonitorScheduledQueryRulesAlertAction"]:
        return typing.cast(typing.Optional["MonitorScheduledQueryRulesAlertAction"], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizedResourceIdsInput")
    def authorized_resource_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authorizedResourceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMitigationEnabledInput")
    def auto_mitigation_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoMitigationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceIdInput")
    def data_source_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="queryTypeInput")
    def query_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="throttlingInput")
    def throttling_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "throttlingInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeWindowInput")
    def time_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerInput")
    def trigger_input(
        self,
    ) -> typing.Optional["MonitorScheduledQueryRulesAlertTrigger"]:
        return typing.cast(typing.Optional["MonitorScheduledQueryRulesAlertTrigger"], jsii.get(self, "triggerInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizedResourceIds")
    def authorized_resource_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authorizedResourceIds"))

    @authorized_resource_ids.setter
    def authorized_resource_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "authorized_resource_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedResourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="autoMitigationEnabled")
    def auto_mitigation_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoMitigationEnabled"))

    @auto_mitigation_enabled.setter
    def auto_mitigation_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "auto_mitigation_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMitigationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="dataSourceId")
    def data_source_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceId"))

    @data_source_id.setter
    def data_source_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "data_source_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="queryType")
    def query_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryType"))

    @query_type.setter
    def query_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "query_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="throttling")
    def throttling(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "throttling"))

    @throttling.setter
    def throttling(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "throttling").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throttling", value)

    @builtins.property
    @jsii.member(jsii_name="timeWindow")
    def time_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeWindow"))

    @time_window.setter
    def time_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlert, "time_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeWindow", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertAction",
    jsii_struct_bases=[],
    name_mapping={
        "action_group": "actionGroup",
        "custom_webhook_payload": "customWebhookPayload",
        "email_subject": "emailSubject",
    },
)
class MonitorScheduledQueryRulesAlertAction:
    def __init__(
        self,
        *,
        action_group: typing.Sequence[builtins.str],
        custom_webhook_payload: typing.Optional[builtins.str] = None,
        email_subject: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#action_group MonitorScheduledQueryRulesAlert#action_group}.
        :param custom_webhook_payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#custom_webhook_payload MonitorScheduledQueryRulesAlert#custom_webhook_payload}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#email_subject MonitorScheduledQueryRulesAlert#email_subject}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertAction.__init__)
            check_type(argname="argument action_group", value=action_group, expected_type=type_hints["action_group"])
            check_type(argname="argument custom_webhook_payload", value=custom_webhook_payload, expected_type=type_hints["custom_webhook_payload"])
            check_type(argname="argument email_subject", value=email_subject, expected_type=type_hints["email_subject"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_group": action_group,
        }
        if custom_webhook_payload is not None:
            self._values["custom_webhook_payload"] = custom_webhook_payload
        if email_subject is not None:
            self._values["email_subject"] = email_subject

    @builtins.property
    def action_group(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#action_group MonitorScheduledQueryRulesAlert#action_group}.'''
        result = self._values.get("action_group")
        assert result is not None, "Required property 'action_group' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def custom_webhook_payload(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#custom_webhook_payload MonitorScheduledQueryRulesAlert#custom_webhook_payload}.'''
        result = self._values.get("custom_webhook_payload")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#email_subject MonitorScheduledQueryRulesAlert#email_subject}.'''
        result = self._values.get("email_subject")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorScheduledQueryRulesAlertActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertActionOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomWebhookPayload")
    def reset_custom_webhook_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomWebhookPayload", []))

    @jsii.member(jsii_name="resetEmailSubject")
    def reset_email_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailSubject", []))

    @builtins.property
    @jsii.member(jsii_name="actionGroupInput")
    def action_group_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="customWebhookPayloadInput")
    def custom_webhook_payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customWebhookPayloadInput"))

    @builtins.property
    @jsii.member(jsii_name="emailSubjectInput")
    def email_subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailSubjectInput"))

    @builtins.property
    @jsii.member(jsii_name="actionGroup")
    def action_group(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actionGroup"))

    @action_group.setter
    def action_group(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertActionOutputReference, "action_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionGroup", value)

    @builtins.property
    @jsii.member(jsii_name="customWebhookPayload")
    def custom_webhook_payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customWebhookPayload"))

    @custom_webhook_payload.setter
    def custom_webhook_payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertActionOutputReference, "custom_webhook_payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customWebhookPayload", value)

    @builtins.property
    @jsii.member(jsii_name="emailSubject")
    def email_subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailSubject"))

    @email_subject.setter
    def email_subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertActionOutputReference, "email_subject").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailSubject", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorScheduledQueryRulesAlertAction]:
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorScheduledQueryRulesAlertAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "data_source_id": "dataSourceId",
        "frequency": "frequency",
        "location": "location",
        "name": "name",
        "query": "query",
        "resource_group_name": "resourceGroupName",
        "time_window": "timeWindow",
        "trigger": "trigger",
        "authorized_resource_ids": "authorizedResourceIds",
        "auto_mitigation_enabled": "autoMitigationEnabled",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "query_type": "queryType",
        "severity": "severity",
        "tags": "tags",
        "throttling": "throttling",
        "timeouts": "timeouts",
    },
)
class MonitorScheduledQueryRulesAlertConfig(cdktf.TerraformMetaArguments):
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
        action: typing.Union[MonitorScheduledQueryRulesAlertAction, typing.Dict[str, typing.Any]],
        data_source_id: builtins.str,
        frequency: jsii.Number,
        location: builtins.str,
        name: builtins.str,
        query: builtins.str,
        resource_group_name: builtins.str,
        time_window: jsii.Number,
        trigger: typing.Union["MonitorScheduledQueryRulesAlertTrigger", typing.Dict[str, typing.Any]],
        authorized_resource_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        auto_mitigation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        query_type: typing.Optional[builtins.str] = None,
        severity: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        throttling: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#action MonitorScheduledQueryRulesAlert#action}
        :param data_source_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#data_source_id MonitorScheduledQueryRulesAlert#data_source_id}.
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#frequency MonitorScheduledQueryRulesAlert#frequency}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#location MonitorScheduledQueryRulesAlert#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#name MonitorScheduledQueryRulesAlert#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#query MonitorScheduledQueryRulesAlert#query}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#resource_group_name MonitorScheduledQueryRulesAlert#resource_group_name}.
        :param time_window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#time_window MonitorScheduledQueryRulesAlert#time_window}.
        :param trigger: trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#trigger MonitorScheduledQueryRulesAlert#trigger}
        :param authorized_resource_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#authorized_resource_ids MonitorScheduledQueryRulesAlert#authorized_resource_ids}.
        :param auto_mitigation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#auto_mitigation_enabled MonitorScheduledQueryRulesAlert#auto_mitigation_enabled}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#description MonitorScheduledQueryRulesAlert#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#enabled MonitorScheduledQueryRulesAlert#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#id MonitorScheduledQueryRulesAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param query_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#query_type MonitorScheduledQueryRulesAlert#query_type}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#severity MonitorScheduledQueryRulesAlert#severity}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#tags MonitorScheduledQueryRulesAlert#tags}.
        :param throttling: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#throttling MonitorScheduledQueryRulesAlert#throttling}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#timeouts MonitorScheduledQueryRulesAlert#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(action, dict):
            action = MonitorScheduledQueryRulesAlertAction(**action)
        if isinstance(trigger, dict):
            trigger = MonitorScheduledQueryRulesAlertTrigger(**trigger)
        if isinstance(timeouts, dict):
            timeouts = MonitorScheduledQueryRulesAlertTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument time_window", value=time_window, expected_type=type_hints["time_window"])
            check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
            check_type(argname="argument authorized_resource_ids", value=authorized_resource_ids, expected_type=type_hints["authorized_resource_ids"])
            check_type(argname="argument auto_mitigation_enabled", value=auto_mitigation_enabled, expected_type=type_hints["auto_mitigation_enabled"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument query_type", value=query_type, expected_type=type_hints["query_type"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument throttling", value=throttling, expected_type=type_hints["throttling"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "data_source_id": data_source_id,
            "frequency": frequency,
            "location": location,
            "name": name,
            "query": query,
            "resource_group_name": resource_group_name,
            "time_window": time_window,
            "trigger": trigger,
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
        if authorized_resource_ids is not None:
            self._values["authorized_resource_ids"] = authorized_resource_ids
        if auto_mitigation_enabled is not None:
            self._values["auto_mitigation_enabled"] = auto_mitigation_enabled
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if query_type is not None:
            self._values["query_type"] = query_type
        if severity is not None:
            self._values["severity"] = severity
        if tags is not None:
            self._values["tags"] = tags
        if throttling is not None:
            self._values["throttling"] = throttling
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
    def action(self) -> MonitorScheduledQueryRulesAlertAction:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#action MonitorScheduledQueryRulesAlert#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(MonitorScheduledQueryRulesAlertAction, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#data_source_id MonitorScheduledQueryRulesAlert#data_source_id}.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def frequency(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#frequency MonitorScheduledQueryRulesAlert#frequency}.'''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#location MonitorScheduledQueryRulesAlert#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#name MonitorScheduledQueryRulesAlert#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#query MonitorScheduledQueryRulesAlert#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#resource_group_name MonitorScheduledQueryRulesAlert#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_window(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#time_window MonitorScheduledQueryRulesAlert#time_window}.'''
        result = self._values.get("time_window")
        assert result is not None, "Required property 'time_window' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def trigger(self) -> "MonitorScheduledQueryRulesAlertTrigger":
        '''trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#trigger MonitorScheduledQueryRulesAlert#trigger}
        '''
        result = self._values.get("trigger")
        assert result is not None, "Required property 'trigger' is missing"
        return typing.cast("MonitorScheduledQueryRulesAlertTrigger", result)

    @builtins.property
    def authorized_resource_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#authorized_resource_ids MonitorScheduledQueryRulesAlert#authorized_resource_ids}.'''
        result = self._values.get("authorized_resource_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def auto_mitigation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#auto_mitigation_enabled MonitorScheduledQueryRulesAlert#auto_mitigation_enabled}.'''
        result = self._values.get("auto_mitigation_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#description MonitorScheduledQueryRulesAlert#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#enabled MonitorScheduledQueryRulesAlert#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#id MonitorScheduledQueryRulesAlert#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#query_type MonitorScheduledQueryRulesAlert#query_type}.'''
        result = self._values.get("query_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def severity(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#severity MonitorScheduledQueryRulesAlert#severity}.'''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#tags MonitorScheduledQueryRulesAlert#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def throttling(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#throttling MonitorScheduledQueryRulesAlert#throttling}.'''
        result = self._values.get("throttling")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MonitorScheduledQueryRulesAlertTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#timeouts MonitorScheduledQueryRulesAlert#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MonitorScheduledQueryRulesAlertTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MonitorScheduledQueryRulesAlertTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#create MonitorScheduledQueryRulesAlert#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#delete MonitorScheduledQueryRulesAlert#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#read MonitorScheduledQueryRulesAlert#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#update MonitorScheduledQueryRulesAlert#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#create MonitorScheduledQueryRulesAlert#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#delete MonitorScheduledQueryRulesAlert#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#read MonitorScheduledQueryRulesAlert#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#update MonitorScheduledQueryRulesAlert#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorScheduledQueryRulesAlertTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "threshold": "threshold",
        "metric_trigger": "metricTrigger",
    },
)
class MonitorScheduledQueryRulesAlertTrigger:
    def __init__(
        self,
        *,
        operator: builtins.str,
        threshold: jsii.Number,
        metric_trigger: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertTriggerMetricTrigger", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#operator MonitorScheduledQueryRulesAlert#operator}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#threshold MonitorScheduledQueryRulesAlert#threshold}.
        :param metric_trigger: metric_trigger block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_trigger MonitorScheduledQueryRulesAlert#metric_trigger}
        '''
        if isinstance(metric_trigger, dict):
            metric_trigger = MonitorScheduledQueryRulesAlertTriggerMetricTrigger(**metric_trigger)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertTrigger.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument metric_trigger", value=metric_trigger, expected_type=type_hints["metric_trigger"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "threshold": threshold,
        }
        if metric_trigger is not None:
            self._values["metric_trigger"] = metric_trigger

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#operator MonitorScheduledQueryRulesAlert#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#threshold MonitorScheduledQueryRulesAlert#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metric_trigger(
        self,
    ) -> typing.Optional["MonitorScheduledQueryRulesAlertTriggerMetricTrigger"]:
        '''metric_trigger block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_trigger MonitorScheduledQueryRulesAlert#metric_trigger}
        '''
        result = self._values.get("metric_trigger")
        return typing.cast(typing.Optional["MonitorScheduledQueryRulesAlertTriggerMetricTrigger"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertTriggerMetricTrigger",
    jsii_struct_bases=[],
    name_mapping={
        "metric_column": "metricColumn",
        "metric_trigger_type": "metricTriggerType",
        "operator": "operator",
        "threshold": "threshold",
    },
)
class MonitorScheduledQueryRulesAlertTriggerMetricTrigger:
    def __init__(
        self,
        *,
        metric_column: builtins.str,
        metric_trigger_type: builtins.str,
        operator: builtins.str,
        threshold: jsii.Number,
    ) -> None:
        '''
        :param metric_column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_column MonitorScheduledQueryRulesAlert#metric_column}.
        :param metric_trigger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_trigger_type MonitorScheduledQueryRulesAlert#metric_trigger_type}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#operator MonitorScheduledQueryRulesAlert#operator}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#threshold MonitorScheduledQueryRulesAlert#threshold}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertTriggerMetricTrigger.__init__)
            check_type(argname="argument metric_column", value=metric_column, expected_type=type_hints["metric_column"])
            check_type(argname="argument metric_trigger_type", value=metric_trigger_type, expected_type=type_hints["metric_trigger_type"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric_column": metric_column,
            "metric_trigger_type": metric_trigger_type,
            "operator": operator,
            "threshold": threshold,
        }

    @builtins.property
    def metric_column(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_column MonitorScheduledQueryRulesAlert#metric_column}.'''
        result = self._values.get("metric_column")
        assert result is not None, "Required property 'metric_column' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_trigger_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_trigger_type MonitorScheduledQueryRulesAlert#metric_trigger_type}.'''
        result = self._values.get("metric_trigger_type")
        assert result is not None, "Required property 'metric_trigger_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#operator MonitorScheduledQueryRulesAlert#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#threshold MonitorScheduledQueryRulesAlert#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertTriggerMetricTrigger(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="metricColumnInput")
    def metric_column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="metricTriggerTypeInput")
    def metric_trigger_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricTriggerTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="metricColumn")
    def metric_column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricColumn"))

    @metric_column.setter
    def metric_column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference, "metric_column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricColumn", value)

    @builtins.property
    @jsii.member(jsii_name="metricTriggerType")
    def metric_trigger_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricTriggerType"))

    @metric_trigger_type.setter
    def metric_trigger_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference, "metric_trigger_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricTriggerType", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorScheduledQueryRulesAlertTriggerMetricTrigger]:
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertTriggerMetricTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorScheduledQueryRulesAlertTriggerMetricTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorScheduledQueryRulesAlertTriggerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlert.MonitorScheduledQueryRulesAlertTriggerOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertTriggerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetricTrigger")
    def put_metric_trigger(
        self,
        *,
        metric_column: builtins.str,
        metric_trigger_type: builtins.str,
        operator: builtins.str,
        threshold: jsii.Number,
    ) -> None:
        '''
        :param metric_column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_column MonitorScheduledQueryRulesAlert#metric_column}.
        :param metric_trigger_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#metric_trigger_type MonitorScheduledQueryRulesAlert#metric_trigger_type}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#operator MonitorScheduledQueryRulesAlert#operator}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert#threshold MonitorScheduledQueryRulesAlert#threshold}.
        '''
        value = MonitorScheduledQueryRulesAlertTriggerMetricTrigger(
            metric_column=metric_column,
            metric_trigger_type=metric_trigger_type,
            operator=operator,
            threshold=threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putMetricTrigger", [value]))

    @jsii.member(jsii_name="resetMetricTrigger")
    def reset_metric_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricTrigger", []))

    @builtins.property
    @jsii.member(jsii_name="metricTrigger")
    def metric_trigger(
        self,
    ) -> MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference:
        return typing.cast(MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference, jsii.get(self, "metricTrigger"))

    @builtins.property
    @jsii.member(jsii_name="metricTriggerInput")
    def metric_trigger_input(
        self,
    ) -> typing.Optional[MonitorScheduledQueryRulesAlertTriggerMetricTrigger]:
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertTriggerMetricTrigger], jsii.get(self, "metricTriggerInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorScheduledQueryRulesAlertTrigger]:
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertTrigger], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorScheduledQueryRulesAlertTrigger],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertTriggerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorScheduledQueryRulesAlert",
    "MonitorScheduledQueryRulesAlertAction",
    "MonitorScheduledQueryRulesAlertActionOutputReference",
    "MonitorScheduledQueryRulesAlertConfig",
    "MonitorScheduledQueryRulesAlertTimeouts",
    "MonitorScheduledQueryRulesAlertTimeoutsOutputReference",
    "MonitorScheduledQueryRulesAlertTrigger",
    "MonitorScheduledQueryRulesAlertTriggerMetricTrigger",
    "MonitorScheduledQueryRulesAlertTriggerMetricTriggerOutputReference",
    "MonitorScheduledQueryRulesAlertTriggerOutputReference",
]

publication.publish()
