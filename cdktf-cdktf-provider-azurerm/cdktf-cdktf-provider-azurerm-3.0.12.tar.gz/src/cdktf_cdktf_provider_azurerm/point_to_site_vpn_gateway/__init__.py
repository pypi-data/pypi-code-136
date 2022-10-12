'''
# `azurerm_point_to_site_vpn_gateway`

Refer to the Terraform Registory for docs: [`azurerm_point_to_site_vpn_gateway`](https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway).
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


class PointToSiteVpnGateway(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGateway",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway azurerm_point_to_site_vpn_gateway}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        connection_configuration: typing.Union["PointToSiteVpnGatewayConnectionConfiguration", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        scale_unit: jsii.Number,
        virtual_hub_id: builtins.str,
        vpn_server_configuration_id: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PointToSiteVpnGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway azurerm_point_to_site_vpn_gateway} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param connection_configuration: connection_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#connection_configuration PointToSiteVpnGateway#connection_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#location PointToSiteVpnGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#name PointToSiteVpnGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#resource_group_name PointToSiteVpnGateway#resource_group_name}.
        :param scale_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#scale_unit PointToSiteVpnGateway#scale_unit}.
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#virtual_hub_id PointToSiteVpnGateway#virtual_hub_id}.
        :param vpn_server_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#vpn_server_configuration_id PointToSiteVpnGateway#vpn_server_configuration_id}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#dns_servers PointToSiteVpnGateway#dns_servers}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#id PointToSiteVpnGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#tags PointToSiteVpnGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#timeouts PointToSiteVpnGateway#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PointToSiteVpnGateway.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PointToSiteVpnGatewayConfig(
            connection_configuration=connection_configuration,
            location=location,
            name=name,
            resource_group_name=resource_group_name,
            scale_unit=scale_unit,
            virtual_hub_id=virtual_hub_id,
            vpn_server_configuration_id=vpn_server_configuration_id,
            dns_servers=dns_servers,
            id=id,
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

    @jsii.member(jsii_name="putConnectionConfiguration")
    def put_connection_configuration(
        self,
        *,
        name: builtins.str,
        vpn_client_address_pool: typing.Union["PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool", typing.Dict[str, typing.Any]],
        internet_security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        route: typing.Optional[typing.Union["PointToSiteVpnGatewayConnectionConfigurationRoute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#name PointToSiteVpnGateway#name}.
        :param vpn_client_address_pool: vpn_client_address_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#vpn_client_address_pool PointToSiteVpnGateway#vpn_client_address_pool}
        :param internet_security_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#internet_security_enabled PointToSiteVpnGateway#internet_security_enabled}.
        :param route: route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#route PointToSiteVpnGateway#route}
        '''
        value = PointToSiteVpnGatewayConnectionConfiguration(
            name=name,
            vpn_client_address_pool=vpn_client_address_pool,
            internet_security_enabled=internet_security_enabled,
            route=route,
        )

        return typing.cast(None, jsii.invoke(self, "putConnectionConfiguration", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#create PointToSiteVpnGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#delete PointToSiteVpnGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#read PointToSiteVpnGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#update PointToSiteVpnGateway#update}.
        '''
        value = PointToSiteVpnGatewayTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDnsServers")
    def reset_dns_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsServers", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="connectionConfiguration")
    def connection_configuration(
        self,
    ) -> "PointToSiteVpnGatewayConnectionConfigurationOutputReference":
        return typing.cast("PointToSiteVpnGatewayConnectionConfigurationOutputReference", jsii.get(self, "connectionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PointToSiteVpnGatewayTimeoutsOutputReference":
        return typing.cast("PointToSiteVpnGatewayTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="connectionConfigurationInput")
    def connection_configuration_input(
        self,
    ) -> typing.Optional["PointToSiteVpnGatewayConnectionConfiguration"]:
        return typing.cast(typing.Optional["PointToSiteVpnGatewayConnectionConfiguration"], jsii.get(self, "connectionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServersInput")
    def dns_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsServersInput"))

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
    ) -> typing.Optional[typing.Union["PointToSiteVpnGatewayTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PointToSiteVpnGatewayTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualHubIdInput")
    def virtual_hub_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualHubIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnServerConfigurationIdInput")
    def vpn_server_configuration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnServerConfigurationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsServers")
    def dns_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dnsServers"))

    @dns_servers.setter
    def dns_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "dns_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsServers", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="scaleUnit")
    def scale_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "scaleUnit"))

    @scale_unit.setter
    def scale_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "scale_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scaleUnit", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="virtualHubId")
    def virtual_hub_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualHubId"))

    @virtual_hub_id.setter
    def virtual_hub_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "virtual_hub_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualHubId", value)

    @builtins.property
    @jsii.member(jsii_name="vpnServerConfigurationId")
    def vpn_server_configuration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnServerConfigurationId"))

    @vpn_server_configuration_id.setter
    def vpn_server_configuration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGateway, "vpn_server_configuration_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnServerConfigurationId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "connection_configuration": "connectionConfiguration",
        "location": "location",
        "name": "name",
        "resource_group_name": "resourceGroupName",
        "scale_unit": "scaleUnit",
        "virtual_hub_id": "virtualHubId",
        "vpn_server_configuration_id": "vpnServerConfigurationId",
        "dns_servers": "dnsServers",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class PointToSiteVpnGatewayConfig(cdktf.TerraformMetaArguments):
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
        connection_configuration: typing.Union["PointToSiteVpnGatewayConnectionConfiguration", typing.Dict[str, typing.Any]],
        location: builtins.str,
        name: builtins.str,
        resource_group_name: builtins.str,
        scale_unit: jsii.Number,
        virtual_hub_id: builtins.str,
        vpn_server_configuration_id: builtins.str,
        dns_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["PointToSiteVpnGatewayTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param connection_configuration: connection_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#connection_configuration PointToSiteVpnGateway#connection_configuration}
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#location PointToSiteVpnGateway#location}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#name PointToSiteVpnGateway#name}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#resource_group_name PointToSiteVpnGateway#resource_group_name}.
        :param scale_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#scale_unit PointToSiteVpnGateway#scale_unit}.
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#virtual_hub_id PointToSiteVpnGateway#virtual_hub_id}.
        :param vpn_server_configuration_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#vpn_server_configuration_id PointToSiteVpnGateway#vpn_server_configuration_id}.
        :param dns_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#dns_servers PointToSiteVpnGateway#dns_servers}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#id PointToSiteVpnGateway#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#tags PointToSiteVpnGateway#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#timeouts PointToSiteVpnGateway#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(connection_configuration, dict):
            connection_configuration = PointToSiteVpnGatewayConnectionConfiguration(**connection_configuration)
        if isinstance(timeouts, dict):
            timeouts = PointToSiteVpnGatewayTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument connection_configuration", value=connection_configuration, expected_type=type_hints["connection_configuration"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument scale_unit", value=scale_unit, expected_type=type_hints["scale_unit"])
            check_type(argname="argument virtual_hub_id", value=virtual_hub_id, expected_type=type_hints["virtual_hub_id"])
            check_type(argname="argument vpn_server_configuration_id", value=vpn_server_configuration_id, expected_type=type_hints["vpn_server_configuration_id"])
            check_type(argname="argument dns_servers", value=dns_servers, expected_type=type_hints["dns_servers"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "connection_configuration": connection_configuration,
            "location": location,
            "name": name,
            "resource_group_name": resource_group_name,
            "scale_unit": scale_unit,
            "virtual_hub_id": virtual_hub_id,
            "vpn_server_configuration_id": vpn_server_configuration_id,
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
        if dns_servers is not None:
            self._values["dns_servers"] = dns_servers
        if id is not None:
            self._values["id"] = id
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
    def connection_configuration(
        self,
    ) -> "PointToSiteVpnGatewayConnectionConfiguration":
        '''connection_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#connection_configuration PointToSiteVpnGateway#connection_configuration}
        '''
        result = self._values.get("connection_configuration")
        assert result is not None, "Required property 'connection_configuration' is missing"
        return typing.cast("PointToSiteVpnGatewayConnectionConfiguration", result)

    @builtins.property
    def location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#location PointToSiteVpnGateway#location}.'''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#name PointToSiteVpnGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#resource_group_name PointToSiteVpnGateway#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scale_unit(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#scale_unit PointToSiteVpnGateway#scale_unit}.'''
        result = self._values.get("scale_unit")
        assert result is not None, "Required property 'scale_unit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def virtual_hub_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#virtual_hub_id PointToSiteVpnGateway#virtual_hub_id}.'''
        result = self._values.get("virtual_hub_id")
        assert result is not None, "Required property 'virtual_hub_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_server_configuration_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#vpn_server_configuration_id PointToSiteVpnGateway#vpn_server_configuration_id}.'''
        result = self._values.get("vpn_server_configuration_id")
        assert result is not None, "Required property 'vpn_server_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dns_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#dns_servers PointToSiteVpnGateway#dns_servers}.'''
        result = self._values.get("dns_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#id PointToSiteVpnGateway#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#tags PointToSiteVpnGateway#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PointToSiteVpnGatewayTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#timeouts PointToSiteVpnGateway#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PointToSiteVpnGatewayTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PointToSiteVpnGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "vpn_client_address_pool": "vpnClientAddressPool",
        "internet_security_enabled": "internetSecurityEnabled",
        "route": "route",
    },
)
class PointToSiteVpnGatewayConnectionConfiguration:
    def __init__(
        self,
        *,
        name: builtins.str,
        vpn_client_address_pool: typing.Union["PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool", typing.Dict[str, typing.Any]],
        internet_security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        route: typing.Optional[typing.Union["PointToSiteVpnGatewayConnectionConfigurationRoute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#name PointToSiteVpnGateway#name}.
        :param vpn_client_address_pool: vpn_client_address_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#vpn_client_address_pool PointToSiteVpnGateway#vpn_client_address_pool}
        :param internet_security_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#internet_security_enabled PointToSiteVpnGateway#internet_security_enabled}.
        :param route: route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#route PointToSiteVpnGateway#route}
        '''
        if isinstance(vpn_client_address_pool, dict):
            vpn_client_address_pool = PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool(**vpn_client_address_pool)
        if isinstance(route, dict):
            route = PointToSiteVpnGatewayConnectionConfigurationRoute(**route)
        if __debug__:
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfiguration.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument vpn_client_address_pool", value=vpn_client_address_pool, expected_type=type_hints["vpn_client_address_pool"])
            check_type(argname="argument internet_security_enabled", value=internet_security_enabled, expected_type=type_hints["internet_security_enabled"])
            check_type(argname="argument route", value=route, expected_type=type_hints["route"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "vpn_client_address_pool": vpn_client_address_pool,
        }
        if internet_security_enabled is not None:
            self._values["internet_security_enabled"] = internet_security_enabled
        if route is not None:
            self._values["route"] = route

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#name PointToSiteVpnGateway#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_client_address_pool(
        self,
    ) -> "PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool":
        '''vpn_client_address_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#vpn_client_address_pool PointToSiteVpnGateway#vpn_client_address_pool}
        '''
        result = self._values.get("vpn_client_address_pool")
        assert result is not None, "Required property 'vpn_client_address_pool' is missing"
        return typing.cast("PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool", result)

    @builtins.property
    def internet_security_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#internet_security_enabled PointToSiteVpnGateway#internet_security_enabled}.'''
        result = self._values.get("internet_security_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def route(
        self,
    ) -> typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoute"]:
        '''route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#route PointToSiteVpnGateway#route}
        '''
        result = self._values.get("route")
        return typing.cast(typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PointToSiteVpnGatewayConnectionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PointToSiteVpnGatewayConnectionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRoute")
    def put_route(
        self,
        *,
        associated_route_table_id: builtins.str,
        propagated_route_table: typing.Optional[typing.Union["PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param associated_route_table_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#associated_route_table_id PointToSiteVpnGateway#associated_route_table_id}.
        :param propagated_route_table: propagated_route_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#propagated_route_table PointToSiteVpnGateway#propagated_route_table}
        '''
        value = PointToSiteVpnGatewayConnectionConfigurationRoute(
            associated_route_table_id=associated_route_table_id,
            propagated_route_table=propagated_route_table,
        )

        return typing.cast(None, jsii.invoke(self, "putRoute", [value]))

    @jsii.member(jsii_name="putVpnClientAddressPool")
    def put_vpn_client_address_pool(
        self,
        *,
        address_prefixes: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#address_prefixes PointToSiteVpnGateway#address_prefixes}.
        '''
        value = PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool(
            address_prefixes=address_prefixes
        )

        return typing.cast(None, jsii.invoke(self, "putVpnClientAddressPool", [value]))

    @jsii.member(jsii_name="resetInternetSecurityEnabled")
    def reset_internet_security_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternetSecurityEnabled", []))

    @jsii.member(jsii_name="resetRoute")
    def reset_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoute", []))

    @builtins.property
    @jsii.member(jsii_name="route")
    def route(
        self,
    ) -> "PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference":
        return typing.cast("PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference", jsii.get(self, "route"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientAddressPool")
    def vpn_client_address_pool(
        self,
    ) -> "PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference":
        return typing.cast("PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference", jsii.get(self, "vpnClientAddressPool"))

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
    @jsii.member(jsii_name="routeInput")
    def route_input(
        self,
    ) -> typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoute"]:
        return typing.cast(typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoute"], jsii.get(self, "routeInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnClientAddressPoolInput")
    def vpn_client_address_pool_input(
        self,
    ) -> typing.Optional["PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool"]:
        return typing.cast(typing.Optional["PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool"], jsii.get(self, "vpnClientAddressPoolInput"))

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
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationOutputReference, "internet_security_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetSecurityEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PointToSiteVpnGatewayConnectionConfiguration]:
        return typing.cast(typing.Optional[PointToSiteVpnGatewayConnectionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PointToSiteVpnGatewayConnectionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfigurationRoute",
    jsii_struct_bases=[],
    name_mapping={
        "associated_route_table_id": "associatedRouteTableId",
        "propagated_route_table": "propagatedRouteTable",
    },
)
class PointToSiteVpnGatewayConnectionConfigurationRoute:
    def __init__(
        self,
        *,
        associated_route_table_id: builtins.str,
        propagated_route_table: typing.Optional[typing.Union["PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param associated_route_table_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#associated_route_table_id PointToSiteVpnGateway#associated_route_table_id}.
        :param propagated_route_table: propagated_route_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#propagated_route_table PointToSiteVpnGateway#propagated_route_table}
        '''
        if isinstance(propagated_route_table, dict):
            propagated_route_table = PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable(**propagated_route_table)
        if __debug__:
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfigurationRoute.__init__)
            check_type(argname="argument associated_route_table_id", value=associated_route_table_id, expected_type=type_hints["associated_route_table_id"])
            check_type(argname="argument propagated_route_table", value=propagated_route_table, expected_type=type_hints["propagated_route_table"])
        self._values: typing.Dict[str, typing.Any] = {
            "associated_route_table_id": associated_route_table_id,
        }
        if propagated_route_table is not None:
            self._values["propagated_route_table"] = propagated_route_table

    @builtins.property
    def associated_route_table_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#associated_route_table_id PointToSiteVpnGateway#associated_route_table_id}.'''
        result = self._values.get("associated_route_table_id")
        assert result is not None, "Required property 'associated_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def propagated_route_table(
        self,
    ) -> typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable"]:
        '''propagated_route_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#propagated_route_table PointToSiteVpnGateway#propagated_route_table}
        '''
        result = self._values.get("propagated_route_table")
        return typing.cast(typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PointToSiteVpnGatewayConnectionConfigurationRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference",
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
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPropagatedRouteTable")
    def put_propagated_route_table(
        self,
        *,
        ids: typing.Sequence[builtins.str],
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#ids PointToSiteVpnGateway#ids}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#labels PointToSiteVpnGateway#labels}.
        '''
        value = PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable(
            ids=ids, labels=labels
        )

        return typing.cast(None, jsii.invoke(self, "putPropagatedRouteTable", [value]))

    @jsii.member(jsii_name="resetPropagatedRouteTable")
    def reset_propagated_route_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagatedRouteTable", []))

    @builtins.property
    @jsii.member(jsii_name="propagatedRouteTable")
    def propagated_route_table(
        self,
    ) -> "PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference":
        return typing.cast("PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference", jsii.get(self, "propagatedRouteTable"))

    @builtins.property
    @jsii.member(jsii_name="associatedRouteTableIdInput")
    def associated_route_table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associatedRouteTableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="propagatedRouteTableInput")
    def propagated_route_table_input(
        self,
    ) -> typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable"]:
        return typing.cast(typing.Optional["PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable"], jsii.get(self, "propagatedRouteTableInput"))

    @builtins.property
    @jsii.member(jsii_name="associatedRouteTableId")
    def associated_route_table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedRouteTableId"))

    @associated_route_table_id.setter
    def associated_route_table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference, "associated_route_table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedRouteTableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PointToSiteVpnGatewayConnectionConfigurationRoute]:
        return typing.cast(typing.Optional[PointToSiteVpnGatewayConnectionConfigurationRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PointToSiteVpnGatewayConnectionConfigurationRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable",
    jsii_struct_bases=[],
    name_mapping={"ids": "ids", "labels": "labels"},
)
class PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable:
    def __init__(
        self,
        *,
        ids: typing.Sequence[builtins.str],
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#ids PointToSiteVpnGateway#ids}.
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#labels PointToSiteVpnGateway#labels}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable.__init__)
            check_type(argname="argument ids", value=ids, expected_type=type_hints["ids"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
        self._values: typing.Dict[str, typing.Any] = {
            "ids": ids,
        }
        if labels is not None:
            self._values["labels"] = labels

    @builtins.property
    def ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#ids PointToSiteVpnGateway#ids}.'''
        result = self._values.get("ids")
        assert result is not None, "Required property 'ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#labels PointToSiteVpnGateway#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference",
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
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @builtins.property
    @jsii.member(jsii_name="idsInput")
    def ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "idsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="ids")
    def ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ids"))

    @ids.setter
    def ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference, "ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ids", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable]:
        return typing.cast(typing.Optional[PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool",
    jsii_struct_bases=[],
    name_mapping={"address_prefixes": "addressPrefixes"},
)
class PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool:
    def __init__(self, *, address_prefixes: typing.Sequence[builtins.str]) -> None:
        '''
        :param address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#address_prefixes PointToSiteVpnGateway#address_prefixes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool.__init__)
            check_type(argname="argument address_prefixes", value=address_prefixes, expected_type=type_hints["address_prefixes"])
        self._values: typing.Dict[str, typing.Any] = {
            "address_prefixes": address_prefixes,
        }

    @builtins.property
    def address_prefixes(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#address_prefixes PointToSiteVpnGateway#address_prefixes}.'''
        result = self._values.get("address_prefixes")
        assert result is not None, "Required property 'address_prefixes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference",
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
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference, "address_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool]:
        return typing.cast(typing.Optional[PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class PointToSiteVpnGatewayTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#create PointToSiteVpnGateway#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#delete PointToSiteVpnGateway#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#read PointToSiteVpnGateway#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#update PointToSiteVpnGateway#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#create PointToSiteVpnGateway#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#delete PointToSiteVpnGateway#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#read PointToSiteVpnGateway#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/point_to_site_vpn_gateway#update PointToSiteVpnGateway#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PointToSiteVpnGatewayTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PointToSiteVpnGatewayTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.pointToSiteVpnGateway.PointToSiteVpnGatewayTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(PointToSiteVpnGatewayTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PointToSiteVpnGatewayTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PointToSiteVpnGatewayTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PointToSiteVpnGatewayTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PointToSiteVpnGatewayTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PointToSiteVpnGateway",
    "PointToSiteVpnGatewayConfig",
    "PointToSiteVpnGatewayConnectionConfiguration",
    "PointToSiteVpnGatewayConnectionConfigurationOutputReference",
    "PointToSiteVpnGatewayConnectionConfigurationRoute",
    "PointToSiteVpnGatewayConnectionConfigurationRouteOutputReference",
    "PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTable",
    "PointToSiteVpnGatewayConnectionConfigurationRoutePropagatedRouteTableOutputReference",
    "PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPool",
    "PointToSiteVpnGatewayConnectionConfigurationVpnClientAddressPoolOutputReference",
    "PointToSiteVpnGatewayTimeouts",
    "PointToSiteVpnGatewayTimeoutsOutputReference",
]

publication.publish()
