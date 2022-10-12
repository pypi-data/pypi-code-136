'''
# `google_compute_router_interface`

Refer to the Terraform Registory for docs: [`google_compute_router_interface`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface).
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


class GoogleComputeRouterInterface(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterInterface.GoogleComputeRouterInterface",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface google_compute_router_interface}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        router: builtins.str,
        id: typing.Optional[builtins.str] = None,
        interconnect_attachment: typing.Optional[builtins.str] = None,
        ip_range: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRouterInterfaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_tunnel: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface google_compute_router_interface} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: A unique name for the interface, required by GCE. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#name GoogleComputeRouterInterface#name}
        :param router: The name of the router this interface will be attached to. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#router GoogleComputeRouterInterface#router}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#id GoogleComputeRouterInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interconnect_attachment: The name or resource link to the VLAN interconnect for this interface. Changing this forces a new interface to be created. Only one of vpn_tunnel and interconnect_attachment can be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#interconnect_attachment GoogleComputeRouterInterface#interconnect_attachment}
        :param ip_range: IP address and range of the interface. The IP range must be in the RFC3927 link-local IP space. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#ip_range GoogleComputeRouterInterface#ip_range}
        :param project: The ID of the project in which this interface's router belongs. If it is not provided, the provider project is used. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#project GoogleComputeRouterInterface#project}
        :param region: The region this interface's router sits in. If not specified, the project region will be used. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#region GoogleComputeRouterInterface#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#timeouts GoogleComputeRouterInterface#timeouts}
        :param vpn_tunnel: The name or resource link to the VPN tunnel this interface will be linked to. Changing this forces a new interface to be created. Only one of vpn_tunnel and interconnect_attachment can be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#vpn_tunnel GoogleComputeRouterInterface#vpn_tunnel}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterInterface.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRouterInterfaceConfig(
            name=name,
            router=router,
            id=id,
            interconnect_attachment=interconnect_attachment,
            ip_range=ip_range,
            project=project,
            region=region,
            timeouts=timeouts,
            vpn_tunnel=vpn_tunnel,
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
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#create GoogleComputeRouterInterface#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#delete GoogleComputeRouterInterface#delete}.
        '''
        value = GoogleComputeRouterInterfaceTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInterconnectAttachment")
    def reset_interconnect_attachment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterconnectAttachment", []))

    @jsii.member(jsii_name="resetIpRange")
    def reset_ip_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpRange", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVpnTunnel")
    def reset_vpn_tunnel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpnTunnel", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeRouterInterfaceTimeoutsOutputReference":
        return typing.cast("GoogleComputeRouterInterfaceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interconnectAttachmentInput")
    def interconnect_attachment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interconnectAttachmentInput"))

    @builtins.property
    @jsii.member(jsii_name="ipRangeInput")
    def ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="routerInput")
    def router_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routerInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeRouterInterfaceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRouterInterfaceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpnTunnelInput")
    def vpn_tunnel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpnTunnelInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="interconnectAttachment")
    def interconnect_attachment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interconnectAttachment"))

    @interconnect_attachment.setter
    def interconnect_attachment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "interconnect_attachment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interconnectAttachment", value)

    @builtins.property
    @jsii.member(jsii_name="ipRange")
    def ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipRange"))

    @ip_range.setter
    def ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRange", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="router")
    def router(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "router"))

    @router.setter
    def router(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "router").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "router", value)

    @builtins.property
    @jsii.member(jsii_name="vpnTunnel")
    def vpn_tunnel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpnTunnel"))

    @vpn_tunnel.setter
    def vpn_tunnel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterface, "vpn_tunnel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnTunnel", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterInterface.GoogleComputeRouterInterfaceConfig",
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
        "router": "router",
        "id": "id",
        "interconnect_attachment": "interconnectAttachment",
        "ip_range": "ipRange",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
        "vpn_tunnel": "vpnTunnel",
    },
)
class GoogleComputeRouterInterfaceConfig(cdktf.TerraformMetaArguments):
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
        router: builtins.str,
        id: typing.Optional[builtins.str] = None,
        interconnect_attachment: typing.Optional[builtins.str] = None,
        ip_range: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRouterInterfaceTimeouts", typing.Dict[str, typing.Any]]] = None,
        vpn_tunnel: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: A unique name for the interface, required by GCE. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#name GoogleComputeRouterInterface#name}
        :param router: The name of the router this interface will be attached to. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#router GoogleComputeRouterInterface#router}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#id GoogleComputeRouterInterface#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interconnect_attachment: The name or resource link to the VLAN interconnect for this interface. Changing this forces a new interface to be created. Only one of vpn_tunnel and interconnect_attachment can be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#interconnect_attachment GoogleComputeRouterInterface#interconnect_attachment}
        :param ip_range: IP address and range of the interface. The IP range must be in the RFC3927 link-local IP space. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#ip_range GoogleComputeRouterInterface#ip_range}
        :param project: The ID of the project in which this interface's router belongs. If it is not provided, the provider project is used. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#project GoogleComputeRouterInterface#project}
        :param region: The region this interface's router sits in. If not specified, the project region will be used. Changing this forces a new interface to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#region GoogleComputeRouterInterface#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#timeouts GoogleComputeRouterInterface#timeouts}
        :param vpn_tunnel: The name or resource link to the VPN tunnel this interface will be linked to. Changing this forces a new interface to be created. Only one of vpn_tunnel and interconnect_attachment can be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#vpn_tunnel GoogleComputeRouterInterface#vpn_tunnel}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRouterInterfaceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterInterfaceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument router", value=router, expected_type=type_hints["router"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument interconnect_attachment", value=interconnect_attachment, expected_type=type_hints["interconnect_attachment"])
            check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument vpn_tunnel", value=vpn_tunnel, expected_type=type_hints["vpn_tunnel"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "router": router,
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
        if interconnect_attachment is not None:
            self._values["interconnect_attachment"] = interconnect_attachment
        if ip_range is not None:
            self._values["ip_range"] = ip_range
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if vpn_tunnel is not None:
            self._values["vpn_tunnel"] = vpn_tunnel

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
        '''A unique name for the interface, required by GCE. Changing this forces a new interface to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#name GoogleComputeRouterInterface#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def router(self) -> builtins.str:
        '''The name of the router this interface will be attached to.

        Changing this forces a new interface to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#router GoogleComputeRouterInterface#router}
        '''
        result = self._values.get("router")
        assert result is not None, "Required property 'router' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#id GoogleComputeRouterInterface#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interconnect_attachment(self) -> typing.Optional[builtins.str]:
        '''The name or resource link to the VLAN interconnect for this interface.

        Changing this forces a new interface to be created. Only one of vpn_tunnel and interconnect_attachment can be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#interconnect_attachment GoogleComputeRouterInterface#interconnect_attachment}
        '''
        result = self._values.get("interconnect_attachment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_range(self) -> typing.Optional[builtins.str]:
        '''IP address and range of the interface.

        The IP range must be in the RFC3927 link-local IP space. Changing this forces a new interface to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#ip_range GoogleComputeRouterInterface#ip_range}
        '''
        result = self._values.get("ip_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which this interface's router belongs.

        If it is not provided, the provider project is used. Changing this forces a new interface to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#project GoogleComputeRouterInterface#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The region this interface's router sits in.

        If not specified, the project region will be used. Changing this forces a new interface to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#region GoogleComputeRouterInterface#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeRouterInterfaceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#timeouts GoogleComputeRouterInterface#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRouterInterfaceTimeouts"], result)

    @builtins.property
    def vpn_tunnel(self) -> typing.Optional[builtins.str]:
        '''The name or resource link to the VPN tunnel this interface will be linked to.

        Changing this forces a new interface to be created. Only one of vpn_tunnel and interconnect_attachment can be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#vpn_tunnel GoogleComputeRouterInterface#vpn_tunnel}
        '''
        result = self._values.get("vpn_tunnel")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouterInterfaceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterInterface.GoogleComputeRouterInterfaceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleComputeRouterInterfaceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#create GoogleComputeRouterInterface#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#delete GoogleComputeRouterInterface#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterInterfaceTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#create GoogleComputeRouterInterface#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_interface#delete GoogleComputeRouterInterface#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouterInterfaceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRouterInterfaceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterInterface.GoogleComputeRouterInterfaceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRouterInterfaceTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterfaceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterfaceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRouterInterfaceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRouterInterfaceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRouterInterfaceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterInterfaceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRouterInterface",
    "GoogleComputeRouterInterfaceConfig",
    "GoogleComputeRouterInterfaceTimeouts",
    "GoogleComputeRouterInterfaceTimeoutsOutputReference",
]

publication.publish()
