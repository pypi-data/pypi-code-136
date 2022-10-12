'''
# `datadog_security_monitoring_rule`

Refer to the Terraform Registory for docs: [`datadog_security_monitoring_rule`](https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule).
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


class SecurityMonitoringRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule datadog_security_monitoring_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        case: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleCase", typing.Dict[str, typing.Any]]]],
        message: builtins.str,
        name: builtins.str,
        query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQuery", typing.Dict[str, typing.Any]]]],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleFilter", typing.Dict[str, typing.Any]]]]] = None,
        has_extended_title: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union["SecurityMonitoringRuleOptions", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule datadog_security_monitoring_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param case: case block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#case SecurityMonitoringRule#case}
        :param message: Message for generated signals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#message SecurityMonitoringRule#message}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#name SecurityMonitoringRule#name}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#query SecurityMonitoringRule#query}
        :param enabled: Whether the rule is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#enabled SecurityMonitoringRule#enabled}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#filter SecurityMonitoringRule#filter}
        :param has_extended_title: Whether the notifications include the triggering group-by values in their title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#has_extended_title SecurityMonitoringRule#has_extended_title}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#id SecurityMonitoringRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param options: options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#options SecurityMonitoringRule#options}
        :param tags: Tags for generated signals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#tags SecurityMonitoringRule#tags}
        :param type: The rule type. Valid values are ``log_detection``, ``infrastructure_configuration``, ``workload_security``, ``cloud_configuration``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#type SecurityMonitoringRule#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SecurityMonitoringRuleConfig(
            case=case,
            message=message,
            name=name,
            query=query,
            enabled=enabled,
            filter=filter,
            has_extended_title=has_extended_title,
            id=id,
            options=options,
            tags=tags,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCase")
    def put_case(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleCase", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRule.put_case)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCase", [value]))

    @jsii.member(jsii_name="putFilter")
    def put_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRule.put_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilter", [value]))

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        *,
        keep_alive: jsii.Number,
        max_signal_duration: jsii.Number,
        decrease_criticality_based_on_env: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        detection_method: typing.Optional[builtins.str] = None,
        evaluation_window: typing.Optional[jsii.Number] = None,
        impossible_travel_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsImpossibleTravelOptions", typing.Dict[str, typing.Any]]] = None,
        new_value_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsNewValueOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param keep_alive: Once a signal is generated, the signal will remain “open” if a case is matched at least once within this keep alive window. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#keep_alive SecurityMonitoringRule#keep_alive}
        :param max_signal_duration: A signal will “close” regardless of the query being matched once the time exceeds the maximum duration. This time is calculated from the first seen timestamp. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``, ``43200``, ``86400``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#max_signal_duration SecurityMonitoringRule#max_signal_duration}
        :param decrease_criticality_based_on_env: If true, signals in non-production environments have a lower severity than what is defined by the rule case, which can reduce noise. The decrement is applied when the environment tag of the signal starts with ``staging``, ``test``, or ``dev``. Only available when the rule type is ``log_detection``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#decrease_criticality_based_on_env SecurityMonitoringRule#decrease_criticality_based_on_env}
        :param detection_method: The detection method. Valid values are ``threshold``, ``new_value``, ``anomaly_detection``, ``impossible_travel``, ``hardcoded``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#detection_method SecurityMonitoringRule#detection_method}
        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window and evaluates in real time. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#evaluation_window SecurityMonitoringRule#evaluation_window}
        :param impossible_travel_options: impossible_travel_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#impossible_travel_options SecurityMonitoringRule#impossible_travel_options}
        :param new_value_options: new_value_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#new_value_options SecurityMonitoringRule#new_value_options}
        '''
        value = SecurityMonitoringRuleOptions(
            keep_alive=keep_alive,
            max_signal_duration=max_signal_duration,
            decrease_criticality_based_on_env=decrease_criticality_based_on_env,
            detection_method=detection_method,
            evaluation_window=evaluation_window,
            impossible_travel_options=impossible_travel_options,
            new_value_options=new_value_options,
        )

        return typing.cast(None, jsii.invoke(self, "putOptions", [value]))

    @jsii.member(jsii_name="putQuery")
    def put_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQuery", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRule.put_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQuery", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetHasExtendedTitle")
    def reset_has_extended_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHasExtendedTitle", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="case")
    def case(self) -> "SecurityMonitoringRuleCaseList":
        return typing.cast("SecurityMonitoringRuleCaseList", jsii.get(self, "case"))

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> "SecurityMonitoringRuleFilterList":
        return typing.cast("SecurityMonitoringRuleFilterList", jsii.get(self, "filter"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> "SecurityMonitoringRuleOptionsOutputReference":
        return typing.cast("SecurityMonitoringRuleOptionsOutputReference", jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "SecurityMonitoringRuleQueryList":
        return typing.cast("SecurityMonitoringRuleQueryList", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="caseInput")
    def case_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleCase"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleCase"]]], jsii.get(self, "caseInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="hasExtendedTitleInput")
    def has_extended_title_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hasExtendedTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional["SecurityMonitoringRuleOptions"]:
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptions"], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleQuery"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleQuery"]]], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRule, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="hasExtendedTitle")
    def has_extended_title(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hasExtendedTitle"))

    @has_extended_title.setter
    def has_extended_title(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRule, "has_extended_title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hasExtendedTitle", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRule, "message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRule, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRule, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleCase",
    jsii_struct_bases=[],
    name_mapping={
        "status": "status",
        "condition": "condition",
        "name": "name",
        "notifications": "notifications",
    },
)
class SecurityMonitoringRuleCase:
    def __init__(
        self,
        *,
        status: builtins.str,
        condition: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notifications: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param status: Severity of the Security Signal. Valid values are ``info``, ``low``, ``medium``, ``high``, ``critical``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#status SecurityMonitoringRule#status}
        :param condition: A rule case contains logical operations (``>``,``>=``, ``&&``, ``||``) to determine if a signal should be generated based on the event counts in the previously defined queries. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#condition SecurityMonitoringRule#condition}
        :param name: Name of the case. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#name SecurityMonitoringRule#name}
        :param notifications: Notification targets for each rule case. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#notifications SecurityMonitoringRule#notifications}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleCase.__init__)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notifications", value=notifications, expected_type=type_hints["notifications"])
        self._values: typing.Dict[str, typing.Any] = {
            "status": status,
        }
        if condition is not None:
            self._values["condition"] = condition
        if name is not None:
            self._values["name"] = name
        if notifications is not None:
            self._values["notifications"] = notifications

    @builtins.property
    def status(self) -> builtins.str:
        '''Severity of the Security Signal. Valid values are ``info``, ``low``, ``medium``, ``high``, ``critical``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#status SecurityMonitoringRule#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''A rule case contains logical operations (``>``,``>=``, ``&&``, ``||``) to determine if a signal should be generated based on the event counts in the previously defined queries.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#condition SecurityMonitoringRule#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the case.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notifications(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Notification targets for each rule case.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#notifications SecurityMonitoringRule#notifications}
        '''
        result = self._values.get("notifications")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleCase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleCaseList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleCaseList",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleCaseList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SecurityMonitoringRuleCaseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleCaseList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleCaseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleCase]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleCase]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleCase]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleCaseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleCaseOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleCaseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNotifications")
    def reset_notifications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifications", []))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notificationsInput")
    def notifications_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationsInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseOutputReference, "condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notifications")
    def notifications(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notifications"))

    @notifications.setter
    def notifications(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseOutputReference, "notifications").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifications", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleCase, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleCase, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleCase, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleCaseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "case": "case",
        "message": "message",
        "name": "name",
        "query": "query",
        "enabled": "enabled",
        "filter": "filter",
        "has_extended_title": "hasExtendedTitle",
        "id": "id",
        "options": "options",
        "tags": "tags",
        "type": "type",
    },
)
class SecurityMonitoringRuleConfig(cdktf.TerraformMetaArguments):
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
        case: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleCase, typing.Dict[str, typing.Any]]]],
        message: builtins.str,
        name: builtins.str,
        query: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQuery", typing.Dict[str, typing.Any]]]],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleFilter", typing.Dict[str, typing.Any]]]]] = None,
        has_extended_title: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union["SecurityMonitoringRuleOptions", typing.Dict[str, typing.Any]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param case: case block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#case SecurityMonitoringRule#case}
        :param message: Message for generated signals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#message SecurityMonitoringRule#message}
        :param name: The name of the rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#name SecurityMonitoringRule#name}
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#query SecurityMonitoringRule#query}
        :param enabled: Whether the rule is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#enabled SecurityMonitoringRule#enabled}
        :param filter: filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#filter SecurityMonitoringRule#filter}
        :param has_extended_title: Whether the notifications include the triggering group-by values in their title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#has_extended_title SecurityMonitoringRule#has_extended_title}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#id SecurityMonitoringRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param options: options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#options SecurityMonitoringRule#options}
        :param tags: Tags for generated signals. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#tags SecurityMonitoringRule#tags}
        :param type: The rule type. Valid values are ``log_detection``, ``infrastructure_configuration``, ``workload_security``, ``cloud_configuration``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#type SecurityMonitoringRule#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(options, dict):
            options = SecurityMonitoringRuleOptions(**options)
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument case", value=case, expected_type=type_hints["case"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument has_extended_title", value=has_extended_title, expected_type=type_hints["has_extended_title"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "case": case,
            "message": message,
            "name": name,
            "query": query,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if filter is not None:
            self._values["filter"] = filter
        if has_extended_title is not None:
            self._values["has_extended_title"] = has_extended_title
        if id is not None:
            self._values["id"] = id
        if options is not None:
            self._values["options"] = options
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

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
    def case(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleCase]]:
        '''case block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#case SecurityMonitoringRule#case}
        '''
        result = self._values.get("case")
        assert result is not None, "Required property 'case' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleCase]], result)

    @builtins.property
    def message(self) -> builtins.str:
        '''Message for generated signals.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#message SecurityMonitoringRule#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleQuery"]]:
        '''query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleQuery"]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the rule is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#enabled SecurityMonitoringRule#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]]:
        '''filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#filter SecurityMonitoringRule#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleFilter"]]], result)

    @builtins.property
    def has_extended_title(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the notifications include the triggering group-by values in their title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#has_extended_title SecurityMonitoringRule#has_extended_title}
        '''
        result = self._values.get("has_extended_title")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#id SecurityMonitoringRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional["SecurityMonitoringRuleOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#options SecurityMonitoringRule#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptions"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags for generated signals.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#tags SecurityMonitoringRule#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The rule type. Valid values are ``log_detection``, ``infrastructure_configuration``, ``workload_security``, ``cloud_configuration``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#type SecurityMonitoringRule#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleFilter",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "query": "query"},
)
class SecurityMonitoringRuleFilter:
    def __init__(self, *, action: builtins.str, query: builtins.str) -> None:
        '''
        :param action: The type of filtering action. Valid values are ``require``, ``suppress``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#action SecurityMonitoringRule#action}
        :param query: Query for selecting logs to apply the filtering action. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleFilter.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "query": query,
        }

    @builtins.property
    def action(self) -> builtins.str:
        '''The type of filtering action. Valid values are ``require``, ``suppress``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#action SecurityMonitoringRule#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query(self) -> builtins.str:
        '''Query for selecting logs to apply the filtering action.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleFilterList",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SecurityMonitoringRuleFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleFilterList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleFilterList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleFilterOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleFilterOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleFilterOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "keep_alive": "keepAlive",
        "max_signal_duration": "maxSignalDuration",
        "decrease_criticality_based_on_env": "decreaseCriticalityBasedOnEnv",
        "detection_method": "detectionMethod",
        "evaluation_window": "evaluationWindow",
        "impossible_travel_options": "impossibleTravelOptions",
        "new_value_options": "newValueOptions",
    },
)
class SecurityMonitoringRuleOptions:
    def __init__(
        self,
        *,
        keep_alive: jsii.Number,
        max_signal_duration: jsii.Number,
        decrease_criticality_based_on_env: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        detection_method: typing.Optional[builtins.str] = None,
        evaluation_window: typing.Optional[jsii.Number] = None,
        impossible_travel_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsImpossibleTravelOptions", typing.Dict[str, typing.Any]]] = None,
        new_value_options: typing.Optional[typing.Union["SecurityMonitoringRuleOptionsNewValueOptions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param keep_alive: Once a signal is generated, the signal will remain “open” if a case is matched at least once within this keep alive window. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#keep_alive SecurityMonitoringRule#keep_alive}
        :param max_signal_duration: A signal will “close” regardless of the query being matched once the time exceeds the maximum duration. This time is calculated from the first seen timestamp. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``, ``43200``, ``86400``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#max_signal_duration SecurityMonitoringRule#max_signal_duration}
        :param decrease_criticality_based_on_env: If true, signals in non-production environments have a lower severity than what is defined by the rule case, which can reduce noise. The decrement is applied when the environment tag of the signal starts with ``staging``, ``test``, or ``dev``. Only available when the rule type is ``log_detection``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#decrease_criticality_based_on_env SecurityMonitoringRule#decrease_criticality_based_on_env}
        :param detection_method: The detection method. Valid values are ``threshold``, ``new_value``, ``anomaly_detection``, ``impossible_travel``, ``hardcoded``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#detection_method SecurityMonitoringRule#detection_method}
        :param evaluation_window: A time window is specified to match when at least one of the cases matches true. This is a sliding window and evaluates in real time. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#evaluation_window SecurityMonitoringRule#evaluation_window}
        :param impossible_travel_options: impossible_travel_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#impossible_travel_options SecurityMonitoringRule#impossible_travel_options}
        :param new_value_options: new_value_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#new_value_options SecurityMonitoringRule#new_value_options}
        '''
        if isinstance(impossible_travel_options, dict):
            impossible_travel_options = SecurityMonitoringRuleOptionsImpossibleTravelOptions(**impossible_travel_options)
        if isinstance(new_value_options, dict):
            new_value_options = SecurityMonitoringRuleOptionsNewValueOptions(**new_value_options)
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleOptions.__init__)
            check_type(argname="argument keep_alive", value=keep_alive, expected_type=type_hints["keep_alive"])
            check_type(argname="argument max_signal_duration", value=max_signal_duration, expected_type=type_hints["max_signal_duration"])
            check_type(argname="argument decrease_criticality_based_on_env", value=decrease_criticality_based_on_env, expected_type=type_hints["decrease_criticality_based_on_env"])
            check_type(argname="argument detection_method", value=detection_method, expected_type=type_hints["detection_method"])
            check_type(argname="argument evaluation_window", value=evaluation_window, expected_type=type_hints["evaluation_window"])
            check_type(argname="argument impossible_travel_options", value=impossible_travel_options, expected_type=type_hints["impossible_travel_options"])
            check_type(argname="argument new_value_options", value=new_value_options, expected_type=type_hints["new_value_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "keep_alive": keep_alive,
            "max_signal_duration": max_signal_duration,
        }
        if decrease_criticality_based_on_env is not None:
            self._values["decrease_criticality_based_on_env"] = decrease_criticality_based_on_env
        if detection_method is not None:
            self._values["detection_method"] = detection_method
        if evaluation_window is not None:
            self._values["evaluation_window"] = evaluation_window
        if impossible_travel_options is not None:
            self._values["impossible_travel_options"] = impossible_travel_options
        if new_value_options is not None:
            self._values["new_value_options"] = new_value_options

    @builtins.property
    def keep_alive(self) -> jsii.Number:
        '''Once a signal is generated, the signal will remain “open” if a case is matched at least once within this keep alive window.

        Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#keep_alive SecurityMonitoringRule#keep_alive}
        '''
        result = self._values.get("keep_alive")
        assert result is not None, "Required property 'keep_alive' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_signal_duration(self) -> jsii.Number:
        '''A signal will “close” regardless of the query being matched once the time exceeds the maximum duration.

        This time is calculated from the first seen timestamp. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``, ``10800``, ``21600``, ``43200``, ``86400``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#max_signal_duration SecurityMonitoringRule#max_signal_duration}
        '''
        result = self._values.get("max_signal_duration")
        assert result is not None, "Required property 'max_signal_duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def decrease_criticality_based_on_env(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, signals in non-production environments have a lower severity than what is defined by the rule case, which can reduce noise.

        The decrement is applied when the environment tag of the signal starts with ``staging``, ``test``, or ``dev``. Only available when the rule type is ``log_detection``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#decrease_criticality_based_on_env SecurityMonitoringRule#decrease_criticality_based_on_env}
        '''
        result = self._values.get("decrease_criticality_based_on_env")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def detection_method(self) -> typing.Optional[builtins.str]:
        '''The detection method. Valid values are ``threshold``, ``new_value``, ``anomaly_detection``, ``impossible_travel``, ``hardcoded``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#detection_method SecurityMonitoringRule#detection_method}
        '''
        result = self._values.get("detection_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_window(self) -> typing.Optional[jsii.Number]:
        '''A time window is specified to match when at least one of the cases matches true.

        This is a sliding window and evaluates in real time. Valid values are ``0``, ``60``, ``300``, ``600``, ``900``, ``1800``, ``3600``, ``7200``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#evaluation_window SecurityMonitoringRule#evaluation_window}
        '''
        result = self._values.get("evaluation_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def impossible_travel_options(
        self,
    ) -> typing.Optional["SecurityMonitoringRuleOptionsImpossibleTravelOptions"]:
        '''impossible_travel_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#impossible_travel_options SecurityMonitoringRule#impossible_travel_options}
        '''
        result = self._values.get("impossible_travel_options")
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptionsImpossibleTravelOptions"], result)

    @builtins.property
    def new_value_options(
        self,
    ) -> typing.Optional["SecurityMonitoringRuleOptionsNewValueOptions"]:
        '''new_value_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#new_value_options SecurityMonitoringRule#new_value_options}
        '''
        result = self._values.get("new_value_options")
        return typing.cast(typing.Optional["SecurityMonitoringRuleOptionsNewValueOptions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsImpossibleTravelOptions",
    jsii_struct_bases=[],
    name_mapping={"baseline_user_locations": "baselineUserLocations"},
)
class SecurityMonitoringRuleOptionsImpossibleTravelOptions:
    def __init__(
        self,
        *,
        baseline_user_locations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param baseline_user_locations: If true, signals are suppressed for the first 24 hours. In that time, Datadog learns the user's regular access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#baseline_user_locations SecurityMonitoringRule#baseline_user_locations}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleOptionsImpossibleTravelOptions.__init__)
            check_type(argname="argument baseline_user_locations", value=baseline_user_locations, expected_type=type_hints["baseline_user_locations"])
        self._values: typing.Dict[str, typing.Any] = {}
        if baseline_user_locations is not None:
            self._values["baseline_user_locations"] = baseline_user_locations

    @builtins.property
    def baseline_user_locations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, signals are suppressed for the first 24 hours.

        In that time, Datadog learns the user's regular access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#baseline_user_locations SecurityMonitoringRule#baseline_user_locations}
        '''
        result = self._values.get("baseline_user_locations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleOptionsImpossibleTravelOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBaselineUserLocations")
    def reset_baseline_user_locations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaselineUserLocations", []))

    @builtins.property
    @jsii.member(jsii_name="baselineUserLocationsInput")
    def baseline_user_locations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "baselineUserLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="baselineUserLocations")
    def baseline_user_locations(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "baselineUserLocations"))

    @baseline_user_locations.setter
    def baseline_user_locations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference, "baseline_user_locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baselineUserLocations", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsNewValueOptions",
    jsii_struct_bases=[],
    name_mapping={
        "forget_after": "forgetAfter",
        "learning_duration": "learningDuration",
        "learning_method": "learningMethod",
        "learning_threshold": "learningThreshold",
    },
)
class SecurityMonitoringRuleOptionsNewValueOptions:
    def __init__(
        self,
        *,
        forget_after: jsii.Number,
        learning_duration: typing.Optional[jsii.Number] = None,
        learning_method: typing.Optional[builtins.str] = None,
        learning_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param forget_after: The duration in days after which a learned value is forgotten. Valid values are ``1``, ``2``, ``7``, ``14``, ``21``, ``28``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#forget_after SecurityMonitoringRule#forget_after}
        :param learning_duration: The duration in days during which values are learned, and after which signals will be generated for values that weren't learned. If set to 0, a signal will be generated for all new values after the first value is learned. Valid values are ``0``, ``1``, ``7``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_duration SecurityMonitoringRule#learning_duration}
        :param learning_method: The learning method used to determine when signals should be generated for values that weren't learned. Valid values are ``duration``, ``threshold``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_method SecurityMonitoringRule#learning_method}
        :param learning_threshold: A number of occurrences after which signals are generated for values that weren't learned. Valid values are ``0``, ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_threshold SecurityMonitoringRule#learning_threshold}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleOptionsNewValueOptions.__init__)
            check_type(argname="argument forget_after", value=forget_after, expected_type=type_hints["forget_after"])
            check_type(argname="argument learning_duration", value=learning_duration, expected_type=type_hints["learning_duration"])
            check_type(argname="argument learning_method", value=learning_method, expected_type=type_hints["learning_method"])
            check_type(argname="argument learning_threshold", value=learning_threshold, expected_type=type_hints["learning_threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "forget_after": forget_after,
        }
        if learning_duration is not None:
            self._values["learning_duration"] = learning_duration
        if learning_method is not None:
            self._values["learning_method"] = learning_method
        if learning_threshold is not None:
            self._values["learning_threshold"] = learning_threshold

    @builtins.property
    def forget_after(self) -> jsii.Number:
        '''The duration in days after which a learned value is forgotten.

        Valid values are ``1``, ``2``, ``7``, ``14``, ``21``, ``28``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#forget_after SecurityMonitoringRule#forget_after}
        '''
        result = self._values.get("forget_after")
        assert result is not None, "Required property 'forget_after' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def learning_duration(self) -> typing.Optional[jsii.Number]:
        '''The duration in days during which values are learned, and after which signals will be generated for values that weren't learned.

        If set to 0, a signal will be generated for all new values after the first value is learned. Valid values are ``0``, ``1``, ``7``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_duration SecurityMonitoringRule#learning_duration}
        '''
        result = self._values.get("learning_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def learning_method(self) -> typing.Optional[builtins.str]:
        '''The learning method used to determine when signals should be generated for values that weren't learned.

        Valid values are ``duration``, ``threshold``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_method SecurityMonitoringRule#learning_method}
        '''
        result = self._values.get("learning_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def learning_threshold(self) -> typing.Optional[jsii.Number]:
        '''A number of occurrences after which signals are generated for values that weren't learned. Valid values are ``0``, ``1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_threshold SecurityMonitoringRule#learning_threshold}
        '''
        result = self._values.get("learning_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleOptionsNewValueOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleOptionsNewValueOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsNewValueOptionsOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLearningDuration")
    def reset_learning_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLearningDuration", []))

    @jsii.member(jsii_name="resetLearningMethod")
    def reset_learning_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLearningMethod", []))

    @jsii.member(jsii_name="resetLearningThreshold")
    def reset_learning_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLearningThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="forgetAfterInput")
    def forget_after_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "forgetAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="learningDurationInput")
    def learning_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "learningDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="learningMethodInput")
    def learning_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "learningMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="learningThresholdInput")
    def learning_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "learningThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="forgetAfter")
    def forget_after(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "forgetAfter"))

    @forget_after.setter
    def forget_after(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference, "forget_after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forgetAfter", value)

    @builtins.property
    @jsii.member(jsii_name="learningDuration")
    def learning_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "learningDuration"))

    @learning_duration.setter
    def learning_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference, "learning_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "learningDuration", value)

    @builtins.property
    @jsii.member(jsii_name="learningMethod")
    def learning_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "learningMethod"))

    @learning_method.setter
    def learning_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference, "learning_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "learningMethod", value)

    @builtins.property
    @jsii.member(jsii_name="learningThreshold")
    def learning_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "learningThreshold"))

    @learning_threshold.setter
    def learning_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference, "learning_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "learningThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleOptionsOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putImpossibleTravelOptions")
    def put_impossible_travel_options(
        self,
        *,
        baseline_user_locations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param baseline_user_locations: If true, signals are suppressed for the first 24 hours. In that time, Datadog learns the user's regular access locations. This can be helpful to reduce noise and infer VPN usage or credentialed API access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#baseline_user_locations SecurityMonitoringRule#baseline_user_locations}
        '''
        value = SecurityMonitoringRuleOptionsImpossibleTravelOptions(
            baseline_user_locations=baseline_user_locations
        )

        return typing.cast(None, jsii.invoke(self, "putImpossibleTravelOptions", [value]))

    @jsii.member(jsii_name="putNewValueOptions")
    def put_new_value_options(
        self,
        *,
        forget_after: jsii.Number,
        learning_duration: typing.Optional[jsii.Number] = None,
        learning_method: typing.Optional[builtins.str] = None,
        learning_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param forget_after: The duration in days after which a learned value is forgotten. Valid values are ``1``, ``2``, ``7``, ``14``, ``21``, ``28``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#forget_after SecurityMonitoringRule#forget_after}
        :param learning_duration: The duration in days during which values are learned, and after which signals will be generated for values that weren't learned. If set to 0, a signal will be generated for all new values after the first value is learned. Valid values are ``0``, ``1``, ``7``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_duration SecurityMonitoringRule#learning_duration}
        :param learning_method: The learning method used to determine when signals should be generated for values that weren't learned. Valid values are ``duration``, ``threshold``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_method SecurityMonitoringRule#learning_method}
        :param learning_threshold: A number of occurrences after which signals are generated for values that weren't learned. Valid values are ``0``, ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#learning_threshold SecurityMonitoringRule#learning_threshold}
        '''
        value = SecurityMonitoringRuleOptionsNewValueOptions(
            forget_after=forget_after,
            learning_duration=learning_duration,
            learning_method=learning_method,
            learning_threshold=learning_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putNewValueOptions", [value]))

    @jsii.member(jsii_name="resetDecreaseCriticalityBasedOnEnv")
    def reset_decrease_criticality_based_on_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDecreaseCriticalityBasedOnEnv", []))

    @jsii.member(jsii_name="resetDetectionMethod")
    def reset_detection_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDetectionMethod", []))

    @jsii.member(jsii_name="resetEvaluationWindow")
    def reset_evaluation_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationWindow", []))

    @jsii.member(jsii_name="resetImpossibleTravelOptions")
    def reset_impossible_travel_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImpossibleTravelOptions", []))

    @jsii.member(jsii_name="resetNewValueOptions")
    def reset_new_value_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewValueOptions", []))

    @builtins.property
    @jsii.member(jsii_name="impossibleTravelOptions")
    def impossible_travel_options(
        self,
    ) -> SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference:
        return typing.cast(SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference, jsii.get(self, "impossibleTravelOptions"))

    @builtins.property
    @jsii.member(jsii_name="newValueOptions")
    def new_value_options(
        self,
    ) -> SecurityMonitoringRuleOptionsNewValueOptionsOutputReference:
        return typing.cast(SecurityMonitoringRuleOptionsNewValueOptionsOutputReference, jsii.get(self, "newValueOptions"))

    @builtins.property
    @jsii.member(jsii_name="decreaseCriticalityBasedOnEnvInput")
    def decrease_criticality_based_on_env_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "decreaseCriticalityBasedOnEnvInput"))

    @builtins.property
    @jsii.member(jsii_name="detectionMethodInput")
    def detection_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectionMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationWindowInput")
    def evaluation_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="impossibleTravelOptionsInput")
    def impossible_travel_options_input(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsImpossibleTravelOptions], jsii.get(self, "impossibleTravelOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="keepAliveInput")
    def keep_alive_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keepAliveInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSignalDurationInput")
    def max_signal_duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSignalDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="newValueOptionsInput")
    def new_value_options_input(
        self,
    ) -> typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptionsNewValueOptions], jsii.get(self, "newValueOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="decreaseCriticalityBasedOnEnv")
    def decrease_criticality_based_on_env(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "decreaseCriticalityBasedOnEnv"))

    @decrease_criticality_based_on_env.setter
    def decrease_criticality_based_on_env(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsOutputReference, "decrease_criticality_based_on_env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decreaseCriticalityBasedOnEnv", value)

    @builtins.property
    @jsii.member(jsii_name="detectionMethod")
    def detection_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detectionMethod"))

    @detection_method.setter
    def detection_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsOutputReference, "detection_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectionMethod", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationWindow")
    def evaluation_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "evaluationWindow"))

    @evaluation_window.setter
    def evaluation_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsOutputReference, "evaluation_window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationWindow", value)

    @builtins.property
    @jsii.member(jsii_name="keepAlive")
    def keep_alive(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keepAlive"))

    @keep_alive.setter
    def keep_alive(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsOutputReference, "keep_alive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepAlive", value)

    @builtins.property
    @jsii.member(jsii_name="maxSignalDuration")
    def max_signal_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSignalDuration"))

    @max_signal_duration.setter
    def max_signal_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsOutputReference, "max_signal_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSignalDuration", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SecurityMonitoringRuleOptions]:
        return typing.cast(typing.Optional[SecurityMonitoringRuleOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SecurityMonitoringRuleOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQuery",
    jsii_struct_bases=[],
    name_mapping={
        "query": "query",
        "agent_rule": "agentRule",
        "aggregation": "aggregation",
        "distinct_fields": "distinctFields",
        "group_by_fields": "groupByFields",
        "metric": "metric",
        "metrics": "metrics",
        "name": "name",
    },
)
class SecurityMonitoringRuleQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        agent_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["SecurityMonitoringRuleQueryAgentRule", typing.Dict[str, typing.Any]]]]] = None,
        aggregation: typing.Optional[builtins.str] = None,
        distinct_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        group_by_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        metric: typing.Optional[builtins.str] = None,
        metrics: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param query: Query to run on logs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#query SecurityMonitoringRule#query}
        :param agent_rule: agent_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#agent_rule SecurityMonitoringRule#agent_rule}
        :param aggregation: The aggregation type. Valid values are ``count``, ``cardinality``, ``sum``, ``max``, ``new_value``, ``geo_data``, ``event_count``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#aggregation SecurityMonitoringRule#aggregation}
        :param distinct_fields: Field for which the cardinality is measured. Sent as an array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#distinct_fields SecurityMonitoringRule#distinct_fields}
        :param group_by_fields: Fields to group by. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#group_by_fields SecurityMonitoringRule#group_by_fields}
        :param metric: The target field to aggregate over when using the ``sum``, ``max``, or ``new_value`` aggregations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#metric SecurityMonitoringRule#metric}
        :param metrics: Group of target fields to aggregate over when using the new value aggregations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#metrics SecurityMonitoringRule#metrics}
        :param name: Name of the query. Not compatible with ``new_value`` aggregations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument agent_rule", value=agent_rule, expected_type=type_hints["agent_rule"])
            check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
            check_type(argname="argument distinct_fields", value=distinct_fields, expected_type=type_hints["distinct_fields"])
            check_type(argname="argument group_by_fields", value=group_by_fields, expected_type=type_hints["group_by_fields"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument metrics", value=metrics, expected_type=type_hints["metrics"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if agent_rule is not None:
            self._values["agent_rule"] = agent_rule
        if aggregation is not None:
            self._values["aggregation"] = aggregation
        if distinct_fields is not None:
            self._values["distinct_fields"] = distinct_fields
        if group_by_fields is not None:
            self._values["group_by_fields"] = group_by_fields
        if metric is not None:
            self._values["metric"] = metric
        if metrics is not None:
            self._values["metrics"] = metrics
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def query(self) -> builtins.str:
        '''Query to run on logs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#query SecurityMonitoringRule#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleQueryAgentRule"]]]:
        '''agent_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#agent_rule SecurityMonitoringRule#agent_rule}
        '''
        result = self._values.get("agent_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["SecurityMonitoringRuleQueryAgentRule"]]], result)

    @builtins.property
    def aggregation(self) -> typing.Optional[builtins.str]:
        '''The aggregation type. Valid values are ``count``, ``cardinality``, ``sum``, ``max``, ``new_value``, ``geo_data``, ``event_count``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#aggregation SecurityMonitoringRule#aggregation}
        '''
        result = self._values.get("aggregation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distinct_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Field for which the cardinality is measured. Sent as an array.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#distinct_fields SecurityMonitoringRule#distinct_fields}
        '''
        result = self._values.get("distinct_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def group_by_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fields to group by.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#group_by_fields SecurityMonitoringRule#group_by_fields}
        '''
        result = self._values.get("group_by_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metric(self) -> typing.Optional[builtins.str]:
        '''The target field to aggregate over when using the ``sum``, ``max``, or ``new_value`` aggregations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#metric SecurityMonitoringRule#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metrics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Group of target fields to aggregate over when using the new value aggregations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#metrics SecurityMonitoringRule#metrics}
        '''
        result = self._values.get("metrics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the query. Not compatible with ``new_value`` aggregations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#name SecurityMonitoringRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryAgentRule",
    jsii_struct_bases=[],
    name_mapping={"agent_rule_id": "agentRuleId", "expression": "expression"},
)
class SecurityMonitoringRuleQueryAgentRule:
    def __init__(
        self,
        *,
        agent_rule_id: builtins.str,
        expression: builtins.str,
    ) -> None:
        '''
        :param agent_rule_id: **Deprecated**. It won't be applied anymore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#agent_rule_id SecurityMonitoringRule#agent_rule_id}
        :param expression: **Deprecated**. It won't be applied anymore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#expression SecurityMonitoringRule#expression}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryAgentRule.__init__)
            check_type(argname="argument agent_rule_id", value=agent_rule_id, expected_type=type_hints["agent_rule_id"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        self._values: typing.Dict[str, typing.Any] = {
            "agent_rule_id": agent_rule_id,
            "expression": expression,
        }

    @builtins.property
    def agent_rule_id(self) -> builtins.str:
        '''**Deprecated**. It won't be applied anymore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#agent_rule_id SecurityMonitoringRule#agent_rule_id}
        '''
        result = self._values.get("agent_rule_id")
        assert result is not None, "Required property 'agent_rule_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expression(self) -> builtins.str:
        '''**Deprecated**. It won't be applied anymore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/security_monitoring_rule#expression SecurityMonitoringRule#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityMonitoringRuleQueryAgentRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SecurityMonitoringRuleQueryAgentRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryAgentRuleList",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryAgentRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SecurityMonitoringRuleQueryAgentRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryAgentRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleQueryAgentRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryAgentRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryAgentRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryAgentRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryAgentRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleQueryAgentRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryAgentRuleOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryAgentRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="agentRuleIdInput")
    def agent_rule_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentRuleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="agentRuleId")
    def agent_rule_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "agentRuleId"))

    @agent_rule_id.setter
    def agent_rule_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryAgentRuleOutputReference, "agent_rule_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuleId", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryAgentRuleOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleQueryAgentRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleQueryAgentRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleQueryAgentRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryAgentRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryList",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "SecurityMonitoringRuleQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SecurityMonitoringRuleQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SecurityMonitoringRuleQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.securityMonitoringRule.SecurityMonitoringRuleQueryOutputReference",
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
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAgentRule")
    def put_agent_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[SecurityMonitoringRuleQueryAgentRule, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SecurityMonitoringRuleQueryOutputReference.put_agent_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAgentRule", [value]))

    @jsii.member(jsii_name="resetAgentRule")
    def reset_agent_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAgentRule", []))

    @jsii.member(jsii_name="resetAggregation")
    def reset_aggregation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAggregation", []))

    @jsii.member(jsii_name="resetDistinctFields")
    def reset_distinct_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDistinctFields", []))

    @jsii.member(jsii_name="resetGroupByFields")
    def reset_group_by_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByFields", []))

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @jsii.member(jsii_name="resetMetrics")
    def reset_metrics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetrics", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="agentRule")
    def agent_rule(self) -> SecurityMonitoringRuleQueryAgentRuleList:
        return typing.cast(SecurityMonitoringRuleQueryAgentRuleList, jsii.get(self, "agentRule"))

    @builtins.property
    @jsii.member(jsii_name="agentRuleInput")
    def agent_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[SecurityMonitoringRuleQueryAgentRule]]], jsii.get(self, "agentRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregationInput")
    def aggregation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aggregationInput"))

    @builtins.property
    @jsii.member(jsii_name="distinctFieldsInput")
    def distinct_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "distinctFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByFieldsInput")
    def group_by_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsInput")
    def metrics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "metricsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="aggregation")
    def aggregation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aggregation"))

    @aggregation.setter
    def aggregation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "aggregation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregation", value)

    @builtins.property
    @jsii.member(jsii_name="distinctFields")
    def distinct_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "distinctFields"))

    @distinct_fields.setter
    def distinct_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "distinct_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distinctFields", value)

    @builtins.property
    @jsii.member(jsii_name="groupByFields")
    def group_by_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupByFields"))

    @group_by_fields.setter
    def group_by_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "group_by_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByFields", value)

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metric"))

    @metric.setter
    def metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "metric").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metric", value)

    @builtins.property
    @jsii.member(jsii_name="metrics")
    def metrics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "metrics"))

    @metrics.setter
    def metrics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "metrics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metrics", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SecurityMonitoringRuleQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SecurityMonitoringRuleQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SecurityMonitoringRuleQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SecurityMonitoringRuleQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SecurityMonitoringRule",
    "SecurityMonitoringRuleCase",
    "SecurityMonitoringRuleCaseList",
    "SecurityMonitoringRuleCaseOutputReference",
    "SecurityMonitoringRuleConfig",
    "SecurityMonitoringRuleFilter",
    "SecurityMonitoringRuleFilterList",
    "SecurityMonitoringRuleFilterOutputReference",
    "SecurityMonitoringRuleOptions",
    "SecurityMonitoringRuleOptionsImpossibleTravelOptions",
    "SecurityMonitoringRuleOptionsImpossibleTravelOptionsOutputReference",
    "SecurityMonitoringRuleOptionsNewValueOptions",
    "SecurityMonitoringRuleOptionsNewValueOptionsOutputReference",
    "SecurityMonitoringRuleOptionsOutputReference",
    "SecurityMonitoringRuleQuery",
    "SecurityMonitoringRuleQueryAgentRule",
    "SecurityMonitoringRuleQueryAgentRuleList",
    "SecurityMonitoringRuleQueryAgentRuleOutputReference",
    "SecurityMonitoringRuleQueryList",
    "SecurityMonitoringRuleQueryOutputReference",
]

publication.publish()
