'''
# `azurerm_virtual_hub_connection`

Refer to the Terraform Registory for docs: [`azurerm_virtual_hub_connection`](https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection).
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


class VirtualHubConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection azurerm_virtual_hub_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        remote_virtual_network_id: builtins.str,
        virtual_hub_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        internet_security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        routing: typing.Optional[typing.Union["VirtualHubConnectionRouting", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["VirtualHubConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection azurerm_virtual_hub_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#name VirtualHubConnection#name}.
        :param remote_virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#remote_virtual_network_id VirtualHubConnection#remote_virtual_network_id}.
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#virtual_hub_id VirtualHubConnection#virtual_hub_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#id VirtualHubConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_security_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#internet_security_enabled VirtualHubConnection#internet_security_enabled}.
        :param routing: routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#routing VirtualHubConnection#routing}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#timeouts VirtualHubConnection#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VirtualHubConnectionConfig(
            name=name,
            remote_virtual_network_id=remote_virtual_network_id,
            virtual_hub_id=virtual_hub_id,
            id=id,
            internet_security_enabled=internet_security_enabled,
            routing=routing,
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

    @jsii.member(jsii_name="putRouting")
    def put_routing(
        self,
        *,
        associated_route_table_id: typing.Optional[builtins.str] = None,
        propagated_route_table: typing.Optional[typing.Union["VirtualHubConnectionRoutingPropagatedRouteTable", typing.Dict[str, typing.Any]]] = None,
        static_vnet_route: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualHubConnectionRoutingStaticVnetRoute", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param associated_route_table_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#associated_route_table_id VirtualHubConnection#associated_route_table_id}.
        :param propagated_route_table: propagated_route_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#propagated_route_table VirtualHubConnection#propagated_route_table}
        :param static_vnet_route: static_vnet_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#static_vnet_route VirtualHubConnection#static_vnet_route}
        '''
        value = VirtualHubConnectionRouting(
            associated_route_table_id=associated_route_table_id,
            propagated_route_table=propagated_route_table,
            static_vnet_route=static_vnet_route,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#create VirtualHubConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#delete VirtualHubConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#read VirtualHubConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#update VirtualHubConnection#update}.
        '''
        value = VirtualHubConnectionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

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

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="routing")
    def routing(self) -> "VirtualHubConnectionRoutingOutputReference":
        return typing.cast("VirtualHubConnectionRoutingOutputReference", jsii.get(self, "routing"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "VirtualHubConnectionTimeoutsOutputReference":
        return typing.cast("VirtualHubConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

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
    @jsii.member(jsii_name="remoteVirtualNetworkIdInput")
    def remote_virtual_network_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteVirtualNetworkIdInput"))

    @builtins.property
    @jsii.member(jsii_name="routingInput")
    def routing_input(self) -> typing.Optional["VirtualHubConnectionRouting"]:
        return typing.cast(typing.Optional["VirtualHubConnectionRouting"], jsii.get(self, "routingInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["VirtualHubConnectionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["VirtualHubConnectionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="virtualHubIdInput")
    def virtual_hub_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualHubIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnection, "id").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualHubConnection, "internet_security_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internetSecurityEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnection, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="remoteVirtualNetworkId")
    def remote_virtual_network_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "remoteVirtualNetworkId"))

    @remote_virtual_network_id.setter
    def remote_virtual_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnection, "remote_virtual_network_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteVirtualNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="virtualHubId")
    def virtual_hub_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "virtualHubId"))

    @virtual_hub_id.setter
    def virtual_hub_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnection, "virtual_hub_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualHubId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionConfig",
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
        "remote_virtual_network_id": "remoteVirtualNetworkId",
        "virtual_hub_id": "virtualHubId",
        "id": "id",
        "internet_security_enabled": "internetSecurityEnabled",
        "routing": "routing",
        "timeouts": "timeouts",
    },
)
class VirtualHubConnectionConfig(cdktf.TerraformMetaArguments):
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
        remote_virtual_network_id: builtins.str,
        virtual_hub_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        internet_security_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        routing: typing.Optional[typing.Union["VirtualHubConnectionRouting", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["VirtualHubConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#name VirtualHubConnection#name}.
        :param remote_virtual_network_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#remote_virtual_network_id VirtualHubConnection#remote_virtual_network_id}.
        :param virtual_hub_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#virtual_hub_id VirtualHubConnection#virtual_hub_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#id VirtualHubConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param internet_security_enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#internet_security_enabled VirtualHubConnection#internet_security_enabled}.
        :param routing: routing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#routing VirtualHubConnection#routing}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#timeouts VirtualHubConnection#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(routing, dict):
            routing = VirtualHubConnectionRouting(**routing)
        if isinstance(timeouts, dict):
            timeouts = VirtualHubConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument remote_virtual_network_id", value=remote_virtual_network_id, expected_type=type_hints["remote_virtual_network_id"])
            check_type(argname="argument virtual_hub_id", value=virtual_hub_id, expected_type=type_hints["virtual_hub_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument internet_security_enabled", value=internet_security_enabled, expected_type=type_hints["internet_security_enabled"])
            check_type(argname="argument routing", value=routing, expected_type=type_hints["routing"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "remote_virtual_network_id": remote_virtual_network_id,
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
        if id is not None:
            self._values["id"] = id
        if internet_security_enabled is not None:
            self._values["internet_security_enabled"] = internet_security_enabled
        if routing is not None:
            self._values["routing"] = routing
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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#name VirtualHubConnection#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def remote_virtual_network_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#remote_virtual_network_id VirtualHubConnection#remote_virtual_network_id}.'''
        result = self._values.get("remote_virtual_network_id")
        assert result is not None, "Required property 'remote_virtual_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_hub_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#virtual_hub_id VirtualHubConnection#virtual_hub_id}.'''
        result = self._values.get("virtual_hub_id")
        assert result is not None, "Required property 'virtual_hub_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#id VirtualHubConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internet_security_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#internet_security_enabled VirtualHubConnection#internet_security_enabled}.'''
        result = self._values.get("internet_security_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def routing(self) -> typing.Optional["VirtualHubConnectionRouting"]:
        '''routing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#routing VirtualHubConnection#routing}
        '''
        result = self._values.get("routing")
        return typing.cast(typing.Optional["VirtualHubConnectionRouting"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["VirtualHubConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#timeouts VirtualHubConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["VirtualHubConnectionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualHubConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionRouting",
    jsii_struct_bases=[],
    name_mapping={
        "associated_route_table_id": "associatedRouteTableId",
        "propagated_route_table": "propagatedRouteTable",
        "static_vnet_route": "staticVnetRoute",
    },
)
class VirtualHubConnectionRouting:
    def __init__(
        self,
        *,
        associated_route_table_id: typing.Optional[builtins.str] = None,
        propagated_route_table: typing.Optional[typing.Union["VirtualHubConnectionRoutingPropagatedRouteTable", typing.Dict[str, typing.Any]]] = None,
        static_vnet_route: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualHubConnectionRoutingStaticVnetRoute", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param associated_route_table_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#associated_route_table_id VirtualHubConnection#associated_route_table_id}.
        :param propagated_route_table: propagated_route_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#propagated_route_table VirtualHubConnection#propagated_route_table}
        :param static_vnet_route: static_vnet_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#static_vnet_route VirtualHubConnection#static_vnet_route}
        '''
        if isinstance(propagated_route_table, dict):
            propagated_route_table = VirtualHubConnectionRoutingPropagatedRouteTable(**propagated_route_table)
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnectionRouting.__init__)
            check_type(argname="argument associated_route_table_id", value=associated_route_table_id, expected_type=type_hints["associated_route_table_id"])
            check_type(argname="argument propagated_route_table", value=propagated_route_table, expected_type=type_hints["propagated_route_table"])
            check_type(argname="argument static_vnet_route", value=static_vnet_route, expected_type=type_hints["static_vnet_route"])
        self._values: typing.Dict[str, typing.Any] = {}
        if associated_route_table_id is not None:
            self._values["associated_route_table_id"] = associated_route_table_id
        if propagated_route_table is not None:
            self._values["propagated_route_table"] = propagated_route_table
        if static_vnet_route is not None:
            self._values["static_vnet_route"] = static_vnet_route

    @builtins.property
    def associated_route_table_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#associated_route_table_id VirtualHubConnection#associated_route_table_id}.'''
        result = self._values.get("associated_route_table_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagated_route_table(
        self,
    ) -> typing.Optional["VirtualHubConnectionRoutingPropagatedRouteTable"]:
        '''propagated_route_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#propagated_route_table VirtualHubConnection#propagated_route_table}
        '''
        result = self._values.get("propagated_route_table")
        return typing.cast(typing.Optional["VirtualHubConnectionRoutingPropagatedRouteTable"], result)

    @builtins.property
    def static_vnet_route(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualHubConnectionRoutingStaticVnetRoute"]]]:
        '''static_vnet_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#static_vnet_route VirtualHubConnection#static_vnet_route}
        '''
        result = self._values.get("static_vnet_route")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualHubConnectionRoutingStaticVnetRoute"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualHubConnectionRouting(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualHubConnectionRoutingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionRoutingOutputReference",
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
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPropagatedRouteTable")
    def put_propagated_route_table(
        self,
        *,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#labels VirtualHubConnection#labels}.
        :param route_table_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#route_table_ids VirtualHubConnection#route_table_ids}.
        '''
        value = VirtualHubConnectionRoutingPropagatedRouteTable(
            labels=labels, route_table_ids=route_table_ids
        )

        return typing.cast(None, jsii.invoke(self, "putPropagatedRouteTable", [value]))

    @jsii.member(jsii_name="putStaticVnetRoute")
    def put_static_vnet_route(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["VirtualHubConnectionRoutingStaticVnetRoute", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingOutputReference.put_static_vnet_route)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStaticVnetRoute", [value]))

    @jsii.member(jsii_name="resetAssociatedRouteTableId")
    def reset_associated_route_table_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatedRouteTableId", []))

    @jsii.member(jsii_name="resetPropagatedRouteTable")
    def reset_propagated_route_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPropagatedRouteTable", []))

    @jsii.member(jsii_name="resetStaticVnetRoute")
    def reset_static_vnet_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticVnetRoute", []))

    @builtins.property
    @jsii.member(jsii_name="propagatedRouteTable")
    def propagated_route_table(
        self,
    ) -> "VirtualHubConnectionRoutingPropagatedRouteTableOutputReference":
        return typing.cast("VirtualHubConnectionRoutingPropagatedRouteTableOutputReference", jsii.get(self, "propagatedRouteTable"))

    @builtins.property
    @jsii.member(jsii_name="staticVnetRoute")
    def static_vnet_route(self) -> "VirtualHubConnectionRoutingStaticVnetRouteList":
        return typing.cast("VirtualHubConnectionRoutingStaticVnetRouteList", jsii.get(self, "staticVnetRoute"))

    @builtins.property
    @jsii.member(jsii_name="associatedRouteTableIdInput")
    def associated_route_table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associatedRouteTableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="propagatedRouteTableInput")
    def propagated_route_table_input(
        self,
    ) -> typing.Optional["VirtualHubConnectionRoutingPropagatedRouteTable"]:
        return typing.cast(typing.Optional["VirtualHubConnectionRoutingPropagatedRouteTable"], jsii.get(self, "propagatedRouteTableInput"))

    @builtins.property
    @jsii.member(jsii_name="staticVnetRouteInput")
    def static_vnet_route_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualHubConnectionRoutingStaticVnetRoute"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["VirtualHubConnectionRoutingStaticVnetRoute"]]], jsii.get(self, "staticVnetRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="associatedRouteTableId")
    def associated_route_table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedRouteTableId"))

    @associated_route_table_id.setter
    def associated_route_table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingOutputReference, "associated_route_table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedRouteTableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[VirtualHubConnectionRouting]:
        return typing.cast(typing.Optional[VirtualHubConnectionRouting], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualHubConnectionRouting],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionRoutingPropagatedRouteTable",
    jsii_struct_bases=[],
    name_mapping={"labels": "labels", "route_table_ids": "routeTableIds"},
)
class VirtualHubConnectionRoutingPropagatedRouteTable:
    def __init__(
        self,
        *,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        route_table_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param labels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#labels VirtualHubConnection#labels}.
        :param route_table_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#route_table_ids VirtualHubConnection#route_table_ids}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingPropagatedRouteTable.__init__)
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument route_table_ids", value=route_table_ids, expected_type=type_hints["route_table_ids"])
        self._values: typing.Dict[str, typing.Any] = {}
        if labels is not None:
            self._values["labels"] = labels
        if route_table_ids is not None:
            self._values["route_table_ids"] = route_table_ids

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#labels VirtualHubConnection#labels}.'''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def route_table_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#route_table_ids VirtualHubConnection#route_table_ids}.'''
        result = self._values.get("route_table_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualHubConnectionRoutingPropagatedRouteTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualHubConnectionRoutingPropagatedRouteTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionRoutingPropagatedRouteTableOutputReference",
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
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingPropagatedRouteTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetRouteTableIds")
    def reset_route_table_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRouteTableIds", []))

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
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingPropagatedRouteTableOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="routeTableIds")
    def route_table_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "routeTableIds"))

    @route_table_ids.setter
    def route_table_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingPropagatedRouteTableOutputReference, "route_table_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeTableIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[VirtualHubConnectionRoutingPropagatedRouteTable]:
        return typing.cast(typing.Optional[VirtualHubConnectionRoutingPropagatedRouteTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[VirtualHubConnectionRoutingPropagatedRouteTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingPropagatedRouteTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionRoutingStaticVnetRoute",
    jsii_struct_bases=[],
    name_mapping={
        "address_prefixes": "addressPrefixes",
        "name": "name",
        "next_hop_ip_address": "nextHopIpAddress",
    },
)
class VirtualHubConnectionRoutingStaticVnetRoute:
    def __init__(
        self,
        *,
        address_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        next_hop_ip_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param address_prefixes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#address_prefixes VirtualHubConnection#address_prefixes}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#name VirtualHubConnection#name}.
        :param next_hop_ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#next_hop_ip_address VirtualHubConnection#next_hop_ip_address}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingStaticVnetRoute.__init__)
            check_type(argname="argument address_prefixes", value=address_prefixes, expected_type=type_hints["address_prefixes"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument next_hop_ip_address", value=next_hop_ip_address, expected_type=type_hints["next_hop_ip_address"])
        self._values: typing.Dict[str, typing.Any] = {}
        if address_prefixes is not None:
            self._values["address_prefixes"] = address_prefixes
        if name is not None:
            self._values["name"] = name
        if next_hop_ip_address is not None:
            self._values["next_hop_ip_address"] = next_hop_ip_address

    @builtins.property
    def address_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#address_prefixes VirtualHubConnection#address_prefixes}.'''
        result = self._values.get("address_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#name VirtualHubConnection#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hop_ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#next_hop_ip_address VirtualHubConnection#next_hop_ip_address}.'''
        result = self._values.get("next_hop_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualHubConnectionRoutingStaticVnetRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualHubConnectionRoutingStaticVnetRouteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionRoutingStaticVnetRouteList",
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
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingStaticVnetRouteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "VirtualHubConnectionRoutingStaticVnetRouteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingStaticVnetRouteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("VirtualHubConnectionRoutingStaticVnetRouteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualHubConnectionRoutingStaticVnetRoute]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualHubConnectionRoutingStaticVnetRoute]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[VirtualHubConnectionRoutingStaticVnetRoute]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class VirtualHubConnectionRoutingStaticVnetRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionRoutingStaticVnetRouteOutputReference",
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
            type_hints = typing.get_type_hints(VirtualHubConnectionRoutingStaticVnetRouteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAddressPrefixes")
    def reset_address_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAddressPrefixes", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNextHopIpAddress")
    def reset_next_hop_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHopIpAddress", []))

    @builtins.property
    @jsii.member(jsii_name="addressPrefixesInput")
    def address_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressPrefixesInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopIpAddressInput")
    def next_hop_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="addressPrefixes")
    def address_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addressPrefixes"))

    @address_prefixes.setter
    def address_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteOutputReference, "address_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addressPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopIpAddress")
    def next_hop_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopIpAddress"))

    @next_hop_ip_address.setter
    def next_hop_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteOutputReference, "next_hop_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualHubConnectionRoutingStaticVnetRoute, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualHubConnectionRoutingStaticVnetRoute, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualHubConnectionRoutingStaticVnetRoute, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionRoutingStaticVnetRouteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class VirtualHubConnectionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#create VirtualHubConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#delete VirtualHubConnection#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#read VirtualHubConnection#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#update VirtualHubConnection#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VirtualHubConnectionTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#create VirtualHubConnection#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#delete VirtualHubConnection#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#read VirtualHubConnection#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/virtual_hub_connection#update VirtualHubConnection#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualHubConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VirtualHubConnectionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.virtualHubConnection.VirtualHubConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(VirtualHubConnectionTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[VirtualHubConnectionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[VirtualHubConnectionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[VirtualHubConnectionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VirtualHubConnectionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "VirtualHubConnection",
    "VirtualHubConnectionConfig",
    "VirtualHubConnectionRouting",
    "VirtualHubConnectionRoutingOutputReference",
    "VirtualHubConnectionRoutingPropagatedRouteTable",
    "VirtualHubConnectionRoutingPropagatedRouteTableOutputReference",
    "VirtualHubConnectionRoutingStaticVnetRoute",
    "VirtualHubConnectionRoutingStaticVnetRouteList",
    "VirtualHubConnectionRoutingStaticVnetRouteOutputReference",
    "VirtualHubConnectionTimeouts",
    "VirtualHubConnectionTimeoutsOutputReference",
]

publication.publish()
