'''
# `azurerm_monitor_alert_processing_rule_suppression`

Refer to the Terraform Registory for docs: [`azurerm_monitor_alert_processing_rule_suppression`](https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression).
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


class MonitorAlertProcessingRuleSuppression(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppression",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression azurerm_monitor_alert_processing_rule_suppression}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        resource_group_name: builtins.str,
        scopes: typing.Sequence[builtins.str],
        condition: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionCondition", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionSchedule", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression azurerm_monitor_alert_processing_rule_suppression} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#name MonitorAlertProcessingRuleSuppression#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#resource_group_name MonitorAlertProcessingRuleSuppression#resource_group_name}.
        :param scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#scopes MonitorAlertProcessingRuleSuppression#scopes}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#condition MonitorAlertProcessingRuleSuppression#condition}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#description MonitorAlertProcessingRuleSuppression#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#enabled MonitorAlertProcessingRuleSuppression#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#id MonitorAlertProcessingRuleSuppression#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#schedule MonitorAlertProcessingRuleSuppression#schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#tags MonitorAlertProcessingRuleSuppression#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#timeouts MonitorAlertProcessingRuleSuppression#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppression.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorAlertProcessingRuleSuppressionConfig(
            name=name,
            resource_group_name=resource_group_name,
            scopes=scopes,
            condition=condition,
            description=description,
            enabled=enabled,
            id=id,
            schedule=schedule,
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

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        alert_context: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionAlertContext", typing.Dict[str, typing.Any]]] = None,
        alert_rule_id: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionAlertRuleId", typing.Dict[str, typing.Any]]] = None,
        alert_rule_name: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionAlertRuleName", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionDescription", typing.Dict[str, typing.Any]]] = None,
        monitor_condition: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionMonitorCondition", typing.Dict[str, typing.Any]]] = None,
        monitor_service: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionMonitorService", typing.Dict[str, typing.Any]]] = None,
        severity: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionSeverity", typing.Dict[str, typing.Any]]] = None,
        signal_type: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionSignalType", typing.Dict[str, typing.Any]]] = None,
        target_resource: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionTargetResource", typing.Dict[str, typing.Any]]] = None,
        target_resource_group: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup", typing.Dict[str, typing.Any]]] = None,
        target_resource_type: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionTargetResourceType", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param alert_context: alert_context block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_context MonitorAlertProcessingRuleSuppression#alert_context}
        :param alert_rule_id: alert_rule_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_rule_id MonitorAlertProcessingRuleSuppression#alert_rule_id}
        :param alert_rule_name: alert_rule_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_rule_name MonitorAlertProcessingRuleSuppression#alert_rule_name}
        :param description: description block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#description MonitorAlertProcessingRuleSuppression#description}
        :param monitor_condition: monitor_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monitor_condition MonitorAlertProcessingRuleSuppression#monitor_condition}
        :param monitor_service: monitor_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monitor_service MonitorAlertProcessingRuleSuppression#monitor_service}
        :param severity: severity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#severity MonitorAlertProcessingRuleSuppression#severity}
        :param signal_type: signal_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#signal_type MonitorAlertProcessingRuleSuppression#signal_type}
        :param target_resource: target_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource MonitorAlertProcessingRuleSuppression#target_resource}
        :param target_resource_group: target_resource_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource_group MonitorAlertProcessingRuleSuppression#target_resource_group}
        :param target_resource_type: target_resource_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource_type MonitorAlertProcessingRuleSuppression#target_resource_type}
        '''
        value = MonitorAlertProcessingRuleSuppressionCondition(
            alert_context=alert_context,
            alert_rule_id=alert_rule_id,
            alert_rule_name=alert_rule_name,
            description=description,
            monitor_condition=monitor_condition,
            monitor_service=monitor_service,
            severity=severity,
            signal_type=signal_type,
            target_resource=target_resource,
            target_resource_group=target_resource_group,
            target_resource_type=target_resource_type,
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        effective_from: typing.Optional[builtins.str] = None,
        effective_until: typing.Optional[builtins.str] = None,
        recurrence: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrence", typing.Dict[str, typing.Any]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param effective_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#effective_from MonitorAlertProcessingRuleSuppression#effective_from}.
        :param effective_until: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#effective_until MonitorAlertProcessingRuleSuppression#effective_until}.
        :param recurrence: recurrence block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#recurrence MonitorAlertProcessingRuleSuppression#recurrence}
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#time_zone MonitorAlertProcessingRuleSuppression#time_zone}.
        '''
        value = MonitorAlertProcessingRuleSuppressionSchedule(
            effective_from=effective_from,
            effective_until=effective_until,
            recurrence=recurrence,
            time_zone=time_zone,
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#create MonitorAlertProcessingRuleSuppression#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#delete MonitorAlertProcessingRuleSuppression#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#read MonitorAlertProcessingRuleSuppression#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#update MonitorAlertProcessingRuleSuppression#update}.
        '''
        value = MonitorAlertProcessingRuleSuppressionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

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
    @jsii.member(jsii_name="condition")
    def condition(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionConditionOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionConditionOutputReference", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionScheduleOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionCondition"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionCondition"], jsii.get(self, "conditionInput"))

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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionSchedule"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="scopesInput")
    def scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scopesInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppression, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppression, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppression, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppression, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppression, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scopes"))

    @scopes.setter
    def scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppression, "scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopes", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppression, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionCondition",
    jsii_struct_bases=[],
    name_mapping={
        "alert_context": "alertContext",
        "alert_rule_id": "alertRuleId",
        "alert_rule_name": "alertRuleName",
        "description": "description",
        "monitor_condition": "monitorCondition",
        "monitor_service": "monitorService",
        "severity": "severity",
        "signal_type": "signalType",
        "target_resource": "targetResource",
        "target_resource_group": "targetResourceGroup",
        "target_resource_type": "targetResourceType",
    },
)
class MonitorAlertProcessingRuleSuppressionCondition:
    def __init__(
        self,
        *,
        alert_context: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionAlertContext", typing.Dict[str, typing.Any]]] = None,
        alert_rule_id: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionAlertRuleId", typing.Dict[str, typing.Any]]] = None,
        alert_rule_name: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionAlertRuleName", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionDescription", typing.Dict[str, typing.Any]]] = None,
        monitor_condition: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionMonitorCondition", typing.Dict[str, typing.Any]]] = None,
        monitor_service: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionMonitorService", typing.Dict[str, typing.Any]]] = None,
        severity: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionSeverity", typing.Dict[str, typing.Any]]] = None,
        signal_type: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionSignalType", typing.Dict[str, typing.Any]]] = None,
        target_resource: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionTargetResource", typing.Dict[str, typing.Any]]] = None,
        target_resource_group: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup", typing.Dict[str, typing.Any]]] = None,
        target_resource_type: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionConditionTargetResourceType", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param alert_context: alert_context block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_context MonitorAlertProcessingRuleSuppression#alert_context}
        :param alert_rule_id: alert_rule_id block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_rule_id MonitorAlertProcessingRuleSuppression#alert_rule_id}
        :param alert_rule_name: alert_rule_name block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_rule_name MonitorAlertProcessingRuleSuppression#alert_rule_name}
        :param description: description block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#description MonitorAlertProcessingRuleSuppression#description}
        :param monitor_condition: monitor_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monitor_condition MonitorAlertProcessingRuleSuppression#monitor_condition}
        :param monitor_service: monitor_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monitor_service MonitorAlertProcessingRuleSuppression#monitor_service}
        :param severity: severity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#severity MonitorAlertProcessingRuleSuppression#severity}
        :param signal_type: signal_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#signal_type MonitorAlertProcessingRuleSuppression#signal_type}
        :param target_resource: target_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource MonitorAlertProcessingRuleSuppression#target_resource}
        :param target_resource_group: target_resource_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource_group MonitorAlertProcessingRuleSuppression#target_resource_group}
        :param target_resource_type: target_resource_type block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource_type MonitorAlertProcessingRuleSuppression#target_resource_type}
        '''
        if isinstance(alert_context, dict):
            alert_context = MonitorAlertProcessingRuleSuppressionConditionAlertContext(**alert_context)
        if isinstance(alert_rule_id, dict):
            alert_rule_id = MonitorAlertProcessingRuleSuppressionConditionAlertRuleId(**alert_rule_id)
        if isinstance(alert_rule_name, dict):
            alert_rule_name = MonitorAlertProcessingRuleSuppressionConditionAlertRuleName(**alert_rule_name)
        if isinstance(description, dict):
            description = MonitorAlertProcessingRuleSuppressionConditionDescription(**description)
        if isinstance(monitor_condition, dict):
            monitor_condition = MonitorAlertProcessingRuleSuppressionConditionMonitorCondition(**monitor_condition)
        if isinstance(monitor_service, dict):
            monitor_service = MonitorAlertProcessingRuleSuppressionConditionMonitorService(**monitor_service)
        if isinstance(severity, dict):
            severity = MonitorAlertProcessingRuleSuppressionConditionSeverity(**severity)
        if isinstance(signal_type, dict):
            signal_type = MonitorAlertProcessingRuleSuppressionConditionSignalType(**signal_type)
        if isinstance(target_resource, dict):
            target_resource = MonitorAlertProcessingRuleSuppressionConditionTargetResource(**target_resource)
        if isinstance(target_resource_group, dict):
            target_resource_group = MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup(**target_resource_group)
        if isinstance(target_resource_type, dict):
            target_resource_type = MonitorAlertProcessingRuleSuppressionConditionTargetResourceType(**target_resource_type)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionCondition.__init__)
            check_type(argname="argument alert_context", value=alert_context, expected_type=type_hints["alert_context"])
            check_type(argname="argument alert_rule_id", value=alert_rule_id, expected_type=type_hints["alert_rule_id"])
            check_type(argname="argument alert_rule_name", value=alert_rule_name, expected_type=type_hints["alert_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument monitor_condition", value=monitor_condition, expected_type=type_hints["monitor_condition"])
            check_type(argname="argument monitor_service", value=monitor_service, expected_type=type_hints["monitor_service"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument signal_type", value=signal_type, expected_type=type_hints["signal_type"])
            check_type(argname="argument target_resource", value=target_resource, expected_type=type_hints["target_resource"])
            check_type(argname="argument target_resource_group", value=target_resource_group, expected_type=type_hints["target_resource_group"])
            check_type(argname="argument target_resource_type", value=target_resource_type, expected_type=type_hints["target_resource_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alert_context is not None:
            self._values["alert_context"] = alert_context
        if alert_rule_id is not None:
            self._values["alert_rule_id"] = alert_rule_id
        if alert_rule_name is not None:
            self._values["alert_rule_name"] = alert_rule_name
        if description is not None:
            self._values["description"] = description
        if monitor_condition is not None:
            self._values["monitor_condition"] = monitor_condition
        if monitor_service is not None:
            self._values["monitor_service"] = monitor_service
        if severity is not None:
            self._values["severity"] = severity
        if signal_type is not None:
            self._values["signal_type"] = signal_type
        if target_resource is not None:
            self._values["target_resource"] = target_resource
        if target_resource_group is not None:
            self._values["target_resource_group"] = target_resource_group
        if target_resource_type is not None:
            self._values["target_resource_type"] = target_resource_type

    @builtins.property
    def alert_context(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionAlertContext"]:
        '''alert_context block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_context MonitorAlertProcessingRuleSuppression#alert_context}
        '''
        result = self._values.get("alert_context")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionAlertContext"], result)

    @builtins.property
    def alert_rule_id(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionAlertRuleId"]:
        '''alert_rule_id block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_rule_id MonitorAlertProcessingRuleSuppression#alert_rule_id}
        '''
        result = self._values.get("alert_rule_id")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionAlertRuleId"], result)

    @builtins.property
    def alert_rule_name(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionAlertRuleName"]:
        '''alert_rule_name block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#alert_rule_name MonitorAlertProcessingRuleSuppression#alert_rule_name}
        '''
        result = self._values.get("alert_rule_name")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionAlertRuleName"], result)

    @builtins.property
    def description(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionDescription"]:
        '''description block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#description MonitorAlertProcessingRuleSuppression#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionDescription"], result)

    @builtins.property
    def monitor_condition(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionMonitorCondition"]:
        '''monitor_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monitor_condition MonitorAlertProcessingRuleSuppression#monitor_condition}
        '''
        result = self._values.get("monitor_condition")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionMonitorCondition"], result)

    @builtins.property
    def monitor_service(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionMonitorService"]:
        '''monitor_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monitor_service MonitorAlertProcessingRuleSuppression#monitor_service}
        '''
        result = self._values.get("monitor_service")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionMonitorService"], result)

    @builtins.property
    def severity(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSeverity"]:
        '''severity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#severity MonitorAlertProcessingRuleSuppression#severity}
        '''
        result = self._values.get("severity")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSeverity"], result)

    @builtins.property
    def signal_type(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSignalType"]:
        '''signal_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#signal_type MonitorAlertProcessingRuleSuppression#signal_type}
        '''
        result = self._values.get("signal_type")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSignalType"], result)

    @builtins.property
    def target_resource(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResource"]:
        '''target_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource MonitorAlertProcessingRuleSuppression#target_resource}
        '''
        result = self._values.get("target_resource")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResource"], result)

    @builtins.property
    def target_resource_group(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup"]:
        '''target_resource_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource_group MonitorAlertProcessingRuleSuppression#target_resource_group}
        '''
        result = self._values.get("target_resource_group")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup"], result)

    @builtins.property
    def target_resource_type(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceType"]:
        '''target_resource_type block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#target_resource_type MonitorAlertProcessingRuleSuppression#target_resource_type}
        '''
        result = self._values.get("target_resource_type")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionAlertContext",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionAlertContext:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionAlertContext.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionAlertContext(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertContext]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertContext], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertContext],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionAlertRuleId",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionAlertRuleId:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionAlertRuleId.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionAlertRuleId(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleId]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleId], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleId],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionAlertRuleName",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionAlertRuleName:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionAlertRuleName.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionAlertRuleName(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleName]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleName], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleName],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionDescription",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionDescription:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionDescription.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionDescription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionDescription]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionDescription], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionDescription],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionMonitorCondition",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionMonitorCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionMonitorCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionMonitorCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorCondition]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionMonitorService",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionMonitorService:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionMonitorService.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionMonitorService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorService]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorService],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertProcessingRuleSuppressionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAlertContext")
    def put_alert_context(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionAlertContext(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putAlertContext", [value]))

    @jsii.member(jsii_name="putAlertRuleId")
    def put_alert_rule_id(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionAlertRuleId(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putAlertRuleId", [value]))

    @jsii.member(jsii_name="putAlertRuleName")
    def put_alert_rule_name(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionAlertRuleName(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putAlertRuleName", [value]))

    @jsii.member(jsii_name="putDescription")
    def put_description(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionDescription(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putDescription", [value]))

    @jsii.member(jsii_name="putMonitorCondition")
    def put_monitor_condition(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionMonitorCondition(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putMonitorCondition", [value]))

    @jsii.member(jsii_name="putMonitorService")
    def put_monitor_service(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionMonitorService(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putMonitorService", [value]))

    @jsii.member(jsii_name="putSeverity")
    def put_severity(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionSeverity(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSeverity", [value]))

    @jsii.member(jsii_name="putSignalType")
    def put_signal_type(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionSignalType(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putSignalType", [value]))

    @jsii.member(jsii_name="putTargetResource")
    def put_target_resource(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionTargetResource(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTargetResource", [value]))

    @jsii.member(jsii_name="putTargetResourceGroup")
    def put_target_resource_group(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTargetResourceGroup", [value]))

    @jsii.member(jsii_name="putTargetResourceType")
    def put_target_resource_type(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        value = MonitorAlertProcessingRuleSuppressionConditionTargetResourceType(
            operator=operator, values=values
        )

        return typing.cast(None, jsii.invoke(self, "putTargetResourceType", [value]))

    @jsii.member(jsii_name="resetAlertContext")
    def reset_alert_context(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertContext", []))

    @jsii.member(jsii_name="resetAlertRuleId")
    def reset_alert_rule_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertRuleId", []))

    @jsii.member(jsii_name="resetAlertRuleName")
    def reset_alert_rule_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertRuleName", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetMonitorCondition")
    def reset_monitor_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorCondition", []))

    @jsii.member(jsii_name="resetMonitorService")
    def reset_monitor_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitorService", []))

    @jsii.member(jsii_name="resetSeverity")
    def reset_severity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverity", []))

    @jsii.member(jsii_name="resetSignalType")
    def reset_signal_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignalType", []))

    @jsii.member(jsii_name="resetTargetResource")
    def reset_target_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResource", []))

    @jsii.member(jsii_name="resetTargetResourceGroup")
    def reset_target_resource_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResourceGroup", []))

    @jsii.member(jsii_name="resetTargetResourceType")
    def reset_target_resource_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetResourceType", []))

    @builtins.property
    @jsii.member(jsii_name="alertContext")
    def alert_context(
        self,
    ) -> MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference:
        return typing.cast(MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference, jsii.get(self, "alertContext"))

    @builtins.property
    @jsii.member(jsii_name="alertRuleId")
    def alert_rule_id(
        self,
    ) -> MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference:
        return typing.cast(MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference, jsii.get(self, "alertRuleId"))

    @builtins.property
    @jsii.member(jsii_name="alertRuleName")
    def alert_rule_name(
        self,
    ) -> MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference:
        return typing.cast(MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference, jsii.get(self, "alertRuleName"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(
        self,
    ) -> MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference:
        return typing.cast(MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="monitorCondition")
    def monitor_condition(
        self,
    ) -> MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference:
        return typing.cast(MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference, jsii.get(self, "monitorCondition"))

    @builtins.property
    @jsii.member(jsii_name="monitorService")
    def monitor_service(
        self,
    ) -> MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference:
        return typing.cast(MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference, jsii.get(self, "monitorService"))

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference", jsii.get(self, "severity"))

    @builtins.property
    @jsii.member(jsii_name="signalType")
    def signal_type(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference", jsii.get(self, "signalType"))

    @builtins.property
    @jsii.member(jsii_name="targetResource")
    def target_resource(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference", jsii.get(self, "targetResource"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceGroup")
    def target_resource_group(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference", jsii.get(self, "targetResourceGroup"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceType")
    def target_resource_type(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference", jsii.get(self, "targetResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alertContextInput")
    def alert_context_input(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertContext]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertContext], jsii.get(self, "alertContextInput"))

    @builtins.property
    @jsii.member(jsii_name="alertRuleIdInput")
    def alert_rule_id_input(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleId]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleId], jsii.get(self, "alertRuleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="alertRuleNameInput")
    def alert_rule_name_input(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleName]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionAlertRuleName], jsii.get(self, "alertRuleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionDescription]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionDescription], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorConditionInput")
    def monitor_condition_input(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorCondition]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorCondition], jsii.get(self, "monitorConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="monitorServiceInput")
    def monitor_service_input(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorService]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionMonitorService], jsii.get(self, "monitorServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSeverity"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSeverity"], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="signalTypeInput")
    def signal_type_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSignalType"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionSignalType"], jsii.get(self, "signalTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceGroupInput")
    def target_resource_group_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup"], jsii.get(self, "targetResourceGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceInput")
    def target_resource_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResource"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResource"], jsii.get(self, "targetResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetResourceTypeInput")
    def target_resource_type_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceType"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionConditionTargetResourceType"], jsii.get(self, "targetResourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionCondition]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionSeverity",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionSeverity:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionSeverity.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionSeverity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionSeverity]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionSeverity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionSeverity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionSignalType",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionSignalType:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionSignalType.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionSignalType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionSignalType]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionSignalType], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionSignalType],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionTargetResource",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionTargetResource:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionTargetResource.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionTargetResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResource]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionTargetResourceType",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "values": "values"},
)
class MonitorAlertProcessingRuleSuppressionConditionTargetResourceType:
    def __init__(
        self,
        *,
        operator: builtins.str,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.
        :param values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionTargetResourceType.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "values": values,
        }

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#operator MonitorAlertProcessingRuleSuppression#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#values MonitorAlertProcessingRuleSuppression#values}.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConditionTargetResourceType(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResourceType]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResourceType], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionConditionTargetResourceType],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionConfig",
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
        "resource_group_name": "resourceGroupName",
        "scopes": "scopes",
        "condition": "condition",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "schedule": "schedule",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class MonitorAlertProcessingRuleSuppressionConfig(cdktf.TerraformMetaArguments):
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
        resource_group_name: builtins.str,
        scopes: typing.Sequence[builtins.str],
        condition: typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionCondition, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionSchedule", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#name MonitorAlertProcessingRuleSuppression#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#resource_group_name MonitorAlertProcessingRuleSuppression#resource_group_name}.
        :param scopes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#scopes MonitorAlertProcessingRuleSuppression#scopes}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#condition MonitorAlertProcessingRuleSuppression#condition}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#description MonitorAlertProcessingRuleSuppression#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#enabled MonitorAlertProcessingRuleSuppression#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#id MonitorAlertProcessingRuleSuppression#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#schedule MonitorAlertProcessingRuleSuppression#schedule}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#tags MonitorAlertProcessingRuleSuppression#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#timeouts MonitorAlertProcessingRuleSuppression#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(condition, dict):
            condition = MonitorAlertProcessingRuleSuppressionCondition(**condition)
        if isinstance(schedule, dict):
            schedule = MonitorAlertProcessingRuleSuppressionSchedule(**schedule)
        if isinstance(timeouts, dict):
            timeouts = MonitorAlertProcessingRuleSuppressionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "resource_group_name": resource_group_name,
            "scopes": scopes,
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
        if condition is not None:
            self._values["condition"] = condition
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if schedule is not None:
            self._values["schedule"] = schedule
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#name MonitorAlertProcessingRuleSuppression#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#resource_group_name MonitorAlertProcessingRuleSuppression#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scopes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#scopes MonitorAlertProcessingRuleSuppression#scopes}.'''
        result = self._values.get("scopes")
        assert result is not None, "Required property 'scopes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionCondition]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#condition MonitorAlertProcessingRuleSuppression#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionCondition], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#description MonitorAlertProcessingRuleSuppression#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#enabled MonitorAlertProcessingRuleSuppression#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#id MonitorAlertProcessingRuleSuppression#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionSchedule"]:
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#schedule MonitorAlertProcessingRuleSuppression#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionSchedule"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#tags MonitorAlertProcessingRuleSuppression#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#timeouts MonitorAlertProcessingRuleSuppression#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "effective_from": "effectiveFrom",
        "effective_until": "effectiveUntil",
        "recurrence": "recurrence",
        "time_zone": "timeZone",
    },
)
class MonitorAlertProcessingRuleSuppressionSchedule:
    def __init__(
        self,
        *,
        effective_from: typing.Optional[builtins.str] = None,
        effective_until: typing.Optional[builtins.str] = None,
        recurrence: typing.Optional[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrence", typing.Dict[str, typing.Any]]] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param effective_from: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#effective_from MonitorAlertProcessingRuleSuppression#effective_from}.
        :param effective_until: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#effective_until MonitorAlertProcessingRuleSuppression#effective_until}.
        :param recurrence: recurrence block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#recurrence MonitorAlertProcessingRuleSuppression#recurrence}
        :param time_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#time_zone MonitorAlertProcessingRuleSuppression#time_zone}.
        '''
        if isinstance(recurrence, dict):
            recurrence = MonitorAlertProcessingRuleSuppressionScheduleRecurrence(**recurrence)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionSchedule.__init__)
            check_type(argname="argument effective_from", value=effective_from, expected_type=type_hints["effective_from"])
            check_type(argname="argument effective_until", value=effective_until, expected_type=type_hints["effective_until"])
            check_type(argname="argument recurrence", value=recurrence, expected_type=type_hints["recurrence"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[str, typing.Any] = {}
        if effective_from is not None:
            self._values["effective_from"] = effective_from
        if effective_until is not None:
            self._values["effective_until"] = effective_until
        if recurrence is not None:
            self._values["recurrence"] = recurrence
        if time_zone is not None:
            self._values["time_zone"] = time_zone

    @builtins.property
    def effective_from(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#effective_from MonitorAlertProcessingRuleSuppression#effective_from}.'''
        result = self._values.get("effective_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def effective_until(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#effective_until MonitorAlertProcessingRuleSuppression#effective_until}.'''
        result = self._values.get("effective_until")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recurrence(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionScheduleRecurrence"]:
        '''recurrence block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#recurrence MonitorAlertProcessingRuleSuppression#recurrence}
        '''
        result = self._values.get("recurrence")
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionScheduleRecurrence"], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#time_zone MonitorAlertProcessingRuleSuppression#time_zone}.'''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionScheduleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRecurrence")
    def put_recurrence(
        self,
        *,
        daily: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily", typing.Dict[str, typing.Any]]]]] = None,
        monthly: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly", typing.Dict[str, typing.Any]]]]] = None,
        weekly: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param daily: daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#daily MonitorAlertProcessingRuleSuppression#daily}
        :param monthly: monthly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monthly MonitorAlertProcessingRuleSuppression#monthly}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#weekly MonitorAlertProcessingRuleSuppression#weekly}
        '''
        value = MonitorAlertProcessingRuleSuppressionScheduleRecurrence(
            daily=daily, monthly=monthly, weekly=weekly
        )

        return typing.cast(None, jsii.invoke(self, "putRecurrence", [value]))

    @jsii.member(jsii_name="resetEffectiveFrom")
    def reset_effective_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffectiveFrom", []))

    @jsii.member(jsii_name="resetEffectiveUntil")
    def reset_effective_until(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffectiveUntil", []))

    @jsii.member(jsii_name="resetRecurrence")
    def reset_recurrence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecurrence", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @builtins.property
    @jsii.member(jsii_name="recurrence")
    def recurrence(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference":
        return typing.cast("MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference", jsii.get(self, "recurrence"))

    @builtins.property
    @jsii.member(jsii_name="effectiveFromInput")
    def effective_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectiveFromInput"))

    @builtins.property
    @jsii.member(jsii_name="effectiveUntilInput")
    def effective_until_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectiveUntilInput"))

    @builtins.property
    @jsii.member(jsii_name="recurrenceInput")
    def recurrence_input(
        self,
    ) -> typing.Optional["MonitorAlertProcessingRuleSuppressionScheduleRecurrence"]:
        return typing.cast(typing.Optional["MonitorAlertProcessingRuleSuppressionScheduleRecurrence"], jsii.get(self, "recurrenceInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="effectiveFrom")
    def effective_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effectiveFrom"))

    @effective_from.setter
    def effective_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleOutputReference, "effective_from").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effectiveFrom", value)

    @builtins.property
    @jsii.member(jsii_name="effectiveUntil")
    def effective_until(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effectiveUntil"))

    @effective_until.setter
    def effective_until(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleOutputReference, "effective_until").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effectiveUntil", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleOutputReference, "time_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionSchedule]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionSchedule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrence",
    jsii_struct_bases=[],
    name_mapping={"daily": "daily", "monthly": "monthly", "weekly": "weekly"},
)
class MonitorAlertProcessingRuleSuppressionScheduleRecurrence:
    def __init__(
        self,
        *,
        daily: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily", typing.Dict[str, typing.Any]]]]] = None,
        monthly: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly", typing.Dict[str, typing.Any]]]]] = None,
        weekly: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param daily: daily block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#daily MonitorAlertProcessingRuleSuppression#daily}
        :param monthly: monthly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monthly MonitorAlertProcessingRuleSuppression#monthly}
        :param weekly: weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#weekly MonitorAlertProcessingRuleSuppression#weekly}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrence.__init__)
            check_type(argname="argument daily", value=daily, expected_type=type_hints["daily"])
            check_type(argname="argument monthly", value=monthly, expected_type=type_hints["monthly"])
            check_type(argname="argument weekly", value=weekly, expected_type=type_hints["weekly"])
        self._values: typing.Dict[str, typing.Any] = {}
        if daily is not None:
            self._values["daily"] = daily
        if monthly is not None:
            self._values["monthly"] = monthly
        if weekly is not None:
            self._values["weekly"] = weekly

    @builtins.property
    def daily(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily"]]]:
        '''daily block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#daily MonitorAlertProcessingRuleSuppression#daily}
        '''
        result = self._values.get("daily")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily"]]], result)

    @builtins.property
    def monthly(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly"]]]:
        '''monthly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#monthly MonitorAlertProcessingRuleSuppression#monthly}
        '''
        result = self._values.get("monthly")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly"]]], result)

    @builtins.property
    def weekly(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly"]]]:
        '''weekly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#weekly MonitorAlertProcessingRuleSuppression#weekly}
        '''
        result = self._values.get("weekly")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionScheduleRecurrence(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily",
    jsii_struct_bases=[],
    name_mapping={"end_time": "endTime", "start_time": "startTime"},
)
class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily:
    def __init__(self, *, end_time: builtins.str, start_time: builtins.str) -> None:
        '''
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#end_time MonitorAlertProcessingRuleSuppression#end_time}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#start_time MonitorAlertProcessingRuleSuppression#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily.__init__)
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "end_time": end_time,
            "start_time": start_time,
        }

    @builtins.property
    def end_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#end_time MonitorAlertProcessingRuleSuppression#end_time}.'''
        result = self._values.get("end_time")
        assert result is not None, "Required property 'end_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#start_time MonitorAlertProcessingRuleSuppression#start_time}.'''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly",
    jsii_struct_bases=[],
    name_mapping={
        "days_of_month": "daysOfMonth",
        "end_time": "endTime",
        "start_time": "startTime",
    },
)
class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly:
    def __init__(
        self,
        *,
        days_of_month: typing.Sequence[jsii.Number],
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param days_of_month: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#days_of_month MonitorAlertProcessingRuleSuppression#days_of_month}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#end_time MonitorAlertProcessingRuleSuppression#end_time}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#start_time MonitorAlertProcessingRuleSuppression#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly.__init__)
            check_type(argname="argument days_of_month", value=days_of_month, expected_type=type_hints["days_of_month"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "days_of_month": days_of_month,
        }
        if end_time is not None:
            self._values["end_time"] = end_time
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def days_of_month(self) -> typing.List[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#days_of_month MonitorAlertProcessingRuleSuppression#days_of_month}.'''
        result = self._values.get("days_of_month")
        assert result is not None, "Required property 'days_of_month' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#end_time MonitorAlertProcessingRuleSuppression#end_time}.'''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#start_time MonitorAlertProcessingRuleSuppression#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="daysOfMonthInput")
    def days_of_month_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "daysOfMonthInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="daysOfMonth")
    def days_of_month(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "daysOfMonth"))

    @days_of_month.setter
    def days_of_month(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference, "days_of_month").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysOfMonth", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDaily")
    def put_daily(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference.put_daily)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDaily", [value]))

    @jsii.member(jsii_name="putMonthly")
    def put_monthly(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference.put_monthly)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMonthly", [value]))

    @jsii.member(jsii_name="putWeekly")
    def put_weekly(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference.put_weekly)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWeekly", [value]))

    @jsii.member(jsii_name="resetDaily")
    def reset_daily(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaily", []))

    @jsii.member(jsii_name="resetMonthly")
    def reset_monthly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthly", []))

    @jsii.member(jsii_name="resetWeekly")
    def reset_weekly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekly", []))

    @builtins.property
    @jsii.member(jsii_name="daily")
    def daily(self) -> MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList:
        return typing.cast(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList, jsii.get(self, "daily"))

    @builtins.property
    @jsii.member(jsii_name="monthly")
    def monthly(
        self,
    ) -> MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList:
        return typing.cast(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList, jsii.get(self, "monthly"))

    @builtins.property
    @jsii.member(jsii_name="weekly")
    def weekly(
        self,
    ) -> "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList":
        return typing.cast("MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList", jsii.get(self, "weekly"))

    @builtins.property
    @jsii.member(jsii_name="dailyInput")
    def daily_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily]]], jsii.get(self, "dailyInput"))

    @builtins.property
    @jsii.member(jsii_name="monthlyInput")
    def monthly_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly]]], jsii.get(self, "monthlyInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklyInput")
    def weekly_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly"]]], jsii.get(self, "weeklyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorAlertProcessingRuleSuppressionScheduleRecurrence]:
        return typing.cast(typing.Optional[MonitorAlertProcessingRuleSuppressionScheduleRecurrence], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorAlertProcessingRuleSuppressionScheduleRecurrence],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly",
    jsii_struct_bases=[],
    name_mapping={
        "days_of_week": "daysOfWeek",
        "end_time": "endTime",
        "start_time": "startTime",
    },
)
class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly:
    def __init__(
        self,
        *,
        days_of_week: typing.Sequence[builtins.str],
        end_time: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param days_of_week: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#days_of_week MonitorAlertProcessingRuleSuppression#days_of_week}.
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#end_time MonitorAlertProcessingRuleSuppression#end_time}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#start_time MonitorAlertProcessingRuleSuppression#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly.__init__)
            check_type(argname="argument days_of_week", value=days_of_week, expected_type=type_hints["days_of_week"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {
            "days_of_week": days_of_week,
        }
        if end_time is not None:
            self._values["end_time"] = end_time
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def days_of_week(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#days_of_week MonitorAlertProcessingRuleSuppression#days_of_week}.'''
        result = self._values.get("days_of_week")
        assert result is not None, "Required property 'days_of_week' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#end_time MonitorAlertProcessingRuleSuppression#end_time}.'''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#start_time MonitorAlertProcessingRuleSuppression#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @builtins.property
    @jsii.member(jsii_name="daysOfWeekInput")
    def days_of_week_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "daysOfWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="daysOfWeek")
    def days_of_week(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "daysOfWeek"))

    @days_of_week.setter
    def days_of_week(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference, "days_of_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysOfWeek", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MonitorAlertProcessingRuleSuppressionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#create MonitorAlertProcessingRuleSuppression#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#delete MonitorAlertProcessingRuleSuppression#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#read MonitorAlertProcessingRuleSuppression#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#update MonitorAlertProcessingRuleSuppression#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#create MonitorAlertProcessingRuleSuppression#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#delete MonitorAlertProcessingRuleSuppression#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#read MonitorAlertProcessingRuleSuppression#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_alert_processing_rule_suppression#update MonitorAlertProcessingRuleSuppression#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertProcessingRuleSuppressionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorAlertProcessingRuleSuppression.MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorAlertProcessingRuleSuppressionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorAlertProcessingRuleSuppression",
    "MonitorAlertProcessingRuleSuppressionCondition",
    "MonitorAlertProcessingRuleSuppressionConditionAlertContext",
    "MonitorAlertProcessingRuleSuppressionConditionAlertContextOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionAlertRuleId",
    "MonitorAlertProcessingRuleSuppressionConditionAlertRuleIdOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionAlertRuleName",
    "MonitorAlertProcessingRuleSuppressionConditionAlertRuleNameOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionDescription",
    "MonitorAlertProcessingRuleSuppressionConditionDescriptionOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionMonitorCondition",
    "MonitorAlertProcessingRuleSuppressionConditionMonitorConditionOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionMonitorService",
    "MonitorAlertProcessingRuleSuppressionConditionMonitorServiceOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionSeverity",
    "MonitorAlertProcessingRuleSuppressionConditionSeverityOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionSignalType",
    "MonitorAlertProcessingRuleSuppressionConditionSignalTypeOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionTargetResource",
    "MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroup",
    "MonitorAlertProcessingRuleSuppressionConditionTargetResourceGroupOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionTargetResourceOutputReference",
    "MonitorAlertProcessingRuleSuppressionConditionTargetResourceType",
    "MonitorAlertProcessingRuleSuppressionConditionTargetResourceTypeOutputReference",
    "MonitorAlertProcessingRuleSuppressionConfig",
    "MonitorAlertProcessingRuleSuppressionSchedule",
    "MonitorAlertProcessingRuleSuppressionScheduleOutputReference",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrence",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDaily",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyList",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceDailyOutputReference",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthly",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyList",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceMonthlyOutputReference",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceOutputReference",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeekly",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyList",
    "MonitorAlertProcessingRuleSuppressionScheduleRecurrenceWeeklyOutputReference",
    "MonitorAlertProcessingRuleSuppressionTimeouts",
    "MonitorAlertProcessingRuleSuppressionTimeoutsOutputReference",
]

publication.publish()
