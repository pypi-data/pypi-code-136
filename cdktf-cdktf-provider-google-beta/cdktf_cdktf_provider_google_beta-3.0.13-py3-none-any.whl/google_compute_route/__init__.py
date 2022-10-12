'''
# `google_compute_route`

Refer to the Terraform Registory for docs: [`google_compute_route`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_route).
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


class GoogleComputeRoute(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRoute.GoogleComputeRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route google_compute_route}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dest_range: builtins.str,
        name: builtins.str,
        network: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        next_hop_gateway: typing.Optional[builtins.str] = None,
        next_hop_ilb: typing.Optional[builtins.str] = None,
        next_hop_instance: typing.Optional[builtins.str] = None,
        next_hop_instance_zone: typing.Optional[builtins.str] = None,
        next_hop_ip: typing.Optional[builtins.str] = None,
        next_hop_vpn_tunnel: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRouteTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route google_compute_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dest_range: The destination range of outgoing packets that this route applies to. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#dest_range GoogleComputeRoute#dest_range}
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#name GoogleComputeRoute#name}
        :param network: The network that this route applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#network GoogleComputeRoute#network}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#description GoogleComputeRoute#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#id GoogleComputeRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param next_hop_gateway: URL to a gateway that should handle matching packets. Currently, you can only specify the internet gateway, using a full or partial valid URL: 'https://www.googleapis.com/compute/v1/projects/project/global/gateways/default-internet-gateway' 'projects/project/global/gateways/default-internet-gateway' 'global/gateways/default-internet-gateway' The string 'default-internet-gateway'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_gateway GoogleComputeRoute#next_hop_gateway}
        :param next_hop_ilb: The IP address or URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets. With the GA provider you can only specify the forwarding rule as a partial or full URL. For example, the following are all valid values: 10.128.0.56 https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule regions/region/forwardingRules/forwardingRule When the beta provider, you can also specify the IP address of a forwarding rule from the same VPC or any peered VPC. Note that this can only be used when the destinationRange is a public (non-RFC 1918) IP CIDR range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_ilb GoogleComputeRoute#next_hop_ilb}
        :param next_hop_instance: URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example: 'https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance' 'projects/project/zones/zone/instances/instance' 'zones/zone/instances/instance' Just the instance name, with the zone in 'next_hop_instance_zone'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_instance GoogleComputeRoute#next_hop_instance}
        :param next_hop_instance_zone: The zone of the instance specified in next_hop_instance. Omit if next_hop_instance is specified as a URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_instance_zone GoogleComputeRoute#next_hop_instance_zone}
        :param next_hop_ip: Network IP address of an instance that should handle matching packets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_ip GoogleComputeRoute#next_hop_ip}
        :param next_hop_vpn_tunnel: URL to a VpnTunnel that should handle matching packets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_vpn_tunnel GoogleComputeRoute#next_hop_vpn_tunnel}
        :param priority: The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In the case of two routes with equal prefix length, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#priority GoogleComputeRoute#priority}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#project GoogleComputeRoute#project}.
        :param tags: A list of instance tags to which this route applies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#tags GoogleComputeRoute#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#timeouts GoogleComputeRoute#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRoute.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRouteConfig(
            dest_range=dest_range,
            name=name,
            network=network,
            description=description,
            id=id,
            next_hop_gateway=next_hop_gateway,
            next_hop_ilb=next_hop_ilb,
            next_hop_instance=next_hop_instance,
            next_hop_instance_zone=next_hop_instance_zone,
            next_hop_ip=next_hop_ip,
            next_hop_vpn_tunnel=next_hop_vpn_tunnel,
            priority=priority,
            project=project,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#create GoogleComputeRoute#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#delete GoogleComputeRoute#delete}.
        '''
        value = GoogleComputeRouteTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNextHopGateway")
    def reset_next_hop_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHopGateway", []))

    @jsii.member(jsii_name="resetNextHopIlb")
    def reset_next_hop_ilb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHopIlb", []))

    @jsii.member(jsii_name="resetNextHopInstance")
    def reset_next_hop_instance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHopInstance", []))

    @jsii.member(jsii_name="resetNextHopInstanceZone")
    def reset_next_hop_instance_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHopInstanceZone", []))

    @jsii.member(jsii_name="resetNextHopIp")
    def reset_next_hop_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHopIp", []))

    @jsii.member(jsii_name="resetNextHopVpnTunnel")
    def reset_next_hop_vpn_tunnel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNextHopVpnTunnel", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="nextHopNetwork")
    def next_hop_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopNetwork"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeRouteTimeoutsOutputReference":
        return typing.cast("GoogleComputeRouteTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destRangeInput")
    def dest_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopGatewayInput")
    def next_hop_gateway_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopIlbInput")
    def next_hop_ilb_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopIlbInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopInstanceInput")
    def next_hop_instance_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopInstanceInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopInstanceZoneInput")
    def next_hop_instance_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopInstanceZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopIpInput")
    def next_hop_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopIpInput"))

    @builtins.property
    @jsii.member(jsii_name="nextHopVpnTunnelInput")
    def next_hop_vpn_tunnel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextHopVpnTunnelInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeRouteTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRouteTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destRange")
    def dest_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destRange"))

    @dest_range.setter
    def dest_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "dest_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destRange", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopGateway")
    def next_hop_gateway(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopGateway"))

    @next_hop_gateway.setter
    def next_hop_gateway(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "next_hop_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopGateway", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopIlb")
    def next_hop_ilb(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopIlb"))

    @next_hop_ilb.setter
    def next_hop_ilb(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "next_hop_ilb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopIlb", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopInstance")
    def next_hop_instance(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopInstance"))

    @next_hop_instance.setter
    def next_hop_instance(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "next_hop_instance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopInstance", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopInstanceZone")
    def next_hop_instance_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopInstanceZone"))

    @next_hop_instance_zone.setter
    def next_hop_instance_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "next_hop_instance_zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopInstanceZone", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopIp")
    def next_hop_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopIp"))

    @next_hop_ip.setter
    def next_hop_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "next_hop_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopIp", value)

    @builtins.property
    @jsii.member(jsii_name="nextHopVpnTunnel")
    def next_hop_vpn_tunnel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextHopVpnTunnel"))

    @next_hop_vpn_tunnel.setter
    def next_hop_vpn_tunnel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "next_hop_vpn_tunnel").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextHopVpnTunnel", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRoute, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRoute.GoogleComputeRouteConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dest_range": "destRange",
        "name": "name",
        "network": "network",
        "description": "description",
        "id": "id",
        "next_hop_gateway": "nextHopGateway",
        "next_hop_ilb": "nextHopIlb",
        "next_hop_instance": "nextHopInstance",
        "next_hop_instance_zone": "nextHopInstanceZone",
        "next_hop_ip": "nextHopIp",
        "next_hop_vpn_tunnel": "nextHopVpnTunnel",
        "priority": "priority",
        "project": "project",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class GoogleComputeRouteConfig(cdktf.TerraformMetaArguments):
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
        dest_range: builtins.str,
        name: builtins.str,
        network: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        next_hop_gateway: typing.Optional[builtins.str] = None,
        next_hop_ilb: typing.Optional[builtins.str] = None,
        next_hop_instance: typing.Optional[builtins.str] = None,
        next_hop_instance_zone: typing.Optional[builtins.str] = None,
        next_hop_ip: typing.Optional[builtins.str] = None,
        next_hop_vpn_tunnel: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRouteTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dest_range: The destination range of outgoing packets that this route applies to. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#dest_range GoogleComputeRoute#dest_range}
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#name GoogleComputeRoute#name}
        :param network: The network that this route applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#network GoogleComputeRoute#network}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#description GoogleComputeRoute#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#id GoogleComputeRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param next_hop_gateway: URL to a gateway that should handle matching packets. Currently, you can only specify the internet gateway, using a full or partial valid URL: 'https://www.googleapis.com/compute/v1/projects/project/global/gateways/default-internet-gateway' 'projects/project/global/gateways/default-internet-gateway' 'global/gateways/default-internet-gateway' The string 'default-internet-gateway'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_gateway GoogleComputeRoute#next_hop_gateway}
        :param next_hop_ilb: The IP address or URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets. With the GA provider you can only specify the forwarding rule as a partial or full URL. For example, the following are all valid values: 10.128.0.56 https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule regions/region/forwardingRules/forwardingRule When the beta provider, you can also specify the IP address of a forwarding rule from the same VPC or any peered VPC. Note that this can only be used when the destinationRange is a public (non-RFC 1918) IP CIDR range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_ilb GoogleComputeRoute#next_hop_ilb}
        :param next_hop_instance: URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example: 'https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance' 'projects/project/zones/zone/instances/instance' 'zones/zone/instances/instance' Just the instance name, with the zone in 'next_hop_instance_zone'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_instance GoogleComputeRoute#next_hop_instance}
        :param next_hop_instance_zone: The zone of the instance specified in next_hop_instance. Omit if next_hop_instance is specified as a URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_instance_zone GoogleComputeRoute#next_hop_instance_zone}
        :param next_hop_ip: Network IP address of an instance that should handle matching packets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_ip GoogleComputeRoute#next_hop_ip}
        :param next_hop_vpn_tunnel: URL to a VpnTunnel that should handle matching packets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_vpn_tunnel GoogleComputeRoute#next_hop_vpn_tunnel}
        :param priority: The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In the case of two routes with equal prefix length, the one with the lowest-numbered priority value wins. Default value is 1000. Valid range is 0 through 65535. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#priority GoogleComputeRoute#priority}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#project GoogleComputeRoute#project}.
        :param tags: A list of instance tags to which this route applies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#tags GoogleComputeRoute#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#timeouts GoogleComputeRoute#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRouteTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouteConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dest_range", value=dest_range, expected_type=type_hints["dest_range"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument next_hop_gateway", value=next_hop_gateway, expected_type=type_hints["next_hop_gateway"])
            check_type(argname="argument next_hop_ilb", value=next_hop_ilb, expected_type=type_hints["next_hop_ilb"])
            check_type(argname="argument next_hop_instance", value=next_hop_instance, expected_type=type_hints["next_hop_instance"])
            check_type(argname="argument next_hop_instance_zone", value=next_hop_instance_zone, expected_type=type_hints["next_hop_instance_zone"])
            check_type(argname="argument next_hop_ip", value=next_hop_ip, expected_type=type_hints["next_hop_ip"])
            check_type(argname="argument next_hop_vpn_tunnel", value=next_hop_vpn_tunnel, expected_type=type_hints["next_hop_vpn_tunnel"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "dest_range": dest_range,
            "name": name,
            "network": network,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if next_hop_gateway is not None:
            self._values["next_hop_gateway"] = next_hop_gateway
        if next_hop_ilb is not None:
            self._values["next_hop_ilb"] = next_hop_ilb
        if next_hop_instance is not None:
            self._values["next_hop_instance"] = next_hop_instance
        if next_hop_instance_zone is not None:
            self._values["next_hop_instance_zone"] = next_hop_instance_zone
        if next_hop_ip is not None:
            self._values["next_hop_ip"] = next_hop_ip
        if next_hop_vpn_tunnel is not None:
            self._values["next_hop_vpn_tunnel"] = next_hop_vpn_tunnel
        if priority is not None:
            self._values["priority"] = priority
        if project is not None:
            self._values["project"] = project
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
    def dest_range(self) -> builtins.str:
        '''The destination range of outgoing packets that this route applies to. Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#dest_range GoogleComputeRoute#dest_range}
        '''
        result = self._values.get("dest_range")
        assert result is not None, "Required property 'dest_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035.  Specifically, the name must be 1-63 characters long and
        match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means
        the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the
        last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#name GoogleComputeRoute#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The network that this route applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#network GoogleComputeRoute#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#description GoogleComputeRoute#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#id GoogleComputeRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hop_gateway(self) -> typing.Optional[builtins.str]:
        '''URL to a gateway that should handle matching packets.

        Currently, you can only specify the internet gateway, using a full or
        partial valid URL:
        'https://www.googleapis.com/compute/v1/projects/project/global/gateways/default-internet-gateway'
        'projects/project/global/gateways/default-internet-gateway'
        'global/gateways/default-internet-gateway'
        The string 'default-internet-gateway'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_gateway GoogleComputeRoute#next_hop_gateway}
        '''
        result = self._values.get("next_hop_gateway")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hop_ilb(self) -> typing.Optional[builtins.str]:
        '''The IP address or URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets.

        With the GA provider you can only specify the forwarding
        rule as a partial or full URL. For example, the following
        are all valid values:
        10.128.0.56
        https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule
        regions/region/forwardingRules/forwardingRule

        When the beta provider, you can also specify the IP address
        of a forwarding rule from the same VPC or any peered VPC.

        Note that this can only be used when the destinationRange is
        a public (non-RFC 1918) IP CIDR range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_ilb GoogleComputeRoute#next_hop_ilb}
        '''
        result = self._values.get("next_hop_ilb")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hop_instance(self) -> typing.Optional[builtins.str]:
        '''URL to an instance that should handle matching packets.

        You can specify this as a full or partial URL. For example:
        'https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance'
        'projects/project/zones/zone/instances/instance'
        'zones/zone/instances/instance'
        Just the instance name, with the zone in 'next_hop_instance_zone'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_instance GoogleComputeRoute#next_hop_instance}
        '''
        result = self._values.get("next_hop_instance")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hop_instance_zone(self) -> typing.Optional[builtins.str]:
        '''The zone of the instance specified in next_hop_instance. Omit if next_hop_instance is specified as a URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_instance_zone GoogleComputeRoute#next_hop_instance_zone}
        '''
        result = self._values.get("next_hop_instance_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hop_ip(self) -> typing.Optional[builtins.str]:
        '''Network IP address of an instance that should handle matching packets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_ip GoogleComputeRoute#next_hop_ip}
        '''
        result = self._values.get("next_hop_ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_hop_vpn_tunnel(self) -> typing.Optional[builtins.str]:
        '''URL to a VpnTunnel that should handle matching packets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#next_hop_vpn_tunnel GoogleComputeRoute#next_hop_vpn_tunnel}
        '''
        result = self._values.get("next_hop_vpn_tunnel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority of this route.

        Priority is used to break ties in cases
        where there is more than one matching route of equal prefix length.

        In the case of two routes with equal prefix length, the one with the
        lowest-numbered priority value wins.

        Default value is 1000. Valid range is 0 through 65535.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#priority GoogleComputeRoute#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#project GoogleComputeRoute#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of instance tags to which this route applies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#tags GoogleComputeRoute#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeRouteTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#timeouts GoogleComputeRoute#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRouteTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRoute.GoogleComputeRouteTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleComputeRouteTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#create GoogleComputeRoute#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#delete GoogleComputeRoute#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouteTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#create GoogleComputeRoute#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_route#delete GoogleComputeRoute#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouteTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRouteTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRoute.GoogleComputeRouteTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRouteTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouteTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouteTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRouteTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRouteTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRouteTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouteTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRoute",
    "GoogleComputeRouteConfig",
    "GoogleComputeRouteTimeouts",
    "GoogleComputeRouteTimeoutsOutputReference",
]

publication.publish()
