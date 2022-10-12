'''
# `azurerm_monitor_scheduled_query_rules_alert_v2`

Refer to the Terraform Registory for docs: [`azurerm_monitor_scheduled_query_rules_alert_v2`](https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2).
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


class MonitorScheduledQueryRulesAlertV2(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2 azurerm_monitor_scheduled_query_rules_alert_v2}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        criteria: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorScheduledQueryRulesAlertV2Criteria", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        scopes: typing.Sequence[builtins.str],
        severity: jsii.Number,
        window_duration: builtins.str,
        action: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertV2Action", typing.Dict[str, typing.Any]]] = None,
        auto_mitigation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        evaluation_frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mute_actions_after_alert_duration: typing.Optional[builtins.str] = None,
        query_time_range_override: typing.Optional[builtins.str] = None,
        skip_query_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertV2Timeouts", typing.Dict[str, typing.Any]]] = None,
        workspace_alerts_storage_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2 azurerm_monitor_scheduled_query_rules_alert_v2} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param criteria: criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#criteria MonitorScheduledQueryRulesAlertV2#criteria}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#location MonitorScheduledQueryRulesAlertV2#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#name MonitorScheduledQueryRulesAlertV2#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#resource_group_name MonitorScheduledQueryRulesAlertV2#resource_group_name}.
        :param scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#scopes MonitorScheduledQueryRulesAlertV2#scopes}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#severity MonitorScheduledQueryRulesAlertV2#severity}.
        :param window_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#window_duration MonitorScheduledQueryRulesAlertV2#window_duration}.
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#action MonitorScheduledQueryRulesAlertV2#action}
        :param auto_mitigation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#auto_mitigation_enabled MonitorScheduledQueryRulesAlertV2#auto_mitigation_enabled}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#description MonitorScheduledQueryRulesAlertV2#description}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#display_name MonitorScheduledQueryRulesAlertV2#display_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#enabled MonitorScheduledQueryRulesAlertV2#enabled}.
        :param evaluation_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#evaluation_frequency MonitorScheduledQueryRulesAlertV2#evaluation_frequency}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#id MonitorScheduledQueryRulesAlertV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mute_actions_after_alert_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#mute_actions_after_alert_duration MonitorScheduledQueryRulesAlertV2#mute_actions_after_alert_duration}.
        :param query_time_range_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#query_time_range_override MonitorScheduledQueryRulesAlertV2#query_time_range_override}.
        :param skip_query_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#skip_query_validation MonitorScheduledQueryRulesAlertV2#skip_query_validation}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#tags MonitorScheduledQueryRulesAlertV2#tags}.
        :param target_resource_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#target_resource_types MonitorScheduledQueryRulesAlertV2#target_resource_types}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#timeouts MonitorScheduledQueryRulesAlertV2#timeouts}
        :param workspace_alerts_storage_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#workspace_alerts_storage_enabled MonitorScheduledQueryRulesAlertV2#workspace_alerts_storage_enabled}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorScheduledQueryRulesAlertV2Config(
            criteria=criteria,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            scopes=scopes,
            severity=severity,
            window_duration=window_duration,
            action=action,
            auto_mitigation_enabled=auto_mitigation_enabled,
            description=description,
            display_name=display_name,
            enabled=enabled,
            evaluation_frequency=evaluation_frequency,
            id=id,
            mute_actions_after_alert_duration=mute_actions_after_alert_duration,
            query_time_range_override=query_time_range_override,
            skip_query_validation=skip_query_validation,
            tags=tags,
            target_resource_types=target_resource_types,
            timeouts=timeouts,
            workspace_alerts_storage_enabled=workspace_alerts_storage_enabled,
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
        action_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param action_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#action_groups MonitorScheduledQueryRulesAlertV2#action_groups}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#custom_properties MonitorScheduledQueryRulesAlertV2#custom_properties}.
        '''
        value = MonitorScheduledQueryRulesAlertV2Action(
            action_groups=action_groups, custom_properties=custom_properties
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putCriteria")
    def put_criteria(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorScheduledQueryRulesAlertV2Criteria", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2.put_criteria)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCriteria", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#create MonitorScheduledQueryRulesAlertV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#delete MonitorScheduledQueryRulesAlertV2#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#read MonitorScheduledQueryRulesAlertV2#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#update MonitorScheduledQueryRulesAlertV2#update}.
        '''
        value = MonitorScheduledQueryRulesAlertV2Timeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetAutoMitigationEnabled")
    def reset_auto_mitigation_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMitigationEnabled", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEvaluationFrequency")
    def reset_evaluation_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationFrequency", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMuteActionsAfterAlertDuration")
    def reset_mute_actions_after_alert_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMuteActionsAfterAlertDuration", []))

    @jsii.member(jsii_name="resetQueryTimeRangeOverride")
    def reset_query_time_range_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryTimeRangeOverride", []))

    @jsii.member(jsii_name="resetSkipQueryValidation")
    def reset_skip_query_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipQueryValidation", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTargetResourceTypes")
    def reset_target_resource_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResourceTypes", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetWorkspaceAlertsStorageEnabled")
    def reset_workspace_alerts_storage_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceAlertsStorageEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> "MonitorScheduledQueryRulesAlertV2ActionOutputReference":
        return typing.cast("MonitorScheduledQueryRulesAlertV2ActionOutputReference", jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="createdWithApiVersion")
    def created_with_api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdWithApiVersion"))

    @builtins.property
    @jsii.member(jsii_name="criteria")
    def criteria(self) -> "MonitorScheduledQueryRulesAlertV2CriteriaList":
        return typing.cast("MonitorScheduledQueryRulesAlertV2CriteriaList", jsii.get(self, "criteria"))

    @builtins.property
    @jsii.member(jsii_name="isALegacyLogAnalyticsRule")
    def is_a_legacy_log_analytics_rule(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isALegacyLogAnalyticsRule"))

    @builtins.property
    @jsii.member(jsii_name="isWorkspaceAlertsStorageConfigured")
    def is_workspace_alerts_storage_configured(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "isWorkspaceAlertsStorageConfigured"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference":
        return typing.cast("MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(
        self,
    ) -> typing.Optional["MonitorScheduledQueryRulesAlertV2Action"]:
        return typing.cast(typing.Optional["MonitorScheduledQueryRulesAlertV2Action"], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMitigationEnabledInput")
    def auto_mitigation_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoMitigationEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="criteriaInput")
    def criteria_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorScheduledQueryRulesAlertV2Criteria"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorScheduledQueryRulesAlertV2Criteria"]]], jsii.get(self, "criteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationFrequencyInput")
    def evaluation_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="muteActionsAfterAlertDurationInput")
    def mute_actions_after_alert_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "muteActionsAfterAlertDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryTimeRangeOverrideInput")
    def query_time_range_override_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryTimeRangeOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scopesInput")
    def scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scopesInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="skipQueryValidationInput")
    def skip_query_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipQueryValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceTypesInput")
    def target_resource_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetResourceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertV2Timeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertV2Timeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowDurationInput")
    def window_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceAlertsStorageEnabledInput")
    def workspace_alerts_storage_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "workspaceAlertsStorageEnabledInput"))

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
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "auto_mitigation_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMitigationEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationFrequency")
    def evaluation_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluationFrequency"))

    @evaluation_frequency.setter
    def evaluation_frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "evaluation_frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="muteActionsAfterAlertDuration")
    def mute_actions_after_alert_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "muteActionsAfterAlertDuration"))

    @mute_actions_after_alert_duration.setter
    def mute_actions_after_alert_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "mute_actions_after_alert_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "muteActionsAfterAlertDuration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryTimeRangeOverride")
    def query_time_range_override(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryTimeRangeOverride"))

    @query_time_range_override.setter
    def query_time_range_override(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "query_time_range_override").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryTimeRangeOverride", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scopes"))

    @scopes.setter
    def scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopes", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="skipQueryValidation")
    def skip_query_validation(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipQueryValidation"))

    @skip_query_validation.setter
    def skip_query_validation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "skip_query_validation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipQueryValidation", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="targetResourceTypes")
    def target_resource_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetResourceTypes"))

    @target_resource_types.setter
    def target_resource_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "target_resource_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetResourceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="windowDuration")
    def window_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "windowDuration"))

    @window_duration.setter
    def window_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "window_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowDuration", value)

    @builtins.property
    @jsii.member(jsii_name="workspaceAlertsStorageEnabled")
    def workspace_alerts_storage_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "workspaceAlertsStorageEnabled"))

    @workspace_alerts_storage_enabled.setter
    def workspace_alerts_storage_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2, "workspace_alerts_storage_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceAlertsStorageEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2Action",
    jsii_struct_bases=[],
    name_mapping={
        "action_groups": "actionGroups",
        "custom_properties": "customProperties",
    },
)
class MonitorScheduledQueryRulesAlertV2Action:
    def __init__(
        self,
        *,
        action_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        custom_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param action_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#action_groups MonitorScheduledQueryRulesAlertV2#action_groups}.
        :param custom_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#custom_properties MonitorScheduledQueryRulesAlertV2#custom_properties}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2Action.__init__)
            check_type(argname="argument action_groups", value=action_groups, expected_type=type_hints["action_groups"])
            check_type(argname="argument custom_properties", value=custom_properties, expected_type=type_hints["custom_properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action_groups is not None:
            self._values["action_groups"] = action_groups
        if custom_properties is not None:
            self._values["custom_properties"] = custom_properties

    @builtins.property
    def action_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#action_groups MonitorScheduledQueryRulesAlertV2#action_groups}.'''
        result = self._values.get("action_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def custom_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#custom_properties MonitorScheduledQueryRulesAlertV2#custom_properties}.'''
        result = self._values.get("custom_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertV2Action(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorScheduledQueryRulesAlertV2ActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2ActionOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2ActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActionGroups")
    def reset_action_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionGroups", []))

    @jsii.member(jsii_name="resetCustomProperties")
    def reset_custom_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomProperties", []))

    @builtins.property
    @jsii.member(jsii_name="actionGroupsInput")
    def action_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "actionGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="customPropertiesInput")
    def custom_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="actionGroups")
    def action_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actionGroups"))

    @action_groups.setter
    def action_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2ActionOutputReference, "action_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionGroups", value)

    @builtins.property
    @jsii.member(jsii_name="customProperties")
    def custom_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customProperties"))

    @custom_properties.setter
    def custom_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2ActionOutputReference, "custom_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customProperties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorScheduledQueryRulesAlertV2Action]:
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertV2Action], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorScheduledQueryRulesAlertV2Action],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2ActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "criteria": "criteria",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "scopes": "scopes",
        "severity": "severity",
        "window_duration": "windowDuration",
        "action": "action",
        "auto_mitigation_enabled": "autoMitigationEnabled",
        "description": "description",
        "display_name": "displayName",
        "enabled": "enabled",
        "evaluation_frequency": "evaluationFrequency",
        "id": "id",
        "mute_actions_after_alert_duration": "muteActionsAfterAlertDuration",
        "query_time_range_override": "queryTimeRangeOverride",
        "skip_query_validation": "skipQueryValidation",
        "tags": "tags",
        "target_resource_types": "targetResourceTypes",
        "timeouts": "timeouts",
        "workspace_alerts_storage_enabled": "workspaceAlertsStorageEnabled",
    },
)
class MonitorScheduledQueryRulesAlertV2Config(cdktf.TerraformMetaArguments):
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
        criteria: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorScheduledQueryRulesAlertV2Criteria", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        scopes: typing.Sequence[builtins.str],
        severity: jsii.Number,
        window_duration: builtins.str,
        action: typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2Action, typing.Dict[str, typing.Any]]] = None,
        auto_mitigation_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        evaluation_frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        mute_actions_after_alert_duration: typing.Optional[builtins.str] = None,
        query_time_range_override: typing.Optional[builtins.str] = None,
        skip_query_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertV2Timeouts", typing.Dict[str, typing.Any]]] = None,
        workspace_alerts_storage_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param criteria: criteria block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#criteria MonitorScheduledQueryRulesAlertV2#criteria}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#location MonitorScheduledQueryRulesAlertV2#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#name MonitorScheduledQueryRulesAlertV2#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#resource_group_name MonitorScheduledQueryRulesAlertV2#resource_group_name}.
        :param scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#scopes MonitorScheduledQueryRulesAlertV2#scopes}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#severity MonitorScheduledQueryRulesAlertV2#severity}.
        :param window_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#window_duration MonitorScheduledQueryRulesAlertV2#window_duration}.
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#action MonitorScheduledQueryRulesAlertV2#action}
        :param auto_mitigation_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#auto_mitigation_enabled MonitorScheduledQueryRulesAlertV2#auto_mitigation_enabled}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#description MonitorScheduledQueryRulesAlertV2#description}.
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#display_name MonitorScheduledQueryRulesAlertV2#display_name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#enabled MonitorScheduledQueryRulesAlertV2#enabled}.
        :param evaluation_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#evaluation_frequency MonitorScheduledQueryRulesAlertV2#evaluation_frequency}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#id MonitorScheduledQueryRulesAlertV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param mute_actions_after_alert_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#mute_actions_after_alert_duration MonitorScheduledQueryRulesAlertV2#mute_actions_after_alert_duration}.
        :param query_time_range_override: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#query_time_range_override MonitorScheduledQueryRulesAlertV2#query_time_range_override}.
        :param skip_query_validation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#skip_query_validation MonitorScheduledQueryRulesAlertV2#skip_query_validation}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#tags MonitorScheduledQueryRulesAlertV2#tags}.
        :param target_resource_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#target_resource_types MonitorScheduledQueryRulesAlertV2#target_resource_types}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#timeouts MonitorScheduledQueryRulesAlertV2#timeouts}
        :param workspace_alerts_storage_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#workspace_alerts_storage_enabled MonitorScheduledQueryRulesAlertV2#workspace_alerts_storage_enabled}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(action, dict):
            action = MonitorScheduledQueryRulesAlertV2Action(**action)
        if isinstance(timeouts, dict):
            timeouts = MonitorScheduledQueryRulesAlertV2Timeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument window_duration", value=window_duration, expected_type=type_hints["window_duration"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument auto_mitigation_enabled", value=auto_mitigation_enabled, expected_type=type_hints["auto_mitigation_enabled"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument evaluation_frequency", value=evaluation_frequency, expected_type=type_hints["evaluation_frequency"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument mute_actions_after_alert_duration", value=mute_actions_after_alert_duration, expected_type=type_hints["mute_actions_after_alert_duration"])
            check_type(argname="argument query_time_range_override", value=query_time_range_override, expected_type=type_hints["query_time_range_override"])
            check_type(argname="argument skip_query_validation", value=skip_query_validation, expected_type=type_hints["skip_query_validation"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_resource_types", value=target_resource_types, expected_type=type_hints["target_resource_types"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument workspace_alerts_storage_enabled", value=workspace_alerts_storage_enabled, expected_type=type_hints["workspace_alerts_storage_enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "criteria": criteria,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "scopes": scopes,
            "severity": severity,
            "window_duration": window_duration,
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
        if action is not None:
            self._values["action"] = action
        if auto_mitigation_enabled is not None:
            self._values["auto_mitigation_enabled"] = auto_mitigation_enabled
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if evaluation_frequency is not None:
            self._values["evaluation_frequency"] = evaluation_frequency
        if id is not None:
            self._values["id"] = id
        if mute_actions_after_alert_duration is not None:
            self._values["mute_actions_after_alert_duration"] = mute_actions_after_alert_duration
        if query_time_range_override is not None:
            self._values["query_time_range_override"] = query_time_range_override
        if skip_query_validation is not None:
            self._values["skip_query_validation"] = skip_query_validation
        if tags is not None:
            self._values["tags"] = tags
        if target_resource_types is not None:
            self._values["target_resource_types"] = target_resource_types
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if workspace_alerts_storage_enabled is not None:
            self._values["workspace_alerts_storage_enabled"] = workspace_alerts_storage_enabled

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
    def criteria(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["MonitorScheduledQueryRulesAlertV2Criteria"]]:
        '''criteria block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#criteria MonitorScheduledQueryRulesAlertV2#criteria}
        '''
        result = self._values.get("criteria")
        assert result is not None, "Required property 'criteria' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["MonitorScheduledQueryRulesAlertV2Criteria"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#location MonitorScheduledQueryRulesAlertV2#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#name MonitorScheduledQueryRulesAlertV2#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#resource_group_name MonitorScheduledQueryRulesAlertV2#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scopes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#scopes MonitorScheduledQueryRulesAlertV2#scopes}.'''
        result = self._values.get("scopes")
        assert result is not None, "Required property 'scopes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def severity(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#severity MonitorScheduledQueryRulesAlertV2#severity}.'''
        result = self._values.get("severity")
        assert result is not None, "Required property 'severity' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def window_duration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#window_duration MonitorScheduledQueryRulesAlertV2#window_duration}.'''
        result = self._values.get("window_duration")
        assert result is not None, "Required property 'window_duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action(self) -> typing.Optional[MonitorScheduledQueryRulesAlertV2Action]:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#action MonitorScheduledQueryRulesAlertV2#action}
        '''
        result = self._values.get("action")
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertV2Action], result)

    @builtins.property
    def auto_mitigation_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#auto_mitigation_enabled MonitorScheduledQueryRulesAlertV2#auto_mitigation_enabled}.'''
        result = self._values.get("auto_mitigation_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#description MonitorScheduledQueryRulesAlertV2#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#display_name MonitorScheduledQueryRulesAlertV2#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#enabled MonitorScheduledQueryRulesAlertV2#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def evaluation_frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#evaluation_frequency MonitorScheduledQueryRulesAlertV2#evaluation_frequency}.'''
        result = self._values.get("evaluation_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#id MonitorScheduledQueryRulesAlertV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mute_actions_after_alert_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#mute_actions_after_alert_duration MonitorScheduledQueryRulesAlertV2#mute_actions_after_alert_duration}.'''
        result = self._values.get("mute_actions_after_alert_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_time_range_override(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#query_time_range_override MonitorScheduledQueryRulesAlertV2#query_time_range_override}.'''
        result = self._values.get("query_time_range_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_query_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#skip_query_validation MonitorScheduledQueryRulesAlertV2#skip_query_validation}.'''
        result = self._values.get("skip_query_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#tags MonitorScheduledQueryRulesAlertV2#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#target_resource_types MonitorScheduledQueryRulesAlertV2#target_resource_types}.'''
        result = self._values.get("target_resource_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MonitorScheduledQueryRulesAlertV2Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#timeouts MonitorScheduledQueryRulesAlertV2#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MonitorScheduledQueryRulesAlertV2Timeouts"], result)

    @builtins.property
    def workspace_alerts_storage_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#workspace_alerts_storage_enabled MonitorScheduledQueryRulesAlertV2#workspace_alerts_storage_enabled}.'''
        result = self._values.get("workspace_alerts_storage_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertV2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2Criteria",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "query": "query",
        "threshold": "threshold",
        "time_aggregation_method": "timeAggregationMethod",
        "dimension": "dimension",
        "failing_periods": "failingPeriods",
        "metric_measure_column": "metricMeasureColumn",
        "resource_id_column": "resourceIdColumn",
    },
)
class MonitorScheduledQueryRulesAlertV2Criteria:
    def __init__(
        self,
        *,
        operator: builtins.str,
        query: builtins.str,
        threshold: jsii.Number,
        time_aggregation_method: builtins.str,
        dimension: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorScheduledQueryRulesAlertV2CriteriaDimension", typing.Dict[str, typing.Any]]]]] = None,
        failing_periods: typing.Optional[typing.Union["MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods", typing.Dict[str, typing.Any]]] = None,
        metric_measure_column: typing.Optional[builtins.str] = None,
        resource_id_column: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#operator MonitorScheduledQueryRulesAlertV2#operator}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#query MonitorScheduledQueryRulesAlertV2#query}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#threshold MonitorScheduledQueryRulesAlertV2#threshold}.
        :param time_aggregation_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#time_aggregation_method MonitorScheduledQueryRulesAlertV2#time_aggregation_method}.
        :param dimension: dimension block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#dimension MonitorScheduledQueryRulesAlertV2#dimension}
        :param failing_periods: failing_periods block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#failing_periods MonitorScheduledQueryRulesAlertV2#failing_periods}
        :param metric_measure_column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#metric_measure_column MonitorScheduledQueryRulesAlertV2#metric_measure_column}.
        :param resource_id_column: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#resource_id_column MonitorScheduledQueryRulesAlertV2#resource_id_column}.
        '''
        if isinstance(failing_periods, dict):
            failing_periods = MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods(**failing_periods)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2Criteria.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument time_aggregation_method", value=time_aggregation_method, expected_type=type_hints["time_aggregation_method"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument failing_periods", value=failing_periods, expected_type=type_hints["failing_periods"])
            check_type(argname="argument metric_measure_column", value=metric_measure_column, expected_type=type_hints["metric_measure_column"])
            check_type(argname="argument resource_id_column", value=resource_id_column, expected_type=type_hints["resource_id_column"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "query": query,
            "threshold": threshold,
            "time_aggregation_method": time_aggregation_method,
        }
        if dimension is not None:
            self._values["dimension"] = dimension
        if failing_periods is not None:
            self._values["failing_periods"] = failing_periods
        if metric_measure_column is not None:
            self._values["metric_measure_column"] = metric_measure_column
        if resource_id_column is not None:
            self._values["resource_id_column"] = resource_id_column

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#operator MonitorScheduledQueryRulesAlertV2#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#query MonitorScheduledQueryRulesAlertV2#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#threshold MonitorScheduledQueryRulesAlertV2#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_aggregation_method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#time_aggregation_method MonitorScheduledQueryRulesAlertV2#time_aggregation_method}.'''
        result = self._values.get("time_aggregation_method")
        assert result is not None, "Required property 'time_aggregation_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimension(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorScheduledQueryRulesAlertV2CriteriaDimension"]]]:
        '''dimension block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#dimension MonitorScheduledQueryRulesAlertV2#dimension}
        '''
        result = self._values.get("dimension")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorScheduledQueryRulesAlertV2CriteriaDimension"]]], result)

    @builtins.property
    def failing_periods(
        self,
    ) -> typing.Optional["MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods"]:
        '''failing_periods block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#failing_periods MonitorScheduledQueryRulesAlertV2#failing_periods}
        '''
        result = self._values.get("failing_periods")
        return typing.cast(typing.Optional["MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods"], result)

    @builtins.property
    def metric_measure_column(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#metric_measure_column MonitorScheduledQueryRulesAlertV2#metric_measure_column}.'''
        result = self._values.get("metric_measure_column")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_id_column(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#resource_id_column MonitorScheduledQueryRulesAlertV2#resource_id_column}.'''
        result = self._values.get("resource_id_column")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertV2Criteria(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2CriteriaDimension",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "operator": "operator", "values": "values"},
)
class MonitorScheduledQueryRulesAlertV2CriteriaDimension:
    def __init__(
        self,
        *,
        name: builtins.str,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#name MonitorScheduledQueryRulesAlertV2#name}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#operator MonitorScheduledQueryRulesAlertV2#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#values MonitorScheduledQueryRulesAlertV2#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaDimension.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#name MonitorScheduledQueryRulesAlertV2#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#operator MonitorScheduledQueryRulesAlertV2#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#values MonitorScheduledQueryRulesAlertV2#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertV2CriteriaDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorScheduledQueryRulesAlertV2CriteriaDimensionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2CriteriaDimensionList",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaDimensionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaDimensionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2CriteriaDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2CriteriaDimension]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2CriteriaDimension]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2CriteriaDimension, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2CriteriaDimension, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2CriteriaDimension, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods",
    jsii_struct_bases=[],
    name_mapping={
        "minimum_failing_periods_to_trigger_alert": "minimumFailingPeriodsToTriggerAlert",
        "number_of_evaluation_periods": "numberOfEvaluationPeriods",
    },
)
class MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods:
    def __init__(
        self,
        *,
        minimum_failing_periods_to_trigger_alert: jsii.Number,
        number_of_evaluation_periods: jsii.Number,
    ) -> None:
        '''
        :param minimum_failing_periods_to_trigger_alert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#minimum_failing_periods_to_trigger_alert MonitorScheduledQueryRulesAlertV2#minimum_failing_periods_to_trigger_alert}.
        :param number_of_evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#number_of_evaluation_periods MonitorScheduledQueryRulesAlertV2#number_of_evaluation_periods}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods.__init__)
            check_type(argname="argument minimum_failing_periods_to_trigger_alert", value=minimum_failing_periods_to_trigger_alert, expected_type=type_hints["minimum_failing_periods_to_trigger_alert"])
            check_type(argname="argument number_of_evaluation_periods", value=number_of_evaluation_periods, expected_type=type_hints["number_of_evaluation_periods"])
        self._values: typing.Dict[str, typing.Any] = {
            "minimum_failing_periods_to_trigger_alert": minimum_failing_periods_to_trigger_alert,
            "number_of_evaluation_periods": number_of_evaluation_periods,
        }

    @builtins.property
    def minimum_failing_periods_to_trigger_alert(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#minimum_failing_periods_to_trigger_alert MonitorScheduledQueryRulesAlertV2#minimum_failing_periods_to_trigger_alert}.'''
        result = self._values.get("minimum_failing_periods_to_trigger_alert")
        assert result is not None, "Required property 'minimum_failing_periods_to_trigger_alert' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def number_of_evaluation_periods(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#number_of_evaluation_periods MonitorScheduledQueryRulesAlertV2#number_of_evaluation_periods}.'''
        result = self._values.get("number_of_evaluation_periods")
        assert result is not None, "Required property 'number_of_evaluation_periods' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="minimumFailingPeriodsToTriggerAlertInput")
    def minimum_failing_periods_to_trigger_alert_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumFailingPeriodsToTriggerAlertInput"))

    @builtins.property
    @jsii.member(jsii_name="numberOfEvaluationPeriodsInput")
    def number_of_evaluation_periods_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numberOfEvaluationPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumFailingPeriodsToTriggerAlert")
    def minimum_failing_periods_to_trigger_alert(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minimumFailingPeriodsToTriggerAlert"))

    @minimum_failing_periods_to_trigger_alert.setter
    def minimum_failing_periods_to_trigger_alert(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference, "minimum_failing_periods_to_trigger_alert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumFailingPeriodsToTriggerAlert", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfEvaluationPeriods")
    def number_of_evaluation_periods(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numberOfEvaluationPeriods"))

    @number_of_evaluation_periods.setter
    def number_of_evaluation_periods(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference, "number_of_evaluation_periods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfEvaluationPeriods", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods]:
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorScheduledQueryRulesAlertV2CriteriaList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2CriteriaList",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorScheduledQueryRulesAlertV2CriteriaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorScheduledQueryRulesAlertV2CriteriaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2Criteria]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2Criteria]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2Criteria]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorScheduledQueryRulesAlertV2CriteriaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2CriteriaOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDimension")
    def put_dimension(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorScheduledQueryRulesAlertV2CriteriaDimension, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference.put_dimension)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDimension", [value]))

    @jsii.member(jsii_name="putFailingPeriods")
    def put_failing_periods(
        self,
        *,
        minimum_failing_periods_to_trigger_alert: jsii.Number,
        number_of_evaluation_periods: jsii.Number,
    ) -> None:
        '''
        :param minimum_failing_periods_to_trigger_alert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#minimum_failing_periods_to_trigger_alert MonitorScheduledQueryRulesAlertV2#minimum_failing_periods_to_trigger_alert}.
        :param number_of_evaluation_periods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#number_of_evaluation_periods MonitorScheduledQueryRulesAlertV2#number_of_evaluation_periods}.
        '''
        value = MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods(
            minimum_failing_periods_to_trigger_alert=minimum_failing_periods_to_trigger_alert,
            number_of_evaluation_periods=number_of_evaluation_periods,
        )

        return typing.cast(None, jsii.invoke(self, "putFailingPeriods", [value]))

    @jsii.member(jsii_name="resetDimension")
    def reset_dimension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDimension", []))

    @jsii.member(jsii_name="resetFailingPeriods")
    def reset_failing_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailingPeriods", []))

    @jsii.member(jsii_name="resetMetricMeasureColumn")
    def reset_metric_measure_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricMeasureColumn", []))

    @jsii.member(jsii_name="resetResourceIdColumn")
    def reset_resource_id_column(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceIdColumn", []))

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> MonitorScheduledQueryRulesAlertV2CriteriaDimensionList:
        return typing.cast(MonitorScheduledQueryRulesAlertV2CriteriaDimensionList, jsii.get(self, "dimension"))

    @builtins.property
    @jsii.member(jsii_name="failingPeriods")
    def failing_periods(
        self,
    ) -> MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference:
        return typing.cast(MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference, jsii.get(self, "failingPeriods"))

    @builtins.property
    @jsii.member(jsii_name="dimensionInput")
    def dimension_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2CriteriaDimension]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorScheduledQueryRulesAlertV2CriteriaDimension]]], jsii.get(self, "dimensionInput"))

    @builtins.property
    @jsii.member(jsii_name="failingPeriodsInput")
    def failing_periods_input(
        self,
    ) -> typing.Optional[MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods]:
        return typing.cast(typing.Optional[MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods], jsii.get(self, "failingPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricMeasureColumnInput")
    def metric_measure_column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricMeasureColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdColumnInput")
    def resource_id_column_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdColumnInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeAggregationMethodInput")
    def time_aggregation_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeAggregationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="metricMeasureColumn")
    def metric_measure_column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricMeasureColumn"))

    @metric_measure_column.setter
    def metric_measure_column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference, "metric_measure_column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricMeasureColumn", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdColumn")
    def resource_id_column(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceIdColumn"))

    @resource_id_column.setter
    def resource_id_column(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference, "resource_id_column").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdColumn", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="timeAggregationMethod")
    def time_aggregation_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeAggregationMethod"))

    @time_aggregation_method.setter
    def time_aggregation_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference, "time_aggregation_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeAggregationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2Criteria, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2Criteria, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2Criteria, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2CriteriaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2Timeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MonitorScheduledQueryRulesAlertV2Timeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#create MonitorScheduledQueryRulesAlertV2#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#delete MonitorScheduledQueryRulesAlertV2#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#read MonitorScheduledQueryRulesAlertV2#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#update MonitorScheduledQueryRulesAlertV2#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2Timeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#create MonitorScheduledQueryRulesAlertV2#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#delete MonitorScheduledQueryRulesAlertV2#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#read MonitorScheduledQueryRulesAlertV2#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_scheduled_query_rules_alert_v2#update MonitorScheduledQueryRulesAlertV2#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorScheduledQueryRulesAlertV2Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorScheduledQueryRulesAlertV2.MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2Timeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2Timeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorScheduledQueryRulesAlertV2Timeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorScheduledQueryRulesAlertV2",
    "MonitorScheduledQueryRulesAlertV2Action",
    "MonitorScheduledQueryRulesAlertV2ActionOutputReference",
    "MonitorScheduledQueryRulesAlertV2Config",
    "MonitorScheduledQueryRulesAlertV2Criteria",
    "MonitorScheduledQueryRulesAlertV2CriteriaDimension",
    "MonitorScheduledQueryRulesAlertV2CriteriaDimensionList",
    "MonitorScheduledQueryRulesAlertV2CriteriaDimensionOutputReference",
    "MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriods",
    "MonitorScheduledQueryRulesAlertV2CriteriaFailingPeriodsOutputReference",
    "MonitorScheduledQueryRulesAlertV2CriteriaList",
    "MonitorScheduledQueryRulesAlertV2CriteriaOutputReference",
    "MonitorScheduledQueryRulesAlertV2Timeouts",
    "MonitorScheduledQueryRulesAlertV2TimeoutsOutputReference",
]

publication.publish()
