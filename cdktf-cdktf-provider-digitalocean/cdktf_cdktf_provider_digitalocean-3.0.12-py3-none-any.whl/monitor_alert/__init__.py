'''
# `digitalocean_monitor_alert`

Refer to the Terraform Registory for docs: [`digitalocean_monitor_alert`](https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert).
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


class MonitorAlert(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.monitorAlert.MonitorAlert",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert digitalocean_monitor_alert}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        alerts: typing.Union["MonitorAlertAlerts", typing.Dict[str, typing.Any]],
        compare: builtins.str,
        description: builtins.str,
        type: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        entities: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert digitalocean_monitor_alert} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alerts: alerts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#alerts MonitorAlert#alerts}
        :param compare: The comparison operator to use for value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#compare MonitorAlert#compare}
        :param description: Description of the alert policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#description MonitorAlert#description}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#type MonitorAlert#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#value MonitorAlert#value}.
        :param window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#window MonitorAlert#window}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#enabled MonitorAlert#enabled}.
        :param entities: The droplets to apply the alert policy to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#entities MonitorAlert#entities}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#id MonitorAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#tags MonitorAlert#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlert.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MonitorAlertConfig(
            alerts=alerts,
            compare=compare,
            description=description,
            type=type,
            value=value,
            window=window,
            enabled=enabled,
            entities=entities,
            id=id,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlerts")
    def put_alerts(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        slack: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertAlertsSlack", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param email: List of email addresses to sent notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#email MonitorAlert#email}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#slack MonitorAlert#slack}
        '''
        value = MonitorAlertAlerts(email=email, slack=slack)

        return typing.cast(None, jsii.invoke(self, "putAlerts", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEntities")
    def reset_entities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntities", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alerts")
    def alerts(self) -> "MonitorAlertAlertsOutputReference":
        return typing.cast("MonitorAlertAlertsOutputReference", jsii.get(self, "alerts"))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="alertsInput")
    def alerts_input(self) -> typing.Optional["MonitorAlertAlerts"]:
        return typing.cast(typing.Optional["MonitorAlertAlerts"], jsii.get(self, "alertsInput"))

    @builtins.property
    @jsii.member(jsii_name="compareInput")
    def compare_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compareInput"))

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
    @jsii.member(jsii_name="entitiesInput")
    def entities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "entitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="windowInput")
    def window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowInput"))

    @builtins.property
    @jsii.member(jsii_name="compare")
    def compare(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compare"))

    @compare.setter
    def compare(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "compare").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compare", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="entities")
    def entities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "entities"))

    @entities.setter
    def entities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "entities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entities", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="window")
    def window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "window"))

    @window.setter
    def window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlert, "window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "window", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.monitorAlert.MonitorAlertAlerts",
    jsii_struct_bases=[],
    name_mapping={"email": "email", "slack": "slack"},
)
class MonitorAlertAlerts:
    def __init__(
        self,
        *,
        email: typing.Optional[typing.Sequence[builtins.str]] = None,
        slack: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertAlertsSlack", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param email: List of email addresses to sent notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#email MonitorAlert#email}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#slack MonitorAlert#slack}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertAlerts.__init__)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
        self._values: typing.Dict[str, typing.Any] = {}
        if email is not None:
            self._values["email"] = email
        if slack is not None:
            self._values["slack"] = slack

    @builtins.property
    def email(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of email addresses to sent notifications to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#email MonitorAlert#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertAlertsSlack"]]]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#slack MonitorAlert#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertAlertsSlack"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertAlerts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertAlertsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.monitorAlert.MonitorAlertAlertsOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertAlertsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MonitorAlertAlertsSlack", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertAlertsOutputReference.put_slack)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> "MonitorAlertAlertsSlackList":
        return typing.cast("MonitorAlertAlertsSlackList", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertAlertsSlack"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MonitorAlertAlertsSlack"]]], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsOutputReference, "email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MonitorAlertAlerts]:
        return typing.cast(typing.Optional[MonitorAlertAlerts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MonitorAlertAlerts]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.monitorAlert.MonitorAlertAlertsSlack",
    jsii_struct_bases=[],
    name_mapping={"channel": "channel", "url": "url"},
)
class MonitorAlertAlertsSlack:
    def __init__(self, *, channel: builtins.str, url: builtins.str) -> None:
        '''
        :param channel: The Slack channel to send alerts to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#channel MonitorAlert#channel}
        :param url: The webhook URL for Slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#url MonitorAlert#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertAlertsSlack.__init__)
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[str, typing.Any] = {
            "channel": channel,
            "url": url,
        }

    @builtins.property
    def channel(self) -> builtins.str:
        '''The Slack channel to send alerts to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#channel MonitorAlert#channel}
        '''
        result = self._values.get("channel")
        assert result is not None, "Required property 'channel' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The webhook URL for Slack.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#url MonitorAlert#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertAlertsSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MonitorAlertAlertsSlackList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.monitorAlert.MonitorAlertAlertsSlackList",
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
            type_hints = typing.get_type_hints(MonitorAlertAlertsSlackList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MonitorAlertAlertsSlackOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertAlertsSlackList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MonitorAlertAlertsSlackOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsSlackList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsSlackList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsSlackList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertAlertsSlack]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertAlertsSlack]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MonitorAlertAlertsSlack]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsSlackList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MonitorAlertAlertsSlackOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.monitorAlert.MonitorAlertAlertsSlackOutputReference",
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
            type_hints = typing.get_type_hints(MonitorAlertAlertsSlackOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsSlackOutputReference, "channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsSlackOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MonitorAlertAlertsSlack, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MonitorAlertAlertsSlack, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MonitorAlertAlertsSlack, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MonitorAlertAlertsSlackOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.monitorAlert.MonitorAlertConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "alerts": "alerts",
        "compare": "compare",
        "description": "description",
        "type": "type",
        "value": "value",
        "window": "window",
        "enabled": "enabled",
        "entities": "entities",
        "id": "id",
        "tags": "tags",
    },
)
class MonitorAlertConfig(cdktf.TerraformMetaArguments):
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
        alerts: typing.Union[MonitorAlertAlerts, typing.Dict[str, typing.Any]],
        compare: builtins.str,
        description: builtins.str,
        type: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        entities: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param alerts: alerts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#alerts MonitorAlert#alerts}
        :param compare: The comparison operator to use for value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#compare MonitorAlert#compare}
        :param description: Description of the alert policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#description MonitorAlert#description}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#type MonitorAlert#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#value MonitorAlert#value}.
        :param window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#window MonitorAlert#window}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#enabled MonitorAlert#enabled}.
        :param entities: The droplets to apply the alert policy to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#entities MonitorAlert#entities}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#id MonitorAlert#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#tags MonitorAlert#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alerts, dict):
            alerts = MonitorAlertAlerts(**alerts)
        if __debug__:
            type_hints = typing.get_type_hints(MonitorAlertConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument alerts", value=alerts, expected_type=type_hints["alerts"])
            check_type(argname="argument compare", value=compare, expected_type=type_hints["compare"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument window", value=window, expected_type=type_hints["window"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument entities", value=entities, expected_type=type_hints["entities"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "alerts": alerts,
            "compare": compare,
            "description": description,
            "type": type,
            "value": value,
            "window": window,
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
        if entities is not None:
            self._values["entities"] = entities
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags

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
    def alerts(self) -> MonitorAlertAlerts:
        '''alerts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#alerts MonitorAlert#alerts}
        '''
        result = self._values.get("alerts")
        assert result is not None, "Required property 'alerts' is missing"
        return typing.cast(MonitorAlertAlerts, result)

    @builtins.property
    def compare(self) -> builtins.str:
        '''The comparison operator to use for value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#compare MonitorAlert#compare}
        '''
        result = self._values.get("compare")
        assert result is not None, "Required property 'compare' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''Description of the alert policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#description MonitorAlert#description}
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#type MonitorAlert#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#value MonitorAlert#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def window(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#window MonitorAlert#window}.'''
        result = self._values.get("window")
        assert result is not None, "Required property 'window' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#enabled MonitorAlert#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def entities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The droplets to apply the alert policy to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#entities MonitorAlert#entities}
        '''
        result = self._values.get("entities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#id MonitorAlert#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/monitor_alert#tags MonitorAlert#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorAlertConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MonitorAlert",
    "MonitorAlertAlerts",
    "MonitorAlertAlertsOutputReference",
    "MonitorAlertAlertsSlack",
    "MonitorAlertAlertsSlackList",
    "MonitorAlertAlertsSlackOutputReference",
    "MonitorAlertConfig",
]

publication.publish()
