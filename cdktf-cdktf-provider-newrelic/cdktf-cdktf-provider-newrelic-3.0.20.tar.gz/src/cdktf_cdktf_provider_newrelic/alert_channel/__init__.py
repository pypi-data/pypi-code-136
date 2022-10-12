'''
# `newrelic_alert_channel`

Refer to the Terraform Registory for docs: [`newrelic_alert_channel`](https://www.terraform.io/docs/providers/newrelic/r/alert_channel).
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


class AlertChannel(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.alertChannel.AlertChannel",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel newrelic_alert_channel}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        config: typing.Optional[typing.Union["AlertChannelConfigA", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel newrelic_alert_channel} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: (Required) The name of the channel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#name AlertChannel#name}
        :param type: (Required) The type of channel. One of: (user, victorops, webhook, email, opsgenie, pagerduty, slack). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#type AlertChannel#type}
        :param account_id: The New Relic account ID where you want to create alert channels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#account_id AlertChannel#account_id}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#config AlertChannel#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#id AlertChannel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AlertChannel.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config_ = AlertChannelConfig(
            name=name,
            type=type,
            account_id=account_id,
            config=config,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config_])

    @jsii.member(jsii_name="putConfig")
    def put_config(
        self,
        *,
        api_key: typing.Optional[builtins.str] = None,
        auth_password: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        auth_username: typing.Optional[builtins.str] = None,
        base_url: typing.Optional[builtins.str] = None,
        channel: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        headers_string: typing.Optional[builtins.str] = None,
        include_json_attachment: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        payload: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        payload_string: typing.Optional[builtins.str] = None,
        payload_type: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        route_key: typing.Optional[builtins.str] = None,
        service_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
        teams: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: The API key for integrating with OpsGenie. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#api_key AlertChannel#api_key}
        :param auth_password: Specifies an authentication password for use with a channel. Supported by the webhook channel type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_password AlertChannel#auth_password}
        :param auth_type: Specifies an authentication method for use with a channel. Supported by the webhook channel type. Only HTTP basic authentication is currently supported via the value BASIC. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_type AlertChannel#auth_type}
        :param auth_username: Specifies an authentication username for use with a channel. Supported by the webhook channel type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_username AlertChannel#auth_username}
        :param base_url: The base URL of the webhook destination. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#base_url AlertChannel#base_url}
        :param channel: The Slack channel to send notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#channel AlertChannel#channel}
        :param headers: A map of key/value pairs that represents extra HTTP headers to be sent along with the webhook payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#headers AlertChannel#headers}
        :param headers_string: Use instead of headers if the desired payload is more complex than a list of key/value pairs (e.g. a set of headers that makes use of nested objects). The value provided should be a valid JSON string with escaped double quotes. Conflicts with headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#headers_string AlertChannel#headers_string}
        :param include_json_attachment: true or false. Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#include_json_attachment AlertChannel#include_json_attachment}
        :param key: The key for integrating with VictorOps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#key AlertChannel#key}
        :param payload: A map of key/value pairs that represents the webhook payload. Must provide payload_type if setting this argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload AlertChannel#payload}
        :param payload_string: Use instead of payload if the desired payload is more complex than a list of key/value pairs (e.g. a payload that makes use of nested objects). The value provided should be a valid JSON string with escaped double quotes. Conflicts with payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload_string AlertChannel#payload_string}
        :param payload_type: Can either be application/json or application/x-www-form-urlencoded. The payload_type argument is required if payload is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload_type AlertChannel#payload_type}
        :param recipients: A set of recipients for targeting notifications. Multiple values are comma separated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#recipients AlertChannel#recipients}
        :param region: The data center region to store your data. Valid values are US and EU. Default is US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#region AlertChannel#region}
        :param route_key: The route key for integrating with VictorOps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#route_key AlertChannel#route_key}
        :param service_key: Specifies the service key for integrating with Pagerduty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#service_key AlertChannel#service_key}
        :param tags: A set of tags for targeting notifications. Multiple values are comma separated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#tags AlertChannel#tags}
        :param teams: A set of teams for targeting notifications. Multiple values are comma separated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#teams AlertChannel#teams}
        :param url: Your organization's Slack URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#url AlertChannel#url}
        :param user_id: The user ID for use with the user channel type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#user_id AlertChannel#user_id}
        '''
        value = AlertChannelConfigA(
            api_key=api_key,
            auth_password=auth_password,
            auth_type=auth_type,
            auth_username=auth_username,
            base_url=base_url,
            channel=channel,
            headers=headers,
            headers_string=headers_string,
            include_json_attachment=include_json_attachment,
            key=key,
            payload=payload,
            payload_string=payload_string,
            payload_type=payload_type,
            recipients=recipients,
            region=region,
            route_key=route_key,
            service_key=service_key,
            tags=tags,
            teams=teams,
            url=url,
            user_id=user_id,
        )

        return typing.cast(None, jsii.invoke(self, "putConfig", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetConfig")
    def reset_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfig", []))

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
    @jsii.member(jsii_name="config")
    def config(self) -> "AlertChannelConfigAOutputReference":
        return typing.cast("AlertChannelConfigAOutputReference", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="configInput")
    def config_input(self) -> typing.Optional["AlertChannelConfigA"]:
        return typing.cast(typing.Optional["AlertChannelConfigA"], jsii.get(self, "configInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannel, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannel, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannel, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannel, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.alertChannel.AlertChannelConfig",
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
        "type": "type",
        "account_id": "accountId",
        "config": "config",
        "id": "id",
    },
)
class AlertChannelConfig(cdktf.TerraformMetaArguments):
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
        type: builtins.str,
        account_id: typing.Optional[jsii.Number] = None,
        config: typing.Optional[typing.Union["AlertChannelConfigA", typing.Dict[str, typing.Any]]] = None,
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
        :param name: (Required) The name of the channel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#name AlertChannel#name}
        :param type: (Required) The type of channel. One of: (user, victorops, webhook, email, opsgenie, pagerduty, slack). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#type AlertChannel#type}
        :param account_id: The New Relic account ID where you want to create alert channels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#account_id AlertChannel#account_id}
        :param config: config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#config AlertChannel#config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#id AlertChannel#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(config, dict):
            config = AlertChannelConfigA(**config)
        if __debug__:
            type_hints = typing.get_type_hints(AlertChannelConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if config is not None:
            self._values["config"] = config
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
    def name(self) -> builtins.str:
        '''(Required) The name of the channel.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#name AlertChannel#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''(Required) The type of channel. One of: (user, victorops, webhook, email, opsgenie, pagerduty, slack).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#type AlertChannel#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The New Relic account ID where you want to create alert channels.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#account_id AlertChannel#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def config(self) -> typing.Optional["AlertChannelConfigA"]:
        '''config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#config AlertChannel#config}
        '''
        result = self._values.get("config")
        return typing.cast(typing.Optional["AlertChannelConfigA"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#id AlertChannel#id}.

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
        return "AlertChannelConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.alertChannel.AlertChannelConfigA",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "auth_password": "authPassword",
        "auth_type": "authType",
        "auth_username": "authUsername",
        "base_url": "baseUrl",
        "channel": "channel",
        "headers": "headers",
        "headers_string": "headersString",
        "include_json_attachment": "includeJsonAttachment",
        "key": "key",
        "payload": "payload",
        "payload_string": "payloadString",
        "payload_type": "payloadType",
        "recipients": "recipients",
        "region": "region",
        "route_key": "routeKey",
        "service_key": "serviceKey",
        "tags": "tags",
        "teams": "teams",
        "url": "url",
        "user_id": "userId",
    },
)
class AlertChannelConfigA:
    def __init__(
        self,
        *,
        api_key: typing.Optional[builtins.str] = None,
        auth_password: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        auth_username: typing.Optional[builtins.str] = None,
        base_url: typing.Optional[builtins.str] = None,
        channel: typing.Optional[builtins.str] = None,
        headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        headers_string: typing.Optional[builtins.str] = None,
        include_json_attachment: typing.Optional[builtins.str] = None,
        key: typing.Optional[builtins.str] = None,
        payload: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        payload_string: typing.Optional[builtins.str] = None,
        payload_type: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        route_key: typing.Optional[builtins.str] = None,
        service_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[builtins.str] = None,
        teams: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        user_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: The API key for integrating with OpsGenie. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#api_key AlertChannel#api_key}
        :param auth_password: Specifies an authentication password for use with a channel. Supported by the webhook channel type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_password AlertChannel#auth_password}
        :param auth_type: Specifies an authentication method for use with a channel. Supported by the webhook channel type. Only HTTP basic authentication is currently supported via the value BASIC. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_type AlertChannel#auth_type}
        :param auth_username: Specifies an authentication username for use with a channel. Supported by the webhook channel type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_username AlertChannel#auth_username}
        :param base_url: The base URL of the webhook destination. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#base_url AlertChannel#base_url}
        :param channel: The Slack channel to send notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#channel AlertChannel#channel}
        :param headers: A map of key/value pairs that represents extra HTTP headers to be sent along with the webhook payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#headers AlertChannel#headers}
        :param headers_string: Use instead of headers if the desired payload is more complex than a list of key/value pairs (e.g. a set of headers that makes use of nested objects). The value provided should be a valid JSON string with escaped double quotes. Conflicts with headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#headers_string AlertChannel#headers_string}
        :param include_json_attachment: true or false. Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#include_json_attachment AlertChannel#include_json_attachment}
        :param key: The key for integrating with VictorOps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#key AlertChannel#key}
        :param payload: A map of key/value pairs that represents the webhook payload. Must provide payload_type if setting this argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload AlertChannel#payload}
        :param payload_string: Use instead of payload if the desired payload is more complex than a list of key/value pairs (e.g. a payload that makes use of nested objects). The value provided should be a valid JSON string with escaped double quotes. Conflicts with payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload_string AlertChannel#payload_string}
        :param payload_type: Can either be application/json or application/x-www-form-urlencoded. The payload_type argument is required if payload is set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload_type AlertChannel#payload_type}
        :param recipients: A set of recipients for targeting notifications. Multiple values are comma separated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#recipients AlertChannel#recipients}
        :param region: The data center region to store your data. Valid values are US and EU. Default is US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#region AlertChannel#region}
        :param route_key: The route key for integrating with VictorOps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#route_key AlertChannel#route_key}
        :param service_key: Specifies the service key for integrating with Pagerduty. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#service_key AlertChannel#service_key}
        :param tags: A set of tags for targeting notifications. Multiple values are comma separated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#tags AlertChannel#tags}
        :param teams: A set of teams for targeting notifications. Multiple values are comma separated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#teams AlertChannel#teams}
        :param url: Your organization's Slack URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#url AlertChannel#url}
        :param user_id: The user ID for use with the user channel type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#user_id AlertChannel#user_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AlertChannelConfigA.__init__)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument auth_password", value=auth_password, expected_type=type_hints["auth_password"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument auth_username", value=auth_username, expected_type=type_hints["auth_username"])
            check_type(argname="argument base_url", value=base_url, expected_type=type_hints["base_url"])
            check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument headers_string", value=headers_string, expected_type=type_hints["headers_string"])
            check_type(argname="argument include_json_attachment", value=include_json_attachment, expected_type=type_hints["include_json_attachment"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument payload_string", value=payload_string, expected_type=type_hints["payload_string"])
            check_type(argname="argument payload_type", value=payload_type, expected_type=type_hints["payload_type"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument route_key", value=route_key, expected_type=type_hints["route_key"])
            check_type(argname="argument service_key", value=service_key, expected_type=type_hints["service_key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if api_key is not None:
            self._values["api_key"] = api_key
        if auth_password is not None:
            self._values["auth_password"] = auth_password
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if auth_username is not None:
            self._values["auth_username"] = auth_username
        if base_url is not None:
            self._values["base_url"] = base_url
        if channel is not None:
            self._values["channel"] = channel
        if headers is not None:
            self._values["headers"] = headers
        if headers_string is not None:
            self._values["headers_string"] = headers_string
        if include_json_attachment is not None:
            self._values["include_json_attachment"] = include_json_attachment
        if key is not None:
            self._values["key"] = key
        if payload is not None:
            self._values["payload"] = payload
        if payload_string is not None:
            self._values["payload_string"] = payload_string
        if payload_type is not None:
            self._values["payload_type"] = payload_type
        if recipients is not None:
            self._values["recipients"] = recipients
        if region is not None:
            self._values["region"] = region
        if route_key is not None:
            self._values["route_key"] = route_key
        if service_key is not None:
            self._values["service_key"] = service_key
        if tags is not None:
            self._values["tags"] = tags
        if teams is not None:
            self._values["teams"] = teams
        if url is not None:
            self._values["url"] = url
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def api_key(self) -> typing.Optional[builtins.str]:
        '''The API key for integrating with OpsGenie.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#api_key AlertChannel#api_key}
        '''
        result = self._values.get("api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_password(self) -> typing.Optional[builtins.str]:
        '''Specifies an authentication password for use with a channel. Supported by the webhook channel type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_password AlertChannel#auth_password}
        '''
        result = self._values.get("auth_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''Specifies an authentication method for use with a channel.

        Supported by the webhook channel type. Only HTTP basic authentication is currently supported via the value BASIC.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_type AlertChannel#auth_type}
        '''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_username(self) -> typing.Optional[builtins.str]:
        '''Specifies an authentication username for use with a channel. Supported by the webhook channel type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#auth_username AlertChannel#auth_username}
        '''
        result = self._values.get("auth_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_url(self) -> typing.Optional[builtins.str]:
        '''The base URL of the webhook destination.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#base_url AlertChannel#base_url}
        '''
        result = self._values.get("base_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel(self) -> typing.Optional[builtins.str]:
        '''The Slack channel to send notifications to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#channel AlertChannel#channel}
        '''
        result = self._values.get("channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key/value pairs that represents extra HTTP headers to be sent along with the webhook payload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#headers AlertChannel#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def headers_string(self) -> typing.Optional[builtins.str]:
        '''Use instead of headers if the desired payload is more complex than a list of key/value pairs (e.g. a set of headers that makes use of nested objects). The value provided should be a valid JSON string with escaped double quotes. Conflicts with headers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#headers_string AlertChannel#headers_string}
        '''
        result = self._values.get("headers_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_json_attachment(self) -> typing.Optional[builtins.str]:
        '''true or false.

        Flag for whether or not to attach a JSON document containing information about the associated alert to the email that is sent to recipients.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#include_json_attachment AlertChannel#include_json_attachment}
        '''
        result = self._values.get("include_json_attachment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The key for integrating with VictorOps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#key AlertChannel#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key/value pairs that represents the webhook payload. Must provide payload_type if setting this argument.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload AlertChannel#payload}
        '''
        result = self._values.get("payload")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def payload_string(self) -> typing.Optional[builtins.str]:
        '''Use instead of payload if the desired payload is more complex than a list of key/value pairs (e.g. a payload that makes use of nested objects). The value provided should be a valid JSON string with escaped double quotes. Conflicts with payload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload_string AlertChannel#payload_string}
        '''
        result = self._values.get("payload_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload_type(self) -> typing.Optional[builtins.str]:
        '''Can either be application/json or application/x-www-form-urlencoded. The payload_type argument is required if payload is set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#payload_type AlertChannel#payload_type}
        '''
        result = self._values.get("payload_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[builtins.str]:
        '''A set of recipients for targeting notifications. Multiple values are comma separated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#recipients AlertChannel#recipients}
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The data center region to store your data. Valid values are US and EU. Default is US.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#region AlertChannel#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_key(self) -> typing.Optional[builtins.str]:
        '''The route key for integrating with VictorOps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#route_key AlertChannel#route_key}
        '''
        result = self._values.get("route_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_key(self) -> typing.Optional[builtins.str]:
        '''Specifies the service key for integrating with Pagerduty.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#service_key AlertChannel#service_key}
        '''
        result = self._values.get("service_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[builtins.str]:
        '''A set of tags for targeting notifications. Multiple values are comma separated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#tags AlertChannel#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def teams(self) -> typing.Optional[builtins.str]:
        '''A set of teams for targeting notifications. Multiple values are comma separated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#teams AlertChannel#teams}
        '''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Your organization's Slack URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#url AlertChannel#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_id(self) -> typing.Optional[builtins.str]:
        '''The user ID for use with the user channel type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/alert_channel#user_id AlertChannel#user_id}
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlertChannelConfigA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AlertChannelConfigAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.alertChannel.AlertChannelConfigAOutputReference",
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
            type_hints = typing.get_type_hints(AlertChannelConfigAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApiKey")
    def reset_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiKey", []))

    @jsii.member(jsii_name="resetAuthPassword")
    def reset_auth_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthPassword", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetAuthUsername")
    def reset_auth_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthUsername", []))

    @jsii.member(jsii_name="resetBaseUrl")
    def reset_base_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBaseUrl", []))

    @jsii.member(jsii_name="resetChannel")
    def reset_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannel", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetHeadersString")
    def reset_headers_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeadersString", []))

    @jsii.member(jsii_name="resetIncludeJsonAttachment")
    def reset_include_json_attachment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeJsonAttachment", []))

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetPayload")
    def reset_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayload", []))

    @jsii.member(jsii_name="resetPayloadString")
    def reset_payload_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayloadString", []))

    @jsii.member(jsii_name="resetPayloadType")
    def reset_payload_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayloadType", []))

    @jsii.member(jsii_name="resetRecipients")
    def reset_recipients(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecipients", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRouteKey")
    def reset_route_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteKey", []))

    @jsii.member(jsii_name="resetServiceKey")
    def reset_service_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceKey", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="authPasswordInput")
    def auth_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authUsernameInput")
    def auth_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="baseUrlInput")
    def base_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "baseUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="channelInput")
    def channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="headersStringInput")
    def headers_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headersStringInput"))

    @builtins.property
    @jsii.member(jsii_name="includeJsonAttachmentInput")
    def include_json_attachment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "includeJsonAttachmentInput"))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadStringInput")
    def payload_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadStringInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadTypeInput")
    def payload_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="recipientsInput")
    def recipients_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recipientsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="routeKeyInput")
    def route_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceKeyInput")
    def service_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="authPassword")
    def auth_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authPassword"))

    @auth_password.setter
    def auth_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "auth_password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authPassword", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "auth_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="authUsername")
    def auth_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authUsername"))

    @auth_username.setter
    def auth_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "auth_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authUsername", value)

    @builtins.property
    @jsii.member(jsii_name="baseUrl")
    def base_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "baseUrl"))

    @base_url.setter
    def base_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "base_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseUrl", value)

    @builtins.property
    @jsii.member(jsii_name="channel")
    def channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channel"))

    @channel.setter
    def channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "channel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channel", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="headersString")
    def headers_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headersString"))

    @headers_string.setter
    def headers_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "headers_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersString", value)

    @builtins.property
    @jsii.member(jsii_name="includeJsonAttachment")
    def include_json_attachment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "includeJsonAttachment"))

    @include_json_attachment.setter
    def include_json_attachment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "include_json_attachment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeJsonAttachment", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="payloadString")
    def payload_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payloadString"))

    @payload_string.setter
    def payload_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "payload_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadString", value)

    @builtins.property
    @jsii.member(jsii_name="payloadType")
    def payload_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payloadType"))

    @payload_type.setter
    def payload_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "payload_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadType", value)

    @builtins.property
    @jsii.member(jsii_name="recipients")
    def recipients(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recipients"))

    @recipients.setter
    def recipients(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "recipients").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipients", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="routeKey")
    def route_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routeKey"))

    @route_key.setter
    def route_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "route_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeKey", value)

    @builtins.property
    @jsii.member(jsii_name="serviceKey")
    def service_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceKey"))

    @service_key.setter
    def service_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "service_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceKey", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teams"))

    @teams.setter
    def teams(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "teams").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teams", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "user_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AlertChannelConfigA]:
        return typing.cast(typing.Optional[AlertChannelConfigA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AlertChannelConfigA]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AlertChannelConfigAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AlertChannel",
    "AlertChannelConfig",
    "AlertChannelConfigA",
    "AlertChannelConfigAOutputReference",
]

publication.publish()
