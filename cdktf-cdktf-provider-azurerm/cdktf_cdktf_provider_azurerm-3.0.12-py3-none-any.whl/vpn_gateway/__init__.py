'''
# `azurerm_vpn_gateway`

Refer to the Terraform Registory for docs: [`azurerm_vpn_gateway`](https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway).
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


class VpnGateway(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway azurerm_vpn_gateway}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        virtual_hub_id: builtins.str,
        bgp_route_translation_for_nat_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bgp_settings: typing.Optional[typing.Union["VpnGatewayBgpSettings", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        routing_preference: typing.Optional[builtins.str] = None,
        scale_unit: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpnGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway azurerm_vpn_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#location VpnGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#name VpnGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#resource_group_name VpnGateway#resource_group_name}.
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#virtual_hub_id VpnGateway#virtual_hub_id}.
        :param bgp_route_translation_for_nat_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#bgp_route_translation_for_nat_enabled VpnGateway#bgp_route_translation_for_nat_enabled}.
        :param bgp_settings: bgp_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#bgp_settings VpnGateway#bgp_settings}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#id VpnGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param routing_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#routing_preference VpnGateway#routing_preference}.
        :param scale_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#scale_unit VpnGateway#scale_unit}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#tags VpnGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#timeouts VpnGateway#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGateway.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VpnGatewayConfig(
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            virtual_hub_id=virtual_hub_id,
            bgp_route_translation_for_nat_enabled=bgp_route_translation_for_nat_enabled,
            bgp_settings=bgp_settings,
            id=id,
            routing_preference=routing_preference,
            scale_unit=scale_unit,
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

    @jsii.member(jsii_name="putBgpSettings")
    def put_bgp_settings(
        self,
        *,
        asn: jsii.Number,
        peer_weight: jsii.Number,
        instance0_bgp_peering_address: typing.Optional[typing.Union["VpnGatewayBgpSettingsInstance0BgpPeeringAddress", typing.Dict[str, typing.Any]]] = None,
        instance1_bgp_peering_address: typing.Optional[typing.Union["VpnGatewayBgpSettingsInstance1BgpPeeringAddress", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#asn VpnGateway#asn}.
        :param peer_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#peer_weight VpnGateway#peer_weight}.
        :param instance0_bgp_peering_address: instance_0_bgp_peering_address block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#instance_0_bgp_peering_address VpnGateway#instance_0_bgp_peering_address}
        :param instance1_bgp_peering_address: instance_1_bgp_peering_address block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#instance_1_bgp_peering_address VpnGateway#instance_1_bgp_peering_address}
        '''
        value = VpnGatewayBgpSettings(
            asn=asn,
            peer_weight=peer_weight,
            instance0_bgp_peering_address=instance0_bgp_peering_address,
            instance1_bgp_peering_address=instance1_bgp_peering_address,
        )

        return typing.cast(None, jsii.invoke(self, "putBgpSettings", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#create VpnGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#delete VpnGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#read VpnGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#update VpnGateway#update}.
        '''
        value = VpnGatewayTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetBgpRouteTranslationForNatEnabled")
    def reset_bgp_route_translation_for_nat_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgpRouteTranslationForNatEnabled", []))

    @jsii.member(jsii_name="resetBgpSettings")
    def reset_bgp_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgpSettings", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRoutingPreference")
    def reset_routing_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutingPreference", []))

    @jsii.member(jsii_name="resetScaleUnit")
    def reset_scale_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleUnit", []))

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
    @jsii.member(jsii_name="bgpSettings")
    def bgp_settings(self) -> "VpnGatewayBgpSettingsOutputReference":
        return typing.cast("VpnGatewayBgpSettingsOutputReference", jsii.get(self, "bgpSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VpnGatewayTimeoutsOutputReference":
        return typing.cast("VpnGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="bgpRouteTranslationForNatEnabledInput")
    def bgp_route_translation_for_nat_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bgpRouteTranslationForNatEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="bgpSettingsInput")
    def bgp_settings_input(self) -> typing.Optional["VpnGatewayBgpSettings"]:
        return typing.cast(typing.Optional["VpnGatewayBgpSettings"], jsii.get(self, "bgpSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="routingPreferenceInput")
    def routing_preference_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routingPreferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleUnitInput")
    def scale_unit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "scaleUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VpnGatewayTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VpnGatewayTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualHubIdInput")
    def virtual_hub_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualHubIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bgpRouteTranslationForNatEnabled")
    def bgp_route_translation_for_nat_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bgpRouteTranslationForNatEnabled"))

    @bgp_route_translation_for_nat_enabled.setter
    def bgp_route_translation_for_nat_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "bgp_route_translation_for_nat_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpRouteTranslationForNatEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="routingPreference")
    def routing_preference(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routingPreference"))

    @routing_preference.setter
    def routing_preference(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "routing_preference").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingPreference", value)

    @builtins.property
    @jsii.member(jsii_name="scaleUnit")
    def scale_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleUnit"))

    @scale_unit.setter
    def scale_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "scale_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleUnit", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualHubId")
    def virtual_hub_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualHubId"))

    @virtual_hub_id.setter
    def virtual_hub_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGateway, "virtual_hub_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualHubId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayBgpSettings",
    jsii_struct_bases=[],
    name_mapping={
        "asn": "asn",
        "peer_weight": "peerWeight",
        "instance0_bgp_peering_address": "instance0BgpPeeringAddress",
        "instance1_bgp_peering_address": "instance1BgpPeeringAddress",
    },
)
class VpnGatewayBgpSettings:
    def __init__(
        self,
        *,
        asn: jsii.Number,
        peer_weight: jsii.Number,
        instance0_bgp_peering_address: typing.Optional[typing.Union["VpnGatewayBgpSettingsInstance0BgpPeeringAddress", typing.Dict[str, typing.Any]]] = None,
        instance1_bgp_peering_address: typing.Optional[typing.Union["VpnGatewayBgpSettingsInstance1BgpPeeringAddress", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param asn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#asn VpnGateway#asn}.
        :param peer_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#peer_weight VpnGateway#peer_weight}.
        :param instance0_bgp_peering_address: instance_0_bgp_peering_address block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#instance_0_bgp_peering_address VpnGateway#instance_0_bgp_peering_address}
        :param instance1_bgp_peering_address: instance_1_bgp_peering_address block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#instance_1_bgp_peering_address VpnGateway#instance_1_bgp_peering_address}
        '''
        if isinstance(instance0_bgp_peering_address, dict):
            instance0_bgp_peering_address = VpnGatewayBgpSettingsInstance0BgpPeeringAddress(**instance0_bgp_peering_address)
        if isinstance(instance1_bgp_peering_address, dict):
            instance1_bgp_peering_address = VpnGatewayBgpSettingsInstance1BgpPeeringAddress(**instance1_bgp_peering_address)
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayBgpSettings.__init__)
            check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
            check_type(argname="argument peer_weight", value=peer_weight, expected_type=type_hints["peer_weight"])
            check_type(argname="argument instance0_bgp_peering_address", value=instance0_bgp_peering_address, expected_type=type_hints["instance0_bgp_peering_address"])
            check_type(argname="argument instance1_bgp_peering_address", value=instance1_bgp_peering_address, expected_type=type_hints["instance1_bgp_peering_address"])
        self._values: typing.Dict[str, typing.Any] = {
            "asn": asn,
            "peer_weight": peer_weight,
        }
        if instance0_bgp_peering_address is not None:
            self._values["instance0_bgp_peering_address"] = instance0_bgp_peering_address
        if instance1_bgp_peering_address is not None:
            self._values["instance1_bgp_peering_address"] = instance1_bgp_peering_address

    @builtins.property
    def asn(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#asn VpnGateway#asn}.'''
        result = self._values.get("asn")
        assert result is not None, "Required property 'asn' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def peer_weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#peer_weight VpnGateway#peer_weight}.'''
        result = self._values.get("peer_weight")
        assert result is not None, "Required property 'peer_weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def instance0_bgp_peering_address(
        self,
    ) -> typing.Optional["VpnGatewayBgpSettingsInstance0BgpPeeringAddress"]:
        '''instance_0_bgp_peering_address block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#instance_0_bgp_peering_address VpnGateway#instance_0_bgp_peering_address}
        '''
        result = self._values.get("instance0_bgp_peering_address")
        return typing.cast(typing.Optional["VpnGatewayBgpSettingsInstance0BgpPeeringAddress"], result)

    @builtins.property
    def instance1_bgp_peering_address(
        self,
    ) -> typing.Optional["VpnGatewayBgpSettingsInstance1BgpPeeringAddress"]:
        '''instance_1_bgp_peering_address block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#instance_1_bgp_peering_address VpnGateway#instance_1_bgp_peering_address}
        '''
        result = self._values.get("instance1_bgp_peering_address")
        return typing.cast(typing.Optional["VpnGatewayBgpSettingsInstance1BgpPeeringAddress"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayBgpSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayBgpSettingsInstance0BgpPeeringAddress",
    jsii_struct_bases=[],
    name_mapping={"custom_ips": "customIps"},
)
class VpnGatewayBgpSettingsInstance0BgpPeeringAddress:
    def __init__(self, *, custom_ips: typing.Sequence[builtins.str]) -> None:
        '''
        :param custom_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#custom_ips VpnGateway#custom_ips}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayBgpSettingsInstance0BgpPeeringAddress.__init__)
            check_type(argname="argument custom_ips", value=custom_ips, expected_type=type_hints["custom_ips"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_ips": custom_ips,
        }

    @builtins.property
    def custom_ips(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#custom_ips VpnGateway#custom_ips}.'''
        result = self._values.get("custom_ips")
        assert result is not None, "Required property 'custom_ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayBgpSettingsInstance0BgpPeeringAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultIps")
    def default_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultIps"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationId")
    def ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="tunnelIps")
    def tunnel_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnelIps"))

    @builtins.property
    @jsii.member(jsii_name="customIpsInput")
    def custom_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="customIps")
    def custom_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customIps"))

    @custom_ips.setter
    def custom_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference, "custom_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customIps", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VpnGatewayBgpSettingsInstance0BgpPeeringAddress]:
        return typing.cast(typing.Optional[VpnGatewayBgpSettingsInstance0BgpPeeringAddress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnGatewayBgpSettingsInstance0BgpPeeringAddress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayBgpSettingsInstance1BgpPeeringAddress",
    jsii_struct_bases=[],
    name_mapping={"custom_ips": "customIps"},
)
class VpnGatewayBgpSettingsInstance1BgpPeeringAddress:
    def __init__(self, *, custom_ips: typing.Sequence[builtins.str]) -> None:
        '''
        :param custom_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#custom_ips VpnGateway#custom_ips}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayBgpSettingsInstance1BgpPeeringAddress.__init__)
            check_type(argname="argument custom_ips", value=custom_ips, expected_type=type_hints["custom_ips"])
        self._values: typing.Dict[str, typing.Any] = {
            "custom_ips": custom_ips,
        }

    @builtins.property
    def custom_ips(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#custom_ips VpnGateway#custom_ips}.'''
        result = self._values.get("custom_ips")
        assert result is not None, "Required property 'custom_ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayBgpSettingsInstance1BgpPeeringAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultIps")
    def default_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultIps"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationId")
    def ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="tunnelIps")
    def tunnel_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tunnelIps"))

    @builtins.property
    @jsii.member(jsii_name="customIpsInput")
    def custom_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "customIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="customIps")
    def custom_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "customIps"))

    @custom_ips.setter
    def custom_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference, "custom_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customIps", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VpnGatewayBgpSettingsInstance1BgpPeeringAddress]:
        return typing.cast(typing.Optional[VpnGatewayBgpSettingsInstance1BgpPeeringAddress], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnGatewayBgpSettingsInstance1BgpPeeringAddress],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnGatewayBgpSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayBgpSettingsOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayBgpSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putInstance0BgpPeeringAddress")
    def put_instance0_bgp_peering_address(
        self,
        *,
        custom_ips: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param custom_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#custom_ips VpnGateway#custom_ips}.
        '''
        value = VpnGatewayBgpSettingsInstance0BgpPeeringAddress(custom_ips=custom_ips)

        return typing.cast(None, jsii.invoke(self, "putInstance0BgpPeeringAddress", [value]))

    @jsii.member(jsii_name="putInstance1BgpPeeringAddress")
    def put_instance1_bgp_peering_address(
        self,
        *,
        custom_ips: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param custom_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#custom_ips VpnGateway#custom_ips}.
        '''
        value = VpnGatewayBgpSettingsInstance1BgpPeeringAddress(custom_ips=custom_ips)

        return typing.cast(None, jsii.invoke(self, "putInstance1BgpPeeringAddress", [value]))

    @jsii.member(jsii_name="resetInstance0BgpPeeringAddress")
    def reset_instance0_bgp_peering_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstance0BgpPeeringAddress", []))

    @jsii.member(jsii_name="resetInstance1BgpPeeringAddress")
    def reset_instance1_bgp_peering_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstance1BgpPeeringAddress", []))

    @builtins.property
    @jsii.member(jsii_name="bgpPeeringAddress")
    def bgp_peering_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bgpPeeringAddress"))

    @builtins.property
    @jsii.member(jsii_name="instance0BgpPeeringAddress")
    def instance0_bgp_peering_address(
        self,
    ) -> VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference:
        return typing.cast(VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference, jsii.get(self, "instance0BgpPeeringAddress"))

    @builtins.property
    @jsii.member(jsii_name="instance1BgpPeeringAddress")
    def instance1_bgp_peering_address(
        self,
    ) -> VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference:
        return typing.cast(VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference, jsii.get(self, "instance1BgpPeeringAddress"))

    @builtins.property
    @jsii.member(jsii_name="asnInput")
    def asn_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "asnInput"))

    @builtins.property
    @jsii.member(jsii_name="instance0BgpPeeringAddressInput")
    def instance0_bgp_peering_address_input(
        self,
    ) -> typing.Optional[VpnGatewayBgpSettingsInstance0BgpPeeringAddress]:
        return typing.cast(typing.Optional[VpnGatewayBgpSettingsInstance0BgpPeeringAddress], jsii.get(self, "instance0BgpPeeringAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="instance1BgpPeeringAddressInput")
    def instance1_bgp_peering_address_input(
        self,
    ) -> typing.Optional[VpnGatewayBgpSettingsInstance1BgpPeeringAddress]:
        return typing.cast(typing.Optional[VpnGatewayBgpSettingsInstance1BgpPeeringAddress], jsii.get(self, "instance1BgpPeeringAddressInput"))

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
            type_hints = typing.get_type_hints(getattr(VpnGatewayBgpSettingsOutputReference, "asn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "asn", value)

    @builtins.property
    @jsii.member(jsii_name="peerWeight")
    def peer_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "peerWeight"))

    @peer_weight.setter
    def peer_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayBgpSettingsOutputReference, "peer_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerWeight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnGatewayBgpSettings]:
        return typing.cast(typing.Optional[VpnGatewayBgpSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[VpnGatewayBgpSettings]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayBgpSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayConfig",
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
        "virtual_hub_id": "virtualHubId",
        "bgp_route_translation_for_nat_enabled": "bgpRouteTranslationForNatEnabled",
        "bgp_settings": "bgpSettings",
        "id": "id",
        "routing_preference": "routingPreference",
        "scale_unit": "scaleUnit",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class VpnGatewayConfig(cdktf.TerraformMetaArguments):
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
        virtual_hub_id: builtins.str,
        bgp_route_translation_for_nat_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bgp_settings: typing.Optional[typing.Union[VpnGatewayBgpSettings, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        routing_preference: typing.Optional[builtins.str] = None,
        scale_unit: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["VpnGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#location VpnGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#name VpnGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#resource_group_name VpnGateway#resource_group_name}.
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#virtual_hub_id VpnGateway#virtual_hub_id}.
        :param bgp_route_translation_for_nat_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#bgp_route_translation_for_nat_enabled VpnGateway#bgp_route_translation_for_nat_enabled}.
        :param bgp_settings: bgp_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#bgp_settings VpnGateway#bgp_settings}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#id VpnGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param routing_preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#routing_preference VpnGateway#routing_preference}.
        :param scale_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#scale_unit VpnGateway#scale_unit}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#tags VpnGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#timeouts VpnGateway#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(bgp_settings, dict):
            bgp_settings = VpnGatewayBgpSettings(**bgp_settings)
        if isinstance(timeouts, dict):
            timeouts = VpnGatewayTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConfig.__init__)
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
            check_type(argname="argument virtual_hub_id", value=virtual_hub_id, expected_type=type_hints["virtual_hub_id"])
            check_type(argname="argument bgp_route_translation_for_nat_enabled", value=bgp_route_translation_for_nat_enabled, expected_type=type_hints["bgp_route_translation_for_nat_enabled"])
            check_type(argname="argument bgp_settings", value=bgp_settings, expected_type=type_hints["bgp_settings"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument routing_preference", value=routing_preference, expected_type=type_hints["routing_preference"])
            check_type(argname="argument scale_unit", value=scale_unit, expected_type=type_hints["scale_unit"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "virtual_hub_id": virtual_hub_id,
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
        if bgp_route_translation_for_nat_enabled is not None:
            self._values["bgp_route_translation_for_nat_enabled"] = bgp_route_translation_for_nat_enabled
        if bgp_settings is not None:
            self._values["bgp_settings"] = bgp_settings
        if id is not None:
            self._values["id"] = id
        if routing_preference is not None:
            self._values["routing_preference"] = routing_preference
        if scale_unit is not None:
            self._values["scale_unit"] = scale_unit
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
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#location VpnGateway#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#name VpnGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#resource_group_name VpnGateway#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_hub_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#virtual_hub_id VpnGateway#virtual_hub_id}.'''
        result = self._values.get("virtual_hub_id")
        assert result is not None, "Required property 'virtual_hub_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bgp_route_translation_for_nat_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#bgp_route_translation_for_nat_enabled VpnGateway#bgp_route_translation_for_nat_enabled}.'''
        result = self._values.get("bgp_route_translation_for_nat_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def bgp_settings(self) -> typing.Optional[VpnGatewayBgpSettings]:
        '''bgp_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#bgp_settings VpnGateway#bgp_settings}
        '''
        result = self._values.get("bgp_settings")
        return typing.cast(typing.Optional[VpnGatewayBgpSettings], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#id VpnGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routing_preference(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#routing_preference VpnGateway#routing_preference}.'''
        result = self._values.get("routing_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scale_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#scale_unit VpnGateway#scale_unit}.'''
        result = self._values.get("scale_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#tags VpnGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VpnGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#timeouts VpnGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VpnGatewayTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VpnGatewayTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#create VpnGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#delete VpnGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#read VpnGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#update VpnGateway#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#create VpnGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#delete VpnGateway#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#read VpnGateway#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway#update VpnGateway#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGateway.VpnGatewayTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnGatewayTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnGatewayTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnGatewayTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpnGateway",
    "VpnGatewayBgpSettings",
    "VpnGatewayBgpSettingsInstance0BgpPeeringAddress",
    "VpnGatewayBgpSettingsInstance0BgpPeeringAddressOutputReference",
    "VpnGatewayBgpSettingsInstance1BgpPeeringAddress",
    "VpnGatewayBgpSettingsInstance1BgpPeeringAddressOutputReference",
    "VpnGatewayBgpSettingsOutputReference",
    "VpnGatewayConfig",
    "VpnGatewayTimeouts",
    "VpnGatewayTimeoutsOutputReference",
]

publication.publish()
