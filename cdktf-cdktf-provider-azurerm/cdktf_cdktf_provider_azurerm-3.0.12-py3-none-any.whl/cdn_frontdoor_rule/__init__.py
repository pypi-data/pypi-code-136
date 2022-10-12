'''
# `azurerm_cdn_frontdoor_rule`

Refer to the Terraform Registory for docs: [`azurerm_cdn_frontdoor_rule`](https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule).
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


class CdnFrontdoorRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule azurerm_cdn_frontdoor_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        actions: typing.Union["CdnFrontdoorRuleActions", typing.Dict[str, typing.Any]],
        cdn_frontdoor_rule_set_id: builtins.str,
        name: builtins.str,
        order: jsii.Number,
        behavior_on_match: typing.Optional[builtins.str] = None,
        conditions: typing.Optional[typing.Union["CdnFrontdoorRuleConditions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule azurerm_cdn_frontdoor_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#actions CdnFrontdoorRule#actions}
        :param cdn_frontdoor_rule_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cdn_frontdoor_rule_set_id CdnFrontdoorRule#cdn_frontdoor_rule_set_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#name CdnFrontdoorRule#name}.
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#order CdnFrontdoorRule#order}.
        :param behavior_on_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#behavior_on_match CdnFrontdoorRule#behavior_on_match}.
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#conditions CdnFrontdoorRule#conditions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#id CdnFrontdoorRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#timeouts CdnFrontdoorRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CdnFrontdoorRuleConfig(
            actions=actions,
            cdn_frontdoor_rule_set_id=cdn_frontdoor_rule_set_id,
            name=name,
            order=order,
            behavior_on_match=behavior_on_match,
            conditions=conditions,
            id=id,
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

    @jsii.member(jsii_name="putActions")
    def put_actions(
        self,
        *,
        request_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleActionsRequestHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        response_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleActionsResponseHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        route_configuration_override_action: typing.Optional[typing.Union["CdnFrontdoorRuleActionsRouteConfigurationOverrideAction", typing.Dict[str, typing.Any]]] = None,
        url_redirect_action: typing.Optional[typing.Union["CdnFrontdoorRuleActionsUrlRedirectAction", typing.Dict[str, typing.Any]]] = None,
        url_rewrite_action: typing.Optional[typing.Union["CdnFrontdoorRuleActionsUrlRewriteAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param request_header_action: request_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_header_action CdnFrontdoorRule#request_header_action}
        :param response_header_action: response_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#response_header_action CdnFrontdoorRule#response_header_action}
        :param route_configuration_override_action: route_configuration_override_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#route_configuration_override_action CdnFrontdoorRule#route_configuration_override_action}
        :param url_redirect_action: url_redirect_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_redirect_action CdnFrontdoorRule#url_redirect_action}
        :param url_rewrite_action: url_rewrite_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_rewrite_action CdnFrontdoorRule#url_rewrite_action}
        '''
        value = CdnFrontdoorRuleActions(
            request_header_action=request_header_action,
            response_header_action=response_header_action,
            route_configuration_override_action=route_configuration_override_action,
            url_redirect_action=url_redirect_action,
            url_rewrite_action=url_rewrite_action,
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putConditions")
    def put_conditions(
        self,
        *,
        client_port_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsClientPortCondition", typing.Dict[str, typing.Any]]]]] = None,
        cookies_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsCookiesCondition", typing.Dict[str, typing.Any]]]]] = None,
        host_name_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsHostNameCondition", typing.Dict[str, typing.Any]]]]] = None,
        http_version_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsHttpVersionCondition", typing.Dict[str, typing.Any]]]]] = None,
        is_device_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsIsDeviceCondition", typing.Dict[str, typing.Any]]]]] = None,
        post_args_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsPostArgsCondition", typing.Dict[str, typing.Any]]]]] = None,
        query_string_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsQueryStringCondition", typing.Dict[str, typing.Any]]]]] = None,
        remote_address_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRemoteAddressCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_body_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestBodyCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_header_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestHeaderCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_method_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestMethodCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_scheme_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestSchemeCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_uri_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestUriCondition", typing.Dict[str, typing.Any]]]]] = None,
        server_port_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsServerPortCondition", typing.Dict[str, typing.Any]]]]] = None,
        socket_address_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsSocketAddressCondition", typing.Dict[str, typing.Any]]]]] = None,
        ssl_protocol_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsSslProtocolCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_file_extension_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlFileExtensionCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_filename_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlFilenameCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_path_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlPathCondition", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param client_port_condition: client_port_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#client_port_condition CdnFrontdoorRule#client_port_condition}
        :param cookies_condition: cookies_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cookies_condition CdnFrontdoorRule#cookies_condition}
        :param host_name_condition: host_name_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#host_name_condition CdnFrontdoorRule#host_name_condition}
        :param http_version_condition: http_version_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#http_version_condition CdnFrontdoorRule#http_version_condition}
        :param is_device_condition: is_device_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#is_device_condition CdnFrontdoorRule#is_device_condition}
        :param post_args_condition: post_args_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#post_args_condition CdnFrontdoorRule#post_args_condition}
        :param query_string_condition: query_string_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_condition CdnFrontdoorRule#query_string_condition}
        :param remote_address_condition: remote_address_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#remote_address_condition CdnFrontdoorRule#remote_address_condition}
        :param request_body_condition: request_body_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_body_condition CdnFrontdoorRule#request_body_condition}
        :param request_header_condition: request_header_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_header_condition CdnFrontdoorRule#request_header_condition}
        :param request_method_condition: request_method_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_method_condition CdnFrontdoorRule#request_method_condition}
        :param request_scheme_condition: request_scheme_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_scheme_condition CdnFrontdoorRule#request_scheme_condition}
        :param request_uri_condition: request_uri_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_uri_condition CdnFrontdoorRule#request_uri_condition}
        :param server_port_condition: server_port_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#server_port_condition CdnFrontdoorRule#server_port_condition}
        :param socket_address_condition: socket_address_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#socket_address_condition CdnFrontdoorRule#socket_address_condition}
        :param ssl_protocol_condition: ssl_protocol_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#ssl_protocol_condition CdnFrontdoorRule#ssl_protocol_condition}
        :param url_file_extension_condition: url_file_extension_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_file_extension_condition CdnFrontdoorRule#url_file_extension_condition}
        :param url_filename_condition: url_filename_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_filename_condition CdnFrontdoorRule#url_filename_condition}
        :param url_path_condition: url_path_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_path_condition CdnFrontdoorRule#url_path_condition}
        '''
        value = CdnFrontdoorRuleConditions(
            client_port_condition=client_port_condition,
            cookies_condition=cookies_condition,
            host_name_condition=host_name_condition,
            http_version_condition=http_version_condition,
            is_device_condition=is_device_condition,
            post_args_condition=post_args_condition,
            query_string_condition=query_string_condition,
            remote_address_condition=remote_address_condition,
            request_body_condition=request_body_condition,
            request_header_condition=request_header_condition,
            request_method_condition=request_method_condition,
            request_scheme_condition=request_scheme_condition,
            request_uri_condition=request_uri_condition,
            server_port_condition=server_port_condition,
            socket_address_condition=socket_address_condition,
            ssl_protocol_condition=ssl_protocol_condition,
            url_file_extension_condition=url_file_extension_condition,
            url_filename_condition=url_filename_condition,
            url_path_condition=url_path_condition,
        )

        return typing.cast(None, jsii.invoke(self, "putConditions", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#create CdnFrontdoorRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#delete CdnFrontdoorRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#read CdnFrontdoorRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#update CdnFrontdoorRule#update}.
        '''
        value = CdnFrontdoorRuleTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBehaviorOnMatch")
    def reset_behavior_on_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBehaviorOnMatch", []))

    @jsii.member(jsii_name="resetConditions")
    def reset_conditions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConditions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="actions")
    def actions(self) -> "CdnFrontdoorRuleActionsOutputReference":
        return typing.cast("CdnFrontdoorRuleActionsOutputReference", jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorRuleSetName")
    def cdn_frontdoor_rule_set_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorRuleSetName"))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(self) -> "CdnFrontdoorRuleConditionsOutputReference":
        return typing.cast("CdnFrontdoorRuleConditionsOutputReference", jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CdnFrontdoorRuleTimeoutsOutputReference":
        return typing.cast("CdnFrontdoorRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional["CdnFrontdoorRuleActions"]:
        return typing.cast(typing.Optional["CdnFrontdoorRuleActions"], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="behaviorOnMatchInput")
    def behavior_on_match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "behaviorOnMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorRuleSetIdInput")
    def cdn_frontdoor_rule_set_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorRuleSetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionsInput")
    def conditions_input(self) -> typing.Optional["CdnFrontdoorRuleConditions"]:
        return typing.cast(typing.Optional["CdnFrontdoorRuleConditions"], jsii.get(self, "conditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CdnFrontdoorRuleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CdnFrontdoorRuleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="behaviorOnMatch")
    def behavior_on_match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "behaviorOnMatch"))

    @behavior_on_match.setter
    def behavior_on_match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRule, "behavior_on_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "behaviorOnMatch", value)

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorRuleSetId")
    def cdn_frontdoor_rule_set_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorRuleSetId"))

    @cdn_frontdoor_rule_set_id.setter
    def cdn_frontdoor_rule_set_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRule, "cdn_frontdoor_rule_set_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorRuleSetId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "order"))

    @order.setter
    def order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRule, "order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActions",
    jsii_struct_bases=[],
    name_mapping={
        "request_header_action": "requestHeaderAction",
        "response_header_action": "responseHeaderAction",
        "route_configuration_override_action": "routeConfigurationOverrideAction",
        "url_redirect_action": "urlRedirectAction",
        "url_rewrite_action": "urlRewriteAction",
    },
)
class CdnFrontdoorRuleActions:
    def __init__(
        self,
        *,
        request_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleActionsRequestHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        response_header_action: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleActionsResponseHeaderAction", typing.Dict[str, typing.Any]]]]] = None,
        route_configuration_override_action: typing.Optional[typing.Union["CdnFrontdoorRuleActionsRouteConfigurationOverrideAction", typing.Dict[str, typing.Any]]] = None,
        url_redirect_action: typing.Optional[typing.Union["CdnFrontdoorRuleActionsUrlRedirectAction", typing.Dict[str, typing.Any]]] = None,
        url_rewrite_action: typing.Optional[typing.Union["CdnFrontdoorRuleActionsUrlRewriteAction", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param request_header_action: request_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_header_action CdnFrontdoorRule#request_header_action}
        :param response_header_action: response_header_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#response_header_action CdnFrontdoorRule#response_header_action}
        :param route_configuration_override_action: route_configuration_override_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#route_configuration_override_action CdnFrontdoorRule#route_configuration_override_action}
        :param url_redirect_action: url_redirect_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_redirect_action CdnFrontdoorRule#url_redirect_action}
        :param url_rewrite_action: url_rewrite_action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_rewrite_action CdnFrontdoorRule#url_rewrite_action}
        '''
        if isinstance(route_configuration_override_action, dict):
            route_configuration_override_action = CdnFrontdoorRuleActionsRouteConfigurationOverrideAction(**route_configuration_override_action)
        if isinstance(url_redirect_action, dict):
            url_redirect_action = CdnFrontdoorRuleActionsUrlRedirectAction(**url_redirect_action)
        if isinstance(url_rewrite_action, dict):
            url_rewrite_action = CdnFrontdoorRuleActionsUrlRewriteAction(**url_rewrite_action)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActions.__init__)
            check_type(argname="argument request_header_action", value=request_header_action, expected_type=type_hints["request_header_action"])
            check_type(argname="argument response_header_action", value=response_header_action, expected_type=type_hints["response_header_action"])
            check_type(argname="argument route_configuration_override_action", value=route_configuration_override_action, expected_type=type_hints["route_configuration_override_action"])
            check_type(argname="argument url_redirect_action", value=url_redirect_action, expected_type=type_hints["url_redirect_action"])
            check_type(argname="argument url_rewrite_action", value=url_rewrite_action, expected_type=type_hints["url_rewrite_action"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_header_action is not None:
            self._values["request_header_action"] = request_header_action
        if response_header_action is not None:
            self._values["response_header_action"] = response_header_action
        if route_configuration_override_action is not None:
            self._values["route_configuration_override_action"] = route_configuration_override_action
        if url_redirect_action is not None:
            self._values["url_redirect_action"] = url_redirect_action
        if url_rewrite_action is not None:
            self._values["url_rewrite_action"] = url_rewrite_action

    @builtins.property
    def request_header_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsRequestHeaderAction"]]]:
        '''request_header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_header_action CdnFrontdoorRule#request_header_action}
        '''
        result = self._values.get("request_header_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsRequestHeaderAction"]]], result)

    @builtins.property
    def response_header_action(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsResponseHeaderAction"]]]:
        '''response_header_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#response_header_action CdnFrontdoorRule#response_header_action}
        '''
        result = self._values.get("response_header_action")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsResponseHeaderAction"]]], result)

    @builtins.property
    def route_configuration_override_action(
        self,
    ) -> typing.Optional["CdnFrontdoorRuleActionsRouteConfigurationOverrideAction"]:
        '''route_configuration_override_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#route_configuration_override_action CdnFrontdoorRule#route_configuration_override_action}
        '''
        result = self._values.get("route_configuration_override_action")
        return typing.cast(typing.Optional["CdnFrontdoorRuleActionsRouteConfigurationOverrideAction"], result)

    @builtins.property
    def url_redirect_action(
        self,
    ) -> typing.Optional["CdnFrontdoorRuleActionsUrlRedirectAction"]:
        '''url_redirect_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_redirect_action CdnFrontdoorRule#url_redirect_action}
        '''
        result = self._values.get("url_redirect_action")
        return typing.cast(typing.Optional["CdnFrontdoorRuleActionsUrlRedirectAction"], result)

    @builtins.property
    def url_rewrite_action(
        self,
    ) -> typing.Optional["CdnFrontdoorRuleActionsUrlRewriteAction"]:
        '''url_rewrite_action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_rewrite_action CdnFrontdoorRule#url_rewrite_action}
        '''
        result = self._values.get("url_rewrite_action")
        return typing.cast(typing.Optional["CdnFrontdoorRuleActionsUrlRewriteAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestHeaderAction")
    def put_request_header_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleActionsRequestHeaderAction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsOutputReference.put_request_header_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeaderAction", [value]))

    @jsii.member(jsii_name="putResponseHeaderAction")
    def put_response_header_action(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleActionsResponseHeaderAction", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsOutputReference.put_response_header_action)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResponseHeaderAction", [value]))

    @jsii.member(jsii_name="putRouteConfigurationOverrideAction")
    def put_route_configuration_override_action(
        self,
        *,
        cache_duration: builtins.str,
        cdn_frontdoor_origin_group_id: builtins.str,
        cache_behavior: typing.Optional[builtins.str] = None,
        compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_protocol: typing.Optional[builtins.str] = None,
        query_string_caching_behavior: typing.Optional[builtins.str] = None,
        query_string_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cache_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cache_duration CdnFrontdoorRule#cache_duration}.
        :param cdn_frontdoor_origin_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cdn_frontdoor_origin_group_id CdnFrontdoorRule#cdn_frontdoor_origin_group_id}.
        :param cache_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cache_behavior CdnFrontdoorRule#cache_behavior}.
        :param compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#compression_enabled CdnFrontdoorRule#compression_enabled}.
        :param forwarding_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#forwarding_protocol CdnFrontdoorRule#forwarding_protocol}.
        :param query_string_caching_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_caching_behavior CdnFrontdoorRule#query_string_caching_behavior}.
        :param query_string_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_parameters CdnFrontdoorRule#query_string_parameters}.
        '''
        value = CdnFrontdoorRuleActionsRouteConfigurationOverrideAction(
            cache_duration=cache_duration,
            cdn_frontdoor_origin_group_id=cdn_frontdoor_origin_group_id,
            cache_behavior=cache_behavior,
            compression_enabled=compression_enabled,
            forwarding_protocol=forwarding_protocol,
            query_string_caching_behavior=query_string_caching_behavior,
            query_string_parameters=query_string_parameters,
        )

        return typing.cast(None, jsii.invoke(self, "putRouteConfigurationOverrideAction", [value]))

    @jsii.member(jsii_name="putUrlRedirectAction")
    def put_url_redirect_action(
        self,
        *,
        destination_hostname: builtins.str,
        redirect_type: builtins.str,
        destination_fragment: typing.Optional[builtins.str] = None,
        destination_path: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
        redirect_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_hostname CdnFrontdoorRule#destination_hostname}.
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#redirect_type CdnFrontdoorRule#redirect_type}.
        :param destination_fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_fragment CdnFrontdoorRule#destination_fragment}.
        :param destination_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_path CdnFrontdoorRule#destination_path}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string CdnFrontdoorRule#query_string}.
        :param redirect_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#redirect_protocol CdnFrontdoorRule#redirect_protocol}.
        '''
        value = CdnFrontdoorRuleActionsUrlRedirectAction(
            destination_hostname=destination_hostname,
            redirect_type=redirect_type,
            destination_fragment=destination_fragment,
            destination_path=destination_path,
            query_string=query_string,
            redirect_protocol=redirect_protocol,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRedirectAction", [value]))

    @jsii.member(jsii_name="putUrlRewriteAction")
    def put_url_rewrite_action(
        self,
        *,
        destination: builtins.str,
        source_pattern: builtins.str,
        preserve_unmatched_path: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination CdnFrontdoorRule#destination}.
        :param source_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#source_pattern CdnFrontdoorRule#source_pattern}.
        :param preserve_unmatched_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#preserve_unmatched_path CdnFrontdoorRule#preserve_unmatched_path}.
        '''
        value = CdnFrontdoorRuleActionsUrlRewriteAction(
            destination=destination,
            source_pattern=source_pattern,
            preserve_unmatched_path=preserve_unmatched_path,
        )

        return typing.cast(None, jsii.invoke(self, "putUrlRewriteAction", [value]))

    @jsii.member(jsii_name="resetRequestHeaderAction")
    def reset_request_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaderAction", []))

    @jsii.member(jsii_name="resetResponseHeaderAction")
    def reset_response_header_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeaderAction", []))

    @jsii.member(jsii_name="resetRouteConfigurationOverrideAction")
    def reset_route_configuration_override_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteConfigurationOverrideAction", []))

    @jsii.member(jsii_name="resetUrlRedirectAction")
    def reset_url_redirect_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRedirectAction", []))

    @jsii.member(jsii_name="resetUrlRewriteAction")
    def reset_url_rewrite_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlRewriteAction", []))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderAction")
    def request_header_action(self) -> "CdnFrontdoorRuleActionsRequestHeaderActionList":
        return typing.cast("CdnFrontdoorRuleActionsRequestHeaderActionList", jsii.get(self, "requestHeaderAction"))

    @builtins.property
    @jsii.member(jsii_name="responseHeaderAction")
    def response_header_action(
        self,
    ) -> "CdnFrontdoorRuleActionsResponseHeaderActionList":
        return typing.cast("CdnFrontdoorRuleActionsResponseHeaderActionList", jsii.get(self, "responseHeaderAction"))

    @builtins.property
    @jsii.member(jsii_name="routeConfigurationOverrideAction")
    def route_configuration_override_action(
        self,
    ) -> "CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference":
        return typing.cast("CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference", jsii.get(self, "routeConfigurationOverrideAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectAction")
    def url_redirect_action(
        self,
    ) -> "CdnFrontdoorRuleActionsUrlRedirectActionOutputReference":
        return typing.cast("CdnFrontdoorRuleActionsUrlRedirectActionOutputReference", jsii.get(self, "urlRedirectAction"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteAction")
    def url_rewrite_action(
        self,
    ) -> "CdnFrontdoorRuleActionsUrlRewriteActionOutputReference":
        return typing.cast("CdnFrontdoorRuleActionsUrlRewriteActionOutputReference", jsii.get(self, "urlRewriteAction"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderActionInput")
    def request_header_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsRequestHeaderAction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsRequestHeaderAction"]]], jsii.get(self, "requestHeaderActionInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeaderActionInput")
    def response_header_action_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsResponseHeaderAction"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleActionsResponseHeaderAction"]]], jsii.get(self, "responseHeaderActionInput"))

    @builtins.property
    @jsii.member(jsii_name="routeConfigurationOverrideActionInput")
    def route_configuration_override_action_input(
        self,
    ) -> typing.Optional["CdnFrontdoorRuleActionsRouteConfigurationOverrideAction"]:
        return typing.cast(typing.Optional["CdnFrontdoorRuleActionsRouteConfigurationOverrideAction"], jsii.get(self, "routeConfigurationOverrideActionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRedirectActionInput")
    def url_redirect_action_input(
        self,
    ) -> typing.Optional["CdnFrontdoorRuleActionsUrlRedirectAction"]:
        return typing.cast(typing.Optional["CdnFrontdoorRuleActionsUrlRedirectAction"], jsii.get(self, "urlRedirectActionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlRewriteActionInput")
    def url_rewrite_action_input(
        self,
    ) -> typing.Optional["CdnFrontdoorRuleActionsUrlRewriteAction"]:
        return typing.cast(typing.Optional["CdnFrontdoorRuleActionsUrlRewriteAction"], jsii.get(self, "urlRewriteActionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CdnFrontdoorRuleActions]:
        return typing.cast(typing.Optional[CdnFrontdoorRuleActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CdnFrontdoorRuleActions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsRequestHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "header_action": "headerAction",
        "header_name": "headerName",
        "value": "value",
    },
)
class CdnFrontdoorRuleActionsRequestHeaderAction:
    def __init__(
        self,
        *,
        header_action: builtins.str,
        header_name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param header_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_action CdnFrontdoorRule#header_action}.
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_name CdnFrontdoorRule#header_name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#value CdnFrontdoorRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsRequestHeaderAction.__init__)
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_action": header_action,
            "header_name": header_name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def header_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_action CdnFrontdoorRule#header_action}.'''
        result = self._values.get("header_action")
        assert result is not None, "Required property 'header_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_name CdnFrontdoorRule#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#value CdnFrontdoorRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleActionsRequestHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleActionsRequestHeaderActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsRequestHeaderActionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsRequestHeaderActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleActionsRequestHeaderActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsRequestHeaderActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleActionsRequestHeaderActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleActionsRequestHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleActionsRequestHeaderAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleActionsRequestHeaderAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleActionsRequestHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsRequestHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsRequestHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerAction"))

    @header_action.setter
    def header_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionOutputReference, "header_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerAction", value)

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleActionsRequestHeaderAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleActionsRequestHeaderAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleActionsRequestHeaderAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRequestHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsResponseHeaderAction",
    jsii_struct_bases=[],
    name_mapping={
        "header_action": "headerAction",
        "header_name": "headerName",
        "value": "value",
    },
)
class CdnFrontdoorRuleActionsResponseHeaderAction:
    def __init__(
        self,
        *,
        header_action: builtins.str,
        header_name: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param header_action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_action CdnFrontdoorRule#header_action}.
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_name CdnFrontdoorRule#header_name}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#value CdnFrontdoorRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsResponseHeaderAction.__init__)
            check_type(argname="argument header_action", value=header_action, expected_type=type_hints["header_action"])
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_action": header_action,
            "header_name": header_name,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def header_action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_action CdnFrontdoorRule#header_action}.'''
        result = self._values.get("header_action")
        assert result is not None, "Required property 'header_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_name CdnFrontdoorRule#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#value CdnFrontdoorRule#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleActionsResponseHeaderAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleActionsResponseHeaderActionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsResponseHeaderActionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsResponseHeaderActionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleActionsResponseHeaderActionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsResponseHeaderActionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleActionsResponseHeaderActionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleActionsResponseHeaderAction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleActionsResponseHeaderAction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleActionsResponseHeaderAction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleActionsResponseHeaderActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsResponseHeaderActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsResponseHeaderActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="headerActionInput")
    def header_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerActionInput"))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="headerAction")
    def header_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerAction"))

    @header_action.setter
    def header_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionOutputReference, "header_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerAction", value)

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleActionsResponseHeaderAction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleActionsResponseHeaderAction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleActionsResponseHeaderAction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsResponseHeaderActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsRouteConfigurationOverrideAction",
    jsii_struct_bases=[],
    name_mapping={
        "cache_duration": "cacheDuration",
        "cdn_frontdoor_origin_group_id": "cdnFrontdoorOriginGroupId",
        "cache_behavior": "cacheBehavior",
        "compression_enabled": "compressionEnabled",
        "forwarding_protocol": "forwardingProtocol",
        "query_string_caching_behavior": "queryStringCachingBehavior",
        "query_string_parameters": "queryStringParameters",
    },
)
class CdnFrontdoorRuleActionsRouteConfigurationOverrideAction:
    def __init__(
        self,
        *,
        cache_duration: builtins.str,
        cdn_frontdoor_origin_group_id: builtins.str,
        cache_behavior: typing.Optional[builtins.str] = None,
        compression_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_protocol: typing.Optional[builtins.str] = None,
        query_string_caching_behavior: typing.Optional[builtins.str] = None,
        query_string_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cache_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cache_duration CdnFrontdoorRule#cache_duration}.
        :param cdn_frontdoor_origin_group_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cdn_frontdoor_origin_group_id CdnFrontdoorRule#cdn_frontdoor_origin_group_id}.
        :param cache_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cache_behavior CdnFrontdoorRule#cache_behavior}.
        :param compression_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#compression_enabled CdnFrontdoorRule#compression_enabled}.
        :param forwarding_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#forwarding_protocol CdnFrontdoorRule#forwarding_protocol}.
        :param query_string_caching_behavior: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_caching_behavior CdnFrontdoorRule#query_string_caching_behavior}.
        :param query_string_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_parameters CdnFrontdoorRule#query_string_parameters}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsRouteConfigurationOverrideAction.__init__)
            check_type(argname="argument cache_duration", value=cache_duration, expected_type=type_hints["cache_duration"])
            check_type(argname="argument cdn_frontdoor_origin_group_id", value=cdn_frontdoor_origin_group_id, expected_type=type_hints["cdn_frontdoor_origin_group_id"])
            check_type(argname="argument cache_behavior", value=cache_behavior, expected_type=type_hints["cache_behavior"])
            check_type(argname="argument compression_enabled", value=compression_enabled, expected_type=type_hints["compression_enabled"])
            check_type(argname="argument forwarding_protocol", value=forwarding_protocol, expected_type=type_hints["forwarding_protocol"])
            check_type(argname="argument query_string_caching_behavior", value=query_string_caching_behavior, expected_type=type_hints["query_string_caching_behavior"])
            check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "cache_duration": cache_duration,
            "cdn_frontdoor_origin_group_id": cdn_frontdoor_origin_group_id,
        }
        if cache_behavior is not None:
            self._values["cache_behavior"] = cache_behavior
        if compression_enabled is not None:
            self._values["compression_enabled"] = compression_enabled
        if forwarding_protocol is not None:
            self._values["forwarding_protocol"] = forwarding_protocol
        if query_string_caching_behavior is not None:
            self._values["query_string_caching_behavior"] = query_string_caching_behavior
        if query_string_parameters is not None:
            self._values["query_string_parameters"] = query_string_parameters

    @builtins.property
    def cache_duration(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cache_duration CdnFrontdoorRule#cache_duration}.'''
        result = self._values.get("cache_duration")
        assert result is not None, "Required property 'cache_duration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdn_frontdoor_origin_group_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cdn_frontdoor_origin_group_id CdnFrontdoorRule#cdn_frontdoor_origin_group_id}.'''
        result = self._values.get("cdn_frontdoor_origin_group_id")
        assert result is not None, "Required property 'cdn_frontdoor_origin_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cache_behavior CdnFrontdoorRule#cache_behavior}.'''
        result = self._values.get("cache_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compression_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#compression_enabled CdnFrontdoorRule#compression_enabled}.'''
        result = self._values.get("compression_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forwarding_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#forwarding_protocol CdnFrontdoorRule#forwarding_protocol}.'''
        result = self._values.get("forwarding_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_string_caching_behavior(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_caching_behavior CdnFrontdoorRule#query_string_caching_behavior}.'''
        result = self._values.get("query_string_caching_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_string_parameters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_parameters CdnFrontdoorRule#query_string_parameters}.'''
        result = self._values.get("query_string_parameters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleActionsRouteConfigurationOverrideAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCacheBehavior")
    def reset_cache_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheBehavior", []))

    @jsii.member(jsii_name="resetCompressionEnabled")
    def reset_compression_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompressionEnabled", []))

    @jsii.member(jsii_name="resetForwardingProtocol")
    def reset_forwarding_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingProtocol", []))

    @jsii.member(jsii_name="resetQueryStringCachingBehavior")
    def reset_query_string_caching_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringCachingBehavior", []))

    @jsii.member(jsii_name="resetQueryStringParameters")
    def reset_query_string_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringParameters", []))

    @builtins.property
    @jsii.member(jsii_name="cacheBehaviorInput")
    def cache_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheDurationInput")
    def cache_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginGroupIdInput")
    def cdn_frontdoor_origin_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorOriginGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionEnabledInput")
    def compression_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "compressionEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingProtocolInput")
    def forwarding_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardingProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringCachingBehaviorInput")
    def query_string_caching_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringCachingBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringParametersInput")
    def query_string_parameters_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryStringParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheBehavior")
    def cache_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheBehavior"))

    @cache_behavior.setter
    def cache_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "cache_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="cacheDuration")
    def cache_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheDuration"))

    @cache_duration.setter
    def cache_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "cache_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheDuration", value)

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorOriginGroupId")
    def cdn_frontdoor_origin_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorOriginGroupId"))

    @cdn_frontdoor_origin_group_id.setter
    def cdn_frontdoor_origin_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "cdn_frontdoor_origin_group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorOriginGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="compressionEnabled")
    def compression_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "compressionEnabled"))

    @compression_enabled.setter
    def compression_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "compression_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compressionEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="forwardingProtocol")
    def forwarding_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardingProtocol"))

    @forwarding_protocol.setter
    def forwarding_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "forwarding_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardingProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringCachingBehavior")
    def query_string_caching_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryStringCachingBehavior"))

    @query_string_caching_behavior.setter
    def query_string_caching_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "query_string_caching_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringCachingBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="queryStringParameters")
    def query_string_parameters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryStringParameters"))

    @query_string_parameters.setter
    def query_string_parameters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "query_string_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryStringParameters", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnFrontdoorRuleActionsRouteConfigurationOverrideAction]:
        return typing.cast(typing.Optional[CdnFrontdoorRuleActionsRouteConfigurationOverrideAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorRuleActionsRouteConfigurationOverrideAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsUrlRedirectAction",
    jsii_struct_bases=[],
    name_mapping={
        "destination_hostname": "destinationHostname",
        "redirect_type": "redirectType",
        "destination_fragment": "destinationFragment",
        "destination_path": "destinationPath",
        "query_string": "queryString",
        "redirect_protocol": "redirectProtocol",
    },
)
class CdnFrontdoorRuleActionsUrlRedirectAction:
    def __init__(
        self,
        *,
        destination_hostname: builtins.str,
        redirect_type: builtins.str,
        destination_fragment: typing.Optional[builtins.str] = None,
        destination_path: typing.Optional[builtins.str] = None,
        query_string: typing.Optional[builtins.str] = None,
        redirect_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_hostname CdnFrontdoorRule#destination_hostname}.
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#redirect_type CdnFrontdoorRule#redirect_type}.
        :param destination_fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_fragment CdnFrontdoorRule#destination_fragment}.
        :param destination_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_path CdnFrontdoorRule#destination_path}.
        :param query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string CdnFrontdoorRule#query_string}.
        :param redirect_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#redirect_protocol CdnFrontdoorRule#redirect_protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsUrlRedirectAction.__init__)
            check_type(argname="argument destination_hostname", value=destination_hostname, expected_type=type_hints["destination_hostname"])
            check_type(argname="argument redirect_type", value=redirect_type, expected_type=type_hints["redirect_type"])
            check_type(argname="argument destination_fragment", value=destination_fragment, expected_type=type_hints["destination_fragment"])
            check_type(argname="argument destination_path", value=destination_path, expected_type=type_hints["destination_path"])
            check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
            check_type(argname="argument redirect_protocol", value=redirect_protocol, expected_type=type_hints["redirect_protocol"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_hostname": destination_hostname,
            "redirect_type": redirect_type,
        }
        if destination_fragment is not None:
            self._values["destination_fragment"] = destination_fragment
        if destination_path is not None:
            self._values["destination_path"] = destination_path
        if query_string is not None:
            self._values["query_string"] = query_string
        if redirect_protocol is not None:
            self._values["redirect_protocol"] = redirect_protocol

    @builtins.property
    def destination_hostname(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_hostname CdnFrontdoorRule#destination_hostname}.'''
        result = self._values.get("destination_hostname")
        assert result is not None, "Required property 'destination_hostname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def redirect_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#redirect_type CdnFrontdoorRule#redirect_type}.'''
        result = self._values.get("redirect_type")
        assert result is not None, "Required property 'redirect_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_fragment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_fragment CdnFrontdoorRule#destination_fragment}.'''
        result = self._values.get("destination_fragment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination_path CdnFrontdoorRule#destination_path}.'''
        result = self._values.get("destination_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string CdnFrontdoorRule#query_string}.'''
        result = self._values.get("query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#redirect_protocol CdnFrontdoorRule#redirect_protocol}.'''
        result = self._values.get("redirect_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleActionsUrlRedirectAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleActionsUrlRedirectActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsUrlRedirectActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDestinationFragment")
    def reset_destination_fragment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFragment", []))

    @jsii.member(jsii_name="resetDestinationPath")
    def reset_destination_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationPath", []))

    @jsii.member(jsii_name="resetQueryString")
    def reset_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryString", []))

    @jsii.member(jsii_name="resetRedirectProtocol")
    def reset_redirect_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="destinationFragmentInput")
    def destination_fragment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationFragmentInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationHostnameInput")
    def destination_hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationHostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationPathInput")
    def destination_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationPathInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringInput")
    def query_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectProtocolInput")
    def redirect_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectTypeInput")
    def redirect_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFragment")
    def destination_fragment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationFragment"))

    @destination_fragment.setter
    def destination_fragment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference, "destination_fragment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFragment", value)

    @builtins.property
    @jsii.member(jsii_name="destinationHostname")
    def destination_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationHostname"))

    @destination_hostname.setter
    def destination_hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference, "destination_hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationHostname", value)

    @builtins.property
    @jsii.member(jsii_name="destinationPath")
    def destination_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationPath"))

    @destination_path.setter
    def destination_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference, "destination_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationPath", value)

    @builtins.property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryString"))

    @query_string.setter
    def query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference, "query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryString", value)

    @builtins.property
    @jsii.member(jsii_name="redirectProtocol")
    def redirect_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectProtocol"))

    @redirect_protocol.setter
    def redirect_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference, "redirect_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="redirectType")
    def redirect_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectType"))

    @redirect_type.setter
    def redirect_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference, "redirect_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnFrontdoorRuleActionsUrlRedirectAction]:
        return typing.cast(typing.Optional[CdnFrontdoorRuleActionsUrlRedirectAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorRuleActionsUrlRedirectAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRedirectActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsUrlRewriteAction",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "source_pattern": "sourcePattern",
        "preserve_unmatched_path": "preserveUnmatchedPath",
    },
)
class CdnFrontdoorRuleActionsUrlRewriteAction:
    def __init__(
        self,
        *,
        destination: builtins.str,
        source_pattern: builtins.str,
        preserve_unmatched_path: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination CdnFrontdoorRule#destination}.
        :param source_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#source_pattern CdnFrontdoorRule#source_pattern}.
        :param preserve_unmatched_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#preserve_unmatched_path CdnFrontdoorRule#preserve_unmatched_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsUrlRewriteAction.__init__)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument source_pattern", value=source_pattern, expected_type=type_hints["source_pattern"])
            check_type(argname="argument preserve_unmatched_path", value=preserve_unmatched_path, expected_type=type_hints["preserve_unmatched_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination": destination,
            "source_pattern": source_pattern,
        }
        if preserve_unmatched_path is not None:
            self._values["preserve_unmatched_path"] = preserve_unmatched_path

    @builtins.property
    def destination(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#destination CdnFrontdoorRule#destination}.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_pattern(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#source_pattern CdnFrontdoorRule#source_pattern}.'''
        result = self._values.get("source_pattern")
        assert result is not None, "Required property 'source_pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preserve_unmatched_path(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#preserve_unmatched_path CdnFrontdoorRule#preserve_unmatched_path}.'''
        result = self._values.get("preserve_unmatched_path")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleActionsUrlRewriteAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleActionsUrlRewriteActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleActionsUrlRewriteActionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleActionsUrlRewriteActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPreserveUnmatchedPath")
    def reset_preserve_unmatched_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreserveUnmatchedPath", []))

    @builtins.property
    @jsii.member(jsii_name="destinationInput")
    def destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationInput"))

    @builtins.property
    @jsii.member(jsii_name="preserveUnmatchedPathInput")
    def preserve_unmatched_path_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preserveUnmatchedPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePatternInput")
    def source_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePatternInput"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRewriteActionOutputReference, "destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="preserveUnmatchedPath")
    def preserve_unmatched_path(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preserveUnmatchedPath"))

    @preserve_unmatched_path.setter
    def preserve_unmatched_path(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRewriteActionOutputReference, "preserve_unmatched_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preserveUnmatchedPath", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePattern")
    def source_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourcePattern"))

    @source_pattern.setter
    def source_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRewriteActionOutputReference, "source_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePattern", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CdnFrontdoorRuleActionsUrlRewriteAction]:
        return typing.cast(typing.Optional[CdnFrontdoorRuleActionsUrlRewriteAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorRuleActionsUrlRewriteAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleActionsUrlRewriteActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditions",
    jsii_struct_bases=[],
    name_mapping={
        "client_port_condition": "clientPortCondition",
        "cookies_condition": "cookiesCondition",
        "host_name_condition": "hostNameCondition",
        "http_version_condition": "httpVersionCondition",
        "is_device_condition": "isDeviceCondition",
        "post_args_condition": "postArgsCondition",
        "query_string_condition": "queryStringCondition",
        "remote_address_condition": "remoteAddressCondition",
        "request_body_condition": "requestBodyCondition",
        "request_header_condition": "requestHeaderCondition",
        "request_method_condition": "requestMethodCondition",
        "request_scheme_condition": "requestSchemeCondition",
        "request_uri_condition": "requestUriCondition",
        "server_port_condition": "serverPortCondition",
        "socket_address_condition": "socketAddressCondition",
        "ssl_protocol_condition": "sslProtocolCondition",
        "url_file_extension_condition": "urlFileExtensionCondition",
        "url_filename_condition": "urlFilenameCondition",
        "url_path_condition": "urlPathCondition",
    },
)
class CdnFrontdoorRuleConditions:
    def __init__(
        self,
        *,
        client_port_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsClientPortCondition", typing.Dict[str, typing.Any]]]]] = None,
        cookies_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsCookiesCondition", typing.Dict[str, typing.Any]]]]] = None,
        host_name_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsHostNameCondition", typing.Dict[str, typing.Any]]]]] = None,
        http_version_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsHttpVersionCondition", typing.Dict[str, typing.Any]]]]] = None,
        is_device_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsIsDeviceCondition", typing.Dict[str, typing.Any]]]]] = None,
        post_args_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsPostArgsCondition", typing.Dict[str, typing.Any]]]]] = None,
        query_string_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsQueryStringCondition", typing.Dict[str, typing.Any]]]]] = None,
        remote_address_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRemoteAddressCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_body_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestBodyCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_header_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestHeaderCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_method_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestMethodCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_scheme_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestSchemeCondition", typing.Dict[str, typing.Any]]]]] = None,
        request_uri_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestUriCondition", typing.Dict[str, typing.Any]]]]] = None,
        server_port_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsServerPortCondition", typing.Dict[str, typing.Any]]]]] = None,
        socket_address_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsSocketAddressCondition", typing.Dict[str, typing.Any]]]]] = None,
        ssl_protocol_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsSslProtocolCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_file_extension_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlFileExtensionCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_filename_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlFilenameCondition", typing.Dict[str, typing.Any]]]]] = None,
        url_path_condition: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlPathCondition", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param client_port_condition: client_port_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#client_port_condition CdnFrontdoorRule#client_port_condition}
        :param cookies_condition: cookies_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cookies_condition CdnFrontdoorRule#cookies_condition}
        :param host_name_condition: host_name_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#host_name_condition CdnFrontdoorRule#host_name_condition}
        :param http_version_condition: http_version_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#http_version_condition CdnFrontdoorRule#http_version_condition}
        :param is_device_condition: is_device_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#is_device_condition CdnFrontdoorRule#is_device_condition}
        :param post_args_condition: post_args_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#post_args_condition CdnFrontdoorRule#post_args_condition}
        :param query_string_condition: query_string_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_condition CdnFrontdoorRule#query_string_condition}
        :param remote_address_condition: remote_address_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#remote_address_condition CdnFrontdoorRule#remote_address_condition}
        :param request_body_condition: request_body_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_body_condition CdnFrontdoorRule#request_body_condition}
        :param request_header_condition: request_header_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_header_condition CdnFrontdoorRule#request_header_condition}
        :param request_method_condition: request_method_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_method_condition CdnFrontdoorRule#request_method_condition}
        :param request_scheme_condition: request_scheme_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_scheme_condition CdnFrontdoorRule#request_scheme_condition}
        :param request_uri_condition: request_uri_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_uri_condition CdnFrontdoorRule#request_uri_condition}
        :param server_port_condition: server_port_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#server_port_condition CdnFrontdoorRule#server_port_condition}
        :param socket_address_condition: socket_address_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#socket_address_condition CdnFrontdoorRule#socket_address_condition}
        :param ssl_protocol_condition: ssl_protocol_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#ssl_protocol_condition CdnFrontdoorRule#ssl_protocol_condition}
        :param url_file_extension_condition: url_file_extension_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_file_extension_condition CdnFrontdoorRule#url_file_extension_condition}
        :param url_filename_condition: url_filename_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_filename_condition CdnFrontdoorRule#url_filename_condition}
        :param url_path_condition: url_path_condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_path_condition CdnFrontdoorRule#url_path_condition}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditions.__init__)
            check_type(argname="argument client_port_condition", value=client_port_condition, expected_type=type_hints["client_port_condition"])
            check_type(argname="argument cookies_condition", value=cookies_condition, expected_type=type_hints["cookies_condition"])
            check_type(argname="argument host_name_condition", value=host_name_condition, expected_type=type_hints["host_name_condition"])
            check_type(argname="argument http_version_condition", value=http_version_condition, expected_type=type_hints["http_version_condition"])
            check_type(argname="argument is_device_condition", value=is_device_condition, expected_type=type_hints["is_device_condition"])
            check_type(argname="argument post_args_condition", value=post_args_condition, expected_type=type_hints["post_args_condition"])
            check_type(argname="argument query_string_condition", value=query_string_condition, expected_type=type_hints["query_string_condition"])
            check_type(argname="argument remote_address_condition", value=remote_address_condition, expected_type=type_hints["remote_address_condition"])
            check_type(argname="argument request_body_condition", value=request_body_condition, expected_type=type_hints["request_body_condition"])
            check_type(argname="argument request_header_condition", value=request_header_condition, expected_type=type_hints["request_header_condition"])
            check_type(argname="argument request_method_condition", value=request_method_condition, expected_type=type_hints["request_method_condition"])
            check_type(argname="argument request_scheme_condition", value=request_scheme_condition, expected_type=type_hints["request_scheme_condition"])
            check_type(argname="argument request_uri_condition", value=request_uri_condition, expected_type=type_hints["request_uri_condition"])
            check_type(argname="argument server_port_condition", value=server_port_condition, expected_type=type_hints["server_port_condition"])
            check_type(argname="argument socket_address_condition", value=socket_address_condition, expected_type=type_hints["socket_address_condition"])
            check_type(argname="argument ssl_protocol_condition", value=ssl_protocol_condition, expected_type=type_hints["ssl_protocol_condition"])
            check_type(argname="argument url_file_extension_condition", value=url_file_extension_condition, expected_type=type_hints["url_file_extension_condition"])
            check_type(argname="argument url_filename_condition", value=url_filename_condition, expected_type=type_hints["url_filename_condition"])
            check_type(argname="argument url_path_condition", value=url_path_condition, expected_type=type_hints["url_path_condition"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_port_condition is not None:
            self._values["client_port_condition"] = client_port_condition
        if cookies_condition is not None:
            self._values["cookies_condition"] = cookies_condition
        if host_name_condition is not None:
            self._values["host_name_condition"] = host_name_condition
        if http_version_condition is not None:
            self._values["http_version_condition"] = http_version_condition
        if is_device_condition is not None:
            self._values["is_device_condition"] = is_device_condition
        if post_args_condition is not None:
            self._values["post_args_condition"] = post_args_condition
        if query_string_condition is not None:
            self._values["query_string_condition"] = query_string_condition
        if remote_address_condition is not None:
            self._values["remote_address_condition"] = remote_address_condition
        if request_body_condition is not None:
            self._values["request_body_condition"] = request_body_condition
        if request_header_condition is not None:
            self._values["request_header_condition"] = request_header_condition
        if request_method_condition is not None:
            self._values["request_method_condition"] = request_method_condition
        if request_scheme_condition is not None:
            self._values["request_scheme_condition"] = request_scheme_condition
        if request_uri_condition is not None:
            self._values["request_uri_condition"] = request_uri_condition
        if server_port_condition is not None:
            self._values["server_port_condition"] = server_port_condition
        if socket_address_condition is not None:
            self._values["socket_address_condition"] = socket_address_condition
        if ssl_protocol_condition is not None:
            self._values["ssl_protocol_condition"] = ssl_protocol_condition
        if url_file_extension_condition is not None:
            self._values["url_file_extension_condition"] = url_file_extension_condition
        if url_filename_condition is not None:
            self._values["url_filename_condition"] = url_filename_condition
        if url_path_condition is not None:
            self._values["url_path_condition"] = url_path_condition

    @builtins.property
    def client_port_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsClientPortCondition"]]]:
        '''client_port_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#client_port_condition CdnFrontdoorRule#client_port_condition}
        '''
        result = self._values.get("client_port_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsClientPortCondition"]]], result)

    @builtins.property
    def cookies_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsCookiesCondition"]]]:
        '''cookies_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cookies_condition CdnFrontdoorRule#cookies_condition}
        '''
        result = self._values.get("cookies_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsCookiesCondition"]]], result)

    @builtins.property
    def host_name_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsHostNameCondition"]]]:
        '''host_name_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#host_name_condition CdnFrontdoorRule#host_name_condition}
        '''
        result = self._values.get("host_name_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsHostNameCondition"]]], result)

    @builtins.property
    def http_version_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsHttpVersionCondition"]]]:
        '''http_version_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#http_version_condition CdnFrontdoorRule#http_version_condition}
        '''
        result = self._values.get("http_version_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsHttpVersionCondition"]]], result)

    @builtins.property
    def is_device_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsIsDeviceCondition"]]]:
        '''is_device_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#is_device_condition CdnFrontdoorRule#is_device_condition}
        '''
        result = self._values.get("is_device_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsIsDeviceCondition"]]], result)

    @builtins.property
    def post_args_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsPostArgsCondition"]]]:
        '''post_args_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#post_args_condition CdnFrontdoorRule#post_args_condition}
        '''
        result = self._values.get("post_args_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsPostArgsCondition"]]], result)

    @builtins.property
    def query_string_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsQueryStringCondition"]]]:
        '''query_string_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#query_string_condition CdnFrontdoorRule#query_string_condition}
        '''
        result = self._values.get("query_string_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsQueryStringCondition"]]], result)

    @builtins.property
    def remote_address_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRemoteAddressCondition"]]]:
        '''remote_address_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#remote_address_condition CdnFrontdoorRule#remote_address_condition}
        '''
        result = self._values.get("remote_address_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRemoteAddressCondition"]]], result)

    @builtins.property
    def request_body_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestBodyCondition"]]]:
        '''request_body_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_body_condition CdnFrontdoorRule#request_body_condition}
        '''
        result = self._values.get("request_body_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestBodyCondition"]]], result)

    @builtins.property
    def request_header_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestHeaderCondition"]]]:
        '''request_header_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_header_condition CdnFrontdoorRule#request_header_condition}
        '''
        result = self._values.get("request_header_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestHeaderCondition"]]], result)

    @builtins.property
    def request_method_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestMethodCondition"]]]:
        '''request_method_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_method_condition CdnFrontdoorRule#request_method_condition}
        '''
        result = self._values.get("request_method_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestMethodCondition"]]], result)

    @builtins.property
    def request_scheme_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestSchemeCondition"]]]:
        '''request_scheme_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_scheme_condition CdnFrontdoorRule#request_scheme_condition}
        '''
        result = self._values.get("request_scheme_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestSchemeCondition"]]], result)

    @builtins.property
    def request_uri_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestUriCondition"]]]:
        '''request_uri_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#request_uri_condition CdnFrontdoorRule#request_uri_condition}
        '''
        result = self._values.get("request_uri_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestUriCondition"]]], result)

    @builtins.property
    def server_port_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsServerPortCondition"]]]:
        '''server_port_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#server_port_condition CdnFrontdoorRule#server_port_condition}
        '''
        result = self._values.get("server_port_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsServerPortCondition"]]], result)

    @builtins.property
    def socket_address_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSocketAddressCondition"]]]:
        '''socket_address_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#socket_address_condition CdnFrontdoorRule#socket_address_condition}
        '''
        result = self._values.get("socket_address_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSocketAddressCondition"]]], result)

    @builtins.property
    def ssl_protocol_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSslProtocolCondition"]]]:
        '''ssl_protocol_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#ssl_protocol_condition CdnFrontdoorRule#ssl_protocol_condition}
        '''
        result = self._values.get("ssl_protocol_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSslProtocolCondition"]]], result)

    @builtins.property
    def url_file_extension_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFileExtensionCondition"]]]:
        '''url_file_extension_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_file_extension_condition CdnFrontdoorRule#url_file_extension_condition}
        '''
        result = self._values.get("url_file_extension_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFileExtensionCondition"]]], result)

    @builtins.property
    def url_filename_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFilenameCondition"]]]:
        '''url_filename_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_filename_condition CdnFrontdoorRule#url_filename_condition}
        '''
        result = self._values.get("url_filename_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFilenameCondition"]]], result)

    @builtins.property
    def url_path_condition(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlPathCondition"]]]:
        '''url_path_condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#url_path_condition CdnFrontdoorRule#url_path_condition}
        '''
        result = self._values.get("url_path_condition")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlPathCondition"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsClientPortCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
    },
)
class CdnFrontdoorRuleConditionsClientPortCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsClientPortCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsClientPortCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsClientPortConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsClientPortConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsClientPortConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsClientPortConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsClientPortConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsClientPortConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsClientPortCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsClientPortCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsClientPortCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsClientPortConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsClientPortConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsClientPortConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsClientPortCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsClientPortCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsClientPortCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsClientPortConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsCookiesCondition",
    jsii_struct_bases=[],
    name_mapping={
        "cookie_name": "cookieName",
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsCookiesCondition:
    def __init__(
        self,
        *,
        cookie_name: builtins.str,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cookie_name CdnFrontdoorRule#cookie_name}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsCookiesCondition.__init__)
            check_type(argname="argument cookie_name", value=cookie_name, expected_type=type_hints["cookie_name"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "cookie_name": cookie_name,
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def cookie_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cookie_name CdnFrontdoorRule#cookie_name}.'''
        result = self._values.get("cookie_name")
        assert result is not None, "Required property 'cookie_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsCookiesCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsCookiesConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsCookiesConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsCookiesConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsCookiesConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsCookiesConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsCookiesConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsCookiesCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsCookiesCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsCookiesCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsCookiesConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsCookiesConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsCookiesConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="cookieNameInput")
    def cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieName")
    def cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieName"))

    @cookie_name.setter
    def cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionOutputReference, "cookie_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieName", value)

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsCookiesCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsCookiesCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsCookiesCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsCookiesConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsHostNameCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsHostNameCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHostNameCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsHostNameCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsHostNameConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsHostNameConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHostNameConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsHostNameConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHostNameConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsHostNameConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHostNameCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHostNameCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHostNameCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsHostNameConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsHostNameConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHostNameConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsHostNameCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsHostNameCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsHostNameCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHostNameConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsHttpVersionCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnFrontdoorRuleConditionsHttpVersionCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHttpVersionCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsHttpVersionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsHttpVersionConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsHttpVersionConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHttpVersionConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHttpVersionConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHttpVersionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHttpVersionCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHttpVersionCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsHttpVersionCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsHttpVersionCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsHttpVersionCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsIsDeviceCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnFrontdoorRuleConditionsIsDeviceCondition:
    def __init__(
        self,
        *,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsIsDeviceCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsIsDeviceCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsIsDeviceConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsIsDeviceConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsIsDeviceConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsIsDeviceConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsIsDeviceCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsIsDeviceCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsIsDeviceCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsIsDeviceCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsIsDeviceCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsIsDeviceCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putClientPortCondition")
    def put_client_port_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorRuleConditionsClientPortCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_client_port_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putClientPortCondition", [value]))

    @jsii.member(jsii_name="putCookiesCondition")
    def put_cookies_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorRuleConditionsCookiesCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_cookies_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCookiesCondition", [value]))

    @jsii.member(jsii_name="putHostNameCondition")
    def put_host_name_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorRuleConditionsHostNameCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_host_name_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostNameCondition", [value]))

    @jsii.member(jsii_name="putHttpVersionCondition")
    def put_http_version_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorRuleConditionsHttpVersionCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_http_version_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpVersionCondition", [value]))

    @jsii.member(jsii_name="putIsDeviceCondition")
    def put_is_device_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CdnFrontdoorRuleConditionsIsDeviceCondition, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_is_device_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIsDeviceCondition", [value]))

    @jsii.member(jsii_name="putPostArgsCondition")
    def put_post_args_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsPostArgsCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_post_args_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPostArgsCondition", [value]))

    @jsii.member(jsii_name="putQueryStringCondition")
    def put_query_string_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsQueryStringCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_query_string_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryStringCondition", [value]))

    @jsii.member(jsii_name="putRemoteAddressCondition")
    def put_remote_address_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRemoteAddressCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_remote_address_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRemoteAddressCondition", [value]))

    @jsii.member(jsii_name="putRequestBodyCondition")
    def put_request_body_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestBodyCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_request_body_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestBodyCondition", [value]))

    @jsii.member(jsii_name="putRequestHeaderCondition")
    def put_request_header_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestHeaderCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_request_header_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestHeaderCondition", [value]))

    @jsii.member(jsii_name="putRequestMethodCondition")
    def put_request_method_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestMethodCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_request_method_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestMethodCondition", [value]))

    @jsii.member(jsii_name="putRequestSchemeCondition")
    def put_request_scheme_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestSchemeCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_request_scheme_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestSchemeCondition", [value]))

    @jsii.member(jsii_name="putRequestUriCondition")
    def put_request_uri_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsRequestUriCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_request_uri_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequestUriCondition", [value]))

    @jsii.member(jsii_name="putServerPortCondition")
    def put_server_port_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsServerPortCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_server_port_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServerPortCondition", [value]))

    @jsii.member(jsii_name="putSocketAddressCondition")
    def put_socket_address_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsSocketAddressCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_socket_address_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSocketAddressCondition", [value]))

    @jsii.member(jsii_name="putSslProtocolCondition")
    def put_ssl_protocol_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsSslProtocolCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_ssl_protocol_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSslProtocolCondition", [value]))

    @jsii.member(jsii_name="putUrlFileExtensionCondition")
    def put_url_file_extension_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlFileExtensionCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_url_file_extension_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlFileExtensionCondition", [value]))

    @jsii.member(jsii_name="putUrlFilenameCondition")
    def put_url_filename_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlFilenameCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_url_filename_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlFilenameCondition", [value]))

    @jsii.member(jsii_name="putUrlPathCondition")
    def put_url_path_condition(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CdnFrontdoorRuleConditionsUrlPathCondition", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsOutputReference.put_url_path_condition)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlPathCondition", [value]))

    @jsii.member(jsii_name="resetClientPortCondition")
    def reset_client_port_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientPortCondition", []))

    @jsii.member(jsii_name="resetCookiesCondition")
    def reset_cookies_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookiesCondition", []))

    @jsii.member(jsii_name="resetHostNameCondition")
    def reset_host_name_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostNameCondition", []))

    @jsii.member(jsii_name="resetHttpVersionCondition")
    def reset_http_version_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpVersionCondition", []))

    @jsii.member(jsii_name="resetIsDeviceCondition")
    def reset_is_device_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDeviceCondition", []))

    @jsii.member(jsii_name="resetPostArgsCondition")
    def reset_post_args_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostArgsCondition", []))

    @jsii.member(jsii_name="resetQueryStringCondition")
    def reset_query_string_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryStringCondition", []))

    @jsii.member(jsii_name="resetRemoteAddressCondition")
    def reset_remote_address_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoteAddressCondition", []))

    @jsii.member(jsii_name="resetRequestBodyCondition")
    def reset_request_body_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestBodyCondition", []))

    @jsii.member(jsii_name="resetRequestHeaderCondition")
    def reset_request_header_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestHeaderCondition", []))

    @jsii.member(jsii_name="resetRequestMethodCondition")
    def reset_request_method_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestMethodCondition", []))

    @jsii.member(jsii_name="resetRequestSchemeCondition")
    def reset_request_scheme_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestSchemeCondition", []))

    @jsii.member(jsii_name="resetRequestUriCondition")
    def reset_request_uri_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestUriCondition", []))

    @jsii.member(jsii_name="resetServerPortCondition")
    def reset_server_port_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerPortCondition", []))

    @jsii.member(jsii_name="resetSocketAddressCondition")
    def reset_socket_address_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSocketAddressCondition", []))

    @jsii.member(jsii_name="resetSslProtocolCondition")
    def reset_ssl_protocol_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslProtocolCondition", []))

    @jsii.member(jsii_name="resetUrlFileExtensionCondition")
    def reset_url_file_extension_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlFileExtensionCondition", []))

    @jsii.member(jsii_name="resetUrlFilenameCondition")
    def reset_url_filename_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlFilenameCondition", []))

    @jsii.member(jsii_name="resetUrlPathCondition")
    def reset_url_path_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlPathCondition", []))

    @builtins.property
    @jsii.member(jsii_name="clientPortCondition")
    def client_port_condition(
        self,
    ) -> CdnFrontdoorRuleConditionsClientPortConditionList:
        return typing.cast(CdnFrontdoorRuleConditionsClientPortConditionList, jsii.get(self, "clientPortCondition"))

    @builtins.property
    @jsii.member(jsii_name="cookiesCondition")
    def cookies_condition(self) -> CdnFrontdoorRuleConditionsCookiesConditionList:
        return typing.cast(CdnFrontdoorRuleConditionsCookiesConditionList, jsii.get(self, "cookiesCondition"))

    @builtins.property
    @jsii.member(jsii_name="hostNameCondition")
    def host_name_condition(self) -> CdnFrontdoorRuleConditionsHostNameConditionList:
        return typing.cast(CdnFrontdoorRuleConditionsHostNameConditionList, jsii.get(self, "hostNameCondition"))

    @builtins.property
    @jsii.member(jsii_name="httpVersionCondition")
    def http_version_condition(
        self,
    ) -> CdnFrontdoorRuleConditionsHttpVersionConditionList:
        return typing.cast(CdnFrontdoorRuleConditionsHttpVersionConditionList, jsii.get(self, "httpVersionCondition"))

    @builtins.property
    @jsii.member(jsii_name="isDeviceCondition")
    def is_device_condition(self) -> CdnFrontdoorRuleConditionsIsDeviceConditionList:
        return typing.cast(CdnFrontdoorRuleConditionsIsDeviceConditionList, jsii.get(self, "isDeviceCondition"))

    @builtins.property
    @jsii.member(jsii_name="postArgsCondition")
    def post_args_condition(self) -> "CdnFrontdoorRuleConditionsPostArgsConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsPostArgsConditionList", jsii.get(self, "postArgsCondition"))

    @builtins.property
    @jsii.member(jsii_name="queryStringCondition")
    def query_string_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsQueryStringConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsQueryStringConditionList", jsii.get(self, "queryStringCondition"))

    @builtins.property
    @jsii.member(jsii_name="remoteAddressCondition")
    def remote_address_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsRemoteAddressConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsRemoteAddressConditionList", jsii.get(self, "remoteAddressCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestBodyCondition")
    def request_body_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsRequestBodyConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsRequestBodyConditionList", jsii.get(self, "requestBodyCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderCondition")
    def request_header_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsRequestHeaderConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsRequestHeaderConditionList", jsii.get(self, "requestHeaderCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestMethodCondition")
    def request_method_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsRequestMethodConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsRequestMethodConditionList", jsii.get(self, "requestMethodCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestSchemeCondition")
    def request_scheme_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsRequestSchemeConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsRequestSchemeConditionList", jsii.get(self, "requestSchemeCondition"))

    @builtins.property
    @jsii.member(jsii_name="requestUriCondition")
    def request_uri_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsRequestUriConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsRequestUriConditionList", jsii.get(self, "requestUriCondition"))

    @builtins.property
    @jsii.member(jsii_name="serverPortCondition")
    def server_port_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsServerPortConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsServerPortConditionList", jsii.get(self, "serverPortCondition"))

    @builtins.property
    @jsii.member(jsii_name="socketAddressCondition")
    def socket_address_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsSocketAddressConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsSocketAddressConditionList", jsii.get(self, "socketAddressCondition"))

    @builtins.property
    @jsii.member(jsii_name="sslProtocolCondition")
    def ssl_protocol_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsSslProtocolConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsSslProtocolConditionList", jsii.get(self, "sslProtocolCondition"))

    @builtins.property
    @jsii.member(jsii_name="urlFileExtensionCondition")
    def url_file_extension_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsUrlFileExtensionConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsUrlFileExtensionConditionList", jsii.get(self, "urlFileExtensionCondition"))

    @builtins.property
    @jsii.member(jsii_name="urlFilenameCondition")
    def url_filename_condition(
        self,
    ) -> "CdnFrontdoorRuleConditionsUrlFilenameConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsUrlFilenameConditionList", jsii.get(self, "urlFilenameCondition"))

    @builtins.property
    @jsii.member(jsii_name="urlPathCondition")
    def url_path_condition(self) -> "CdnFrontdoorRuleConditionsUrlPathConditionList":
        return typing.cast("CdnFrontdoorRuleConditionsUrlPathConditionList", jsii.get(self, "urlPathCondition"))

    @builtins.property
    @jsii.member(jsii_name="clientPortConditionInput")
    def client_port_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsClientPortCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsClientPortCondition]]], jsii.get(self, "clientPortConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="cookiesConditionInput")
    def cookies_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsCookiesCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsCookiesCondition]]], jsii.get(self, "cookiesConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameConditionInput")
    def host_name_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHostNameCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHostNameCondition]]], jsii.get(self, "hostNameConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="httpVersionConditionInput")
    def http_version_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHttpVersionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsHttpVersionCondition]]], jsii.get(self, "httpVersionConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="isDeviceConditionInput")
    def is_device_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsIsDeviceCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsIsDeviceCondition]]], jsii.get(self, "isDeviceConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="postArgsConditionInput")
    def post_args_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsPostArgsCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsPostArgsCondition"]]], jsii.get(self, "postArgsConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="queryStringConditionInput")
    def query_string_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsQueryStringCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsQueryStringCondition"]]], jsii.get(self, "queryStringConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteAddressConditionInput")
    def remote_address_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRemoteAddressCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRemoteAddressCondition"]]], jsii.get(self, "remoteAddressConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestBodyConditionInput")
    def request_body_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestBodyCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestBodyCondition"]]], jsii.get(self, "requestBodyConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestHeaderConditionInput")
    def request_header_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestHeaderCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestHeaderCondition"]]], jsii.get(self, "requestHeaderConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestMethodConditionInput")
    def request_method_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestMethodCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestMethodCondition"]]], jsii.get(self, "requestMethodConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestSchemeConditionInput")
    def request_scheme_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestSchemeCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestSchemeCondition"]]], jsii.get(self, "requestSchemeConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="requestUriConditionInput")
    def request_uri_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestUriCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsRequestUriCondition"]]], jsii.get(self, "requestUriConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="serverPortConditionInput")
    def server_port_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsServerPortCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsServerPortCondition"]]], jsii.get(self, "serverPortConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="socketAddressConditionInput")
    def socket_address_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSocketAddressCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSocketAddressCondition"]]], jsii.get(self, "socketAddressConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="sslProtocolConditionInput")
    def ssl_protocol_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSslProtocolCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsSslProtocolCondition"]]], jsii.get(self, "sslProtocolConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlFileExtensionConditionInput")
    def url_file_extension_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFileExtensionCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFileExtensionCondition"]]], jsii.get(self, "urlFileExtensionConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlFilenameConditionInput")
    def url_filename_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFilenameCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlFilenameCondition"]]], jsii.get(self, "urlFilenameConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="urlPathConditionInput")
    def url_path_condition_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlPathCondition"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CdnFrontdoorRuleConditionsUrlPathCondition"]]], jsii.get(self, "urlPathConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CdnFrontdoorRuleConditions]:
        return typing.cast(typing.Optional[CdnFrontdoorRuleConditions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorRuleConditions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsPostArgsCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "post_args_name": "postArgsName",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsPostArgsCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        post_args_name: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param post_args_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#post_args_name CdnFrontdoorRule#post_args_name}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsPostArgsCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument post_args_name", value=post_args_name, expected_type=type_hints["post_args_name"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "post_args_name": post_args_name,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def post_args_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#post_args_name CdnFrontdoorRule#post_args_name}.'''
        result = self._values.get("post_args_name")
        assert result is not None, "Required property 'post_args_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsPostArgsCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsPostArgsConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsPostArgsConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsPostArgsConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsPostArgsConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsPostArgsConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsPostArgsConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsPostArgsCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsPostArgsCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsPostArgsCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsPostArgsConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsPostArgsConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsPostArgsConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="postArgsNameInput")
    def post_args_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postArgsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="postArgsName")
    def post_args_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "postArgsName"))

    @post_args_name.setter
    def post_args_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionOutputReference, "post_args_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postArgsName", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsPostArgsCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsPostArgsCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsPostArgsCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsPostArgsConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsQueryStringCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsQueryStringCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsQueryStringCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsQueryStringCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsQueryStringConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsQueryStringConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsQueryStringConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsQueryStringConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsQueryStringConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsQueryStringConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsQueryStringCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsQueryStringCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsQueryStringCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsQueryStringConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsQueryStringConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsQueryStringConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsQueryStringCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsQueryStringCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsQueryStringCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsQueryStringConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRemoteAddressCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnFrontdoorRuleConditionsRemoteAddressCondition:
    def __init__(
        self,
        *,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRemoteAddressCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsRemoteAddressCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsRemoteAddressConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRemoteAddressConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRemoteAddressConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRemoteAddressConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRemoteAddressCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRemoteAddressCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRemoteAddressCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRemoteAddressCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRemoteAddressCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRemoteAddressCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestBodyCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "operator": "operator",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsRequestBodyCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        operator: builtins.str,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestBodyCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
            "operator": operator,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsRequestBodyCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsRequestBodyConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestBodyConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestBodyConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestBodyConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestBodyCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestBodyCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestBodyCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestBodyCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestBodyCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestBodyCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestHeaderCondition",
    jsii_struct_bases=[],
    name_mapping={
        "header_name": "headerName",
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsRequestHeaderCondition:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param header_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_name CdnFrontdoorRule#header_name}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestHeaderCondition.__init__)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "header_name": header_name,
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def header_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#header_name CdnFrontdoorRule#header_name}.'''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsRequestHeaderCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsRequestHeaderConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestHeaderConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestHeaderConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestHeaderConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestHeaderCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestHeaderCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestHeaderCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="headerNameInput")
    def header_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="headerName")
    def header_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerName"))

    @header_name.setter
    def header_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference, "header_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headerName", value)

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestHeaderCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestHeaderCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestHeaderCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestMethodCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnFrontdoorRuleConditionsRequestMethodCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestMethodCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsRequestMethodCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsRequestMethodConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestMethodConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestMethodConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestMethodConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestMethodCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestMethodCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestMethodCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestMethodCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestMethodCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestMethodCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestSchemeCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnFrontdoorRuleConditionsRequestSchemeCondition:
    def __init__(
        self,
        *,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestSchemeCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsRequestSchemeCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsRequestSchemeConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestSchemeConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestSchemeConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestSchemeConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestSchemeCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestSchemeCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestSchemeCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestSchemeCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestSchemeCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestSchemeCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestUriCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsRequestUriCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestUriCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsRequestUriCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsRequestUriConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestUriConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestUriConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsRequestUriConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestUriConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsRequestUriConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestUriCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestUriCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsRequestUriCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsRequestUriConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsRequestUriConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsRequestUriConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestUriCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestUriCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsRequestUriCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsRequestUriConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsServerPortCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "operator": "operator",
        "negate_condition": "negateCondition",
    },
)
class CdnFrontdoorRuleConditionsServerPortCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        operator: builtins.str,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsServerPortCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
            "operator": operator,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsServerPortCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsServerPortConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsServerPortConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsServerPortConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsServerPortConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsServerPortConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsServerPortConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsServerPortCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsServerPortCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsServerPortCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsServerPortConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsServerPortConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsServerPortConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsServerPortCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsServerPortCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsServerPortCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsServerPortConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsSocketAddressCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnFrontdoorRuleConditionsSocketAddressCondition:
    def __init__(
        self,
        *,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSocketAddressCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsSocketAddressCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsSocketAddressConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsSocketAddressConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSocketAddressConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSocketAddressConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsSocketAddressCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsSocketAddressCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsSocketAddressCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsSocketAddressCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsSocketAddressCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsSocketAddressCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsSslProtocolCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "operator": "operator",
    },
)
class CdnFrontdoorRuleConditionsSslProtocolCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operator: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSslProtocolCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if operator is not None:
            self._values["operator"] = operator

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsSslProtocolCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsSslProtocolConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsSslProtocolConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSslProtocolConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSslProtocolConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsSslProtocolCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsSslProtocolCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsSslProtocolCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsSslProtocolCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsSslProtocolCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsSslProtocolCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlFileExtensionCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "operator": "operator",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsUrlFileExtensionCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        operator: builtins.str,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFileExtensionCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
            "operator": operator,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsUrlFileExtensionCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsUrlFileExtensionConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlFileExtensionConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFileExtensionConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFileExtensionConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlFileExtensionCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlFileExtensionCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlFileExtensionCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlFileExtensionCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlFileExtensionCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlFileExtensionCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlFilenameCondition",
    jsii_struct_bases=[],
    name_mapping={
        "match_values": "matchValues",
        "operator": "operator",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsUrlFilenameCondition:
    def __init__(
        self,
        *,
        match_values: typing.Sequence[builtins.str],
        operator: builtins.str,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFilenameCondition.__init__)
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "match_values": match_values,
            "operator": operator,
        }
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def match_values(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        assert result is not None, "Required property 'match_values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsUrlFilenameCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsUrlFilenameConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlFilenameConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFilenameConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFilenameConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlFilenameCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlFilenameCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlFilenameCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlFilenameCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlFilenameCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlFilenameCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlPathCondition",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "match_values": "matchValues",
        "negate_condition": "negateCondition",
        "transforms": "transforms",
    },
)
class CdnFrontdoorRuleConditionsUrlPathCondition:
    def __init__(
        self,
        *,
        operator: builtins.str,
        match_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate_condition: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        transforms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.
        :param match_values: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.
        :param negate_condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.
        :param transforms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlPathCondition.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument match_values", value=match_values, expected_type=type_hints["match_values"])
            check_type(argname="argument negate_condition", value=negate_condition, expected_type=type_hints["negate_condition"])
            check_type(argname="argument transforms", value=transforms, expected_type=type_hints["transforms"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
        }
        if match_values is not None:
            self._values["match_values"] = match_values
        if negate_condition is not None:
            self._values["negate_condition"] = negate_condition
        if transforms is not None:
            self._values["transforms"] = transforms

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#operator CdnFrontdoorRule#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#match_values CdnFrontdoorRule#match_values}.'''
        result = self._values.get("match_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate_condition(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#negate_condition CdnFrontdoorRule#negate_condition}.'''
        result = self._values.get("negate_condition")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def transforms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#transforms CdnFrontdoorRule#transforms}.'''
        result = self._values.get("transforms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConditionsUrlPathCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleConditionsUrlPathConditionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlPathConditionList",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlPathConditionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CdnFrontdoorRuleConditionsUrlPathConditionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlPathConditionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CdnFrontdoorRuleConditionsUrlPathConditionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlPathCondition]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlPathCondition]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CdnFrontdoorRuleConditionsUrlPathCondition]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CdnFrontdoorRuleConditionsUrlPathConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConditionsUrlPathConditionOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConditionsUrlPathConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMatchValues")
    def reset_match_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchValues", []))

    @jsii.member(jsii_name="resetNegateCondition")
    def reset_negate_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegateCondition", []))

    @jsii.member(jsii_name="resetTransforms")
    def reset_transforms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTransforms", []))

    @builtins.property
    @jsii.member(jsii_name="matchValuesInput")
    def match_values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="negateConditionInput")
    def negate_condition_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateConditionInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="transformsInput")
    def transforms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "transformsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchValues")
    def match_values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchValues"))

    @match_values.setter
    def match_values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionOutputReference, "match_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchValues", value)

    @builtins.property
    @jsii.member(jsii_name="negateCondition")
    def negate_condition(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negateCondition"))

    @negate_condition.setter
    def negate_condition(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionOutputReference, "negate_condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negateCondition", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="transforms")
    def transforms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "transforms"))

    @transforms.setter
    def transforms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionOutputReference, "transforms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transforms", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlPathCondition, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlPathCondition, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleConditionsUrlPathCondition, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleConditionsUrlPathConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "actions": "actions",
        "cdn_frontdoor_rule_set_id": "cdnFrontdoorRuleSetId",
        "name": "name",
        "order": "order",
        "behavior_on_match": "behaviorOnMatch",
        "conditions": "conditions",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class CdnFrontdoorRuleConfig(cdktf.TerraformMetaArguments):
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
        actions: typing.Union[CdnFrontdoorRuleActions, typing.Dict[str, typing.Any]],
        cdn_frontdoor_rule_set_id: builtins.str,
        name: builtins.str,
        order: jsii.Number,
        behavior_on_match: typing.Optional[builtins.str] = None,
        conditions: typing.Optional[typing.Union[CdnFrontdoorRuleConditions, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#actions CdnFrontdoorRule#actions}
        :param cdn_frontdoor_rule_set_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cdn_frontdoor_rule_set_id CdnFrontdoorRule#cdn_frontdoor_rule_set_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#name CdnFrontdoorRule#name}.
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#order CdnFrontdoorRule#order}.
        :param behavior_on_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#behavior_on_match CdnFrontdoorRule#behavior_on_match}.
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#conditions CdnFrontdoorRule#conditions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#id CdnFrontdoorRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#timeouts CdnFrontdoorRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(actions, dict):
            actions = CdnFrontdoorRuleActions(**actions)
        if isinstance(conditions, dict):
            conditions = CdnFrontdoorRuleConditions(**conditions)
        if isinstance(timeouts, dict):
            timeouts = CdnFrontdoorRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument cdn_frontdoor_rule_set_id", value=cdn_frontdoor_rule_set_id, expected_type=type_hints["cdn_frontdoor_rule_set_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument behavior_on_match", value=behavior_on_match, expected_type=type_hints["behavior_on_match"])
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "actions": actions,
            "cdn_frontdoor_rule_set_id": cdn_frontdoor_rule_set_id,
            "name": name,
            "order": order,
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
        if behavior_on_match is not None:
            self._values["behavior_on_match"] = behavior_on_match
        if conditions is not None:
            self._values["conditions"] = conditions
        if id is not None:
            self._values["id"] = id
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
    def actions(self) -> CdnFrontdoorRuleActions:
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#actions CdnFrontdoorRule#actions}
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(CdnFrontdoorRuleActions, result)

    @builtins.property
    def cdn_frontdoor_rule_set_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#cdn_frontdoor_rule_set_id CdnFrontdoorRule#cdn_frontdoor_rule_set_id}.'''
        result = self._values.get("cdn_frontdoor_rule_set_id")
        assert result is not None, "Required property 'cdn_frontdoor_rule_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#name CdnFrontdoorRule#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def order(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#order CdnFrontdoorRule#order}.'''
        result = self._values.get("order")
        assert result is not None, "Required property 'order' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def behavior_on_match(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#behavior_on_match CdnFrontdoorRule#behavior_on_match}.'''
        result = self._values.get("behavior_on_match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conditions(self) -> typing.Optional[CdnFrontdoorRuleConditions]:
        '''conditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#conditions CdnFrontdoorRule#conditions}
        '''
        result = self._values.get("conditions")
        return typing.cast(typing.Optional[CdnFrontdoorRuleConditions], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#id CdnFrontdoorRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CdnFrontdoorRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#timeouts CdnFrontdoorRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CdnFrontdoorRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CdnFrontdoorRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#create CdnFrontdoorRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#delete CdnFrontdoorRule#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#read CdnFrontdoorRule#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#update CdnFrontdoorRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorRuleTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#create CdnFrontdoorRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#delete CdnFrontdoorRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#read CdnFrontdoorRule#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_rule#update CdnFrontdoorRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorRuleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorRule.CdnFrontdoorRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorRuleTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorRuleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorRuleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorRuleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorRuleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CdnFrontdoorRule",
    "CdnFrontdoorRuleActions",
    "CdnFrontdoorRuleActionsOutputReference",
    "CdnFrontdoorRuleActionsRequestHeaderAction",
    "CdnFrontdoorRuleActionsRequestHeaderActionList",
    "CdnFrontdoorRuleActionsRequestHeaderActionOutputReference",
    "CdnFrontdoorRuleActionsResponseHeaderAction",
    "CdnFrontdoorRuleActionsResponseHeaderActionList",
    "CdnFrontdoorRuleActionsResponseHeaderActionOutputReference",
    "CdnFrontdoorRuleActionsRouteConfigurationOverrideAction",
    "CdnFrontdoorRuleActionsRouteConfigurationOverrideActionOutputReference",
    "CdnFrontdoorRuleActionsUrlRedirectAction",
    "CdnFrontdoorRuleActionsUrlRedirectActionOutputReference",
    "CdnFrontdoorRuleActionsUrlRewriteAction",
    "CdnFrontdoorRuleActionsUrlRewriteActionOutputReference",
    "CdnFrontdoorRuleConditions",
    "CdnFrontdoorRuleConditionsClientPortCondition",
    "CdnFrontdoorRuleConditionsClientPortConditionList",
    "CdnFrontdoorRuleConditionsClientPortConditionOutputReference",
    "CdnFrontdoorRuleConditionsCookiesCondition",
    "CdnFrontdoorRuleConditionsCookiesConditionList",
    "CdnFrontdoorRuleConditionsCookiesConditionOutputReference",
    "CdnFrontdoorRuleConditionsHostNameCondition",
    "CdnFrontdoorRuleConditionsHostNameConditionList",
    "CdnFrontdoorRuleConditionsHostNameConditionOutputReference",
    "CdnFrontdoorRuleConditionsHttpVersionCondition",
    "CdnFrontdoorRuleConditionsHttpVersionConditionList",
    "CdnFrontdoorRuleConditionsHttpVersionConditionOutputReference",
    "CdnFrontdoorRuleConditionsIsDeviceCondition",
    "CdnFrontdoorRuleConditionsIsDeviceConditionList",
    "CdnFrontdoorRuleConditionsIsDeviceConditionOutputReference",
    "CdnFrontdoorRuleConditionsOutputReference",
    "CdnFrontdoorRuleConditionsPostArgsCondition",
    "CdnFrontdoorRuleConditionsPostArgsConditionList",
    "CdnFrontdoorRuleConditionsPostArgsConditionOutputReference",
    "CdnFrontdoorRuleConditionsQueryStringCondition",
    "CdnFrontdoorRuleConditionsQueryStringConditionList",
    "CdnFrontdoorRuleConditionsQueryStringConditionOutputReference",
    "CdnFrontdoorRuleConditionsRemoteAddressCondition",
    "CdnFrontdoorRuleConditionsRemoteAddressConditionList",
    "CdnFrontdoorRuleConditionsRemoteAddressConditionOutputReference",
    "CdnFrontdoorRuleConditionsRequestBodyCondition",
    "CdnFrontdoorRuleConditionsRequestBodyConditionList",
    "CdnFrontdoorRuleConditionsRequestBodyConditionOutputReference",
    "CdnFrontdoorRuleConditionsRequestHeaderCondition",
    "CdnFrontdoorRuleConditionsRequestHeaderConditionList",
    "CdnFrontdoorRuleConditionsRequestHeaderConditionOutputReference",
    "CdnFrontdoorRuleConditionsRequestMethodCondition",
    "CdnFrontdoorRuleConditionsRequestMethodConditionList",
    "CdnFrontdoorRuleConditionsRequestMethodConditionOutputReference",
    "CdnFrontdoorRuleConditionsRequestSchemeCondition",
    "CdnFrontdoorRuleConditionsRequestSchemeConditionList",
    "CdnFrontdoorRuleConditionsRequestSchemeConditionOutputReference",
    "CdnFrontdoorRuleConditionsRequestUriCondition",
    "CdnFrontdoorRuleConditionsRequestUriConditionList",
    "CdnFrontdoorRuleConditionsRequestUriConditionOutputReference",
    "CdnFrontdoorRuleConditionsServerPortCondition",
    "CdnFrontdoorRuleConditionsServerPortConditionList",
    "CdnFrontdoorRuleConditionsServerPortConditionOutputReference",
    "CdnFrontdoorRuleConditionsSocketAddressCondition",
    "CdnFrontdoorRuleConditionsSocketAddressConditionList",
    "CdnFrontdoorRuleConditionsSocketAddressConditionOutputReference",
    "CdnFrontdoorRuleConditionsSslProtocolCondition",
    "CdnFrontdoorRuleConditionsSslProtocolConditionList",
    "CdnFrontdoorRuleConditionsSslProtocolConditionOutputReference",
    "CdnFrontdoorRuleConditionsUrlFileExtensionCondition",
    "CdnFrontdoorRuleConditionsUrlFileExtensionConditionList",
    "CdnFrontdoorRuleConditionsUrlFileExtensionConditionOutputReference",
    "CdnFrontdoorRuleConditionsUrlFilenameCondition",
    "CdnFrontdoorRuleConditionsUrlFilenameConditionList",
    "CdnFrontdoorRuleConditionsUrlFilenameConditionOutputReference",
    "CdnFrontdoorRuleConditionsUrlPathCondition",
    "CdnFrontdoorRuleConditionsUrlPathConditionList",
    "CdnFrontdoorRuleConditionsUrlPathConditionOutputReference",
    "CdnFrontdoorRuleConfig",
    "CdnFrontdoorRuleTimeouts",
    "CdnFrontdoorRuleTimeoutsOutputReference",
]

publication.publish()
