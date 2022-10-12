'''
# `newrelic_synthetics_multilocation_alert_condition`

Refer to the Terraform Registory for docs: [`newrelic_synthetics_multilocation_alert_condition`](https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition).
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


class SyntheticsMultilocationAlertCondition(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMultilocationAlertCondition.SyntheticsMultilocationAlertCondition",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition newrelic_synthetics_multilocation_alert_condition}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        critical: typing.Union["SyntheticsMultilocationAlertConditionCritical", typing.Dict[str, typing.Any]],
        entities: typing.Sequence[builtins.str],
        name: builtins.str,
        policy_id: jsii.Number,
        violation_time_limit_seconds: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        warning: typing.Optional[typing.Union["SyntheticsMultilocationAlertConditionWarning", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition newrelic_synthetics_multilocation_alert_condition} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param critical: critical block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#critical SyntheticsMultilocationAlertCondition#critical}
        :param entities: The GUIDs of the Synthetics monitors to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#entities SyntheticsMultilocationAlertCondition#entities}
        :param name: The title of this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#name SyntheticsMultilocationAlertCondition#name}
        :param policy_id: The ID of the policy where this condition will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#policy_id SyntheticsMultilocationAlertCondition#policy_id}
        :param violation_time_limit_seconds: The maximum number of seconds a violation can remain open before being closed by the system. Must be one of: 0, 3600, 7200, 14400, 28800, 43200, 86400 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#violation_time_limit_seconds SyntheticsMultilocationAlertCondition#violation_time_limit_seconds}
        :param enabled: Set whether to enable the alert condition. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#enabled SyntheticsMultilocationAlertCondition#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#id SyntheticsMultilocationAlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#runbook_url SyntheticsMultilocationAlertCondition#runbook_url}
        :param warning: warning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#warning SyntheticsMultilocationAlertCondition#warning}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsMultilocationAlertCondition.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SyntheticsMultilocationAlertConditionConfig(
            critical=critical,
            entities=entities,
            name=name,
            policy_id=policy_id,
            violation_time_limit_seconds=violation_time_limit_seconds,
            enabled=enabled,
            id=id,
            runbook_url=runbook_url,
            warning=warning,
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
    def put_critical(self, *, threshold: jsii.Number) -> None:
        '''
        :param threshold: The minimum number of monitor locations that must be concurrently failing before a violation is opened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#threshold SyntheticsMultilocationAlertCondition#threshold}
        '''
        value = SyntheticsMultilocationAlertConditionCritical(threshold=threshold)

        return typing.cast(None, jsii.invoke(self, "putCritical", [value]))

    @jsii.member(jsii_name="putWarning")
    def put_warning(self, *, threshold: jsii.Number) -> None:
        '''
        :param threshold: The minimum number of monitor locations that must be concurrently failing before a violation is opened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#threshold SyntheticsMultilocationAlertCondition#threshold}
        '''
        value = SyntheticsMultilocationAlertConditionWarning(threshold=threshold)

        return typing.cast(None, jsii.invoke(self, "putWarning", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRunbookUrl")
    def reset_runbook_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunbookUrl", []))

    @jsii.member(jsii_name="resetWarning")
    def reset_warning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWarning", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="critical")
    def critical(
        self,
    ) -> "SyntheticsMultilocationAlertConditionCriticalOutputReference":
        return typing.cast("SyntheticsMultilocationAlertConditionCriticalOutputReference", jsii.get(self, "critical"))

    @builtins.property
    @jsii.member(jsii_name="warning")
    def warning(self) -> "SyntheticsMultilocationAlertConditionWarningOutputReference":
        return typing.cast("SyntheticsMultilocationAlertConditionWarningOutputReference", jsii.get(self, "warning"))

    @builtins.property
    @jsii.member(jsii_name="criticalInput")
    def critical_input(
        self,
    ) -> typing.Optional["SyntheticsMultilocationAlertConditionCritical"]:
        return typing.cast(typing.Optional["SyntheticsMultilocationAlertConditionCritical"], jsii.get(self, "criticalInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="entitiesInput")
    def entities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyIdInput")
    def policy_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "policyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="runbookUrlInput")
    def runbook_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runbookUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="violationTimeLimitSecondsInput")
    def violation_time_limit_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "violationTimeLimitSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="warningInput")
    def warning_input(
        self,
    ) -> typing.Optional["SyntheticsMultilocationAlertConditionWarning"]:
        return typing.cast(typing.Optional["SyntheticsMultilocationAlertConditionWarning"], jsii.get(self, "warningInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertCondition, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="entities")
    def entities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entities"))

    @entities.setter
    def entities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertCondition, "entities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entities", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertCondition, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertCondition, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "policyId"))

    @policy_id.setter
    def policy_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertCondition, "policy_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyId", value)

    @builtins.property
    @jsii.member(jsii_name="runbookUrl")
    def runbook_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runbookUrl"))

    @runbook_url.setter
    def runbook_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertCondition, "runbook_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runbookUrl", value)

    @builtins.property
    @jsii.member(jsii_name="violationTimeLimitSeconds")
    def violation_time_limit_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "violationTimeLimitSeconds"))

    @violation_time_limit_seconds.setter
    def violation_time_limit_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertCondition, "violation_time_limit_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "violationTimeLimitSeconds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsMultilocationAlertCondition.SyntheticsMultilocationAlertConditionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "critical": "critical",
        "entities": "entities",
        "name": "name",
        "policy_id": "policyId",
        "violation_time_limit_seconds": "violationTimeLimitSeconds",
        "enabled": "enabled",
        "id": "id",
        "runbook_url": "runbookUrl",
        "warning": "warning",
    },
)
class SyntheticsMultilocationAlertConditionConfig(cdktf.TerraformMetaArguments):
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
        critical: typing.Union["SyntheticsMultilocationAlertConditionCritical", typing.Dict[str, typing.Any]],
        entities: typing.Sequence[builtins.str],
        name: builtins.str,
        policy_id: jsii.Number,
        violation_time_limit_seconds: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        runbook_url: typing.Optional[builtins.str] = None,
        warning: typing.Optional[typing.Union["SyntheticsMultilocationAlertConditionWarning", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param critical: critical block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#critical SyntheticsMultilocationAlertCondition#critical}
        :param entities: The GUIDs of the Synthetics monitors to alert on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#entities SyntheticsMultilocationAlertCondition#entities}
        :param name: The title of this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#name SyntheticsMultilocationAlertCondition#name}
        :param policy_id: The ID of the policy where this condition will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#policy_id SyntheticsMultilocationAlertCondition#policy_id}
        :param violation_time_limit_seconds: The maximum number of seconds a violation can remain open before being closed by the system. Must be one of: 0, 3600, 7200, 14400, 28800, 43200, 86400 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#violation_time_limit_seconds SyntheticsMultilocationAlertCondition#violation_time_limit_seconds}
        :param enabled: Set whether to enable the alert condition. Defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#enabled SyntheticsMultilocationAlertCondition#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#id SyntheticsMultilocationAlertCondition#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param runbook_url: Runbook URL to display in notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#runbook_url SyntheticsMultilocationAlertCondition#runbook_url}
        :param warning: warning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#warning SyntheticsMultilocationAlertCondition#warning}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(critical, dict):
            critical = SyntheticsMultilocationAlertConditionCritical(**critical)
        if isinstance(warning, dict):
            warning = SyntheticsMultilocationAlertConditionWarning(**warning)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsMultilocationAlertConditionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            check_type(argname="argument entities", value=entities, expected_type=type_hints["entities"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument violation_time_limit_seconds", value=violation_time_limit_seconds, expected_type=type_hints["violation_time_limit_seconds"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument runbook_url", value=runbook_url, expected_type=type_hints["runbook_url"])
            check_type(argname="argument warning", value=warning, expected_type=type_hints["warning"])
        self._values: typing.Dict[str, typing.Any] = {
            "critical": critical,
            "entities": entities,
            "name": name,
            "policy_id": policy_id,
            "violation_time_limit_seconds": violation_time_limit_seconds,
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
        if id is not None:
            self._values["id"] = id
        if runbook_url is not None:
            self._values["runbook_url"] = runbook_url
        if warning is not None:
            self._values["warning"] = warning

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
    def critical(self) -> "SyntheticsMultilocationAlertConditionCritical":
        '''critical block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#critical SyntheticsMultilocationAlertCondition#critical}
        '''
        result = self._values.get("critical")
        assert result is not None, "Required property 'critical' is missing"
        return typing.cast("SyntheticsMultilocationAlertConditionCritical", result)

    @builtins.property
    def entities(self) -> typing.List[builtins.str]:
        '''The GUIDs of the Synthetics monitors to alert on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#entities SyntheticsMultilocationAlertCondition#entities}
        '''
        result = self._values.get("entities")
        assert result is not None, "Required property 'entities' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The title of this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#name SyntheticsMultilocationAlertCondition#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_id(self) -> jsii.Number:
        '''The ID of the policy where this condition will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#policy_id SyntheticsMultilocationAlertCondition#policy_id}
        '''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def violation_time_limit_seconds(self) -> jsii.Number:
        '''The maximum number of seconds a violation can remain open before being closed by the system.

        Must be one of: 0, 3600, 7200, 14400, 28800, 43200, 86400

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#violation_time_limit_seconds SyntheticsMultilocationAlertCondition#violation_time_limit_seconds}
        '''
        result = self._values.get("violation_time_limit_seconds")
        assert result is not None, "Required property 'violation_time_limit_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set whether to enable the alert condition. Defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#enabled SyntheticsMultilocationAlertCondition#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#id SyntheticsMultilocationAlertCondition#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runbook_url(self) -> typing.Optional[builtins.str]:
        '''Runbook URL to display in notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#runbook_url SyntheticsMultilocationAlertCondition#runbook_url}
        '''
        result = self._values.get("runbook_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def warning(
        self,
    ) -> typing.Optional["SyntheticsMultilocationAlertConditionWarning"]:
        '''warning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#warning SyntheticsMultilocationAlertCondition#warning}
        '''
        result = self._values.get("warning")
        return typing.cast(typing.Optional["SyntheticsMultilocationAlertConditionWarning"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsMultilocationAlertConditionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsMultilocationAlertCondition.SyntheticsMultilocationAlertConditionCritical",
    jsii_struct_bases=[],
    name_mapping={"threshold": "threshold"},
)
class SyntheticsMultilocationAlertConditionCritical:
    def __init__(self, *, threshold: jsii.Number) -> None:
        '''
        :param threshold: The minimum number of monitor locations that must be concurrently failing before a violation is opened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#threshold SyntheticsMultilocationAlertCondition#threshold}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsMultilocationAlertConditionCritical.__init__)
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold": threshold,
        }

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''The minimum number of monitor locations that must be concurrently failing before a violation is opened.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#threshold SyntheticsMultilocationAlertCondition#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsMultilocationAlertConditionCritical(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsMultilocationAlertConditionCriticalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMultilocationAlertCondition.SyntheticsMultilocationAlertConditionCriticalOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsMultilocationAlertConditionCriticalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertConditionCriticalOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsMultilocationAlertConditionCritical]:
        return typing.cast(typing.Optional[SyntheticsMultilocationAlertConditionCritical], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsMultilocationAlertConditionCritical],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertConditionCriticalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsMultilocationAlertCondition.SyntheticsMultilocationAlertConditionWarning",
    jsii_struct_bases=[],
    name_mapping={"threshold": "threshold"},
)
class SyntheticsMultilocationAlertConditionWarning:
    def __init__(self, *, threshold: jsii.Number) -> None:
        '''
        :param threshold: The minimum number of monitor locations that must be concurrently failing before a violation is opened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#threshold SyntheticsMultilocationAlertCondition#threshold}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsMultilocationAlertConditionWarning.__init__)
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "threshold": threshold,
        }

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''The minimum number of monitor locations that must be concurrently failing before a violation is opened.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_multilocation_alert_condition#threshold SyntheticsMultilocationAlertCondition#threshold}
        '''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsMultilocationAlertConditionWarning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsMultilocationAlertConditionWarningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMultilocationAlertCondition.SyntheticsMultilocationAlertConditionWarningOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsMultilocationAlertConditionWarningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertConditionWarningOutputReference, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsMultilocationAlertConditionWarning]:
        return typing.cast(typing.Optional[SyntheticsMultilocationAlertConditionWarning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsMultilocationAlertConditionWarning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMultilocationAlertConditionWarningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SyntheticsMultilocationAlertCondition",
    "SyntheticsMultilocationAlertConditionConfig",
    "SyntheticsMultilocationAlertConditionCritical",
    "SyntheticsMultilocationAlertConditionCriticalOutputReference",
    "SyntheticsMultilocationAlertConditionWarning",
    "SyntheticsMultilocationAlertConditionWarningOutputReference",
]

publication.publish()
