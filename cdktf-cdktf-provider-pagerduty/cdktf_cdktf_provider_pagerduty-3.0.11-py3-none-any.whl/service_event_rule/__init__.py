'''
# `pagerduty_service_event_rule`

Refer to the Terraform Registory for docs: [`pagerduty_service_event_rule`](https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule).
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


class ServiceEventRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule pagerduty_service_event_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        service: builtins.str,
        actions: typing.Optional[typing.Union["ServiceEventRuleActions", typing.Dict[str, typing.Any]]] = None,
        conditions: typing.Optional[typing.Union["ServiceEventRuleConditions", typing.Dict[str, typing.Any]]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
        time_frame: typing.Optional[typing.Union["ServiceEventRuleTimeFrame", typing.Dict[str, typing.Any]]] = None,
        variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleVariable", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule pagerduty_service_event_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#service ServiceEventRule#service}.
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#actions ServiceEventRule#actions}
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#conditions ServiceEventRule#conditions}
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#disabled ServiceEventRule#disabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#id ServiceEventRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#position ServiceEventRule#position}.
        :param time_frame: time_frame block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#time_frame ServiceEventRule#time_frame}
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#variable ServiceEventRule#variable}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceEventRuleConfig(
            service=service,
            actions=actions,
            conditions=conditions,
            disabled=disabled,
            id=id,
            position=position,
            time_frame=time_frame,
            variable=variable,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        annotate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsAnnotate", typing.Dict[str, typing.Any]]]]] = None,
        event_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsEventAction", typing.Dict[str, typing.Any]]]]] = None,
        extractions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsExtractions", typing.Dict[str, typing.Any]]]]] = None,
        priority: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsPriority", typing.Dict[str, typing.Any]]]]] = None,
        severity: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSeverity", typing.Dict[str, typing.Any]]]]] = None,
        suppress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSuppress", typing.Dict[str, typing.Any]]]]] = None,
        suspend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSuspend", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param annotate: annotate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#annotate ServiceEventRule#annotate}
        :param event_action: event_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#event_action ServiceEventRule#event_action}
        :param extractions: extractions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#extractions ServiceEventRule#extractions}
        :param priority: priority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#priority ServiceEventRule#priority}
        :param severity: severity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#severity ServiceEventRule#severity}
        :param suppress: suppress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#suppress ServiceEventRule#suppress}
        :param suspend: suspend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#suspend ServiceEventRule#suspend}
        '''
        value = ServiceEventRuleActions(
            annotate=annotate,
            event_action=event_action,
            extractions=extractions,
            priority=priority,
            severity=severity,
            suppress=suppress,
            suspend=suspend,
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putConditions")
    def put_conditions(
        self,
        *,
        operator: typing.Optional[builtins.str] = None,
        subconditions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleConditionsSubconditions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#operator ServiceEventRule#operator}.
        :param subconditions: subconditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#subconditions ServiceEventRule#subconditions}
        '''
        value = ServiceEventRuleConditions(
            operator=operator, subconditions=subconditions
        )

        return typing.cast(None, jsii.invoke(self, "putConditions", [value]))

    @jsii.member(jsii_name="putTimeFrame")
    def put_time_frame(
        self,
        *,
        active_between: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleTimeFrameActiveBetween", typing.Dict[str, typing.Any]]]]] = None,
        scheduled_weekly: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleTimeFrameScheduledWeekly", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param active_between: active_between block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#active_between ServiceEventRule#active_between}
        :param scheduled_weekly: scheduled_weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#scheduled_weekly ServiceEventRule#scheduled_weekly}
        '''
        value = ServiceEventRuleTimeFrame(
            active_between=active_between, scheduled_weekly=scheduled_weekly
        )

        return typing.cast(None, jsii.invoke(self, "putTimeFrame", [value]))

    @jsii.member(jsii_name="putVariable")
    def put_variable(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleVariable", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRule.put_variable)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVariable", [value]))

    @jsii.member(jsii_name="resetActions")
    def reset_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActions", []))

    @jsii.member(jsii_name="resetConditions")
    def reset_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditions", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPosition")
    def reset_position(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPosition", []))

    @jsii.member(jsii_name="resetTimeFrame")
    def reset_time_frame(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeFrame", []))

    @jsii.member(jsii_name="resetVariable")
    def reset_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariable", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> "ServiceEventRuleActionsOutputReference":
        return typing.cast("ServiceEventRuleActionsOutputReference", jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> "ServiceEventRuleConditionsOutputReference":
        return typing.cast("ServiceEventRuleConditionsOutputReference", jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="timeFrame")
    def time_frame(self) -> "ServiceEventRuleTimeFrameOutputReference":
        return typing.cast("ServiceEventRuleTimeFrameOutputReference", jsii.get(self, "timeFrame"))

    @builtins.property
    @jsii.member(jsii_name="variable")
    def variable(self) -> "ServiceEventRuleVariableList":
        return typing.cast("ServiceEventRuleVariableList", jsii.get(self, "variable"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional["ServiceEventRuleActions"]:
        return typing.cast(typing.Optional["ServiceEventRuleActions"], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionsInput")
    def conditions_input(self) -> typing.Optional["ServiceEventRuleConditions"]:
        return typing.cast(typing.Optional["ServiceEventRuleConditions"], jsii.get(self, "conditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "positionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFrameInput")
    def time_frame_input(self) -> typing.Optional["ServiceEventRuleTimeFrame"]:
        return typing.cast(typing.Optional["ServiceEventRuleTimeFrame"], jsii.get(self, "timeFrameInput"))

    @builtins.property
    @jsii.member(jsii_name="variableInput")
    def variable_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariable"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariable"]]], jsii.get(self, "variableInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRule, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "position"))

    @position.setter
    def position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRule, "position").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRule, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActions",
    jsii_struct_bases=[],
    name_mapping={
        "annotate": "annotate",
        "event_action": "eventAction",
        "extractions": "extractions",
        "priority": "priority",
        "severity": "severity",
        "suppress": "suppress",
        "suspend": "suspend",
    },
)
class ServiceEventRuleActions:
    def __init__(
        self,
        *,
        annotate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsAnnotate", typing.Dict[str, typing.Any]]]]] = None,
        event_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsEventAction", typing.Dict[str, typing.Any]]]]] = None,
        extractions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsExtractions", typing.Dict[str, typing.Any]]]]] = None,
        priority: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsPriority", typing.Dict[str, typing.Any]]]]] = None,
        severity: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSeverity", typing.Dict[str, typing.Any]]]]] = None,
        suppress: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSuppress", typing.Dict[str, typing.Any]]]]] = None,
        suspend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSuspend", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param annotate: annotate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#annotate ServiceEventRule#annotate}
        :param event_action: event_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#event_action ServiceEventRule#event_action}
        :param extractions: extractions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#extractions ServiceEventRule#extractions}
        :param priority: priority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#priority ServiceEventRule#priority}
        :param severity: severity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#severity ServiceEventRule#severity}
        :param suppress: suppress block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#suppress ServiceEventRule#suppress}
        :param suspend: suspend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#suspend ServiceEventRule#suspend}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActions.__init__)
            check_type(argname="argument annotate", value=annotate, expected_type=type_hints["annotate"])
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument extractions", value=extractions, expected_type=type_hints["extractions"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument suppress", value=suppress, expected_type=type_hints["suppress"])
            check_type(argname="argument suspend", value=suspend, expected_type=type_hints["suspend"])
        self._values: typing.Dict[str, typing.Any] = {}
        if annotate is not None:
            self._values["annotate"] = annotate
        if event_action is not None:
            self._values["event_action"] = event_action
        if extractions is not None:
            self._values["extractions"] = extractions
        if priority is not None:
            self._values["priority"] = priority
        if severity is not None:
            self._values["severity"] = severity
        if suppress is not None:
            self._values["suppress"] = suppress
        if suspend is not None:
            self._values["suspend"] = suspend

    @builtins.property
    def annotate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsAnnotate"]]]:
        '''annotate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#annotate ServiceEventRule#annotate}
        '''
        result = self._values.get("annotate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsAnnotate"]]], result)

    @builtins.property
    def event_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsEventAction"]]]:
        '''event_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#event_action ServiceEventRule#event_action}
        '''
        result = self._values.get("event_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsEventAction"]]], result)

    @builtins.property
    def extractions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsExtractions"]]]:
        '''extractions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#extractions ServiceEventRule#extractions}
        '''
        result = self._values.get("extractions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsExtractions"]]], result)

    @builtins.property
    def priority(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsPriority"]]]:
        '''priority block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#priority ServiceEventRule#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsPriority"]]], result)

    @builtins.property
    def severity(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSeverity"]]]:
        '''severity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#severity ServiceEventRule#severity}
        '''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSeverity"]]], result)

    @builtins.property
    def suppress(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuppress"]]]:
        '''suppress block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#suppress ServiceEventRule#suppress}
        '''
        result = self._values.get("suppress")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuppress"]]], result)

    @builtins.property
    def suspend(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuspend"]]]:
        '''suspend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#suspend ServiceEventRule#suspend}
        '''
        result = self._values.get("suspend")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuspend"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsAnnotate",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class ServiceEventRuleActionsAnnotate:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsAnnotate.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActionsAnnotate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleActionsAnnotateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsAnnotateList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsAnnotateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleActionsAnnotateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsAnnotateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleActionsAnnotateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsAnnotateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsAnnotateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsAnnotateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsAnnotate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsAnnotate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsAnnotate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsAnnotateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsAnnotateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsAnnotateOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsAnnotateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsAnnotateOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleActionsAnnotate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleActionsAnnotate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleActionsAnnotate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsAnnotateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsEventAction",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class ServiceEventRuleActionsEventAction:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsEventAction.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActionsEventAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleActionsEventActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsEventActionList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsEventActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleActionsEventActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsEventActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleActionsEventActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsEventActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsEventActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsEventActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsEventAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsEventAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsEventAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsEventActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsEventActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsEventActionOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsEventActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsEventActionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleActionsEventAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleActionsEventAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleActionsEventAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsEventActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsExtractions",
    jsii_struct_bases=[],
    name_mapping={
        "regex": "regex",
        "source": "source",
        "target": "target",
        "template": "template",
    },
)
class ServiceEventRuleActionsExtractions:
    def __init__(
        self,
        *,
        regex: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#regex ServiceEventRule#regex}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#source ServiceEventRule#source}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#target ServiceEventRule#target}.
        :param template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#template ServiceEventRule#template}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsExtractions.__init__)
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        self._values: typing.Dict[str, typing.Any] = {}
        if regex is not None:
            self._values["regex"] = regex
        if source is not None:
            self._values["source"] = source
        if target is not None:
            self._values["target"] = target
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#regex ServiceEventRule#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#source ServiceEventRule#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#target ServiceEventRule#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#template ServiceEventRule#template}.'''
        result = self._values.get("template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActionsExtractions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleActionsExtractionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsExtractionsList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsExtractionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleActionsExtractionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsExtractionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleActionsExtractionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsExtractions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsExtractions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsExtractions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsExtractionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsExtractionsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsExtractionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsOutputReference, "template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleActionsExtractions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleActionsExtractions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleActionsExtractions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsExtractionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAnnotate")
    def put_annotate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceEventRuleActionsAnnotate, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.put_annotate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAnnotate", [value]))

    @jsii.member(jsii_name="putEventAction")
    def put_event_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceEventRuleActionsEventAction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.put_event_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEventAction", [value]))

    @jsii.member(jsii_name="putExtractions")
    def put_extractions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceEventRuleActionsExtractions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.put_extractions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtractions", [value]))

    @jsii.member(jsii_name="putPriority")
    def put_priority(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsPriority", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.put_priority)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPriority", [value]))

    @jsii.member(jsii_name="putSeverity")
    def put_severity(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSeverity", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.put_severity)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSeverity", [value]))

    @jsii.member(jsii_name="putSuppress")
    def put_suppress(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSuppress", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.put_suppress)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSuppress", [value]))

    @jsii.member(jsii_name="putSuspend")
    def put_suspend(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleActionsSuspend", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsOutputReference.put_suspend)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSuspend", [value]))

    @jsii.member(jsii_name="resetAnnotate")
    def reset_annotate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotate", []))

    @jsii.member(jsii_name="resetEventAction")
    def reset_event_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventAction", []))

    @jsii.member(jsii_name="resetExtractions")
    def reset_extractions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtractions", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetSeverity")
    def reset_severity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverity", []))

    @jsii.member(jsii_name="resetSuppress")
    def reset_suppress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppress", []))

    @jsii.member(jsii_name="resetSuspend")
    def reset_suspend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspend", []))

    @builtins.property
    @jsii.member(jsii_name="annotate")
    def annotate(self) -> ServiceEventRuleActionsAnnotateList:
        return typing.cast(ServiceEventRuleActionsAnnotateList, jsii.get(self, "annotate"))

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> ServiceEventRuleActionsEventActionList:
        return typing.cast(ServiceEventRuleActionsEventActionList, jsii.get(self, "eventAction"))

    @builtins.property
    @jsii.member(jsii_name="extractions")
    def extractions(self) -> ServiceEventRuleActionsExtractionsList:
        return typing.cast(ServiceEventRuleActionsExtractionsList, jsii.get(self, "extractions"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> "ServiceEventRuleActionsPriorityList":
        return typing.cast("ServiceEventRuleActionsPriorityList", jsii.get(self, "priority"))

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> "ServiceEventRuleActionsSeverityList":
        return typing.cast("ServiceEventRuleActionsSeverityList", jsii.get(self, "severity"))

    @builtins.property
    @jsii.member(jsii_name="suppress")
    def suppress(self) -> "ServiceEventRuleActionsSuppressList":
        return typing.cast("ServiceEventRuleActionsSuppressList", jsii.get(self, "suppress"))

    @builtins.property
    @jsii.member(jsii_name="suspend")
    def suspend(self) -> "ServiceEventRuleActionsSuspendList":
        return typing.cast("ServiceEventRuleActionsSuspendList", jsii.get(self, "suspend"))

    @builtins.property
    @jsii.member(jsii_name="annotateInput")
    def annotate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsAnnotate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsAnnotate]]], jsii.get(self, "annotateInput"))

    @builtins.property
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsEventAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsEventAction]]], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="extractionsInput")
    def extractions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsExtractions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsExtractions]]], jsii.get(self, "extractionsInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsPriority"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsPriority"]]], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSeverity"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSeverity"]]], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressInput")
    def suppress_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuppress"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuppress"]]], jsii.get(self, "suppressInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendInput")
    def suspend_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuspend"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleActionsSuspend"]]], jsii.get(self, "suspendInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceEventRuleActions]:
        return typing.cast(typing.Optional[ServiceEventRuleActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceEventRuleActions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsPriority",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class ServiceEventRuleActionsPriority:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsPriority.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActionsPriority(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleActionsPriorityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsPriorityList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsPriorityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleActionsPriorityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsPriorityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleActionsPriorityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsPriorityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsPriorityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsPriorityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsPriority]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsPriority]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsPriority]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsPriorityList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsPriorityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsPriorityOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsPriorityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsPriorityOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleActionsPriority, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleActionsPriority, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleActionsPriority, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsPriorityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSeverity",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class ServiceEventRuleActionsSeverity:
    def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSeverity.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActionsSeverity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleActionsSeverityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSeverityList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSeverityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleActionsSeverityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSeverityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleActionsSeverityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSeverityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSeverityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSeverityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSeverity]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSeverity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSeverity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSeverityList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsSeverityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSeverityOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSeverityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSeverityOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleActionsSeverity, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleActionsSeverity, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleActionsSeverity, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSeverityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSuppress",
    jsii_struct_bases=[],
    name_mapping={
        "threshold_time_amount": "thresholdTimeAmount",
        "threshold_time_unit": "thresholdTimeUnit",
        "threshold_value": "thresholdValue",
        "value": "value",
    },
)
class ServiceEventRuleActionsSuppress:
    def __init__(
        self,
        *,
        threshold_time_amount: typing.Optional[jsii.Number] = None,
        threshold_time_unit: typing.Optional[builtins.str] = None,
        threshold_value: typing.Optional[jsii.Number] = None,
        value: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param threshold_time_amount: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#threshold_time_amount ServiceEventRule#threshold_time_amount}.
        :param threshold_time_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#threshold_time_unit ServiceEventRule#threshold_time_unit}.
        :param threshold_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#threshold_value ServiceEventRule#threshold_value}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuppress.__init__)
            check_type(argname="argument threshold_time_amount", value=threshold_time_amount, expected_type=type_hints["threshold_time_amount"])
            check_type(argname="argument threshold_time_unit", value=threshold_time_unit, expected_type=type_hints["threshold_time_unit"])
            check_type(argname="argument threshold_value", value=threshold_value, expected_type=type_hints["threshold_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if threshold_time_amount is not None:
            self._values["threshold_time_amount"] = threshold_time_amount
        if threshold_time_unit is not None:
            self._values["threshold_time_unit"] = threshold_time_unit
        if threshold_value is not None:
            self._values["threshold_value"] = threshold_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def threshold_time_amount(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#threshold_time_amount ServiceEventRule#threshold_time_amount}.'''
        result = self._values.get("threshold_time_amount")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def threshold_time_unit(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#threshold_time_unit ServiceEventRule#threshold_time_unit}.'''
        result = self._values.get("threshold_time_unit")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def threshold_value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#threshold_value ServiceEventRule#threshold_value}.'''
        result = self._values.get("threshold_value")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActionsSuppress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleActionsSuppressList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSuppressList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuppressList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleActionsSuppressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuppressList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleActionsSuppressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSuppress]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSuppress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSuppress]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsSuppressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSuppressOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuppressOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetThresholdTimeAmount")
    def reset_threshold_time_amount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdTimeAmount", []))

    @jsii.member(jsii_name="resetThresholdTimeUnit")
    def reset_threshold_time_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdTimeUnit", []))

    @jsii.member(jsii_name="resetThresholdValue")
    def reset_threshold_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThresholdValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="thresholdTimeAmountInput")
    def threshold_time_amount_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdTimeAmountInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdTimeUnitInput")
    def threshold_time_unit_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thresholdTimeUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdValueInput")
    def threshold_value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdValueInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdTimeAmount")
    def threshold_time_amount(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdTimeAmount"))

    @threshold_time_amount.setter
    def threshold_time_amount(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressOutputReference, "threshold_time_amount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdTimeAmount", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdTimeUnit")
    def threshold_time_unit(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thresholdTimeUnit"))

    @threshold_time_unit.setter
    def threshold_time_unit(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressOutputReference, "threshold_time_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdTimeUnit", value)

    @builtins.property
    @jsii.member(jsii_name="thresholdValue")
    def threshold_value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "thresholdValue"))

    @threshold_value.setter
    def threshold_value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressOutputReference, "threshold_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thresholdValue", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "value"))

    @value.setter
    def value(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleActionsSuppress, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleActionsSuppress, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleActionsSuppress, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuppressOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSuspend",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class ServiceEventRuleActionsSuspend:
    def __init__(self, *, value: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuspend.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def value(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleActionsSuspend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleActionsSuspendList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSuspendList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuspendList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleActionsSuspendOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuspendList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleActionsSuspendOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuspendList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuspendList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuspendList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSuspend]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSuspend]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleActionsSuspend]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuspendList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleActionsSuspendOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleActionsSuspendOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleActionsSuspendOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuspendOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleActionsSuspend, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleActionsSuspend, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleActionsSuspend, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleActionsSuspendOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditions",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "subconditions": "subconditions"},
)
class ServiceEventRuleConditions:
    def __init__(
        self,
        *,
        operator: typing.Optional[builtins.str] = None,
        subconditions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleConditionsSubconditions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#operator ServiceEventRule#operator}.
        :param subconditions: subconditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#subconditions ServiceEventRule#subconditions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConditions.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument subconditions", value=subconditions, expected_type=type_hints["subconditions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if operator is not None:
            self._values["operator"] = operator
        if subconditions is not None:
            self._values["subconditions"] = subconditions

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#operator ServiceEventRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subconditions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditions"]]]:
        '''subconditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#subconditions ServiceEventRule#subconditions}
        '''
        result = self._values.get("subconditions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleConditionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditionsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSubconditions")
    def put_subconditions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleConditionsSubconditions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsOutputReference.put_subconditions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSubconditions", [value]))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetSubconditions")
    def reset_subconditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubconditions", []))

    @builtins.property
    @jsii.member(jsii_name="subconditions")
    def subconditions(self) -> "ServiceEventRuleConditionsSubconditionsList":
        return typing.cast("ServiceEventRuleConditionsSubconditionsList", jsii.get(self, "subconditions"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="subconditionsInput")
    def subconditions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditions"]]], jsii.get(self, "subconditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceEventRuleConditions]:
        return typing.cast(typing.Optional[ServiceEventRuleConditions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceEventRuleConditions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditionsSubconditions",
    jsii_struct_bases=[],
    name_mapping={"operator": "operator", "parameter": "parameter"},
)
class ServiceEventRuleConditionsSubconditions:
    def __init__(
        self,
        *,
        operator: typing.Optional[builtins.str] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleConditionsSubconditionsParameter", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#operator ServiceEventRule#operator}.
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#parameter ServiceEventRule#parameter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditions.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        self._values: typing.Dict[str, typing.Any] = {}
        if operator is not None:
            self._values["operator"] = operator
        if parameter is not None:
            self._values["parameter"] = parameter

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#operator ServiceEventRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditionsParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#parameter ServiceEventRule#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditionsParameter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleConditionsSubconditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleConditionsSubconditionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditionsSubconditionsList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleConditionsSubconditionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleConditionsSubconditionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleConditionsSubconditions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleConditionsSubconditions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleConditionsSubconditions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleConditionsSubconditionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditionsSubconditionsOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleConditionsSubconditionsParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsOutputReference.put_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(self) -> "ServiceEventRuleConditionsSubconditionsParameterList":
        return typing.cast("ServiceEventRuleConditionsSubconditionsParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditionsParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleConditionsSubconditionsParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleConditionsSubconditions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleConditionsSubconditions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleConditionsSubconditions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditionsSubconditionsParameter",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "value": "value"},
)
class ServiceEventRuleConditionsSubconditionsParameter:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#path ServiceEventRule#path}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsParameter.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#path ServiceEventRule#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleConditionsSubconditionsParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleConditionsSubconditionsParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditionsSubconditionsParameterList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleConditionsSubconditionsParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleConditionsSubconditionsParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleConditionsSubconditionsParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleConditionsSubconditionsParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleConditionsSubconditionsParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleConditionsSubconditionsParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConditionsSubconditionsParameterOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleConditionsSubconditionsParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsParameterOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsParameterOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleConditionsSubconditionsParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleConditionsSubconditionsParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleConditionsSubconditionsParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleConditionsSubconditionsParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "service": "service",
        "actions": "actions",
        "conditions": "conditions",
        "disabled": "disabled",
        "id": "id",
        "position": "position",
        "time_frame": "timeFrame",
        "variable": "variable",
    },
)
class ServiceEventRuleConfig(cdktf.TerraformMetaArguments):
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
        service: builtins.str,
        actions: typing.Optional[typing.Union[ServiceEventRuleActions, typing.Dict[str, typing.Any]]] = None,
        conditions: typing.Optional[typing.Union[ServiceEventRuleConditions, typing.Dict[str, typing.Any]]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        position: typing.Optional[jsii.Number] = None,
        time_frame: typing.Optional[typing.Union["ServiceEventRuleTimeFrame", typing.Dict[str, typing.Any]]] = None,
        variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleVariable", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#service ServiceEventRule#service}.
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#actions ServiceEventRule#actions}
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#conditions ServiceEventRule#conditions}
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#disabled ServiceEventRule#disabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#id ServiceEventRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param position: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#position ServiceEventRule#position}.
        :param time_frame: time_frame block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#time_frame ServiceEventRule#time_frame}
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#variable ServiceEventRule#variable}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(actions, dict):
            actions = ServiceEventRuleActions(**actions)
        if isinstance(conditions, dict):
            conditions = ServiceEventRuleConditions(**conditions)
        if isinstance(time_frame, dict):
            time_frame = ServiceEventRuleTimeFrame(**time_frame)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            check_type(argname="argument time_frame", value=time_frame, expected_type=type_hints["time_frame"])
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
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
        if actions is not None:
            self._values["actions"] = actions
        if conditions is not None:
            self._values["conditions"] = conditions
        if disabled is not None:
            self._values["disabled"] = disabled
        if id is not None:
            self._values["id"] = id
        if position is not None:
            self._values["position"] = position
        if time_frame is not None:
            self._values["time_frame"] = time_frame
        if variable is not None:
            self._values["variable"] = variable

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
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#service ServiceEventRule#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def actions(self) -> typing.Optional[ServiceEventRuleActions]:
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#actions ServiceEventRule#actions}
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[ServiceEventRuleActions], result)

    @builtins.property
    def conditions(self) -> typing.Optional[ServiceEventRuleConditions]:
        '''conditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#conditions ServiceEventRule#conditions}
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[ServiceEventRuleConditions], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#disabled ServiceEventRule#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#id ServiceEventRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def position(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#position ServiceEventRule#position}.'''
        result = self._values.get("position")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time_frame(self) -> typing.Optional["ServiceEventRuleTimeFrame"]:
        '''time_frame block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#time_frame ServiceEventRule#time_frame}
        '''
        result = self._values.get("time_frame")
        return typing.cast(typing.Optional["ServiceEventRuleTimeFrame"], result)

    @builtins.property
    def variable(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariable"]]]:
        '''variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#variable ServiceEventRule#variable}
        '''
        result = self._values.get("variable")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariable"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrame",
    jsii_struct_bases=[],
    name_mapping={
        "active_between": "activeBetween",
        "scheduled_weekly": "scheduledWeekly",
    },
)
class ServiceEventRuleTimeFrame:
    def __init__(
        self,
        *,
        active_between: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleTimeFrameActiveBetween", typing.Dict[str, typing.Any]]]]] = None,
        scheduled_weekly: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleTimeFrameScheduledWeekly", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param active_between: active_between block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#active_between ServiceEventRule#active_between}
        :param scheduled_weekly: scheduled_weekly block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#scheduled_weekly ServiceEventRule#scheduled_weekly}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrame.__init__)
            check_type(argname="argument active_between", value=active_between, expected_type=type_hints["active_between"])
            check_type(argname="argument scheduled_weekly", value=scheduled_weekly, expected_type=type_hints["scheduled_weekly"])
        self._values: typing.Dict[str, typing.Any] = {}
        if active_between is not None:
            self._values["active_between"] = active_between
        if scheduled_weekly is not None:
            self._values["scheduled_weekly"] = scheduled_weekly

    @builtins.property
    def active_between(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleTimeFrameActiveBetween"]]]:
        '''active_between block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#active_between ServiceEventRule#active_between}
        '''
        result = self._values.get("active_between")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleTimeFrameActiveBetween"]]], result)

    @builtins.property
    def scheduled_weekly(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleTimeFrameScheduledWeekly"]]]:
        '''scheduled_weekly block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#scheduled_weekly ServiceEventRule#scheduled_weekly}
        '''
        result = self._values.get("scheduled_weekly")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleTimeFrameScheduledWeekly"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleTimeFrame(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrameActiveBetween",
    jsii_struct_bases=[],
    name_mapping={"end_time": "endTime", "start_time": "startTime"},
)
class ServiceEventRuleTimeFrameActiveBetween:
    def __init__(
        self,
        *,
        end_time: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#end_time ServiceEventRule#end_time}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#start_time ServiceEventRule#start_time}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameActiveBetween.__init__)
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
        self._values: typing.Dict[str, typing.Any] = {}
        if end_time is not None:
            self._values["end_time"] = end_time
        if start_time is not None:
            self._values["start_time"] = start_time

    @builtins.property
    def end_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#end_time ServiceEventRule#end_time}.'''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#start_time ServiceEventRule#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleTimeFrameActiveBetween(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleTimeFrameActiveBetweenList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrameActiveBetweenList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameActiveBetweenList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleTimeFrameActiveBetweenOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameActiveBetweenList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleTimeFrameActiveBetweenOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameActiveBetweenList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameActiveBetweenList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameActiveBetweenList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameActiveBetween]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameActiveBetween]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameActiveBetween]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameActiveBetweenList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleTimeFrameActiveBetweenOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrameActiveBetweenOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameActiveBetweenOutputReference.__init__)
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
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameActiveBetweenOutputReference, "end_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameActiveBetweenOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleTimeFrameActiveBetween, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleTimeFrameActiveBetween, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleTimeFrameActiveBetween, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameActiveBetweenOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleTimeFrameOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrameOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActiveBetween")
    def put_active_between(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceEventRuleTimeFrameActiveBetween, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameOutputReference.put_active_between)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActiveBetween", [value]))

    @jsii.member(jsii_name="putScheduledWeekly")
    def put_scheduled_weekly(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleTimeFrameScheduledWeekly", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameOutputReference.put_scheduled_weekly)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduledWeekly", [value]))

    @jsii.member(jsii_name="resetActiveBetween")
    def reset_active_between(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveBetween", []))

    @jsii.member(jsii_name="resetScheduledWeekly")
    def reset_scheduled_weekly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduledWeekly", []))

    @builtins.property
    @jsii.member(jsii_name="activeBetween")
    def active_between(self) -> ServiceEventRuleTimeFrameActiveBetweenList:
        return typing.cast(ServiceEventRuleTimeFrameActiveBetweenList, jsii.get(self, "activeBetween"))

    @builtins.property
    @jsii.member(jsii_name="scheduledWeekly")
    def scheduled_weekly(self) -> "ServiceEventRuleTimeFrameScheduledWeeklyList":
        return typing.cast("ServiceEventRuleTimeFrameScheduledWeeklyList", jsii.get(self, "scheduledWeekly"))

    @builtins.property
    @jsii.member(jsii_name="activeBetweenInput")
    def active_between_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameActiveBetween]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameActiveBetween]]], jsii.get(self, "activeBetweenInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduledWeeklyInput")
    def scheduled_weekly_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleTimeFrameScheduledWeekly"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleTimeFrameScheduledWeekly"]]], jsii.get(self, "scheduledWeeklyInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ServiceEventRuleTimeFrame]:
        return typing.cast(typing.Optional[ServiceEventRuleTimeFrame], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ServiceEventRuleTimeFrame]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrameScheduledWeekly",
    jsii_struct_bases=[],
    name_mapping={
        "duration": "duration",
        "start_time": "startTime",
        "timezone": "timezone",
        "weekdays": "weekdays",
    },
)
class ServiceEventRuleTimeFrameScheduledWeekly:
    def __init__(
        self,
        *,
        duration: typing.Optional[jsii.Number] = None,
        start_time: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[builtins.str] = None,
        weekdays: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#duration ServiceEventRule#duration}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#start_time ServiceEventRule#start_time}.
        :param timezone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#timezone ServiceEventRule#timezone}.
        :param weekdays: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#weekdays ServiceEventRule#weekdays}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameScheduledWeekly.__init__)
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument weekdays", value=weekdays, expected_type=type_hints["weekdays"])
        self._values: typing.Dict[str, typing.Any] = {}
        if duration is not None:
            self._values["duration"] = duration
        if start_time is not None:
            self._values["start_time"] = start_time
        if timezone is not None:
            self._values["timezone"] = timezone
        if weekdays is not None:
            self._values["weekdays"] = weekdays

    @builtins.property
    def duration(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#duration ServiceEventRule#duration}.'''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_time(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#start_time ServiceEventRule#start_time}.'''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#timezone ServiceEventRule#timezone}.'''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weekdays(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#weekdays ServiceEventRule#weekdays}.'''
        result = self._values.get("weekdays")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleTimeFrameScheduledWeekly(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleTimeFrameScheduledWeeklyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrameScheduledWeeklyList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameScheduledWeeklyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleTimeFrameScheduledWeeklyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameScheduledWeeklyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleTimeFrameScheduledWeeklyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameScheduledWeekly]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameScheduledWeekly]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleTimeFrameScheduledWeekly]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleTimeFrameScheduledWeeklyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleTimeFrameScheduledWeeklyOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleTimeFrameScheduledWeeklyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetWeekdays")
    def reset_weekdays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekdays", []))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="weekdaysInput")
    def weekdays_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "weekdaysInput"))

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyOutputReference, "duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyOutputReference, "start_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyOutputReference, "timezone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="weekdays")
    def weekdays(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "weekdays"))

    @weekdays.setter
    def weekdays(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyOutputReference, "weekdays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekdays", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleTimeFrameScheduledWeekly, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleTimeFrameScheduledWeekly, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleTimeFrameScheduledWeekly, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleTimeFrameScheduledWeeklyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleVariable",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parameters": "parameters", "type": "type"},
)
class ServiceEventRuleVariable:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleVariableParameters", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#name ServiceEventRule#name}.
        :param parameters: parameters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#parameters ServiceEventRule#parameters}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#type ServiceEventRule#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleVariable.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if parameters is not None:
            self._values["parameters"] = parameters
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#name ServiceEventRule#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariableParameters"]]]:
        '''parameters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#parameters ServiceEventRule#parameters}
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariableParameters"]]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#type ServiceEventRule#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleVariableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleVariableList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleVariableList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceEventRuleVariableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleVariableList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleVariableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleVariable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleVariable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleVariable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleVariableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleVariableOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleVariableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putParameters")
    def put_parameters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceEventRuleVariableParameters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleVariableOutputReference.put_parameters)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameters", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> "ServiceEventRuleVariableParametersList":
        return typing.cast("ServiceEventRuleVariableParametersList", jsii.get(self, "parameters"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariableParameters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceEventRuleVariableParameters"]]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleVariable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleVariable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleVariable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleVariableParameters",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "value": "value"},
)
class ServiceEventRuleVariableParameters:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#path ServiceEventRule#path}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleVariableParameters.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#path ServiceEventRule#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_event_rule#value ServiceEventRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEventRuleVariableParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceEventRuleVariableParametersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleVariableParametersList",
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
            type_hints = typing.get_type_hints(ServiceEventRuleVariableParametersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceEventRuleVariableParametersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceEventRuleVariableParametersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceEventRuleVariableParametersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableParametersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableParametersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableParametersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleVariableParameters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleVariableParameters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceEventRuleVariableParameters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableParametersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceEventRuleVariableParametersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceEventRule.ServiceEventRuleVariableParametersOutputReference",
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
            type_hints = typing.get_type_hints(ServiceEventRuleVariableParametersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableParametersOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableParametersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceEventRuleVariableParameters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceEventRuleVariableParameters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceEventRuleVariableParameters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceEventRuleVariableParametersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServiceEventRule",
    "ServiceEventRuleActions",
    "ServiceEventRuleActionsAnnotate",
    "ServiceEventRuleActionsAnnotateList",
    "ServiceEventRuleActionsAnnotateOutputReference",
    "ServiceEventRuleActionsEventAction",
    "ServiceEventRuleActionsEventActionList",
    "ServiceEventRuleActionsEventActionOutputReference",
    "ServiceEventRuleActionsExtractions",
    "ServiceEventRuleActionsExtractionsList",
    "ServiceEventRuleActionsExtractionsOutputReference",
    "ServiceEventRuleActionsOutputReference",
    "ServiceEventRuleActionsPriority",
    "ServiceEventRuleActionsPriorityList",
    "ServiceEventRuleActionsPriorityOutputReference",
    "ServiceEventRuleActionsSeverity",
    "ServiceEventRuleActionsSeverityList",
    "ServiceEventRuleActionsSeverityOutputReference",
    "ServiceEventRuleActionsSuppress",
    "ServiceEventRuleActionsSuppressList",
    "ServiceEventRuleActionsSuppressOutputReference",
    "ServiceEventRuleActionsSuspend",
    "ServiceEventRuleActionsSuspendList",
    "ServiceEventRuleActionsSuspendOutputReference",
    "ServiceEventRuleConditions",
    "ServiceEventRuleConditionsOutputReference",
    "ServiceEventRuleConditionsSubconditions",
    "ServiceEventRuleConditionsSubconditionsList",
    "ServiceEventRuleConditionsSubconditionsOutputReference",
    "ServiceEventRuleConditionsSubconditionsParameter",
    "ServiceEventRuleConditionsSubconditionsParameterList",
    "ServiceEventRuleConditionsSubconditionsParameterOutputReference",
    "ServiceEventRuleConfig",
    "ServiceEventRuleTimeFrame",
    "ServiceEventRuleTimeFrameActiveBetween",
    "ServiceEventRuleTimeFrameActiveBetweenList",
    "ServiceEventRuleTimeFrameActiveBetweenOutputReference",
    "ServiceEventRuleTimeFrameOutputReference",
    "ServiceEventRuleTimeFrameScheduledWeekly",
    "ServiceEventRuleTimeFrameScheduledWeeklyList",
    "ServiceEventRuleTimeFrameScheduledWeeklyOutputReference",
    "ServiceEventRuleVariable",
    "ServiceEventRuleVariableList",
    "ServiceEventRuleVariableOutputReference",
    "ServiceEventRuleVariableParameters",
    "ServiceEventRuleVariableParametersList",
    "ServiceEventRuleVariableParametersOutputReference",
]

publication.publish()
