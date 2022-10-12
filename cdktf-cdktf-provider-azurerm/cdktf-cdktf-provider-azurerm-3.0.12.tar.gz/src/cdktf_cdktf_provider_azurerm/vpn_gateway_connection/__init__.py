'''
# `azurerm_vpn_gateway_connection`

Refer to the Terraform Registory for docs: [`azurerm_vpn_gateway_connection`](https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection).
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


class VpnGatewayConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection azurerm_vpn_gateway_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        remote_vpn_site_id: builtins.str,
        vpn_gateway_id: builtins.str,
        vpn_link: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionVpnLink", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        internet_security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        routing: typing.Optional[typing.Union["VpnGatewayConnectionRouting", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["VpnGatewayConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        traffic_selector_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionTrafficSelectorPolicy", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection azurerm_vpn_gateway_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#name VpnGatewayConnection#name}.
        :param remote_vpn_site_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#remote_vpn_site_id VpnGatewayConnection#remote_vpn_site_id}.
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_gateway_id VpnGatewayConnection#vpn_gateway_id}.
        :param vpn_link: vpn_link block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_link VpnGatewayConnection#vpn_link}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#id VpnGatewayConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_security_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#internet_security_enabled VpnGatewayConnection#internet_security_enabled}.
        :param routing: routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#routing VpnGatewayConnection#routing}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#timeouts VpnGatewayConnection#timeouts}
        :param traffic_selector_policy: traffic_selector_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#traffic_selector_policy VpnGatewayConnection#traffic_selector_policy}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VpnGatewayConnectionConfig(
            name=name,
            remote_vpn_site_id=remote_vpn_site_id,
            vpn_gateway_id=vpn_gateway_id,
            vpn_link=vpn_link,
            id=id,
            internet_security_enabled=internet_security_enabled,
            routing=routing,
            timeouts=timeouts,
            traffic_selector_policy=traffic_selector_policy,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRouting")
    def put_routing(
        self,
        *,
        associated_route_table: builtins.str,
        propagated_route_table: typing.Optional[typing.Union["VpnGatewayConnectionRoutingPropagatedRouteTable", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param associated_route_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#associated_route_table VpnGatewayConnection#associated_route_table}.
        :param propagated_route_table: propagated_route_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#propagated_route_table VpnGatewayConnection#propagated_route_table}
        '''
        value = VpnGatewayConnectionRouting(
            associated_route_table=associated_route_table,
            propagated_route_table=propagated_route_table,
        )

        return typing.cast(None, jsii.invoke(self, "putRouting", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#create VpnGatewayConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#delete VpnGatewayConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#read VpnGatewayConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#update VpnGatewayConnection#update}.
        '''
        value = VpnGatewayConnectionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTrafficSelectorPolicy")
    def put_traffic_selector_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionTrafficSelectorPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnection.put_traffic_selector_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTrafficSelectorPolicy", [value]))

    @jsii.member(jsii_name="putVpnLink")
    def put_vpn_link(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionVpnLink", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnection.put_vpn_link)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVpnLink", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInternetSecurityEnabled")
    def reset_internet_security_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternetSecurityEnabled", []))

    @jsii.member(jsii_name="resetRouting")
    def reset_routing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouting", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTrafficSelectorPolicy")
    def reset_traffic_selector_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrafficSelectorPolicy", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="routing")
    def routing(self) -> "VpnGatewayConnectionRoutingOutputReference":
        return typing.cast("VpnGatewayConnectionRoutingOutputReference", jsii.get(self, "routing"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VpnGatewayConnectionTimeoutsOutputReference":
        return typing.cast("VpnGatewayConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="trafficSelectorPolicy")
    def traffic_selector_policy(
        self,
    ) -> "VpnGatewayConnectionTrafficSelectorPolicyList":
        return typing.cast("VpnGatewayConnectionTrafficSelectorPolicyList", jsii.get(self, "trafficSelectorPolicy"))

    @builtins.property
    @jsii.member(jsii_name="vpnLink")
    def vpn_link(self) -> "VpnGatewayConnectionVpnLinkList":
        return typing.cast("VpnGatewayConnectionVpnLinkList", jsii.get(self, "vpnLink"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="internetSecurityEnabledInput")
    def internet_security_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "internetSecurityEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteVpnSiteIdInput")
    def remote_vpn_site_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteVpnSiteIdInput"))

    @builtins.property
    @jsii.member(jsii_name="routingInput")
    def routing_input(self) -> typing.Optional["VpnGatewayConnectionRouting"]:
        return typing.cast(typing.Optional["VpnGatewayConnectionRouting"], jsii.get(self, "routingInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VpnGatewayConnectionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VpnGatewayConnectionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trafficSelectorPolicyInput")
    def traffic_selector_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionTrafficSelectorPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionTrafficSelectorPolicy"]]], jsii.get(self, "trafficSelectorPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayIdInput")
    def vpn_gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnGatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnLinkInput")
    def vpn_link_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLink"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLink"]]], jsii.get(self, "vpnLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internetSecurityEnabled")
    def internet_security_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "internetSecurityEnabled"))

    @internet_security_enabled.setter
    def internet_security_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnection, "internet_security_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetSecurityEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnection, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="remoteVpnSiteId")
    def remote_vpn_site_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteVpnSiteId"))

    @remote_vpn_site_id.setter
    def remote_vpn_site_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnection, "remote_vpn_site_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteVpnSiteId", value)

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayId")
    def vpn_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnGatewayId"))

    @vpn_gateway_id.setter
    def vpn_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnection, "vpn_gateway_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnGatewayId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionConfig",
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
        "remote_vpn_site_id": "remoteVpnSiteId",
        "vpn_gateway_id": "vpnGatewayId",
        "vpn_link": "vpnLink",
        "id": "id",
        "internet_security_enabled": "internetSecurityEnabled",
        "routing": "routing",
        "timeouts": "timeouts",
        "traffic_selector_policy": "trafficSelectorPolicy",
    },
)
class VpnGatewayConnectionConfig(cdktf.TerraformMetaArguments):
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
        remote_vpn_site_id: builtins.str,
        vpn_gateway_id: builtins.str,
        vpn_link: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionVpnLink", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        internet_security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        routing: typing.Optional[typing.Union["VpnGatewayConnectionRouting", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["VpnGatewayConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        traffic_selector_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionTrafficSelectorPolicy", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#name VpnGatewayConnection#name}.
        :param remote_vpn_site_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#remote_vpn_site_id VpnGatewayConnection#remote_vpn_site_id}.
        :param vpn_gateway_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_gateway_id VpnGatewayConnection#vpn_gateway_id}.
        :param vpn_link: vpn_link block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_link VpnGatewayConnection#vpn_link}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#id VpnGatewayConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_security_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#internet_security_enabled VpnGatewayConnection#internet_security_enabled}.
        :param routing: routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#routing VpnGatewayConnection#routing}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#timeouts VpnGatewayConnection#timeouts}
        :param traffic_selector_policy: traffic_selector_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#traffic_selector_policy VpnGatewayConnection#traffic_selector_policy}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(routing, dict):
            routing = VpnGatewayConnectionRouting(**routing)
        if isinstance(timeouts, dict):
            timeouts = VpnGatewayConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument remote_vpn_site_id", value=remote_vpn_site_id, expected_type=type_hints["remote_vpn_site_id"])
            check_type(argname="argument vpn_gateway_id", value=vpn_gateway_id, expected_type=type_hints["vpn_gateway_id"])
            check_type(argname="argument vpn_link", value=vpn_link, expected_type=type_hints["vpn_link"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument internet_security_enabled", value=internet_security_enabled, expected_type=type_hints["internet_security_enabled"])
            check_type(argname="argument routing", value=routing, expected_type=type_hints["routing"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument traffic_selector_policy", value=traffic_selector_policy, expected_type=type_hints["traffic_selector_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "remote_vpn_site_id": remote_vpn_site_id,
            "vpn_gateway_id": vpn_gateway_id,
            "vpn_link": vpn_link,
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
        if internet_security_enabled is not None:
            self._values["internet_security_enabled"] = internet_security_enabled
        if routing is not None:
            self._values["routing"] = routing
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if traffic_selector_policy is not None:
            self._values["traffic_selector_policy"] = traffic_selector_policy

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#name VpnGatewayConnection#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remote_vpn_site_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#remote_vpn_site_id VpnGatewayConnection#remote_vpn_site_id}.'''
        result = self._values.get("remote_vpn_site_id")
        assert result is not None, "Required property 'remote_vpn_site_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_gateway_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_gateway_id VpnGatewayConnection#vpn_gateway_id}.'''
        result = self._values.get("vpn_gateway_id")
        assert result is not None, "Required property 'vpn_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_link(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLink"]]:
        '''vpn_link block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_link VpnGatewayConnection#vpn_link}
        '''
        result = self._values.get("vpn_link")
        assert result is not None, "Required property 'vpn_link' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLink"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#id VpnGatewayConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internet_security_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#internet_security_enabled VpnGatewayConnection#internet_security_enabled}.'''
        result = self._values.get("internet_security_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def routing(self) -> typing.Optional["VpnGatewayConnectionRouting"]:
        '''routing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#routing VpnGatewayConnection#routing}
        '''
        result = self._values.get("routing")
        return typing.cast(typing.Optional["VpnGatewayConnectionRouting"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VpnGatewayConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#timeouts VpnGatewayConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VpnGatewayConnectionTimeouts"], result)

    @builtins.property
    def traffic_selector_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionTrafficSelectorPolicy"]]]:
        '''traffic_selector_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#traffic_selector_policy VpnGatewayConnection#traffic_selector_policy}
        '''
        result = self._values.get("traffic_selector_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionTrafficSelectorPolicy"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionRouting",
    jsii_struct_bases=[],
    name_mapping={
        "associated_route_table": "associatedRouteTable",
        "propagated_route_table": "propagatedRouteTable",
    },
)
class VpnGatewayConnectionRouting:
    def __init__(
        self,
        *,
        associated_route_table: builtins.str,
        propagated_route_table: typing.Optional[typing.Union["VpnGatewayConnectionRoutingPropagatedRouteTable", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param associated_route_table: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#associated_route_table VpnGatewayConnection#associated_route_table}.
        :param propagated_route_table: propagated_route_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#propagated_route_table VpnGatewayConnection#propagated_route_table}
        '''
        if isinstance(propagated_route_table, dict):
            propagated_route_table = VpnGatewayConnectionRoutingPropagatedRouteTable(**propagated_route_table)
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionRouting.__init__)
            check_type(argname="argument associated_route_table", value=associated_route_table, expected_type=type_hints["associated_route_table"])
            check_type(argname="argument propagated_route_table", value=propagated_route_table, expected_type=type_hints["propagated_route_table"])
        self._values: typing.Dict[str, typing.Any] = {
            "associated_route_table": associated_route_table,
        }
        if propagated_route_table is not None:
            self._values["propagated_route_table"] = propagated_route_table

    @builtins.property
    def associated_route_table(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#associated_route_table VpnGatewayConnection#associated_route_table}.'''
        result = self._values.get("associated_route_table")
        assert result is not None, "Required property 'associated_route_table' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagated_route_table(
        self,
    ) -> typing.Optional["VpnGatewayConnectionRoutingPropagatedRouteTable"]:
        '''propagated_route_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#propagated_route_table VpnGatewayConnection#propagated_route_table}
        '''
        result = self._values.get("propagated_route_table")
        return typing.cast(typing.Optional["VpnGatewayConnectionRoutingPropagatedRouteTable"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionRouting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayConnectionRoutingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionRoutingOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionRoutingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPropagatedRouteTable")
    def put_propagated_route_table(
        self,
        *,
        route_table_ids: typing.Sequence[builtins.str],
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param route_table_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#route_table_ids VpnGatewayConnection#route_table_ids}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#labels VpnGatewayConnection#labels}.
        '''
        value = VpnGatewayConnectionRoutingPropagatedRouteTable(
            route_table_ids=route_table_ids, labels=labels
        )

        return typing.cast(None, jsii.invoke(self, "putPropagatedRouteTable", [value]))

    @jsii.member(jsii_name="resetPropagatedRouteTable")
    def reset_propagated_route_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagatedRouteTable", []))

    @builtins.property
    @jsii.member(jsii_name="propagatedRouteTable")
    def propagated_route_table(
        self,
    ) -> "VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference":
        return typing.cast("VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference", jsii.get(self, "propagatedRouteTable"))

    @builtins.property
    @jsii.member(jsii_name="associatedRouteTableInput")
    def associated_route_table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associatedRouteTableInput"))

    @builtins.property
    @jsii.member(jsii_name="propagatedRouteTableInput")
    def propagated_route_table_input(
        self,
    ) -> typing.Optional["VpnGatewayConnectionRoutingPropagatedRouteTable"]:
        return typing.cast(typing.Optional["VpnGatewayConnectionRoutingPropagatedRouteTable"], jsii.get(self, "propagatedRouteTableInput"))

    @builtins.property
    @jsii.member(jsii_name="associatedRouteTable")
    def associated_route_table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedRouteTable"))

    @associated_route_table.setter
    def associated_route_table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionRoutingOutputReference, "associated_route_table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedRouteTable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VpnGatewayConnectionRouting]:
        return typing.cast(typing.Optional[VpnGatewayConnectionRouting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnGatewayConnectionRouting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionRoutingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionRoutingPropagatedRouteTable",
    jsii_struct_bases=[],
    name_mapping={"route_table_ids": "routeTableIds", "labels": "labels"},
)
class VpnGatewayConnectionRoutingPropagatedRouteTable:
    def __init__(
        self,
        *,
        route_table_ids: typing.Sequence[builtins.str],
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param route_table_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#route_table_ids VpnGatewayConnection#route_table_ids}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#labels VpnGatewayConnection#labels}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionRoutingPropagatedRouteTable.__init__)
            check_type(argname="argument route_table_ids", value=route_table_ids, expected_type=type_hints["route_table_ids"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[str, typing.Any] = {
            "route_table_ids": route_table_ids,
        }
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def route_table_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#route_table_ids VpnGatewayConnection#route_table_ids}.'''
        result = self._values.get("route_table_ids")
        assert result is not None, "Required property 'route_table_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#labels VpnGatewayConnection#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionRoutingPropagatedRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="routeTableIdsInput")
    def route_table_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "routeTableIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="routeTableIds")
    def route_table_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "routeTableIds"))

    @route_table_ids.setter
    def route_table_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference, "route_table_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeTableIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VpnGatewayConnectionRoutingPropagatedRouteTable]:
        return typing.cast(typing.Optional[VpnGatewayConnectionRoutingPropagatedRouteTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VpnGatewayConnectionRoutingPropagatedRouteTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VpnGatewayConnectionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#create VpnGatewayConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#delete VpnGatewayConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#read VpnGatewayConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#update VpnGatewayConnection#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#create VpnGatewayConnection#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#delete VpnGatewayConnection#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#read VpnGatewayConnection#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#update VpnGatewayConnection#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayConnectionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnGatewayConnectionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnGatewayConnectionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnGatewayConnectionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionTrafficSelectorPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "local_address_ranges": "localAddressRanges",
        "remote_address_ranges": "remoteAddressRanges",
    },
)
class VpnGatewayConnectionTrafficSelectorPolicy:
    def __init__(
        self,
        *,
        local_address_ranges: typing.Sequence[builtins.str],
        remote_address_ranges: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param local_address_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#local_address_ranges VpnGatewayConnection#local_address_ranges}.
        :param remote_address_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#remote_address_ranges VpnGatewayConnection#remote_address_ranges}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionTrafficSelectorPolicy.__init__)
            check_type(argname="argument local_address_ranges", value=local_address_ranges, expected_type=type_hints["local_address_ranges"])
            check_type(argname="argument remote_address_ranges", value=remote_address_ranges, expected_type=type_hints["remote_address_ranges"])
        self._values: typing.Dict[str, typing.Any] = {
            "local_address_ranges": local_address_ranges,
            "remote_address_ranges": remote_address_ranges,
        }

    @builtins.property
    def local_address_ranges(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#local_address_ranges VpnGatewayConnection#local_address_ranges}.'''
        result = self._values.get("local_address_ranges")
        assert result is not None, "Required property 'local_address_ranges' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def remote_address_ranges(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#remote_address_ranges VpnGatewayConnection#remote_address_ranges}.'''
        result = self._values.get("remote_address_ranges")
        assert result is not None, "Required property 'remote_address_ranges' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionTrafficSelectorPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayConnectionTrafficSelectorPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionTrafficSelectorPolicyList",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionTrafficSelectorPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnGatewayConnectionTrafficSelectorPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionTrafficSelectorPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnGatewayConnectionTrafficSelectorPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTrafficSelectorPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTrafficSelectorPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTrafficSelectorPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionTrafficSelectorPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionTrafficSelectorPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionTrafficSelectorPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTrafficSelectorPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnGatewayConnectionTrafficSelectorPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionTrafficSelectorPolicyOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionTrafficSelectorPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="localAddressRangesInput")
    def local_address_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "localAddressRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="remoteAddressRangesInput")
    def remote_address_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "remoteAddressRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="localAddressRanges")
    def local_address_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "localAddressRanges"))

    @local_address_ranges.setter
    def local_address_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTrafficSelectorPolicyOutputReference, "local_address_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAddressRanges", value)

    @builtins.property
    @jsii.member(jsii_name="remoteAddressRanges")
    def remote_address_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "remoteAddressRanges"))

    @remote_address_ranges.setter
    def remote_address_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTrafficSelectorPolicyOutputReference, "remote_address_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteAddressRanges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnGatewayConnectionTrafficSelectorPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnGatewayConnectionTrafficSelectorPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnGatewayConnectionTrafficSelectorPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionTrafficSelectorPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLink",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "vpn_site_link_id": "vpnSiteLinkId",
        "bandwidth_mbps": "bandwidthMbps",
        "bgp_enabled": "bgpEnabled",
        "connection_mode": "connectionMode",
        "custom_bgp_address": "customBgpAddress",
        "egress_nat_rule_ids": "egressNatRuleIds",
        "ingress_nat_rule_ids": "ingressNatRuleIds",
        "ipsec_policy": "ipsecPolicy",
        "local_azure_ip_address_enabled": "localAzureIpAddressEnabled",
        "policy_based_traffic_selector_enabled": "policyBasedTrafficSelectorEnabled",
        "protocol": "protocol",
        "ratelimit_enabled": "ratelimitEnabled",
        "route_weight": "routeWeight",
        "shared_key": "sharedKey",
    },
)
class VpnGatewayConnectionVpnLink:
    def __init__(
        self,
        *,
        name: builtins.str,
        vpn_site_link_id: builtins.str,
        bandwidth_mbps: typing.Optional[jsii.Number] = None,
        bgp_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection_mode: typing.Optional[builtins.str] = None,
        custom_bgp_address: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionVpnLinkCustomBgpAddress", typing.Dict[str, typing.Any]]]]] = None,
        egress_nat_rule_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ingress_nat_rule_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ipsec_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VpnGatewayConnectionVpnLinkIpsecPolicy", typing.Dict[str, typing.Any]]]]] = None,
        local_azure_ip_address_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        policy_based_traffic_selector_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        protocol: typing.Optional[builtins.str] = None,
        ratelimit_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        route_weight: typing.Optional[jsii.Number] = None,
        shared_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#name VpnGatewayConnection#name}.
        :param vpn_site_link_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_site_link_id VpnGatewayConnection#vpn_site_link_id}.
        :param bandwidth_mbps: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#bandwidth_mbps VpnGatewayConnection#bandwidth_mbps}.
        :param bgp_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#bgp_enabled VpnGatewayConnection#bgp_enabled}.
        :param connection_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#connection_mode VpnGatewayConnection#connection_mode}.
        :param custom_bgp_address: custom_bgp_address block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#custom_bgp_address VpnGatewayConnection#custom_bgp_address}
        :param egress_nat_rule_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#egress_nat_rule_ids VpnGatewayConnection#egress_nat_rule_ids}.
        :param ingress_nat_rule_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ingress_nat_rule_ids VpnGatewayConnection#ingress_nat_rule_ids}.
        :param ipsec_policy: ipsec_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ipsec_policy VpnGatewayConnection#ipsec_policy}
        :param local_azure_ip_address_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#local_azure_ip_address_enabled VpnGatewayConnection#local_azure_ip_address_enabled}.
        :param policy_based_traffic_selector_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#policy_based_traffic_selector_enabled VpnGatewayConnection#policy_based_traffic_selector_enabled}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#protocol VpnGatewayConnection#protocol}.
        :param ratelimit_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ratelimit_enabled VpnGatewayConnection#ratelimit_enabled}.
        :param route_weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#route_weight VpnGatewayConnection#route_weight}.
        :param shared_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#shared_key VpnGatewayConnection#shared_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLink.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument vpn_site_link_id", value=vpn_site_link_id, expected_type=type_hints["vpn_site_link_id"])
            check_type(argname="argument bandwidth_mbps", value=bandwidth_mbps, expected_type=type_hints["bandwidth_mbps"])
            check_type(argname="argument bgp_enabled", value=bgp_enabled, expected_type=type_hints["bgp_enabled"])
            check_type(argname="argument connection_mode", value=connection_mode, expected_type=type_hints["connection_mode"])
            check_type(argname="argument custom_bgp_address", value=custom_bgp_address, expected_type=type_hints["custom_bgp_address"])
            check_type(argname="argument egress_nat_rule_ids", value=egress_nat_rule_ids, expected_type=type_hints["egress_nat_rule_ids"])
            check_type(argname="argument ingress_nat_rule_ids", value=ingress_nat_rule_ids, expected_type=type_hints["ingress_nat_rule_ids"])
            check_type(argname="argument ipsec_policy", value=ipsec_policy, expected_type=type_hints["ipsec_policy"])
            check_type(argname="argument local_azure_ip_address_enabled", value=local_azure_ip_address_enabled, expected_type=type_hints["local_azure_ip_address_enabled"])
            check_type(argname="argument policy_based_traffic_selector_enabled", value=policy_based_traffic_selector_enabled, expected_type=type_hints["policy_based_traffic_selector_enabled"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument ratelimit_enabled", value=ratelimit_enabled, expected_type=type_hints["ratelimit_enabled"])
            check_type(argname="argument route_weight", value=route_weight, expected_type=type_hints["route_weight"])
            check_type(argname="argument shared_key", value=shared_key, expected_type=type_hints["shared_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "vpn_site_link_id": vpn_site_link_id,
        }
        if bandwidth_mbps is not None:
            self._values["bandwidth_mbps"] = bandwidth_mbps
        if bgp_enabled is not None:
            self._values["bgp_enabled"] = bgp_enabled
        if connection_mode is not None:
            self._values["connection_mode"] = connection_mode
        if custom_bgp_address is not None:
            self._values["custom_bgp_address"] = custom_bgp_address
        if egress_nat_rule_ids is not None:
            self._values["egress_nat_rule_ids"] = egress_nat_rule_ids
        if ingress_nat_rule_ids is not None:
            self._values["ingress_nat_rule_ids"] = ingress_nat_rule_ids
        if ipsec_policy is not None:
            self._values["ipsec_policy"] = ipsec_policy
        if local_azure_ip_address_enabled is not None:
            self._values["local_azure_ip_address_enabled"] = local_azure_ip_address_enabled
        if policy_based_traffic_selector_enabled is not None:
            self._values["policy_based_traffic_selector_enabled"] = policy_based_traffic_selector_enabled
        if protocol is not None:
            self._values["protocol"] = protocol
        if ratelimit_enabled is not None:
            self._values["ratelimit_enabled"] = ratelimit_enabled
        if route_weight is not None:
            self._values["route_weight"] = route_weight
        if shared_key is not None:
            self._values["shared_key"] = shared_key

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#name VpnGatewayConnection#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_site_link_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#vpn_site_link_id VpnGatewayConnection#vpn_site_link_id}.'''
        result = self._values.get("vpn_site_link_id")
        assert result is not None, "Required property 'vpn_site_link_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bandwidth_mbps(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#bandwidth_mbps VpnGatewayConnection#bandwidth_mbps}.'''
        result = self._values.get("bandwidth_mbps")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def bgp_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#bgp_enabled VpnGatewayConnection#bgp_enabled}.'''
        result = self._values.get("bgp_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def connection_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#connection_mode VpnGatewayConnection#connection_mode}.'''
        result = self._values.get("connection_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_bgp_address(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLinkCustomBgpAddress"]]]:
        '''custom_bgp_address block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#custom_bgp_address VpnGatewayConnection#custom_bgp_address}
        '''
        result = self._values.get("custom_bgp_address")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLinkCustomBgpAddress"]]], result)

    @builtins.property
    def egress_nat_rule_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#egress_nat_rule_ids VpnGatewayConnection#egress_nat_rule_ids}.'''
        result = self._values.get("egress_nat_rule_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ingress_nat_rule_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ingress_nat_rule_ids VpnGatewayConnection#ingress_nat_rule_ids}.'''
        result = self._values.get("ingress_nat_rule_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ipsec_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLinkIpsecPolicy"]]]:
        '''ipsec_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ipsec_policy VpnGatewayConnection#ipsec_policy}
        '''
        result = self._values.get("ipsec_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VpnGatewayConnectionVpnLinkIpsecPolicy"]]], result)

    @builtins.property
    def local_azure_ip_address_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#local_azure_ip_address_enabled VpnGatewayConnection#local_azure_ip_address_enabled}.'''
        result = self._values.get("local_azure_ip_address_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def policy_based_traffic_selector_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#policy_based_traffic_selector_enabled VpnGatewayConnection#policy_based_traffic_selector_enabled}.'''
        result = self._values.get("policy_based_traffic_selector_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#protocol VpnGatewayConnection#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ratelimit_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ratelimit_enabled VpnGatewayConnection#ratelimit_enabled}.'''
        result = self._values.get("ratelimit_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def route_weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#route_weight VpnGatewayConnection#route_weight}.'''
        result = self._values.get("route_weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def shared_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#shared_key VpnGatewayConnection#shared_key}.'''
        result = self._values.get("shared_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionVpnLink(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkCustomBgpAddress",
    jsii_struct_bases=[],
    name_mapping={
        "ip_address": "ipAddress",
        "ip_configuration_id": "ipConfigurationId",
    },
)
class VpnGatewayConnectionVpnLinkCustomBgpAddress:
    def __init__(
        self,
        *,
        ip_address: builtins.str,
        ip_configuration_id: builtins.str,
    ) -> None:
        '''
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ip_address VpnGatewayConnection#ip_address}.
        :param ip_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ip_configuration_id VpnGatewayConnection#ip_configuration_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkCustomBgpAddress.__init__)
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument ip_configuration_id", value=ip_configuration_id, expected_type=type_hints["ip_configuration_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_address": ip_address,
            "ip_configuration_id": ip_configuration_id,
        }

    @builtins.property
    def ip_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ip_address VpnGatewayConnection#ip_address}.'''
        result = self._values.get("ip_address")
        assert result is not None, "Required property 'ip_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_configuration_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ip_configuration_id VpnGatewayConnection#ip_configuration_id}.'''
        result = self._values.get("ip_configuration_id")
        assert result is not None, "Required property 'ip_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionVpnLinkCustomBgpAddress(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayConnectionVpnLinkCustomBgpAddressList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkCustomBgpAddressList",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkCustomBgpAddressList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkCustomBgpAddressList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkCustomBgpAddressList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkCustomBgpAddressList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkCustomBgpAddressList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkCustomBgpAddress]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkCustomBgpAddress]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkCustomBgpAddress]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkCustomBgpAddressList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationIdInput")
    def ip_configuration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipConfigurationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="ipConfigurationId")
    def ip_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipConfigurationId"))

    @ip_configuration_id.setter
    def ip_configuration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference, "ip_configuration_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipConfigurationId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnGatewayConnectionVpnLinkCustomBgpAddress, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnGatewayConnectionVpnLinkCustomBgpAddress, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnGatewayConnectionVpnLinkCustomBgpAddress, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkIpsecPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "dh_group": "dhGroup",
        "encryption_algorithm": "encryptionAlgorithm",
        "ike_encryption_algorithm": "ikeEncryptionAlgorithm",
        "ike_integrity_algorithm": "ikeIntegrityAlgorithm",
        "integrity_algorithm": "integrityAlgorithm",
        "pfs_group": "pfsGroup",
        "sa_data_size_kb": "saDataSizeKb",
        "sa_lifetime_sec": "saLifetimeSec",
    },
)
class VpnGatewayConnectionVpnLinkIpsecPolicy:
    def __init__(
        self,
        *,
        dh_group: builtins.str,
        encryption_algorithm: builtins.str,
        ike_encryption_algorithm: builtins.str,
        ike_integrity_algorithm: builtins.str,
        integrity_algorithm: builtins.str,
        pfs_group: builtins.str,
        sa_data_size_kb: jsii.Number,
        sa_lifetime_sec: jsii.Number,
    ) -> None:
        '''
        :param dh_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#dh_group VpnGatewayConnection#dh_group}.
        :param encryption_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#encryption_algorithm VpnGatewayConnection#encryption_algorithm}.
        :param ike_encryption_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ike_encryption_algorithm VpnGatewayConnection#ike_encryption_algorithm}.
        :param ike_integrity_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ike_integrity_algorithm VpnGatewayConnection#ike_integrity_algorithm}.
        :param integrity_algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#integrity_algorithm VpnGatewayConnection#integrity_algorithm}.
        :param pfs_group: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#pfs_group VpnGatewayConnection#pfs_group}.
        :param sa_data_size_kb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#sa_data_size_kb VpnGatewayConnection#sa_data_size_kb}.
        :param sa_lifetime_sec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#sa_lifetime_sec VpnGatewayConnection#sa_lifetime_sec}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkIpsecPolicy.__init__)
            check_type(argname="argument dh_group", value=dh_group, expected_type=type_hints["dh_group"])
            check_type(argname="argument encryption_algorithm", value=encryption_algorithm, expected_type=type_hints["encryption_algorithm"])
            check_type(argname="argument ike_encryption_algorithm", value=ike_encryption_algorithm, expected_type=type_hints["ike_encryption_algorithm"])
            check_type(argname="argument ike_integrity_algorithm", value=ike_integrity_algorithm, expected_type=type_hints["ike_integrity_algorithm"])
            check_type(argname="argument integrity_algorithm", value=integrity_algorithm, expected_type=type_hints["integrity_algorithm"])
            check_type(argname="argument pfs_group", value=pfs_group, expected_type=type_hints["pfs_group"])
            check_type(argname="argument sa_data_size_kb", value=sa_data_size_kb, expected_type=type_hints["sa_data_size_kb"])
            check_type(argname="argument sa_lifetime_sec", value=sa_lifetime_sec, expected_type=type_hints["sa_lifetime_sec"])
        self._values: typing.Dict[str, typing.Any] = {
            "dh_group": dh_group,
            "encryption_algorithm": encryption_algorithm,
            "ike_encryption_algorithm": ike_encryption_algorithm,
            "ike_integrity_algorithm": ike_integrity_algorithm,
            "integrity_algorithm": integrity_algorithm,
            "pfs_group": pfs_group,
            "sa_data_size_kb": sa_data_size_kb,
            "sa_lifetime_sec": sa_lifetime_sec,
        }

    @builtins.property
    def dh_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#dh_group VpnGatewayConnection#dh_group}.'''
        result = self._values.get("dh_group")
        assert result is not None, "Required property 'dh_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#encryption_algorithm VpnGatewayConnection#encryption_algorithm}.'''
        result = self._values.get("encryption_algorithm")
        assert result is not None, "Required property 'encryption_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_encryption_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ike_encryption_algorithm VpnGatewayConnection#ike_encryption_algorithm}.'''
        result = self._values.get("ike_encryption_algorithm")
        assert result is not None, "Required property 'ike_encryption_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ike_integrity_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#ike_integrity_algorithm VpnGatewayConnection#ike_integrity_algorithm}.'''
        result = self._values.get("ike_integrity_algorithm")
        assert result is not None, "Required property 'ike_integrity_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integrity_algorithm(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#integrity_algorithm VpnGatewayConnection#integrity_algorithm}.'''
        result = self._values.get("integrity_algorithm")
        assert result is not None, "Required property 'integrity_algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pfs_group(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#pfs_group VpnGatewayConnection#pfs_group}.'''
        result = self._values.get("pfs_group")
        assert result is not None, "Required property 'pfs_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sa_data_size_kb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#sa_data_size_kb VpnGatewayConnection#sa_data_size_kb}.'''
        result = self._values.get("sa_data_size_kb")
        assert result is not None, "Required property 'sa_data_size_kb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def sa_lifetime_sec(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/vpn_gateway_connection#sa_lifetime_sec VpnGatewayConnection#sa_lifetime_sec}.'''
        result = self._values.get("sa_lifetime_sec")
        assert result is not None, "Required property 'sa_lifetime_sec' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpnGatewayConnectionVpnLinkIpsecPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpnGatewayConnectionVpnLinkIpsecPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkIpsecPolicyList",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkIpsecPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkIpsecPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkIpsecPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkIpsecPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkIpsecPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="dhGroupInput")
    def dh_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dhGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionAlgorithmInput")
    def encryption_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeEncryptionAlgorithmInput")
    def ike_encryption_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeEncryptionAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrityAlgorithmInput")
    def ike_integrity_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ikeIntegrityAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="integrityAlgorithmInput")
    def integrity_algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrityAlgorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="pfsGroupInput")
    def pfs_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pfsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="saDataSizeKbInput")
    def sa_data_size_kb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saDataSizeKbInput"))

    @builtins.property
    @jsii.member(jsii_name="saLifetimeSecInput")
    def sa_lifetime_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "saLifetimeSecInput"))

    @builtins.property
    @jsii.member(jsii_name="dhGroup")
    def dh_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dhGroup"))

    @dh_group.setter
    def dh_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "dh_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhGroup", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionAlgorithm")
    def encryption_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionAlgorithm"))

    @encryption_algorithm.setter
    def encryption_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "encryption_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="ikeEncryptionAlgorithm")
    def ike_encryption_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeEncryptionAlgorithm"))

    @ike_encryption_algorithm.setter
    def ike_encryption_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "ike_encryption_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeEncryptionAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="ikeIntegrityAlgorithm")
    def ike_integrity_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ikeIntegrityAlgorithm"))

    @ike_integrity_algorithm.setter
    def ike_integrity_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "ike_integrity_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ikeIntegrityAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="integrityAlgorithm")
    def integrity_algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrityAlgorithm"))

    @integrity_algorithm.setter
    def integrity_algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "integrity_algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrityAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="pfsGroup")
    def pfs_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pfsGroup"))

    @pfs_group.setter
    def pfs_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "pfs_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pfsGroup", value)

    @builtins.property
    @jsii.member(jsii_name="saDataSizeKb")
    def sa_data_size_kb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saDataSizeKb"))

    @sa_data_size_kb.setter
    def sa_data_size_kb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "sa_data_size_kb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saDataSizeKb", value)

    @builtins.property
    @jsii.member(jsii_name="saLifetimeSec")
    def sa_lifetime_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "saLifetimeSec"))

    @sa_lifetime_sec.setter
    def sa_lifetime_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "sa_lifetime_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "saLifetimeSec", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnGatewayConnectionVpnLinkIpsecPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnGatewayConnectionVpnLinkIpsecPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnGatewayConnectionVpnLinkIpsecPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnGatewayConnectionVpnLinkList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkList",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "VpnGatewayConnectionVpnLinkOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VpnGatewayConnectionVpnLinkOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLink]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLink]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLink]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VpnGatewayConnectionVpnLinkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.vpnGatewayConnection.VpnGatewayConnectionVpnLinkOutputReference",
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
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCustomBgpAddress")
    def put_custom_bgp_address(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VpnGatewayConnectionVpnLinkCustomBgpAddress, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkOutputReference.put_custom_bgp_address)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomBgpAddress", [value]))

    @jsii.member(jsii_name="putIpsecPolicy")
    def put_ipsec_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[VpnGatewayConnectionVpnLinkIpsecPolicy, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VpnGatewayConnectionVpnLinkOutputReference.put_ipsec_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIpsecPolicy", [value]))

    @jsii.member(jsii_name="resetBandwidthMbps")
    def reset_bandwidth_mbps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBandwidthMbps", []))

    @jsii.member(jsii_name="resetBgpEnabled")
    def reset_bgp_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBgpEnabled", []))

    @jsii.member(jsii_name="resetConnectionMode")
    def reset_connection_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionMode", []))

    @jsii.member(jsii_name="resetCustomBgpAddress")
    def reset_custom_bgp_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomBgpAddress", []))

    @jsii.member(jsii_name="resetEgressNatRuleIds")
    def reset_egress_nat_rule_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEgressNatRuleIds", []))

    @jsii.member(jsii_name="resetIngressNatRuleIds")
    def reset_ingress_nat_rule_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIngressNatRuleIds", []))

    @jsii.member(jsii_name="resetIpsecPolicy")
    def reset_ipsec_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpsecPolicy", []))

    @jsii.member(jsii_name="resetLocalAzureIpAddressEnabled")
    def reset_local_azure_ip_address_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalAzureIpAddressEnabled", []))

    @jsii.member(jsii_name="resetPolicyBasedTrafficSelectorEnabled")
    def reset_policy_based_traffic_selector_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicyBasedTrafficSelectorEnabled", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRatelimitEnabled")
    def reset_ratelimit_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRatelimitEnabled", []))

    @jsii.member(jsii_name="resetRouteWeight")
    def reset_route_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteWeight", []))

    @jsii.member(jsii_name="resetSharedKey")
    def reset_shared_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedKey", []))

    @builtins.property
    @jsii.member(jsii_name="customBgpAddress")
    def custom_bgp_address(self) -> VpnGatewayConnectionVpnLinkCustomBgpAddressList:
        return typing.cast(VpnGatewayConnectionVpnLinkCustomBgpAddressList, jsii.get(self, "customBgpAddress"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicy")
    def ipsec_policy(self) -> VpnGatewayConnectionVpnLinkIpsecPolicyList:
        return typing.cast(VpnGatewayConnectionVpnLinkIpsecPolicyList, jsii.get(self, "ipsecPolicy"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthMbpsInput")
    def bandwidth_mbps_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bandwidthMbpsInput"))

    @builtins.property
    @jsii.member(jsii_name="bgpEnabledInput")
    def bgp_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bgpEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionModeInput")
    def connection_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionModeInput"))

    @builtins.property
    @jsii.member(jsii_name="customBgpAddressInput")
    def custom_bgp_address_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkCustomBgpAddress]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkCustomBgpAddress]]], jsii.get(self, "customBgpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="egressNatRuleIdsInput")
    def egress_nat_rule_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "egressNatRuleIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="ingressNatRuleIdsInput")
    def ingress_nat_rule_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ingressNatRuleIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecPolicyInput")
    def ipsec_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkIpsecPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VpnGatewayConnectionVpnLinkIpsecPolicy]]], jsii.get(self, "ipsecPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="localAzureIpAddressEnabledInput")
    def local_azure_ip_address_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localAzureIpAddressEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="policyBasedTrafficSelectorEnabledInput")
    def policy_based_traffic_selector_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "policyBasedTrafficSelectorEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ratelimitEnabledInput")
    def ratelimit_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ratelimitEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="routeWeightInput")
    def route_weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "routeWeightInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedKeyInput")
    def shared_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sharedKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnSiteLinkIdInput")
    def vpn_site_link_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnSiteLinkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthMbps")
    def bandwidth_mbps(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bandwidthMbps"))

    @bandwidth_mbps.setter
    def bandwidth_mbps(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "bandwidth_mbps").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidthMbps", value)

    @builtins.property
    @jsii.member(jsii_name="bgpEnabled")
    def bgp_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bgpEnabled"))

    @bgp_enabled.setter
    def bgp_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "bgp_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="connectionMode")
    def connection_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionMode"))

    @connection_mode.setter
    def connection_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "connection_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionMode", value)

    @builtins.property
    @jsii.member(jsii_name="egressNatRuleIds")
    def egress_nat_rule_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "egressNatRuleIds"))

    @egress_nat_rule_ids.setter
    def egress_nat_rule_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "egress_nat_rule_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressNatRuleIds", value)

    @builtins.property
    @jsii.member(jsii_name="ingressNatRuleIds")
    def ingress_nat_rule_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ingressNatRuleIds"))

    @ingress_nat_rule_ids.setter
    def ingress_nat_rule_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "ingress_nat_rule_ids").fset)
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
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "local_azure_ip_address_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localAzureIpAddressEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyBasedTrafficSelectorEnabled")
    def policy_based_traffic_selector_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "policyBasedTrafficSelectorEnabled"))

    @policy_based_traffic_selector_enabled.setter
    def policy_based_traffic_selector_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "policy_based_traffic_selector_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyBasedTrafficSelectorEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="ratelimitEnabled")
    def ratelimit_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ratelimitEnabled"))

    @ratelimit_enabled.setter
    def ratelimit_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "ratelimit_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ratelimitEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="routeWeight")
    def route_weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "routeWeight"))

    @route_weight.setter
    def route_weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "route_weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeWeight", value)

    @builtins.property
    @jsii.member(jsii_name="sharedKey")
    def shared_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sharedKey"))

    @shared_key.setter
    def shared_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "shared_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedKey", value)

    @builtins.property
    @jsii.member(jsii_name="vpnSiteLinkId")
    def vpn_site_link_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnSiteLinkId"))

    @vpn_site_link_id.setter
    def vpn_site_link_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "vpn_site_link_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnSiteLinkId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VpnGatewayConnectionVpnLink, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VpnGatewayConnectionVpnLink, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VpnGatewayConnectionVpnLink, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VpnGatewayConnectionVpnLinkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VpnGatewayConnection",
    "VpnGatewayConnectionConfig",
    "VpnGatewayConnectionRouting",
    "VpnGatewayConnectionRoutingOutputReference",
    "VpnGatewayConnectionRoutingPropagatedRouteTable",
    "VpnGatewayConnectionRoutingPropagatedRouteTableOutputReference",
    "VpnGatewayConnectionTimeouts",
    "VpnGatewayConnectionTimeoutsOutputReference",
    "VpnGatewayConnectionTrafficSelectorPolicy",
    "VpnGatewayConnectionTrafficSelectorPolicyList",
    "VpnGatewayConnectionTrafficSelectorPolicyOutputReference",
    "VpnGatewayConnectionVpnLink",
    "VpnGatewayConnectionVpnLinkCustomBgpAddress",
    "VpnGatewayConnectionVpnLinkCustomBgpAddressList",
    "VpnGatewayConnectionVpnLinkCustomBgpAddressOutputReference",
    "VpnGatewayConnectionVpnLinkIpsecPolicy",
    "VpnGatewayConnectionVpnLinkIpsecPolicyList",
    "VpnGatewayConnectionVpnLinkIpsecPolicyOutputReference",
    "VpnGatewayConnectionVpnLinkList",
    "VpnGatewayConnectionVpnLinkOutputReference",
]

publication.publish()
