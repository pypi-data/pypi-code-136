'''
# `google_compute_network_peering`

Refer to the Terraform Registory for docs: [`google_compute_network_peering`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering).
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


class GoogleComputeNetworkPeering(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkPeering.GoogleComputeNetworkPeering",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering google_compute_network_peering}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        network: builtins.str,
        peer_network: builtins.str,
        export_custom_routes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        export_subnet_routes_with_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        import_custom_routes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        import_subnet_routes_with_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeNetworkPeeringTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering google_compute_network_peering} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the peering. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#name GoogleComputeNetworkPeering#name}
        :param network: The primary network of the peering. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#network GoogleComputeNetworkPeering#network}
        :param peer_network: The peer network in the peering. The peer network may belong to a different project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#peer_network GoogleComputeNetworkPeering#peer_network}
        :param export_custom_routes: Whether to export the custom routes to the peer network. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#export_custom_routes GoogleComputeNetworkPeering#export_custom_routes}
        :param export_subnet_routes_with_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#export_subnet_routes_with_public_ip GoogleComputeNetworkPeering#export_subnet_routes_with_public_ip}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#id GoogleComputeNetworkPeering#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_custom_routes: Whether to export the custom routes from the peer network. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#import_custom_routes GoogleComputeNetworkPeering#import_custom_routes}
        :param import_subnet_routes_with_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#import_subnet_routes_with_public_ip GoogleComputeNetworkPeering#import_subnet_routes_with_public_ip}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#timeouts GoogleComputeNetworkPeering#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeNetworkPeering.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeNetworkPeeringConfig(
            name=name,
            network=network,
            peer_network=peer_network,
            export_custom_routes=export_custom_routes,
            export_subnet_routes_with_public_ip=export_subnet_routes_with_public_ip,
            id=id,
            import_custom_routes=import_custom_routes,
            import_subnet_routes_with_public_ip=import_subnet_routes_with_public_ip,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#create GoogleComputeNetworkPeering#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#delete GoogleComputeNetworkPeering#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#update GoogleComputeNetworkPeering#update}.
        '''
        value = GoogleComputeNetworkPeeringTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetExportCustomRoutes")
    def reset_export_custom_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExportCustomRoutes", []))

    @jsii.member(jsii_name="resetExportSubnetRoutesWithPublicIp")
    def reset_export_subnet_routes_with_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExportSubnetRoutesWithPublicIp", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportCustomRoutes")
    def reset_import_custom_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportCustomRoutes", []))

    @jsii.member(jsii_name="resetImportSubnetRoutesWithPublicIp")
    def reset_import_subnet_routes_with_public_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportSubnetRoutesWithPublicIp", []))

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
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="stateDetails")
    def state_details(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateDetails"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeNetworkPeeringTimeoutsOutputReference":
        return typing.cast("GoogleComputeNetworkPeeringTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="exportCustomRoutesInput")
    def export_custom_routes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "exportCustomRoutesInput"))

    @builtins.property
    @jsii.member(jsii_name="exportSubnetRoutesWithPublicIpInput")
    def export_subnet_routes_with_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "exportSubnetRoutesWithPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importCustomRoutesInput")
    def import_custom_routes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "importCustomRoutesInput"))

    @builtins.property
    @jsii.member(jsii_name="importSubnetRoutesWithPublicIpInput")
    def import_subnet_routes_with_public_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "importSubnetRoutesWithPublicIpInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="peerNetworkInput")
    def peer_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeNetworkPeeringTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeNetworkPeeringTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="exportCustomRoutes")
    def export_custom_routes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "exportCustomRoutes"))

    @export_custom_routes.setter
    def export_custom_routes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "export_custom_routes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exportCustomRoutes", value)

    @builtins.property
    @jsii.member(jsii_name="exportSubnetRoutesWithPublicIp")
    def export_subnet_routes_with_public_ip(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "exportSubnetRoutesWithPublicIp"))

    @export_subnet_routes_with_public_ip.setter
    def export_subnet_routes_with_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "export_subnet_routes_with_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exportSubnetRoutesWithPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importCustomRoutes")
    def import_custom_routes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "importCustomRoutes"))

    @import_custom_routes.setter
    def import_custom_routes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "import_custom_routes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importCustomRoutes", value)

    @builtins.property
    @jsii.member(jsii_name="importSubnetRoutesWithPublicIp")
    def import_subnet_routes_with_public_ip(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "importSubnetRoutesWithPublicIp"))

    @import_subnet_routes_with_public_ip.setter
    def import_subnet_routes_with_public_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "import_subnet_routes_with_public_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importSubnetRoutesWithPublicIp", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="peerNetwork")
    def peer_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerNetwork"))

    @peer_network.setter
    def peer_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeering, "peer_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerNetwork", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkPeering.GoogleComputeNetworkPeeringConfig",
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
        "network": "network",
        "peer_network": "peerNetwork",
        "export_custom_routes": "exportCustomRoutes",
        "export_subnet_routes_with_public_ip": "exportSubnetRoutesWithPublicIp",
        "id": "id",
        "import_custom_routes": "importCustomRoutes",
        "import_subnet_routes_with_public_ip": "importSubnetRoutesWithPublicIp",
        "timeouts": "timeouts",
    },
)
class GoogleComputeNetworkPeeringConfig(cdktf.TerraformMetaArguments):
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
        network: builtins.str,
        peer_network: builtins.str,
        export_custom_routes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        export_subnet_routes_with_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        import_custom_routes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        import_subnet_routes_with_public_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeNetworkPeeringTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the peering. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#name GoogleComputeNetworkPeering#name}
        :param network: The primary network of the peering. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#network GoogleComputeNetworkPeering#network}
        :param peer_network: The peer network in the peering. The peer network may belong to a different project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#peer_network GoogleComputeNetworkPeering#peer_network}
        :param export_custom_routes: Whether to export the custom routes to the peer network. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#export_custom_routes GoogleComputeNetworkPeering#export_custom_routes}
        :param export_subnet_routes_with_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#export_subnet_routes_with_public_ip GoogleComputeNetworkPeering#export_subnet_routes_with_public_ip}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#id GoogleComputeNetworkPeering#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_custom_routes: Whether to export the custom routes from the peer network. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#import_custom_routes GoogleComputeNetworkPeering#import_custom_routes}
        :param import_subnet_routes_with_public_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#import_subnet_routes_with_public_ip GoogleComputeNetworkPeering#import_subnet_routes_with_public_ip}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#timeouts GoogleComputeNetworkPeering#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeNetworkPeeringTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeNetworkPeeringConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument peer_network", value=peer_network, expected_type=type_hints["peer_network"])
            check_type(argname="argument export_custom_routes", value=export_custom_routes, expected_type=type_hints["export_custom_routes"])
            check_type(argname="argument export_subnet_routes_with_public_ip", value=export_subnet_routes_with_public_ip, expected_type=type_hints["export_subnet_routes_with_public_ip"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument import_custom_routes", value=import_custom_routes, expected_type=type_hints["import_custom_routes"])
            check_type(argname="argument import_subnet_routes_with_public_ip", value=import_subnet_routes_with_public_ip, expected_type=type_hints["import_subnet_routes_with_public_ip"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "network": network,
            "peer_network": peer_network,
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
        if export_custom_routes is not None:
            self._values["export_custom_routes"] = export_custom_routes
        if export_subnet_routes_with_public_ip is not None:
            self._values["export_subnet_routes_with_public_ip"] = export_subnet_routes_with_public_ip
        if id is not None:
            self._values["id"] = id
        if import_custom_routes is not None:
            self._values["import_custom_routes"] = import_custom_routes
        if import_subnet_routes_with_public_ip is not None:
            self._values["import_subnet_routes_with_public_ip"] = import_subnet_routes_with_public_ip
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
        '''Name of the peering.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#name GoogleComputeNetworkPeering#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The primary network of the peering.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#network GoogleComputeNetworkPeering#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peer_network(self) -> builtins.str:
        '''The peer network in the peering. The peer network may belong to a different project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#peer_network GoogleComputeNetworkPeering#peer_network}
        '''
        result = self._values.get("peer_network")
        assert result is not None, "Required property 'peer_network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def export_custom_routes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to export the custom routes to the peer network. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#export_custom_routes GoogleComputeNetworkPeering#export_custom_routes}
        '''
        result = self._values.get("export_custom_routes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def export_subnet_routes_with_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#export_subnet_routes_with_public_ip GoogleComputeNetworkPeering#export_subnet_routes_with_public_ip}.'''
        result = self._values.get("export_subnet_routes_with_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#id GoogleComputeNetworkPeering#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_custom_routes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to export the custom routes from the peer network. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#import_custom_routes GoogleComputeNetworkPeering#import_custom_routes}
        '''
        result = self._values.get("import_custom_routes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def import_subnet_routes_with_public_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#import_subnet_routes_with_public_ip GoogleComputeNetworkPeering#import_subnet_routes_with_public_ip}.'''
        result = self._values.get("import_subnet_routes_with_public_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeNetworkPeeringTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#timeouts GoogleComputeNetworkPeering#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeNetworkPeeringTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkPeeringConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkPeering.GoogleComputeNetworkPeeringTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeNetworkPeeringTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#create GoogleComputeNetworkPeering#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#delete GoogleComputeNetworkPeering#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#update GoogleComputeNetworkPeering#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeNetworkPeeringTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#create GoogleComputeNetworkPeering#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#delete GoogleComputeNetworkPeering#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_network_peering#update GoogleComputeNetworkPeering#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeNetworkPeeringTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeNetworkPeeringTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeNetworkPeering.GoogleComputeNetworkPeeringTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeNetworkPeeringTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeeringTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeeringTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeeringTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeNetworkPeeringTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeNetworkPeeringTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeNetworkPeeringTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeNetworkPeeringTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeNetworkPeering",
    "GoogleComputeNetworkPeeringConfig",
    "GoogleComputeNetworkPeeringTimeouts",
    "GoogleComputeNetworkPeeringTimeoutsOutputReference",
]

publication.publish()
