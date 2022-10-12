'''
# `spotinst_multai_routing_rule`

Refer to the Terraform Registory for docs: [`spotinst_multai_routing_rule`](https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule).
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


class MultaiRoutingRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.multaiRoutingRule.MultaiRoutingRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule spotinst_multai_routing_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        balancer_id: builtins.str,
        listener_id: builtins.str,
        route: builtins.str,
        target_set_ids: typing.Sequence[builtins.str],
        id: typing.Optional[builtins.str] = None,
        middleware_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MultaiRoutingRuleTags", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule spotinst_multai_routing_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param balancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#balancer_id MultaiRoutingRule#balancer_id}.
        :param listener_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#listener_id MultaiRoutingRule#listener_id}.
        :param route: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#route MultaiRoutingRule#route}.
        :param target_set_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#target_set_ids MultaiRoutingRule#target_set_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#id MultaiRoutingRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param middleware_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#middleware_ids MultaiRoutingRule#middleware_ids}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#priority MultaiRoutingRule#priority}.
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#strategy MultaiRoutingRule#strategy}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#tags MultaiRoutingRule#tags}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiRoutingRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MultaiRoutingRuleConfig(
            balancer_id=balancer_id,
            listener_id=listener_id,
            route=route,
            target_set_ids=target_set_ids,
            id=id,
            middleware_ids=middleware_ids,
            priority=priority,
            strategy=strategy,
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

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MultaiRoutingRuleTags", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiRoutingRule.put_tags)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMiddlewareIds")
    def reset_middleware_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMiddlewareIds", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetStrategy")
    def reset_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrategy", []))

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> "MultaiRoutingRuleTagsList":
        return typing.cast("MultaiRoutingRuleTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="balancerIdInput")
    def balancer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerIdInput")
    def listener_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listenerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="middlewareIdsInput")
    def middleware_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "middlewareIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="routeInput")
    def route_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeInput"))

    @builtins.property
    @jsii.member(jsii_name="strategyInput")
    def strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "strategyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiRoutingRuleTags"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiRoutingRuleTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetSetIdsInput")
    def target_set_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetSetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="balancerId")
    def balancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "balancerId"))

    @balancer_id.setter
    def balancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "balancer_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancerId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="listenerId")
    def listener_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listenerId"))

    @listener_id.setter
    def listener_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "listener_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerId", value)

    @builtins.property
    @jsii.member(jsii_name="middlewareIds")
    def middleware_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "middlewareIds"))

    @middleware_ids.setter
    def middleware_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "middleware_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "middlewareIds", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="route")
    def route(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "route"))

    @route.setter
    def route(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "route").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "route", value)

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "strategy"))

    @strategy.setter
    def strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strategy", value)

    @builtins.property
    @jsii.member(jsii_name="targetSetIds")
    def target_set_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetSetIds"))

    @target_set_ids.setter
    def target_set_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRule, "target_set_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetSetIds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.multaiRoutingRule.MultaiRoutingRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "balancer_id": "balancerId",
        "listener_id": "listenerId",
        "route": "route",
        "target_set_ids": "targetSetIds",
        "id": "id",
        "middleware_ids": "middlewareIds",
        "priority": "priority",
        "strategy": "strategy",
        "tags": "tags",
    },
)
class MultaiRoutingRuleConfig(cdktf.TerraformMetaArguments):
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
        balancer_id: builtins.str,
        listener_id: builtins.str,
        route: builtins.str,
        target_set_ids: typing.Sequence[builtins.str],
        id: typing.Optional[builtins.str] = None,
        middleware_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        priority: typing.Optional[jsii.Number] = None,
        strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["MultaiRoutingRuleTags", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param balancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#balancer_id MultaiRoutingRule#balancer_id}.
        :param listener_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#listener_id MultaiRoutingRule#listener_id}.
        :param route: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#route MultaiRoutingRule#route}.
        :param target_set_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#target_set_ids MultaiRoutingRule#target_set_ids}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#id MultaiRoutingRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param middleware_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#middleware_ids MultaiRoutingRule#middleware_ids}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#priority MultaiRoutingRule#priority}.
        :param strategy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#strategy MultaiRoutingRule#strategy}.
        :param tags: tags block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#tags MultaiRoutingRule#tags}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(MultaiRoutingRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument balancer_id", value=balancer_id, expected_type=type_hints["balancer_id"])
            check_type(argname="argument listener_id", value=listener_id, expected_type=type_hints["listener_id"])
            check_type(argname="argument route", value=route, expected_type=type_hints["route"])
            check_type(argname="argument target_set_ids", value=target_set_ids, expected_type=type_hints["target_set_ids"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument middleware_ids", value=middleware_ids, expected_type=type_hints["middleware_ids"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument strategy", value=strategy, expected_type=type_hints["strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "balancer_id": balancer_id,
            "listener_id": listener_id,
            "route": route,
            "target_set_ids": target_set_ids,
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
        if middleware_ids is not None:
            self._values["middleware_ids"] = middleware_ids
        if priority is not None:
            self._values["priority"] = priority
        if strategy is not None:
            self._values["strategy"] = strategy
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
    def balancer_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#balancer_id MultaiRoutingRule#balancer_id}.'''
        result = self._values.get("balancer_id")
        assert result is not None, "Required property 'balancer_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listener_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#listener_id MultaiRoutingRule#listener_id}.'''
        result = self._values.get("listener_id")
        assert result is not None, "Required property 'listener_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#route MultaiRoutingRule#route}.'''
        result = self._values.get("route")
        assert result is not None, "Required property 'route' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_set_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#target_set_ids MultaiRoutingRule#target_set_ids}.'''
        result = self._values.get("target_set_ids")
        assert result is not None, "Required property 'target_set_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#id MultaiRoutingRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def middleware_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#middleware_ids MultaiRoutingRule#middleware_ids}.'''
        result = self._values.get("middleware_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#priority MultaiRoutingRule#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def strategy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#strategy MultaiRoutingRule#strategy}.'''
        result = self._values.get("strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiRoutingRuleTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#tags MultaiRoutingRule#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["MultaiRoutingRuleTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultaiRoutingRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.multaiRoutingRule.MultaiRoutingRuleTags",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "value": "value"},
)
class MultaiRoutingRuleTags:
    def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#key MultaiRoutingRule#key}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#value MultaiRoutingRule#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiRoutingRuleTags.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#key MultaiRoutingRule#key}.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/multai_routing_rule#value MultaiRoutingRule#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultaiRoutingRuleTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MultaiRoutingRuleTagsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.multaiRoutingRule.MultaiRoutingRuleTagsList",
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
            type_hints = typing.get_type_hints(MultaiRoutingRuleTagsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "MultaiRoutingRuleTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MultaiRoutingRuleTagsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MultaiRoutingRuleTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRuleTagsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRuleTagsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRuleTagsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MultaiRoutingRuleTags]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MultaiRoutingRuleTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[MultaiRoutingRuleTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRuleTagsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MultaiRoutingRuleTagsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.multaiRoutingRule.MultaiRoutingRuleTagsOutputReference",
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
            type_hints = typing.get_type_hints(MultaiRoutingRuleTagsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRuleTagsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRuleTagsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MultaiRoutingRuleTags, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MultaiRoutingRuleTags, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MultaiRoutingRuleTags, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MultaiRoutingRuleTagsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MultaiRoutingRule",
    "MultaiRoutingRuleConfig",
    "MultaiRoutingRuleTags",
    "MultaiRoutingRuleTagsList",
    "MultaiRoutingRuleTagsOutputReference",
]

publication.publish()
