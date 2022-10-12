'''
# `pagerduty_event_orchestration_service`

Refer to the Terraform Registory for docs: [`pagerduty_event_orchestration_service`](https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service).
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


class EventOrchestrationService(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationService",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service pagerduty_event_orchestration_service}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        catch_all: typing.Union["EventOrchestrationServiceCatchAll", typing.Dict[str, typing.Any]],
        service: builtins.str,
        set: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSet", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service pagerduty_event_orchestration_service} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param catch_all: catch_all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#catch_all EventOrchestrationService#catch_all}
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#service EventOrchestrationService#service}.
        :param set: set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#set EventOrchestrationService#set}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#id EventOrchestrationService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationService.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = EventOrchestrationServiceConfig(
            catch_all=catch_all,
            service=service,
            set=set,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCatchAll")
    def put_catch_all(
        self,
        *,
        actions: typing.Union["EventOrchestrationServiceCatchAllActions", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#actions EventOrchestrationService#actions}
        '''
        value = EventOrchestrationServiceCatchAll(actions=actions)

        return typing.cast(None, jsii.invoke(self, "putCatchAll", [value]))

    @jsii.member(jsii_name="putSet")
    def put_set(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSet", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationService.put_set)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSet", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="catchAll")
    def catch_all(self) -> "EventOrchestrationServiceCatchAllOutputReference":
        return typing.cast("EventOrchestrationServiceCatchAllOutputReference", jsii.get(self, "catchAll"))

    @builtins.property
    @jsii.member(jsii_name="set")
    def set(self) -> "EventOrchestrationServiceSetList":
        return typing.cast("EventOrchestrationServiceSetList", jsii.get(self, "set"))

    @builtins.property
    @jsii.member(jsii_name="catchAllInput")
    def catch_all_input(self) -> typing.Optional["EventOrchestrationServiceCatchAll"]:
        return typing.cast(typing.Optional["EventOrchestrationServiceCatchAll"], jsii.get(self, "catchAllInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="setInput")
    def set_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSet"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSet"]]], jsii.get(self, "setInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationService, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationService, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAll",
    jsii_struct_bases=[],
    name_mapping={"actions": "actions"},
)
class EventOrchestrationServiceCatchAll:
    def __init__(
        self,
        *,
        actions: typing.Union["EventOrchestrationServiceCatchAllActions", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#actions EventOrchestrationService#actions}
        '''
        if isinstance(actions, dict):
            actions = EventOrchestrationServiceCatchAllActions(**actions)
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAll.__init__)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
        }

    @builtins.property
    def actions(self) -> "EventOrchestrationServiceCatchAllActions":
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#actions EventOrchestrationService#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast("EventOrchestrationServiceCatchAllActions", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAll(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActions",
    jsii_struct_bases=[],
    name_mapping={
        "annotate": "annotate",
        "automation_action": "automationAction",
        "event_action": "eventAction",
        "extraction": "extraction",
        "pagerduty_automation_action": "pagerdutyAutomationAction",
        "priority": "priority",
        "route_to": "routeTo",
        "severity": "severity",
        "suppress": "suppress",
        "suspend": "suspend",
        "variable": "variable",
    },
)
class EventOrchestrationServiceCatchAllActions:
    def __init__(
        self,
        *,
        annotate: typing.Optional[builtins.str] = None,
        automation_action: typing.Optional[typing.Union["EventOrchestrationServiceCatchAllActionsAutomationAction", typing.Dict[str, typing.Any]]] = None,
        event_action: typing.Optional[builtins.str] = None,
        extraction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceCatchAllActionsExtraction", typing.Dict[str, typing.Any]]]]] = None,
        pagerduty_automation_action: typing.Optional[typing.Union["EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction", typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        route_to: typing.Optional[builtins.str] = None,
        severity: typing.Optional[builtins.str] = None,
        suppress: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suspend: typing.Optional[jsii.Number] = None,
        variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceCatchAllActionsVariable", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param annotate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#annotate EventOrchestrationService#annotate}.
        :param automation_action: automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#automation_action EventOrchestrationService#automation_action}
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#event_action EventOrchestrationService#event_action}.
        :param extraction: extraction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#extraction EventOrchestrationService#extraction}
        :param pagerduty_automation_action: pagerduty_automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#pagerduty_automation_action EventOrchestrationService#pagerduty_automation_action}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#priority EventOrchestrationService#priority}.
        :param route_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#route_to EventOrchestrationService#route_to}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#severity EventOrchestrationService#severity}.
        :param suppress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suppress EventOrchestrationService#suppress}.
        :param suspend: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suspend EventOrchestrationService#suspend}.
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#variable EventOrchestrationService#variable}
        '''
        if isinstance(automation_action, dict):
            automation_action = EventOrchestrationServiceCatchAllActionsAutomationAction(**automation_action)
        if isinstance(pagerduty_automation_action, dict):
            pagerduty_automation_action = EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction(**pagerduty_automation_action)
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActions.__init__)
            check_type(argname="argument annotate", value=annotate, expected_type=type_hints["annotate"])
            check_type(argname="argument automation_action", value=automation_action, expected_type=type_hints["automation_action"])
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument extraction", value=extraction, expected_type=type_hints["extraction"])
            check_type(argname="argument pagerduty_automation_action", value=pagerduty_automation_action, expected_type=type_hints["pagerduty_automation_action"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument route_to", value=route_to, expected_type=type_hints["route_to"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument suppress", value=suppress, expected_type=type_hints["suppress"])
            check_type(argname="argument suspend", value=suspend, expected_type=type_hints["suspend"])
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        self._values: typing.Dict[str, typing.Any] = {}
        if annotate is not None:
            self._values["annotate"] = annotate
        if automation_action is not None:
            self._values["automation_action"] = automation_action
        if event_action is not None:
            self._values["event_action"] = event_action
        if extraction is not None:
            self._values["extraction"] = extraction
        if pagerduty_automation_action is not None:
            self._values["pagerduty_automation_action"] = pagerduty_automation_action
        if priority is not None:
            self._values["priority"] = priority
        if route_to is not None:
            self._values["route_to"] = route_to
        if severity is not None:
            self._values["severity"] = severity
        if suppress is not None:
            self._values["suppress"] = suppress
        if suspend is not None:
            self._values["suspend"] = suspend
        if variable is not None:
            self._values["variable"] = variable

    @builtins.property
    def annotate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#annotate EventOrchestrationService#annotate}.'''
        result = self._values.get("annotate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automation_action(
        self,
    ) -> typing.Optional["EventOrchestrationServiceCatchAllActionsAutomationAction"]:
        '''automation_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#automation_action EventOrchestrationService#automation_action}
        '''
        result = self._values.get("automation_action")
        return typing.cast(typing.Optional["EventOrchestrationServiceCatchAllActionsAutomationAction"], result)

    @builtins.property
    def event_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#event_action EventOrchestrationService#event_action}.'''
        result = self._values.get("event_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extraction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsExtraction"]]]:
        '''extraction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#extraction EventOrchestrationService#extraction}
        '''
        result = self._values.get("extraction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsExtraction"]]], result)

    @builtins.property
    def pagerduty_automation_action(
        self,
    ) -> typing.Optional["EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction"]:
        '''pagerduty_automation_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#pagerduty_automation_action EventOrchestrationService#pagerduty_automation_action}
        '''
        result = self._values.get("pagerduty_automation_action")
        return typing.cast(typing.Optional["EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction"], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#priority EventOrchestrationService#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#route_to EventOrchestrationService#route_to}.'''
        result = self._values.get("route_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def severity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#severity EventOrchestrationService#severity}.'''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suppress(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suppress EventOrchestrationService#suppress}.'''
        result = self._values.get("suppress")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def suspend(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suspend EventOrchestrationService#suspend}.'''
        result = self._values.get("suspend")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variable(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsVariable"]]]:
        '''variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#variable EventOrchestrationService#variable}
        '''
        result = self._values.get("variable")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsVariable"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAllActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationAction",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "url": "url",
        "auto_send": "autoSend",
        "header": "header",
        "parameter": "parameter",
    },
)
class EventOrchestrationServiceCatchAllActionsAutomationAction:
    def __init__(
        self,
        *,
        name: builtins.str,
        url: builtins.str,
        auto_send: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceCatchAllActionsAutomationActionHeader", typing.Dict[str, typing.Any]]]]] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceCatchAllActionsAutomationActionParameter", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#url EventOrchestrationService#url}.
        :param auto_send: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#auto_send EventOrchestrationService#auto_send}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#header EventOrchestrationService#header}
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#parameter EventOrchestrationService#parameter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationAction.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument auto_send", value=auto_send, expected_type=type_hints["auto_send"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "url": url,
        }
        if auto_send is not None:
            self._values["auto_send"] = auto_send
        if header is not None:
            self._values["header"] = header
        if parameter is not None:
            self._values["parameter"] = parameter

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#url EventOrchestrationService#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_send(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#auto_send EventOrchestrationService#auto_send}.'''
        result = self._values.get("auto_send")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsAutomationActionHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#header EventOrchestrationService#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsAutomationActionHeader"]]], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsAutomationActionParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#parameter EventOrchestrationService#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsAutomationActionParameter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAllActionsAutomationAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationActionHeader",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventOrchestrationServiceCatchAllActionsAutomationActionHeader:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionHeader.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAllActionsAutomationActionHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceCatchAllActionsAutomationActionParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference.put_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetAutoSend")
    def reset_auto_send(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoSend", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(
        self,
    ) -> EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList:
        return typing.cast(EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(
        self,
    ) -> "EventOrchestrationServiceCatchAllActionsAutomationActionParameterList":
        return typing.cast("EventOrchestrationServiceCatchAllActionsAutomationActionParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="autoSendInput")
    def auto_send_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoSendInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsAutomationActionParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsAutomationActionParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="autoSend")
    def auto_send(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoSend"))

    @auto_send.setter
    def auto_send(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference, "auto_send").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSend", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventOrchestrationServiceCatchAllActionsAutomationAction]:
        return typing.cast(typing.Optional[EventOrchestrationServiceCatchAllActionsAutomationAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventOrchestrationServiceCatchAllActionsAutomationAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationActionParameter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventOrchestrationServiceCatchAllActionsAutomationActionParameter:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionParameter.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAllActionsAutomationActionParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceCatchAllActionsAutomationActionParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationActionParameterList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsAutomationActionParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsExtraction",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "regex": "regex",
        "source": "source",
        "template": "template",
    },
)
class EventOrchestrationServiceCatchAllActionsExtraction:
    def __init__(
        self,
        *,
        target: builtins.str,
        regex: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#target EventOrchestrationService#target}.
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#regex EventOrchestrationService#regex}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#source EventOrchestrationService#source}.
        :param template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#template EventOrchestrationService#template}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsExtraction.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
        }
        if regex is not None:
            self._values["regex"] = regex
        if source is not None:
            self._values["source"] = source
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#target EventOrchestrationService#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#regex EventOrchestrationService#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#source EventOrchestrationService#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#template EventOrchestrationService#template}.'''
        result = self._values.get("template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAllActionsExtraction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceCatchAllActionsExtractionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsExtractionList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsExtractionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceCatchAllActionsExtractionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsExtractionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceCatchAllActionsExtractionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsExtraction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsExtraction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsExtraction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceCatchAllActionsExtractionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsExtractionOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsExtractionOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionOutputReference, "template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsExtraction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsExtraction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsExtraction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsExtractionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceCatchAllActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutomationAction")
    def put_automation_action(
        self,
        *,
        name: builtins.str,
        url: builtins.str,
        auto_send: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionHeader, typing.Dict[str, typing.Any]]]]] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationActionParameter, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#url EventOrchestrationService#url}.
        :param auto_send: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#auto_send EventOrchestrationService#auto_send}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#header EventOrchestrationService#header}
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#parameter EventOrchestrationService#parameter}
        '''
        value = EventOrchestrationServiceCatchAllActionsAutomationAction(
            name=name, url=url, auto_send=auto_send, header=header, parameter=parameter
        )

        return typing.cast(None, jsii.invoke(self, "putAutomationAction", [value]))

    @jsii.member(jsii_name="putExtraction")
    def put_extraction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceCatchAllActionsExtraction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsOutputReference.put_extraction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtraction", [value]))

    @jsii.member(jsii_name="putPagerdutyAutomationAction")
    def put_pagerduty_automation_action(self, *, action_id: builtins.str) -> None:
        '''
        :param action_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#action_id EventOrchestrationService#action_id}.
        '''
        value = EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction(
            action_id=action_id
        )

        return typing.cast(None, jsii.invoke(self, "putPagerdutyAutomationAction", [value]))

    @jsii.member(jsii_name="putVariable")
    def put_variable(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceCatchAllActionsVariable", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsOutputReference.put_variable)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVariable", [value]))

    @jsii.member(jsii_name="resetAnnotate")
    def reset_annotate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotate", []))

    @jsii.member(jsii_name="resetAutomationAction")
    def reset_automation_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomationAction", []))

    @jsii.member(jsii_name="resetEventAction")
    def reset_event_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventAction", []))

    @jsii.member(jsii_name="resetExtraction")
    def reset_extraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraction", []))

    @jsii.member(jsii_name="resetPagerdutyAutomationAction")
    def reset_pagerduty_automation_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPagerdutyAutomationAction", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetRouteTo")
    def reset_route_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteTo", []))

    @jsii.member(jsii_name="resetSeverity")
    def reset_severity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverity", []))

    @jsii.member(jsii_name="resetSuppress")
    def reset_suppress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppress", []))

    @jsii.member(jsii_name="resetSuspend")
    def reset_suspend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspend", []))

    @jsii.member(jsii_name="resetVariable")
    def reset_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariable", []))

    @builtins.property
    @jsii.member(jsii_name="automationAction")
    def automation_action(
        self,
    ) -> EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference:
        return typing.cast(EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference, jsii.get(self, "automationAction"))

    @builtins.property
    @jsii.member(jsii_name="extraction")
    def extraction(self) -> EventOrchestrationServiceCatchAllActionsExtractionList:
        return typing.cast(EventOrchestrationServiceCatchAllActionsExtractionList, jsii.get(self, "extraction"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyAutomationAction")
    def pagerduty_automation_action(
        self,
    ) -> "EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference":
        return typing.cast("EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference", jsii.get(self, "pagerdutyAutomationAction"))

    @builtins.property
    @jsii.member(jsii_name="variable")
    def variable(self) -> "EventOrchestrationServiceCatchAllActionsVariableList":
        return typing.cast("EventOrchestrationServiceCatchAllActionsVariableList", jsii.get(self, "variable"))

    @builtins.property
    @jsii.member(jsii_name="annotateInput")
    def annotate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "annotateInput"))

    @builtins.property
    @jsii.member(jsii_name="automationActionInput")
    def automation_action_input(
        self,
    ) -> typing.Optional[EventOrchestrationServiceCatchAllActionsAutomationAction]:
        return typing.cast(typing.Optional[EventOrchestrationServiceCatchAllActionsAutomationAction], jsii.get(self, "automationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="extractionInput")
    def extraction_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsExtraction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsExtraction]]], jsii.get(self, "extractionInput"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyAutomationActionInput")
    def pagerduty_automation_action_input(
        self,
    ) -> typing.Optional["EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction"]:
        return typing.cast(typing.Optional["EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction"], jsii.get(self, "pagerdutyAutomationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="routeToInput")
    def route_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeToInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressInput")
    def suppress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "suppressInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendInput")
    def suspend_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "suspendInput"))

    @builtins.property
    @jsii.member(jsii_name="variableInput")
    def variable_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsVariable"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceCatchAllActionsVariable"]]], jsii.get(self, "variableInput"))

    @builtins.property
    @jsii.member(jsii_name="annotate")
    def annotate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "annotate"))

    @annotate.setter
    def annotate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "annotate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotate", value)

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "event_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="routeTo")
    def route_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeTo"))

    @route_to.setter
    def route_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "route_to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeTo", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="suppress")
    def suppress(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "suppress"))

    @suppress.setter
    def suppress(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "suppress").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppress", value)

    @builtins.property
    @jsii.member(jsii_name="suspend")
    def suspend(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "suspend"))

    @suspend.setter
    def suspend(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "suspend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspend", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventOrchestrationServiceCatchAllActions]:
        return typing.cast(typing.Optional[EventOrchestrationServiceCatchAllActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventOrchestrationServiceCatchAllActions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction",
    jsii_struct_bases=[],
    name_mapping={"action_id": "actionId"},
)
class EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction:
    def __init__(self, *, action_id: builtins.str) -> None:
        '''
        :param action_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#action_id EventOrchestrationService#action_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction.__init__)
            check_type(argname="argument action_id", value=action_id, expected_type=type_hints["action_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_id": action_id,
        }

    @builtins.property
    def action_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#action_id EventOrchestrationService#action_id}.'''
        result = self._values.get("action_id")
        assert result is not None, "Required property 'action_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="actionIdInput")
    def action_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="actionId")
    def action_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionId"))

    @action_id.setter
    def action_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference, "action_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction]:
        return typing.cast(typing.Optional[EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsVariable",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "type": "type", "value": "value"},
)
class EventOrchestrationServiceCatchAllActionsVariable:
    def __init__(
        self,
        *,
        name: builtins.str,
        path: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#path EventOrchestrationService#path}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#type EventOrchestrationService#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsVariable.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "path": path,
            "type": type,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#path EventOrchestrationService#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#type EventOrchestrationService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceCatchAllActionsVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceCatchAllActionsVariableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsVariableList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsVariableList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceCatchAllActionsVariableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsVariableList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceCatchAllActionsVariableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsVariable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsVariable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceCatchAllActionsVariable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceCatchAllActionsVariableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllActionsVariableOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllActionsVariableOutputReference.__init__)
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
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsVariable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsVariable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsVariable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllActionsVariableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceCatchAllOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceCatchAllOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceCatchAllOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        annotate: typing.Optional[builtins.str] = None,
        automation_action: typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsAutomationAction, typing.Dict[str, typing.Any]]] = None,
        event_action: typing.Optional[builtins.str] = None,
        extraction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceCatchAllActionsExtraction, typing.Dict[str, typing.Any]]]]] = None,
        pagerduty_automation_action: typing.Optional[typing.Union[EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction, typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        route_to: typing.Optional[builtins.str] = None,
        severity: typing.Optional[builtins.str] = None,
        suppress: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suspend: typing.Optional[jsii.Number] = None,
        variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceCatchAllActionsVariable, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param annotate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#annotate EventOrchestrationService#annotate}.
        :param automation_action: automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#automation_action EventOrchestrationService#automation_action}
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#event_action EventOrchestrationService#event_action}.
        :param extraction: extraction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#extraction EventOrchestrationService#extraction}
        :param pagerduty_automation_action: pagerduty_automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#pagerduty_automation_action EventOrchestrationService#pagerduty_automation_action}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#priority EventOrchestrationService#priority}.
        :param route_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#route_to EventOrchestrationService#route_to}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#severity EventOrchestrationService#severity}.
        :param suppress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suppress EventOrchestrationService#suppress}.
        :param suspend: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suspend EventOrchestrationService#suspend}.
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#variable EventOrchestrationService#variable}
        '''
        value = EventOrchestrationServiceCatchAllActions(
            annotate=annotate,
            automation_action=automation_action,
            event_action=event_action,
            extraction=extraction,
            pagerduty_automation_action=pagerduty_automation_action,
            priority=priority,
            route_to=route_to,
            severity=severity,
            suppress=suppress,
            suspend=suspend,
            variable=variable,
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> EventOrchestrationServiceCatchAllActionsOutputReference:
        return typing.cast(EventOrchestrationServiceCatchAllActionsOutputReference, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(
        self,
    ) -> typing.Optional[EventOrchestrationServiceCatchAllActions]:
        return typing.cast(typing.Optional[EventOrchestrationServiceCatchAllActions], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[EventOrchestrationServiceCatchAll]:
        return typing.cast(typing.Optional[EventOrchestrationServiceCatchAll], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventOrchestrationServiceCatchAll],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceCatchAllOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "catch_all": "catchAll",
        "service": "service",
        "set": "set",
        "id": "id",
    },
)
class EventOrchestrationServiceConfig(cdktf.TerraformMetaArguments):
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
        catch_all: typing.Union[EventOrchestrationServiceCatchAll, typing.Dict[str, typing.Any]],
        service: builtins.str,
        set: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSet", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param catch_all: catch_all block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#catch_all EventOrchestrationService#catch_all}
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#service EventOrchestrationService#service}.
        :param set: set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#set EventOrchestrationService#set}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#id EventOrchestrationService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(catch_all, dict):
            catch_all = EventOrchestrationServiceCatchAll(**catch_all)
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument catch_all", value=catch_all, expected_type=type_hints["catch_all"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument set", value=set, expected_type=type_hints["set"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "catch_all": catch_all,
            "service": service,
            "set": set,
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
    def catch_all(self) -> EventOrchestrationServiceCatchAll:
        '''catch_all block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#catch_all EventOrchestrationService#catch_all}
        '''
        result = self._values.get("catch_all")
        assert result is not None, "Required property 'catch_all' is missing"
        return typing.cast(EventOrchestrationServiceCatchAll, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#service EventOrchestrationService#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def set(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSet"]]:
        '''set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#set EventOrchestrationService#set}
        '''
        result = self._values.get("set")
        assert result is not None, "Required property 'set' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSet"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#id EventOrchestrationService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSet",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "rule": "rule"},
)
class EventOrchestrationServiceSet:
    def __init__(
        self,
        *,
        id: builtins.str,
        rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRule", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#id EventOrchestrationService#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#rule EventOrchestrationService#rule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSet.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if rule is not None:
            self._values["rule"] = rule

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#id EventOrchestrationService#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRule"]]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#rule EventOrchestrationService#rule}
        '''
        result = self._values.get("rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceSetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "EventOrchestrationServiceSetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceSetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSet]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetOutputReference.put_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

    @jsii.member(jsii_name="resetRule")
    def reset_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRule", []))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "EventOrchestrationServiceSetRuleList":
        return typing.cast("EventOrchestrationServiceSetRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceSet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceSet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceSet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRule",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "condition": "condition",
        "disabled": "disabled",
        "label": "label",
    },
)
class EventOrchestrationServiceSetRule:
    def __init__(
        self,
        *,
        actions: typing.Union["EventOrchestrationServiceSetRuleActions", typing.Dict[str, typing.Any]],
        condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRuleCondition", typing.Dict[str, typing.Any]]]]] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#actions EventOrchestrationService#actions}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#condition EventOrchestrationService#condition}
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#disabled EventOrchestrationService#disabled}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#label EventOrchestrationService#label}.
        '''
        if isinstance(actions, dict):
            actions = EventOrchestrationServiceSetRuleActions(**actions)
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRule.__init__)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
        }
        if condition is not None:
            self._values["condition"] = condition
        if disabled is not None:
            self._values["disabled"] = disabled
        if label is not None:
            self._values["label"] = label

    @builtins.property
    def actions(self) -> "EventOrchestrationServiceSetRuleActions":
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#actions EventOrchestrationService#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast("EventOrchestrationServiceSetRuleActions", result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleCondition"]]]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#condition EventOrchestrationService#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleCondition"]]], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#disabled EventOrchestrationService#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#label EventOrchestrationService#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActions",
    jsii_struct_bases=[],
    name_mapping={
        "annotate": "annotate",
        "automation_action": "automationAction",
        "event_action": "eventAction",
        "extraction": "extraction",
        "pagerduty_automation_action": "pagerdutyAutomationAction",
        "priority": "priority",
        "route_to": "routeTo",
        "severity": "severity",
        "suppress": "suppress",
        "suspend": "suspend",
        "variable": "variable",
    },
)
class EventOrchestrationServiceSetRuleActions:
    def __init__(
        self,
        *,
        annotate: typing.Optional[builtins.str] = None,
        automation_action: typing.Optional[typing.Union["EventOrchestrationServiceSetRuleActionsAutomationAction", typing.Dict[str, typing.Any]]] = None,
        event_action: typing.Optional[builtins.str] = None,
        extraction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRuleActionsExtraction", typing.Dict[str, typing.Any]]]]] = None,
        pagerduty_automation_action: typing.Optional[typing.Union["EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction", typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        route_to: typing.Optional[builtins.str] = None,
        severity: typing.Optional[builtins.str] = None,
        suppress: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suspend: typing.Optional[jsii.Number] = None,
        variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRuleActionsVariable", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param annotate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#annotate EventOrchestrationService#annotate}.
        :param automation_action: automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#automation_action EventOrchestrationService#automation_action}
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#event_action EventOrchestrationService#event_action}.
        :param extraction: extraction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#extraction EventOrchestrationService#extraction}
        :param pagerduty_automation_action: pagerduty_automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#pagerduty_automation_action EventOrchestrationService#pagerduty_automation_action}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#priority EventOrchestrationService#priority}.
        :param route_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#route_to EventOrchestrationService#route_to}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#severity EventOrchestrationService#severity}.
        :param suppress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suppress EventOrchestrationService#suppress}.
        :param suspend: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suspend EventOrchestrationService#suspend}.
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#variable EventOrchestrationService#variable}
        '''
        if isinstance(automation_action, dict):
            automation_action = EventOrchestrationServiceSetRuleActionsAutomationAction(**automation_action)
        if isinstance(pagerduty_automation_action, dict):
            pagerduty_automation_action = EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction(**pagerduty_automation_action)
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActions.__init__)
            check_type(argname="argument annotate", value=annotate, expected_type=type_hints["annotate"])
            check_type(argname="argument automation_action", value=automation_action, expected_type=type_hints["automation_action"])
            check_type(argname="argument event_action", value=event_action, expected_type=type_hints["event_action"])
            check_type(argname="argument extraction", value=extraction, expected_type=type_hints["extraction"])
            check_type(argname="argument pagerduty_automation_action", value=pagerduty_automation_action, expected_type=type_hints["pagerduty_automation_action"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument route_to", value=route_to, expected_type=type_hints["route_to"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument suppress", value=suppress, expected_type=type_hints["suppress"])
            check_type(argname="argument suspend", value=suspend, expected_type=type_hints["suspend"])
            check_type(argname="argument variable", value=variable, expected_type=type_hints["variable"])
        self._values: typing.Dict[str, typing.Any] = {}
        if annotate is not None:
            self._values["annotate"] = annotate
        if automation_action is not None:
            self._values["automation_action"] = automation_action
        if event_action is not None:
            self._values["event_action"] = event_action
        if extraction is not None:
            self._values["extraction"] = extraction
        if pagerduty_automation_action is not None:
            self._values["pagerduty_automation_action"] = pagerduty_automation_action
        if priority is not None:
            self._values["priority"] = priority
        if route_to is not None:
            self._values["route_to"] = route_to
        if severity is not None:
            self._values["severity"] = severity
        if suppress is not None:
            self._values["suppress"] = suppress
        if suspend is not None:
            self._values["suspend"] = suspend
        if variable is not None:
            self._values["variable"] = variable

    @builtins.property
    def annotate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#annotate EventOrchestrationService#annotate}.'''
        result = self._values.get("annotate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automation_action(
        self,
    ) -> typing.Optional["EventOrchestrationServiceSetRuleActionsAutomationAction"]:
        '''automation_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#automation_action EventOrchestrationService#automation_action}
        '''
        result = self._values.get("automation_action")
        return typing.cast(typing.Optional["EventOrchestrationServiceSetRuleActionsAutomationAction"], result)

    @builtins.property
    def event_action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#event_action EventOrchestrationService#event_action}.'''
        result = self._values.get("event_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extraction(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsExtraction"]]]:
        '''extraction block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#extraction EventOrchestrationService#extraction}
        '''
        result = self._values.get("extraction")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsExtraction"]]], result)

    @builtins.property
    def pagerduty_automation_action(
        self,
    ) -> typing.Optional["EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction"]:
        '''pagerduty_automation_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#pagerduty_automation_action EventOrchestrationService#pagerduty_automation_action}
        '''
        result = self._values.get("pagerduty_automation_action")
        return typing.cast(typing.Optional["EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction"], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#priority EventOrchestrationService#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_to(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#route_to EventOrchestrationService#route_to}.'''
        result = self._values.get("route_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def severity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#severity EventOrchestrationService#severity}.'''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def suppress(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suppress EventOrchestrationService#suppress}.'''
        result = self._values.get("suppress")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def suspend(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suspend EventOrchestrationService#suspend}.'''
        result = self._values.get("suspend")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def variable(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsVariable"]]]:
        '''variable block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#variable EventOrchestrationService#variable}
        '''
        result = self._values.get("variable")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsVariable"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationAction",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "url": "url",
        "auto_send": "autoSend",
        "header": "header",
        "parameter": "parameter",
    },
)
class EventOrchestrationServiceSetRuleActionsAutomationAction:
    def __init__(
        self,
        *,
        name: builtins.str,
        url: builtins.str,
        auto_send: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRuleActionsAutomationActionHeader", typing.Dict[str, typing.Any]]]]] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRuleActionsAutomationActionParameter", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#url EventOrchestrationService#url}.
        :param auto_send: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#auto_send EventOrchestrationService#auto_send}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#header EventOrchestrationService#header}
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#parameter EventOrchestrationService#parameter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationAction.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument auto_send", value=auto_send, expected_type=type_hints["auto_send"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "url": url,
        }
        if auto_send is not None:
            self._values["auto_send"] = auto_send
        if header is not None:
            self._values["header"] = header
        if parameter is not None:
            self._values["parameter"] = parameter

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#url EventOrchestrationService#url}.'''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_send(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#auto_send EventOrchestrationService#auto_send}.'''
        result = self._values.get("auto_send")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsAutomationActionHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#header EventOrchestrationService#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsAutomationActionHeader"]]], result)

    @builtins.property
    def parameter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsAutomationActionParameter"]]]:
        '''parameter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#parameter EventOrchestrationService#parameter}
        '''
        result = self._values.get("parameter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsAutomationActionParameter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleActionsAutomationAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationActionHeader",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventOrchestrationServiceSetRuleActionsAutomationActionHeader:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionHeader.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleActionsAutomationActionHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putParameter")
    def put_parameter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRuleActionsAutomationActionParameter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference.put_parameter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParameter", [value]))

    @jsii.member(jsii_name="resetAutoSend")
    def reset_auto_send(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoSend", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetParameter")
    def reset_parameter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameter", []))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(
        self,
    ) -> EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList:
        return typing.cast(EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="parameter")
    def parameter(
        self,
    ) -> "EventOrchestrationServiceSetRuleActionsAutomationActionParameterList":
        return typing.cast("EventOrchestrationServiceSetRuleActionsAutomationActionParameterList", jsii.get(self, "parameter"))

    @builtins.property
    @jsii.member(jsii_name="autoSendInput")
    def auto_send_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoSendInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterInput")
    def parameter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsAutomationActionParameter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsAutomationActionParameter"]]], jsii.get(self, "parameterInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="autoSend")
    def auto_send(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoSend"))

    @auto_send.setter
    def auto_send(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference, "auto_send").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoSend", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventOrchestrationServiceSetRuleActionsAutomationAction]:
        return typing.cast(typing.Optional[EventOrchestrationServiceSetRuleActionsAutomationAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventOrchestrationServiceSetRuleActionsAutomationAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationActionParameter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class EventOrchestrationServiceSetRuleActionsAutomationActionParameter:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionParameter.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#key EventOrchestrationService#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleActionsAutomationActionParameter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceSetRuleActionsAutomationActionParameterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationActionParameterList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionParameterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionParameterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionParameterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionParameterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionParameterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionParameter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionParameter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsAutomationActionParameter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionParameterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionParameter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionParameter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionParameter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsExtraction",
    jsii_struct_bases=[],
    name_mapping={
        "target": "target",
        "regex": "regex",
        "source": "source",
        "template": "template",
    },
)
class EventOrchestrationServiceSetRuleActionsExtraction:
    def __init__(
        self,
        *,
        target: builtins.str,
        regex: typing.Optional[builtins.str] = None,
        source: typing.Optional[builtins.str] = None,
        template: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#target EventOrchestrationService#target}.
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#regex EventOrchestrationService#regex}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#source EventOrchestrationService#source}.
        :param template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#template EventOrchestrationService#template}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsExtraction.__init__)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        self._values: typing.Dict[str, typing.Any] = {
            "target": target,
        }
        if regex is not None:
            self._values["regex"] = regex
        if source is not None:
            self._values["source"] = source
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#target EventOrchestrationService#target}.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#regex EventOrchestrationService#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#source EventOrchestrationService#source}.'''
        result = self._values.get("source")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#template EventOrchestrationService#template}.'''
        result = self._values.get("template")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleActionsExtraction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceSetRuleActionsExtractionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsExtractionList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsExtractionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceSetRuleActionsExtractionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsExtractionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceSetRuleActionsExtractionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsExtraction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsExtraction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsExtraction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleActionsExtractionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsExtractionOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsExtractionOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "template"))

    @template.setter
    def template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionOutputReference, "template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsExtraction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsExtraction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsExtraction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsExtractionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutomationAction")
    def put_automation_action(
        self,
        *,
        name: builtins.str,
        url: builtins.str,
        auto_send: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionHeader, typing.Dict[str, typing.Any]]]]] = None,
        parameter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationActionParameter, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#url EventOrchestrationService#url}.
        :param auto_send: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#auto_send EventOrchestrationService#auto_send}.
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#header EventOrchestrationService#header}
        :param parameter: parameter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#parameter EventOrchestrationService#parameter}
        '''
        value = EventOrchestrationServiceSetRuleActionsAutomationAction(
            name=name, url=url, auto_send=auto_send, header=header, parameter=parameter
        )

        return typing.cast(None, jsii.invoke(self, "putAutomationAction", [value]))

    @jsii.member(jsii_name="putExtraction")
    def put_extraction(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceSetRuleActionsExtraction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsOutputReference.put_extraction)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtraction", [value]))

    @jsii.member(jsii_name="putPagerdutyAutomationAction")
    def put_pagerduty_automation_action(self, *, action_id: builtins.str) -> None:
        '''
        :param action_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#action_id EventOrchestrationService#action_id}.
        '''
        value = EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction(
            action_id=action_id
        )

        return typing.cast(None, jsii.invoke(self, "putPagerdutyAutomationAction", [value]))

    @jsii.member(jsii_name="putVariable")
    def put_variable(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["EventOrchestrationServiceSetRuleActionsVariable", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsOutputReference.put_variable)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVariable", [value]))

    @jsii.member(jsii_name="resetAnnotate")
    def reset_annotate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotate", []))

    @jsii.member(jsii_name="resetAutomationAction")
    def reset_automation_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomationAction", []))

    @jsii.member(jsii_name="resetEventAction")
    def reset_event_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEventAction", []))

    @jsii.member(jsii_name="resetExtraction")
    def reset_extraction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraction", []))

    @jsii.member(jsii_name="resetPagerdutyAutomationAction")
    def reset_pagerduty_automation_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPagerdutyAutomationAction", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetRouteTo")
    def reset_route_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteTo", []))

    @jsii.member(jsii_name="resetSeverity")
    def reset_severity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverity", []))

    @jsii.member(jsii_name="resetSuppress")
    def reset_suppress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuppress", []))

    @jsii.member(jsii_name="resetSuspend")
    def reset_suspend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuspend", []))

    @jsii.member(jsii_name="resetVariable")
    def reset_variable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVariable", []))

    @builtins.property
    @jsii.member(jsii_name="automationAction")
    def automation_action(
        self,
    ) -> EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference:
        return typing.cast(EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference, jsii.get(self, "automationAction"))

    @builtins.property
    @jsii.member(jsii_name="extraction")
    def extraction(self) -> EventOrchestrationServiceSetRuleActionsExtractionList:
        return typing.cast(EventOrchestrationServiceSetRuleActionsExtractionList, jsii.get(self, "extraction"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyAutomationAction")
    def pagerduty_automation_action(
        self,
    ) -> "EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference":
        return typing.cast("EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference", jsii.get(self, "pagerdutyAutomationAction"))

    @builtins.property
    @jsii.member(jsii_name="variable")
    def variable(self) -> "EventOrchestrationServiceSetRuleActionsVariableList":
        return typing.cast("EventOrchestrationServiceSetRuleActionsVariableList", jsii.get(self, "variable"))

    @builtins.property
    @jsii.member(jsii_name="annotateInput")
    def annotate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "annotateInput"))

    @builtins.property
    @jsii.member(jsii_name="automationActionInput")
    def automation_action_input(
        self,
    ) -> typing.Optional[EventOrchestrationServiceSetRuleActionsAutomationAction]:
        return typing.cast(typing.Optional[EventOrchestrationServiceSetRuleActionsAutomationAction], jsii.get(self, "automationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="eventActionInput")
    def event_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventActionInput"))

    @builtins.property
    @jsii.member(jsii_name="extractionInput")
    def extraction_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsExtraction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsExtraction]]], jsii.get(self, "extractionInput"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyAutomationActionInput")
    def pagerduty_automation_action_input(
        self,
    ) -> typing.Optional["EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction"]:
        return typing.cast(typing.Optional["EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction"], jsii.get(self, "pagerdutyAutomationActionInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="routeToInput")
    def route_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeToInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="suppressInput")
    def suppress_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "suppressInput"))

    @builtins.property
    @jsii.member(jsii_name="suspendInput")
    def suspend_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "suspendInput"))

    @builtins.property
    @jsii.member(jsii_name="variableInput")
    def variable_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsVariable"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["EventOrchestrationServiceSetRuleActionsVariable"]]], jsii.get(self, "variableInput"))

    @builtins.property
    @jsii.member(jsii_name="annotate")
    def annotate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "annotate"))

    @annotate.setter
    def annotate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "annotate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotate", value)

    @builtins.property
    @jsii.member(jsii_name="eventAction")
    def event_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "eventAction"))

    @event_action.setter
    def event_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "event_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventAction", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="routeTo")
    def route_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeTo"))

    @route_to.setter
    def route_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "route_to").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeTo", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="suppress")
    def suppress(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "suppress"))

    @suppress.setter
    def suppress(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "suppress").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppress", value)

    @builtins.property
    @jsii.member(jsii_name="suspend")
    def suspend(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "suspend"))

    @suspend.setter
    def suspend(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "suspend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suspend", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventOrchestrationServiceSetRuleActions]:
        return typing.cast(typing.Optional[EventOrchestrationServiceSetRuleActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventOrchestrationServiceSetRuleActions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction",
    jsii_struct_bases=[],
    name_mapping={"action_id": "actionId"},
)
class EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction:
    def __init__(self, *, action_id: builtins.str) -> None:
        '''
        :param action_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#action_id EventOrchestrationService#action_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction.__init__)
            check_type(argname="argument action_id", value=action_id, expected_type=type_hints["action_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_id": action_id,
        }

    @builtins.property
    def action_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#action_id EventOrchestrationService#action_id}.'''
        result = self._values.get("action_id")
        assert result is not None, "Required property 'action_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="actionIdInput")
    def action_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="actionId")
    def action_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionId"))

    @action_id.setter
    def action_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference, "action_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction]:
        return typing.cast(typing.Optional[EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsVariable",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path", "type": "type", "value": "value"},
)
class EventOrchestrationServiceSetRuleActionsVariable:
    def __init__(
        self,
        *,
        name: builtins.str,
        path: builtins.str,
        type: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#path EventOrchestrationService#path}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#type EventOrchestrationService#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsVariable.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "path": path,
            "type": type,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#name EventOrchestrationService#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#path EventOrchestrationService#path}.'''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#type EventOrchestrationService#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#value EventOrchestrationService#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleActionsVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceSetRuleActionsVariableList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsVariableList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsVariableList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceSetRuleActionsVariableOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsVariableList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceSetRuleActionsVariableOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsVariable]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsVariable]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleActionsVariable]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleActionsVariableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleActionsVariableOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleActionsVariableOutputReference.__init__)
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
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsVariable, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsVariable, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsVariable, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleActionsVariableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleCondition",
    jsii_struct_bases=[],
    name_mapping={"expression": "expression"},
)
class EventOrchestrationServiceSetRuleCondition:
    def __init__(self, *, expression: builtins.str) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#expression EventOrchestrationService#expression}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleCondition.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
        }

    @builtins.property
    def expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#expression EventOrchestrationService#expression}.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventOrchestrationServiceSetRuleCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class EventOrchestrationServiceSetRuleConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleConditionList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceSetRuleConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceSetRuleConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleConditionOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleConditionOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceSetRuleCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceSetRuleCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceSetRuleCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleList",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "EventOrchestrationServiceSetRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("EventOrchestrationServiceSetRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class EventOrchestrationServiceSetRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.eventOrchestrationService.EventOrchestrationServiceSetRuleOutputReference",
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
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        annotate: typing.Optional[builtins.str] = None,
        automation_action: typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsAutomationAction, typing.Dict[str, typing.Any]]] = None,
        event_action: typing.Optional[builtins.str] = None,
        extraction: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceSetRuleActionsExtraction, typing.Dict[str, typing.Any]]]]] = None,
        pagerduty_automation_action: typing.Optional[typing.Union[EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction, typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[builtins.str] = None,
        route_to: typing.Optional[builtins.str] = None,
        severity: typing.Optional[builtins.str] = None,
        suppress: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        suspend: typing.Optional[jsii.Number] = None,
        variable: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceSetRuleActionsVariable, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param annotate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#annotate EventOrchestrationService#annotate}.
        :param automation_action: automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#automation_action EventOrchestrationService#automation_action}
        :param event_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#event_action EventOrchestrationService#event_action}.
        :param extraction: extraction block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#extraction EventOrchestrationService#extraction}
        :param pagerduty_automation_action: pagerduty_automation_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#pagerduty_automation_action EventOrchestrationService#pagerduty_automation_action}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#priority EventOrchestrationService#priority}.
        :param route_to: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#route_to EventOrchestrationService#route_to}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#severity EventOrchestrationService#severity}.
        :param suppress: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suppress EventOrchestrationService#suppress}.
        :param suspend: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#suspend EventOrchestrationService#suspend}.
        :param variable: variable block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/event_orchestration_service#variable EventOrchestrationService#variable}
        '''
        value = EventOrchestrationServiceSetRuleActions(
            annotate=annotate,
            automation_action=automation_action,
            event_action=event_action,
            extraction=extraction,
            pagerduty_automation_action=pagerduty_automation_action,
            priority=priority,
            route_to=route_to,
            severity=severity,
            suppress=suppress,
            suspend=suspend,
            variable=variable,
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[EventOrchestrationServiceSetRuleCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(EventOrchestrationServiceSetRuleOutputReference.put_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> EventOrchestrationServiceSetRuleActionsOutputReference:
        return typing.cast(EventOrchestrationServiceSetRuleActionsOutputReference, jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> EventOrchestrationServiceSetRuleConditionList:
        return typing.cast(EventOrchestrationServiceSetRuleConditionList, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional[EventOrchestrationServiceSetRuleActions]:
        return typing.cast(typing.Optional[EventOrchestrationServiceSetRuleActions], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[EventOrchestrationServiceSetRuleCondition]]], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[EventOrchestrationServiceSetRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[EventOrchestrationServiceSetRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[EventOrchestrationServiceSetRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(EventOrchestrationServiceSetRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "EventOrchestrationService",
    "EventOrchestrationServiceCatchAll",
    "EventOrchestrationServiceCatchAllActions",
    "EventOrchestrationServiceCatchAllActionsAutomationAction",
    "EventOrchestrationServiceCatchAllActionsAutomationActionHeader",
    "EventOrchestrationServiceCatchAllActionsAutomationActionHeaderList",
    "EventOrchestrationServiceCatchAllActionsAutomationActionHeaderOutputReference",
    "EventOrchestrationServiceCatchAllActionsAutomationActionOutputReference",
    "EventOrchestrationServiceCatchAllActionsAutomationActionParameter",
    "EventOrchestrationServiceCatchAllActionsAutomationActionParameterList",
    "EventOrchestrationServiceCatchAllActionsAutomationActionParameterOutputReference",
    "EventOrchestrationServiceCatchAllActionsExtraction",
    "EventOrchestrationServiceCatchAllActionsExtractionList",
    "EventOrchestrationServiceCatchAllActionsExtractionOutputReference",
    "EventOrchestrationServiceCatchAllActionsOutputReference",
    "EventOrchestrationServiceCatchAllActionsPagerdutyAutomationAction",
    "EventOrchestrationServiceCatchAllActionsPagerdutyAutomationActionOutputReference",
    "EventOrchestrationServiceCatchAllActionsVariable",
    "EventOrchestrationServiceCatchAllActionsVariableList",
    "EventOrchestrationServiceCatchAllActionsVariableOutputReference",
    "EventOrchestrationServiceCatchAllOutputReference",
    "EventOrchestrationServiceConfig",
    "EventOrchestrationServiceSet",
    "EventOrchestrationServiceSetList",
    "EventOrchestrationServiceSetOutputReference",
    "EventOrchestrationServiceSetRule",
    "EventOrchestrationServiceSetRuleActions",
    "EventOrchestrationServiceSetRuleActionsAutomationAction",
    "EventOrchestrationServiceSetRuleActionsAutomationActionHeader",
    "EventOrchestrationServiceSetRuleActionsAutomationActionHeaderList",
    "EventOrchestrationServiceSetRuleActionsAutomationActionHeaderOutputReference",
    "EventOrchestrationServiceSetRuleActionsAutomationActionOutputReference",
    "EventOrchestrationServiceSetRuleActionsAutomationActionParameter",
    "EventOrchestrationServiceSetRuleActionsAutomationActionParameterList",
    "EventOrchestrationServiceSetRuleActionsAutomationActionParameterOutputReference",
    "EventOrchestrationServiceSetRuleActionsExtraction",
    "EventOrchestrationServiceSetRuleActionsExtractionList",
    "EventOrchestrationServiceSetRuleActionsExtractionOutputReference",
    "EventOrchestrationServiceSetRuleActionsOutputReference",
    "EventOrchestrationServiceSetRuleActionsPagerdutyAutomationAction",
    "EventOrchestrationServiceSetRuleActionsPagerdutyAutomationActionOutputReference",
    "EventOrchestrationServiceSetRuleActionsVariable",
    "EventOrchestrationServiceSetRuleActionsVariableList",
    "EventOrchestrationServiceSetRuleActionsVariableOutputReference",
    "EventOrchestrationServiceSetRuleCondition",
    "EventOrchestrationServiceSetRuleConditionList",
    "EventOrchestrationServiceSetRuleConditionOutputReference",
    "EventOrchestrationServiceSetRuleList",
    "EventOrchestrationServiceSetRuleOutputReference",
]

publication.publish()
