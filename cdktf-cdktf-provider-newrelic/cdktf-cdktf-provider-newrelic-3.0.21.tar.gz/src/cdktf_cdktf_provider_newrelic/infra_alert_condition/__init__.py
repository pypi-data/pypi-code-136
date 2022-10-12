'''
# `newrelic_infra_alert_condition`

Refer to the Terraform Registory for docs: [`newrelic_infra_alert_condition`](https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition).
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


class InfraAlertCondition(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.infraAlertCondition.InfraAlertCondition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition newrelic_infra_alert_condition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        policy_id: jsii.Number,
        type: builtins.str,
        comparison: typing.Optional[builtins.str] = None,
        critical: typing.Optional[typing.Union["InfraAlertConditionCritical", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        event: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_provider: typing.Optional[builtins.str] = None,
        process_where: typing.Optional[builtins.str] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        select: typing.Optional[builtins.str] = None,
        violation_close_timer: typing.Optional[jsii.Number] = None,
        warning: typing.Optional[typing.Union["InfraAlertConditionWarning", typing.Dict[str, typing.Any]]] = None,
        where: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition newrelic_infra_alert_condition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The Infrastructure alert condition's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#name InfraAlertCondition#name}
        :param policy_id: The ID of the alert policy where this condition should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#policy_id InfraAlertCondition#policy_id}
        :param type: The type of Infrastructure alert condition. Valid values are infra_process_running, infra_metric, and infra_host_not_reporting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#type InfraAlertCondition#type}
        :param comparison: The operator used to evaluate the threshold value. Valid values are above, below, and equal. Supported by the infra_metric and infra_process_running condition types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#comparison InfraAlertCondition#comparison}
        :param critical: critical block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#critical InfraAlertCondition#critical}
        :param description: The description of the Infrastructure alert condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#description InfraAlertCondition#description}
        :param enabled: Whether the condition is turned on or off. Valid values are true and false. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#enabled InfraAlertCondition#enabled}
        :param event: The metric event; for example, SystemSample or StorageSample. Supported by the infra_metric condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#event InfraAlertCondition#event}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#id InfraAlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_provider: For alerts on integrations, use this instead of event. Supported by the infra_metric condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#integration_provider InfraAlertCondition#integration_provider}
        :param process_where: Any filters applied to processes; for example: commandName = 'java'. Supported by the infra_process_running condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#process_where InfraAlertCondition#process_where}
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#runbook_url InfraAlertCondition#runbook_url}
        :param select: The attribute name to identify the metric being targeted; for example, cpuPercent, diskFreePercent, or memoryResidentSizeBytes. The underlying API will automatically populate this value for Infrastructure integrations (for example diskFreePercent), so make sure to explicitly include this value to avoid diff issues. Supported by the infra_metric condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#select InfraAlertCondition#select}
        :param violation_close_timer: Determines how much time, in hours, will pass before a violation is automatically closed. Valid values are 1, 2, 4, 8, 12, 24, 48, or 72 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#violation_close_timer InfraAlertCondition#violation_close_timer}
        :param warning: warning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#warning InfraAlertCondition#warning}
        :param where: If applicable, this identifies any Infrastructure host filters used; for example: hostname LIKE '%cassandra%'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#where InfraAlertCondition#where}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(InfraAlertCondition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = InfraAlertConditionConfig(
            name=name,
            policy_id=policy_id,
            type=type,
            comparison=comparison,
            critical=critical,
            description=description,
            enabled=enabled,
            event=event,
            id=id,
            integration_provider=integration_provider,
            process_where=process_where,
            runbook_url=runbook_url,
            select=select,
            violation_close_timer=violation_close_timer,
            warning=warning,
            where=where,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCritical")
    def put_critical(
        self,
        *,
        duration: jsii.Number,
        time_function: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#duration InfraAlertCondition#duration}.
        :param time_function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#time_function InfraAlertCondition#time_function}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#value InfraAlertCondition#value}.
        '''
        value_ = InfraAlertConditionCritical(
            duration=duration, time_function=time_function, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putCritical", [value_]))

    @jsii.member(jsii_name="putWarning")
    def put_warning(
        self,
        *,
        duration: jsii.Number,
        time_function: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#duration InfraAlertCondition#duration}.
        :param time_function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#time_function InfraAlertCondition#time_function}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#value InfraAlertCondition#value}.
        '''
        value_ = InfraAlertConditionWarning(
            duration=duration, time_function=time_function, value=value
        )

        return typing.cast(None, jsii.invoke(self, "putWarning", [value_]))

    @jsii.member(jsii_name="resetComparison")
    def reset_comparison(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComparison", []))

    @jsii.member(jsii_name="resetCritical")
    def reset_critical(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCritical", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEvent")
    def reset_event(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvent", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIntegrationProvider")
    def reset_integration_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationProvider", []))

    @jsii.member(jsii_name="resetProcessWhere")
    def reset_process_where(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcessWhere", []))

    @jsii.member(jsii_name="resetRunbookUrl")
    def reset_runbook_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunbookUrl", []))

    @jsii.member(jsii_name="resetSelect")
    def reset_select(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelect", []))

    @jsii.member(jsii_name="resetViolationCloseTimer")
    def reset_violation_close_timer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViolationCloseTimer", []))

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @jsii.member(jsii_name="resetWhere")
    def reset_where(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWhere", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="critical")
    def critical(self) -> "InfraAlertConditionCriticalOutputReference":
        return typing.cast("InfraAlertConditionCriticalOutputReference", jsii.get(self, "critical"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> "InfraAlertConditionWarningOutputReference":
        return typing.cast("InfraAlertConditionWarningOutputReference", jsii.get(self, "warning"))

    @builtins.property
    @jsii.member(jsii_name="comparisonInput")
    def comparison_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comparisonInput"))

    @builtins.property
    @jsii.member(jsii_name="criticalInput")
    def critical_input(self) -> typing.Optional["InfraAlertConditionCritical"]:
        return typing.cast(typing.Optional["InfraAlertConditionCritical"], jsii.get(self, "criticalInput"))

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
    @jsii.member(jsii_name="eventInput")
    def event_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationProviderInput")
    def integration_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="processWhereInput")
    def process_where_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "processWhereInput"))

    @builtins.property
    @jsii.member(jsii_name="runbookUrlInput")
    def runbook_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runbookUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="selectInput")
    def select_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="violationCloseTimerInput")
    def violation_close_timer_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "violationCloseTimerInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(self) -> typing.Optional["InfraAlertConditionWarning"]:
        return typing.cast(typing.Optional["InfraAlertConditionWarning"], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="whereInput")
    def where_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whereInput"))

    @builtins.property
    @jsii.member(jsii_name="comparison")
    def comparison(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comparison"))

    @comparison.setter
    def comparison(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "comparison").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comparison", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="event")
    def event(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "event"))

    @event.setter
    def event(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "event").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "event", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationProvider")
    def integration_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationProvider"))

    @integration_provider.setter
    def integration_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "integration_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationProvider", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="processWhere")
    def process_where(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "processWhere"))

    @process_where.setter
    def process_where(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "process_where").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "processWhere", value)

    @builtins.property
    @jsii.member(jsii_name="runbookUrl")
    def runbook_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runbookUrl"))

    @runbook_url.setter
    def runbook_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "runbook_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runbookUrl", value)

    @builtins.property
    @jsii.member(jsii_name="select")
    def select(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "select"))

    @select.setter
    def select(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "select").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "select", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="violationCloseTimer")
    def violation_close_timer(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "violationCloseTimer"))

    @violation_close_timer.setter
    def violation_close_timer(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "violation_close_timer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "violationCloseTimer", value)

    @builtins.property
    @jsii.member(jsii_name="where")
    def where(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "where"))

    @where.setter
    def where(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertCondition, "where").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "where", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.infraAlertCondition.InfraAlertConditionConfig",
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
        "policy_id": "policyId",
        "type": "type",
        "comparison": "comparison",
        "critical": "critical",
        "description": "description",
        "enabled": "enabled",
        "event": "event",
        "id": "id",
        "integration_provider": "integrationProvider",
        "process_where": "processWhere",
        "runbook_url": "runbookUrl",
        "select": "select",
        "violation_close_timer": "violationCloseTimer",
        "warning": "warning",
        "where": "where",
    },
)
class InfraAlertConditionConfig(cdktf.TerraformMetaArguments):
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
        policy_id: jsii.Number,
        type: builtins.str,
        comparison: typing.Optional[builtins.str] = None,
        critical: typing.Optional[typing.Union["InfraAlertConditionCritical", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        event: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_provider: typing.Optional[builtins.str] = None,
        process_where: typing.Optional[builtins.str] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        select: typing.Optional[builtins.str] = None,
        violation_close_timer: typing.Optional[jsii.Number] = None,
        warning: typing.Optional[typing.Union["InfraAlertConditionWarning", typing.Dict[str, typing.Any]]] = None,
        where: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The Infrastructure alert condition's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#name InfraAlertCondition#name}
        :param policy_id: The ID of the alert policy where this condition should be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#policy_id InfraAlertCondition#policy_id}
        :param type: The type of Infrastructure alert condition. Valid values are infra_process_running, infra_metric, and infra_host_not_reporting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#type InfraAlertCondition#type}
        :param comparison: The operator used to evaluate the threshold value. Valid values are above, below, and equal. Supported by the infra_metric and infra_process_running condition types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#comparison InfraAlertCondition#comparison}
        :param critical: critical block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#critical InfraAlertCondition#critical}
        :param description: The description of the Infrastructure alert condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#description InfraAlertCondition#description}
        :param enabled: Whether the condition is turned on or off. Valid values are true and false. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#enabled InfraAlertCondition#enabled}
        :param event: The metric event; for example, SystemSample or StorageSample. Supported by the infra_metric condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#event InfraAlertCondition#event}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#id InfraAlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_provider: For alerts on integrations, use this instead of event. Supported by the infra_metric condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#integration_provider InfraAlertCondition#integration_provider}
        :param process_where: Any filters applied to processes; for example: commandName = 'java'. Supported by the infra_process_running condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#process_where InfraAlertCondition#process_where}
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#runbook_url InfraAlertCondition#runbook_url}
        :param select: The attribute name to identify the metric being targeted; for example, cpuPercent, diskFreePercent, or memoryResidentSizeBytes. The underlying API will automatically populate this value for Infrastructure integrations (for example diskFreePercent), so make sure to explicitly include this value to avoid diff issues. Supported by the infra_metric condition type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#select InfraAlertCondition#select}
        :param violation_close_timer: Determines how much time, in hours, will pass before a violation is automatically closed. Valid values are 1, 2, 4, 8, 12, 24, 48, or 72 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#violation_close_timer InfraAlertCondition#violation_close_timer}
        :param warning: warning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#warning InfraAlertCondition#warning}
        :param where: If applicable, this identifies any Infrastructure host filters used; for example: hostname LIKE '%cassandra%'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#where InfraAlertCondition#where}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(critical, dict):
            critical = InfraAlertConditionCritical(**critical)
        if isinstance(warning, dict):
            warning = InfraAlertConditionWarning(**warning)
        if __debug__:
            type_hints = typing.get_type_hints(InfraAlertConditionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
            check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration_provider", value=integration_provider, expected_type=type_hints["integration_provider"])
            check_type(argname="argument process_where", value=process_where, expected_type=type_hints["process_where"])
            check_type(argname="argument runbook_url", value=runbook_url, expected_type=type_hints["runbook_url"])
            check_type(argname="argument select", value=select, expected_type=type_hints["select"])
            check_type(argname="argument violation_close_timer", value=violation_close_timer, expected_type=type_hints["violation_close_timer"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
            check_type(argname="argument where", value=where, expected_type=type_hints["where"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "policy_id": policy_id,
            "type": type,
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
        if comparison is not None:
            self._values["comparison"] = comparison
        if critical is not None:
            self._values["critical"] = critical
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if event is not None:
            self._values["event"] = event
        if id is not None:
            self._values["id"] = id
        if integration_provider is not None:
            self._values["integration_provider"] = integration_provider
        if process_where is not None:
            self._values["process_where"] = process_where
        if runbook_url is not None:
            self._values["runbook_url"] = runbook_url
        if select is not None:
            self._values["select"] = select
        if violation_close_timer is not None:
            self._values["violation_close_timer"] = violation_close_timer
        if warning is not None:
            self._values["warning"] = warning
        if where is not None:
            self._values["where"] = where

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
        '''The Infrastructure alert condition's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#name InfraAlertCondition#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_id(self) -> jsii.Number:
        '''The ID of the alert policy where this condition should be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#policy_id InfraAlertCondition#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of Infrastructure alert condition. Valid values are infra_process_running, infra_metric, and infra_host_not_reporting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#type InfraAlertCondition#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comparison(self) -> typing.Optional[builtins.str]:
        '''The operator used to evaluate the threshold value.

        Valid values are above, below, and equal. Supported by the infra_metric and infra_process_running condition types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#comparison InfraAlertCondition#comparison}
        '''
        result = self._values.get("comparison")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def critical(self) -> typing.Optional["InfraAlertConditionCritical"]:
        '''critical block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#critical InfraAlertCondition#critical}
        '''
        result = self._values.get("critical")
        return typing.cast(typing.Optional["InfraAlertConditionCritical"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the Infrastructure alert condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#description InfraAlertCondition#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the condition is turned on or off. Valid values are true and false. Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#enabled InfraAlertCondition#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def event(self) -> typing.Optional[builtins.str]:
        '''The metric event; for example, SystemSample or StorageSample. Supported by the infra_metric condition type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#event InfraAlertCondition#event}
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#id InfraAlertCondition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_provider(self) -> typing.Optional[builtins.str]:
        '''For alerts on integrations, use this instead of event. Supported by the infra_metric condition type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#integration_provider InfraAlertCondition#integration_provider}
        '''
        result = self._values.get("integration_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def process_where(self) -> typing.Optional[builtins.str]:
        '''Any filters applied to processes; for example: commandName = 'java'. Supported by the infra_process_running condition type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#process_where InfraAlertCondition#process_where}
        '''
        result = self._values.get("process_where")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runbook_url(self) -> typing.Optional[builtins.str]:
        '''Runbook URL to display in notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#runbook_url InfraAlertCondition#runbook_url}
        '''
        result = self._values.get("runbook_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def select(self) -> typing.Optional[builtins.str]:
        '''The attribute name to identify the metric being targeted;

        for example, cpuPercent, diskFreePercent, or memoryResidentSizeBytes. The underlying API will automatically populate this value for Infrastructure integrations (for example diskFreePercent), so make sure to explicitly include this value to avoid diff issues. Supported by the infra_metric condition type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#select InfraAlertCondition#select}
        '''
        result = self._values.get("select")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def violation_close_timer(self) -> typing.Optional[jsii.Number]:
        '''Determines how much time, in hours, will pass before a violation is automatically closed.

        Valid values are 1, 2, 4, 8, 12, 24, 48, or 72

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#violation_close_timer InfraAlertCondition#violation_close_timer}
        '''
        result = self._values.get("violation_close_timer")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def warning(self) -> typing.Optional["InfraAlertConditionWarning"]:
        '''warning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#warning InfraAlertCondition#warning}
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional["InfraAlertConditionWarning"], result)

    @builtins.property
    def where(self) -> typing.Optional[builtins.str]:
        '''If applicable, this identifies any Infrastructure host filters used; for example: hostname LIKE '%cassandra%'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#where InfraAlertCondition#where}
        '''
        result = self._values.get("where")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InfraAlertConditionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.infraAlertCondition.InfraAlertConditionCritical",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "time_function": "timeFunction",
        "value": "value",
    },
)
class InfraAlertConditionCritical:
    def __init__(
        self,
        *,
        duration: jsii.Number,
        time_function: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#duration InfraAlertCondition#duration}.
        :param time_function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#time_function InfraAlertCondition#time_function}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#value InfraAlertCondition#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(InfraAlertConditionCritical.__init__)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument time_function", value=time_function, expected_type=type_hints["time_function"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration": duration,
        }
        if time_function is not None:
            self._values["time_function"] = time_function
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def duration(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#duration InfraAlertCondition#duration}.'''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_function(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#time_function InfraAlertCondition#time_function}.'''
        result = self._values.get("time_function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#value InfraAlertCondition#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InfraAlertConditionCritical(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InfraAlertConditionCriticalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.infraAlertCondition.InfraAlertConditionCriticalOutputReference",
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
            type_hints = typing.get_type_hints(InfraAlertConditionCriticalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTimeFunction")
    def reset_time_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeFunction", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFunctionInput")
    def time_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionCriticalOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="timeFunction")
    def time_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeFunction"))

    @time_function.setter
    def time_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionCriticalOutputReference, "time_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeFunction", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionCriticalOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InfraAlertConditionCritical]:
        return typing.cast(typing.Optional[InfraAlertConditionCritical], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InfraAlertConditionCritical],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionCriticalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.infraAlertCondition.InfraAlertConditionWarning",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "time_function": "timeFunction",
        "value": "value",
    },
)
class InfraAlertConditionWarning:
    def __init__(
        self,
        *,
        duration: jsii.Number,
        time_function: typing.Optional[builtins.str] = None,
        value: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#duration InfraAlertCondition#duration}.
        :param time_function: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#time_function InfraAlertCondition#time_function}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#value InfraAlertCondition#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(InfraAlertConditionWarning.__init__)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument time_function", value=time_function, expected_type=type_hints["time_function"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "duration": duration,
        }
        if time_function is not None:
            self._values["time_function"] = time_function
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def duration(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#duration InfraAlertCondition#duration}.'''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time_function(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#time_function InfraAlertCondition#time_function}.'''
        result = self._values.get("time_function")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/infra_alert_condition#value InfraAlertCondition#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InfraAlertConditionWarning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InfraAlertConditionWarningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.infraAlertCondition.InfraAlertConditionWarningOutputReference",
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
            type_hints = typing.get_type_hints(InfraAlertConditionWarningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTimeFunction")
    def reset_time_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeFunction", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFunctionInput")
    def time_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionWarningOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="timeFunction")
    def time_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeFunction"))

    @time_function.setter
    def time_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionWarningOutputReference, "time_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeFunction", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionWarningOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[InfraAlertConditionWarning]:
        return typing.cast(typing.Optional[InfraAlertConditionWarning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[InfraAlertConditionWarning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(InfraAlertConditionWarningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "InfraAlertCondition",
    "InfraAlertConditionConfig",
    "InfraAlertConditionCritical",
    "InfraAlertConditionCriticalOutputReference",
    "InfraAlertConditionWarning",
    "InfraAlertConditionWarningOutputReference",
]

publication.publish()
