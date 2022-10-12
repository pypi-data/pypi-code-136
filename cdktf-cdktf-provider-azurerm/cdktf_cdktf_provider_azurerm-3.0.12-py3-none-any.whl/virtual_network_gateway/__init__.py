'''
# `azurerm_virtual_network_gateway`

Refer to the Terraform Registory for docs: [`azurerm_virtual_network_gateway`](https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway).
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


class VirtualNetworkGateway(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway azurerm_virtual_network_gateway}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayIpConfiguration", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        type: builtins.str,
        active_active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bgp_settings: typing.Optional[typing.Union["VirtualNetworkGatewayBgpSettings", typing.Dict[str, typing.Any]]] = None,
        custom_route: typing.Optional[typing.Union["VirtualNetworkGatewayCustomRoute", typing.Dict[str, typing.Any]]] = None,
        default_local_network_gateway_id: typing.Optional[builtins.str] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        generation: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        private_ip_address_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_client_configuration: typing.Optional[typing.Union["VirtualNetworkGatewayVpnClientConfiguration", typing.Dict[str, typing.Any]]] = None,
        vpn_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway azurerm_virtual_network_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#ip_configuration VirtualNetworkGateway#ip_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#location VirtualNetworkGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#resource_group_name VirtualNetworkGateway#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#sku VirtualNetworkGateway#sku}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#type VirtualNetworkGateway#type}.
        :param active_active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#active_active VirtualNetworkGateway#active_active}.
        :param bgp_settings: bgp_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#bgp_settings VirtualNetworkGateway#bgp_settings}
        :param custom_route: custom_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#custom_route VirtualNetworkGateway#custom_route}
        :param default_local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#default_local_network_gateway_id VirtualNetworkGateway#default_local_network_gateway_id}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#edge_zone VirtualNetworkGateway#edge_zone}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#enable_bgp VirtualNetworkGateway#enable_bgp}.
        :param generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#generation VirtualNetworkGateway#generation}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#id VirtualNetworkGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_ip_address_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#private_ip_address_enabled VirtualNetworkGateway#private_ip_address_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#tags VirtualNetworkGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#timeouts VirtualNetworkGateway#timeouts}
        :param vpn_client_configuration: vpn_client_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_client_configuration VirtualNetworkGateway#vpn_client_configuration}
        :param vpn_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_type VirtualNetworkGateway#vpn_type}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGateway.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualNetworkGatewayConfig(
            ip_configuration=ip_configuration,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            sku=sku,
            type=type,
            active_active=active_active,
            bgp_settings=bgp_settings,
            custom_route=custom_route,
            default_local_network_gateway_id=default_local_network_gateway_id,
            edge_zone=edge_zone,
            enable_bgp=enable_bgp,
            generation=generation,
            id=id,
            private_ip_address_enabled=private_ip_address_enabled,
            tags=tags,
            timeouts=timeouts,
            vpn_client_configuration=vpn_client_configuration,
            vpn_type=vpn_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBgpSettings")
    def put_bgp_settings(
        self,
        *,
        asn: typing.Optional[jsii.Number] = None,
        peering_addresses: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayBgpSettingsPeeringAddresses", typing.Dict[str, typing.Any]]]]] = None,
        peer_weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#asn VirtualNetworkGateway#asn}.
        :param peering_addresses: peering_addresses block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#peering_addresses VirtualNetworkGateway#peering_addresses}
        :param peer_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#peer_weight VirtualNetworkGateway#peer_weight}.
        '''
        value = VirtualNetworkGatewayBgpSettings(
            asn=asn, peering_addresses=peering_addresses, peer_weight=peer_weight
        )

        return typing.cast(None, jsii.invoke(self, "putBgpSettings", [value]))

    @jsii.member(jsii_name="putCustomRoute")
    def put_custom_route(
        self,
        *,
        address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#address_prefixes VirtualNetworkGateway#address_prefixes}.
        '''
        value = VirtualNetworkGatewayCustomRoute(address_prefixes=address_prefixes)

        return typing.cast(None, jsii.invoke(self, "putCustomRoute", [value]))

    @jsii.member(jsii_name="putIpConfiguration")
    def put_ip_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayIpConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGateway.put_ip_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpConfiguration", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#create VirtualNetworkGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#delete VirtualNetworkGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#read VirtualNetworkGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#update VirtualNetworkGateway#update}.
        '''
        value = VirtualNetworkGatewayTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVpnClientConfiguration")
    def put_vpn_client_configuration(
        self,
        *,
        address_space: typing.Sequence[builtins.str],
        aad_audience: typing.Optional[builtins.str] = None,
        aad_issuer: typing.Optional[builtins.str] = None,
        aad_tenant: typing.Optional[builtins.str] = None,
        radius_server_address: typing.Optional[builtins.str] = None,
        radius_server_secret: typing.Optional[builtins.str] = None,
        revoked_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate", typing.Dict[str, typing.Any]]]]] = None,
        root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
        vpn_auth_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpn_client_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param address_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#address_space VirtualNetworkGateway#address_space}.
        :param aad_audience: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_audience VirtualNetworkGateway#aad_audience}.
        :param aad_issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_issuer VirtualNetworkGateway#aad_issuer}.
        :param aad_tenant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_tenant VirtualNetworkGateway#aad_tenant}.
        :param radius_server_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#radius_server_address VirtualNetworkGateway#radius_server_address}.
        :param radius_server_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#radius_server_secret VirtualNetworkGateway#radius_server_secret}.
        :param revoked_certificate: revoked_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#revoked_certificate VirtualNetworkGateway#revoked_certificate}
        :param root_certificate: root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#root_certificate VirtualNetworkGateway#root_certificate}
        :param vpn_auth_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_auth_types VirtualNetworkGateway#vpn_auth_types}.
        :param vpn_client_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_client_protocols VirtualNetworkGateway#vpn_client_protocols}.
        '''
        value = VirtualNetworkGatewayVpnClientConfiguration(
            address_space=address_space,
            aad_audience=aad_audience,
            aad_issuer=aad_issuer,
            aad_tenant=aad_tenant,
            radius_server_address=radius_server_address,
            radius_server_secret=radius_server_secret,
            revoked_certificate=revoked_certificate,
            root_certificate=root_certificate,
            vpn_auth_types=vpn_auth_types,
            vpn_client_protocols=vpn_client_protocols,
        )

        return typing.cast(None, jsii.invoke(self, "putVpnClientConfiguration", [value]))

    @jsii.member(jsii_name="resetActiveActive")
    def reset_active_active(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActiveActive", []))

    @jsii.member(jsii_name="resetBgpSettings")
    def reset_bgp_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgpSettings", []))

    @jsii.member(jsii_name="resetCustomRoute")
    def reset_custom_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomRoute", []))

    @jsii.member(jsii_name="resetDefaultLocalNetworkGatewayId")
    def reset_default_local_network_gateway_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLocalNetworkGatewayId", []))

    @jsii.member(jsii_name="resetEdgeZone")
    def reset_edge_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeZone", []))

    @jsii.member(jsii_name="resetEnableBgp")
    def reset_enable_bgp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBgp", []))

    @jsii.member(jsii_name="resetGeneration")
    def reset_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeneration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrivateIpAddressEnabled")
    def reset_private_ip_address_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddressEnabled", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpnClientConfiguration")
    def reset_vpn_client_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnClientConfiguration", []))

    @jsii.member(jsii_name="resetVpnType")
    def reset_vpn_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bgpSettings")
    def bgp_settings(self) -> "VirtualNetworkGatewayBgpSettingsOutputReference":
        return typing.cast("VirtualNetworkGatewayBgpSettingsOutputReference", jsii.get(self, "bgpSettings"))

    @builtins.property
    @jsii.member(jsii_name="customRoute")
    def custom_route(self) -> "VirtualNetworkGatewayCustomRouteOutputReference":
        return typing.cast("VirtualNetworkGatewayCustomRouteOutputReference", jsii.get(self, "customRoute"))

    @builtins.property
    @jsii.member(jsii_name="ipConfiguration")
    def ip_configuration(self) -> "VirtualNetworkGatewayIpConfigurationList":
        return typing.cast("VirtualNetworkGatewayIpConfigurationList", jsii.get(self, "ipConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualNetworkGatewayTimeoutsOutputReference":
        return typing.cast("VirtualNetworkGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientConfiguration")
    def vpn_client_configuration(
        self,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationOutputReference":
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationOutputReference", jsii.get(self, "vpnClientConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="activeActiveInput")
    def active_active_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "activeActiveInput"))

    @builtins.property
    @jsii.member(jsii_name="bgpSettingsInput")
    def bgp_settings_input(self) -> typing.Optional["VirtualNetworkGatewayBgpSettings"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayBgpSettings"], jsii.get(self, "bgpSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="customRouteInput")
    def custom_route_input(self) -> typing.Optional["VirtualNetworkGatewayCustomRoute"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayCustomRoute"], jsii.get(self, "customRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLocalNetworkGatewayIdInput")
    def default_local_network_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLocalNetworkGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeZoneInput")
    def edge_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBgpInput")
    def enable_bgp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBgpInput"))

    @builtins.property
    @jsii.member(jsii_name="generationInput")
    def generation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationInput")
    def ip_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]]], jsii.get(self, "ipConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressEnabledInput")
    def private_ip_address_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateIpAddressEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientConfigurationInput")
    def vpn_client_configuration_input(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"]:
        return typing.cast(typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"], jsii.get(self, "vpnClientConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnTypeInput")
    def vpn_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="activeActive")
    def active_active(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "activeActive"))

    @active_active.setter
    def active_active(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "active_active").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeActive", value)

    @builtins.property
    @jsii.member(jsii_name="defaultLocalNetworkGatewayId")
    def default_local_network_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLocalNetworkGatewayId"))

    @default_local_network_gateway_id.setter
    def default_local_network_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "default_local_network_gateway_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLocalNetworkGatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="edgeZone")
    def edge_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeZone"))

    @edge_zone.setter
    def edge_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "edge_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeZone", value)

    @builtins.property
    @jsii.member(jsii_name="enableBgp")
    def enable_bgp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBgp"))

    @enable_bgp.setter
    def enable_bgp(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "enable_bgp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBgp", value)

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generation"))

    @generation.setter
    def generation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "generation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generation", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressEnabled")
    def private_ip_address_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privateIpAddressEnabled"))

    @private_ip_address_enabled.setter
    def private_ip_address_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "private_ip_address_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddressEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="vpnType")
    def vpn_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnType"))

    @vpn_type.setter
    def vpn_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGateway, "vpn_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayBgpSettings",
    jsii_struct_bases=[],
    name_mapping={
        "asn": "asn",
        "peering_addresses": "peeringAddresses",
        "peer_weight": "peerWeight",
    },
)
class VirtualNetworkGatewayBgpSettings:
    def __init__(
        self,
        *,
        asn: typing.Optional[jsii.Number] = None,
        peering_addresses: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayBgpSettingsPeeringAddresses", typing.Dict[str, typing.Any]]]]] = None,
        peer_weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#asn VirtualNetworkGateway#asn}.
        :param peering_addresses: peering_addresses block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#peering_addresses VirtualNetworkGateway#peering_addresses}
        :param peer_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#peer_weight VirtualNetworkGateway#peer_weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayBgpSettings.__init__)
            check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
            check_type(argname="argument peering_addresses", value=peering_addresses, expected_type=type_hints["peering_addresses"])
            check_type(argname="argument peer_weight", value=peer_weight, expected_type=type_hints["peer_weight"])
        self._values: typing.Dict[str, typing.Any] = {}
        if asn is not None:
            self._values["asn"] = asn
        if peering_addresses is not None:
            self._values["peering_addresses"] = peering_addresses
        if peer_weight is not None:
            self._values["peer_weight"] = peer_weight

    @builtins.property
    def asn(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#asn VirtualNetworkGateway#asn}.'''
        result = self._values.get("asn")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def peering_addresses(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayBgpSettingsPeeringAddresses"]]]:
        '''peering_addresses block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#peering_addresses VirtualNetworkGateway#peering_addresses}
        '''
        result = self._values.get("peering_addresses")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayBgpSettingsPeeringAddresses"]]], result)

    @builtins.property
    def peer_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#peer_weight VirtualNetworkGateway#peer_weight}.'''
        result = self._values.get("peer_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayBgpSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayBgpSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayBgpSettingsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayBgpSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPeeringAddresses")
    def put_peering_addresses(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayBgpSettingsPeeringAddresses", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayBgpSettingsOutputReference.put_peering_addresses)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPeeringAddresses", [value]))

    @jsii.member(jsii_name="resetAsn")
    def reset_asn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAsn", []))

    @jsii.member(jsii_name="resetPeeringAddresses")
    def reset_peering_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeeringAddresses", []))

    @jsii.member(jsii_name="resetPeerWeight")
    def reset_peer_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeerWeight", []))

    @builtins.property
    @jsii.member(jsii_name="peeringAddresses")
    def peering_addresses(
        self,
    ) -> "VirtualNetworkGatewayBgpSettingsPeeringAddressesList":
        return typing.cast("VirtualNetworkGatewayBgpSettingsPeeringAddressesList", jsii.get(self, "peeringAddresses"))

    @builtins.property
    @jsii.member(jsii_name="asnInput")
    def asn_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "asnInput"))

    @builtins.property
    @jsii.member(jsii_name="peeringAddressesInput")
    def peering_addresses_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayBgpSettingsPeeringAddresses"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayBgpSettingsPeeringAddresses"]]], jsii.get(self, "peeringAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="peerWeightInput")
    def peer_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "peerWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="asn")
    def asn(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "asn"))

    @asn.setter
    def asn(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsOutputReference, "asn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asn", value)

    @builtins.property
    @jsii.member(jsii_name="peerWeight")
    def peer_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "peerWeight"))

    @peer_weight.setter
    def peer_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsOutputReference, "peer_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerWeight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualNetworkGatewayBgpSettings]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayBgpSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayBgpSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayBgpSettingsPeeringAddresses",
    jsii_struct_bases=[],
    name_mapping={
        "apipa_addresses": "apipaAddresses",
        "ip_configuration_name": "ipConfigurationName",
    },
)
class VirtualNetworkGatewayBgpSettingsPeeringAddresses:
    def __init__(
        self,
        *,
        apipa_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_configuration_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param apipa_addresses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#apipa_addresses VirtualNetworkGateway#apipa_addresses}.
        :param ip_configuration_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#ip_configuration_name VirtualNetworkGateway#ip_configuration_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayBgpSettingsPeeringAddresses.__init__)
            check_type(argname="argument apipa_addresses", value=apipa_addresses, expected_type=type_hints["apipa_addresses"])
            check_type(argname="argument ip_configuration_name", value=ip_configuration_name, expected_type=type_hints["ip_configuration_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if apipa_addresses is not None:
            self._values["apipa_addresses"] = apipa_addresses
        if ip_configuration_name is not None:
            self._values["ip_configuration_name"] = ip_configuration_name

    @builtins.property
    def apipa_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#apipa_addresses VirtualNetworkGateway#apipa_addresses}.'''
        result = self._values.get("apipa_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_configuration_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#ip_configuration_name VirtualNetworkGateway#ip_configuration_name}.'''
        result = self._values.get("ip_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayBgpSettingsPeeringAddresses(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayBgpSettingsPeeringAddressesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayBgpSettingsPeeringAddressesList",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayBgpSettingsPeeringAddressesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayBgpSettingsPeeringAddressesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsPeeringAddressesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsPeeringAddressesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsPeeringAddressesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayBgpSettingsPeeringAddresses]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayBgpSettingsPeeringAddresses]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayBgpSettingsPeeringAddresses]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsPeeringAddressesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApipaAddresses")
    def reset_apipa_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApipaAddresses", []))

    @jsii.member(jsii_name="resetIpConfigurationName")
    def reset_ip_configuration_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpConfigurationName", []))

    @builtins.property
    @jsii.member(jsii_name="defaultAddresses")
    def default_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultAddresses"))

    @builtins.property
    @jsii.member(jsii_name="tunnelIpAddresses")
    def tunnel_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnelIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="apipaAddressesInput")
    def apipa_addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apipaAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationNameInput")
    def ip_configuration_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipConfigurationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="apipaAddresses")
    def apipa_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apipaAddresses"))

    @apipa_addresses.setter
    def apipa_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference, "apipa_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apipaAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationName")
    def ip_configuration_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipConfigurationName"))

    @ip_configuration_name.setter
    def ip_configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference, "ip_configuration_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayBgpSettingsPeeringAddresses, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayBgpSettingsPeeringAddresses, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayBgpSettingsPeeringAddresses, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ip_configuration": "ipConfiguration",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "sku": "sku",
        "type": "type",
        "active_active": "activeActive",
        "bgp_settings": "bgpSettings",
        "custom_route": "customRoute",
        "default_local_network_gateway_id": "defaultLocalNetworkGatewayId",
        "edge_zone": "edgeZone",
        "enable_bgp": "enableBgp",
        "generation": "generation",
        "id": "id",
        "private_ip_address_enabled": "privateIpAddressEnabled",
        "tags": "tags",
        "timeouts": "timeouts",
        "vpn_client_configuration": "vpnClientConfiguration",
        "vpn_type": "vpnType",
    },
)
class VirtualNetworkGatewayConfig(cdktf.TerraformMetaArguments):
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
        ip_configuration: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayIpConfiguration", typing.Dict[str, typing.Any]]]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        sku: builtins.str,
        type: builtins.str,
        active_active: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bgp_settings: typing.Optional[typing.Union[VirtualNetworkGatewayBgpSettings, typing.Dict[str, typing.Any]]] = None,
        custom_route: typing.Optional[typing.Union["VirtualNetworkGatewayCustomRoute", typing.Dict[str, typing.Any]]] = None,
        default_local_network_gateway_id: typing.Optional[builtins.str] = None,
        edge_zone: typing.Optional[builtins.str] = None,
        enable_bgp: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        generation: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        private_ip_address_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VirtualNetworkGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_client_configuration: typing.Optional[typing.Union["VirtualNetworkGatewayVpnClientConfiguration", typing.Dict[str, typing.Any]]] = None,
        vpn_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ip_configuration: ip_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#ip_configuration VirtualNetworkGateway#ip_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#location VirtualNetworkGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#resource_group_name VirtualNetworkGateway#resource_group_name}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#sku VirtualNetworkGateway#sku}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#type VirtualNetworkGateway#type}.
        :param active_active: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#active_active VirtualNetworkGateway#active_active}.
        :param bgp_settings: bgp_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#bgp_settings VirtualNetworkGateway#bgp_settings}
        :param custom_route: custom_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#custom_route VirtualNetworkGateway#custom_route}
        :param default_local_network_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#default_local_network_gateway_id VirtualNetworkGateway#default_local_network_gateway_id}.
        :param edge_zone: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#edge_zone VirtualNetworkGateway#edge_zone}.
        :param enable_bgp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#enable_bgp VirtualNetworkGateway#enable_bgp}.
        :param generation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#generation VirtualNetworkGateway#generation}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#id VirtualNetworkGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param private_ip_address_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#private_ip_address_enabled VirtualNetworkGateway#private_ip_address_enabled}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#tags VirtualNetworkGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#timeouts VirtualNetworkGateway#timeouts}
        :param vpn_client_configuration: vpn_client_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_client_configuration VirtualNetworkGateway#vpn_client_configuration}
        :param vpn_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_type VirtualNetworkGateway#vpn_type}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(bgp_settings, dict):
            bgp_settings = VirtualNetworkGatewayBgpSettings(**bgp_settings)
        if isinstance(custom_route, dict):
            custom_route = VirtualNetworkGatewayCustomRoute(**custom_route)
        if isinstance(timeouts, dict):
            timeouts = VirtualNetworkGatewayTimeouts(**timeouts)
        if isinstance(vpn_client_configuration, dict):
            vpn_client_configuration = VirtualNetworkGatewayVpnClientConfiguration(**vpn_client_configuration)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ip_configuration", value=ip_configuration, expected_type=type_hints["ip_configuration"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument active_active", value=active_active, expected_type=type_hints["active_active"])
            check_type(argname="argument bgp_settings", value=bgp_settings, expected_type=type_hints["bgp_settings"])
            check_type(argname="argument custom_route", value=custom_route, expected_type=type_hints["custom_route"])
            check_type(argname="argument default_local_network_gateway_id", value=default_local_network_gateway_id, expected_type=type_hints["default_local_network_gateway_id"])
            check_type(argname="argument edge_zone", value=edge_zone, expected_type=type_hints["edge_zone"])
            check_type(argname="argument enable_bgp", value=enable_bgp, expected_type=type_hints["enable_bgp"])
            check_type(argname="argument generation", value=generation, expected_type=type_hints["generation"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument private_ip_address_enabled", value=private_ip_address_enabled, expected_type=type_hints["private_ip_address_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpn_client_configuration", value=vpn_client_configuration, expected_type=type_hints["vpn_client_configuration"])
            check_type(argname="argument vpn_type", value=vpn_type, expected_type=type_hints["vpn_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_configuration": ip_configuration,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "sku": sku,
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
        if active_active is not None:
            self._values["active_active"] = active_active
        if bgp_settings is not None:
            self._values["bgp_settings"] = bgp_settings
        if custom_route is not None:
            self._values["custom_route"] = custom_route
        if default_local_network_gateway_id is not None:
            self._values["default_local_network_gateway_id"] = default_local_network_gateway_id
        if edge_zone is not None:
            self._values["edge_zone"] = edge_zone
        if enable_bgp is not None:
            self._values["enable_bgp"] = enable_bgp
        if generation is not None:
            self._values["generation"] = generation
        if id is not None:
            self._values["id"] = id
        if private_ip_address_enabled is not None:
            self._values["private_ip_address_enabled"] = private_ip_address_enabled
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpn_client_configuration is not None:
            self._values["vpn_client_configuration"] = vpn_client_configuration
        if vpn_type is not None:
            self._values["vpn_type"] = vpn_type

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
    def ip_configuration(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]]:
        '''ip_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#ip_configuration VirtualNetworkGateway#ip_configuration}
        '''
        result = self._values.get("ip_configuration")
        assert result is not None, "Required property 'ip_configuration' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayIpConfiguration"]], result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#location VirtualNetworkGateway#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#resource_group_name VirtualNetworkGateway#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sku(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#sku VirtualNetworkGateway#sku}.'''
        result = self._values.get("sku")
        assert result is not None, "Required property 'sku' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#type VirtualNetworkGateway#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_active(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#active_active VirtualNetworkGateway#active_active}.'''
        result = self._values.get("active_active")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def bgp_settings(self) -> typing.Optional[VirtualNetworkGatewayBgpSettings]:
        '''bgp_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#bgp_settings VirtualNetworkGateway#bgp_settings}
        '''
        result = self._values.get("bgp_settings")
        return typing.cast(typing.Optional[VirtualNetworkGatewayBgpSettings], result)

    @builtins.property
    def custom_route(self) -> typing.Optional["VirtualNetworkGatewayCustomRoute"]:
        '''custom_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#custom_route VirtualNetworkGateway#custom_route}
        '''
        result = self._values.get("custom_route")
        return typing.cast(typing.Optional["VirtualNetworkGatewayCustomRoute"], result)

    @builtins.property
    def default_local_network_gateway_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#default_local_network_gateway_id VirtualNetworkGateway#default_local_network_gateway_id}.'''
        result = self._values.get("default_local_network_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edge_zone(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#edge_zone VirtualNetworkGateway#edge_zone}.'''
        result = self._values.get("edge_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_bgp(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#enable_bgp VirtualNetworkGateway#enable_bgp}.'''
        result = self._values.get("enable_bgp")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def generation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#generation VirtualNetworkGateway#generation}.'''
        result = self._values.get("generation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#id VirtualNetworkGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_address_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#private_ip_address_enabled VirtualNetworkGateway#private_ip_address_enabled}.'''
        result = self._values.get("private_ip_address_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#tags VirtualNetworkGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualNetworkGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#timeouts VirtualNetworkGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualNetworkGatewayTimeouts"], result)

    @builtins.property
    def vpn_client_configuration(
        self,
    ) -> typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"]:
        '''vpn_client_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_client_configuration VirtualNetworkGateway#vpn_client_configuration}
        '''
        result = self._values.get("vpn_client_configuration")
        return typing.cast(typing.Optional["VirtualNetworkGatewayVpnClientConfiguration"], result)

    @builtins.property
    def vpn_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_type VirtualNetworkGateway#vpn_type}.'''
        result = self._values.get("vpn_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayCustomRoute",
    jsii_struct_bases=[],
    name_mapping={"address_prefixes": "addressPrefixes"},
)
class VirtualNetworkGatewayCustomRoute:
    def __init__(
        self,
        *,
        address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#address_prefixes VirtualNetworkGateway#address_prefixes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayCustomRoute.__init__)
            check_type(argname="argument address_prefixes", value=address_prefixes, expected_type=type_hints["address_prefixes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if address_prefixes is not None:
            self._values["address_prefixes"] = address_prefixes

    @builtins.property
    def address_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#address_prefixes VirtualNetworkGateway#address_prefixes}.'''
        result = self._values.get("address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayCustomRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayCustomRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayCustomRouteOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayCustomRouteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAddressPrefixes")
    def reset_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressPrefixes", []))

    @builtins.property
    @jsii.member(jsii_name="addressPrefixesInput")
    def address_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="addressPrefixes")
    def address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addressPrefixes"))

    @address_prefixes.setter
    def address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayCustomRouteOutputReference, "address_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualNetworkGatewayCustomRoute]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayCustomRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayCustomRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayCustomRouteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayIpConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "public_ip_address_id": "publicIpAddressId",
        "subnet_id": "subnetId",
        "name": "name",
        "private_ip_address_allocation": "privateIpAddressAllocation",
    },
)
class VirtualNetworkGatewayIpConfiguration:
    def __init__(
        self,
        *,
        public_ip_address_id: builtins.str,
        subnet_id: builtins.str,
        name: typing.Optional[builtins.str] = None,
        private_ip_address_allocation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param public_ip_address_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#public_ip_address_id VirtualNetworkGateway#public_ip_address_id}.
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#subnet_id VirtualNetworkGateway#subnet_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param private_ip_address_allocation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#private_ip_address_allocation VirtualNetworkGateway#private_ip_address_allocation}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayIpConfiguration.__init__)
            check_type(argname="argument public_ip_address_id", value=public_ip_address_id, expected_type=type_hints["public_ip_address_id"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument private_ip_address_allocation", value=private_ip_address_allocation, expected_type=type_hints["private_ip_address_allocation"])
        self._values: typing.Dict[str, typing.Any] = {
            "public_ip_address_id": public_ip_address_id,
            "subnet_id": subnet_id,
        }
        if name is not None:
            self._values["name"] = name
        if private_ip_address_allocation is not None:
            self._values["private_ip_address_allocation"] = private_ip_address_allocation

    @builtins.property
    def public_ip_address_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#public_ip_address_id VirtualNetworkGateway#public_ip_address_id}.'''
        result = self._values.get("public_ip_address_id")
        assert result is not None, "Required property 'public_ip_address_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#subnet_id VirtualNetworkGateway#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_ip_address_allocation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#private_ip_address_allocation VirtualNetworkGateway#private_ip_address_allocation}.'''
        result = self._values.get("private_ip_address_allocation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayIpConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayIpConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayIpConfigurationList",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayIpConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayIpConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayIpConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayIpConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayIpConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayIpConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayIpConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayIpConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayIpConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayIpConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPrivateIpAddressAllocation")
    def reset_private_ip_address_allocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateIpAddressAllocation", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocationInput")
    def private_ip_address_allocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateIpAddressAllocationInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressIdInput")
    def public_ip_address_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicIpAddressIdInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="privateIpAddressAllocation")
    def private_ip_address_allocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateIpAddressAllocation"))

    @private_ip_address_allocation.setter
    def private_ip_address_allocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationOutputReference, "private_ip_address_allocation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateIpAddressAllocation", value)

    @builtins.property
    @jsii.member(jsii_name="publicIpAddressId")
    def public_ip_address_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicIpAddressId"))

    @public_ip_address_id.setter
    def public_ip_address_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationOutputReference, "public_ip_address_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIpAddressId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayIpConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayIpConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayIpConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayIpConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualNetworkGatewayTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#create VirtualNetworkGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#delete VirtualNetworkGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#read VirtualNetworkGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#update VirtualNetworkGateway#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#create VirtualNetworkGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#delete VirtualNetworkGateway#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#read VirtualNetworkGateway#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#update VirtualNetworkGateway#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "address_space": "addressSpace",
        "aad_audience": "aadAudience",
        "aad_issuer": "aadIssuer",
        "aad_tenant": "aadTenant",
        "radius_server_address": "radiusServerAddress",
        "radius_server_secret": "radiusServerSecret",
        "revoked_certificate": "revokedCertificate",
        "root_certificate": "rootCertificate",
        "vpn_auth_types": "vpnAuthTypes",
        "vpn_client_protocols": "vpnClientProtocols",
    },
)
class VirtualNetworkGatewayVpnClientConfiguration:
    def __init__(
        self,
        *,
        address_space: typing.Sequence[builtins.str],
        aad_audience: typing.Optional[builtins.str] = None,
        aad_issuer: typing.Optional[builtins.str] = None,
        aad_tenant: typing.Optional[builtins.str] = None,
        radius_server_address: typing.Optional[builtins.str] = None,
        radius_server_secret: typing.Optional[builtins.str] = None,
        revoked_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate", typing.Dict[str, typing.Any]]]]] = None,
        root_certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRootCertificate", typing.Dict[str, typing.Any]]]]] = None,
        vpn_auth_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        vpn_client_protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param address_space: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#address_space VirtualNetworkGateway#address_space}.
        :param aad_audience: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_audience VirtualNetworkGateway#aad_audience}.
        :param aad_issuer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_issuer VirtualNetworkGateway#aad_issuer}.
        :param aad_tenant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_tenant VirtualNetworkGateway#aad_tenant}.
        :param radius_server_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#radius_server_address VirtualNetworkGateway#radius_server_address}.
        :param radius_server_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#radius_server_secret VirtualNetworkGateway#radius_server_secret}.
        :param revoked_certificate: revoked_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#revoked_certificate VirtualNetworkGateway#revoked_certificate}
        :param root_certificate: root_certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#root_certificate VirtualNetworkGateway#root_certificate}
        :param vpn_auth_types: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_auth_types VirtualNetworkGateway#vpn_auth_types}.
        :param vpn_client_protocols: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_client_protocols VirtualNetworkGateway#vpn_client_protocols}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfiguration.__init__)
            check_type(argname="argument address_space", value=address_space, expected_type=type_hints["address_space"])
            check_type(argname="argument aad_audience", value=aad_audience, expected_type=type_hints["aad_audience"])
            check_type(argname="argument aad_issuer", value=aad_issuer, expected_type=type_hints["aad_issuer"])
            check_type(argname="argument aad_tenant", value=aad_tenant, expected_type=type_hints["aad_tenant"])
            check_type(argname="argument radius_server_address", value=radius_server_address, expected_type=type_hints["radius_server_address"])
            check_type(argname="argument radius_server_secret", value=radius_server_secret, expected_type=type_hints["radius_server_secret"])
            check_type(argname="argument revoked_certificate", value=revoked_certificate, expected_type=type_hints["revoked_certificate"])
            check_type(argname="argument root_certificate", value=root_certificate, expected_type=type_hints["root_certificate"])
            check_type(argname="argument vpn_auth_types", value=vpn_auth_types, expected_type=type_hints["vpn_auth_types"])
            check_type(argname="argument vpn_client_protocols", value=vpn_client_protocols, expected_type=type_hints["vpn_client_protocols"])
        self._values: typing.Dict[str, typing.Any] = {
            "address_space": address_space,
        }
        if aad_audience is not None:
            self._values["aad_audience"] = aad_audience
        if aad_issuer is not None:
            self._values["aad_issuer"] = aad_issuer
        if aad_tenant is not None:
            self._values["aad_tenant"] = aad_tenant
        if radius_server_address is not None:
            self._values["radius_server_address"] = radius_server_address
        if radius_server_secret is not None:
            self._values["radius_server_secret"] = radius_server_secret
        if revoked_certificate is not None:
            self._values["revoked_certificate"] = revoked_certificate
        if root_certificate is not None:
            self._values["root_certificate"] = root_certificate
        if vpn_auth_types is not None:
            self._values["vpn_auth_types"] = vpn_auth_types
        if vpn_client_protocols is not None:
            self._values["vpn_client_protocols"] = vpn_client_protocols

    @builtins.property
    def address_space(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#address_space VirtualNetworkGateway#address_space}.'''
        result = self._values.get("address_space")
        assert result is not None, "Required property 'address_space' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def aad_audience(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_audience VirtualNetworkGateway#aad_audience}.'''
        result = self._values.get("aad_audience")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aad_issuer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_issuer VirtualNetworkGateway#aad_issuer}.'''
        result = self._values.get("aad_issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def aad_tenant(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#aad_tenant VirtualNetworkGateway#aad_tenant}.'''
        result = self._values.get("aad_tenant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def radius_server_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#radius_server_address VirtualNetworkGateway#radius_server_address}.'''
        result = self._values.get("radius_server_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def radius_server_secret(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#radius_server_secret VirtualNetworkGateway#radius_server_secret}.'''
        result = self._values.get("radius_server_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def revoked_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]]:
        '''revoked_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#revoked_certificate VirtualNetworkGateway#revoked_certificate}
        '''
        result = self._values.get("revoked_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]], result)

    @builtins.property
    def root_certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]]:
        '''root_certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#root_certificate VirtualNetworkGateway#root_certificate}
        '''
        result = self._values.get("root_certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]], result)

    @builtins.property
    def vpn_auth_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_auth_types VirtualNetworkGateway#vpn_auth_types}.'''
        result = self._values.get("vpn_auth_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vpn_client_protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#vpn_client_protocols VirtualNetworkGateway#vpn_client_protocols}.'''
        result = self._values.get("vpn_client_protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayVpnClientConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayVpnClientConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRevokedCertificate")
    def put_revoked_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationOutputReference.put_revoked_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRevokedCertificate", [value]))

    @jsii.member(jsii_name="putRootCertificate")
    def put_root_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualNetworkGatewayVpnClientConfigurationRootCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationOutputReference.put_root_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRootCertificate", [value]))

    @jsii.member(jsii_name="resetAadAudience")
    def reset_aad_audience(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAadAudience", []))

    @jsii.member(jsii_name="resetAadIssuer")
    def reset_aad_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAadIssuer", []))

    @jsii.member(jsii_name="resetAadTenant")
    def reset_aad_tenant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAadTenant", []))

    @jsii.member(jsii_name="resetRadiusServerAddress")
    def reset_radius_server_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadiusServerAddress", []))

    @jsii.member(jsii_name="resetRadiusServerSecret")
    def reset_radius_server_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadiusServerSecret", []))

    @jsii.member(jsii_name="resetRevokedCertificate")
    def reset_revoked_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevokedCertificate", []))

    @jsii.member(jsii_name="resetRootCertificate")
    def reset_root_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRootCertificate", []))

    @jsii.member(jsii_name="resetVpnAuthTypes")
    def reset_vpn_auth_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnAuthTypes", []))

    @jsii.member(jsii_name="resetVpnClientProtocols")
    def reset_vpn_client_protocols(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnClientProtocols", []))

    @builtins.property
    @jsii.member(jsii_name="revokedCertificate")
    def revoked_certificate(
        self,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList":
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList", jsii.get(self, "revokedCertificate"))

    @builtins.property
    @jsii.member(jsii_name="rootCertificate")
    def root_certificate(
        self,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRootCertificateList":
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRootCertificateList", jsii.get(self, "rootCertificate"))

    @builtins.property
    @jsii.member(jsii_name="aadAudienceInput")
    def aad_audience_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aadAudienceInput"))

    @builtins.property
    @jsii.member(jsii_name="aadIssuerInput")
    def aad_issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aadIssuerInput"))

    @builtins.property
    @jsii.member(jsii_name="aadTenantInput")
    def aad_tenant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aadTenantInput"))

    @builtins.property
    @jsii.member(jsii_name="addressSpaceInput")
    def address_space_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressSpaceInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusServerAddressInput")
    def radius_server_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radiusServerAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="radiusServerSecretInput")
    def radius_server_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radiusServerSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="revokedCertificateInput")
    def revoked_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate"]]], jsii.get(self, "revokedCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="rootCertificateInput")
    def root_certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualNetworkGatewayVpnClientConfigurationRootCertificate"]]], jsii.get(self, "rootCertificateInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnAuthTypesInput")
    def vpn_auth_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpnAuthTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientProtocolsInput")
    def vpn_client_protocols_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpnClientProtocolsInput"))

    @builtins.property
    @jsii.member(jsii_name="aadAudience")
    def aad_audience(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aadAudience"))

    @aad_audience.setter
    def aad_audience(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "aad_audience").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aadAudience", value)

    @builtins.property
    @jsii.member(jsii_name="aadIssuer")
    def aad_issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aadIssuer"))

    @aad_issuer.setter
    def aad_issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "aad_issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aadIssuer", value)

    @builtins.property
    @jsii.member(jsii_name="aadTenant")
    def aad_tenant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aadTenant"))

    @aad_tenant.setter
    def aad_tenant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "aad_tenant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aadTenant", value)

    @builtins.property
    @jsii.member(jsii_name="addressSpace")
    def address_space(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addressSpace"))

    @address_space.setter
    def address_space(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "address_space").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressSpace", value)

    @builtins.property
    @jsii.member(jsii_name="radiusServerAddress")
    def radius_server_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radiusServerAddress"))

    @radius_server_address.setter
    def radius_server_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "radius_server_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusServerAddress", value)

    @builtins.property
    @jsii.member(jsii_name="radiusServerSecret")
    def radius_server_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radiusServerSecret"))

    @radius_server_secret.setter
    def radius_server_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "radius_server_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radiusServerSecret", value)

    @builtins.property
    @jsii.member(jsii_name="vpnAuthTypes")
    def vpn_auth_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpnAuthTypes"))

    @vpn_auth_types.setter
    def vpn_auth_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "vpn_auth_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnAuthTypes", value)

    @builtins.property
    @jsii.member(jsii_name="vpnClientProtocols")
    def vpn_client_protocols(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpnClientProtocols"))

    @vpn_client_protocols.setter
    def vpn_client_protocols(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "vpn_client_protocols").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnClientProtocols", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualNetworkGatewayVpnClientConfiguration]:
        return typing.cast(typing.Optional[VirtualNetworkGatewayVpnClientConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualNetworkGatewayVpnClientConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "thumbprint": "thumbprint"},
)
class VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate:
    def __init__(self, *, name: builtins.str, thumbprint: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param thumbprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#thumbprint VirtualNetworkGateway#thumbprint}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "thumbprint": thumbprint,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thumbprint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#thumbprint VirtualNetworkGateway#thumbprint}.'''
        result = self._values.get("thumbprint")
        assert result is not None, "Required property 'thumbprint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRootCertificate",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "public_cert_data": "publicCertData"},
)
class VirtualNetworkGatewayVpnClientConfigurationRootCertificate:
    def __init__(self, *, name: builtins.str, public_cert_data: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.
        :param public_cert_data: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#public_cert_data VirtualNetworkGateway#public_cert_data}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRootCertificate.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument public_cert_data", value=public_cert_data, expected_type=type_hints["public_cert_data"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "public_cert_data": public_cert_data,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#name VirtualNetworkGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_cert_data(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_network_gateway#public_cert_data VirtualNetworkGateway#public_cert_data}.'''
        result = self._values.get("public_cert_data")
        assert result is not None, "Required property 'public_cert_data' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNetworkGatewayVpnClientConfigurationRootCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualNetworkGatewayVpnClientConfigurationRootCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRootCertificateList",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRootCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRootCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRootCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRootCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRootCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRootCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRootCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualNetworkGatewayVpnClientConfigurationRootCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRootCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualNetworkGateway.VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference",
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
            type_hints = typing.get_type_hints(VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicCertDataInput")
    def public_cert_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicCertDataInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publicCertData")
    def public_cert_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicCertData"))

    @public_cert_data.setter
    def public_cert_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference, "public_cert_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicCertData", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualNetworkGatewayVpnClientConfigurationRootCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualNetworkGateway",
    "VirtualNetworkGatewayBgpSettings",
    "VirtualNetworkGatewayBgpSettingsOutputReference",
    "VirtualNetworkGatewayBgpSettingsPeeringAddresses",
    "VirtualNetworkGatewayBgpSettingsPeeringAddressesList",
    "VirtualNetworkGatewayBgpSettingsPeeringAddressesOutputReference",
    "VirtualNetworkGatewayConfig",
    "VirtualNetworkGatewayCustomRoute",
    "VirtualNetworkGatewayCustomRouteOutputReference",
    "VirtualNetworkGatewayIpConfiguration",
    "VirtualNetworkGatewayIpConfigurationList",
    "VirtualNetworkGatewayIpConfigurationOutputReference",
    "VirtualNetworkGatewayTimeouts",
    "VirtualNetworkGatewayTimeoutsOutputReference",
    "VirtualNetworkGatewayVpnClientConfiguration",
    "VirtualNetworkGatewayVpnClientConfigurationOutputReference",
    "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificate",
    "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateList",
    "VirtualNetworkGatewayVpnClientConfigurationRevokedCertificateOutputReference",
    "VirtualNetworkGatewayVpnClientConfigurationRootCertificate",
    "VirtualNetworkGatewayVpnClientConfigurationRootCertificateList",
    "VirtualNetworkGatewayVpnClientConfigurationRootCertificateOutputReference",
]

publication.publish()
