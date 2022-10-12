'''
# `azurerm_frontdoor`

Refer to the Terraform Registory for docs: [`azurerm_frontdoor`](https://www.terraform.io/docs/providers/azurerm/r/frontdoor).
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


class Frontdoor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.Frontdoor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor azurerm_frontdoor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend_pool: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPool", typing.Dict[str, typing.Any]]]],
        backend_pool_health_probe: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPoolHealthProbe", typing.Dict[str, typing.Any]]]],
        backend_pool_load_balancing: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPoolLoadBalancing", typing.Dict[str, typing.Any]]]],
        frontend_endpoint: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorFrontendEndpoint", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        resource_group_name: builtins.str,
        routing_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorRoutingRule", typing.Dict[str, typing.Any]]]],
        backend_pool_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPoolSettings", typing.Dict[str, typing.Any]]]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FrontdoorTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor azurerm_frontdoor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend_pool: backend_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool Frontdoor#backend_pool}
        :param backend_pool_health_probe: backend_pool_health_probe block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_health_probe Frontdoor#backend_pool_health_probe}
        :param backend_pool_load_balancing: backend_pool_load_balancing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_load_balancing Frontdoor#backend_pool_load_balancing}
        :param frontend_endpoint: frontend_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#frontend_endpoint Frontdoor#frontend_endpoint}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#resource_group_name Frontdoor#resource_group_name}.
        :param routing_rule: routing_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#routing_rule Frontdoor#routing_rule}
        :param backend_pool_settings: backend_pool_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_settings Frontdoor#backend_pool_settings}
        :param friendly_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#friendly_name Frontdoor#friendly_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#id Frontdoor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#load_balancer_enabled Frontdoor#load_balancer_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#tags Frontdoor#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#timeouts Frontdoor#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Frontdoor.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FrontdoorConfig(
            backend_pool=backend_pool,
            backend_pool_health_probe=backend_pool_health_probe,
            backend_pool_load_balancing=backend_pool_load_balancing,
            frontend_endpoint=frontend_endpoint,
            name=name,
            resource_group_name=resource_group_name,
            routing_rule=routing_rule,
            backend_pool_settings=backend_pool_settings,
            friendly_name=friendly_name,
            id=id,
            load_balancer_enabled=load_balancer_enabled,
            tags=tags,
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

    @jsii.member(jsii_name="putBackendPool")
    def put_backend_pool(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPool", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Frontdoor.put_backend_pool)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackendPool", [value]))

    @jsii.member(jsii_name="putBackendPoolHealthProbe")
    def put_backend_pool_health_probe(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPoolHealthProbe", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Frontdoor.put_backend_pool_health_probe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackendPoolHealthProbe", [value]))

    @jsii.member(jsii_name="putBackendPoolLoadBalancing")
    def put_backend_pool_load_balancing(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPoolLoadBalancing", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Frontdoor.put_backend_pool_load_balancing)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackendPoolLoadBalancing", [value]))

    @jsii.member(jsii_name="putBackendPoolSettings")
    def put_backend_pool_settings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPoolSettings", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Frontdoor.put_backend_pool_settings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackendPoolSettings", [value]))

    @jsii.member(jsii_name="putFrontendEndpoint")
    def put_frontend_endpoint(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorFrontendEndpoint", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Frontdoor.put_frontend_endpoint)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFrontendEndpoint", [value]))

    @jsii.member(jsii_name="putRoutingRule")
    def put_routing_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorRoutingRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Frontdoor.put_routing_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutingRule", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#create Frontdoor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#delete Frontdoor#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#read Frontdoor#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#update Frontdoor#update}.
        '''
        value = FrontdoorTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBackendPoolSettings")
    def reset_backend_pool_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendPoolSettings", []))

    @jsii.member(jsii_name="resetFriendlyName")
    def reset_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFriendlyName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoadBalancerEnabled")
    def reset_load_balancer_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="backendPool")
    def backend_pool(self) -> "FrontdoorBackendPoolList":
        return typing.cast("FrontdoorBackendPoolList", jsii.get(self, "backendPool"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolHealthProbe")
    def backend_pool_health_probe(self) -> "FrontdoorBackendPoolHealthProbeList":
        return typing.cast("FrontdoorBackendPoolHealthProbeList", jsii.get(self, "backendPoolHealthProbe"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolHealthProbes")
    def backend_pool_health_probes(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "backendPoolHealthProbes"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolLoadBalancing")
    def backend_pool_load_balancing(self) -> "FrontdoorBackendPoolLoadBalancingList":
        return typing.cast("FrontdoorBackendPoolLoadBalancingList", jsii.get(self, "backendPoolLoadBalancing"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolLoadBalancingSettings")
    def backend_pool_load_balancing_settings(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "backendPoolLoadBalancingSettings"))

    @builtins.property
    @jsii.member(jsii_name="backendPools")
    def backend_pools(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "backendPools"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolSettings")
    def backend_pool_settings(self) -> "FrontdoorBackendPoolSettingsList":
        return typing.cast("FrontdoorBackendPoolSettingsList", jsii.get(self, "backendPoolSettings"))

    @builtins.property
    @jsii.member(jsii_name="cname")
    def cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cname"))

    @builtins.property
    @jsii.member(jsii_name="explicitResourceOrder")
    def explicit_resource_order(self) -> "FrontdoorExplicitResourceOrderList":
        return typing.cast("FrontdoorExplicitResourceOrderList", jsii.get(self, "explicitResourceOrder"))

    @builtins.property
    @jsii.member(jsii_name="frontendEndpoint")
    def frontend_endpoint(self) -> "FrontdoorFrontendEndpointList":
        return typing.cast("FrontdoorFrontendEndpointList", jsii.get(self, "frontendEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="frontendEndpoints")
    def frontend_endpoints(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "frontendEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="headerFrontdoorId")
    def header_frontdoor_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "headerFrontdoorId"))

    @builtins.property
    @jsii.member(jsii_name="routingRule")
    def routing_rule(self) -> "FrontdoorRoutingRuleList":
        return typing.cast("FrontdoorRoutingRuleList", jsii.get(self, "routingRule"))

    @builtins.property
    @jsii.member(jsii_name="routingRules")
    def routing_rules(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "routingRules"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FrontdoorTimeoutsOutputReference":
        return typing.cast("FrontdoorTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolHealthProbeInput")
    def backend_pool_health_probe_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolHealthProbe"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolHealthProbe"]]], jsii.get(self, "backendPoolHealthProbeInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolInput")
    def backend_pool_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPool"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPool"]]], jsii.get(self, "backendPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolLoadBalancingInput")
    def backend_pool_load_balancing_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolLoadBalancing"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolLoadBalancing"]]], jsii.get(self, "backendPoolLoadBalancingInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolSettingsInput")
    def backend_pool_settings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolSettings"]]], jsii.get(self, "backendPoolSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyNameInput")
    def friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "friendlyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendEndpointInput")
    def frontend_endpoint_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorFrontendEndpoint"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorFrontendEndpoint"]]], jsii.get(self, "frontendEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerEnabledInput")
    def load_balancer_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "loadBalancerEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="routingRuleInput")
    def routing_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorRoutingRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FrontdoorRoutingRule"]]], jsii.get(self, "routingRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["FrontdoorTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FrontdoorTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyName")
    def friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "friendlyName"))

    @friendly_name.setter
    def friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Frontdoor, "friendly_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "friendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Frontdoor, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerEnabled")
    def load_balancer_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "loadBalancerEnabled"))

    @load_balancer_enabled.setter
    def load_balancer_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Frontdoor, "load_balancer_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Frontdoor, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Frontdoor, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Frontdoor, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPool",
    jsii_struct_bases=[],
    name_mapping={
        "backend": "backend",
        "health_probe_name": "healthProbeName",
        "load_balancing_name": "loadBalancingName",
        "name": "name",
    },
)
class FrontdoorBackendPool:
    def __init__(
        self,
        *,
        backend: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorBackendPoolBackend", typing.Dict[str, typing.Any]]]],
        health_probe_name: builtins.str,
        load_balancing_name: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param backend: backend block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend Frontdoor#backend}
        :param health_probe_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#health_probe_name Frontdoor#health_probe_name}.
        :param load_balancing_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#load_balancing_name Frontdoor#load_balancing_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPool.__init__)
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument health_probe_name", value=health_probe_name, expected_type=type_hints["health_probe_name"])
            check_type(argname="argument load_balancing_name", value=load_balancing_name, expected_type=type_hints["load_balancing_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
            "health_probe_name": health_probe_name,
            "load_balancing_name": load_balancing_name,
            "name": name,
        }

    @builtins.property
    def backend(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolBackend"]]:
        '''backend block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend Frontdoor#backend}
        '''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FrontdoorBackendPoolBackend"]], result)

    @builtins.property
    def health_probe_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#health_probe_name Frontdoor#health_probe_name}.'''
        result = self._values.get("health_probe_name")
        assert result is not None, "Required property 'health_probe_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancing_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#load_balancing_name Frontdoor#load_balancing_name}.'''
        result = self._values.get("load_balancing_name")
        assert result is not None, "Required property 'load_balancing_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorBackendPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolBackend",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "host_header": "hostHeader",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "enabled": "enabled",
        "priority": "priority",
        "weight": "weight",
    },
)
class FrontdoorBackendPoolBackend:
    def __init__(
        self,
        *,
        address: builtins.str,
        host_header: builtins.str,
        http_port: jsii.Number,
        https_port: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        priority: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#address Frontdoor#address}.
        :param host_header: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#host_header Frontdoor#host_header}.
        :param http_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#http_port Frontdoor#http_port}.
        :param https_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#https_port Frontdoor#https_port}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enabled Frontdoor#enabled}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#priority Frontdoor#priority}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#weight Frontdoor#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolBackend.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument host_header", value=host_header, expected_type=type_hints["host_header"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
            "host_header": host_header,
            "http_port": http_port,
            "https_port": https_port,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if priority is not None:
            self._values["priority"] = priority
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#address Frontdoor#address}.'''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_header(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#host_header Frontdoor#host_header}.'''
        result = self._values.get("host_header")
        assert result is not None, "Required property 'host_header' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#http_port Frontdoor#http_port}.'''
        result = self._values.get("http_port")
        assert result is not None, "Required property 'http_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def https_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#https_port Frontdoor#https_port}.'''
        result = self._values.get("https_port")
        assert result is not None, "Required property 'https_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enabled Frontdoor#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#priority Frontdoor#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#weight Frontdoor#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorBackendPoolBackend(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorBackendPoolBackendList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolBackendList",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolBackendList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FrontdoorBackendPoolBackendOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolBackendList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorBackendPoolBackendOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolBackend]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolBackend]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolBackend]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorBackendPoolBackendOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolBackendOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolBackendOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="hostHeaderInput")
    def host_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="httpPortInput")
    def http_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpPortInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsPortInput")
    def https_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpsPortInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="hostHeader")
    def host_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostHeader"))

    @host_header.setter
    def host_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "host_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostHeader", value)

    @builtins.property
    @jsii.member(jsii_name="httpPort")
    def http_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPort"))

    @http_port.setter
    def http_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "http_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPort", value)

    @builtins.property
    @jsii.member(jsii_name="httpsPort")
    def https_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpsPort"))

    @https_port.setter
    def https_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "https_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpsPort", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorBackendPoolBackend, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorBackendPoolBackend, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorBackendPoolBackend, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolBackendOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolHealthProbe",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "enabled": "enabled",
        "interval_in_seconds": "intervalInSeconds",
        "path": "path",
        "probe_method": "probeMethod",
        "protocol": "protocol",
    },
)
class FrontdoorBackendPoolHealthProbe:
    def __init__(
        self,
        *,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        interval_in_seconds: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        probe_method: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enabled Frontdoor#enabled}.
        :param interval_in_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#interval_in_seconds Frontdoor#interval_in_seconds}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#path Frontdoor#path}.
        :param probe_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#probe_method Frontdoor#probe_method}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#protocol Frontdoor#protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolHealthProbe.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument probe_method", value=probe_method, expected_type=type_hints["probe_method"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if interval_in_seconds is not None:
            self._values["interval_in_seconds"] = interval_in_seconds
        if path is not None:
            self._values["path"] = path
        if probe_method is not None:
            self._values["probe_method"] = probe_method
        if protocol is not None:
            self._values["protocol"] = protocol

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enabled Frontdoor#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#interval_in_seconds Frontdoor#interval_in_seconds}.'''
        result = self._values.get("interval_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#path Frontdoor#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def probe_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#probe_method Frontdoor#probe_method}.'''
        result = self._values.get("probe_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#protocol Frontdoor#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorBackendPoolHealthProbe(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorBackendPoolHealthProbeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolHealthProbeList",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolHealthProbeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FrontdoorBackendPoolHealthProbeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolHealthProbeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorBackendPoolHealthProbeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolHealthProbe]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolHealthProbe]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolHealthProbe]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorBackendPoolHealthProbeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolHealthProbeOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolHealthProbeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetIntervalInSeconds")
    def reset_interval_in_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntervalInSeconds", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetProbeMethod")
    def reset_probe_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProbeMethod", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInSecondsInput")
    def interval_in_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="probeMethodInput")
    def probe_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "probeMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="intervalInSeconds")
    def interval_in_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalInSeconds"))

    @interval_in_seconds.setter
    def interval_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeOutputReference, "interval_in_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="probeMethod")
    def probe_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "probeMethod"))

    @probe_method.setter
    def probe_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeOutputReference, "probe_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probeMethod", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorBackendPoolHealthProbe, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorBackendPoolHealthProbe, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorBackendPoolHealthProbe, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolHealthProbeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorBackendPoolList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolList",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FrontdoorBackendPoolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorBackendPoolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPool]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPool]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPool]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolLoadBalancing",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "additional_latency_milliseconds": "additionalLatencyMilliseconds",
        "sample_size": "sampleSize",
        "successful_samples_required": "successfulSamplesRequired",
    },
)
class FrontdoorBackendPoolLoadBalancing:
    def __init__(
        self,
        *,
        name: builtins.str,
        additional_latency_milliseconds: typing.Optional[jsii.Number] = None,
        sample_size: typing.Optional[jsii.Number] = None,
        successful_samples_required: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.
        :param additional_latency_milliseconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#additional_latency_milliseconds Frontdoor#additional_latency_milliseconds}.
        :param sample_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#sample_size Frontdoor#sample_size}.
        :param successful_samples_required: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#successful_samples_required Frontdoor#successful_samples_required}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolLoadBalancing.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_latency_milliseconds", value=additional_latency_milliseconds, expected_type=type_hints["additional_latency_milliseconds"])
            check_type(argname="argument sample_size", value=sample_size, expected_type=type_hints["sample_size"])
            check_type(argname="argument successful_samples_required", value=successful_samples_required, expected_type=type_hints["successful_samples_required"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if additional_latency_milliseconds is not None:
            self._values["additional_latency_milliseconds"] = additional_latency_milliseconds
        if sample_size is not None:
            self._values["sample_size"] = sample_size
        if successful_samples_required is not None:
            self._values["successful_samples_required"] = successful_samples_required

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_latency_milliseconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#additional_latency_milliseconds Frontdoor#additional_latency_milliseconds}.'''
        result = self._values.get("additional_latency_milliseconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sample_size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#sample_size Frontdoor#sample_size}.'''
        result = self._values.get("sample_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def successful_samples_required(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#successful_samples_required Frontdoor#successful_samples_required}.'''
        result = self._values.get("successful_samples_required")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorBackendPoolLoadBalancing(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorBackendPoolLoadBalancingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolLoadBalancingList",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolLoadBalancingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FrontdoorBackendPoolLoadBalancingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolLoadBalancingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorBackendPoolLoadBalancingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolLoadBalancing]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolLoadBalancing]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolLoadBalancing]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorBackendPoolLoadBalancingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolLoadBalancingOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolLoadBalancingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAdditionalLatencyMilliseconds")
    def reset_additional_latency_milliseconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalLatencyMilliseconds", []))

    @jsii.member(jsii_name="resetSampleSize")
    def reset_sample_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleSize", []))

    @jsii.member(jsii_name="resetSuccessfulSamplesRequired")
    def reset_successful_samples_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessfulSamplesRequired", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="additionalLatencyMillisecondsInput")
    def additional_latency_milliseconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "additionalLatencyMillisecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleSizeInput")
    def sample_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sampleSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="successfulSamplesRequiredInput")
    def successful_samples_required_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successfulSamplesRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalLatencyMilliseconds")
    def additional_latency_milliseconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "additionalLatencyMilliseconds"))

    @additional_latency_milliseconds.setter
    def additional_latency_milliseconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingOutputReference, "additional_latency_milliseconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalLatencyMilliseconds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sampleSize")
    def sample_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sampleSize"))

    @sample_size.setter
    def sample_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingOutputReference, "sample_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleSize", value)

    @builtins.property
    @jsii.member(jsii_name="successfulSamplesRequired")
    def successful_samples_required(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successfulSamplesRequired"))

    @successful_samples_required.setter
    def successful_samples_required(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingOutputReference, "successful_samples_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successfulSamplesRequired", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorBackendPoolLoadBalancing, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorBackendPoolLoadBalancing, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorBackendPoolLoadBalancing, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolLoadBalancingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorBackendPoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackend")
    def put_backend(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FrontdoorBackendPoolBackend, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolOutputReference.put_backend)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackend", [value]))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> FrontdoorBackendPoolBackendList:
        return typing.cast(FrontdoorBackendPoolBackendList, jsii.get(self, "backend"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolBackend]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolBackend]]], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="healthProbeNameInput")
    def health_probe_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthProbeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingNameInput")
    def load_balancing_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="healthProbeName")
    def health_probe_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthProbeName"))

    @health_probe_name.setter
    def health_probe_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolOutputReference, "health_probe_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthProbeName", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingName")
    def load_balancing_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingName"))

    @load_balancing_name.setter
    def load_balancing_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolOutputReference, "load_balancing_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorBackendPool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorBackendPool, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorBackendPool, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enforce_backend_pools_certificate_name_check": "enforceBackendPoolsCertificateNameCheck",
        "backend_pools_send_receive_timeout_seconds": "backendPoolsSendReceiveTimeoutSeconds",
    },
)
class FrontdoorBackendPoolSettings:
    def __init__(
        self,
        *,
        enforce_backend_pools_certificate_name_check: typing.Union[builtins.bool, cdktf.IResolvable],
        backend_pools_send_receive_timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enforce_backend_pools_certificate_name_check: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enforce_backend_pools_certificate_name_check Frontdoor#enforce_backend_pools_certificate_name_check}.
        :param backend_pools_send_receive_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pools_send_receive_timeout_seconds Frontdoor#backend_pools_send_receive_timeout_seconds}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolSettings.__init__)
            check_type(argname="argument enforce_backend_pools_certificate_name_check", value=enforce_backend_pools_certificate_name_check, expected_type=type_hints["enforce_backend_pools_certificate_name_check"])
            check_type(argname="argument backend_pools_send_receive_timeout_seconds", value=backend_pools_send_receive_timeout_seconds, expected_type=type_hints["backend_pools_send_receive_timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "enforce_backend_pools_certificate_name_check": enforce_backend_pools_certificate_name_check,
        }
        if backend_pools_send_receive_timeout_seconds is not None:
            self._values["backend_pools_send_receive_timeout_seconds"] = backend_pools_send_receive_timeout_seconds

    @builtins.property
    def enforce_backend_pools_certificate_name_check(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enforce_backend_pools_certificate_name_check Frontdoor#enforce_backend_pools_certificate_name_check}.'''
        result = self._values.get("enforce_backend_pools_certificate_name_check")
        assert result is not None, "Required property 'enforce_backend_pools_certificate_name_check' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def backend_pools_send_receive_timeout_seconds(
        self,
    ) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pools_send_receive_timeout_seconds Frontdoor#backend_pools_send_receive_timeout_seconds}.'''
        result = self._values.get("backend_pools_send_receive_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorBackendPoolSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorBackendPoolSettingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolSettingsList",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolSettingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FrontdoorBackendPoolSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorBackendPoolSettingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorBackendPoolSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolSettingsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolSettingsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolSettingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolSettings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolSettingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorBackendPoolSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorBackendPoolSettingsOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorBackendPoolSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBackendPoolsSendReceiveTimeoutSeconds")
    def reset_backend_pools_send_receive_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendPoolsSendReceiveTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="backendPoolsSendReceiveTimeoutSecondsInput")
    def backend_pools_send_receive_timeout_seconds_input(
        self,
    ) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backendPoolsSendReceiveTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceBackendPoolsCertificateNameCheckInput")
    def enforce_backend_pools_certificate_name_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforceBackendPoolsCertificateNameCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolsSendReceiveTimeoutSeconds")
    def backend_pools_send_receive_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backendPoolsSendReceiveTimeoutSeconds"))

    @backend_pools_send_receive_timeout_seconds.setter
    def backend_pools_send_receive_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolSettingsOutputReference, "backend_pools_send_receive_timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPoolsSendReceiveTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="enforceBackendPoolsCertificateNameCheck")
    def enforce_backend_pools_certificate_name_check(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforceBackendPoolsCertificateNameCheck"))

    @enforce_backend_pools_certificate_name_check.setter
    def enforce_backend_pools_certificate_name_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolSettingsOutputReference, "enforce_backend_pools_certificate_name_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceBackendPoolsCertificateNameCheck", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorBackendPoolSettings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorBackendPoolSettings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorBackendPoolSettings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorBackendPoolSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend_pool": "backendPool",
        "backend_pool_health_probe": "backendPoolHealthProbe",
        "backend_pool_load_balancing": "backendPoolLoadBalancing",
        "frontend_endpoint": "frontendEndpoint",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "routing_rule": "routingRule",
        "backend_pool_settings": "backendPoolSettings",
        "friendly_name": "friendlyName",
        "id": "id",
        "load_balancer_enabled": "loadBalancerEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class FrontdoorConfig(cdktf.TerraformMetaArguments):
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
        backend_pool: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FrontdoorBackendPool, typing.Dict[str, typing.Any]]]],
        backend_pool_health_probe: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FrontdoorBackendPoolHealthProbe, typing.Dict[str, typing.Any]]]],
        backend_pool_load_balancing: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FrontdoorBackendPoolLoadBalancing, typing.Dict[str, typing.Any]]]],
        frontend_endpoint: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorFrontendEndpoint", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        resource_group_name: builtins.str,
        routing_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FrontdoorRoutingRule", typing.Dict[str, typing.Any]]]],
        backend_pool_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[FrontdoorBackendPoolSettings, typing.Dict[str, typing.Any]]]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["FrontdoorTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend_pool: backend_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool Frontdoor#backend_pool}
        :param backend_pool_health_probe: backend_pool_health_probe block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_health_probe Frontdoor#backend_pool_health_probe}
        :param backend_pool_load_balancing: backend_pool_load_balancing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_load_balancing Frontdoor#backend_pool_load_balancing}
        :param frontend_endpoint: frontend_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#frontend_endpoint Frontdoor#frontend_endpoint}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#resource_group_name Frontdoor#resource_group_name}.
        :param routing_rule: routing_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#routing_rule Frontdoor#routing_rule}
        :param backend_pool_settings: backend_pool_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_settings Frontdoor#backend_pool_settings}
        :param friendly_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#friendly_name Frontdoor#friendly_name}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#id Frontdoor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#load_balancer_enabled Frontdoor#load_balancer_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#tags Frontdoor#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#timeouts Frontdoor#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = FrontdoorTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend_pool", value=backend_pool, expected_type=type_hints["backend_pool"])
            check_type(argname="argument backend_pool_health_probe", value=backend_pool_health_probe, expected_type=type_hints["backend_pool_health_probe"])
            check_type(argname="argument backend_pool_load_balancing", value=backend_pool_load_balancing, expected_type=type_hints["backend_pool_load_balancing"])
            check_type(argname="argument frontend_endpoint", value=frontend_endpoint, expected_type=type_hints["frontend_endpoint"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument routing_rule", value=routing_rule, expected_type=type_hints["routing_rule"])
            check_type(argname="argument backend_pool_settings", value=backend_pool_settings, expected_type=type_hints["backend_pool_settings"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument load_balancer_enabled", value=load_balancer_enabled, expected_type=type_hints["load_balancer_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_pool": backend_pool,
            "backend_pool_health_probe": backend_pool_health_probe,
            "backend_pool_load_balancing": backend_pool_load_balancing,
            "frontend_endpoint": frontend_endpoint,
            "name": name,
            "resource_group_name": resource_group_name,
            "routing_rule": routing_rule,
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
        if backend_pool_settings is not None:
            self._values["backend_pool_settings"] = backend_pool_settings
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if id is not None:
            self._values["id"] = id
        if load_balancer_enabled is not None:
            self._values["load_balancer_enabled"] = load_balancer_enabled
        if tags is not None:
            self._values["tags"] = tags
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
    def backend_pool(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPool]]:
        '''backend_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool Frontdoor#backend_pool}
        '''
        result = self._values.get("backend_pool")
        assert result is not None, "Required property 'backend_pool' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPool]], result)

    @builtins.property
    def backend_pool_health_probe(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolHealthProbe]]:
        '''backend_pool_health_probe block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_health_probe Frontdoor#backend_pool_health_probe}
        '''
        result = self._values.get("backend_pool_health_probe")
        assert result is not None, "Required property 'backend_pool_health_probe' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolHealthProbe]], result)

    @builtins.property
    def backend_pool_load_balancing(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolLoadBalancing]]:
        '''backend_pool_load_balancing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_load_balancing Frontdoor#backend_pool_load_balancing}
        '''
        result = self._values.get("backend_pool_load_balancing")
        assert result is not None, "Required property 'backend_pool_load_balancing' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolLoadBalancing]], result)

    @builtins.property
    def frontend_endpoint(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FrontdoorFrontendEndpoint"]]:
        '''frontend_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#frontend_endpoint Frontdoor#frontend_endpoint}
        '''
        result = self._values.get("frontend_endpoint")
        assert result is not None, "Required property 'frontend_endpoint' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FrontdoorFrontendEndpoint"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#resource_group_name Frontdoor#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def routing_rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["FrontdoorRoutingRule"]]:
        '''routing_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#routing_rule Frontdoor#routing_rule}
        '''
        result = self._values.get("routing_rule")
        assert result is not None, "Required property 'routing_rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["FrontdoorRoutingRule"]], result)

    @builtins.property
    def backend_pool_settings(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolSettings]]]:
        '''backend_pool_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_settings Frontdoor#backend_pool_settings}
        '''
        result = self._values.get("backend_pool_settings")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorBackendPoolSettings]]], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#friendly_name Frontdoor#friendly_name}.'''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#id Frontdoor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#load_balancer_enabled Frontdoor#load_balancer_enabled}.'''
        result = self._values.get("load_balancer_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#tags Frontdoor#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FrontdoorTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#timeouts Frontdoor#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FrontdoorTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorExplicitResourceOrder",
    jsii_struct_bases=[],
    name_mapping={},
)
class FrontdoorExplicitResourceOrder:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorExplicitResourceOrder(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorExplicitResourceOrderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorExplicitResourceOrderList",
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
            type_hints = typing.get_type_hints(FrontdoorExplicitResourceOrderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "FrontdoorExplicitResourceOrderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorExplicitResourceOrderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorExplicitResourceOrderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorExplicitResourceOrderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorExplicitResourceOrderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorExplicitResourceOrderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class FrontdoorExplicitResourceOrderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorExplicitResourceOrderOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorExplicitResourceOrderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="backendPoolHealthProbeIds")
    def backend_pool_health_probe_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "backendPoolHealthProbeIds"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolIds")
    def backend_pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "backendPoolIds"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolLoadBalancingIds")
    def backend_pool_load_balancing_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "backendPoolLoadBalancingIds"))

    @builtins.property
    @jsii.member(jsii_name="frontendEndpointIds")
    def frontend_endpoint_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "frontendEndpointIds"))

    @builtins.property
    @jsii.member(jsii_name="routingRuleIds")
    def routing_rule_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "routingRuleIds"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[FrontdoorExplicitResourceOrder]:
        return typing.cast(typing.Optional[FrontdoorExplicitResourceOrder], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FrontdoorExplicitResourceOrder],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorExplicitResourceOrderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorFrontendEndpoint",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "name": "name",
        "session_affinity_enabled": "sessionAffinityEnabled",
        "session_affinity_ttl_seconds": "sessionAffinityTtlSeconds",
        "web_application_firewall_policy_link_id": "webApplicationFirewallPolicyLinkId",
    },
)
class FrontdoorFrontendEndpoint:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        name: builtins.str,
        session_affinity_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        session_affinity_ttl_seconds: typing.Optional[jsii.Number] = None,
        web_application_firewall_policy_link_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#host_name Frontdoor#host_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.
        :param session_affinity_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#session_affinity_enabled Frontdoor#session_affinity_enabled}.
        :param session_affinity_ttl_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#session_affinity_ttl_seconds Frontdoor#session_affinity_ttl_seconds}.
        :param web_application_firewall_policy_link_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#web_application_firewall_policy_link_id Frontdoor#web_application_firewall_policy_link_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorFrontendEndpoint.__init__)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument session_affinity_enabled", value=session_affinity_enabled, expected_type=type_hints["session_affinity_enabled"])
            check_type(argname="argument session_affinity_ttl_seconds", value=session_affinity_ttl_seconds, expected_type=type_hints["session_affinity_ttl_seconds"])
            check_type(argname="argument web_application_firewall_policy_link_id", value=web_application_firewall_policy_link_id, expected_type=type_hints["web_application_firewall_policy_link_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "host_name": host_name,
            "name": name,
        }
        if session_affinity_enabled is not None:
            self._values["session_affinity_enabled"] = session_affinity_enabled
        if session_affinity_ttl_seconds is not None:
            self._values["session_affinity_ttl_seconds"] = session_affinity_ttl_seconds
        if web_application_firewall_policy_link_id is not None:
            self._values["web_application_firewall_policy_link_id"] = web_application_firewall_policy_link_id

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#host_name Frontdoor#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def session_affinity_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#session_affinity_enabled Frontdoor#session_affinity_enabled}.'''
        result = self._values.get("session_affinity_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def session_affinity_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#session_affinity_ttl_seconds Frontdoor#session_affinity_ttl_seconds}.'''
        result = self._values.get("session_affinity_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def web_application_firewall_policy_link_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#web_application_firewall_policy_link_id Frontdoor#web_application_firewall_policy_link_id}.'''
        result = self._values.get("web_application_firewall_policy_link_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorFrontendEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorFrontendEndpointList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorFrontendEndpointList",
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
            type_hints = typing.get_type_hints(FrontdoorFrontendEndpointList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FrontdoorFrontendEndpointOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorFrontendEndpointList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorFrontendEndpointOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorFrontendEndpoint]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorFrontendEndpoint]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorFrontendEndpoint]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorFrontendEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorFrontendEndpointOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorFrontendEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSessionAffinityEnabled")
    def reset_session_affinity_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinityEnabled", []))

    @jsii.member(jsii_name="resetSessionAffinityTtlSeconds")
    def reset_session_affinity_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinityTtlSeconds", []))

    @jsii.member(jsii_name="resetWebApplicationFirewallPolicyLinkId")
    def reset_web_application_firewall_policy_link_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebApplicationFirewallPolicyLinkId", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityEnabledInput")
    def session_affinity_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sessionAffinityEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityTtlSecondsInput")
    def session_affinity_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionAffinityTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="webApplicationFirewallPolicyLinkIdInput")
    def web_application_firewall_policy_link_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "webApplicationFirewallPolicyLinkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointOutputReference, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityEnabled")
    def session_affinity_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sessionAffinityEnabled"))

    @session_affinity_enabled.setter
    def session_affinity_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointOutputReference, "session_affinity_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinityEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityTtlSeconds")
    def session_affinity_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionAffinityTtlSeconds"))

    @session_affinity_ttl_seconds.setter
    def session_affinity_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointOutputReference, "session_affinity_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinityTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="webApplicationFirewallPolicyLinkId")
    def web_application_firewall_policy_link_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webApplicationFirewallPolicyLinkId"))

    @web_application_firewall_policy_link_id.setter
    def web_application_firewall_policy_link_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointOutputReference, "web_application_firewall_policy_link_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "webApplicationFirewallPolicyLinkId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorFrontendEndpoint, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorFrontendEndpoint, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorFrontendEndpoint, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorFrontendEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorRoutingRule",
    jsii_struct_bases=[],
    name_mapping={
        "accepted_protocols": "acceptedProtocols",
        "frontend_endpoints": "frontendEndpoints",
        "name": "name",
        "patterns_to_match": "patternsToMatch",
        "enabled": "enabled",
        "forwarding_configuration": "forwardingConfiguration",
        "redirect_configuration": "redirectConfiguration",
    },
)
class FrontdoorRoutingRule:
    def __init__(
        self,
        *,
        accepted_protocols: typing.Sequence[builtins.str],
        frontend_endpoints: typing.Sequence[builtins.str],
        name: builtins.str,
        patterns_to_match: typing.Sequence[builtins.str],
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_configuration: typing.Optional[typing.Union["FrontdoorRoutingRuleForwardingConfiguration", typing.Dict[str, typing.Any]]] = None,
        redirect_configuration: typing.Optional[typing.Union["FrontdoorRoutingRuleRedirectConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param accepted_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#accepted_protocols Frontdoor#accepted_protocols}.
        :param frontend_endpoints: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#frontend_endpoints Frontdoor#frontend_endpoints}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.
        :param patterns_to_match: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#patterns_to_match Frontdoor#patterns_to_match}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enabled Frontdoor#enabled}.
        :param forwarding_configuration: forwarding_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#forwarding_configuration Frontdoor#forwarding_configuration}
        :param redirect_configuration: redirect_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_configuration Frontdoor#redirect_configuration}
        '''
        if isinstance(forwarding_configuration, dict):
            forwarding_configuration = FrontdoorRoutingRuleForwardingConfiguration(**forwarding_configuration)
        if isinstance(redirect_configuration, dict):
            redirect_configuration = FrontdoorRoutingRuleRedirectConfiguration(**redirect_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorRoutingRule.__init__)
            check_type(argname="argument accepted_protocols", value=accepted_protocols, expected_type=type_hints["accepted_protocols"])
            check_type(argname="argument frontend_endpoints", value=frontend_endpoints, expected_type=type_hints["frontend_endpoints"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument patterns_to_match", value=patterns_to_match, expected_type=type_hints["patterns_to_match"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument forwarding_configuration", value=forwarding_configuration, expected_type=type_hints["forwarding_configuration"])
            check_type(argname="argument redirect_configuration", value=redirect_configuration, expected_type=type_hints["redirect_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "accepted_protocols": accepted_protocols,
            "frontend_endpoints": frontend_endpoints,
            "name": name,
            "patterns_to_match": patterns_to_match,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if forwarding_configuration is not None:
            self._values["forwarding_configuration"] = forwarding_configuration
        if redirect_configuration is not None:
            self._values["redirect_configuration"] = redirect_configuration

    @builtins.property
    def accepted_protocols(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#accepted_protocols Frontdoor#accepted_protocols}.'''
        result = self._values.get("accepted_protocols")
        assert result is not None, "Required property 'accepted_protocols' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def frontend_endpoints(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#frontend_endpoints Frontdoor#frontend_endpoints}.'''
        result = self._values.get("frontend_endpoints")
        assert result is not None, "Required property 'frontend_endpoints' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#name Frontdoor#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def patterns_to_match(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#patterns_to_match Frontdoor#patterns_to_match}.'''
        result = self._values.get("patterns_to_match")
        assert result is not None, "Required property 'patterns_to_match' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#enabled Frontdoor#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forwarding_configuration(
        self,
    ) -> typing.Optional["FrontdoorRoutingRuleForwardingConfiguration"]:
        '''forwarding_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#forwarding_configuration Frontdoor#forwarding_configuration}
        '''
        result = self._values.get("forwarding_configuration")
        return typing.cast(typing.Optional["FrontdoorRoutingRuleForwardingConfiguration"], result)

    @builtins.property
    def redirect_configuration(
        self,
    ) -> typing.Optional["FrontdoorRoutingRuleRedirectConfiguration"]:
        '''redirect_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_configuration Frontdoor#redirect_configuration}
        '''
        result = self._values.get("redirect_configuration")
        return typing.cast(typing.Optional["FrontdoorRoutingRuleRedirectConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorRoutingRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorRoutingRuleForwardingConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "backend_pool_name": "backendPoolName",
        "cache_duration": "cacheDuration",
        "cache_enabled": "cacheEnabled",
        "cache_query_parameters": "cacheQueryParameters",
        "cache_query_parameter_strip_directive": "cacheQueryParameterStripDirective",
        "cache_use_dynamic_compression": "cacheUseDynamicCompression",
        "custom_forwarding_path": "customForwardingPath",
        "forwarding_protocol": "forwardingProtocol",
    },
)
class FrontdoorRoutingRuleForwardingConfiguration:
    def __init__(
        self,
        *,
        backend_pool_name: builtins.str,
        cache_duration: typing.Optional[builtins.str] = None,
        cache_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_query_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_query_parameter_strip_directive: typing.Optional[builtins.str] = None,
        cache_use_dynamic_compression: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_forwarding_path: typing.Optional[builtins.str] = None,
        forwarding_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_name Frontdoor#backend_pool_name}.
        :param cache_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_duration Frontdoor#cache_duration}.
        :param cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_enabled Frontdoor#cache_enabled}.
        :param cache_query_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_query_parameters Frontdoor#cache_query_parameters}.
        :param cache_query_parameter_strip_directive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_query_parameter_strip_directive Frontdoor#cache_query_parameter_strip_directive}.
        :param cache_use_dynamic_compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_use_dynamic_compression Frontdoor#cache_use_dynamic_compression}.
        :param custom_forwarding_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_forwarding_path Frontdoor#custom_forwarding_path}.
        :param forwarding_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#forwarding_protocol Frontdoor#forwarding_protocol}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorRoutingRuleForwardingConfiguration.__init__)
            check_type(argname="argument backend_pool_name", value=backend_pool_name, expected_type=type_hints["backend_pool_name"])
            check_type(argname="argument cache_duration", value=cache_duration, expected_type=type_hints["cache_duration"])
            check_type(argname="argument cache_enabled", value=cache_enabled, expected_type=type_hints["cache_enabled"])
            check_type(argname="argument cache_query_parameters", value=cache_query_parameters, expected_type=type_hints["cache_query_parameters"])
            check_type(argname="argument cache_query_parameter_strip_directive", value=cache_query_parameter_strip_directive, expected_type=type_hints["cache_query_parameter_strip_directive"])
            check_type(argname="argument cache_use_dynamic_compression", value=cache_use_dynamic_compression, expected_type=type_hints["cache_use_dynamic_compression"])
            check_type(argname="argument custom_forwarding_path", value=custom_forwarding_path, expected_type=type_hints["custom_forwarding_path"])
            check_type(argname="argument forwarding_protocol", value=forwarding_protocol, expected_type=type_hints["forwarding_protocol"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_pool_name": backend_pool_name,
        }
        if cache_duration is not None:
            self._values["cache_duration"] = cache_duration
        if cache_enabled is not None:
            self._values["cache_enabled"] = cache_enabled
        if cache_query_parameters is not None:
            self._values["cache_query_parameters"] = cache_query_parameters
        if cache_query_parameter_strip_directive is not None:
            self._values["cache_query_parameter_strip_directive"] = cache_query_parameter_strip_directive
        if cache_use_dynamic_compression is not None:
            self._values["cache_use_dynamic_compression"] = cache_use_dynamic_compression
        if custom_forwarding_path is not None:
            self._values["custom_forwarding_path"] = custom_forwarding_path
        if forwarding_protocol is not None:
            self._values["forwarding_protocol"] = forwarding_protocol

    @builtins.property
    def backend_pool_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_name Frontdoor#backend_pool_name}.'''
        result = self._values.get("backend_pool_name")
        assert result is not None, "Required property 'backend_pool_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cache_duration(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_duration Frontdoor#cache_duration}.'''
        result = self._values.get("cache_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_enabled Frontdoor#cache_enabled}.'''
        result = self._values.get("cache_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cache_query_parameters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_query_parameters Frontdoor#cache_query_parameters}.'''
        result = self._values.get("cache_query_parameters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_query_parameter_strip_directive(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_query_parameter_strip_directive Frontdoor#cache_query_parameter_strip_directive}.'''
        result = self._values.get("cache_query_parameter_strip_directive")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_use_dynamic_compression(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_use_dynamic_compression Frontdoor#cache_use_dynamic_compression}.'''
        result = self._values.get("cache_use_dynamic_compression")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def custom_forwarding_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_forwarding_path Frontdoor#custom_forwarding_path}.'''
        result = self._values.get("custom_forwarding_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forwarding_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#forwarding_protocol Frontdoor#forwarding_protocol}.'''
        result = self._values.get("forwarding_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorRoutingRuleForwardingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorRoutingRuleForwardingConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorRoutingRuleForwardingConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorRoutingRuleForwardingConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCacheDuration")
    def reset_cache_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheDuration", []))

    @jsii.member(jsii_name="resetCacheEnabled")
    def reset_cache_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheEnabled", []))

    @jsii.member(jsii_name="resetCacheQueryParameters")
    def reset_cache_query_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheQueryParameters", []))

    @jsii.member(jsii_name="resetCacheQueryParameterStripDirective")
    def reset_cache_query_parameter_strip_directive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheQueryParameterStripDirective", []))

    @jsii.member(jsii_name="resetCacheUseDynamicCompression")
    def reset_cache_use_dynamic_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheUseDynamicCompression", []))

    @jsii.member(jsii_name="resetCustomForwardingPath")
    def reset_custom_forwarding_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomForwardingPath", []))

    @jsii.member(jsii_name="resetForwardingProtocol")
    def reset_forwarding_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingProtocol", []))

    @builtins.property
    @jsii.member(jsii_name="backendPoolNameInput")
    def backend_pool_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendPoolNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheDurationInput")
    def cache_duration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheDurationInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheEnabledInput")
    def cache_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cacheEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheQueryParametersInput")
    def cache_query_parameters_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cacheQueryParametersInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheQueryParameterStripDirectiveInput")
    def cache_query_parameter_strip_directive_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheQueryParameterStripDirectiveInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheUseDynamicCompressionInput")
    def cache_use_dynamic_compression_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "cacheUseDynamicCompressionInput"))

    @builtins.property
    @jsii.member(jsii_name="customForwardingPathInput")
    def custom_forwarding_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customForwardingPathInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingProtocolInput")
    def forwarding_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardingProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPoolName")
    def backend_pool_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backendPoolName"))

    @backend_pool_name.setter
    def backend_pool_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "backend_pool_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPoolName", value)

    @builtins.property
    @jsii.member(jsii_name="cacheDuration")
    def cache_duration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheDuration"))

    @cache_duration.setter
    def cache_duration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "cache_duration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheDuration", value)

    @builtins.property
    @jsii.member(jsii_name="cacheEnabled")
    def cache_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cacheEnabled"))

    @cache_enabled.setter
    def cache_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "cache_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cacheQueryParameters")
    def cache_query_parameters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cacheQueryParameters"))

    @cache_query_parameters.setter
    def cache_query_parameters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "cache_query_parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheQueryParameters", value)

    @builtins.property
    @jsii.member(jsii_name="cacheQueryParameterStripDirective")
    def cache_query_parameter_strip_directive(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheQueryParameterStripDirective"))

    @cache_query_parameter_strip_directive.setter
    def cache_query_parameter_strip_directive(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "cache_query_parameter_strip_directive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheQueryParameterStripDirective", value)

    @builtins.property
    @jsii.member(jsii_name="cacheUseDynamicCompression")
    def cache_use_dynamic_compression(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "cacheUseDynamicCompression"))

    @cache_use_dynamic_compression.setter
    def cache_use_dynamic_compression(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "cache_use_dynamic_compression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheUseDynamicCompression", value)

    @builtins.property
    @jsii.member(jsii_name="customForwardingPath")
    def custom_forwarding_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customForwardingPath"))

    @custom_forwarding_path.setter
    def custom_forwarding_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "custom_forwarding_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customForwardingPath", value)

    @builtins.property
    @jsii.member(jsii_name="forwardingProtocol")
    def forwarding_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardingProtocol"))

    @forwarding_protocol.setter
    def forwarding_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "forwarding_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardingProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FrontdoorRoutingRuleForwardingConfiguration]:
        return typing.cast(typing.Optional[FrontdoorRoutingRuleForwardingConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FrontdoorRoutingRuleForwardingConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleForwardingConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorRoutingRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorRoutingRuleList",
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
            type_hints = typing.get_type_hints(FrontdoorRoutingRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FrontdoorRoutingRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorRoutingRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FrontdoorRoutingRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorRoutingRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorRoutingRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FrontdoorRoutingRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FrontdoorRoutingRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorRoutingRuleOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorRoutingRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putForwardingConfiguration")
    def put_forwarding_configuration(
        self,
        *,
        backend_pool_name: builtins.str,
        cache_duration: typing.Optional[builtins.str] = None,
        cache_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cache_query_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_query_parameter_strip_directive: typing.Optional[builtins.str] = None,
        cache_use_dynamic_compression: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        custom_forwarding_path: typing.Optional[builtins.str] = None,
        forwarding_protocol: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backend_pool_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#backend_pool_name Frontdoor#backend_pool_name}.
        :param cache_duration: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_duration Frontdoor#cache_duration}.
        :param cache_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_enabled Frontdoor#cache_enabled}.
        :param cache_query_parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_query_parameters Frontdoor#cache_query_parameters}.
        :param cache_query_parameter_strip_directive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_query_parameter_strip_directive Frontdoor#cache_query_parameter_strip_directive}.
        :param cache_use_dynamic_compression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#cache_use_dynamic_compression Frontdoor#cache_use_dynamic_compression}.
        :param custom_forwarding_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_forwarding_path Frontdoor#custom_forwarding_path}.
        :param forwarding_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#forwarding_protocol Frontdoor#forwarding_protocol}.
        '''
        value = FrontdoorRoutingRuleForwardingConfiguration(
            backend_pool_name=backend_pool_name,
            cache_duration=cache_duration,
            cache_enabled=cache_enabled,
            cache_query_parameters=cache_query_parameters,
            cache_query_parameter_strip_directive=cache_query_parameter_strip_directive,
            cache_use_dynamic_compression=cache_use_dynamic_compression,
            custom_forwarding_path=custom_forwarding_path,
            forwarding_protocol=forwarding_protocol,
        )

        return typing.cast(None, jsii.invoke(self, "putForwardingConfiguration", [value]))

    @jsii.member(jsii_name="putRedirectConfiguration")
    def put_redirect_configuration(
        self,
        *,
        redirect_protocol: builtins.str,
        redirect_type: builtins.str,
        custom_fragment: typing.Optional[builtins.str] = None,
        custom_host: typing.Optional[builtins.str] = None,
        custom_path: typing.Optional[builtins.str] = None,
        custom_query_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param redirect_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_protocol Frontdoor#redirect_protocol}.
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_type Frontdoor#redirect_type}.
        :param custom_fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_fragment Frontdoor#custom_fragment}.
        :param custom_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_host Frontdoor#custom_host}.
        :param custom_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_path Frontdoor#custom_path}.
        :param custom_query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_query_string Frontdoor#custom_query_string}.
        '''
        value = FrontdoorRoutingRuleRedirectConfiguration(
            redirect_protocol=redirect_protocol,
            redirect_type=redirect_type,
            custom_fragment=custom_fragment,
            custom_host=custom_host,
            custom_path=custom_path,
            custom_query_string=custom_query_string,
        )

        return typing.cast(None, jsii.invoke(self, "putRedirectConfiguration", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetForwardingConfiguration")
    def reset_forwarding_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingConfiguration", []))

    @jsii.member(jsii_name="resetRedirectConfiguration")
    def reset_redirect_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="forwardingConfiguration")
    def forwarding_configuration(
        self,
    ) -> FrontdoorRoutingRuleForwardingConfigurationOutputReference:
        return typing.cast(FrontdoorRoutingRuleForwardingConfigurationOutputReference, jsii.get(self, "forwardingConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfiguration")
    def redirect_configuration(
        self,
    ) -> "FrontdoorRoutingRuleRedirectConfigurationOutputReference":
        return typing.cast("FrontdoorRoutingRuleRedirectConfigurationOutputReference", jsii.get(self, "redirectConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="acceptedProtocolsInput")
    def accepted_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "acceptedProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingConfigurationInput")
    def forwarding_configuration_input(
        self,
    ) -> typing.Optional[FrontdoorRoutingRuleForwardingConfiguration]:
        return typing.cast(typing.Optional[FrontdoorRoutingRuleForwardingConfiguration], jsii.get(self, "forwardingConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendEndpointsInput")
    def frontend_endpoints_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "frontendEndpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="patternsToMatchInput")
    def patterns_to_match_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "patternsToMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectConfigurationInput")
    def redirect_configuration_input(
        self,
    ) -> typing.Optional["FrontdoorRoutingRuleRedirectConfiguration"]:
        return typing.cast(typing.Optional["FrontdoorRoutingRuleRedirectConfiguration"], jsii.get(self, "redirectConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="acceptedProtocols")
    def accepted_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "acceptedProtocols"))

    @accepted_protocols.setter
    def accepted_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleOutputReference, "accepted_protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptedProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="frontendEndpoints")
    def frontend_endpoints(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "frontendEndpoints"))

    @frontend_endpoints.setter
    def frontend_endpoints(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleOutputReference, "frontend_endpoints").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="patternsToMatch")
    def patterns_to_match(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "patternsToMatch"))

    @patterns_to_match.setter
    def patterns_to_match(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleOutputReference, "patterns_to_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "patternsToMatch", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorRoutingRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorRoutingRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorRoutingRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorRoutingRuleRedirectConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "redirect_protocol": "redirectProtocol",
        "redirect_type": "redirectType",
        "custom_fragment": "customFragment",
        "custom_host": "customHost",
        "custom_path": "customPath",
        "custom_query_string": "customQueryString",
    },
)
class FrontdoorRoutingRuleRedirectConfiguration:
    def __init__(
        self,
        *,
        redirect_protocol: builtins.str,
        redirect_type: builtins.str,
        custom_fragment: typing.Optional[builtins.str] = None,
        custom_host: typing.Optional[builtins.str] = None,
        custom_path: typing.Optional[builtins.str] = None,
        custom_query_string: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param redirect_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_protocol Frontdoor#redirect_protocol}.
        :param redirect_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_type Frontdoor#redirect_type}.
        :param custom_fragment: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_fragment Frontdoor#custom_fragment}.
        :param custom_host: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_host Frontdoor#custom_host}.
        :param custom_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_path Frontdoor#custom_path}.
        :param custom_query_string: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_query_string Frontdoor#custom_query_string}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorRoutingRuleRedirectConfiguration.__init__)
            check_type(argname="argument redirect_protocol", value=redirect_protocol, expected_type=type_hints["redirect_protocol"])
            check_type(argname="argument redirect_type", value=redirect_type, expected_type=type_hints["redirect_type"])
            check_type(argname="argument custom_fragment", value=custom_fragment, expected_type=type_hints["custom_fragment"])
            check_type(argname="argument custom_host", value=custom_host, expected_type=type_hints["custom_host"])
            check_type(argname="argument custom_path", value=custom_path, expected_type=type_hints["custom_path"])
            check_type(argname="argument custom_query_string", value=custom_query_string, expected_type=type_hints["custom_query_string"])
        self._values: typing.Dict[str, typing.Any] = {
            "redirect_protocol": redirect_protocol,
            "redirect_type": redirect_type,
        }
        if custom_fragment is not None:
            self._values["custom_fragment"] = custom_fragment
        if custom_host is not None:
            self._values["custom_host"] = custom_host
        if custom_path is not None:
            self._values["custom_path"] = custom_path
        if custom_query_string is not None:
            self._values["custom_query_string"] = custom_query_string

    @builtins.property
    def redirect_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_protocol Frontdoor#redirect_protocol}.'''
        result = self._values.get("redirect_protocol")
        assert result is not None, "Required property 'redirect_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def redirect_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#redirect_type Frontdoor#redirect_type}.'''
        result = self._values.get("redirect_type")
        assert result is not None, "Required property 'redirect_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_fragment(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_fragment Frontdoor#custom_fragment}.'''
        result = self._values.get("custom_fragment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_host(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_host Frontdoor#custom_host}.'''
        result = self._values.get("custom_host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_path Frontdoor#custom_path}.'''
        result = self._values.get("custom_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_query_string(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#custom_query_string Frontdoor#custom_query_string}.'''
        result = self._values.get("custom_query_string")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorRoutingRuleRedirectConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorRoutingRuleRedirectConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorRoutingRuleRedirectConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorRoutingRuleRedirectConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomFragment")
    def reset_custom_fragment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomFragment", []))

    @jsii.member(jsii_name="resetCustomHost")
    def reset_custom_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomHost", []))

    @jsii.member(jsii_name="resetCustomPath")
    def reset_custom_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPath", []))

    @jsii.member(jsii_name="resetCustomQueryString")
    def reset_custom_query_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomQueryString", []))

    @builtins.property
    @jsii.member(jsii_name="customFragmentInput")
    def custom_fragment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customFragmentInput"))

    @builtins.property
    @jsii.member(jsii_name="customHostInput")
    def custom_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customHostInput"))

    @builtins.property
    @jsii.member(jsii_name="customPathInput")
    def custom_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customPathInput"))

    @builtins.property
    @jsii.member(jsii_name="customQueryStringInput")
    def custom_query_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customQueryStringInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectProtocolInput")
    def redirect_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectTypeInput")
    def redirect_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "redirectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="customFragment")
    def custom_fragment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customFragment"))

    @custom_fragment.setter
    def custom_fragment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleRedirectConfigurationOutputReference, "custom_fragment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customFragment", value)

    @builtins.property
    @jsii.member(jsii_name="customHost")
    def custom_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customHost"))

    @custom_host.setter
    def custom_host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleRedirectConfigurationOutputReference, "custom_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customHost", value)

    @builtins.property
    @jsii.member(jsii_name="customPath")
    def custom_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customPath"))

    @custom_path.setter
    def custom_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleRedirectConfigurationOutputReference, "custom_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customPath", value)

    @builtins.property
    @jsii.member(jsii_name="customQueryString")
    def custom_query_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customQueryString"))

    @custom_query_string.setter
    def custom_query_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleRedirectConfigurationOutputReference, "custom_query_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customQueryString", value)

    @builtins.property
    @jsii.member(jsii_name="redirectProtocol")
    def redirect_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectProtocol"))

    @redirect_protocol.setter
    def redirect_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleRedirectConfigurationOutputReference, "redirect_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="redirectType")
    def redirect_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectType"))

    @redirect_type.setter
    def redirect_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleRedirectConfigurationOutputReference, "redirect_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[FrontdoorRoutingRuleRedirectConfiguration]:
        return typing.cast(typing.Optional[FrontdoorRoutingRuleRedirectConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[FrontdoorRoutingRuleRedirectConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorRoutingRuleRedirectConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class FrontdoorTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#create Frontdoor#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#delete Frontdoor#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#read Frontdoor#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#update Frontdoor#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FrontdoorTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#create Frontdoor#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#delete Frontdoor#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#read Frontdoor#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/frontdoor#update Frontdoor#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrontdoorTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FrontdoorTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.frontdoor.FrontdoorTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(FrontdoorTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(FrontdoorTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FrontdoorTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FrontdoorTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FrontdoorTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FrontdoorTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Frontdoor",
    "FrontdoorBackendPool",
    "FrontdoorBackendPoolBackend",
    "FrontdoorBackendPoolBackendList",
    "FrontdoorBackendPoolBackendOutputReference",
    "FrontdoorBackendPoolHealthProbe",
    "FrontdoorBackendPoolHealthProbeList",
    "FrontdoorBackendPoolHealthProbeOutputReference",
    "FrontdoorBackendPoolList",
    "FrontdoorBackendPoolLoadBalancing",
    "FrontdoorBackendPoolLoadBalancingList",
    "FrontdoorBackendPoolLoadBalancingOutputReference",
    "FrontdoorBackendPoolOutputReference",
    "FrontdoorBackendPoolSettings",
    "FrontdoorBackendPoolSettingsList",
    "FrontdoorBackendPoolSettingsOutputReference",
    "FrontdoorConfig",
    "FrontdoorExplicitResourceOrder",
    "FrontdoorExplicitResourceOrderList",
    "FrontdoorExplicitResourceOrderOutputReference",
    "FrontdoorFrontendEndpoint",
    "FrontdoorFrontendEndpointList",
    "FrontdoorFrontendEndpointOutputReference",
    "FrontdoorRoutingRule",
    "FrontdoorRoutingRuleForwardingConfiguration",
    "FrontdoorRoutingRuleForwardingConfigurationOutputReference",
    "FrontdoorRoutingRuleList",
    "FrontdoorRoutingRuleOutputReference",
    "FrontdoorRoutingRuleRedirectConfiguration",
    "FrontdoorRoutingRuleRedirectConfigurationOutputReference",
    "FrontdoorTimeouts",
    "FrontdoorTimeoutsOutputReference",
]

publication.publish()
