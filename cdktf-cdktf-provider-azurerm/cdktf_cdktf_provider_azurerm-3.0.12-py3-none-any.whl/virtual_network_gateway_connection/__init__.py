'''
# `azurerm_virtual_network_gateway_connection`

Refer to the Terraform Registory for docs: [`azurerm_virtual_network_gateway_connection`](https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection).
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


class VirtualNetworkGatewayConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection azurerm_virtual_network_gateway_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        type: builtins.str,
        virtual_network_gateway_id: builtins.str,
        authorization_key: typing.Optional[builtins.str] = None,
        connection_mode: typing.Optional[builtins.str] = None,
        connection_protocol: typing.Optional[builtins.str] = None,
        custom_bgp_addresses: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionCustomBgpAddresses", typing.Dict[str, typing.Any]]] = None,
        dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        egress_nat_rule_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        express_route_circuit_id: typing.Optional[builtins.str] = None,
        express_route_gateway_bypass: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress_nat_rule_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipsec_policy: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionIpsecPolicy", typing.Dict[str, typing.Any]]] = None,
        local_azure_ip_address_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        local_network_gateway_id: typing.Optional[builtins.str] = None,
        peer_virtual_network_gateway_id: typing.Optional[builtins.str] = None,
        routing_weight: typing.Optional[jsii.Number] = None,
        shared_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        traffic_selector_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayConnectionTrafficSelectorPolicy", typing.Dict[str, typing.Any]]]]] = None,
        use_policy_based_traffic_selectors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection azurerm_virtual_network_gateway_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#location VirtualNetworkGatewayConnection#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#name VirtualNetworkGatewayConnection#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#resource_group_name VirtualNetworkGatewayConnection#resource_group_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#type VirtualNetworkGatewayConnection#type}.
        :param virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#virtual_network_gateway_id VirtualNetworkGatewayConnection#virtual_network_gateway_id}.
        :param authorization_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#authorization_key VirtualNetworkGatewayConnection#authorization_key}.
        :param connection_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#connection_mode VirtualNetworkGatewayConnection#connection_mode}.
        :param connection_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#connection_protocol VirtualNetworkGatewayConnection#connection_protocol}.
        :param custom_bgp_addresses: custom_bgp_addresses block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#custom_bgp_addresses VirtualNetworkGatewayConnection#custom_bgp_addresses}
        :param dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#dpd_timeout_seconds VirtualNetworkGatewayConnection#dpd_timeout_seconds}.
        :param egress_nat_rule_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#egress_nat_rule_ids VirtualNetworkGatewayConnection#egress_nat_rule_ids}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#enable_bgp VirtualNetworkGatewayConnection#enable_bgp}.
        :param express_route_circuit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#express_route_circuit_id VirtualNetworkGatewayConnection#express_route_circuit_id}.
        :param express_route_gateway_bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#express_route_gateway_bypass VirtualNetworkGatewayConnection#express_route_gateway_bypass}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#id VirtualNetworkGatewayConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress_nat_rule_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ingress_nat_rule_ids VirtualNetworkGatewayConnection#ingress_nat_rule_ids}.
        :param ipsec_policy: ipsec_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_policy VirtualNetworkGatewayConnection#ipsec_policy}
        :param local_azure_ip_address_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_azure_ip_address_enabled VirtualNetworkGatewayConnection#local_azure_ip_address_enabled}.
        :param local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_network_gateway_id VirtualNetworkGatewayConnection#local_network_gateway_id}.
        :param peer_virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#peer_virtual_network_gateway_id VirtualNetworkGatewayConnection#peer_virtual_network_gateway_id}.
        :param routing_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#routing_weight VirtualNetworkGatewayConnection#routing_weight}.
        :param shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#shared_key VirtualNetworkGatewayConnection#shared_key}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#tags VirtualNetworkGatewayConnection#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#timeouts VirtualNetworkGatewayConnection#timeouts}
        :param traffic_selector_policy: traffic_selector_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#traffic_selector_policy VirtualNetworkGatewayConnection#traffic_selector_policy}
        :param use_policy_based_traffic_selectors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#use_policy_based_traffic_selectors VirtualNetworkGatewayConnection#use_policy_based_traffic_selectors}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualNetworkGatewayConnectionConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            type=type,
            virtual_network_gateway_id=virtual_network_gateway_id,
            authorization_key=authorization_key,
            connection_mode=connection_mode,
            connection_protocol=connection_protocol,
            custom_bgp_addresses=custom_bgp_addresses,
            dpd_timeout_seconds=dpd_timeout_seconds,
            egress_nat_rule_ids=egress_nat_rule_ids,
            enable_bgp=enable_bgp,
            express_route_circuit_id=express_route_circuit_id,
            express_route_gateway_bypass=express_route_gateway_bypass,
            id=id,
            ingress_nat_rule_ids=ingress_nat_rule_ids,
            ipsec_policy=ipsec_policy,
            local_azure_ip_address_enabled=local_azure_ip_address_enabled,
            local_network_gateway_id=local_network_gateway_id,
            peer_virtual_network_gateway_id=peer_virtual_network_gateway_id,
            routing_weight=routing_weight,
            shared_key=shared_key,
            tags=tags,
            timeouts=timeouts,
            traffic_selector_policy=traffic_selector_policy,
            use_policy_based_traffic_selectors=use_policy_based_traffic_selectors,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCustomBgpAddresses")
    def put_custom_bgp_addresses(
        self,
        *,
        primary: builtins.str,
        secondary: builtins.str,
    ) -> None:
        '''
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#primary VirtualNetworkGatewayConnection#primary}.
        :param secondary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#secondary VirtualNetworkGatewayConnection#secondary}.
        '''
        value = VirtualNetworkGatewayConnectionCustomBgpAddresses(
            primary=primary, secondary=secondary
        )

        return typing.cast(None, jsii.invoke(self, "putCustomBgpAddresses", [value]))

    @jsii.member(jsii_name="putIpsecPolicy")
    def put_ipsec_policy(
        self,
        *,
        dh_group: builtins.str,
        ike_encryption: builtins.str,
        ike_integrity: builtins.str,
        ipsec_encryption: builtins.str,
        ipsec_integrity: builtins.str,
        pfs_group: builtins.str,
        sa_datasize: typing.Optional[jsii.Number] = None,
        sa_lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#dh_group VirtualNetworkGatewayConnection#dh_group}.
        :param ike_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ike_encryption VirtualNetworkGatewayConnection#ike_encryption}.
        :param ike_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ike_integrity VirtualNetworkGatewayConnection#ike_integrity}.
        :param ipsec_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_encryption VirtualNetworkGatewayConnection#ipsec_encryption}.
        :param ipsec_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_integrity VirtualNetworkGatewayConnection#ipsec_integrity}.
        :param pfs_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#pfs_group VirtualNetworkGatewayConnection#pfs_group}.
        :param sa_datasize: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#sa_datasize VirtualNetworkGatewayConnection#sa_datasize}.
        :param sa_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#sa_lifetime VirtualNetworkGatewayConnection#sa_lifetime}.
        '''
        value = VirtualNetworkGatewayConnectionIpsecPolicy(
            dh_group=dh_group,
            ike_encryption=ike_encryption,
            ike_integrity=ike_integrity,
            ipsec_encryption=ipsec_encryption,
            ipsec_integrity=ipsec_integrity,
            pfs_group=pfs_group,
            sa_datasize=sa_datasize,
            sa_lifetime=sa_lifetime,
        )

        return typing.cast(None, jsii.invoke(self, "putIpsecPolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#create VirtualNetworkGatewayConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#delete VirtualNetworkGatewayConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#read VirtualNetworkGatewayConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#update VirtualNetworkGatewayConnection#update}.
        '''
        value = VirtualNetworkGatewayConnectionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTrafficSelectorPolicy")
    def put_traffic_selector_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayConnectionTrafficSelectorPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnection.put_traffic_selector_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrafficSelectorPolicy", [value]))

    @jsii.member(jsii_name="resetAuthorizationKey")
    def reset_authorization_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationKey", []))

    @jsii.member(jsii_name="resetConnectionMode")
    def reset_connection_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionMode", []))

    @jsii.member(jsii_name="resetConnectionProtocol")
    def reset_connection_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionProtocol", []))

    @jsii.member(jsii_name="resetCustomBgpAddresses")
    def reset_custom_bgp_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomBgpAddresses", []))

    @jsii.member(jsii_name="resetDpdTimeoutSeconds")
    def reset_dpd_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDpdTimeoutSeconds", []))

    @jsii.member(jsii_name="resetEgressNatRuleIds")
    def reset_egress_nat_rule_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressNatRuleIds", []))

    @jsii.member(jsii_name="resetEnableBgp")
    def reset_enable_bgp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBgp", []))

    @jsii.member(jsii_name="resetExpressRouteCircuitId")
    def reset_express_route_circuit_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpressRouteCircuitId", []))

    @jsii.member(jsii_name="resetExpressRouteGatewayBypass")
    def reset_express_route_gateway_bypass(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpressRouteGatewayBypass", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIngressNatRuleIds")
    def reset_ingress_nat_rule_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressNatRuleIds", []))

    @jsii.member(jsii_name="resetIpsecPolicy")
    def reset_ipsec_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpsecPolicy", []))

    @jsii.member(jsii_name="resetLocalAzureIpAddressEnabled")
    def reset_local_azure_ip_address_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAzureIpAddressEnabled", []))

    @jsii.member(jsii_name="resetLocalNetworkGatewayId")
    def reset_local_network_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalNetworkGatewayId", []))

    @jsii.member(jsii_name="resetPeerVirtualNetworkGatewayId")
    def reset_peer_virtual_network_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerVirtualNetworkGatewayId", []))

    @jsii.member(jsii_name="resetRoutingWeight")
    def reset_routing_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutingWeight", []))

    @jsii.member(jsii_name="resetSharedKey")
    def reset_shared_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedKey", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrafficSelectorPolicy")
    def reset_traffic_selector_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficSelectorPolicy", []))

    @jsii.member(jsii_name="resetUsePolicyBasedTrafficSelectors")
    def reset_use_policy_based_traffic_selectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsePolicyBasedTrafficSelectors", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customBgpAddresses")
    def custom_bgp_addresses(
        self,
    ) -> "VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference":
        return typing.cast("VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference", jsii.get(self, "customBgpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicy")
    def ipsec_policy(
        self,
    ) -> "VirtualNetworkGatewayConnectionIpsecPolicyOutputReference":
        return typing.cast("VirtualNetworkGatewayConnectionIpsecPolicyOutputReference", jsii.get(self, "ipsecPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualNetworkGatewayConnectionTimeoutsOutputReference":
        return typing.cast("VirtualNetworkGatewayConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="trafficSelectorPolicy")
    def traffic_selector_policy(
        self,
    ) -> "VirtualNetworkGatewayConnectionTrafficSelectorPolicyList":
        return typing.cast("VirtualNetworkGatewayConnectionTrafficSelectorPolicyList", jsii.get(self, "trafficSelectorPolicy"))

    @builtins.property
    @jsii.member(jsii_name="authorizationKeyInput")
    def authorization_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionModeInput")
    def connection_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionProtocolInput")
    def connection_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="customBgpAddressesInput")
    def custom_bgp_addresses_input(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayConnectionCustomBgpAddresses"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionCustomBgpAddresses"], jsii.get(self, "customBgpAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="dpdTimeoutSecondsInput")
    def dpd_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dpdTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="egressNatRuleIdsInput")
    def egress_nat_rule_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "egressNatRuleIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBgpInput")
    def enable_bgp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBgpInput"))

    @builtins.property
    @jsii.member(jsii_name="expressRouteCircuitIdInput")
    def express_route_circuit_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressRouteCircuitIdInput"))

    @builtins.property
    @jsii.member(jsii_name="expressRouteGatewayBypassInput")
    def express_route_gateway_bypass_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "expressRouteGatewayBypassInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressNatRuleIdsInput")
    def ingress_nat_rule_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ingressNatRuleIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicyInput")
    def ipsec_policy_input(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"], jsii.get(self, "ipsecPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="localAzureIpAddressEnabledInput")
    def local_azure_ip_address_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAzureIpAddressEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="localNetworkGatewayIdInput")
    def local_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="peerVirtualNetworkGatewayIdInput")
    def peer_virtual_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVirtualNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="routingWeightInput")
    def routing_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "routingWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedKeyInput")
    def shared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficSelectorPolicyInput")
    def traffic_selector_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayConnectionTrafficSelectorPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayConnectionTrafficSelectorPolicy"]]], jsii.get(self, "trafficSelectorPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usePolicyBasedTrafficSelectorsInput")
    def use_policy_based_traffic_selectors_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "usePolicyBasedTrafficSelectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkGatewayIdInput")
    def virtual_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationKey")
    def authorization_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationKey"))

    @authorization_key.setter
    def authorization_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "authorization_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationKey", value)

    @builtins.property
    @jsii.member(jsii_name="connectionMode")
    def connection_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionMode"))

    @connection_mode.setter
    def connection_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "connection_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionMode", value)

    @builtins.property
    @jsii.member(jsii_name="connectionProtocol")
    def connection_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionProtocol"))

    @connection_protocol.setter
    def connection_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "connection_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="dpdTimeoutSeconds")
    def dpd_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dpdTimeoutSeconds"))

    @dpd_timeout_seconds.setter
    def dpd_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "dpd_timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dpdTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="egressNatRuleIds")
    def egress_nat_rule_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "egressNatRuleIds"))

    @egress_nat_rule_ids.setter
    def egress_nat_rule_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "egress_nat_rule_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressNatRuleIds", value)

    @builtins.property
    @jsii.member(jsii_name="enableBgp")
    def enable_bgp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBgp"))

    @enable_bgp.setter
    def enable_bgp(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "enable_bgp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBgp", value)

    @builtins.property
    @jsii.member(jsii_name="expressRouteCircuitId")
    def express_route_circuit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expressRouteCircuitId"))

    @express_route_circuit_id.setter
    def express_route_circuit_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "express_route_circuit_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expressRouteCircuitId", value)

    @builtins.property
    @jsii.member(jsii_name="expressRouteGatewayBypass")
    def express_route_gateway_bypass(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "expressRouteGatewayBypass"))

    @express_route_gateway_bypass.setter
    def express_route_gateway_bypass(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "express_route_gateway_bypass").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expressRouteGatewayBypass", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ingressNatRuleIds")
    def ingress_nat_rule_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ingressNatRuleIds"))

    @ingress_nat_rule_ids.setter
    def ingress_nat_rule_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "ingress_nat_rule_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressNatRuleIds", value)

    @builtins.property
    @jsii.member(jsii_name="localAzureIpAddressEnabled")
    def local_azure_ip_address_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "localAzureIpAddressEnabled"))

    @local_azure_ip_address_enabled.setter
    def local_azure_ip_address_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "local_azure_ip_address_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAzureIpAddressEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="localNetworkGatewayId")
    def local_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localNetworkGatewayId"))

    @local_network_gateway_id.setter
    def local_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "local_network_gateway_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localNetworkGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="peerVirtualNetworkGatewayId")
    def peer_virtual_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerVirtualNetworkGatewayId"))

    @peer_virtual_network_gateway_id.setter
    def peer_virtual_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "peer_virtual_network_gateway_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVirtualNetworkGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="routingWeight")
    def routing_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "routingWeight"))

    @routing_weight.setter
    def routing_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "routing_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingWeight", value)

    @builtins.property
    @jsii.member(jsii_name="sharedKey")
    def shared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedKey"))

    @shared_key.setter
    def shared_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "shared_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="usePolicyBasedTrafficSelectors")
    def use_policy_based_traffic_selectors(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "usePolicyBasedTrafficSelectors"))

    @use_policy_based_traffic_selectors.setter
    def use_policy_based_traffic_selectors(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "use_policy_based_traffic_selectors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usePolicyBasedTrafficSelectors", value)

    @builtins.property
    @jsii.member(jsii_name="virtualNetworkGatewayId")
    def virtual_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualNetworkGatewayId"))

    @virtual_network_gateway_id.setter
    def virtual_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnection, "virtual_network_gateway_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualNetworkGatewayId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "type": "type",
        "virtual_network_gateway_id": "virtualNetworkGatewayId",
        "authorization_key": "authorizationKey",
        "connection_mode": "connectionMode",
        "connection_protocol": "connectionProtocol",
        "custom_bgp_addresses": "customBgpAddresses",
        "dpd_timeout_seconds": "dpdTimeoutSeconds",
        "egress_nat_rule_ids": "egressNatRuleIds",
        "enable_bgp": "enableBgp",
        "express_route_circuit_id": "expressRouteCircuitId",
        "express_route_gateway_bypass": "expressRouteGatewayBypass",
        "id": "id",
        "ingress_nat_rule_ids": "ingressNatRuleIds",
        "ipsec_policy": "ipsecPolicy",
        "local_azure_ip_address_enabled": "localAzureIpAddressEnabled",
        "local_network_gateway_id": "localNetworkGatewayId",
        "peer_virtual_network_gateway_id": "peerVirtualNetworkGatewayId",
        "routing_weight": "routingWeight",
        "shared_key": "sharedKey",
        "tags": "tags",
        "timeouts": "timeouts",
        "traffic_selector_policy": "trafficSelectorPolicy",
        "use_policy_based_traffic_selectors": "usePolicyBasedTrafficSelectors",
    },
)
class VirtualNetworkGatewayConnectionConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        type: builtins.str,
        virtual_network_gateway_id: builtins.str,
        authorization_key: typing.Optional[builtins.str] = None,
        connection_mode: typing.Optional[builtins.str] = None,
        connection_protocol: typing.Optional[builtins.str] = None,
        custom_bgp_addresses: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionCustomBgpAddresses", typing.Dict[str, typing.Any]]] = None,
        dpd_timeout_seconds: typing.Optional[jsii.Number] = None,
        egress_nat_rule_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        express_route_circuit_id: typing.Optional[builtins.str] = None,
        express_route_gateway_bypass: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ingress_nat_rule_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipsec_policy: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionIpsecPolicy", typing.Dict[str, typing.Any]]] = None,
        local_azure_ip_address_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        local_network_gateway_id: typing.Optional[builtins.str] = None,
        peer_virtual_network_gateway_id: typing.Optional[builtins.str] = None,
        routing_weight: typing.Optional[jsii.Number] = None,
        shared_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        traffic_selector_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayConnectionTrafficSelectorPolicy", typing.Dict[str, typing.Any]]]]] = None,
        use_policy_based_traffic_selectors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#location VirtualNetworkGatewayConnection#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#name VirtualNetworkGatewayConnection#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#resource_group_name VirtualNetworkGatewayConnection#resource_group_name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#type VirtualNetworkGatewayConnection#type}.
        :param virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#virtual_network_gateway_id VirtualNetworkGatewayConnection#virtual_network_gateway_id}.
        :param authorization_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#authorization_key VirtualNetworkGatewayConnection#authorization_key}.
        :param connection_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#connection_mode VirtualNetworkGatewayConnection#connection_mode}.
        :param connection_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#connection_protocol VirtualNetworkGatewayConnection#connection_protocol}.
        :param custom_bgp_addresses: custom_bgp_addresses block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#custom_bgp_addresses VirtualNetworkGatewayConnection#custom_bgp_addresses}
        :param dpd_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#dpd_timeout_seconds VirtualNetworkGatewayConnection#dpd_timeout_seconds}.
        :param egress_nat_rule_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#egress_nat_rule_ids VirtualNetworkGatewayConnection#egress_nat_rule_ids}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#enable_bgp VirtualNetworkGatewayConnection#enable_bgp}.
        :param express_route_circuit_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#express_route_circuit_id VirtualNetworkGatewayConnection#express_route_circuit_id}.
        :param express_route_gateway_bypass: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#express_route_gateway_bypass VirtualNetworkGatewayConnection#express_route_gateway_bypass}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#id VirtualNetworkGatewayConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ingress_nat_rule_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ingress_nat_rule_ids VirtualNetworkGatewayConnection#ingress_nat_rule_ids}.
        :param ipsec_policy: ipsec_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_policy VirtualNetworkGatewayConnection#ipsec_policy}
        :param local_azure_ip_address_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_azure_ip_address_enabled VirtualNetworkGatewayConnection#local_azure_ip_address_enabled}.
        :param local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_network_gateway_id VirtualNetworkGatewayConnection#local_network_gateway_id}.
        :param peer_virtual_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#peer_virtual_network_gateway_id VirtualNetworkGatewayConnection#peer_virtual_network_gateway_id}.
        :param routing_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#routing_weight VirtualNetworkGatewayConnection#routing_weight}.
        :param shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#shared_key VirtualNetworkGatewayConnection#shared_key}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#tags VirtualNetworkGatewayConnection#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#timeouts VirtualNetworkGatewayConnection#timeouts}
        :param traffic_selector_policy: traffic_selector_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#traffic_selector_policy VirtualNetworkGatewayConnection#traffic_selector_policy}
        :param use_policy_based_traffic_selectors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#use_policy_based_traffic_selectors VirtualNetworkGatewayConnection#use_policy_based_traffic_selectors}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_bgp_addresses, dict):
            custom_bgp_addresses = VirtualNetworkGatewayConnectionCustomBgpAddresses(**custom_bgp_addresses)
        if isinstance(ipsec_policy, dict):
            ipsec_policy = VirtualNetworkGatewayConnectionIpsecPolicy(**ipsec_policy)
        if isinstance(timeouts, dict):
            timeouts = VirtualNetworkGatewayConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument virtual_network_gateway_id", value=virtual_network_gateway_id, expected_type=type_hints["virtual_network_gateway_id"])
            check_type(argname="argument authorization_key", value=authorization_key, expected_type=type_hints["authorization_key"])
            check_type(argname="argument connection_mode", value=connection_mode, expected_type=type_hints["connection_mode"])
            check_type(argname="argument connection_protocol", value=connection_protocol, expected_type=type_hints["connection_protocol"])
            check_type(argname="argument custom_bgp_addresses", value=custom_bgp_addresses, expected_type=type_hints["custom_bgp_addresses"])
            check_type(argname="argument dpd_timeout_seconds", value=dpd_timeout_seconds, expected_type=type_hints["dpd_timeout_seconds"])
            check_type(argname="argument egress_nat_rule_ids", value=egress_nat_rule_ids, expected_type=type_hints["egress_nat_rule_ids"])
            check_type(argname="argument enable_bgp", value=enable_bgp, expected_type=type_hints["enable_bgp"])
            check_type(argname="argument express_route_circuit_id", value=express_route_circuit_id, expected_type=type_hints["express_route_circuit_id"])
            check_type(argname="argument express_route_gateway_bypass", value=express_route_gateway_bypass, expected_type=type_hints["express_route_gateway_bypass"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ingress_nat_rule_ids", value=ingress_nat_rule_ids, expected_type=type_hints["ingress_nat_rule_ids"])
            check_type(argname="argument ipsec_policy", value=ipsec_policy, expected_type=type_hints["ipsec_policy"])
            check_type(argname="argument local_azure_ip_address_enabled", value=local_azure_ip_address_enabled, expected_type=type_hints["local_azure_ip_address_enabled"])
            check_type(argname="argument local_network_gateway_id", value=local_network_gateway_id, expected_type=type_hints["local_network_gateway_id"])
            check_type(argname="argument peer_virtual_network_gateway_id", value=peer_virtual_network_gateway_id, expected_type=type_hints["peer_virtual_network_gateway_id"])
            check_type(argname="argument routing_weight", value=routing_weight, expected_type=type_hints["routing_weight"])
            check_type(argname="argument shared_key", value=shared_key, expected_type=type_hints["shared_key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument traffic_selector_policy", value=traffic_selector_policy, expected_type=type_hints["traffic_selector_policy"])
            check_type(argname="argument use_policy_based_traffic_selectors", value=use_policy_based_traffic_selectors, expected_type=type_hints["use_policy_based_traffic_selectors"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "type": type,
            "virtual_network_gateway_id": virtual_network_gateway_id,
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
        if authorization_key is not None:
            self._values["authorization_key"] = authorization_key
        if connection_mode is not None:
            self._values["connection_mode"] = connection_mode
        if connection_protocol is not None:
            self._values["connection_protocol"] = connection_protocol
        if custom_bgp_addresses is not None:
            self._values["custom_bgp_addresses"] = custom_bgp_addresses
        if dpd_timeout_seconds is not None:
            self._values["dpd_timeout_seconds"] = dpd_timeout_seconds
        if egress_nat_rule_ids is not None:
            self._values["egress_nat_rule_ids"] = egress_nat_rule_ids
        if enable_bgp is not None:
            self._values["enable_bgp"] = enable_bgp
        if express_route_circuit_id is not None:
            self._values["express_route_circuit_id"] = express_route_circuit_id
        if express_route_gateway_bypass is not None:
            self._values["express_route_gateway_bypass"] = express_route_gateway_bypass
        if id is not None:
            self._values["id"] = id
        if ingress_nat_rule_ids is not None:
            self._values["ingress_nat_rule_ids"] = ingress_nat_rule_ids
        if ipsec_policy is not None:
            self._values["ipsec_policy"] = ipsec_policy
        if local_azure_ip_address_enabled is not None:
            self._values["local_azure_ip_address_enabled"] = local_azure_ip_address_enabled
        if local_network_gateway_id is not None:
            self._values["local_network_gateway_id"] = local_network_gateway_id
        if peer_virtual_network_gateway_id is not None:
            self._values["peer_virtual_network_gateway_id"] = peer_virtual_network_gateway_id
        if routing_weight is not None:
            self._values["routing_weight"] = routing_weight
        if shared_key is not None:
            self._values["shared_key"] = shared_key
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if traffic_selector_policy is not None:
            self._values["traffic_selector_policy"] = traffic_selector_policy
        if use_policy_based_traffic_selectors is not None:
            self._values["use_policy_based_traffic_selectors"] = use_policy_based_traffic_selectors

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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#location VirtualNetworkGatewayConnection#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#name VirtualNetworkGatewayConnection#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#resource_group_name VirtualNetworkGatewayConnection#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#type VirtualNetworkGatewayConnection#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_network_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#virtual_network_gateway_id VirtualNetworkGatewayConnection#virtual_network_gateway_id}.'''
        result = self._values.get("virtual_network_gateway_id")
        assert result is not None, "Required property 'virtual_network_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#authorization_key VirtualNetworkGatewayConnection#authorization_key}.'''
        result = self._values.get("authorization_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#connection_mode VirtualNetworkGatewayConnection#connection_mode}.'''
        result = self._values.get("connection_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#connection_protocol VirtualNetworkGatewayConnection#connection_protocol}.'''
        result = self._values.get("connection_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_bgp_addresses(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayConnectionCustomBgpAddresses"]:
        '''custom_bgp_addresses block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#custom_bgp_addresses VirtualNetworkGatewayConnection#custom_bgp_addresses}
        '''
        result = self._values.get("custom_bgp_addresses")
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionCustomBgpAddresses"], result)

    @builtins.property
    def dpd_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#dpd_timeout_seconds VirtualNetworkGatewayConnection#dpd_timeout_seconds}.'''
        result = self._values.get("dpd_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def egress_nat_rule_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#egress_nat_rule_ids VirtualNetworkGatewayConnection#egress_nat_rule_ids}.'''
        result = self._values.get("egress_nat_rule_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enable_bgp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#enable_bgp VirtualNetworkGatewayConnection#enable_bgp}.'''
        result = self._values.get("enable_bgp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def express_route_circuit_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#express_route_circuit_id VirtualNetworkGatewayConnection#express_route_circuit_id}.'''
        result = self._values.get("express_route_circuit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def express_route_gateway_bypass(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#express_route_gateway_bypass VirtualNetworkGatewayConnection#express_route_gateway_bypass}.'''
        result = self._values.get("express_route_gateway_bypass")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#id VirtualNetworkGatewayConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ingress_nat_rule_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ingress_nat_rule_ids VirtualNetworkGatewayConnection#ingress_nat_rule_ids}.'''
        result = self._values.get("ingress_nat_rule_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipsec_policy(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"]:
        '''ipsec_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_policy VirtualNetworkGatewayConnection#ipsec_policy}
        '''
        result = self._values.get("ipsec_policy")
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionIpsecPolicy"], result)

    @builtins.property
    def local_azure_ip_address_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_azure_ip_address_enabled VirtualNetworkGatewayConnection#local_azure_ip_address_enabled}.'''
        result = self._values.get("local_azure_ip_address_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def local_network_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_network_gateway_id VirtualNetworkGatewayConnection#local_network_gateway_id}.'''
        result = self._values.get("local_network_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_virtual_network_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#peer_virtual_network_gateway_id VirtualNetworkGatewayConnection#peer_virtual_network_gateway_id}.'''
        result = self._values.get("peer_virtual_network_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routing_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#routing_weight VirtualNetworkGatewayConnection#routing_weight}.'''
        result = self._values.get("routing_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shared_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#shared_key VirtualNetworkGatewayConnection#shared_key}.'''
        result = self._values.get("shared_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#tags VirtualNetworkGatewayConnection#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualNetworkGatewayConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#timeouts VirtualNetworkGatewayConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualNetworkGatewayConnectionTimeouts"], result)

    @builtins.property
    def traffic_selector_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayConnectionTrafficSelectorPolicy"]]]:
        '''traffic_selector_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#traffic_selector_policy VirtualNetworkGatewayConnection#traffic_selector_policy}
        '''
        result = self._values.get("traffic_selector_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayConnectionTrafficSelectorPolicy"]]], result)

    @builtins.property
    def use_policy_based_traffic_selectors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#use_policy_based_traffic_selectors VirtualNetworkGatewayConnection#use_policy_based_traffic_selectors}.'''
        result = self._values.get("use_policy_based_traffic_selectors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionCustomBgpAddresses",
    jsii_struct_bases=[],
    name_mapping={"primary": "primary", "secondary": "secondary"},
)
class VirtualNetworkGatewayConnectionCustomBgpAddresses:
    def __init__(self, *, primary: builtins.str, secondary: builtins.str) -> None:
        '''
        :param primary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#primary VirtualNetworkGatewayConnection#primary}.
        :param secondary: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#secondary VirtualNetworkGatewayConnection#secondary}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionCustomBgpAddresses.__init__)
            check_type(argname="argument primary", value=primary, expected_type=type_hints["primary"])
            check_type(argname="argument secondary", value=secondary, expected_type=type_hints["secondary"])
        self._values: typing.Dict[str, typing.Any] = {
            "primary": primary,
            "secondary": secondary,
        }

    @builtins.property
    def primary(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#primary VirtualNetworkGatewayConnection#primary}.'''
        result = self._values.get("primary")
        assert result is not None, "Required property 'primary' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secondary(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#secondary VirtualNetworkGatewayConnection#secondary}.'''
        result = self._values.get("secondary")
        assert result is not None, "Required property 'secondary' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionCustomBgpAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="primaryInput")
    def primary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryInput")
    def secondary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondaryInput"))

    @builtins.property
    @jsii.member(jsii_name="primary")
    def primary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primary"))

    @primary.setter
    def primary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference, "primary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primary", value)

    @builtins.property
    @jsii.member(jsii_name="secondary")
    def secondary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondary"))

    @secondary.setter
    def secondary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference, "secondary").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualNetworkGatewayConnectionCustomBgpAddresses]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayConnectionCustomBgpAddresses], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayConnectionCustomBgpAddresses],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionIpsecPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "dh_group": "dhGroup",
        "ike_encryption": "ikeEncryption",
        "ike_integrity": "ikeIntegrity",
        "ipsec_encryption": "ipsecEncryption",
        "ipsec_integrity": "ipsecIntegrity",
        "pfs_group": "pfsGroup",
        "sa_datasize": "saDatasize",
        "sa_lifetime": "saLifetime",
    },
)
class VirtualNetworkGatewayConnectionIpsecPolicy:
    def __init__(
        self,
        *,
        dh_group: builtins.str,
        ike_encryption: builtins.str,
        ike_integrity: builtins.str,
        ipsec_encryption: builtins.str,
        ipsec_integrity: builtins.str,
        pfs_group: builtins.str,
        sa_datasize: typing.Optional[jsii.Number] = None,
        sa_lifetime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#dh_group VirtualNetworkGatewayConnection#dh_group}.
        :param ike_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ike_encryption VirtualNetworkGatewayConnection#ike_encryption}.
        :param ike_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ike_integrity VirtualNetworkGatewayConnection#ike_integrity}.
        :param ipsec_encryption: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_encryption VirtualNetworkGatewayConnection#ipsec_encryption}.
        :param ipsec_integrity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_integrity VirtualNetworkGatewayConnection#ipsec_integrity}.
        :param pfs_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#pfs_group VirtualNetworkGatewayConnection#pfs_group}.
        :param sa_datasize: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#sa_datasize VirtualNetworkGatewayConnection#sa_datasize}.
        :param sa_lifetime: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#sa_lifetime VirtualNetworkGatewayConnection#sa_lifetime}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionIpsecPolicy.__init__)
            check_type(argname="argument dh_group", value=dh_group, expected_type=type_hints["dh_group"])
            check_type(argname="argument ike_encryption", value=ike_encryption, expected_type=type_hints["ike_encryption"])
            check_type(argname="argument ike_integrity", value=ike_integrity, expected_type=type_hints["ike_integrity"])
            check_type(argname="argument ipsec_encryption", value=ipsec_encryption, expected_type=type_hints["ipsec_encryption"])
            check_type(argname="argument ipsec_integrity", value=ipsec_integrity, expected_type=type_hints["ipsec_integrity"])
            check_type(argname="argument pfs_group", value=pfs_group, expected_type=type_hints["pfs_group"])
            check_type(argname="argument sa_datasize", value=sa_datasize, expected_type=type_hints["sa_datasize"])
            check_type(argname="argument sa_lifetime", value=sa_lifetime, expected_type=type_hints["sa_lifetime"])
        self._values: typing.Dict[str, typing.Any] = {
            "dh_group": dh_group,
            "ike_encryption": ike_encryption,
            "ike_integrity": ike_integrity,
            "ipsec_encryption": ipsec_encryption,
            "ipsec_integrity": ipsec_integrity,
            "pfs_group": pfs_group,
        }
        if sa_datasize is not None:
            self._values["sa_datasize"] = sa_datasize
        if sa_lifetime is not None:
            self._values["sa_lifetime"] = sa_lifetime

    @builtins.property
    def dh_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#dh_group VirtualNetworkGatewayConnection#dh_group}.'''
        result = self._values.get("dh_group")
        assert result is not None, "Required property 'dh_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ike_encryption VirtualNetworkGatewayConnection#ike_encryption}.'''
        result = self._values.get("ike_encryption")
        assert result is not None, "Required property 'ike_encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_integrity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ike_integrity VirtualNetworkGatewayConnection#ike_integrity}.'''
        result = self._values.get("ike_integrity")
        assert result is not None, "Required property 'ike_integrity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipsec_encryption(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_encryption VirtualNetworkGatewayConnection#ipsec_encryption}.'''
        result = self._values.get("ipsec_encryption")
        assert result is not None, "Required property 'ipsec_encryption' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipsec_integrity(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#ipsec_integrity VirtualNetworkGatewayConnection#ipsec_integrity}.'''
        result = self._values.get("ipsec_integrity")
        assert result is not None, "Required property 'ipsec_integrity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pfs_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#pfs_group VirtualNetworkGatewayConnection#pfs_group}.'''
        result = self._values.get("pfs_group")
        assert result is not None, "Required property 'pfs_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sa_datasize(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#sa_datasize VirtualNetworkGatewayConnection#sa_datasize}.'''
        result = self._values.get("sa_datasize")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sa_lifetime(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#sa_lifetime VirtualNetworkGatewayConnection#sa_lifetime}.'''
        result = self._values.get("sa_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionIpsecPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayConnectionIpsecPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionIpsecPolicyOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSaDatasize")
    def reset_sa_datasize(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaDatasize", []))

    @jsii.member(jsii_name="resetSaLifetime")
    def reset_sa_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSaLifetime", []))

    @builtins.property
    @jsii.member(jsii_name="dhGroupInput")
    def dh_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeEncryptionInput")
    def ike_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrityInput")
    def ike_integrity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeIntegrityInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecEncryptionInput")
    def ipsec_encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipsecEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecIntegrityInput")
    def ipsec_integrity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipsecIntegrityInput"))

    @builtins.property
    @jsii.member(jsii_name="pfsGroupInput")
    def pfs_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pfsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="saDatasizeInput")
    def sa_datasize_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saDatasizeInput"))

    @builtins.property
    @jsii.member(jsii_name="saLifetimeInput")
    def sa_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="dhGroup")
    def dh_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dhGroup"))

    @dh_group.setter
    def dh_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "dh_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhGroup", value)

    @builtins.property
    @jsii.member(jsii_name="ikeEncryption")
    def ike_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeEncryption"))

    @ike_encryption.setter
    def ike_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "ike_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrity")
    def ike_integrity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeIntegrity"))

    @ike_integrity.setter
    def ike_integrity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "ike_integrity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeIntegrity", value)

    @builtins.property
    @jsii.member(jsii_name="ipsecEncryption")
    def ipsec_encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipsecEncryption"))

    @ipsec_encryption.setter
    def ipsec_encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "ipsec_encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipsecEncryption", value)

    @builtins.property
    @jsii.member(jsii_name="ipsecIntegrity")
    def ipsec_integrity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipsecIntegrity"))

    @ipsec_integrity.setter
    def ipsec_integrity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "ipsec_integrity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipsecIntegrity", value)

    @builtins.property
    @jsii.member(jsii_name="pfsGroup")
    def pfs_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pfsGroup"))

    @pfs_group.setter
    def pfs_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "pfs_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pfsGroup", value)

    @builtins.property
    @jsii.member(jsii_name="saDatasize")
    def sa_datasize(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saDatasize"))

    @sa_datasize.setter
    def sa_datasize(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "sa_datasize").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saDatasize", value)

    @builtins.property
    @jsii.member(jsii_name="saLifetime")
    def sa_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saLifetime"))

    @sa_lifetime.setter
    def sa_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "sa_lifetime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualNetworkGatewayConnectionIpsecPolicy]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayConnectionIpsecPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayConnectionIpsecPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionIpsecPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualNetworkGatewayConnectionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#create VirtualNetworkGatewayConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#delete VirtualNetworkGatewayConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#read VirtualNetworkGatewayConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#update VirtualNetworkGatewayConnection#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#create VirtualNetworkGatewayConnection#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#delete VirtualNetworkGatewayConnection#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#read VirtualNetworkGatewayConnection#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#update VirtualNetworkGatewayConnection#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayConnectionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionTrafficSelectorPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "local_address_cidrs": "localAddressCidrs",
        "remote_address_cidrs": "remoteAddressCidrs",
    },
)
class VirtualNetworkGatewayConnectionTrafficSelectorPolicy:
    def __init__(
        self,
        *,
        local_address_cidrs: typing.Sequence[builtins.str],
        remote_address_cidrs: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param local_address_cidrs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_address_cidrs VirtualNetworkGatewayConnection#local_address_cidrs}.
        :param remote_address_cidrs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#remote_address_cidrs VirtualNetworkGatewayConnection#remote_address_cidrs}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionTrafficSelectorPolicy.__init__)
            check_type(argname="argument local_address_cidrs", value=local_address_cidrs, expected_type=type_hints["local_address_cidrs"])
            check_type(argname="argument remote_address_cidrs", value=remote_address_cidrs, expected_type=type_hints["remote_address_cidrs"])
        self._values: typing.Dict[str, typing.Any] = {
            "local_address_cidrs": local_address_cidrs,
            "remote_address_cidrs": remote_address_cidrs,
        }

    @builtins.property
    def local_address_cidrs(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#local_address_cidrs VirtualNetworkGatewayConnection#local_address_cidrs}.'''
        result = self._values.get("local_address_cidrs")
        assert result is not None, "Required property 'local_address_cidrs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def remote_address_cidrs(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway_connection#remote_address_cidrs VirtualNetworkGatewayConnection#remote_address_cidrs}.'''
        result = self._values.get("remote_address_cidrs")
        assert result is not None, "Required property 'remote_address_cidrs' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConnectionTrafficSelectorPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayConnectionTrafficSelectorPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionTrafficSelectorPolicyList",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionTrafficSelectorPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionTrafficSelectorPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTrafficSelectorPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTrafficSelectorPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTrafficSelectorPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayConnectionTrafficSelectorPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayConnectionTrafficSelectorPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayConnectionTrafficSelectorPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTrafficSelectorPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGatewayConnection.VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="localAddressCidrsInput")
    def local_address_cidrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "localAddressCidrsInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteAddressCidrsInput")
    def remote_address_cidrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "remoteAddressCidrsInput"))

    @builtins.property
    @jsii.member(jsii_name="localAddressCidrs")
    def local_address_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "localAddressCidrs"))

    @local_address_cidrs.setter
    def local_address_cidrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference, "local_address_cidrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAddressCidrs", value)

    @builtins.property
    @jsii.member(jsii_name="remoteAddressCidrs")
    def remote_address_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "remoteAddressCidrs"))

    @remote_address_cidrs.setter
    def remote_address_cidrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference, "remote_address_cidrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteAddressCidrs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTrafficSelectorPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTrafficSelectorPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayConnectionTrafficSelectorPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualNetworkGatewayConnection",
    "VirtualNetworkGatewayConnectionConfig",
    "VirtualNetworkGatewayConnectionCustomBgpAddresses",
    "VirtualNetworkGatewayConnectionCustomBgpAddressesOutputReference",
    "VirtualNetworkGatewayConnectionIpsecPolicy",
    "VirtualNetworkGatewayConnectionIpsecPolicyOutputReference",
    "VirtualNetworkGatewayConnectionTimeouts",
    "VirtualNetworkGatewayConnectionTimeoutsOutputReference",
    "VirtualNetworkGatewayConnectionTrafficSelectorPolicy",
    "VirtualNetworkGatewayConnectionTrafficSelectorPolicyList",
    "VirtualNetworkGatewayConnectionTrafficSelectorPolicyOutputReference",
]

publication.publish()
