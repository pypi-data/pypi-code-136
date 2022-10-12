'''
# `azurerm_monitor_smart_detector_alert_rule`

Refer to the Terraform Registory for docs: [`azurerm_monitor_smart_detector_alert_rule`](https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule).
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


class MonitorSmartDetectorAlertRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorSmartDetectorAlertRule.MonitorSmartDetectorAlertRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule azurerm_monitor_smart_detector_alert_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        action_group: typing.Union["MonitorSmartDetectorAlertRuleActionGroup", typing.Dict[str, typing.Any]],
        detector_type: builtins.str,
        frequency: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        scope_resource_ids: typing.Sequence[builtins.str],
        severity: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        throttling_duration: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MonitorSmartDetectorAlertRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule azurerm_monitor_smart_detector_alert_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action_group: action_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#action_group MonitorSmartDetectorAlertRule#action_group}
        :param detector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#detector_type MonitorSmartDetectorAlertRule#detector_type}.
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#frequency MonitorSmartDetectorAlertRule#frequency}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#name MonitorSmartDetectorAlertRule#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#resource_group_name MonitorSmartDetectorAlertRule#resource_group_name}.
        :param scope_resource_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#scope_resource_ids MonitorSmartDetectorAlertRule#scope_resource_ids}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#severity MonitorSmartDetectorAlertRule#severity}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#description MonitorSmartDetectorAlertRule#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#enabled MonitorSmartDetectorAlertRule#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#id MonitorSmartDetectorAlertRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#tags MonitorSmartDetectorAlertRule#tags}.
        :param throttling_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#throttling_duration MonitorSmartDetectorAlertRule#throttling_duration}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#timeouts MonitorSmartDetectorAlertRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorSmartDetectorAlertRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorSmartDetectorAlertRuleConfig(
            action_group=action_group,
            detector_type=detector_type,
            frequency=frequency,
            name=name,
            resource_group_name=resource_group_name,
            scope_resource_ids=scope_resource_ids,
            severity=severity,
            description=description,
            enabled=enabled,
            id=id,
            tags=tags,
            throttling_duration=throttling_duration,
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

    @jsii.member(jsii_name="putActionGroup")
    def put_action_group(
        self,
        *,
        ids: typing.Sequence[builtins.str],
        email_subject: typing.Optional[builtins.str] = None,
        webhook_payload: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#ids MonitorSmartDetectorAlertRule#ids}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#email_subject MonitorSmartDetectorAlertRule#email_subject}.
        :param webhook_payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#webhook_payload MonitorSmartDetectorAlertRule#webhook_payload}.
        '''
        value = MonitorSmartDetectorAlertRuleActionGroup(
            ids=ids, email_subject=email_subject, webhook_payload=webhook_payload
        )

        return typing.cast(None, jsii.invoke(self, "putActionGroup", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#create MonitorSmartDetectorAlertRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#delete MonitorSmartDetectorAlertRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#read MonitorSmartDetectorAlertRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#update MonitorSmartDetectorAlertRule#update}.
        '''
        value = MonitorSmartDetectorAlertRuleTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetThrottlingDuration")
    def reset_throttling_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThrottlingDuration", []))

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
    @jsii.member(jsii_name="actionGroup")
    def action_group(self) -> "MonitorSmartDetectorAlertRuleActionGroupOutputReference":
        return typing.cast("MonitorSmartDetectorAlertRuleActionGroupOutputReference", jsii.get(self, "actionGroup"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MonitorSmartDetectorAlertRuleTimeoutsOutputReference":
        return typing.cast("MonitorSmartDetectorAlertRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="actionGroupInput")
    def action_group_input(
        self,
    ) -> typing.Optional["MonitorSmartDetectorAlertRuleActionGroup"]:
        return typing.cast(typing.Optional["MonitorSmartDetectorAlertRuleActionGroup"], jsii.get(self, "actionGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="detectorTypeInput")
    def detector_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

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
    @jsii.member(jsii_name="scopeResourceIdsInput")
    def scope_resource_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scopeResourceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="throttlingDurationInput")
    def throttling_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "throttlingDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MonitorSmartDetectorAlertRuleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MonitorSmartDetectorAlertRuleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="detectorType")
    def detector_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "detectorType"))

    @detector_type.setter
    def detector_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "detector_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorType", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="scopeResourceIds")
    def scope_resource_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scopeResourceIds"))

    @scope_resource_ids.setter
    def scope_resource_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "scope_resource_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeResourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "severity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="throttlingDuration")
    def throttling_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "throttlingDuration"))

    @throttling_duration.setter
    def throttling_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRule, "throttling_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "throttlingDuration", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorSmartDetectorAlertRule.MonitorSmartDetectorAlertRuleActionGroup",
    jsii_struct_bases=[],
    name_mapping={
        "ids": "ids",
        "email_subject": "emailSubject",
        "webhook_payload": "webhookPayload",
    },
)
class MonitorSmartDetectorAlertRuleActionGroup:
    def __init__(
        self,
        *,
        ids: typing.Sequence[builtins.str],
        email_subject: typing.Optional[builtins.str] = None,
        webhook_payload: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#ids MonitorSmartDetectorAlertRule#ids}.
        :param email_subject: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#email_subject MonitorSmartDetectorAlertRule#email_subject}.
        :param webhook_payload: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#webhook_payload MonitorSmartDetectorAlertRule#webhook_payload}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorSmartDetectorAlertRuleActionGroup.__init__)
            check_type(argname="argument ids", value=ids, expected_type=type_hints["ids"])
            check_type(argname="argument email_subject", value=email_subject, expected_type=type_hints["email_subject"])
            check_type(argname="argument webhook_payload", value=webhook_payload, expected_type=type_hints["webhook_payload"])
        self._values: typing.Dict[str, typing.Any] = {
            "ids": ids,
        }
        if email_subject is not None:
            self._values["email_subject"] = email_subject
        if webhook_payload is not None:
            self._values["webhook_payload"] = webhook_payload

    @builtins.property
    def ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#ids MonitorSmartDetectorAlertRule#ids}.'''
        result = self._values.get("ids")
        assert result is not None, "Required property 'ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def email_subject(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#email_subject MonitorSmartDetectorAlertRule#email_subject}.'''
        result = self._values.get("email_subject")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def webhook_payload(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#webhook_payload MonitorSmartDetectorAlertRule#webhook_payload}.'''
        result = self._values.get("webhook_payload")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorSmartDetectorAlertRuleActionGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorSmartDetectorAlertRuleActionGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorSmartDetectorAlertRule.MonitorSmartDetectorAlertRuleActionGroupOutputReference",
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
            type_hints = typing.get_type_hints(MonitorSmartDetectorAlertRuleActionGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEmailSubject")
    def reset_email_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailSubject", []))

    @jsii.member(jsii_name="resetWebhookPayload")
    def reset_webhook_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhookPayload", []))

    @builtins.property
    @jsii.member(jsii_name="emailSubjectInput")
    def email_subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailSubjectInput"))

    @builtins.property
    @jsii.member(jsii_name="idsInput")
    def ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idsInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookPayloadInput")
    def webhook_payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webhookPayloadInput"))

    @builtins.property
    @jsii.member(jsii_name="emailSubject")
    def email_subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailSubject"))

    @email_subject.setter
    def email_subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleActionGroupOutputReference, "email_subject").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailSubject", value)

    @builtins.property
    @jsii.member(jsii_name="ids")
    def ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ids"))

    @ids.setter
    def ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleActionGroupOutputReference, "ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ids", value)

    @builtins.property
    @jsii.member(jsii_name="webhookPayload")
    def webhook_payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webhookPayload"))

    @webhook_payload.setter
    def webhook_payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleActionGroupOutputReference, "webhook_payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webhookPayload", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MonitorSmartDetectorAlertRuleActionGroup]:
        return typing.cast(typing.Optional[MonitorSmartDetectorAlertRuleActionGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MonitorSmartDetectorAlertRuleActionGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleActionGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorSmartDetectorAlertRule.MonitorSmartDetectorAlertRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action_group": "actionGroup",
        "detector_type": "detectorType",
        "frequency": "frequency",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "scope_resource_ids": "scopeResourceIds",
        "severity": "severity",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "tags": "tags",
        "throttling_duration": "throttlingDuration",
        "timeouts": "timeouts",
    },
)
class MonitorSmartDetectorAlertRuleConfig(cdktf.TerraformMetaArguments):
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
        action_group: typing.Union[MonitorSmartDetectorAlertRuleActionGroup, typing.Dict[str, typing.Any]],
        detector_type: builtins.str,
        frequency: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        scope_resource_ids: typing.Sequence[builtins.str],
        severity: builtins.str,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        throttling_duration: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["MonitorSmartDetectorAlertRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action_group: action_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#action_group MonitorSmartDetectorAlertRule#action_group}
        :param detector_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#detector_type MonitorSmartDetectorAlertRule#detector_type}.
        :param frequency: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#frequency MonitorSmartDetectorAlertRule#frequency}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#name MonitorSmartDetectorAlertRule#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#resource_group_name MonitorSmartDetectorAlertRule#resource_group_name}.
        :param scope_resource_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#scope_resource_ids MonitorSmartDetectorAlertRule#scope_resource_ids}.
        :param severity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#severity MonitorSmartDetectorAlertRule#severity}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#description MonitorSmartDetectorAlertRule#description}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#enabled MonitorSmartDetectorAlertRule#enabled}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#id MonitorSmartDetectorAlertRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#tags MonitorSmartDetectorAlertRule#tags}.
        :param throttling_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#throttling_duration MonitorSmartDetectorAlertRule#throttling_duration}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#timeouts MonitorSmartDetectorAlertRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(action_group, dict):
            action_group = MonitorSmartDetectorAlertRuleActionGroup(**action_group)
        if isinstance(timeouts, dict):
            timeouts = MonitorSmartDetectorAlertRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorSmartDetectorAlertRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action_group", value=action_group, expected_type=type_hints["action_group"])
            check_type(argname="argument detector_type", value=detector_type, expected_type=type_hints["detector_type"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument scope_resource_ids", value=scope_resource_ids, expected_type=type_hints["scope_resource_ids"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument throttling_duration", value=throttling_duration, expected_type=type_hints["throttling_duration"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "action_group": action_group,
            "detector_type": detector_type,
            "frequency": frequency,
            "name": name,
            "resource_group_name": resource_group_name,
            "scope_resource_ids": scope_resource_ids,
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
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if throttling_duration is not None:
            self._values["throttling_duration"] = throttling_duration
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
    def action_group(self) -> MonitorSmartDetectorAlertRuleActionGroup:
        '''action_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#action_group MonitorSmartDetectorAlertRule#action_group}
        '''
        result = self._values.get("action_group")
        assert result is not None, "Required property 'action_group' is missing"
        return typing.cast(MonitorSmartDetectorAlertRuleActionGroup, result)

    @builtins.property
    def detector_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#detector_type MonitorSmartDetectorAlertRule#detector_type}.'''
        result = self._values.get("detector_type")
        assert result is not None, "Required property 'detector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def frequency(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#frequency MonitorSmartDetectorAlertRule#frequency}.'''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#name MonitorSmartDetectorAlertRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#resource_group_name MonitorSmartDetectorAlertRule#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope_resource_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#scope_resource_ids MonitorSmartDetectorAlertRule#scope_resource_ids}.'''
        result = self._values.get("scope_resource_ids")
        assert result is not None, "Required property 'scope_resource_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def severity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#severity MonitorSmartDetectorAlertRule#severity}.'''
        result = self._values.get("severity")
        assert result is not None, "Required property 'severity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#description MonitorSmartDetectorAlertRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#enabled MonitorSmartDetectorAlertRule#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#id MonitorSmartDetectorAlertRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#tags MonitorSmartDetectorAlertRule#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def throttling_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#throttling_duration MonitorSmartDetectorAlertRule#throttling_duration}.'''
        result = self._values.get("throttling_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MonitorSmartDetectorAlertRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#timeouts MonitorSmartDetectorAlertRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MonitorSmartDetectorAlertRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorSmartDetectorAlertRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.monitorSmartDetectorAlertRule.MonitorSmartDetectorAlertRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class MonitorSmartDetectorAlertRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#create MonitorSmartDetectorAlertRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#delete MonitorSmartDetectorAlertRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#read MonitorSmartDetectorAlertRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#update MonitorSmartDetectorAlertRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorSmartDetectorAlertRuleTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#create MonitorSmartDetectorAlertRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#delete MonitorSmartDetectorAlertRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#read MonitorSmartDetectorAlertRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/monitor_smart_detector_alert_rule#update MonitorSmartDetectorAlertRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorSmartDetectorAlertRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorSmartDetectorAlertRuleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.monitorSmartDetectorAlertRule.MonitorSmartDetectorAlertRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorSmartDetectorAlertRuleTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorSmartDetectorAlertRuleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorSmartDetectorAlertRuleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorSmartDetectorAlertRuleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorSmartDetectorAlertRuleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MonitorSmartDetectorAlertRule",
    "MonitorSmartDetectorAlertRuleActionGroup",
    "MonitorSmartDetectorAlertRuleActionGroupOutputReference",
    "MonitorSmartDetectorAlertRuleConfig",
    "MonitorSmartDetectorAlertRuleTimeouts",
    "MonitorSmartDetectorAlertRuleTimeoutsOutputReference",
]

publication.publish()
