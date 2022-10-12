'''
# `cloudflare_load_balancer`

Refer to the Terraform Registory for docs: [`cloudflare_load_balancer`](https://www.terraform.io/docs/providers/cloudflare/r/load_balancer).
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


class LoadBalancer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer cloudflare_load_balancer}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        default_pool_ids: typing.Sequence[builtins.str],
        fallback_pool_id: builtins.str,
        name: builtins.str,
        zone_id: builtins.str,
        adaptive_routing: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerAdaptiveRouting", typing.Dict[str, typing.Any]]]]] = None,
        country_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerCountryPools", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        location_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerLocationStrategy", typing.Dict[str, typing.Any]]]]] = None,
        pop_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPopPools", typing.Dict[str, typing.Any]]]]] = None,
        proxied: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        random_steering: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRandomSteering", typing.Dict[str, typing.Any]]]]] = None,
        region_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRegionPools", typing.Dict[str, typing.Any]]]]] = None,
        rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRules", typing.Dict[str, typing.Any]]]]] = None,
        session_affinity: typing.Optional[builtins.str] = None,
        session_affinity_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        session_affinity_ttl: typing.Optional[jsii.Number] = None,
        steering_policy: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer cloudflare_load_balancer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_pool_ids LoadBalancer#default_pool_ids}.
        :param fallback_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#fallback_pool_id LoadBalancer#fallback_pool_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#name LoadBalancer#name}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#zone_id LoadBalancer#zone_id}
        :param adaptive_routing: adaptive_routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#adaptive_routing LoadBalancer#adaptive_routing}
        :param country_pools: country_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country_pools LoadBalancer#country_pools}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#description LoadBalancer#description}.
        :param enabled: Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#enabled LoadBalancer#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#id LoadBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_strategy: location_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location_strategy LoadBalancer#location_strategy}
        :param pop_pools: pop_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop_pools LoadBalancer#pop_pools}
        :param proxied: Defaults to ``false``. Conflicts with ``ttl``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#proxied LoadBalancer#proxied}
        :param random_steering: random_steering block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#random_steering LoadBalancer#random_steering}
        :param region_pools: region_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region_pools LoadBalancer#region_pools}
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#rules LoadBalancer#rules}
        :param session_affinity: Defaults to ``none``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity LoadBalancer#session_affinity}
        :param session_affinity_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_attributes LoadBalancer#session_affinity_attributes}.
        :param session_affinity_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_ttl LoadBalancer#session_affinity_ttl}.
        :param steering_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#steering_policy LoadBalancer#steering_policy}.
        :param ttl: Conflicts with ``proxied``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#ttl LoadBalancer#ttl}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LoadBalancerConfig(
            default_pool_ids=default_pool_ids,
            fallback_pool_id=fallback_pool_id,
            name=name,
            zone_id=zone_id,
            adaptive_routing=adaptive_routing,
            country_pools=country_pools,
            description=description,
            enabled=enabled,
            id=id,
            location_strategy=location_strategy,
            pop_pools=pop_pools,
            proxied=proxied,
            random_steering=random_steering,
            region_pools=region_pools,
            rules=rules,
            session_affinity=session_affinity,
            session_affinity_attributes=session_affinity_attributes,
            session_affinity_ttl=session_affinity_ttl,
            steering_policy=steering_policy,
            ttl=ttl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAdaptiveRouting")
    def put_adaptive_routing(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerAdaptiveRouting", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.put_adaptive_routing)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdaptiveRouting", [value]))

    @jsii.member(jsii_name="putCountryPools")
    def put_country_pools(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerCountryPools", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.put_country_pools)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCountryPools", [value]))

    @jsii.member(jsii_name="putLocationStrategy")
    def put_location_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerLocationStrategy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.put_location_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocationStrategy", [value]))

    @jsii.member(jsii_name="putPopPools")
    def put_pop_pools(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPopPools", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.put_pop_pools)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPopPools", [value]))

    @jsii.member(jsii_name="putRandomSteering")
    def put_random_steering(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRandomSteering", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.put_random_steering)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRandomSteering", [value]))

    @jsii.member(jsii_name="putRegionPools")
    def put_region_pools(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRegionPools", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.put_region_pools)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegionPools", [value]))

    @jsii.member(jsii_name="putRules")
    def put_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRules", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancer.put_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRules", [value]))

    @jsii.member(jsii_name="resetAdaptiveRouting")
    def reset_adaptive_routing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdaptiveRouting", []))

    @jsii.member(jsii_name="resetCountryPools")
    def reset_country_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryPools", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocationStrategy")
    def reset_location_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationStrategy", []))

    @jsii.member(jsii_name="resetPopPools")
    def reset_pop_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPopPools", []))

    @jsii.member(jsii_name="resetProxied")
    def reset_proxied(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxied", []))

    @jsii.member(jsii_name="resetRandomSteering")
    def reset_random_steering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRandomSteering", []))

    @jsii.member(jsii_name="resetRegionPools")
    def reset_region_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionPools", []))

    @jsii.member(jsii_name="resetRules")
    def reset_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRules", []))

    @jsii.member(jsii_name="resetSessionAffinity")
    def reset_session_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinity", []))

    @jsii.member(jsii_name="resetSessionAffinityAttributes")
    def reset_session_affinity_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinityAttributes", []))

    @jsii.member(jsii_name="resetSessionAffinityTtl")
    def reset_session_affinity_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinityTtl", []))

    @jsii.member(jsii_name="resetSteeringPolicy")
    def reset_steering_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSteeringPolicy", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="adaptiveRouting")
    def adaptive_routing(self) -> "LoadBalancerAdaptiveRoutingList":
        return typing.cast("LoadBalancerAdaptiveRoutingList", jsii.get(self, "adaptiveRouting"))

    @builtins.property
    @jsii.member(jsii_name="countryPools")
    def country_pools(self) -> "LoadBalancerCountryPoolsList":
        return typing.cast("LoadBalancerCountryPoolsList", jsii.get(self, "countryPools"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="locationStrategy")
    def location_strategy(self) -> "LoadBalancerLocationStrategyList":
        return typing.cast("LoadBalancerLocationStrategyList", jsii.get(self, "locationStrategy"))

    @builtins.property
    @jsii.member(jsii_name="modifiedOn")
    def modified_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedOn"))

    @builtins.property
    @jsii.member(jsii_name="popPools")
    def pop_pools(self) -> "LoadBalancerPopPoolsList":
        return typing.cast("LoadBalancerPopPoolsList", jsii.get(self, "popPools"))

    @builtins.property
    @jsii.member(jsii_name="randomSteering")
    def random_steering(self) -> "LoadBalancerRandomSteeringList":
        return typing.cast("LoadBalancerRandomSteeringList", jsii.get(self, "randomSteering"))

    @builtins.property
    @jsii.member(jsii_name="regionPools")
    def region_pools(self) -> "LoadBalancerRegionPoolsList":
        return typing.cast("LoadBalancerRegionPoolsList", jsii.get(self, "regionPools"))

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(self) -> "LoadBalancerRulesList":
        return typing.cast("LoadBalancerRulesList", jsii.get(self, "rules"))

    @builtins.property
    @jsii.member(jsii_name="adaptiveRoutingInput")
    def adaptive_routing_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerAdaptiveRouting"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerAdaptiveRouting"]]], jsii.get(self, "adaptiveRoutingInput"))

    @builtins.property
    @jsii.member(jsii_name="countryPoolsInput")
    def country_pools_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerCountryPools"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerCountryPools"]]], jsii.get(self, "countryPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPoolIdsInput")
    def default_pool_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultPoolIdsInput"))

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
    @jsii.member(jsii_name="fallbackPoolIdInput")
    def fallback_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fallbackPoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationStrategyInput")
    def location_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerLocationStrategy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerLocationStrategy"]]], jsii.get(self, "locationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="popPoolsInput")
    def pop_pools_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPopPools"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPopPools"]]], jsii.get(self, "popPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="proxiedInput")
    def proxied_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "proxiedInput"))

    @builtins.property
    @jsii.member(jsii_name="randomSteeringInput")
    def random_steering_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRandomSteering"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRandomSteering"]]], jsii.get(self, "randomSteeringInput"))

    @builtins.property
    @jsii.member(jsii_name="regionPoolsInput")
    def region_pools_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRegionPools"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRegionPools"]]], jsii.get(self, "regionPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="rulesInput")
    def rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRules"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRules"]]], jsii.get(self, "rulesInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityAttributesInput")
    def session_affinity_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sessionAffinityAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityInput")
    def session_affinity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityTtlInput")
    def session_affinity_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionAffinityTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="steeringPolicyInput")
    def steering_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "steeringPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPoolIds")
    def default_pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultPoolIds"))

    @default_pool_ids.setter
    def default_pool_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "default_pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPoolIds", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="fallbackPoolId")
    def fallback_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fallbackPoolId"))

    @fallback_pool_id.setter
    def fallback_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "fallback_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackPoolId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="proxied")
    def proxied(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "proxied"))

    @proxied.setter
    def proxied(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "proxied").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxied", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinity")
    def session_affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionAffinity"))

    @session_affinity.setter
    def session_affinity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "session_affinity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityAttributes")
    def session_affinity_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sessionAffinityAttributes"))

    @session_affinity_attributes.setter
    def session_affinity_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "session_affinity_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinityAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityTtl")
    def session_affinity_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionAffinityTtl"))

    @session_affinity_ttl.setter
    def session_affinity_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "session_affinity_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinityTtl", value)

    @builtins.property
    @jsii.member(jsii_name="steeringPolicy")
    def steering_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "steeringPolicy"))

    @steering_policy.setter
    def steering_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "steering_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "steeringPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancer, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerAdaptiveRouting",
    jsii_struct_bases=[],
    name_mapping={"failover_across_pools": "failoverAcrossPools"},
)
class LoadBalancerAdaptiveRouting:
    def __init__(
        self,
        *,
        failover_across_pools: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param failover_across_pools: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#failover_across_pools LoadBalancer#failover_across_pools}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerAdaptiveRouting.__init__)
            check_type(argname="argument failover_across_pools", value=failover_across_pools, expected_type=type_hints["failover_across_pools"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failover_across_pools is not None:
            self._values["failover_across_pools"] = failover_across_pools

    @builtins.property
    def failover_across_pools(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#failover_across_pools LoadBalancer#failover_across_pools}.'''
        result = self._values.get("failover_across_pools")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerAdaptiveRouting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerAdaptiveRoutingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerAdaptiveRoutingList",
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
            type_hints = typing.get_type_hints(LoadBalancerAdaptiveRoutingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerAdaptiveRoutingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerAdaptiveRoutingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerAdaptiveRoutingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerAdaptiveRoutingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerAdaptiveRoutingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerAdaptiveRoutingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerAdaptiveRouting]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerAdaptiveRouting]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerAdaptiveRouting]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerAdaptiveRoutingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerAdaptiveRoutingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerAdaptiveRoutingOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerAdaptiveRoutingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFailoverAcrossPools")
    def reset_failover_across_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailoverAcrossPools", []))

    @builtins.property
    @jsii.member(jsii_name="failoverAcrossPoolsInput")
    def failover_across_pools_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failoverAcrossPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverAcrossPools")
    def failover_across_pools(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failoverAcrossPools"))

    @failover_across_pools.setter
    def failover_across_pools(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerAdaptiveRoutingOutputReference, "failover_across_pools").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failoverAcrossPools", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerAdaptiveRouting, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerAdaptiveRouting, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerAdaptiveRouting, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerAdaptiveRoutingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_pool_ids": "defaultPoolIds",
        "fallback_pool_id": "fallbackPoolId",
        "name": "name",
        "zone_id": "zoneId",
        "adaptive_routing": "adaptiveRouting",
        "country_pools": "countryPools",
        "description": "description",
        "enabled": "enabled",
        "id": "id",
        "location_strategy": "locationStrategy",
        "pop_pools": "popPools",
        "proxied": "proxied",
        "random_steering": "randomSteering",
        "region_pools": "regionPools",
        "rules": "rules",
        "session_affinity": "sessionAffinity",
        "session_affinity_attributes": "sessionAffinityAttributes",
        "session_affinity_ttl": "sessionAffinityTtl",
        "steering_policy": "steeringPolicy",
        "ttl": "ttl",
    },
)
class LoadBalancerConfig(cdktf.TerraformMetaArguments):
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
        default_pool_ids: typing.Sequence[builtins.str],
        fallback_pool_id: builtins.str,
        name: builtins.str,
        zone_id: builtins.str,
        adaptive_routing: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadBalancerAdaptiveRouting, typing.Dict[str, typing.Any]]]]] = None,
        country_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerCountryPools", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        location_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerLocationStrategy", typing.Dict[str, typing.Any]]]]] = None,
        pop_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerPopPools", typing.Dict[str, typing.Any]]]]] = None,
        proxied: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        random_steering: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRandomSteering", typing.Dict[str, typing.Any]]]]] = None,
        region_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRegionPools", typing.Dict[str, typing.Any]]]]] = None,
        rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRules", typing.Dict[str, typing.Any]]]]] = None,
        session_affinity: typing.Optional[builtins.str] = None,
        session_affinity_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        session_affinity_ttl: typing.Optional[jsii.Number] = None,
        steering_policy: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_pool_ids LoadBalancer#default_pool_ids}.
        :param fallback_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#fallback_pool_id LoadBalancer#fallback_pool_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#name LoadBalancer#name}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#zone_id LoadBalancer#zone_id}
        :param adaptive_routing: adaptive_routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#adaptive_routing LoadBalancer#adaptive_routing}
        :param country_pools: country_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country_pools LoadBalancer#country_pools}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#description LoadBalancer#description}.
        :param enabled: Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#enabled LoadBalancer#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#id LoadBalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location_strategy: location_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location_strategy LoadBalancer#location_strategy}
        :param pop_pools: pop_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop_pools LoadBalancer#pop_pools}
        :param proxied: Defaults to ``false``. Conflicts with ``ttl``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#proxied LoadBalancer#proxied}
        :param random_steering: random_steering block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#random_steering LoadBalancer#random_steering}
        :param region_pools: region_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region_pools LoadBalancer#region_pools}
        :param rules: rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#rules LoadBalancer#rules}
        :param session_affinity: Defaults to ``none``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity LoadBalancer#session_affinity}
        :param session_affinity_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_attributes LoadBalancer#session_affinity_attributes}.
        :param session_affinity_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_ttl LoadBalancer#session_affinity_ttl}.
        :param steering_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#steering_policy LoadBalancer#steering_policy}.
        :param ttl: Conflicts with ``proxied``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#ttl LoadBalancer#ttl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_pool_ids", value=default_pool_ids, expected_type=type_hints["default_pool_ids"])
            check_type(argname="argument fallback_pool_id", value=fallback_pool_id, expected_type=type_hints["fallback_pool_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument adaptive_routing", value=adaptive_routing, expected_type=type_hints["adaptive_routing"])
            check_type(argname="argument country_pools", value=country_pools, expected_type=type_hints["country_pools"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location_strategy", value=location_strategy, expected_type=type_hints["location_strategy"])
            check_type(argname="argument pop_pools", value=pop_pools, expected_type=type_hints["pop_pools"])
            check_type(argname="argument proxied", value=proxied, expected_type=type_hints["proxied"])
            check_type(argname="argument random_steering", value=random_steering, expected_type=type_hints["random_steering"])
            check_type(argname="argument region_pools", value=region_pools, expected_type=type_hints["region_pools"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument session_affinity", value=session_affinity, expected_type=type_hints["session_affinity"])
            check_type(argname="argument session_affinity_attributes", value=session_affinity_attributes, expected_type=type_hints["session_affinity_attributes"])
            check_type(argname="argument session_affinity_ttl", value=session_affinity_ttl, expected_type=type_hints["session_affinity_ttl"])
            check_type(argname="argument steering_policy", value=steering_policy, expected_type=type_hints["steering_policy"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_pool_ids": default_pool_ids,
            "fallback_pool_id": fallback_pool_id,
            "name": name,
            "zone_id": zone_id,
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
        if adaptive_routing is not None:
            self._values["adaptive_routing"] = adaptive_routing
        if country_pools is not None:
            self._values["country_pools"] = country_pools
        if description is not None:
            self._values["description"] = description
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if location_strategy is not None:
            self._values["location_strategy"] = location_strategy
        if pop_pools is not None:
            self._values["pop_pools"] = pop_pools
        if proxied is not None:
            self._values["proxied"] = proxied
        if random_steering is not None:
            self._values["random_steering"] = random_steering
        if region_pools is not None:
            self._values["region_pools"] = region_pools
        if rules is not None:
            self._values["rules"] = rules
        if session_affinity is not None:
            self._values["session_affinity"] = session_affinity
        if session_affinity_attributes is not None:
            self._values["session_affinity_attributes"] = session_affinity_attributes
        if session_affinity_ttl is not None:
            self._values["session_affinity_ttl"] = session_affinity_ttl
        if steering_policy is not None:
            self._values["steering_policy"] = steering_policy
        if ttl is not None:
            self._values["ttl"] = ttl

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
    def default_pool_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_pool_ids LoadBalancer#default_pool_ids}.'''
        result = self._values.get("default_pool_ids")
        assert result is not None, "Required property 'default_pool_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def fallback_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#fallback_pool_id LoadBalancer#fallback_pool_id}.'''
        result = self._values.get("fallback_pool_id")
        assert result is not None, "Required property 'fallback_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#name LoadBalancer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#zone_id LoadBalancer#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def adaptive_routing(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerAdaptiveRouting]]]:
        '''adaptive_routing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#adaptive_routing LoadBalancer#adaptive_routing}
        '''
        result = self._values.get("adaptive_routing")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerAdaptiveRouting]]], result)

    @builtins.property
    def country_pools(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerCountryPools"]]]:
        '''country_pools block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country_pools LoadBalancer#country_pools}
        '''
        result = self._values.get("country_pools")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerCountryPools"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#description LoadBalancer#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#enabled LoadBalancer#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#id LoadBalancer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerLocationStrategy"]]]:
        '''location_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location_strategy LoadBalancer#location_strategy}
        '''
        result = self._values.get("location_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerLocationStrategy"]]], result)

    @builtins.property
    def pop_pools(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPopPools"]]]:
        '''pop_pools block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop_pools LoadBalancer#pop_pools}
        '''
        result = self._values.get("pop_pools")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerPopPools"]]], result)

    @builtins.property
    def proxied(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``. Conflicts with ``ttl``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#proxied LoadBalancer#proxied}
        '''
        result = self._values.get("proxied")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def random_steering(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRandomSteering"]]]:
        '''random_steering block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#random_steering LoadBalancer#random_steering}
        '''
        result = self._values.get("random_steering")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRandomSteering"]]], result)

    @builtins.property
    def region_pools(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRegionPools"]]]:
        '''region_pools block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region_pools LoadBalancer#region_pools}
        '''
        result = self._values.get("region_pools")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRegionPools"]]], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRules"]]]:
        '''rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#rules LoadBalancer#rules}
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRules"]]], result)

    @builtins.property
    def session_affinity(self) -> typing.Optional[builtins.str]:
        '''Defaults to ``none``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity LoadBalancer#session_affinity}
        '''
        result = self._values.get("session_affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_affinity_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_attributes LoadBalancer#session_affinity_attributes}.'''
        result = self._values.get("session_affinity_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def session_affinity_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_ttl LoadBalancer#session_affinity_ttl}.'''
        result = self._values.get("session_affinity_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def steering_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#steering_policy LoadBalancer#steering_policy}.'''
        result = self._values.get("steering_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Conflicts with ``proxied``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#ttl LoadBalancer#ttl}
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerCountryPools",
    jsii_struct_bases=[],
    name_mapping={"country": "country", "pool_ids": "poolIds"},
)
class LoadBalancerCountryPools:
    def __init__(
        self,
        *,
        country: builtins.str,
        pool_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country LoadBalancer#country}.
        :param pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerCountryPools.__init__)
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument pool_ids", value=pool_ids, expected_type=type_hints["pool_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "country": country,
            "pool_ids": pool_ids,
        }

    @builtins.property
    def country(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country LoadBalancer#country}.'''
        result = self._values.get("country")
        assert result is not None, "Required property 'country' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pool_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.'''
        result = self._values.get("pool_ids")
        assert result is not None, "Required property 'pool_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerCountryPools(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerCountryPoolsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerCountryPoolsList",
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
            type_hints = typing.get_type_hints(LoadBalancerCountryPoolsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerCountryPoolsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerCountryPoolsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerCountryPoolsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerCountryPoolsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerCountryPoolsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerCountryPoolsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerCountryPools]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerCountryPools]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerCountryPools]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerCountryPoolsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerCountryPoolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerCountryPoolsOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerCountryPoolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIdsInput")
    def pool_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerCountryPoolsOutputReference, "country").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="poolIds")
    def pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolIds"))

    @pool_ids.setter
    def pool_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerCountryPoolsOutputReference, "pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerCountryPools, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerCountryPools, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerCountryPools, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerCountryPoolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerLocationStrategy",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "prefer_ecs": "preferEcs"},
)
class LoadBalancerLocationStrategy:
    def __init__(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        prefer_ecs: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#mode LoadBalancer#mode}.
        :param prefer_ecs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#prefer_ecs LoadBalancer#prefer_ecs}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerLocationStrategy.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument prefer_ecs", value=prefer_ecs, expected_type=type_hints["prefer_ecs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if prefer_ecs is not None:
            self._values["prefer_ecs"] = prefer_ecs

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#mode LoadBalancer#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefer_ecs(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#prefer_ecs LoadBalancer#prefer_ecs}.'''
        result = self._values.get("prefer_ecs")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerLocationStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerLocationStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerLocationStrategyList",
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
            type_hints = typing.get_type_hints(LoadBalancerLocationStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerLocationStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerLocationStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerLocationStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerLocationStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerLocationStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerLocationStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerLocationStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerLocationStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerLocationStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerLocationStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerLocationStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerLocationStrategyOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerLocationStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetPreferEcs")
    def reset_prefer_ecs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferEcs", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="preferEcsInput")
    def prefer_ecs_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferEcsInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerLocationStrategyOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="preferEcs")
    def prefer_ecs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferEcs"))

    @prefer_ecs.setter
    def prefer_ecs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerLocationStrategyOutputReference, "prefer_ecs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferEcs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerLocationStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerLocationStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerLocationStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerLocationStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerPopPools",
    jsii_struct_bases=[],
    name_mapping={"pool_ids": "poolIds", "pop": "pop"},
)
class LoadBalancerPopPools:
    def __init__(
        self,
        *,
        pool_ids: typing.Sequence[builtins.str],
        pop: builtins.str,
    ) -> None:
        '''
        :param pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.
        :param pop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop LoadBalancer#pop}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPopPools.__init__)
            check_type(argname="argument pool_ids", value=pool_ids, expected_type=type_hints["pool_ids"])
            check_type(argname="argument pop", value=pop, expected_type=type_hints["pop"])
        self._values: typing.Dict[str, typing.Any] = {
            "pool_ids": pool_ids,
            "pop": pop,
        }

    @builtins.property
    def pool_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.'''
        result = self._values.get("pool_ids")
        assert result is not None, "Required property 'pool_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def pop(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop LoadBalancer#pop}.'''
        result = self._values.get("pop")
        assert result is not None, "Required property 'pop' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerPopPools(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerPopPoolsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerPopPoolsList",
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
            type_hints = typing.get_type_hints(LoadBalancerPopPoolsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerPopPoolsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerPopPoolsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerPopPoolsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPopPoolsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPopPoolsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerPopPoolsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPopPools]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPopPools]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerPopPools]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPopPoolsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerPopPoolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerPopPoolsOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerPopPoolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="poolIdsInput")
    def pool_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="popInput")
    def pop_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "popInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIds")
    def pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolIds"))

    @pool_ids.setter
    def pool_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPopPoolsOutputReference, "pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolIds", value)

    @builtins.property
    @jsii.member(jsii_name="pop")
    def pop(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pop"))

    @pop.setter
    def pop(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPopPoolsOutputReference, "pop").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pop", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerPopPools, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerPopPools, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerPopPools, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerPopPoolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRandomSteering",
    jsii_struct_bases=[],
    name_mapping={"default_weight": "defaultWeight", "pool_weights": "poolWeights"},
)
class LoadBalancerRandomSteering:
    def __init__(
        self,
        *,
        default_weight: typing.Optional[jsii.Number] = None,
        pool_weights: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param default_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_weight LoadBalancer#default_weight}.
        :param pool_weights: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_weights LoadBalancer#pool_weights}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRandomSteering.__init__)
            check_type(argname="argument default_weight", value=default_weight, expected_type=type_hints["default_weight"])
            check_type(argname="argument pool_weights", value=pool_weights, expected_type=type_hints["pool_weights"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_weight is not None:
            self._values["default_weight"] = default_weight
        if pool_weights is not None:
            self._values["pool_weights"] = pool_weights

    @builtins.property
    def default_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_weight LoadBalancer#default_weight}.'''
        result = self._values.get("default_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pool_weights(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_weights LoadBalancer#pool_weights}.'''
        result = self._values.get("pool_weights")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRandomSteering(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRandomSteeringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRandomSteeringList",
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
            type_hints = typing.get_type_hints(LoadBalancerRandomSteeringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerRandomSteeringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRandomSteeringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRandomSteeringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRandomSteeringList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRandomSteeringList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRandomSteeringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRandomSteering]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRandomSteering]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRandomSteering]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRandomSteeringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRandomSteeringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRandomSteeringOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRandomSteeringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDefaultWeight")
    def reset_default_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultWeight", []))

    @jsii.member(jsii_name="resetPoolWeights")
    def reset_pool_weights(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoolWeights", []))

    @builtins.property
    @jsii.member(jsii_name="defaultWeightInput")
    def default_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="poolWeightsInput")
    def pool_weights_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], jsii.get(self, "poolWeightsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultWeight")
    def default_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultWeight"))

    @default_weight.setter
    def default_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRandomSteeringOutputReference, "default_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultWeight", value)

    @builtins.property
    @jsii.member(jsii_name="poolWeights")
    def pool_weights(self) -> typing.Mapping[builtins.str, jsii.Number]:
        return typing.cast(typing.Mapping[builtins.str, jsii.Number], jsii.get(self, "poolWeights"))

    @pool_weights.setter
    def pool_weights(self, value: typing.Mapping[builtins.str, jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRandomSteeringOutputReference, "pool_weights").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolWeights", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRandomSteering, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRandomSteering, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRandomSteering, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRandomSteeringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRegionPools",
    jsii_struct_bases=[],
    name_mapping={"pool_ids": "poolIds", "region": "region"},
)
class LoadBalancerRegionPools:
    def __init__(
        self,
        *,
        pool_ids: typing.Sequence[builtins.str],
        region: builtins.str,
    ) -> None:
        '''
        :param pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region LoadBalancer#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRegionPools.__init__)
            check_type(argname="argument pool_ids", value=pool_ids, expected_type=type_hints["pool_ids"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "pool_ids": pool_ids,
            "region": region,
        }

    @builtins.property
    def pool_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.'''
        result = self._values.get("pool_ids")
        assert result is not None, "Required property 'pool_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region LoadBalancer#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRegionPools(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRegionPoolsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRegionPoolsList",
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
            type_hints = typing.get_type_hints(LoadBalancerRegionPoolsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerRegionPoolsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRegionPoolsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRegionPoolsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRegionPoolsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRegionPoolsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRegionPoolsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRegionPools]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRegionPools]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRegionPools]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRegionPoolsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRegionPoolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRegionPoolsOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRegionPoolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="poolIdsInput")
    def pool_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIds")
    def pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolIds"))

    @pool_ids.setter
    def pool_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRegionPoolsOutputReference, "pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolIds", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRegionPoolsOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRegionPools, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRegionPools, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRegionPools, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRegionPoolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRules",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "condition": "condition",
        "disabled": "disabled",
        "fixed_response": "fixedResponse",
        "overrides": "overrides",
        "priority": "priority",
        "terminates": "terminates",
    },
)
class LoadBalancerRules:
    def __init__(
        self,
        *,
        name: builtins.str,
        condition: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fixed_response: typing.Optional[typing.Union["LoadBalancerRulesFixedResponse", typing.Dict[str, typing.Any]]] = None,
        overrides: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverrides", typing.Dict[str, typing.Any]]]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        terminates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#name LoadBalancer#name}.
        :param condition: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#condition LoadBalancer#condition}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#disabled LoadBalancer#disabled}.
        :param fixed_response: fixed_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#fixed_response LoadBalancer#fixed_response}
        :param overrides: overrides block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#overrides LoadBalancer#overrides}
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#priority LoadBalancer#priority}.
        :param terminates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#terminates LoadBalancer#terminates}.
        '''
        if isinstance(fixed_response, dict):
            fixed_response = LoadBalancerRulesFixedResponse(**fixed_response)
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRules.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument fixed_response", value=fixed_response, expected_type=type_hints["fixed_response"])
            check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument terminates", value=terminates, expected_type=type_hints["terminates"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if condition is not None:
            self._values["condition"] = condition
        if disabled is not None:
            self._values["disabled"] = disabled
        if fixed_response is not None:
            self._values["fixed_response"] = fixed_response
        if overrides is not None:
            self._values["overrides"] = overrides
        if priority is not None:
            self._values["priority"] = priority
        if terminates is not None:
            self._values["terminates"] = terminates

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#name LoadBalancer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#condition LoadBalancer#condition}.'''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#disabled LoadBalancer#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fixed_response(self) -> typing.Optional["LoadBalancerRulesFixedResponse"]:
        '''fixed_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#fixed_response LoadBalancer#fixed_response}
        '''
        result = self._values.get("fixed_response")
        return typing.cast(typing.Optional["LoadBalancerRulesFixedResponse"], result)

    @builtins.property
    def overrides(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverrides"]]]:
        '''overrides block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#overrides LoadBalancer#overrides}
        '''
        result = self._values.get("overrides")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverrides"]]], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#priority LoadBalancer#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def terminates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#terminates LoadBalancer#terminates}.'''
        result = self._values.get("terminates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesFixedResponse",
    jsii_struct_bases=[],
    name_mapping={
        "content_type": "contentType",
        "location": "location",
        "message_body": "messageBody",
        "status_code": "statusCode",
    },
)
class LoadBalancerRulesFixedResponse:
    def __init__(
        self,
        *,
        content_type: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        message_body: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#content_type LoadBalancer#content_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location LoadBalancer#location}.
        :param message_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#message_body LoadBalancer#message_body}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#status_code LoadBalancer#status_code}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesFixedResponse.__init__)
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument message_body", value=message_body, expected_type=type_hints["message_body"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[str, typing.Any] = {}
        if content_type is not None:
            self._values["content_type"] = content_type
        if location is not None:
            self._values["location"] = location
        if message_body is not None:
            self._values["message_body"] = message_body
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#content_type LoadBalancer#content_type}.'''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location LoadBalancer#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_body(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#message_body LoadBalancer#message_body}.'''
        result = self._values.get("message_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status_code(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#status_code LoadBalancer#status_code}.'''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesFixedResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRulesFixedResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesFixedResponseOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesFixedResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContentType")
    def reset_content_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContentType", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetMessageBody")
    def reset_message_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageBody", []))

    @jsii.member(jsii_name="resetStatusCode")
    def reset_status_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusCode", []))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="messageBodyInput")
    def message_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="statusCodeInput")
    def status_code_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "statusCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesFixedResponseOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesFixedResponseOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="messageBody")
    def message_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageBody"))

    @message_body.setter
    def message_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesFixedResponseOutputReference, "message_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageBody", value)

    @builtins.property
    @jsii.member(jsii_name="statusCode")
    def status_code(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "statusCode"))

    @status_code.setter
    def status_code(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesFixedResponseOutputReference, "status_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusCode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadBalancerRulesFixedResponse]:
        return typing.cast(typing.Optional[LoadBalancerRulesFixedResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoadBalancerRulesFixedResponse],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesFixedResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFixedResponse")
    def put_fixed_response(
        self,
        *,
        content_type: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        message_body: typing.Optional[builtins.str] = None,
        status_code: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#content_type LoadBalancer#content_type}.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location LoadBalancer#location}.
        :param message_body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#message_body LoadBalancer#message_body}.
        :param status_code: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#status_code LoadBalancer#status_code}.
        '''
        value = LoadBalancerRulesFixedResponse(
            content_type=content_type,
            location=location,
            message_body=message_body,
            status_code=status_code,
        )

        return typing.cast(None, jsii.invoke(self, "putFixedResponse", [value]))

    @jsii.member(jsii_name="putOverrides")
    def put_overrides(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverrides", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOutputReference.put_overrides)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOverrides", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetFixedResponse")
    def reset_fixed_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedResponse", []))

    @jsii.member(jsii_name="resetOverrides")
    def reset_overrides(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrides", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetTerminates")
    def reset_terminates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminates", []))

    @builtins.property
    @jsii.member(jsii_name="fixedResponse")
    def fixed_response(self) -> LoadBalancerRulesFixedResponseOutputReference:
        return typing.cast(LoadBalancerRulesFixedResponseOutputReference, jsii.get(self, "fixedResponse"))

    @builtins.property
    @jsii.member(jsii_name="overrides")
    def overrides(self) -> "LoadBalancerRulesOverridesList":
        return typing.cast("LoadBalancerRulesOverridesList", jsii.get(self, "overrides"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="fixedResponseInput")
    def fixed_response_input(self) -> typing.Optional[LoadBalancerRulesFixedResponse]:
        return typing.cast(typing.Optional[LoadBalancerRulesFixedResponse], jsii.get(self, "fixedResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="overridesInput")
    def overrides_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverrides"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverrides"]]], jsii.get(self, "overridesInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="terminatesInput")
    def terminates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "terminatesInput"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOutputReference, "condition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="terminates")
    def terminates(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "terminates"))

    @terminates.setter
    def terminates(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOutputReference, "terminates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminates", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverrides",
    jsii_struct_bases=[],
    name_mapping={
        "adaptive_routing": "adaptiveRouting",
        "country_pools": "countryPools",
        "default_pools": "defaultPools",
        "fallback_pool": "fallbackPool",
        "location_strategy": "locationStrategy",
        "pop_pools": "popPools",
        "random_steering": "randomSteering",
        "region_pools": "regionPools",
        "session_affinity": "sessionAffinity",
        "session_affinity_attributes": "sessionAffinityAttributes",
        "session_affinity_ttl": "sessionAffinityTtl",
        "steering_policy": "steeringPolicy",
        "ttl": "ttl",
    },
)
class LoadBalancerRulesOverrides:
    def __init__(
        self,
        *,
        adaptive_routing: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesAdaptiveRouting", typing.Dict[str, typing.Any]]]]] = None,
        country_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesCountryPools", typing.Dict[str, typing.Any]]]]] = None,
        default_pools: typing.Optional[typing.Sequence[builtins.str]] = None,
        fallback_pool: typing.Optional[builtins.str] = None,
        location_strategy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesLocationStrategy", typing.Dict[str, typing.Any]]]]] = None,
        pop_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesPopPools", typing.Dict[str, typing.Any]]]]] = None,
        random_steering: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesRandomSteering", typing.Dict[str, typing.Any]]]]] = None,
        region_pools: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesRegionPools", typing.Dict[str, typing.Any]]]]] = None,
        session_affinity: typing.Optional[builtins.str] = None,
        session_affinity_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        session_affinity_ttl: typing.Optional[jsii.Number] = None,
        steering_policy: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param adaptive_routing: adaptive_routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#adaptive_routing LoadBalancer#adaptive_routing}
        :param country_pools: country_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country_pools LoadBalancer#country_pools}
        :param default_pools: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_pools LoadBalancer#default_pools}.
        :param fallback_pool: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#fallback_pool LoadBalancer#fallback_pool}.
        :param location_strategy: location_strategy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location_strategy LoadBalancer#location_strategy}
        :param pop_pools: pop_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop_pools LoadBalancer#pop_pools}
        :param random_steering: random_steering block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#random_steering LoadBalancer#random_steering}
        :param region_pools: region_pools block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region_pools LoadBalancer#region_pools}
        :param session_affinity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity LoadBalancer#session_affinity}.
        :param session_affinity_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_attributes LoadBalancer#session_affinity_attributes}.
        :param session_affinity_ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_ttl LoadBalancer#session_affinity_ttl}.
        :param steering_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#steering_policy LoadBalancer#steering_policy}.
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#ttl LoadBalancer#ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverrides.__init__)
            check_type(argname="argument adaptive_routing", value=adaptive_routing, expected_type=type_hints["adaptive_routing"])
            check_type(argname="argument country_pools", value=country_pools, expected_type=type_hints["country_pools"])
            check_type(argname="argument default_pools", value=default_pools, expected_type=type_hints["default_pools"])
            check_type(argname="argument fallback_pool", value=fallback_pool, expected_type=type_hints["fallback_pool"])
            check_type(argname="argument location_strategy", value=location_strategy, expected_type=type_hints["location_strategy"])
            check_type(argname="argument pop_pools", value=pop_pools, expected_type=type_hints["pop_pools"])
            check_type(argname="argument random_steering", value=random_steering, expected_type=type_hints["random_steering"])
            check_type(argname="argument region_pools", value=region_pools, expected_type=type_hints["region_pools"])
            check_type(argname="argument session_affinity", value=session_affinity, expected_type=type_hints["session_affinity"])
            check_type(argname="argument session_affinity_attributes", value=session_affinity_attributes, expected_type=type_hints["session_affinity_attributes"])
            check_type(argname="argument session_affinity_ttl", value=session_affinity_ttl, expected_type=type_hints["session_affinity_ttl"])
            check_type(argname="argument steering_policy", value=steering_policy, expected_type=type_hints["steering_policy"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if adaptive_routing is not None:
            self._values["adaptive_routing"] = adaptive_routing
        if country_pools is not None:
            self._values["country_pools"] = country_pools
        if default_pools is not None:
            self._values["default_pools"] = default_pools
        if fallback_pool is not None:
            self._values["fallback_pool"] = fallback_pool
        if location_strategy is not None:
            self._values["location_strategy"] = location_strategy
        if pop_pools is not None:
            self._values["pop_pools"] = pop_pools
        if random_steering is not None:
            self._values["random_steering"] = random_steering
        if region_pools is not None:
            self._values["region_pools"] = region_pools
        if session_affinity is not None:
            self._values["session_affinity"] = session_affinity
        if session_affinity_attributes is not None:
            self._values["session_affinity_attributes"] = session_affinity_attributes
        if session_affinity_ttl is not None:
            self._values["session_affinity_ttl"] = session_affinity_ttl
        if steering_policy is not None:
            self._values["steering_policy"] = steering_policy
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def adaptive_routing(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesAdaptiveRouting"]]]:
        '''adaptive_routing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#adaptive_routing LoadBalancer#adaptive_routing}
        '''
        result = self._values.get("adaptive_routing")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesAdaptiveRouting"]]], result)

    @builtins.property
    def country_pools(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesCountryPools"]]]:
        '''country_pools block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country_pools LoadBalancer#country_pools}
        '''
        result = self._values.get("country_pools")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesCountryPools"]]], result)

    @builtins.property
    def default_pools(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_pools LoadBalancer#default_pools}.'''
        result = self._values.get("default_pools")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fallback_pool(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#fallback_pool LoadBalancer#fallback_pool}.'''
        result = self._values.get("fallback_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location_strategy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesLocationStrategy"]]]:
        '''location_strategy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#location_strategy LoadBalancer#location_strategy}
        '''
        result = self._values.get("location_strategy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesLocationStrategy"]]], result)

    @builtins.property
    def pop_pools(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesPopPools"]]]:
        '''pop_pools block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop_pools LoadBalancer#pop_pools}
        '''
        result = self._values.get("pop_pools")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesPopPools"]]], result)

    @builtins.property
    def random_steering(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRandomSteering"]]]:
        '''random_steering block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#random_steering LoadBalancer#random_steering}
        '''
        result = self._values.get("random_steering")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRandomSteering"]]], result)

    @builtins.property
    def region_pools(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRegionPools"]]]:
        '''region_pools block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region_pools LoadBalancer#region_pools}
        '''
        result = self._values.get("region_pools")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRegionPools"]]], result)

    @builtins.property
    def session_affinity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity LoadBalancer#session_affinity}.'''
        result = self._values.get("session_affinity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_affinity_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_attributes LoadBalancer#session_affinity_attributes}.'''
        result = self._values.get("session_affinity_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def session_affinity_ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#session_affinity_ttl LoadBalancer#session_affinity_ttl}.'''
        result = self._values.get("session_affinity_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def steering_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#steering_policy LoadBalancer#steering_policy}.'''
        result = self._values.get("steering_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#ttl LoadBalancer#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesOverrides(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesAdaptiveRouting",
    jsii_struct_bases=[],
    name_mapping={"failover_across_pools": "failoverAcrossPools"},
)
class LoadBalancerRulesOverridesAdaptiveRouting:
    def __init__(
        self,
        *,
        failover_across_pools: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param failover_across_pools: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#failover_across_pools LoadBalancer#failover_across_pools}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesAdaptiveRouting.__init__)
            check_type(argname="argument failover_across_pools", value=failover_across_pools, expected_type=type_hints["failover_across_pools"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failover_across_pools is not None:
            self._values["failover_across_pools"] = failover_across_pools

    @builtins.property
    def failover_across_pools(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#failover_across_pools LoadBalancer#failover_across_pools}.'''
        result = self._values.get("failover_across_pools")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesOverridesAdaptiveRouting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRulesOverridesAdaptiveRoutingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesAdaptiveRoutingList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesAdaptiveRoutingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadBalancerRulesOverridesAdaptiveRoutingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesAdaptiveRoutingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOverridesAdaptiveRoutingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesAdaptiveRoutingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesAdaptiveRoutingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesAdaptiveRoutingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesAdaptiveRouting]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesAdaptiveRouting]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesAdaptiveRouting]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesAdaptiveRoutingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesAdaptiveRoutingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesAdaptiveRoutingOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesAdaptiveRoutingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFailoverAcrossPools")
    def reset_failover_across_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailoverAcrossPools", []))

    @builtins.property
    @jsii.member(jsii_name="failoverAcrossPoolsInput")
    def failover_across_pools_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "failoverAcrossPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverAcrossPools")
    def failover_across_pools(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "failoverAcrossPools"))

    @failover_across_pools.setter
    def failover_across_pools(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesAdaptiveRoutingOutputReference, "failover_across_pools").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failoverAcrossPools", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRulesOverridesAdaptiveRouting, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRulesOverridesAdaptiveRouting, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRulesOverridesAdaptiveRouting, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesAdaptiveRoutingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesCountryPools",
    jsii_struct_bases=[],
    name_mapping={"country": "country", "pool_ids": "poolIds"},
)
class LoadBalancerRulesOverridesCountryPools:
    def __init__(
        self,
        *,
        country: builtins.str,
        pool_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param country: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country LoadBalancer#country}.
        :param pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesCountryPools.__init__)
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument pool_ids", value=pool_ids, expected_type=type_hints["pool_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "country": country,
            "pool_ids": pool_ids,
        }

    @builtins.property
    def country(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#country LoadBalancer#country}.'''
        result = self._values.get("country")
        assert result is not None, "Required property 'country' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pool_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.'''
        result = self._values.get("pool_ids")
        assert result is not None, "Required property 'pool_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesOverridesCountryPools(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRulesOverridesCountryPoolsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesCountryPoolsList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesCountryPoolsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadBalancerRulesOverridesCountryPoolsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesCountryPoolsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOverridesCountryPoolsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesCountryPoolsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesCountryPoolsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesCountryPoolsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesCountryPools]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesCountryPools]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesCountryPools]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesCountryPoolsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesCountryPoolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesCountryPoolsOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesCountryPoolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIdsInput")
    def pool_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesCountryPoolsOutputReference, "country").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value)

    @builtins.property
    @jsii.member(jsii_name="poolIds")
    def pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolIds"))

    @pool_ids.setter
    def pool_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesCountryPoolsOutputReference, "pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRulesOverridesCountryPools, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRulesOverridesCountryPools, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRulesOverridesCountryPools, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesCountryPoolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadBalancerRulesOverridesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOverridesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverrides]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverrides]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverrides]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesLocationStrategy",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "prefer_ecs": "preferEcs"},
)
class LoadBalancerRulesOverridesLocationStrategy:
    def __init__(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        prefer_ecs: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#mode LoadBalancer#mode}.
        :param prefer_ecs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#prefer_ecs LoadBalancer#prefer_ecs}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesLocationStrategy.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument prefer_ecs", value=prefer_ecs, expected_type=type_hints["prefer_ecs"])
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if prefer_ecs is not None:
            self._values["prefer_ecs"] = prefer_ecs

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#mode LoadBalancer#mode}.'''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefer_ecs(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#prefer_ecs LoadBalancer#prefer_ecs}.'''
        result = self._values.get("prefer_ecs")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesOverridesLocationStrategy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRulesOverridesLocationStrategyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesLocationStrategyList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesLocationStrategyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadBalancerRulesOverridesLocationStrategyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesLocationStrategyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOverridesLocationStrategyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesLocationStrategyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesLocationStrategyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesLocationStrategyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesLocationStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesLocationStrategy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesLocationStrategy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesLocationStrategyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesLocationStrategyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesLocationStrategyOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesLocationStrategyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetPreferEcs")
    def reset_prefer_ecs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreferEcs", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="preferEcsInput")
    def prefer_ecs_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferEcsInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesLocationStrategyOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="preferEcs")
    def prefer_ecs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "preferEcs"))

    @prefer_ecs.setter
    def prefer_ecs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesLocationStrategyOutputReference, "prefer_ecs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferEcs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRulesOverridesLocationStrategy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRulesOverridesLocationStrategy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRulesOverridesLocationStrategy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesLocationStrategyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAdaptiveRouting")
    def put_adaptive_routing(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadBalancerRulesOverridesAdaptiveRouting, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesOutputReference.put_adaptive_routing)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdaptiveRouting", [value]))

    @jsii.member(jsii_name="putCountryPools")
    def put_country_pools(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadBalancerRulesOverridesCountryPools, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesOutputReference.put_country_pools)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCountryPools", [value]))

    @jsii.member(jsii_name="putLocationStrategy")
    def put_location_strategy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LoadBalancerRulesOverridesLocationStrategy, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesOutputReference.put_location_strategy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLocationStrategy", [value]))

    @jsii.member(jsii_name="putPopPools")
    def put_pop_pools(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesPopPools", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesOutputReference.put_pop_pools)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPopPools", [value]))

    @jsii.member(jsii_name="putRandomSteering")
    def put_random_steering(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesRandomSteering", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesOutputReference.put_random_steering)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRandomSteering", [value]))

    @jsii.member(jsii_name="putRegionPools")
    def put_region_pools(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadBalancerRulesOverridesRegionPools", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesOutputReference.put_region_pools)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegionPools", [value]))

    @jsii.member(jsii_name="resetAdaptiveRouting")
    def reset_adaptive_routing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdaptiveRouting", []))

    @jsii.member(jsii_name="resetCountryPools")
    def reset_country_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountryPools", []))

    @jsii.member(jsii_name="resetDefaultPools")
    def reset_default_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultPools", []))

    @jsii.member(jsii_name="resetFallbackPool")
    def reset_fallback_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFallbackPool", []))

    @jsii.member(jsii_name="resetLocationStrategy")
    def reset_location_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocationStrategy", []))

    @jsii.member(jsii_name="resetPopPools")
    def reset_pop_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPopPools", []))

    @jsii.member(jsii_name="resetRandomSteering")
    def reset_random_steering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRandomSteering", []))

    @jsii.member(jsii_name="resetRegionPools")
    def reset_region_pools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionPools", []))

    @jsii.member(jsii_name="resetSessionAffinity")
    def reset_session_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinity", []))

    @jsii.member(jsii_name="resetSessionAffinityAttributes")
    def reset_session_affinity_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinityAttributes", []))

    @jsii.member(jsii_name="resetSessionAffinityTtl")
    def reset_session_affinity_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSessionAffinityTtl", []))

    @jsii.member(jsii_name="resetSteeringPolicy")
    def reset_steering_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSteeringPolicy", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="adaptiveRouting")
    def adaptive_routing(self) -> LoadBalancerRulesOverridesAdaptiveRoutingList:
        return typing.cast(LoadBalancerRulesOverridesAdaptiveRoutingList, jsii.get(self, "adaptiveRouting"))

    @builtins.property
    @jsii.member(jsii_name="countryPools")
    def country_pools(self) -> LoadBalancerRulesOverridesCountryPoolsList:
        return typing.cast(LoadBalancerRulesOverridesCountryPoolsList, jsii.get(self, "countryPools"))

    @builtins.property
    @jsii.member(jsii_name="locationStrategy")
    def location_strategy(self) -> LoadBalancerRulesOverridesLocationStrategyList:
        return typing.cast(LoadBalancerRulesOverridesLocationStrategyList, jsii.get(self, "locationStrategy"))

    @builtins.property
    @jsii.member(jsii_name="popPools")
    def pop_pools(self) -> "LoadBalancerRulesOverridesPopPoolsList":
        return typing.cast("LoadBalancerRulesOverridesPopPoolsList", jsii.get(self, "popPools"))

    @builtins.property
    @jsii.member(jsii_name="randomSteering")
    def random_steering(self) -> "LoadBalancerRulesOverridesRandomSteeringList":
        return typing.cast("LoadBalancerRulesOverridesRandomSteeringList", jsii.get(self, "randomSteering"))

    @builtins.property
    @jsii.member(jsii_name="regionPools")
    def region_pools(self) -> "LoadBalancerRulesOverridesRegionPoolsList":
        return typing.cast("LoadBalancerRulesOverridesRegionPoolsList", jsii.get(self, "regionPools"))

    @builtins.property
    @jsii.member(jsii_name="adaptiveRoutingInput")
    def adaptive_routing_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesAdaptiveRouting]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesAdaptiveRouting]]], jsii.get(self, "adaptiveRoutingInput"))

    @builtins.property
    @jsii.member(jsii_name="countryPoolsInput")
    def country_pools_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesCountryPools]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesCountryPools]]], jsii.get(self, "countryPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPoolsInput")
    def default_pools_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="fallbackPoolInput")
    def fallback_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fallbackPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="locationStrategyInput")
    def location_strategy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesLocationStrategy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesLocationStrategy]]], jsii.get(self, "locationStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="popPoolsInput")
    def pop_pools_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesPopPools"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesPopPools"]]], jsii.get(self, "popPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="randomSteeringInput")
    def random_steering_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRandomSteering"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRandomSteering"]]], jsii.get(self, "randomSteeringInput"))

    @builtins.property
    @jsii.member(jsii_name="regionPoolsInput")
    def region_pools_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRegionPools"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadBalancerRulesOverridesRegionPools"]]], jsii.get(self, "regionPoolsInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityAttributesInput")
    def session_affinity_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sessionAffinityAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityInput")
    def session_affinity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityTtlInput")
    def session_affinity_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sessionAffinityTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="steeringPolicyInput")
    def steering_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "steeringPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultPools")
    def default_pools(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultPools"))

    @default_pools.setter
    def default_pools(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "default_pools").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPools", value)

    @builtins.property
    @jsii.member(jsii_name="fallbackPool")
    def fallback_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fallbackPool"))

    @fallback_pool.setter
    def fallback_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "fallback_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackPool", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinity")
    def session_affinity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionAffinity"))

    @session_affinity.setter
    def session_affinity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "session_affinity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinity", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityAttributes")
    def session_affinity_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sessionAffinityAttributes"))

    @session_affinity_attributes.setter
    def session_affinity_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "session_affinity_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinityAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="sessionAffinityTtl")
    def session_affinity_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sessionAffinityTtl"))

    @session_affinity_ttl.setter
    def session_affinity_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "session_affinity_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionAffinityTtl", value)

    @builtins.property
    @jsii.member(jsii_name="steeringPolicy")
    def steering_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "steeringPolicy"))

    @steering_policy.setter
    def steering_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "steering_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "steeringPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRulesOverrides, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRulesOverrides, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRulesOverrides, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesPopPools",
    jsii_struct_bases=[],
    name_mapping={"pool_ids": "poolIds", "pop": "pop"},
)
class LoadBalancerRulesOverridesPopPools:
    def __init__(
        self,
        *,
        pool_ids: typing.Sequence[builtins.str],
        pop: builtins.str,
    ) -> None:
        '''
        :param pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.
        :param pop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop LoadBalancer#pop}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesPopPools.__init__)
            check_type(argname="argument pool_ids", value=pool_ids, expected_type=type_hints["pool_ids"])
            check_type(argname="argument pop", value=pop, expected_type=type_hints["pop"])
        self._values: typing.Dict[str, typing.Any] = {
            "pool_ids": pool_ids,
            "pop": pop,
        }

    @builtins.property
    def pool_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.'''
        result = self._values.get("pool_ids")
        assert result is not None, "Required property 'pool_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def pop(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pop LoadBalancer#pop}.'''
        result = self._values.get("pop")
        assert result is not None, "Required property 'pop' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesOverridesPopPools(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRulesOverridesPopPoolsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesPopPoolsList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesPopPoolsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadBalancerRulesOverridesPopPoolsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesPopPoolsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOverridesPopPoolsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesPopPoolsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesPopPoolsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesPopPoolsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesPopPools]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesPopPools]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesPopPools]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesPopPoolsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesPopPoolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesPopPoolsOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesPopPoolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="poolIdsInput")
    def pool_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="popInput")
    def pop_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "popInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIds")
    def pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolIds"))

    @pool_ids.setter
    def pool_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesPopPoolsOutputReference, "pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolIds", value)

    @builtins.property
    @jsii.member(jsii_name="pop")
    def pop(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pop"))

    @pop.setter
    def pop(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesPopPoolsOutputReference, "pop").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pop", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRulesOverridesPopPools, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRulesOverridesPopPools, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRulesOverridesPopPools, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesPopPoolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesRandomSteering",
    jsii_struct_bases=[],
    name_mapping={"default_weight": "defaultWeight", "pool_weights": "poolWeights"},
)
class LoadBalancerRulesOverridesRandomSteering:
    def __init__(
        self,
        *,
        default_weight: typing.Optional[jsii.Number] = None,
        pool_weights: typing.Optional[typing.Mapping[builtins.str, jsii.Number]] = None,
    ) -> None:
        '''
        :param default_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_weight LoadBalancer#default_weight}.
        :param pool_weights: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_weights LoadBalancer#pool_weights}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRandomSteering.__init__)
            check_type(argname="argument default_weight", value=default_weight, expected_type=type_hints["default_weight"])
            check_type(argname="argument pool_weights", value=pool_weights, expected_type=type_hints["pool_weights"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_weight is not None:
            self._values["default_weight"] = default_weight
        if pool_weights is not None:
            self._values["pool_weights"] = pool_weights

    @builtins.property
    def default_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#default_weight LoadBalancer#default_weight}.'''
        result = self._values.get("default_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pool_weights(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_weights LoadBalancer#pool_weights}.'''
        result = self._values.get("pool_weights")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesOverridesRandomSteering(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRulesOverridesRandomSteeringList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesRandomSteeringList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRandomSteeringList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadBalancerRulesOverridesRandomSteeringOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRandomSteeringList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOverridesRandomSteeringOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRandomSteeringList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRandomSteeringList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRandomSteeringList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesRandomSteering]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesRandomSteering]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesRandomSteering]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRandomSteeringList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesRandomSteeringOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesRandomSteeringOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRandomSteeringOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDefaultWeight")
    def reset_default_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultWeight", []))

    @jsii.member(jsii_name="resetPoolWeights")
    def reset_pool_weights(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPoolWeights", []))

    @builtins.property
    @jsii.member(jsii_name="defaultWeightInput")
    def default_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="poolWeightsInput")
    def pool_weights_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, jsii.Number]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, jsii.Number]], jsii.get(self, "poolWeightsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultWeight")
    def default_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultWeight"))

    @default_weight.setter
    def default_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRandomSteeringOutputReference, "default_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultWeight", value)

    @builtins.property
    @jsii.member(jsii_name="poolWeights")
    def pool_weights(self) -> typing.Mapping[builtins.str, jsii.Number]:
        return typing.cast(typing.Mapping[builtins.str, jsii.Number], jsii.get(self, "poolWeights"))

    @pool_weights.setter
    def pool_weights(self, value: typing.Mapping[builtins.str, jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRandomSteeringOutputReference, "pool_weights").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolWeights", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRulesOverridesRandomSteering, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRulesOverridesRandomSteering, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRulesOverridesRandomSteering, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRandomSteeringOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesRegionPools",
    jsii_struct_bases=[],
    name_mapping={"pool_ids": "poolIds", "region": "region"},
)
class LoadBalancerRulesOverridesRegionPools:
    def __init__(
        self,
        *,
        pool_ids: typing.Sequence[builtins.str],
        region: builtins.str,
    ) -> None:
        '''
        :param pool_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region LoadBalancer#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRegionPools.__init__)
            check_type(argname="argument pool_ids", value=pool_ids, expected_type=type_hints["pool_ids"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "pool_ids": pool_ids,
            "region": region,
        }

    @builtins.property
    def pool_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#pool_ids LoadBalancer#pool_ids}.'''
        result = self._values.get("pool_ids")
        assert result is not None, "Required property 'pool_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/load_balancer#region LoadBalancer#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerRulesOverridesRegionPools(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerRulesOverridesRegionPoolsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesRegionPoolsList",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRegionPoolsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "LoadBalancerRulesOverridesRegionPoolsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRegionPoolsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadBalancerRulesOverridesRegionPoolsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRegionPoolsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRegionPoolsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRegionPoolsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesRegionPools]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesRegionPools]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadBalancerRulesOverridesRegionPools]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRegionPoolsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadBalancerRulesOverridesRegionPoolsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.loadBalancer.LoadBalancerRulesOverridesRegionPoolsOutputReference",
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
            type_hints = typing.get_type_hints(LoadBalancerRulesOverridesRegionPoolsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="poolIdsInput")
    def pool_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "poolIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="poolIds")
    def pool_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "poolIds"))

    @pool_ids.setter
    def pool_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRegionPoolsOutputReference, "pool_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolIds", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRegionPoolsOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadBalancerRulesOverridesRegionPools, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadBalancerRulesOverridesRegionPools, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadBalancerRulesOverridesRegionPools, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadBalancerRulesOverridesRegionPoolsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LoadBalancer",
    "LoadBalancerAdaptiveRouting",
    "LoadBalancerAdaptiveRoutingList",
    "LoadBalancerAdaptiveRoutingOutputReference",
    "LoadBalancerConfig",
    "LoadBalancerCountryPools",
    "LoadBalancerCountryPoolsList",
    "LoadBalancerCountryPoolsOutputReference",
    "LoadBalancerLocationStrategy",
    "LoadBalancerLocationStrategyList",
    "LoadBalancerLocationStrategyOutputReference",
    "LoadBalancerPopPools",
    "LoadBalancerPopPoolsList",
    "LoadBalancerPopPoolsOutputReference",
    "LoadBalancerRandomSteering",
    "LoadBalancerRandomSteeringList",
    "LoadBalancerRandomSteeringOutputReference",
    "LoadBalancerRegionPools",
    "LoadBalancerRegionPoolsList",
    "LoadBalancerRegionPoolsOutputReference",
    "LoadBalancerRules",
    "LoadBalancerRulesFixedResponse",
    "LoadBalancerRulesFixedResponseOutputReference",
    "LoadBalancerRulesList",
    "LoadBalancerRulesOutputReference",
    "LoadBalancerRulesOverrides",
    "LoadBalancerRulesOverridesAdaptiveRouting",
    "LoadBalancerRulesOverridesAdaptiveRoutingList",
    "LoadBalancerRulesOverridesAdaptiveRoutingOutputReference",
    "LoadBalancerRulesOverridesCountryPools",
    "LoadBalancerRulesOverridesCountryPoolsList",
    "LoadBalancerRulesOverridesCountryPoolsOutputReference",
    "LoadBalancerRulesOverridesList",
    "LoadBalancerRulesOverridesLocationStrategy",
    "LoadBalancerRulesOverridesLocationStrategyList",
    "LoadBalancerRulesOverridesLocationStrategyOutputReference",
    "LoadBalancerRulesOverridesOutputReference",
    "LoadBalancerRulesOverridesPopPools",
    "LoadBalancerRulesOverridesPopPoolsList",
    "LoadBalancerRulesOverridesPopPoolsOutputReference",
    "LoadBalancerRulesOverridesRandomSteering",
    "LoadBalancerRulesOverridesRandomSteeringList",
    "LoadBalancerRulesOverridesRandomSteeringOutputReference",
    "LoadBalancerRulesOverridesRegionPools",
    "LoadBalancerRulesOverridesRegionPoolsList",
    "LoadBalancerRulesOverridesRegionPoolsOutputReference",
]

publication.publish()
