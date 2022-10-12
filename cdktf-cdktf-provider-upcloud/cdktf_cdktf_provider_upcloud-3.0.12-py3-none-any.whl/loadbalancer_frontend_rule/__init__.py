'''
# `upcloud_loadbalancer_frontend_rule`

Refer to the Terraform Registory for docs: [`upcloud_loadbalancer_frontend_rule`](https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule).
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


class LoadbalancerFrontendRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule upcloud_loadbalancer_frontend_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        frontend: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        actions: typing.Optional[typing.Union["LoadbalancerFrontendRuleActions", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        matchers: typing.Optional[typing.Union["LoadbalancerFrontendRuleMatchers", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule upcloud_loadbalancer_frontend_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param frontend: ID of the load balancer frontend to which the rule is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#frontend LoadbalancerFrontendRule#frontend}
        :param name: The name of the frontend rule must be unique within the load balancer service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        :param priority: Rule with the higher priority goes first. Rules with the same priority processed in alphabetical order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#priority LoadbalancerFrontendRule#priority}
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#actions LoadbalancerFrontendRule#actions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#id LoadbalancerFrontendRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param matchers: matchers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#matchers LoadbalancerFrontendRule#matchers}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LoadbalancerFrontendRuleConfig(
            frontend=frontend,
            name=name,
            priority=priority,
            actions=actions,
            id=id,
            matchers=matchers,
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
        http_redirect: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsHttpRedirect", typing.Dict[str, typing.Any]]]]] = None,
        http_return: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsHttpReturn", typing.Dict[str, typing.Any]]]]] = None,
        set_forwarded_headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsSetForwardedHeaders", typing.Dict[str, typing.Any]]]]] = None,
        tcp_reject: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsTcpReject", typing.Dict[str, typing.Any]]]]] = None,
        use_backend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsUseBackend", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param http_redirect: http_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_redirect LoadbalancerFrontendRule#http_redirect}
        :param http_return: http_return block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_return LoadbalancerFrontendRule#http_return}
        :param set_forwarded_headers: set_forwarded_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#set_forwarded_headers LoadbalancerFrontendRule#set_forwarded_headers}
        :param tcp_reject: tcp_reject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#tcp_reject LoadbalancerFrontendRule#tcp_reject}
        :param use_backend: use_backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#use_backend LoadbalancerFrontendRule#use_backend}
        '''
        value = LoadbalancerFrontendRuleActions(
            http_redirect=http_redirect,
            http_return=http_return,
            set_forwarded_headers=set_forwarded_headers,
            tcp_reject=tcp_reject,
            use_backend=use_backend,
        )

        return typing.cast(None, jsii.invoke(self, "putActions", [value]))

    @jsii.member(jsii_name="putMatchers")
    def put_matchers(
        self,
        *,
        body_size: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersBodySize", typing.Dict[str, typing.Any]]]]] = None,
        body_size_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersBodySizeRange", typing.Dict[str, typing.Any]]]]] = None,
        cookie: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersCookie", typing.Dict[str, typing.Any]]]]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersHeader", typing.Dict[str, typing.Any]]]]] = None,
        host: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersHost", typing.Dict[str, typing.Any]]]]] = None,
        http_method: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersHttpMethod", typing.Dict[str, typing.Any]]]]] = None,
        num_members_up: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersNumMembersUp", typing.Dict[str, typing.Any]]]]] = None,
        path: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersPath", typing.Dict[str, typing.Any]]]]] = None,
        src_ip: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcIp", typing.Dict[str, typing.Any]]]]] = None,
        src_port: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcPort", typing.Dict[str, typing.Any]]]]] = None,
        src_port_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcPortRange", typing.Dict[str, typing.Any]]]]] = None,
        url: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrl", typing.Dict[str, typing.Any]]]]] = None,
        url_param: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrlParam", typing.Dict[str, typing.Any]]]]] = None,
        url_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrlQuery", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param body_size: body_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#body_size LoadbalancerFrontendRule#body_size}
        :param body_size_range: body_size_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#body_size_range LoadbalancerFrontendRule#body_size_range}
        :param cookie: cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#cookie LoadbalancerFrontendRule#cookie}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#header LoadbalancerFrontendRule#header}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#host LoadbalancerFrontendRule#host}
        :param http_method: http_method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_method LoadbalancerFrontendRule#http_method}
        :param num_members_up: num_members_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#num_members_up LoadbalancerFrontendRule#num_members_up}
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#path LoadbalancerFrontendRule#path}
        :param src_ip: src_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_ip LoadbalancerFrontendRule#src_ip}
        :param src_port: src_port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_port LoadbalancerFrontendRule#src_port}
        :param src_port_range: src_port_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_port_range LoadbalancerFrontendRule#src_port_range}
        :param url: url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url LoadbalancerFrontendRule#url}
        :param url_param: url_param block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url_param LoadbalancerFrontendRule#url_param}
        :param url_query: url_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url_query LoadbalancerFrontendRule#url_query}
        '''
        value = LoadbalancerFrontendRuleMatchers(
            body_size=body_size,
            body_size_range=body_size_range,
            cookie=cookie,
            header=header,
            host=host,
            http_method=http_method,
            num_members_up=num_members_up,
            path=path,
            src_ip=src_ip,
            src_port=src_port,
            src_port_range=src_port_range,
            url=url,
            url_param=url_param,
            url_query=url_query,
        )

        return typing.cast(None, jsii.invoke(self, "putMatchers", [value]))

    @jsii.member(jsii_name="resetActions")
    def reset_actions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActions", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMatchers")
    def reset_matchers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchers", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(self) -> "LoadbalancerFrontendRuleActionsOutputReference":
        return typing.cast("LoadbalancerFrontendRuleActionsOutputReference", jsii.get(self, "actions"))

    @builtins.property
    @jsii.member(jsii_name="matchers")
    def matchers(self) -> "LoadbalancerFrontendRuleMatchersOutputReference":
        return typing.cast("LoadbalancerFrontendRuleMatchersOutputReference", jsii.get(self, "matchers"))

    @builtins.property
    @jsii.member(jsii_name="actionsInput")
    def actions_input(self) -> typing.Optional["LoadbalancerFrontendRuleActions"]:
        return typing.cast(typing.Optional["LoadbalancerFrontendRuleActions"], jsii.get(self, "actionsInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendInput")
    def frontend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frontendInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchersInput")
    def matchers_input(self) -> typing.Optional["LoadbalancerFrontendRuleMatchers"]:
        return typing.cast(typing.Optional["LoadbalancerFrontendRuleMatchers"], jsii.get(self, "matchersInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="frontend")
    def frontend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontend"))

    @frontend.setter
    def frontend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRule, "frontend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontend", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRule, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActions",
    jsii_struct_bases=[],
    name_mapping={
        "http_redirect": "httpRedirect",
        "http_return": "httpReturn",
        "set_forwarded_headers": "setForwardedHeaders",
        "tcp_reject": "tcpReject",
        "use_backend": "useBackend",
    },
)
class LoadbalancerFrontendRuleActions:
    def __init__(
        self,
        *,
        http_redirect: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsHttpRedirect", typing.Dict[str, typing.Any]]]]] = None,
        http_return: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsHttpReturn", typing.Dict[str, typing.Any]]]]] = None,
        set_forwarded_headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsSetForwardedHeaders", typing.Dict[str, typing.Any]]]]] = None,
        tcp_reject: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsTcpReject", typing.Dict[str, typing.Any]]]]] = None,
        use_backend: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsUseBackend", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param http_redirect: http_redirect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_redirect LoadbalancerFrontendRule#http_redirect}
        :param http_return: http_return block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_return LoadbalancerFrontendRule#http_return}
        :param set_forwarded_headers: set_forwarded_headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#set_forwarded_headers LoadbalancerFrontendRule#set_forwarded_headers}
        :param tcp_reject: tcp_reject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#tcp_reject LoadbalancerFrontendRule#tcp_reject}
        :param use_backend: use_backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#use_backend LoadbalancerFrontendRule#use_backend}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActions.__init__)
            check_type(argname="argument http_redirect", value=http_redirect, expected_type=type_hints["http_redirect"])
            check_type(argname="argument http_return", value=http_return, expected_type=type_hints["http_return"])
            check_type(argname="argument set_forwarded_headers", value=set_forwarded_headers, expected_type=type_hints["set_forwarded_headers"])
            check_type(argname="argument tcp_reject", value=tcp_reject, expected_type=type_hints["tcp_reject"])
            check_type(argname="argument use_backend", value=use_backend, expected_type=type_hints["use_backend"])
        self._values: typing.Dict[str, typing.Any] = {}
        if http_redirect is not None:
            self._values["http_redirect"] = http_redirect
        if http_return is not None:
            self._values["http_return"] = http_return
        if set_forwarded_headers is not None:
            self._values["set_forwarded_headers"] = set_forwarded_headers
        if tcp_reject is not None:
            self._values["tcp_reject"] = tcp_reject
        if use_backend is not None:
            self._values["use_backend"] = use_backend

    @builtins.property
    def http_redirect(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsHttpRedirect"]]]:
        '''http_redirect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_redirect LoadbalancerFrontendRule#http_redirect}
        '''
        result = self._values.get("http_redirect")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsHttpRedirect"]]], result)

    @builtins.property
    def http_return(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsHttpReturn"]]]:
        '''http_return block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_return LoadbalancerFrontendRule#http_return}
        '''
        result = self._values.get("http_return")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsHttpReturn"]]], result)

    @builtins.property
    def set_forwarded_headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsSetForwardedHeaders"]]]:
        '''set_forwarded_headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#set_forwarded_headers LoadbalancerFrontendRule#set_forwarded_headers}
        '''
        result = self._values.get("set_forwarded_headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsSetForwardedHeaders"]]], result)

    @builtins.property
    def tcp_reject(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsTcpReject"]]]:
        '''tcp_reject block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#tcp_reject LoadbalancerFrontendRule#tcp_reject}
        '''
        result = self._values.get("tcp_reject")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsTcpReject"]]], result)

    @builtins.property
    def use_backend(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsUseBackend"]]]:
        '''use_backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#use_backend LoadbalancerFrontendRule#use_backend}
        '''
        result = self._values.get("use_backend")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsUseBackend"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleActions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsHttpRedirect",
    jsii_struct_bases=[],
    name_mapping={"location": "location"},
)
class LoadbalancerFrontendRuleActionsHttpRedirect:
    def __init__(self, *, location: builtins.str) -> None:
        '''
        :param location: Target location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#location LoadbalancerFrontendRule#location}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpRedirect.__init__)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
        }

    @builtins.property
    def location(self) -> builtins.str:
        '''Target location.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#location LoadbalancerFrontendRule#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleActionsHttpRedirect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleActionsHttpRedirectList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsHttpRedirectList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpRedirectList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleActionsHttpRedirectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpRedirectList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleActionsHttpRedirectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpRedirectList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpRedirectList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpRedirectList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpRedirect]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpRedirect]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpRedirect]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpRedirectList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleActionsHttpRedirectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsHttpRedirectOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpRedirectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpRedirectOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsHttpRedirect, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsHttpRedirect, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsHttpRedirect, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpRedirectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsHttpReturn",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "payload": "payload",
        "status": "status",
    },
)
class LoadbalancerFrontendRuleActionsHttpReturn:
    def __init__(
        self,
        *,
        content_type: builtins.str,
        payload: builtins.str,
        status: jsii.Number,
    ) -> None:
        '''
        :param content_type: Content type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#content_type LoadbalancerFrontendRule#content_type}
        :param payload: The payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#payload LoadbalancerFrontendRule#payload}
        :param status: HTTP status code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#status LoadbalancerFrontendRule#status}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpReturn.__init__)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[str, typing.Any] = {
            "content_type": content_type,
            "payload": payload,
            "status": status,
        }

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Content type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#content_type LoadbalancerFrontendRule#content_type}
        '''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def payload(self) -> builtins.str:
        '''The payload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#payload LoadbalancerFrontendRule#payload}
        '''
        result = self._values.get("payload")
        assert result is not None, "Required property 'payload' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> jsii.Number:
        '''HTTP status code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#status LoadbalancerFrontendRule#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleActionsHttpReturn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleActionsHttpReturnList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsHttpReturnList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpReturnList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleActionsHttpReturnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpReturnList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleActionsHttpReturnOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpReturn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpReturn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpReturn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleActionsHttpReturnOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsHttpReturnOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsHttpReturnOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadInput")
    def payload_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="payload")
    def payload(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "payload"))

    @payload.setter
    def payload(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnOutputReference, "payload").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payload", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "status"))

    @status.setter
    def status(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnOutputReference, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsHttpReturn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsHttpReturn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsHttpReturn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsHttpReturnOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleActionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHttpRedirect")
    def put_http_redirect(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleActionsHttpRedirect, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsOutputReference.put_http_redirect)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpRedirect", [value]))

    @jsii.member(jsii_name="putHttpReturn")
    def put_http_return(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleActionsHttpReturn, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsOutputReference.put_http_return)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpReturn", [value]))

    @jsii.member(jsii_name="putSetForwardedHeaders")
    def put_set_forwarded_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsSetForwardedHeaders", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsOutputReference.put_set_forwarded_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSetForwardedHeaders", [value]))

    @jsii.member(jsii_name="putTcpReject")
    def put_tcp_reject(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsTcpReject", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsOutputReference.put_tcp_reject)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTcpReject", [value]))

    @jsii.member(jsii_name="putUseBackend")
    def put_use_backend(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleActionsUseBackend", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsOutputReference.put_use_backend)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUseBackend", [value]))

    @jsii.member(jsii_name="resetHttpRedirect")
    def reset_http_redirect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRedirect", []))

    @jsii.member(jsii_name="resetHttpReturn")
    def reset_http_return(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpReturn", []))

    @jsii.member(jsii_name="resetSetForwardedHeaders")
    def reset_set_forwarded_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetForwardedHeaders", []))

    @jsii.member(jsii_name="resetTcpReject")
    def reset_tcp_reject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpReject", []))

    @jsii.member(jsii_name="resetUseBackend")
    def reset_use_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseBackend", []))

    @builtins.property
    @jsii.member(jsii_name="httpRedirect")
    def http_redirect(self) -> LoadbalancerFrontendRuleActionsHttpRedirectList:
        return typing.cast(LoadbalancerFrontendRuleActionsHttpRedirectList, jsii.get(self, "httpRedirect"))

    @builtins.property
    @jsii.member(jsii_name="httpReturn")
    def http_return(self) -> LoadbalancerFrontendRuleActionsHttpReturnList:
        return typing.cast(LoadbalancerFrontendRuleActionsHttpReturnList, jsii.get(self, "httpReturn"))

    @builtins.property
    @jsii.member(jsii_name="setForwardedHeaders")
    def set_forwarded_headers(
        self,
    ) -> "LoadbalancerFrontendRuleActionsSetForwardedHeadersList":
        return typing.cast("LoadbalancerFrontendRuleActionsSetForwardedHeadersList", jsii.get(self, "setForwardedHeaders"))

    @builtins.property
    @jsii.member(jsii_name="tcpReject")
    def tcp_reject(self) -> "LoadbalancerFrontendRuleActionsTcpRejectList":
        return typing.cast("LoadbalancerFrontendRuleActionsTcpRejectList", jsii.get(self, "tcpReject"))

    @builtins.property
    @jsii.member(jsii_name="useBackend")
    def use_backend(self) -> "LoadbalancerFrontendRuleActionsUseBackendList":
        return typing.cast("LoadbalancerFrontendRuleActionsUseBackendList", jsii.get(self, "useBackend"))

    @builtins.property
    @jsii.member(jsii_name="httpRedirectInput")
    def http_redirect_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpRedirect]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpRedirect]]], jsii.get(self, "httpRedirectInput"))

    @builtins.property
    @jsii.member(jsii_name="httpReturnInput")
    def http_return_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpReturn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsHttpReturn]]], jsii.get(self, "httpReturnInput"))

    @builtins.property
    @jsii.member(jsii_name="setForwardedHeadersInput")
    def set_forwarded_headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsSetForwardedHeaders"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsSetForwardedHeaders"]]], jsii.get(self, "setForwardedHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpRejectInput")
    def tcp_reject_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsTcpReject"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsTcpReject"]]], jsii.get(self, "tcpRejectInput"))

    @builtins.property
    @jsii.member(jsii_name="useBackendInput")
    def use_backend_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsUseBackend"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleActionsUseBackend"]]], jsii.get(self, "useBackendInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerFrontendRuleActions]:
        return typing.cast(typing.Optional[LoadbalancerFrontendRuleActions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoadbalancerFrontendRuleActions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsSetForwardedHeaders",
    jsii_struct_bases=[],
    name_mapping={"active": "active"},
)
class LoadbalancerFrontendRuleActionsSetForwardedHeaders:
    def __init__(
        self,
        *,
        active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#active LoadbalancerFrontendRule#active}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsSetForwardedHeaders.__init__)
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
        self._values: typing.Dict[str, typing.Any] = {}
        if active is not None:
            self._values["active"] = active

    @builtins.property
    def active(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#active LoadbalancerFrontendRule#active}.'''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleActionsSetForwardedHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleActionsSetForwardedHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsSetForwardedHeadersList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsSetForwardedHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsSetForwardedHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsSetForwardedHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsSetForwardedHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsSetForwardedHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsSetForwardedHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsSetForwardedHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsSetForwardedHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsSetForwardedHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @builtins.property
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "activeInput"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "active"))

    @active.setter
    def active(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference, "active").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsSetForwardedHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsSetForwardedHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsSetForwardedHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsTcpReject",
    jsii_struct_bases=[],
    name_mapping={"active": "active"},
)
class LoadbalancerFrontendRuleActionsTcpReject:
    def __init__(
        self,
        *,
        active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#active LoadbalancerFrontendRule#active}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsTcpReject.__init__)
            check_type(argname="argument active", value=active, expected_type=type_hints["active"])
        self._values: typing.Dict[str, typing.Any] = {}
        if active is not None:
            self._values["active"] = active

    @builtins.property
    def active(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#active LoadbalancerFrontendRule#active}.'''
        result = self._values.get("active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleActionsTcpReject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleActionsTcpRejectList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsTcpRejectList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsTcpRejectList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleActionsTcpRejectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsTcpRejectList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleActionsTcpRejectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsTcpRejectList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsTcpRejectList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsTcpRejectList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsTcpReject]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsTcpReject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsTcpReject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsTcpRejectList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleActionsTcpRejectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsTcpRejectOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsTcpRejectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetActive")
    def reset_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActive", []))

    @builtins.property
    @jsii.member(jsii_name="activeInput")
    def active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "activeInput"))

    @builtins.property
    @jsii.member(jsii_name="active")
    def active(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "active"))

    @active.setter
    def active(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsTcpRejectOutputReference, "active").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "active", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsTcpReject, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsTcpReject, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsTcpReject, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsTcpRejectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsUseBackend",
    jsii_struct_bases=[],
    name_mapping={"backend_name": "backendName"},
)
class LoadbalancerFrontendRuleActionsUseBackend:
    def __init__(self, *, backend_name: builtins.str) -> None:
        '''
        :param backend_name: The name of the backend where traffic will be routed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#backend_name LoadbalancerFrontendRule#backend_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsUseBackend.__init__)
            check_type(argname="argument backend_name", value=backend_name, expected_type=type_hints["backend_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_name": backend_name,
        }

    @builtins.property
    def backend_name(self) -> builtins.str:
        '''The name of the backend where traffic will be routed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#backend_name LoadbalancerFrontendRule#backend_name}
        '''
        result = self._values.get("backend_name")
        assert result is not None, "Required property 'backend_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleActionsUseBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleActionsUseBackendList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsUseBackendList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsUseBackendList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleActionsUseBackendOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsUseBackendList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleActionsUseBackendOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsUseBackendList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsUseBackendList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsUseBackendList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsUseBackend]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsUseBackend]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleActionsUseBackend]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsUseBackendList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleActionsUseBackendOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleActionsUseBackendOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleActionsUseBackendOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="backendNameInput")
    def backend_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendName")
    def backend_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendName"))

    @backend_name.setter
    def backend_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsUseBackendOutputReference, "backend_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsUseBackend, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsUseBackend, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleActionsUseBackend, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleActionsUseBackendOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "frontend": "frontend",
        "name": "name",
        "priority": "priority",
        "actions": "actions",
        "id": "id",
        "matchers": "matchers",
    },
)
class LoadbalancerFrontendRuleConfig(cdktf.TerraformMetaArguments):
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
        frontend: builtins.str,
        name: builtins.str,
        priority: jsii.Number,
        actions: typing.Optional[typing.Union[LoadbalancerFrontendRuleActions, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        matchers: typing.Optional[typing.Union["LoadbalancerFrontendRuleMatchers", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param frontend: ID of the load balancer frontend to which the rule is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#frontend LoadbalancerFrontendRule#frontend}
        :param name: The name of the frontend rule must be unique within the load balancer service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        :param priority: Rule with the higher priority goes first. Rules with the same priority processed in alphabetical order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#priority LoadbalancerFrontendRule#priority}
        :param actions: actions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#actions LoadbalancerFrontendRule#actions}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#id LoadbalancerFrontendRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param matchers: matchers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#matchers LoadbalancerFrontendRule#matchers}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(actions, dict):
            actions = LoadbalancerFrontendRuleActions(**actions)
        if isinstance(matchers, dict):
            matchers = LoadbalancerFrontendRuleMatchers(**matchers)
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument frontend", value=frontend, expected_type=type_hints["frontend"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument matchers", value=matchers, expected_type=type_hints["matchers"])
        self._values: typing.Dict[str, typing.Any] = {
            "frontend": frontend,
            "name": name,
            "priority": priority,
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
        if id is not None:
            self._values["id"] = id
        if matchers is not None:
            self._values["matchers"] = matchers

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
    def frontend(self) -> builtins.str:
        '''ID of the load balancer frontend to which the rule is connected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#frontend LoadbalancerFrontendRule#frontend}
        '''
        result = self._values.get("frontend")
        assert result is not None, "Required property 'frontend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the frontend rule must be unique within the load balancer service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Rule with the higher priority goes first. Rules with the same priority processed in alphabetical order.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#priority LoadbalancerFrontendRule#priority}
        '''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def actions(self) -> typing.Optional[LoadbalancerFrontendRuleActions]:
        '''actions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#actions LoadbalancerFrontendRule#actions}
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[LoadbalancerFrontendRuleActions], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#id LoadbalancerFrontendRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def matchers(self) -> typing.Optional["LoadbalancerFrontendRuleMatchers"]:
        '''matchers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#matchers LoadbalancerFrontendRule#matchers}
        '''
        result = self._values.get("matchers")
        return typing.cast(typing.Optional["LoadbalancerFrontendRuleMatchers"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchers",
    jsii_struct_bases=[],
    name_mapping={
        "body_size": "bodySize",
        "body_size_range": "bodySizeRange",
        "cookie": "cookie",
        "header": "header",
        "host": "host",
        "http_method": "httpMethod",
        "num_members_up": "numMembersUp",
        "path": "path",
        "src_ip": "srcIp",
        "src_port": "srcPort",
        "src_port_range": "srcPortRange",
        "url": "url",
        "url_param": "urlParam",
        "url_query": "urlQuery",
    },
)
class LoadbalancerFrontendRuleMatchers:
    def __init__(
        self,
        *,
        body_size: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersBodySize", typing.Dict[str, typing.Any]]]]] = None,
        body_size_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersBodySizeRange", typing.Dict[str, typing.Any]]]]] = None,
        cookie: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersCookie", typing.Dict[str, typing.Any]]]]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersHeader", typing.Dict[str, typing.Any]]]]] = None,
        host: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersHost", typing.Dict[str, typing.Any]]]]] = None,
        http_method: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersHttpMethod", typing.Dict[str, typing.Any]]]]] = None,
        num_members_up: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersNumMembersUp", typing.Dict[str, typing.Any]]]]] = None,
        path: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersPath", typing.Dict[str, typing.Any]]]]] = None,
        src_ip: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcIp", typing.Dict[str, typing.Any]]]]] = None,
        src_port: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcPort", typing.Dict[str, typing.Any]]]]] = None,
        src_port_range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcPortRange", typing.Dict[str, typing.Any]]]]] = None,
        url: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrl", typing.Dict[str, typing.Any]]]]] = None,
        url_param: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrlParam", typing.Dict[str, typing.Any]]]]] = None,
        url_query: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrlQuery", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param body_size: body_size block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#body_size LoadbalancerFrontendRule#body_size}
        :param body_size_range: body_size_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#body_size_range LoadbalancerFrontendRule#body_size_range}
        :param cookie: cookie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#cookie LoadbalancerFrontendRule#cookie}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#header LoadbalancerFrontendRule#header}
        :param host: host block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#host LoadbalancerFrontendRule#host}
        :param http_method: http_method block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_method LoadbalancerFrontendRule#http_method}
        :param num_members_up: num_members_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#num_members_up LoadbalancerFrontendRule#num_members_up}
        :param path: path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#path LoadbalancerFrontendRule#path}
        :param src_ip: src_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_ip LoadbalancerFrontendRule#src_ip}
        :param src_port: src_port block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_port LoadbalancerFrontendRule#src_port}
        :param src_port_range: src_port_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_port_range LoadbalancerFrontendRule#src_port_range}
        :param url: url block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url LoadbalancerFrontendRule#url}
        :param url_param: url_param block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url_param LoadbalancerFrontendRule#url_param}
        :param url_query: url_query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url_query LoadbalancerFrontendRule#url_query}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchers.__init__)
            check_type(argname="argument body_size", value=body_size, expected_type=type_hints["body_size"])
            check_type(argname="argument body_size_range", value=body_size_range, expected_type=type_hints["body_size_range"])
            check_type(argname="argument cookie", value=cookie, expected_type=type_hints["cookie"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument num_members_up", value=num_members_up, expected_type=type_hints["num_members_up"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument src_ip", value=src_ip, expected_type=type_hints["src_ip"])
            check_type(argname="argument src_port", value=src_port, expected_type=type_hints["src_port"])
            check_type(argname="argument src_port_range", value=src_port_range, expected_type=type_hints["src_port_range"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument url_param", value=url_param, expected_type=type_hints["url_param"])
            check_type(argname="argument url_query", value=url_query, expected_type=type_hints["url_query"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body_size is not None:
            self._values["body_size"] = body_size
        if body_size_range is not None:
            self._values["body_size_range"] = body_size_range
        if cookie is not None:
            self._values["cookie"] = cookie
        if header is not None:
            self._values["header"] = header
        if host is not None:
            self._values["host"] = host
        if http_method is not None:
            self._values["http_method"] = http_method
        if num_members_up is not None:
            self._values["num_members_up"] = num_members_up
        if path is not None:
            self._values["path"] = path
        if src_ip is not None:
            self._values["src_ip"] = src_ip
        if src_port is not None:
            self._values["src_port"] = src_port
        if src_port_range is not None:
            self._values["src_port_range"] = src_port_range
        if url is not None:
            self._values["url"] = url
        if url_param is not None:
            self._values["url_param"] = url_param
        if url_query is not None:
            self._values["url_query"] = url_query

    @builtins.property
    def body_size(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersBodySize"]]]:
        '''body_size block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#body_size LoadbalancerFrontendRule#body_size}
        '''
        result = self._values.get("body_size")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersBodySize"]]], result)

    @builtins.property
    def body_size_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersBodySizeRange"]]]:
        '''body_size_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#body_size_range LoadbalancerFrontendRule#body_size_range}
        '''
        result = self._values.get("body_size_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersBodySizeRange"]]], result)

    @builtins.property
    def cookie(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersCookie"]]]:
        '''cookie block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#cookie LoadbalancerFrontendRule#cookie}
        '''
        result = self._values.get("cookie")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersCookie"]]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#header LoadbalancerFrontendRule#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersHeader"]]], result)

    @builtins.property
    def host(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersHost"]]]:
        '''host block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#host LoadbalancerFrontendRule#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersHost"]]], result)

    @builtins.property
    def http_method(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersHttpMethod"]]]:
        '''http_method block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#http_method LoadbalancerFrontendRule#http_method}
        '''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersHttpMethod"]]], result)

    @builtins.property
    def num_members_up(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersNumMembersUp"]]]:
        '''num_members_up block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#num_members_up LoadbalancerFrontendRule#num_members_up}
        '''
        result = self._values.get("num_members_up")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersNumMembersUp"]]], result)

    @builtins.property
    def path(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersPath"]]]:
        '''path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#path LoadbalancerFrontendRule#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersPath"]]], result)

    @builtins.property
    def src_ip(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcIp"]]]:
        '''src_ip block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_ip LoadbalancerFrontendRule#src_ip}
        '''
        result = self._values.get("src_ip")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcIp"]]], result)

    @builtins.property
    def src_port(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPort"]]]:
        '''src_port block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_port LoadbalancerFrontendRule#src_port}
        '''
        result = self._values.get("src_port")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPort"]]], result)

    @builtins.property
    def src_port_range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPortRange"]]]:
        '''src_port_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#src_port_range LoadbalancerFrontendRule#src_port_range}
        '''
        result = self._values.get("src_port_range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPortRange"]]], result)

    @builtins.property
    def url(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrl"]]]:
        '''url block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url LoadbalancerFrontendRule#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrl"]]], result)

    @builtins.property
    def url_param(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlParam"]]]:
        '''url_param block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url_param LoadbalancerFrontendRule#url_param}
        '''
        result = self._values.get("url_param")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlParam"]]], result)

    @builtins.property
    def url_query(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlQuery"]]]:
        '''url_query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#url_query LoadbalancerFrontendRule#url_query}
        '''
        result = self._values.get("url_query")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlQuery"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersBodySize",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "value": "value"},
)
class LoadbalancerFrontendRuleMatchersBodySize:
    def __init__(self, *, method: builtins.str, value: jsii.Number) -> None:
        '''
        :param method: Match method (``equal``, ``greater``, ``greater_or_equal``, ``less``, ``less_or_equal``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param value: Integer value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySize.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
            "value": value,
        }

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``equal``, ``greater``, ``greater_or_equal``, ``less``, ``less_or_equal``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Integer value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersBodySize(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersBodySizeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersBodySizeList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySizeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersBodySizeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySizeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersBodySizeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySize]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySize]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySize]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersBodySizeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersBodySizeOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySizeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersBodySize, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersBodySize, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersBodySize, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersBodySizeRange",
    jsii_struct_bases=[],
    name_mapping={"range_end": "rangeEnd", "range_start": "rangeStart"},
)
class LoadbalancerFrontendRuleMatchersBodySizeRange:
    def __init__(self, *, range_end: jsii.Number, range_start: jsii.Number) -> None:
        '''
        :param range_end: Integer value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_end LoadbalancerFrontendRule#range_end}
        :param range_start: Integer value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_start LoadbalancerFrontendRule#range_start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySizeRange.__init__)
            check_type(argname="argument range_end", value=range_end, expected_type=type_hints["range_end"])
            check_type(argname="argument range_start", value=range_start, expected_type=type_hints["range_start"])
        self._values: typing.Dict[str, typing.Any] = {
            "range_end": range_end,
            "range_start": range_start,
        }

    @builtins.property
    def range_end(self) -> jsii.Number:
        '''Integer value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_end LoadbalancerFrontendRule#range_end}
        '''
        result = self._values.get("range_end")
        assert result is not None, "Required property 'range_end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def range_start(self) -> jsii.Number:
        '''Integer value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_start LoadbalancerFrontendRule#range_start}
        '''
        result = self._values.get("range_start")
        assert result is not None, "Required property 'range_start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersBodySizeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersBodySizeRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersBodySizeRangeList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySizeRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySizeRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySizeRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySizeRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySizeRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="rangeEndInput")
    def range_end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeEndInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeStartInput")
    def range_start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeStartInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeEnd")
    def range_end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeEnd"))

    @range_end.setter
    def range_end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference, "range_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeEnd", value)

    @builtins.property
    @jsii.member(jsii_name="rangeStart")
    def range_start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeStart"))

    @range_start.setter
    def range_start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference, "range_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeStart", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersBodySizeRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersBodySizeRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersBodySizeRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersCookie",
    jsii_struct_bases=[],
    name_mapping={
        "method": "method",
        "name": "name",
        "ignore_case": "ignoreCase",
        "value": "value",
    },
)
class LoadbalancerFrontendRuleMatchersCookie:
    def __init__(
        self,
        *,
        method: builtins.str,
        name: builtins.str,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``). Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param name: Name of the argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        :param ignore_case: Ignore case, default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        :param value: String value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersCookie.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
            "name": name,
        }
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``).

        Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the argument.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore case, default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''String value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersCookie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersCookieList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersCookieList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersCookieList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersCookieOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersCookieList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersCookieOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersCookie]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersCookie]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersCookie]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersCookieOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersCookieOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersCookieOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersCookie, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersCookie, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersCookie, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersCookieOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHeader",
    jsii_struct_bases=[],
    name_mapping={
        "method": "method",
        "name": "name",
        "ignore_case": "ignoreCase",
        "value": "value",
    },
)
class LoadbalancerFrontendRuleMatchersHeader:
    def __init__(
        self,
        *,
        method: builtins.str,
        name: builtins.str,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``). Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param name: Name of the argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        :param ignore_case: Ignore case, default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        :param value: String value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHeader.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
            "name": name,
        }
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``).

        Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the argument.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore case, default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''String value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHeaderList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHeaderOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHeaderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHost",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class LoadbalancerFrontendRuleMatchersHost:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: String value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHost.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''String value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersHost(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersHostList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHostList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHostList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersHostOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHostList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersHostOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHostList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHostList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHostList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHost]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHost]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHost]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHostList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersHostOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHostOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHostOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHostOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHost, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHost, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHost, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHostOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHttpMethod",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class LoadbalancerFrontendRuleMatchersHttpMethod:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: String value (``GET``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, ``DELETE``, ``CONNECT``, ``OPTIONS``, ``TRACE``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHttpMethod.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''String value (``GET``, ``HEAD``, ``POST``, ``PUT``, ``PATCH``, ``DELETE``, ``CONNECT``, ``OPTIONS``, ``TRACE``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersHttpMethod(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersHttpMethodList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHttpMethodList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHttpMethodList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersHttpMethodOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHttpMethodList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersHttpMethodOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHttpMethodList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHttpMethodList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHttpMethodList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHttpMethod]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHttpMethod]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHttpMethod]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHttpMethodList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersHttpMethodOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersHttpMethodOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersHttpMethodOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHttpMethodOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHttpMethod, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHttpMethod, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersHttpMethod, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersHttpMethodOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersNumMembersUp",
    jsii_struct_bases=[],
    name_mapping={"backend_name": "backendName", "method": "method", "value": "value"},
)
class LoadbalancerFrontendRuleMatchersNumMembersUp:
    def __init__(
        self,
        *,
        backend_name: builtins.str,
        method: builtins.str,
        value: jsii.Number,
    ) -> None:
        '''
        :param backend_name: The name of the ``backend`` which members will be monitored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#backend_name LoadbalancerFrontendRule#backend_name}
        :param method: Match method (``equal``, ``greater``, ``greater_or_equal``, ``less``, ``less_or_equal``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param value: Integer value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersNumMembersUp.__init__)
            check_type(argname="argument backend_name", value=backend_name, expected_type=type_hints["backend_name"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_name": backend_name,
            "method": method,
            "value": value,
        }

    @builtins.property
    def backend_name(self) -> builtins.str:
        '''The name of the ``backend`` which members will be monitored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#backend_name LoadbalancerFrontendRule#backend_name}
        '''
        result = self._values.get("backend_name")
        assert result is not None, "Required property 'backend_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``equal``, ``greater``, ``greater_or_equal``, ``less``, ``less_or_equal``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Integer value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersNumMembersUp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersNumMembersUpList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersNumMembersUpList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersNumMembersUpList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersNumMembersUpList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersNumMembersUp]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersNumMembersUp]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersNumMembersUp]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="backendNameInput")
    def backend_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendNameInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="backendName")
    def backend_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendName"))

    @backend_name.setter
    def backend_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference, "backend_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendName", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersNumMembersUp, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersNumMembersUp, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersNumMembersUp, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBodySize")
    def put_body_size(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleMatchersBodySize, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_body_size)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBodySize", [value]))

    @jsii.member(jsii_name="putBodySizeRange")
    def put_body_size_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleMatchersBodySizeRange, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_body_size_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBodySizeRange", [value]))

    @jsii.member(jsii_name="putCookie")
    def put_cookie(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleMatchersCookie, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_cookie)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCookie", [value]))

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleMatchersHeader, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="putHost")
    def put_host(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleMatchersHost, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_host)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHost", [value]))

    @jsii.member(jsii_name="putHttpMethod")
    def put_http_method(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleMatchersHttpMethod, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_http_method)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHttpMethod", [value]))

    @jsii.member(jsii_name="putNumMembersUp")
    def put_num_members_up(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadbalancerFrontendRuleMatchersNumMembersUp, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_num_members_up)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNumMembersUp", [value]))

    @jsii.member(jsii_name="putPath")
    def put_path(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersPath", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_path)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPath", [value]))

    @jsii.member(jsii_name="putSrcIp")
    def put_src_ip(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcIp", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_src_ip)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSrcIp", [value]))

    @jsii.member(jsii_name="putSrcPort")
    def put_src_port(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcPort", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_src_port)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSrcPort", [value]))

    @jsii.member(jsii_name="putSrcPortRange")
    def put_src_port_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersSrcPortRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_src_port_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSrcPortRange", [value]))

    @jsii.member(jsii_name="putUrl")
    def put_url(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrl", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_url)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrl", [value]))

    @jsii.member(jsii_name="putUrlParam")
    def put_url_param(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrlParam", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_url_param)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlParam", [value]))

    @jsii.member(jsii_name="putUrlQuery")
    def put_url_query(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerFrontendRuleMatchersUrlQuery", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersOutputReference.put_url_query)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUrlQuery", [value]))

    @jsii.member(jsii_name="resetBodySize")
    def reset_body_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodySize", []))

    @jsii.member(jsii_name="resetBodySizeRange")
    def reset_body_size_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodySizeRange", []))

    @jsii.member(jsii_name="resetCookie")
    def reset_cookie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookie", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @jsii.member(jsii_name="resetNumMembersUp")
    def reset_num_members_up(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumMembersUp", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetSrcIp")
    def reset_src_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcIp", []))

    @jsii.member(jsii_name="resetSrcPort")
    def reset_src_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcPort", []))

    @jsii.member(jsii_name="resetSrcPortRange")
    def reset_src_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSrcPortRange", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUrlParam")
    def reset_url_param(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlParam", []))

    @jsii.member(jsii_name="resetUrlQuery")
    def reset_url_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlQuery", []))

    @builtins.property
    @jsii.member(jsii_name="bodySize")
    def body_size(self) -> LoadbalancerFrontendRuleMatchersBodySizeList:
        return typing.cast(LoadbalancerFrontendRuleMatchersBodySizeList, jsii.get(self, "bodySize"))

    @builtins.property
    @jsii.member(jsii_name="bodySizeRange")
    def body_size_range(self) -> LoadbalancerFrontendRuleMatchersBodySizeRangeList:
        return typing.cast(LoadbalancerFrontendRuleMatchersBodySizeRangeList, jsii.get(self, "bodySizeRange"))

    @builtins.property
    @jsii.member(jsii_name="cookie")
    def cookie(self) -> LoadbalancerFrontendRuleMatchersCookieList:
        return typing.cast(LoadbalancerFrontendRuleMatchersCookieList, jsii.get(self, "cookie"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> LoadbalancerFrontendRuleMatchersHeaderList:
        return typing.cast(LoadbalancerFrontendRuleMatchersHeaderList, jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> LoadbalancerFrontendRuleMatchersHostList:
        return typing.cast(LoadbalancerFrontendRuleMatchersHostList, jsii.get(self, "host"))

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> LoadbalancerFrontendRuleMatchersHttpMethodList:
        return typing.cast(LoadbalancerFrontendRuleMatchersHttpMethodList, jsii.get(self, "httpMethod"))

    @builtins.property
    @jsii.member(jsii_name="numMembersUp")
    def num_members_up(self) -> LoadbalancerFrontendRuleMatchersNumMembersUpList:
        return typing.cast(LoadbalancerFrontendRuleMatchersNumMembersUpList, jsii.get(self, "numMembersUp"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> "LoadbalancerFrontendRuleMatchersPathList":
        return typing.cast("LoadbalancerFrontendRuleMatchersPathList", jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="srcIp")
    def src_ip(self) -> "LoadbalancerFrontendRuleMatchersSrcIpList":
        return typing.cast("LoadbalancerFrontendRuleMatchersSrcIpList", jsii.get(self, "srcIp"))

    @builtins.property
    @jsii.member(jsii_name="srcPort")
    def src_port(self) -> "LoadbalancerFrontendRuleMatchersSrcPortList":
        return typing.cast("LoadbalancerFrontendRuleMatchersSrcPortList", jsii.get(self, "srcPort"))

    @builtins.property
    @jsii.member(jsii_name="srcPortRange")
    def src_port_range(self) -> "LoadbalancerFrontendRuleMatchersSrcPortRangeList":
        return typing.cast("LoadbalancerFrontendRuleMatchersSrcPortRangeList", jsii.get(self, "srcPortRange"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> "LoadbalancerFrontendRuleMatchersUrlList":
        return typing.cast("LoadbalancerFrontendRuleMatchersUrlList", jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="urlParam")
    def url_param(self) -> "LoadbalancerFrontendRuleMatchersUrlParamList":
        return typing.cast("LoadbalancerFrontendRuleMatchersUrlParamList", jsii.get(self, "urlParam"))

    @builtins.property
    @jsii.member(jsii_name="urlQuery")
    def url_query(self) -> "LoadbalancerFrontendRuleMatchersUrlQueryList":
        return typing.cast("LoadbalancerFrontendRuleMatchersUrlQueryList", jsii.get(self, "urlQuery"))

    @builtins.property
    @jsii.member(jsii_name="bodySizeInput")
    def body_size_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySize]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySize]]], jsii.get(self, "bodySizeInput"))

    @builtins.property
    @jsii.member(jsii_name="bodySizeRangeInput")
    def body_size_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySizeRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersBodySizeRange]]], jsii.get(self, "bodySizeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieInput")
    def cookie_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersCookie]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersCookie]]], jsii.get(self, "cookieInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHeader]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHost]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHost]]], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHttpMethod]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersHttpMethod]]], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="numMembersUpInput")
    def num_members_up_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersNumMembersUp]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersNumMembersUp]]], jsii.get(self, "numMembersUpInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersPath"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersPath"]]], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="srcIpInput")
    def src_ip_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcIp"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcIp"]]], jsii.get(self, "srcIpInput"))

    @builtins.property
    @jsii.member(jsii_name="srcPortInput")
    def src_port_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPort"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPort"]]], jsii.get(self, "srcPortInput"))

    @builtins.property
    @jsii.member(jsii_name="srcPortRangeInput")
    def src_port_range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPortRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersSrcPortRange"]]], jsii.get(self, "srcPortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrl"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrl"]]], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="urlParamInput")
    def url_param_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlParam"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlParam"]]], jsii.get(self, "urlParamInput"))

    @builtins.property
    @jsii.member(jsii_name="urlQueryInput")
    def url_query_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlQuery"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerFrontendRuleMatchersUrlQuery"]]], jsii.get(self, "urlQueryInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerFrontendRuleMatchers]:
        return typing.cast(typing.Optional[LoadbalancerFrontendRuleMatchers], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoadbalancerFrontendRuleMatchers],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersPath",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "ignore_case": "ignoreCase", "value": "value"},
)
class LoadbalancerFrontendRuleMatchersPath:
    def __init__(
        self,
        *,
        method: builtins.str,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``). Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param ignore_case: Ignore case, default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        :param value: String value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersPath.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
        }
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``).

        Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore case, default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''String value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersPathList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersPathList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersPathList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersPathOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersPathList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersPathOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersPath]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersPath]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersPath]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersPathOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersPath, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersPath, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersPath, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcIp",
    jsii_struct_bases=[],
    name_mapping={"value": "value"},
)
class LoadbalancerFrontendRuleMatchersSrcIp:
    def __init__(self, *, value: builtins.str) -> None:
        '''
        :param value: IP address. CIDR masks are supported, e.g. ``192.168.0.0/24``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcIp.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }

    @builtins.property
    def value(self) -> builtins.str:
        '''IP address. CIDR masks are supported, e.g. ``192.168.0.0/24``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersSrcIp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersSrcIpList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcIpList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcIpList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersSrcIpOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcIpList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersSrcIpOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcIpList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcIpList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcIpList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcIp]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcIp]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcIp]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcIpList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersSrcIpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcIpOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcIpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcIpOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcIp, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcIp, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcIp, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcIpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcPort",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "value": "value"},
)
class LoadbalancerFrontendRuleMatchersSrcPort:
    def __init__(self, *, method: builtins.str, value: jsii.Number) -> None:
        '''
        :param method: Match method (``equal``, ``greater``, ``greater_or_equal``, ``less``, ``less_or_equal``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param value: Integer value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPort.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
            "value": value,
        }

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``equal``, ``greater``, ``greater_or_equal``, ``less``, ``less_or_equal``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Integer value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersSrcPort(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersSrcPortList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcPortList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPortList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersSrcPortOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPortList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersSrcPortOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcPort]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcPort]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcPort]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersSrcPortOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcPortOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPortOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcPort, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcPort, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcPort, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcPortRange",
    jsii_struct_bases=[],
    name_mapping={"range_end": "rangeEnd", "range_start": "rangeStart"},
)
class LoadbalancerFrontendRuleMatchersSrcPortRange:
    def __init__(self, *, range_end: jsii.Number, range_start: jsii.Number) -> None:
        '''
        :param range_end: Integer value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_end LoadbalancerFrontendRule#range_end}
        :param range_start: Integer value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_start LoadbalancerFrontendRule#range_start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPortRange.__init__)
            check_type(argname="argument range_end", value=range_end, expected_type=type_hints["range_end"])
            check_type(argname="argument range_start", value=range_start, expected_type=type_hints["range_start"])
        self._values: typing.Dict[str, typing.Any] = {
            "range_end": range_end,
            "range_start": range_start,
        }

    @builtins.property
    def range_end(self) -> jsii.Number:
        '''Integer value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_end LoadbalancerFrontendRule#range_end}
        '''
        result = self._values.get("range_end")
        assert result is not None, "Required property 'range_end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def range_start(self) -> jsii.Number:
        '''Integer value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#range_start LoadbalancerFrontendRule#range_start}
        '''
        result = self._values.get("range_start")
        assert result is not None, "Required property 'range_start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersSrcPortRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersSrcPortRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcPortRangeList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPortRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPortRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcPortRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcPortRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersSrcPortRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="rangeEndInput")
    def range_end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeEndInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeStartInput")
    def range_start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "rangeStartInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeEnd")
    def range_end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeEnd"))

    @range_end.setter
    def range_end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference, "range_end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeEnd", value)

    @builtins.property
    @jsii.member(jsii_name="rangeStart")
    def range_start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rangeStart"))

    @range_start.setter
    def range_start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference, "range_start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rangeStart", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcPortRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcPortRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersSrcPortRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrl",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "ignore_case": "ignoreCase", "value": "value"},
)
class LoadbalancerFrontendRuleMatchersUrl:
    def __init__(
        self,
        *,
        method: builtins.str,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``). Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param ignore_case: Ignore case, default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        :param value: String value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrl.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
        }
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``).

        Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore case, default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''String value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersUrl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersUrlList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersUrlOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersUrlOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrl]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrl]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrl]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersUrlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrl, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrl, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrl, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlParam",
    jsii_struct_bases=[],
    name_mapping={
        "method": "method",
        "name": "name",
        "ignore_case": "ignoreCase",
        "value": "value",
    },
)
class LoadbalancerFrontendRuleMatchersUrlParam:
    def __init__(
        self,
        *,
        method: builtins.str,
        name: builtins.str,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``). Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param name: Name of the argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        :param ignore_case: Ignore case, default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        :param value: String value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlParam.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
            "name": name,
        }
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``).

        Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the argument.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#name LoadbalancerFrontendRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore case, default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''String value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersUrlParam(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersUrlParamList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlParamList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlParamList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersUrlParamOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlParamList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersUrlParamOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrlParam]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrlParam]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrlParam]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersUrlParamOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlParamOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlParamOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrlParam, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrlParam, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrlParam, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlParamOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlQuery",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "ignore_case": "ignoreCase", "value": "value"},
)
class LoadbalancerFrontendRuleMatchersUrlQuery:
    def __init__(
        self,
        *,
        method: builtins.str,
        ignore_case: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param method: Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``). Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        :param ignore_case: Ignore case, default ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        :param value: String value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlQuery.__init__)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument ignore_case", value=ignore_case, expected_type=type_hints["ignore_case"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "method": method,
        }
        if ignore_case is not None:
            self._values["ignore_case"] = ignore_case
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def method(self) -> builtins.str:
        '''Match method (``exact``, ``substring``, ``regexp``, ``starts``, ``ends``, ``domain``, ``ip``, ``exists``).

        Matcher with ``exists`` and ``ip`` methods must be used without ``value`` and ``ignore_case`` fields.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#method LoadbalancerFrontendRule#method}
        '''
        result = self._values.get("method")
        assert result is not None, "Required property 'method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ignore_case(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Ignore case, default ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#ignore_case LoadbalancerFrontendRule#ignore_case}
        '''
        result = self._values.get("ignore_case")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''String value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_frontend_rule#value LoadbalancerFrontendRule#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerFrontendRuleMatchersUrlQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerFrontendRuleMatchersUrlQueryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlQueryList",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlQueryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadbalancerFrontendRuleMatchersUrlQueryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlQueryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerFrontendRuleMatchersUrlQueryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrlQuery]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrlQuery]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerFrontendRuleMatchersUrlQuery]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerFrontendRuleMatchersUrlQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerFrontendRule.LoadbalancerFrontendRuleMatchersUrlQueryOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerFrontendRuleMatchersUrlQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIgnoreCase")
    def reset_ignore_case(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCase", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="ignoreCaseInput")
    def ignore_case_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreCaseInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCase")
    def ignore_case(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreCase"))

    @ignore_case.setter
    def ignore_case(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryOutputReference, "ignore_case").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCase", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrlQuery, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrlQuery, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerFrontendRuleMatchersUrlQuery, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerFrontendRuleMatchersUrlQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LoadbalancerFrontendRule",
    "LoadbalancerFrontendRuleActions",
    "LoadbalancerFrontendRuleActionsHttpRedirect",
    "LoadbalancerFrontendRuleActionsHttpRedirectList",
    "LoadbalancerFrontendRuleActionsHttpRedirectOutputReference",
    "LoadbalancerFrontendRuleActionsHttpReturn",
    "LoadbalancerFrontendRuleActionsHttpReturnList",
    "LoadbalancerFrontendRuleActionsHttpReturnOutputReference",
    "LoadbalancerFrontendRuleActionsOutputReference",
    "LoadbalancerFrontendRuleActionsSetForwardedHeaders",
    "LoadbalancerFrontendRuleActionsSetForwardedHeadersList",
    "LoadbalancerFrontendRuleActionsSetForwardedHeadersOutputReference",
    "LoadbalancerFrontendRuleActionsTcpReject",
    "LoadbalancerFrontendRuleActionsTcpRejectList",
    "LoadbalancerFrontendRuleActionsTcpRejectOutputReference",
    "LoadbalancerFrontendRuleActionsUseBackend",
    "LoadbalancerFrontendRuleActionsUseBackendList",
    "LoadbalancerFrontendRuleActionsUseBackendOutputReference",
    "LoadbalancerFrontendRuleConfig",
    "LoadbalancerFrontendRuleMatchers",
    "LoadbalancerFrontendRuleMatchersBodySize",
    "LoadbalancerFrontendRuleMatchersBodySizeList",
    "LoadbalancerFrontendRuleMatchersBodySizeOutputReference",
    "LoadbalancerFrontendRuleMatchersBodySizeRange",
    "LoadbalancerFrontendRuleMatchersBodySizeRangeList",
    "LoadbalancerFrontendRuleMatchersBodySizeRangeOutputReference",
    "LoadbalancerFrontendRuleMatchersCookie",
    "LoadbalancerFrontendRuleMatchersCookieList",
    "LoadbalancerFrontendRuleMatchersCookieOutputReference",
    "LoadbalancerFrontendRuleMatchersHeader",
    "LoadbalancerFrontendRuleMatchersHeaderList",
    "LoadbalancerFrontendRuleMatchersHeaderOutputReference",
    "LoadbalancerFrontendRuleMatchersHost",
    "LoadbalancerFrontendRuleMatchersHostList",
    "LoadbalancerFrontendRuleMatchersHostOutputReference",
    "LoadbalancerFrontendRuleMatchersHttpMethod",
    "LoadbalancerFrontendRuleMatchersHttpMethodList",
    "LoadbalancerFrontendRuleMatchersHttpMethodOutputReference",
    "LoadbalancerFrontendRuleMatchersNumMembersUp",
    "LoadbalancerFrontendRuleMatchersNumMembersUpList",
    "LoadbalancerFrontendRuleMatchersNumMembersUpOutputReference",
    "LoadbalancerFrontendRuleMatchersOutputReference",
    "LoadbalancerFrontendRuleMatchersPath",
    "LoadbalancerFrontendRuleMatchersPathList",
    "LoadbalancerFrontendRuleMatchersPathOutputReference",
    "LoadbalancerFrontendRuleMatchersSrcIp",
    "LoadbalancerFrontendRuleMatchersSrcIpList",
    "LoadbalancerFrontendRuleMatchersSrcIpOutputReference",
    "LoadbalancerFrontendRuleMatchersSrcPort",
    "LoadbalancerFrontendRuleMatchersSrcPortList",
    "LoadbalancerFrontendRuleMatchersSrcPortOutputReference",
    "LoadbalancerFrontendRuleMatchersSrcPortRange",
    "LoadbalancerFrontendRuleMatchersSrcPortRangeList",
    "LoadbalancerFrontendRuleMatchersSrcPortRangeOutputReference",
    "LoadbalancerFrontendRuleMatchersUrl",
    "LoadbalancerFrontendRuleMatchersUrlList",
    "LoadbalancerFrontendRuleMatchersUrlOutputReference",
    "LoadbalancerFrontendRuleMatchersUrlParam",
    "LoadbalancerFrontendRuleMatchersUrlParamList",
    "LoadbalancerFrontendRuleMatchersUrlParamOutputReference",
    "LoadbalancerFrontendRuleMatchersUrlQuery",
    "LoadbalancerFrontendRuleMatchersUrlQueryList",
    "LoadbalancerFrontendRuleMatchersUrlQueryOutputReference",
]

publication.publish()
