'''
# `upcloud_network`

Refer to the Terraform Registory for docs: [`upcloud_network`](https://www.terraform.io/docs/providers/upcloud/r/network).
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


class Network(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.network.Network",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/network upcloud_network}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        ip_network: typing.Union["NetworkIpNetwork", typing.Dict[str, typing.Any]],
        name: builtins.str,
        zone: builtins.str,
        id: typing.Optional[builtins.str] = None,
        router: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/network upcloud_network} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ip_network: ip_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#ip_network Network#ip_network}
        :param name: A valid name for the network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#name Network#name}
        :param zone: The zone the network is in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#zone Network#zone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param router: The UUID of a router. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#router Network#router}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Network.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkConfig(
            ip_network=ip_network,
            name=name,
            zone=zone,
            id=id,
            router=router,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putIpNetwork")
    def put_ip_network(
        self,
        *,
        address: builtins.str,
        dhcp: typing.Union[builtins.bool, cdktf.IResolvable],
        family: builtins.str,
        dhcp_default_route: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dhcp_dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        gateway: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address: The CIDR range of the subnet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#address Network#address}
        :param dhcp: Is DHCP enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp Network#dhcp}
        :param family: IP address family. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#family Network#family}
        :param dhcp_default_route: Is the gateway the DHCP default route? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp_default_route Network#dhcp_default_route}
        :param dhcp_dns: The DNS servers given by DHCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp_dns Network#dhcp_dns}
        :param gateway: Gateway address given by DHCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#gateway Network#gateway}
        '''
        value = NetworkIpNetwork(
            address=address,
            dhcp=dhcp,
            family=family,
            dhcp_default_route=dhcp_default_route,
            dhcp_dns=dhcp_dns,
            gateway=gateway,
        )

        return typing.cast(None, jsii.invoke(self, "putIpNetwork", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRouter")
    def reset_router(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouter", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> "NetworkIpNetworkOutputReference":
        return typing.cast("NetworkIpNetworkOutputReference", jsii.get(self, "ipNetwork"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional["NetworkIpNetwork"]:
        return typing.cast(typing.Optional["NetworkIpNetwork"], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="routerInput")
    def router_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routerInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="router")
    def router(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "router"))

    @router.setter
    def router(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "router").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "router", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Network, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.network.NetworkConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ip_network": "ipNetwork",
        "name": "name",
        "zone": "zone",
        "id": "id",
        "router": "router",
    },
)
class NetworkConfig(cdktf.TerraformMetaArguments):
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
        ip_network: typing.Union["NetworkIpNetwork", typing.Dict[str, typing.Any]],
        name: builtins.str,
        zone: builtins.str,
        id: typing.Optional[builtins.str] = None,
        router: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ip_network: ip_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#ip_network Network#ip_network}
        :param name: A valid name for the network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#name Network#name}
        :param zone: The zone the network is in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#zone Network#zone}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#id Network#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param router: The UUID of a router. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#router Network#router}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(ip_network, dict):
            ip_network = NetworkIpNetwork(**ip_network)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument router", value=router, expected_type=type_hints["router"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip_network": ip_network,
            "name": name,
            "zone": zone,
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
        if router is not None:
            self._values["router"] = router

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
    def ip_network(self) -> "NetworkIpNetwork":
        '''ip_network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#ip_network Network#ip_network}
        '''
        result = self._values.get("ip_network")
        assert result is not None, "Required property 'ip_network' is missing"
        return typing.cast("NetworkIpNetwork", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A valid name for the network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#name Network#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''The zone the network is in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#zone Network#zone}
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#id Network#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def router(self) -> typing.Optional[builtins.str]:
        '''The UUID of a router.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#router Network#router}
        '''
        result = self._values.get("router")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.network.NetworkIpNetwork",
    jsii_struct_bases=[],
    name_mapping={
        "address": "address",
        "dhcp": "dhcp",
        "family": "family",
        "dhcp_default_route": "dhcpDefaultRoute",
        "dhcp_dns": "dhcpDns",
        "gateway": "gateway",
    },
)
class NetworkIpNetwork:
    def __init__(
        self,
        *,
        address: builtins.str,
        dhcp: typing.Union[builtins.bool, cdktf.IResolvable],
        family: builtins.str,
        dhcp_default_route: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        dhcp_dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        gateway: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address: The CIDR range of the subnet. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#address Network#address}
        :param dhcp: Is DHCP enabled? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp Network#dhcp}
        :param family: IP address family. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#family Network#family}
        :param dhcp_default_route: Is the gateway the DHCP default route? Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp_default_route Network#dhcp_default_route}
        :param dhcp_dns: The DNS servers given by DHCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp_dns Network#dhcp_dns}
        :param gateway: Gateway address given by DHCP. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#gateway Network#gateway}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkIpNetwork.__init__)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument dhcp", value=dhcp, expected_type=type_hints["dhcp"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument dhcp_default_route", value=dhcp_default_route, expected_type=type_hints["dhcp_default_route"])
            check_type(argname="argument dhcp_dns", value=dhcp_dns, expected_type=type_hints["dhcp_dns"])
            check_type(argname="argument gateway", value=gateway, expected_type=type_hints["gateway"])
        self._values: typing.Dict[str, typing.Any] = {
            "address": address,
            "dhcp": dhcp,
            "family": family,
        }
        if dhcp_default_route is not None:
            self._values["dhcp_default_route"] = dhcp_default_route
        if dhcp_dns is not None:
            self._values["dhcp_dns"] = dhcp_dns
        if gateway is not None:
            self._values["gateway"] = gateway

    @builtins.property
    def address(self) -> builtins.str:
        '''The CIDR range of the subnet.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#address Network#address}
        '''
        result = self._values.get("address")
        assert result is not None, "Required property 'address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dhcp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Is DHCP enabled?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp Network#dhcp}
        '''
        result = self._values.get("dhcp")
        assert result is not None, "Required property 'dhcp' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def family(self) -> builtins.str:
        '''IP address family.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#family Network#family}
        '''
        result = self._values.get("family")
        assert result is not None, "Required property 'family' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dhcp_default_route(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Is the gateway the DHCP default route?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp_default_route Network#dhcp_default_route}
        '''
        result = self._values.get("dhcp_default_route")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def dhcp_dns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The DNS servers given by DHCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#dhcp_dns Network#dhcp_dns}
        '''
        result = self._values.get("dhcp_dns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def gateway(self) -> typing.Optional[builtins.str]:
        '''Gateway address given by DHCP.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/network#gateway Network#gateway}
        '''
        result = self._values.get("gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkIpNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkIpNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.network.NetworkIpNetworkOutputReference",
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
            type_hints = typing.get_type_hints(NetworkIpNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDhcpDefaultRoute")
    def reset_dhcp_default_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDhcpDefaultRoute", []))

    @jsii.member(jsii_name="resetDhcpDns")
    def reset_dhcp_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDhcpDns", []))

    @jsii.member(jsii_name="resetGateway")
    def reset_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGateway", []))

    @builtins.property
    @jsii.member(jsii_name="addressInput")
    def address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "addressInput"))

    @builtins.property
    @jsii.member(jsii_name="dhcpDefaultRouteInput")
    def dhcp_default_route_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dhcpDefaultRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="dhcpDnsInput")
    def dhcp_dns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dhcpDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="dhcpInput")
    def dhcp_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dhcpInput"))

    @builtins.property
    @jsii.member(jsii_name="familyInput")
    def family_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "familyInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayInput")
    def gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="address")
    def address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "address"))

    @address.setter
    def address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpNetworkOutputReference, "address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "address", value)

    @builtins.property
    @jsii.member(jsii_name="dhcp")
    def dhcp(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dhcp"))

    @dhcp.setter
    def dhcp(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpNetworkOutputReference, "dhcp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcp", value)

    @builtins.property
    @jsii.member(jsii_name="dhcpDefaultRoute")
    def dhcp_default_route(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dhcpDefaultRoute"))

    @dhcp_default_route.setter
    def dhcp_default_route(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpNetworkOutputReference, "dhcp_default_route").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpDefaultRoute", value)

    @builtins.property
    @jsii.member(jsii_name="dhcpDns")
    def dhcp_dns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dhcpDns"))

    @dhcp_dns.setter
    def dhcp_dns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpNetworkOutputReference, "dhcp_dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dhcpDns", value)

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "family"))

    @family.setter
    def family(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpNetworkOutputReference, "family").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "family", value)

    @builtins.property
    @jsii.member(jsii_name="gateway")
    def gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gateway"))

    @gateway.setter
    def gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpNetworkOutputReference, "gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gateway", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[NetworkIpNetwork]:
        return typing.cast(typing.Optional[NetworkIpNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[NetworkIpNetwork]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkIpNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Network",
    "NetworkConfig",
    "NetworkIpNetwork",
    "NetworkIpNetworkOutputReference",
]

publication.publish()
