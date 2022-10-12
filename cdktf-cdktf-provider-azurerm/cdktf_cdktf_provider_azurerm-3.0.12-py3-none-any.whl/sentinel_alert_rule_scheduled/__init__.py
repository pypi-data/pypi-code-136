'''
# `azurerm_sentinel_alert_rule_scheduled`

Refer to the Terraform Registory for docs: [`azurerm_sentinel_alert_rule_scheduled`](https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled).
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


class SentinelAlertRuleScheduled(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduled",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled azurerm_sentinel_alert_rule_scheduled}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        log_analytics_workspace_id: builtins.str,
        name: builtins.str,
        query: builtins.str,
        severity: builtins.str,
        alert_details_override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SentinelAlertRuleScheduledAlertDetailsOverride", typing.Dict[str, typing.Any]]]]] = None,
        alert_rule_template_guid: typing.Optional[builtins.str] = None,
        alert_rule_template_version: typing.Optional[builtins.str] = None,
        custom_details: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        entity_mapping: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SentinelAlertRuleScheduledEntityMapping", typing.Dict[str, typing.Any]]]]] = None,
        event_grouping: typing.Optional[typing.Union["SentinelAlertRuleScheduledEventGrouping", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        incident_configuration: typing.Optional[typing.Union["SentinelAlertRuleScheduledIncidentConfiguration", typing.Dict[str, typing.Any]]] = None,
        query_frequency: typing.Optional[builtins.str] = None,
        query_period: typing.Optional[builtins.str] = None,
        suppression_duration: typing.Optional[builtins.str] = None,
        suppression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tactics: typing.Optional[typing.Sequence[builtins.str]] = None,
        techniques: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SentinelAlertRuleScheduledTimeouts", typing.Dict[str, typing.Any]]] = None,
        trigger_operator: typing.Optional[builtins.str] = None,
        trigger_threshold: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled azurerm_sentinel_alert_rule_scheduled} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#display_name SentinelAlertRuleScheduled#display_name}.
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#log_analytics_workspace_id SentinelAlertRuleScheduled#log_analytics_workspace_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#name SentinelAlertRuleScheduled#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query SentinelAlertRuleScheduled#query}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#severity SentinelAlertRuleScheduled#severity}.
        :param alert_details_override: alert_details_override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_details_override SentinelAlertRuleScheduled#alert_details_override}
        :param alert_rule_template_guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_rule_template_guid SentinelAlertRuleScheduled#alert_rule_template_guid}.
        :param alert_rule_template_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_rule_template_version SentinelAlertRuleScheduled#alert_rule_template_version}.
        :param custom_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#custom_details SentinelAlertRuleScheduled#custom_details}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#description SentinelAlertRuleScheduled#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#enabled SentinelAlertRuleScheduled#enabled}.
        :param entity_mapping: entity_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_mapping SentinelAlertRuleScheduled#entity_mapping}
        :param event_grouping: event_grouping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#event_grouping SentinelAlertRuleScheduled#event_grouping}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#id SentinelAlertRuleScheduled#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param incident_configuration: incident_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#incident_configuration SentinelAlertRuleScheduled#incident_configuration}
        :param query_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query_frequency SentinelAlertRuleScheduled#query_frequency}.
        :param query_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query_period SentinelAlertRuleScheduled#query_period}.
        :param suppression_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#suppression_duration SentinelAlertRuleScheduled#suppression_duration}.
        :param suppression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#suppression_enabled SentinelAlertRuleScheduled#suppression_enabled}.
        :param tactics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#tactics SentinelAlertRuleScheduled#tactics}.
        :param techniques: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#techniques SentinelAlertRuleScheduled#techniques}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#timeouts SentinelAlertRuleScheduled#timeouts}
        :param trigger_operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#trigger_operator SentinelAlertRuleScheduled#trigger_operator}.
        :param trigger_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#trigger_threshold SentinelAlertRuleScheduled#trigger_threshold}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduled.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SentinelAlertRuleScheduledConfig(
            display_name=display_name,
            log_analytics_workspace_id=log_analytics_workspace_id,
            name=name,
            query=query,
            severity=severity,
            alert_details_override=alert_details_override,
            alert_rule_template_guid=alert_rule_template_guid,
            alert_rule_template_version=alert_rule_template_version,
            custom_details=custom_details,
            description=description,
            enabled=enabled,
            entity_mapping=entity_mapping,
            event_grouping=event_grouping,
            id=id,
            incident_configuration=incident_configuration,
            query_frequency=query_frequency,
            query_period=query_period,
            suppression_duration=suppression_duration,
            suppression_enabled=suppression_enabled,
            tactics=tactics,
            techniques=techniques,
            timeouts=timeouts,
            trigger_operator=trigger_operator,
            trigger_threshold=trigger_threshold,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlertDetailsOverride")
    def put_alert_details_override(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SentinelAlertRuleScheduledAlertDetailsOverride", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduled.put_alert_details_override)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlertDetailsOverride", [value]))

    @jsii.member(jsii_name="putEntityMapping")
    def put_entity_mapping(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SentinelAlertRuleScheduledEntityMapping", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduled.put_entity_mapping)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEntityMapping", [value]))

    @jsii.member(jsii_name="putEventGrouping")
    def put_event_grouping(self, *, aggregation_method: builtins.str) -> None:
        '''
        :param aggregation_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#aggregation_method SentinelAlertRuleScheduled#aggregation_method}.
        '''
        value = SentinelAlertRuleScheduledEventGrouping(
            aggregation_method=aggregation_method
        )

        return typing.cast(None, jsii.invoke(self, "putEventGrouping", [value]))

    @jsii.member(jsii_name="putIncidentConfiguration")
    def put_incident_configuration(
        self,
        *,
        create_incident: typing.Union[builtins.bool, cdktf.IResolvable],
        grouping: typing.Union["SentinelAlertRuleScheduledIncidentConfigurationGrouping", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param create_incident: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#create_incident SentinelAlertRuleScheduled#create_incident}.
        :param grouping: grouping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#grouping SentinelAlertRuleScheduled#grouping}
        '''
        value = SentinelAlertRuleScheduledIncidentConfiguration(
            create_incident=create_incident, grouping=grouping
        )

        return typing.cast(None, jsii.invoke(self, "putIncidentConfiguration", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#create SentinelAlertRuleScheduled#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#delete SentinelAlertRuleScheduled#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#read SentinelAlertRuleScheduled#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#update SentinelAlertRuleScheduled#update}.
        '''
        value = SentinelAlertRuleScheduledTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAlertDetailsOverride")
    def reset_alert_details_override(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertDetailsOverride", []))

    @jsii.member(jsii_name="resetAlertRuleTemplateGuid")
    def reset_alert_rule_template_guid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertRuleTemplateGuid", []))

    @jsii.member(jsii_name="resetAlertRuleTemplateVersion")
    def reset_alert_rule_template_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertRuleTemplateVersion", []))

    @jsii.member(jsii_name="resetCustomDetails")
    def reset_custom_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomDetails", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEntityMapping")
    def reset_entity_mapping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityMapping", []))

    @jsii.member(jsii_name="resetEventGrouping")
    def reset_event_grouping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventGrouping", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIncidentConfiguration")
    def reset_incident_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncidentConfiguration", []))

    @jsii.member(jsii_name="resetQueryFrequency")
    def reset_query_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFrequency", []))

    @jsii.member(jsii_name="resetQueryPeriod")
    def reset_query_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryPeriod", []))

    @jsii.member(jsii_name="resetSuppressionDuration")
    def reset_suppression_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppressionDuration", []))

    @jsii.member(jsii_name="resetSuppressionEnabled")
    def reset_suppression_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppressionEnabled", []))

    @jsii.member(jsii_name="resetTactics")
    def reset_tactics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTactics", []))

    @jsii.member(jsii_name="resetTechniques")
    def reset_techniques(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTechniques", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTriggerOperator")
    def reset_trigger_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerOperator", []))

    @jsii.member(jsii_name="resetTriggerThreshold")
    def reset_trigger_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerThreshold", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alertDetailsOverride")
    def alert_details_override(
        self,
    ) -> "SentinelAlertRuleScheduledAlertDetailsOverrideList":
        return typing.cast("SentinelAlertRuleScheduledAlertDetailsOverrideList", jsii.get(self, "alertDetailsOverride"))

    @builtins.property
    @jsii.member(jsii_name="entityMapping")
    def entity_mapping(self) -> "SentinelAlertRuleScheduledEntityMappingList":
        return typing.cast("SentinelAlertRuleScheduledEntityMappingList", jsii.get(self, "entityMapping"))

    @builtins.property
    @jsii.member(jsii_name="eventGrouping")
    def event_grouping(
        self,
    ) -> "SentinelAlertRuleScheduledEventGroupingOutputReference":
        return typing.cast("SentinelAlertRuleScheduledEventGroupingOutputReference", jsii.get(self, "eventGrouping"))

    @builtins.property
    @jsii.member(jsii_name="incidentConfiguration")
    def incident_configuration(
        self,
    ) -> "SentinelAlertRuleScheduledIncidentConfigurationOutputReference":
        return typing.cast("SentinelAlertRuleScheduledIncidentConfigurationOutputReference", jsii.get(self, "incidentConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "SentinelAlertRuleScheduledTimeoutsOutputReference":
        return typing.cast("SentinelAlertRuleScheduledTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="alertDetailsOverrideInput")
    def alert_details_override_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledAlertDetailsOverride"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledAlertDetailsOverride"]]], jsii.get(self, "alertDetailsOverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="alertRuleTemplateGuidInput")
    def alert_rule_template_guid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertRuleTemplateGuidInput"))

    @builtins.property
    @jsii.member(jsii_name="alertRuleTemplateVersionInput")
    def alert_rule_template_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertRuleTemplateVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="customDetailsInput")
    def custom_details_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customDetailsInput"))

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
    @jsii.member(jsii_name="entityMappingInput")
    def entity_mapping_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledEntityMapping"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledEntityMapping"]]], jsii.get(self, "entityMappingInput"))

    @builtins.property
    @jsii.member(jsii_name="eventGroupingInput")
    def event_grouping_input(
        self,
    ) -> typing.Optional["SentinelAlertRuleScheduledEventGrouping"]:
        return typing.cast(typing.Optional["SentinelAlertRuleScheduledEventGrouping"], jsii.get(self, "eventGroupingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="incidentConfigurationInput")
    def incident_configuration_input(
        self,
    ) -> typing.Optional["SentinelAlertRuleScheduledIncidentConfiguration"]:
        return typing.cast(typing.Optional["SentinelAlertRuleScheduledIncidentConfiguration"], jsii.get(self, "incidentConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceIdInput")
    def log_analytics_workspace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logAnalyticsWorkspaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFrequencyInput")
    def query_frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="queryPeriodInput")
    def query_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressionDurationInput")
    def suppression_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "suppressionDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressionEnabledInput")
    def suppression_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "suppressionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="tacticsInput")
    def tactics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tacticsInput"))

    @builtins.property
    @jsii.member(jsii_name="techniquesInput")
    def techniques_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "techniquesInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["SentinelAlertRuleScheduledTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["SentinelAlertRuleScheduledTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerOperatorInput")
    def trigger_operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerOperatorInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerThresholdInput")
    def trigger_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "triggerThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="alertRuleTemplateGuid")
    def alert_rule_template_guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertRuleTemplateGuid"))

    @alert_rule_template_guid.setter
    def alert_rule_template_guid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "alert_rule_template_guid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertRuleTemplateGuid", value)

    @builtins.property
    @jsii.member(jsii_name="alertRuleTemplateVersion")
    def alert_rule_template_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertRuleTemplateVersion"))

    @alert_rule_template_version.setter
    def alert_rule_template_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "alert_rule_template_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertRuleTemplateVersion", value)

    @builtins.property
    @jsii.member(jsii_name="customDetails")
    def custom_details(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customDetails"))

    @custom_details.setter
    def custom_details(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "custom_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customDetails", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logAnalyticsWorkspaceId")
    def log_analytics_workspace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logAnalyticsWorkspaceId"))

    @log_analytics_workspace_id.setter
    def log_analytics_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "log_analytics_workspace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logAnalyticsWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="queryFrequency")
    def query_frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFrequency"))

    @query_frequency.setter
    def query_frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "query_frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="queryPeriod")
    def query_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryPeriod"))

    @query_period.setter
    def query_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "query_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="suppressionDuration")
    def suppression_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "suppressionDuration"))

    @suppression_duration.setter
    def suppression_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "suppression_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppressionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="suppressionEnabled")
    def suppression_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "suppressionEnabled"))

    @suppression_enabled.setter
    def suppression_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "suppression_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppressionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="tactics")
    def tactics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tactics"))

    @tactics.setter
    def tactics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "tactics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tactics", value)

    @builtins.property
    @jsii.member(jsii_name="techniques")
    def techniques(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "techniques"))

    @techniques.setter
    def techniques(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "techniques").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "techniques", value)

    @builtins.property
    @jsii.member(jsii_name="triggerOperator")
    def trigger_operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerOperator"))

    @trigger_operator.setter
    def trigger_operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "trigger_operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerOperator", value)

    @builtins.property
    @jsii.member(jsii_name="triggerThreshold")
    def trigger_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "triggerThreshold"))

    @trigger_threshold.setter
    def trigger_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduled, "trigger_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerThreshold", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledAlertDetailsOverride",
    jsii_struct_bases=[],
    name_mapping={
        "description_format": "descriptionFormat",
        "display_name_format": "displayNameFormat",
        "severity_column_name": "severityColumnName",
        "tactics_column_name": "tacticsColumnName",
    },
)
class SentinelAlertRuleScheduledAlertDetailsOverride:
    def __init__(
        self,
        *,
        description_format: typing.Optional[builtins.str] = None,
        display_name_format: typing.Optional[builtins.str] = None,
        severity_column_name: typing.Optional[builtins.str] = None,
        tactics_column_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param description_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#description_format SentinelAlertRuleScheduled#description_format}.
        :param display_name_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#display_name_format SentinelAlertRuleScheduled#display_name_format}.
        :param severity_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#severity_column_name SentinelAlertRuleScheduled#severity_column_name}.
        :param tactics_column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#tactics_column_name SentinelAlertRuleScheduled#tactics_column_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledAlertDetailsOverride.__init__)
            check_type(argname="argument description_format", value=description_format, expected_type=type_hints["description_format"])
            check_type(argname="argument display_name_format", value=display_name_format, expected_type=type_hints["display_name_format"])
            check_type(argname="argument severity_column_name", value=severity_column_name, expected_type=type_hints["severity_column_name"])
            check_type(argname="argument tactics_column_name", value=tactics_column_name, expected_type=type_hints["tactics_column_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if description_format is not None:
            self._values["description_format"] = description_format
        if display_name_format is not None:
            self._values["display_name_format"] = display_name_format
        if severity_column_name is not None:
            self._values["severity_column_name"] = severity_column_name
        if tactics_column_name is not None:
            self._values["tactics_column_name"] = tactics_column_name

    @builtins.property
    def description_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#description_format SentinelAlertRuleScheduled#description_format}.'''
        result = self._values.get("description_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#display_name_format SentinelAlertRuleScheduled#display_name_format}.'''
        result = self._values.get("display_name_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def severity_column_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#severity_column_name SentinelAlertRuleScheduled#severity_column_name}.'''
        result = self._values.get("severity_column_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tactics_column_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#tactics_column_name SentinelAlertRuleScheduled#tactics_column_name}.'''
        result = self._values.get("tactics_column_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledAlertDetailsOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SentinelAlertRuleScheduledAlertDetailsOverrideList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledAlertDetailsOverrideList",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledAlertDetailsOverrideList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledAlertDetailsOverrideList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledAlertDetailsOverride]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledAlertDetailsOverride]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledAlertDetailsOverride]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescriptionFormat")
    def reset_description_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescriptionFormat", []))

    @jsii.member(jsii_name="resetDisplayNameFormat")
    def reset_display_name_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayNameFormat", []))

    @jsii.member(jsii_name="resetSeverityColumnName")
    def reset_severity_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverityColumnName", []))

    @jsii.member(jsii_name="resetTacticsColumnName")
    def reset_tactics_column_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTacticsColumnName", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionFormatInput")
    def description_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameFormatInput")
    def display_name_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="severityColumnNameInput")
    def severity_column_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severityColumnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tacticsColumnNameInput")
    def tactics_column_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tacticsColumnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionFormat")
    def description_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "descriptionFormat"))

    @description_format.setter
    def description_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference, "description_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "descriptionFormat", value)

    @builtins.property
    @jsii.member(jsii_name="displayNameFormat")
    def display_name_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayNameFormat"))

    @display_name_format.setter
    def display_name_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference, "display_name_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayNameFormat", value)

    @builtins.property
    @jsii.member(jsii_name="severityColumnName")
    def severity_column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "severityColumnName"))

    @severity_column_name.setter
    def severity_column_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference, "severity_column_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severityColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="tacticsColumnName")
    def tactics_column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tacticsColumnName"))

    @tactics_column_name.setter
    def tactics_column_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference, "tactics_column_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tacticsColumnName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SentinelAlertRuleScheduledAlertDetailsOverride, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SentinelAlertRuleScheduledAlertDetailsOverride, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SentinelAlertRuleScheduledAlertDetailsOverride, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "log_analytics_workspace_id": "logAnalyticsWorkspaceId",
        "name": "name",
        "query": "query",
        "severity": "severity",
        "alert_details_override": "alertDetailsOverride",
        "alert_rule_template_guid": "alertRuleTemplateGuid",
        "alert_rule_template_version": "alertRuleTemplateVersion",
        "custom_details": "customDetails",
        "description": "description",
        "enabled": "enabled",
        "entity_mapping": "entityMapping",
        "event_grouping": "eventGrouping",
        "id": "id",
        "incident_configuration": "incidentConfiguration",
        "query_frequency": "queryFrequency",
        "query_period": "queryPeriod",
        "suppression_duration": "suppressionDuration",
        "suppression_enabled": "suppressionEnabled",
        "tactics": "tactics",
        "techniques": "techniques",
        "timeouts": "timeouts",
        "trigger_operator": "triggerOperator",
        "trigger_threshold": "triggerThreshold",
    },
)
class SentinelAlertRuleScheduledConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        log_analytics_workspace_id: builtins.str,
        name: builtins.str,
        query: builtins.str,
        severity: builtins.str,
        alert_details_override: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SentinelAlertRuleScheduledAlertDetailsOverride, typing.Dict[str, typing.Any]]]]] = None,
        alert_rule_template_guid: typing.Optional[builtins.str] = None,
        alert_rule_template_version: typing.Optional[builtins.str] = None,
        custom_details: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        entity_mapping: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SentinelAlertRuleScheduledEntityMapping", typing.Dict[str, typing.Any]]]]] = None,
        event_grouping: typing.Optional[typing.Union["SentinelAlertRuleScheduledEventGrouping", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        incident_configuration: typing.Optional[typing.Union["SentinelAlertRuleScheduledIncidentConfiguration", typing.Dict[str, typing.Any]]] = None,
        query_frequency: typing.Optional[builtins.str] = None,
        query_period: typing.Optional[builtins.str] = None,
        suppression_duration: typing.Optional[builtins.str] = None,
        suppression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tactics: typing.Optional[typing.Sequence[builtins.str]] = None,
        techniques: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["SentinelAlertRuleScheduledTimeouts", typing.Dict[str, typing.Any]]] = None,
        trigger_operator: typing.Optional[builtins.str] = None,
        trigger_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#display_name SentinelAlertRuleScheduled#display_name}.
        :param log_analytics_workspace_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#log_analytics_workspace_id SentinelAlertRuleScheduled#log_analytics_workspace_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#name SentinelAlertRuleScheduled#name}.
        :param query: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query SentinelAlertRuleScheduled#query}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#severity SentinelAlertRuleScheduled#severity}.
        :param alert_details_override: alert_details_override block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_details_override SentinelAlertRuleScheduled#alert_details_override}
        :param alert_rule_template_guid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_rule_template_guid SentinelAlertRuleScheduled#alert_rule_template_guid}.
        :param alert_rule_template_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_rule_template_version SentinelAlertRuleScheduled#alert_rule_template_version}.
        :param custom_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#custom_details SentinelAlertRuleScheduled#custom_details}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#description SentinelAlertRuleScheduled#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#enabled SentinelAlertRuleScheduled#enabled}.
        :param entity_mapping: entity_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_mapping SentinelAlertRuleScheduled#entity_mapping}
        :param event_grouping: event_grouping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#event_grouping SentinelAlertRuleScheduled#event_grouping}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#id SentinelAlertRuleScheduled#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param incident_configuration: incident_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#incident_configuration SentinelAlertRuleScheduled#incident_configuration}
        :param query_frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query_frequency SentinelAlertRuleScheduled#query_frequency}.
        :param query_period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query_period SentinelAlertRuleScheduled#query_period}.
        :param suppression_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#suppression_duration SentinelAlertRuleScheduled#suppression_duration}.
        :param suppression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#suppression_enabled SentinelAlertRuleScheduled#suppression_enabled}.
        :param tactics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#tactics SentinelAlertRuleScheduled#tactics}.
        :param techniques: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#techniques SentinelAlertRuleScheduled#techniques}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#timeouts SentinelAlertRuleScheduled#timeouts}
        :param trigger_operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#trigger_operator SentinelAlertRuleScheduled#trigger_operator}.
        :param trigger_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#trigger_threshold SentinelAlertRuleScheduled#trigger_threshold}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(event_grouping, dict):
            event_grouping = SentinelAlertRuleScheduledEventGrouping(**event_grouping)
        if isinstance(incident_configuration, dict):
            incident_configuration = SentinelAlertRuleScheduledIncidentConfiguration(**incident_configuration)
        if isinstance(timeouts, dict):
            timeouts = SentinelAlertRuleScheduledTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument log_analytics_workspace_id", value=log_analytics_workspace_id, expected_type=type_hints["log_analytics_workspace_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument alert_details_override", value=alert_details_override, expected_type=type_hints["alert_details_override"])
            check_type(argname="argument alert_rule_template_guid", value=alert_rule_template_guid, expected_type=type_hints["alert_rule_template_guid"])
            check_type(argname="argument alert_rule_template_version", value=alert_rule_template_version, expected_type=type_hints["alert_rule_template_version"])
            check_type(argname="argument custom_details", value=custom_details, expected_type=type_hints["custom_details"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument entity_mapping", value=entity_mapping, expected_type=type_hints["entity_mapping"])
            check_type(argname="argument event_grouping", value=event_grouping, expected_type=type_hints["event_grouping"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument incident_configuration", value=incident_configuration, expected_type=type_hints["incident_configuration"])
            check_type(argname="argument query_frequency", value=query_frequency, expected_type=type_hints["query_frequency"])
            check_type(argname="argument query_period", value=query_period, expected_type=type_hints["query_period"])
            check_type(argname="argument suppression_duration", value=suppression_duration, expected_type=type_hints["suppression_duration"])
            check_type(argname="argument suppression_enabled", value=suppression_enabled, expected_type=type_hints["suppression_enabled"])
            check_type(argname="argument tactics", value=tactics, expected_type=type_hints["tactics"])
            check_type(argname="argument techniques", value=techniques, expected_type=type_hints["techniques"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument trigger_operator", value=trigger_operator, expected_type=type_hints["trigger_operator"])
            check_type(argname="argument trigger_threshold", value=trigger_threshold, expected_type=type_hints["trigger_threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "log_analytics_workspace_id": log_analytics_workspace_id,
            "name": name,
            "query": query,
            "severity": severity,
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
        if alert_details_override is not None:
            self._values["alert_details_override"] = alert_details_override
        if alert_rule_template_guid is not None:
            self._values["alert_rule_template_guid"] = alert_rule_template_guid
        if alert_rule_template_version is not None:
            self._values["alert_rule_template_version"] = alert_rule_template_version
        if custom_details is not None:
            self._values["custom_details"] = custom_details
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if entity_mapping is not None:
            self._values["entity_mapping"] = entity_mapping
        if event_grouping is not None:
            self._values["event_grouping"] = event_grouping
        if id is not None:
            self._values["id"] = id
        if incident_configuration is not None:
            self._values["incident_configuration"] = incident_configuration
        if query_frequency is not None:
            self._values["query_frequency"] = query_frequency
        if query_period is not None:
            self._values["query_period"] = query_period
        if suppression_duration is not None:
            self._values["suppression_duration"] = suppression_duration
        if suppression_enabled is not None:
            self._values["suppression_enabled"] = suppression_enabled
        if tactics is not None:
            self._values["tactics"] = tactics
        if techniques is not None:
            self._values["techniques"] = techniques
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if trigger_operator is not None:
            self._values["trigger_operator"] = trigger_operator
        if trigger_threshold is not None:
            self._values["trigger_threshold"] = trigger_threshold

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
    def display_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#display_name SentinelAlertRuleScheduled#display_name}.'''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_analytics_workspace_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#log_analytics_workspace_id SentinelAlertRuleScheduled#log_analytics_workspace_id}.'''
        result = self._values.get("log_analytics_workspace_id")
        assert result is not None, "Required property 'log_analytics_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#name SentinelAlertRuleScheduled#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query SentinelAlertRuleScheduled#query}.'''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def severity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#severity SentinelAlertRuleScheduled#severity}.'''
        result = self._values.get("severity")
        assert result is not None, "Required property 'severity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert_details_override(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledAlertDetailsOverride]]]:
        '''alert_details_override block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_details_override SentinelAlertRuleScheduled#alert_details_override}
        '''
        result = self._values.get("alert_details_override")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledAlertDetailsOverride]]], result)

    @builtins.property
    def alert_rule_template_guid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_rule_template_guid SentinelAlertRuleScheduled#alert_rule_template_guid}.'''
        result = self._values.get("alert_rule_template_guid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alert_rule_template_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#alert_rule_template_version SentinelAlertRuleScheduled#alert_rule_template_version}.'''
        result = self._values.get("alert_rule_template_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_details(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#custom_details SentinelAlertRuleScheduled#custom_details}.'''
        result = self._values.get("custom_details")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#description SentinelAlertRuleScheduled#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#enabled SentinelAlertRuleScheduled#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def entity_mapping(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledEntityMapping"]]]:
        '''entity_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_mapping SentinelAlertRuleScheduled#entity_mapping}
        '''
        result = self._values.get("entity_mapping")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledEntityMapping"]]], result)

    @builtins.property
    def event_grouping(
        self,
    ) -> typing.Optional["SentinelAlertRuleScheduledEventGrouping"]:
        '''event_grouping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#event_grouping SentinelAlertRuleScheduled#event_grouping}
        '''
        result = self._values.get("event_grouping")
        return typing.cast(typing.Optional["SentinelAlertRuleScheduledEventGrouping"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#id SentinelAlertRuleScheduled#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def incident_configuration(
        self,
    ) -> typing.Optional["SentinelAlertRuleScheduledIncidentConfiguration"]:
        '''incident_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#incident_configuration SentinelAlertRuleScheduled#incident_configuration}
        '''
        result = self._values.get("incident_configuration")
        return typing.cast(typing.Optional["SentinelAlertRuleScheduledIncidentConfiguration"], result)

    @builtins.property
    def query_frequency(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query_frequency SentinelAlertRuleScheduled#query_frequency}.'''
        result = self._values.get("query_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_period(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#query_period SentinelAlertRuleScheduled#query_period}.'''
        result = self._values.get("query_period")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suppression_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#suppression_duration SentinelAlertRuleScheduled#suppression_duration}.'''
        result = self._values.get("suppression_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suppression_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#suppression_enabled SentinelAlertRuleScheduled#suppression_enabled}.'''
        result = self._values.get("suppression_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tactics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#tactics SentinelAlertRuleScheduled#tactics}.'''
        result = self._values.get("tactics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def techniques(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#techniques SentinelAlertRuleScheduled#techniques}.'''
        result = self._values.get("techniques")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["SentinelAlertRuleScheduledTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#timeouts SentinelAlertRuleScheduled#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["SentinelAlertRuleScheduledTimeouts"], result)

    @builtins.property
    def trigger_operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#trigger_operator SentinelAlertRuleScheduled#trigger_operator}.'''
        result = self._values.get("trigger_operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#trigger_threshold SentinelAlertRuleScheduled#trigger_threshold}.'''
        result = self._values.get("trigger_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEntityMapping",
    jsii_struct_bases=[],
    name_mapping={"entity_type": "entityType", "field_mapping": "fieldMapping"},
)
class SentinelAlertRuleScheduledEntityMapping:
    def __init__(
        self,
        *,
        entity_type: builtins.str,
        field_mapping: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SentinelAlertRuleScheduledEntityMappingFieldMapping", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param entity_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_type SentinelAlertRuleScheduled#entity_type}.
        :param field_mapping: field_mapping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#field_mapping SentinelAlertRuleScheduled#field_mapping}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMapping.__init__)
            check_type(argname="argument entity_type", value=entity_type, expected_type=type_hints["entity_type"])
            check_type(argname="argument field_mapping", value=field_mapping, expected_type=type_hints["field_mapping"])
        self._values: typing.Dict[str, typing.Any] = {
            "entity_type": entity_type,
            "field_mapping": field_mapping,
        }

    @builtins.property
    def entity_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_type SentinelAlertRuleScheduled#entity_type}.'''
        result = self._values.get("entity_type")
        assert result is not None, "Required property 'entity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field_mapping(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledEntityMappingFieldMapping"]]:
        '''field_mapping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#field_mapping SentinelAlertRuleScheduled#field_mapping}
        '''
        result = self._values.get("field_mapping")
        assert result is not None, "Required property 'field_mapping' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["SentinelAlertRuleScheduledEntityMappingFieldMapping"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledEntityMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEntityMappingFieldMapping",
    jsii_struct_bases=[],
    name_mapping={"column_name": "columnName", "identifier": "identifier"},
)
class SentinelAlertRuleScheduledEntityMappingFieldMapping:
    def __init__(self, *, column_name: builtins.str, identifier: builtins.str) -> None:
        '''
        :param column_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#column_name SentinelAlertRuleScheduled#column_name}.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#identifier SentinelAlertRuleScheduled#identifier}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingFieldMapping.__init__)
            check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[str, typing.Any] = {
            "column_name": column_name,
            "identifier": identifier,
        }

    @builtins.property
    def column_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#column_name SentinelAlertRuleScheduled#column_name}.'''
        result = self._values.get("column_name")
        assert result is not None, "Required property 'column_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#identifier SentinelAlertRuleScheduled#identifier}.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledEntityMappingFieldMapping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SentinelAlertRuleScheduledEntityMappingFieldMappingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEntityMappingFieldMappingList",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingFieldMappingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingFieldMappingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingFieldMappingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingFieldMappingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingFieldMappingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMappingFieldMapping]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMappingFieldMapping]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMappingFieldMapping]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingFieldMappingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="columnNameInput")
    def column_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "columnNameInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="columnName")
    def column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "columnName"))

    @column_name.setter
    def column_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference, "column_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columnName", value)

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference, "identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SentinelAlertRuleScheduledEntityMappingFieldMapping, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SentinelAlertRuleScheduledEntityMappingFieldMapping, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SentinelAlertRuleScheduledEntityMappingFieldMapping, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SentinelAlertRuleScheduledEntityMappingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEntityMappingList",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SentinelAlertRuleScheduledEntityMappingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SentinelAlertRuleScheduledEntityMappingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMapping]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMapping]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMapping]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SentinelAlertRuleScheduledEntityMappingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEntityMappingOutputReference",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFieldMapping")
    def put_field_mapping(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SentinelAlertRuleScheduledEntityMappingFieldMapping, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEntityMappingOutputReference.put_field_mapping)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFieldMapping", [value]))

    @builtins.property
    @jsii.member(jsii_name="fieldMapping")
    def field_mapping(self) -> SentinelAlertRuleScheduledEntityMappingFieldMappingList:
        return typing.cast(SentinelAlertRuleScheduledEntityMappingFieldMappingList, jsii.get(self, "fieldMapping"))

    @builtins.property
    @jsii.member(jsii_name="entityTypeInput")
    def entity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldMappingInput")
    def field_mapping_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMappingFieldMapping]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SentinelAlertRuleScheduledEntityMappingFieldMapping]]], jsii.get(self, "fieldMappingInput"))

    @builtins.property
    @jsii.member(jsii_name="entityType")
    def entity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityType"))

    @entity_type.setter
    def entity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingOutputReference, "entity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SentinelAlertRuleScheduledEntityMapping, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SentinelAlertRuleScheduledEntityMapping, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SentinelAlertRuleScheduledEntityMapping, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEntityMappingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEventGrouping",
    jsii_struct_bases=[],
    name_mapping={"aggregation_method": "aggregationMethod"},
)
class SentinelAlertRuleScheduledEventGrouping:
    def __init__(self, *, aggregation_method: builtins.str) -> None:
        '''
        :param aggregation_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#aggregation_method SentinelAlertRuleScheduled#aggregation_method}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEventGrouping.__init__)
            check_type(argname="argument aggregation_method", value=aggregation_method, expected_type=type_hints["aggregation_method"])
        self._values: typing.Dict[str, typing.Any] = {
            "aggregation_method": aggregation_method,
        }

    @builtins.property
    def aggregation_method(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#aggregation_method SentinelAlertRuleScheduled#aggregation_method}.'''
        result = self._values.get("aggregation_method")
        assert result is not None, "Required property 'aggregation_method' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledEventGrouping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SentinelAlertRuleScheduledEventGroupingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledEventGroupingOutputReference",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledEventGroupingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="aggregationMethodInput")
    def aggregation_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationMethod")
    def aggregation_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregationMethod"))

    @aggregation_method.setter
    def aggregation_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEventGroupingOutputReference, "aggregation_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SentinelAlertRuleScheduledEventGrouping]:
        return typing.cast(typing.Optional[SentinelAlertRuleScheduledEventGrouping], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SentinelAlertRuleScheduledEventGrouping],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledEventGroupingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledIncidentConfiguration",
    jsii_struct_bases=[],
    name_mapping={"create_incident": "createIncident", "grouping": "grouping"},
)
class SentinelAlertRuleScheduledIncidentConfiguration:
    def __init__(
        self,
        *,
        create_incident: typing.Union[builtins.bool, cdktf.IResolvable],
        grouping: typing.Union["SentinelAlertRuleScheduledIncidentConfigurationGrouping", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param create_incident: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#create_incident SentinelAlertRuleScheduled#create_incident}.
        :param grouping: grouping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#grouping SentinelAlertRuleScheduled#grouping}
        '''
        if isinstance(grouping, dict):
            grouping = SentinelAlertRuleScheduledIncidentConfigurationGrouping(**grouping)
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledIncidentConfiguration.__init__)
            check_type(argname="argument create_incident", value=create_incident, expected_type=type_hints["create_incident"])
            check_type(argname="argument grouping", value=grouping, expected_type=type_hints["grouping"])
        self._values: typing.Dict[str, typing.Any] = {
            "create_incident": create_incident,
            "grouping": grouping,
        }

    @builtins.property
    def create_incident(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#create_incident SentinelAlertRuleScheduled#create_incident}.'''
        result = self._values.get("create_incident")
        assert result is not None, "Required property 'create_incident' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def grouping(self) -> "SentinelAlertRuleScheduledIncidentConfigurationGrouping":
        '''grouping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#grouping SentinelAlertRuleScheduled#grouping}
        '''
        result = self._values.get("grouping")
        assert result is not None, "Required property 'grouping' is missing"
        return typing.cast("SentinelAlertRuleScheduledIncidentConfigurationGrouping", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledIncidentConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledIncidentConfigurationGrouping",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "entity_matching_method": "entityMatchingMethod",
        "group_by_alert_details": "groupByAlertDetails",
        "group_by_custom_details": "groupByCustomDetails",
        "group_by_entities": "groupByEntities",
        "lookback_duration": "lookbackDuration",
        "reopen_closed_incidents": "reopenClosedIncidents",
    },
)
class SentinelAlertRuleScheduledIncidentConfigurationGrouping:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        entity_matching_method: typing.Optional[builtins.str] = None,
        group_by_alert_details: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by_custom_details: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by_entities: typing.Optional[typing.Sequence[builtins.str]] = None,
        lookback_duration: typing.Optional[builtins.str] = None,
        reopen_closed_incidents: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#enabled SentinelAlertRuleScheduled#enabled}.
        :param entity_matching_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_matching_method SentinelAlertRuleScheduled#entity_matching_method}.
        :param group_by_alert_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_alert_details SentinelAlertRuleScheduled#group_by_alert_details}.
        :param group_by_custom_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_custom_details SentinelAlertRuleScheduled#group_by_custom_details}.
        :param group_by_entities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_entities SentinelAlertRuleScheduled#group_by_entities}.
        :param lookback_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#lookback_duration SentinelAlertRuleScheduled#lookback_duration}.
        :param reopen_closed_incidents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#reopen_closed_incidents SentinelAlertRuleScheduled#reopen_closed_incidents}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledIncidentConfigurationGrouping.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument entity_matching_method", value=entity_matching_method, expected_type=type_hints["entity_matching_method"])
            check_type(argname="argument group_by_alert_details", value=group_by_alert_details, expected_type=type_hints["group_by_alert_details"])
            check_type(argname="argument group_by_custom_details", value=group_by_custom_details, expected_type=type_hints["group_by_custom_details"])
            check_type(argname="argument group_by_entities", value=group_by_entities, expected_type=type_hints["group_by_entities"])
            check_type(argname="argument lookback_duration", value=lookback_duration, expected_type=type_hints["lookback_duration"])
            check_type(argname="argument reopen_closed_incidents", value=reopen_closed_incidents, expected_type=type_hints["reopen_closed_incidents"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if entity_matching_method is not None:
            self._values["entity_matching_method"] = entity_matching_method
        if group_by_alert_details is not None:
            self._values["group_by_alert_details"] = group_by_alert_details
        if group_by_custom_details is not None:
            self._values["group_by_custom_details"] = group_by_custom_details
        if group_by_entities is not None:
            self._values["group_by_entities"] = group_by_entities
        if lookback_duration is not None:
            self._values["lookback_duration"] = lookback_duration
        if reopen_closed_incidents is not None:
            self._values["reopen_closed_incidents"] = reopen_closed_incidents

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#enabled SentinelAlertRuleScheduled#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def entity_matching_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_matching_method SentinelAlertRuleScheduled#entity_matching_method}.'''
        result = self._values.get("entity_matching_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_alert_details(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_alert_details SentinelAlertRuleScheduled#group_by_alert_details}.'''
        result = self._values.get("group_by_alert_details")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def group_by_custom_details(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_custom_details SentinelAlertRuleScheduled#group_by_custom_details}.'''
        result = self._values.get("group_by_custom_details")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def group_by_entities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_entities SentinelAlertRuleScheduled#group_by_entities}.'''
        result = self._values.get("group_by_entities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def lookback_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#lookback_duration SentinelAlertRuleScheduled#lookback_duration}.'''
        result = self._values.get("lookback_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reopen_closed_incidents(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#reopen_closed_incidents SentinelAlertRuleScheduled#reopen_closed_incidents}.'''
        result = self._values.get("reopen_closed_incidents")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledIncidentConfigurationGrouping(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEntityMatchingMethod")
    def reset_entity_matching_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntityMatchingMethod", []))

    @jsii.member(jsii_name="resetGroupByAlertDetails")
    def reset_group_by_alert_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByAlertDetails", []))

    @jsii.member(jsii_name="resetGroupByCustomDetails")
    def reset_group_by_custom_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByCustomDetails", []))

    @jsii.member(jsii_name="resetGroupByEntities")
    def reset_group_by_entities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByEntities", []))

    @jsii.member(jsii_name="resetLookbackDuration")
    def reset_lookback_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLookbackDuration", []))

    @jsii.member(jsii_name="resetReopenClosedIncidents")
    def reset_reopen_closed_incidents(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReopenClosedIncidents", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="entityMatchingMethodInput")
    def entity_matching_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityMatchingMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByAlertDetailsInput")
    def group_by_alert_details_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByAlertDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByCustomDetailsInput")
    def group_by_custom_details_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByCustomDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByEntitiesInput")
    def group_by_entities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByEntitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="lookbackDurationInput")
    def lookback_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lookbackDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="reopenClosedIncidentsInput")
    def reopen_closed_incidents_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reopenClosedIncidentsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="entityMatchingMethod")
    def entity_matching_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entityMatchingMethod"))

    @entity_matching_method.setter
    def entity_matching_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "entity_matching_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityMatchingMethod", value)

    @builtins.property
    @jsii.member(jsii_name="groupByAlertDetails")
    def group_by_alert_details(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByAlertDetails"))

    @group_by_alert_details.setter
    def group_by_alert_details(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "group_by_alert_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByAlertDetails", value)

    @builtins.property
    @jsii.member(jsii_name="groupByCustomDetails")
    def group_by_custom_details(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByCustomDetails"))

    @group_by_custom_details.setter
    def group_by_custom_details(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "group_by_custom_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByCustomDetails", value)

    @builtins.property
    @jsii.member(jsii_name="groupByEntities")
    def group_by_entities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByEntities"))

    @group_by_entities.setter
    def group_by_entities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "group_by_entities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByEntities", value)

    @builtins.property
    @jsii.member(jsii_name="lookbackDuration")
    def lookback_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lookbackDuration"))

    @lookback_duration.setter
    def lookback_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "lookback_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lookbackDuration", value)

    @builtins.property
    @jsii.member(jsii_name="reopenClosedIncidents")
    def reopen_closed_incidents(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reopenClosedIncidents"))

    @reopen_closed_incidents.setter
    def reopen_closed_incidents(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "reopen_closed_incidents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reopenClosedIncidents", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SentinelAlertRuleScheduledIncidentConfigurationGrouping]:
        return typing.cast(typing.Optional[SentinelAlertRuleScheduledIncidentConfigurationGrouping], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SentinelAlertRuleScheduledIncidentConfigurationGrouping],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SentinelAlertRuleScheduledIncidentConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledIncidentConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledIncidentConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putGrouping")
    def put_grouping(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        entity_matching_method: typing.Optional[builtins.str] = None,
        group_by_alert_details: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by_custom_details: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by_entities: typing.Optional[typing.Sequence[builtins.str]] = None,
        lookback_duration: typing.Optional[builtins.str] = None,
        reopen_closed_incidents: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#enabled SentinelAlertRuleScheduled#enabled}.
        :param entity_matching_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#entity_matching_method SentinelAlertRuleScheduled#entity_matching_method}.
        :param group_by_alert_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_alert_details SentinelAlertRuleScheduled#group_by_alert_details}.
        :param group_by_custom_details: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_custom_details SentinelAlertRuleScheduled#group_by_custom_details}.
        :param group_by_entities: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#group_by_entities SentinelAlertRuleScheduled#group_by_entities}.
        :param lookback_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#lookback_duration SentinelAlertRuleScheduled#lookback_duration}.
        :param reopen_closed_incidents: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#reopen_closed_incidents SentinelAlertRuleScheduled#reopen_closed_incidents}.
        '''
        value = SentinelAlertRuleScheduledIncidentConfigurationGrouping(
            enabled=enabled,
            entity_matching_method=entity_matching_method,
            group_by_alert_details=group_by_alert_details,
            group_by_custom_details=group_by_custom_details,
            group_by_entities=group_by_entities,
            lookback_duration=lookback_duration,
            reopen_closed_incidents=reopen_closed_incidents,
        )

        return typing.cast(None, jsii.invoke(self, "putGrouping", [value]))

    @builtins.property
    @jsii.member(jsii_name="grouping")
    def grouping(
        self,
    ) -> SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference:
        return typing.cast(SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference, jsii.get(self, "grouping"))

    @builtins.property
    @jsii.member(jsii_name="createIncidentInput")
    def create_incident_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createIncidentInput"))

    @builtins.property
    @jsii.member(jsii_name="groupingInput")
    def grouping_input(
        self,
    ) -> typing.Optional[SentinelAlertRuleScheduledIncidentConfigurationGrouping]:
        return typing.cast(typing.Optional[SentinelAlertRuleScheduledIncidentConfigurationGrouping], jsii.get(self, "groupingInput"))

    @builtins.property
    @jsii.member(jsii_name="createIncident")
    def create_incident(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createIncident"))

    @create_incident.setter
    def create_incident(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationOutputReference, "create_incident").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createIncident", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SentinelAlertRuleScheduledIncidentConfiguration]:
        return typing.cast(typing.Optional[SentinelAlertRuleScheduledIncidentConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SentinelAlertRuleScheduledIncidentConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledIncidentConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class SentinelAlertRuleScheduledTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#create SentinelAlertRuleScheduled#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#delete SentinelAlertRuleScheduled#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#read SentinelAlertRuleScheduled#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#update SentinelAlertRuleScheduled#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#create SentinelAlertRuleScheduled#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#delete SentinelAlertRuleScheduled#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#read SentinelAlertRuleScheduled#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/sentinel_alert_rule_scheduled#update SentinelAlertRuleScheduled#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SentinelAlertRuleScheduledTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SentinelAlertRuleScheduledTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.sentinelAlertRuleScheduled.SentinelAlertRuleScheduledTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(SentinelAlertRuleScheduledTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SentinelAlertRuleScheduledTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SentinelAlertRuleScheduledTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SentinelAlertRuleScheduledTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SentinelAlertRuleScheduledTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SentinelAlertRuleScheduled",
    "SentinelAlertRuleScheduledAlertDetailsOverride",
    "SentinelAlertRuleScheduledAlertDetailsOverrideList",
    "SentinelAlertRuleScheduledAlertDetailsOverrideOutputReference",
    "SentinelAlertRuleScheduledConfig",
    "SentinelAlertRuleScheduledEntityMapping",
    "SentinelAlertRuleScheduledEntityMappingFieldMapping",
    "SentinelAlertRuleScheduledEntityMappingFieldMappingList",
    "SentinelAlertRuleScheduledEntityMappingFieldMappingOutputReference",
    "SentinelAlertRuleScheduledEntityMappingList",
    "SentinelAlertRuleScheduledEntityMappingOutputReference",
    "SentinelAlertRuleScheduledEventGrouping",
    "SentinelAlertRuleScheduledEventGroupingOutputReference",
    "SentinelAlertRuleScheduledIncidentConfiguration",
    "SentinelAlertRuleScheduledIncidentConfigurationGrouping",
    "SentinelAlertRuleScheduledIncidentConfigurationGroupingOutputReference",
    "SentinelAlertRuleScheduledIncidentConfigurationOutputReference",
    "SentinelAlertRuleScheduledTimeouts",
    "SentinelAlertRuleScheduledTimeoutsOutputReference",
]

publication.publish()
