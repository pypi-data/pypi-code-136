'''
# `google_compute_router_peer`

Refer to the Terraform Registory for docs: [`google_compute_router_peer`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer).
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


class GoogleComputeRouterPeer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer google_compute_router_peer}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        interface: builtins.str,
        name: builtins.str,
        peer_asn: jsii.Number,
        peer_ip_address: builtins.str,
        router: builtins.str,
        advertised_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        advertised_ip_ranges: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRouterPeerAdvertisedIpRanges", typing.Dict[str, typing.Any]]]]] = None,
        advertised_route_priority: typing.Optional[jsii.Number] = None,
        advertise_mode: typing.Optional[builtins.str] = None,
        bfd: typing.Optional[typing.Union["GoogleComputeRouterPeerBfd", typing.Dict[str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_address: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRouterPeerTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer google_compute_router_peer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param interface: Name of the interface the BGP peer is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#interface GoogleComputeRouterPeer#interface}
        :param name: Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#name GoogleComputeRouterPeer#name}
        :param peer_asn: Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#peer_asn GoogleComputeRouterPeer#peer_asn}
        :param peer_ip_address: IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#peer_ip_address GoogleComputeRouterPeer#peer_ip_address}
        :param router: The name of the Cloud Router in which this BgpPeer will be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#router GoogleComputeRouterPeer#router}
        :param advertised_groups: User-specified list of prefix groups to advertise in custom mode, which can take one of the following options:. 'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. 'ALL_VPC_SUBNETS': Advertises the router's own VPC subnets. 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp" message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no custom groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_groups GoogleComputeRouterPeer#advertised_groups}
        :param advertised_ip_ranges: advertised_ip_ranges block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_ip_ranges GoogleComputeRouterPeer#advertised_ip_ranges}
        :param advertised_route_priority: The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the routes with the lowest priority value win. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_route_priority GoogleComputeRouterPeer#advertised_route_priority}
        :param advertise_mode: User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT', 'CUSTOM' Default value: "DEFAULT" Possible values: ["DEFAULT", "CUSTOM"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertise_mode GoogleComputeRouterPeer#advertise_mode}
        :param bfd: bfd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#bfd GoogleComputeRouterPeer#bfd}
        :param enable: The status of the BGP peer connection. If set to false, any active session with the peer is terminated and all associated routing information is removed. If set to true, the peer connection can be established with routing information. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#enable GoogleComputeRouterPeer#enable}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#id GoogleComputeRouterPeer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_address: IP address of the interface inside Google Cloud Platform. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#ip_address GoogleComputeRouterPeer#ip_address}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#project GoogleComputeRouterPeer#project}.
        :param region: Region where the router and BgpPeer reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#region GoogleComputeRouterPeer#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#timeouts GoogleComputeRouterPeer#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterPeer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeRouterPeerConfig(
            interface=interface,
            name=name,
            peer_asn=peer_asn,
            peer_ip_address=peer_ip_address,
            router=router,
            advertised_groups=advertised_groups,
            advertised_ip_ranges=advertised_ip_ranges,
            advertised_route_priority=advertised_route_priority,
            advertise_mode=advertise_mode,
            bfd=bfd,
            enable=enable,
            id=id,
            ip_address=ip_address,
            project=project,
            region=region,
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

    @jsii.member(jsii_name="putAdvertisedIpRanges")
    def put_advertised_ip_ranges(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeRouterPeerAdvertisedIpRanges", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterPeer.put_advertised_ip_ranges)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAdvertisedIpRanges", [value]))

    @jsii.member(jsii_name="putBfd")
    def put_bfd(
        self,
        *,
        session_initialization_mode: builtins.str,
        min_receive_interval: typing.Optional[jsii.Number] = None,
        min_transmit_interval: typing.Optional[jsii.Number] = None,
        multiplier: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param session_initialization_mode: The BFD session initialization mode for this BGP peer. If set to 'ACTIVE', the Cloud Router will initiate the BFD session for this BGP peer. If set to 'PASSIVE', the Cloud Router will wait for the peer router to initiate the BFD session for this BGP peer. If set to 'DISABLED', BFD is disabled for this BGP peer. Possible values: ["ACTIVE", "DISABLED", "PASSIVE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#session_initialization_mode GoogleComputeRouterPeer#session_initialization_mode}
        :param min_receive_interval: The minimum interval, in milliseconds, between BFD control packets received from the peer router. The actual value is negotiated between the two routers and is equal to the greater of this value and the transmit interval of the other router. If set, this value must be between 1000 and 30000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#min_receive_interval GoogleComputeRouterPeer#min_receive_interval}
        :param min_transmit_interval: The minimum interval, in milliseconds, between BFD control packets transmitted to the peer router. The actual value is negotiated between the two routers and is equal to the greater of this value and the corresponding receive interval of the other router. If set, this value must be between 1000 and 30000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#min_transmit_interval GoogleComputeRouterPeer#min_transmit_interval}
        :param multiplier: The number of consecutive BFD packets that must be missed before BFD declares that a peer is unavailable. If set, the value must be a value between 5 and 16. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#multiplier GoogleComputeRouterPeer#multiplier}
        '''
        value = GoogleComputeRouterPeerBfd(
            session_initialization_mode=session_initialization_mode,
            min_receive_interval=min_receive_interval,
            min_transmit_interval=min_transmit_interval,
            multiplier=multiplier,
        )

        return typing.cast(None, jsii.invoke(self, "putBfd", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#create GoogleComputeRouterPeer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#delete GoogleComputeRouterPeer#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#update GoogleComputeRouterPeer#update}.
        '''
        value = GoogleComputeRouterPeerTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdvertisedGroups")
    def reset_advertised_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvertisedGroups", []))

    @jsii.member(jsii_name="resetAdvertisedIpRanges")
    def reset_advertised_ip_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvertisedIpRanges", []))

    @jsii.member(jsii_name="resetAdvertisedRoutePriority")
    def reset_advertised_route_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvertisedRoutePriority", []))

    @jsii.member(jsii_name="resetAdvertiseMode")
    def reset_advertise_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdvertiseMode", []))

    @jsii.member(jsii_name="resetBfd")
    def reset_bfd(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBfd", []))

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

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
    @jsii.member(jsii_name="advertisedIpRanges")
    def advertised_ip_ranges(self) -> "GoogleComputeRouterPeerAdvertisedIpRangesList":
        return typing.cast("GoogleComputeRouterPeerAdvertisedIpRangesList", jsii.get(self, "advertisedIpRanges"))

    @builtins.property
    @jsii.member(jsii_name="bfd")
    def bfd(self) -> "GoogleComputeRouterPeerBfdOutputReference":
        return typing.cast("GoogleComputeRouterPeerBfdOutputReference", jsii.get(self, "bfd"))

    @builtins.property
    @jsii.member(jsii_name="managementType")
    def management_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managementType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeRouterPeerTimeoutsOutputReference":
        return typing.cast("GoogleComputeRouterPeerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="advertisedGroupsInput")
    def advertised_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "advertisedGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="advertisedIpRangesInput")
    def advertised_ip_ranges_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRouterPeerAdvertisedIpRanges"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeRouterPeerAdvertisedIpRanges"]]], jsii.get(self, "advertisedIpRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="advertisedRoutePriorityInput")
    def advertised_route_priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "advertisedRoutePriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="advertiseModeInput")
    def advertise_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "advertiseModeInput"))

    @builtins.property
    @jsii.member(jsii_name="bfdInput")
    def bfd_input(self) -> typing.Optional["GoogleComputeRouterPeerBfd"]:
        return typing.cast(typing.Optional["GoogleComputeRouterPeerBfd"], jsii.get(self, "bfdInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interfaceInput")
    def interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="peerAsnInput")
    def peer_asn_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "peerAsnInput"))

    @builtins.property
    @jsii.member(jsii_name="peerIpAddressInput")
    def peer_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerIpAddressInput"))

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
    ) -> typing.Optional[typing.Union["GoogleComputeRouterPeerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeRouterPeerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="advertisedGroups")
    def advertised_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "advertisedGroups"))

    @advertised_groups.setter
    def advertised_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "advertised_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advertisedGroups", value)

    @builtins.property
    @jsii.member(jsii_name="advertisedRoutePriority")
    def advertised_route_priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "advertisedRoutePriority"))

    @advertised_route_priority.setter
    def advertised_route_priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "advertised_route_priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advertisedRoutePriority", value)

    @builtins.property
    @jsii.member(jsii_name="advertiseMode")
    def advertise_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "advertiseMode"))

    @advertise_mode.setter
    def advertise_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "advertise_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "advertiseMode", value)

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="interface")
    def interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interface"))

    @interface.setter
    def interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interface", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="peerAsn")
    def peer_asn(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "peerAsn"))

    @peer_asn.setter
    def peer_asn(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "peer_asn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerAsn", value)

    @builtins.property
    @jsii.member(jsii_name="peerIpAddress")
    def peer_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "peerIpAddress"))

    @peer_ip_address.setter
    def peer_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "peer_ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="router")
    def router(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "router"))

    @router.setter
    def router(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeer, "router").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "router", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerAdvertisedIpRanges",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "description": "description"},
)
class GoogleComputeRouterPeerAdvertisedIpRanges:
    def __init__(
        self,
        *,
        range: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param range: The IP range to advertise. The value must be a CIDR-formatted string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#range GoogleComputeRouterPeer#range}
        :param description: User-specified description for the IP range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#description GoogleComputeRouterPeer#description}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerAdvertisedIpRanges.__init__)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "range": range,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def range(self) -> builtins.str:
        '''The IP range to advertise. The value must be a CIDR-formatted string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#range GoogleComputeRouterPeer#range}
        '''
        result = self._values.get("range")
        assert result is not None, "Required property 'range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''User-specified description for the IP range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#description GoogleComputeRouterPeer#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouterPeerAdvertisedIpRanges(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRouterPeerAdvertisedIpRangesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerAdvertisedIpRangesList",
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
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerAdvertisedIpRangesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeRouterPeerAdvertisedIpRangesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerAdvertisedIpRangesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeRouterPeerAdvertisedIpRangesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerAdvertisedIpRangesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerAdvertisedIpRangesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerAdvertisedIpRangesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRouterPeerAdvertisedIpRanges]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRouterPeerAdvertisedIpRanges]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRouterPeerAdvertisedIpRanges]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerAdvertisedIpRangesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeRouterPeerAdvertisedIpRangesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerAdvertisedIpRangesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerAdvertisedIpRangesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerAdvertisedIpRangesOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "range"))

    @range.setter
    def range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerAdvertisedIpRangesOutputReference, "range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "range", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRouterPeerAdvertisedIpRanges, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRouterPeerAdvertisedIpRanges, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRouterPeerAdvertisedIpRanges, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerAdvertisedIpRangesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerBfd",
    jsii_struct_bases=[],
    name_mapping={
        "session_initialization_mode": "sessionInitializationMode",
        "min_receive_interval": "minReceiveInterval",
        "min_transmit_interval": "minTransmitInterval",
        "multiplier": "multiplier",
    },
)
class GoogleComputeRouterPeerBfd:
    def __init__(
        self,
        *,
        session_initialization_mode: builtins.str,
        min_receive_interval: typing.Optional[jsii.Number] = None,
        min_transmit_interval: typing.Optional[jsii.Number] = None,
        multiplier: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param session_initialization_mode: The BFD session initialization mode for this BGP peer. If set to 'ACTIVE', the Cloud Router will initiate the BFD session for this BGP peer. If set to 'PASSIVE', the Cloud Router will wait for the peer router to initiate the BFD session for this BGP peer. If set to 'DISABLED', BFD is disabled for this BGP peer. Possible values: ["ACTIVE", "DISABLED", "PASSIVE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#session_initialization_mode GoogleComputeRouterPeer#session_initialization_mode}
        :param min_receive_interval: The minimum interval, in milliseconds, between BFD control packets received from the peer router. The actual value is negotiated between the two routers and is equal to the greater of this value and the transmit interval of the other router. If set, this value must be between 1000 and 30000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#min_receive_interval GoogleComputeRouterPeer#min_receive_interval}
        :param min_transmit_interval: The minimum interval, in milliseconds, between BFD control packets transmitted to the peer router. The actual value is negotiated between the two routers and is equal to the greater of this value and the corresponding receive interval of the other router. If set, this value must be between 1000 and 30000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#min_transmit_interval GoogleComputeRouterPeer#min_transmit_interval}
        :param multiplier: The number of consecutive BFD packets that must be missed before BFD declares that a peer is unavailable. If set, the value must be a value between 5 and 16. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#multiplier GoogleComputeRouterPeer#multiplier}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerBfd.__init__)
            check_type(argname="argument session_initialization_mode", value=session_initialization_mode, expected_type=type_hints["session_initialization_mode"])
            check_type(argname="argument min_receive_interval", value=min_receive_interval, expected_type=type_hints["min_receive_interval"])
            check_type(argname="argument min_transmit_interval", value=min_transmit_interval, expected_type=type_hints["min_transmit_interval"])
            check_type(argname="argument multiplier", value=multiplier, expected_type=type_hints["multiplier"])
        self._values: typing.Dict[str, typing.Any] = {
            "session_initialization_mode": session_initialization_mode,
        }
        if min_receive_interval is not None:
            self._values["min_receive_interval"] = min_receive_interval
        if min_transmit_interval is not None:
            self._values["min_transmit_interval"] = min_transmit_interval
        if multiplier is not None:
            self._values["multiplier"] = multiplier

    @builtins.property
    def session_initialization_mode(self) -> builtins.str:
        '''The BFD session initialization mode for this BGP peer.

        If set to 'ACTIVE', the Cloud Router will initiate the BFD session
        for this BGP peer. If set to 'PASSIVE', the Cloud Router will wait
        for the peer router to initiate the BFD session for this BGP peer.
        If set to 'DISABLED', BFD is disabled for this BGP peer. Possible values: ["ACTIVE", "DISABLED", "PASSIVE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#session_initialization_mode GoogleComputeRouterPeer#session_initialization_mode}
        '''
        result = self._values.get("session_initialization_mode")
        assert result is not None, "Required property 'session_initialization_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def min_receive_interval(self) -> typing.Optional[jsii.Number]:
        '''The minimum interval, in milliseconds, between BFD control packets received from the peer router.

        The actual value is negotiated
        between the two routers and is equal to the greater of this value
        and the transmit interval of the other router. If set, this value
        must be between 1000 and 30000.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#min_receive_interval GoogleComputeRouterPeer#min_receive_interval}
        '''
        result = self._values.get("min_receive_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_transmit_interval(self) -> typing.Optional[jsii.Number]:
        '''The minimum interval, in milliseconds, between BFD control packets transmitted to the peer router.

        The actual value is negotiated
        between the two routers and is equal to the greater of this value
        and the corresponding receive interval of the other router. If set,
        this value must be between 1000 and 30000.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#min_transmit_interval GoogleComputeRouterPeer#min_transmit_interval}
        '''
        result = self._values.get("min_transmit_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def multiplier(self) -> typing.Optional[jsii.Number]:
        '''The number of consecutive BFD packets that must be missed before BFD declares that a peer is unavailable.

        If set, the value must
        be a value between 5 and 16.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#multiplier GoogleComputeRouterPeer#multiplier}
        '''
        result = self._values.get("multiplier")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouterPeerBfd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRouterPeerBfdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerBfdOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerBfdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMinReceiveInterval")
    def reset_min_receive_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinReceiveInterval", []))

    @jsii.member(jsii_name="resetMinTransmitInterval")
    def reset_min_transmit_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinTransmitInterval", []))

    @jsii.member(jsii_name="resetMultiplier")
    def reset_multiplier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultiplier", []))

    @builtins.property
    @jsii.member(jsii_name="minReceiveIntervalInput")
    def min_receive_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minReceiveIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="minTransmitIntervalInput")
    def min_transmit_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minTransmitIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="multiplierInput")
    def multiplier_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "multiplierInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionInitializationModeInput")
    def session_initialization_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionInitializationModeInput"))

    @builtins.property
    @jsii.member(jsii_name="minReceiveInterval")
    def min_receive_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minReceiveInterval"))

    @min_receive_interval.setter
    def min_receive_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerBfdOutputReference, "min_receive_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minReceiveInterval", value)

    @builtins.property
    @jsii.member(jsii_name="minTransmitInterval")
    def min_transmit_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minTransmitInterval"))

    @min_transmit_interval.setter
    def min_transmit_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerBfdOutputReference, "min_transmit_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minTransmitInterval", value)

    @builtins.property
    @jsii.member(jsii_name="multiplier")
    def multiplier(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "multiplier"))

    @multiplier.setter
    def multiplier(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerBfdOutputReference, "multiplier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiplier", value)

    @builtins.property
    @jsii.member(jsii_name="sessionInitializationMode")
    def session_initialization_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sessionInitializationMode"))

    @session_initialization_mode.setter
    def session_initialization_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerBfdOutputReference, "session_initialization_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionInitializationMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeRouterPeerBfd]:
        return typing.cast(typing.Optional[GoogleComputeRouterPeerBfd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeRouterPeerBfd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerBfdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "interface": "interface",
        "name": "name",
        "peer_asn": "peerAsn",
        "peer_ip_address": "peerIpAddress",
        "router": "router",
        "advertised_groups": "advertisedGroups",
        "advertised_ip_ranges": "advertisedIpRanges",
        "advertised_route_priority": "advertisedRoutePriority",
        "advertise_mode": "advertiseMode",
        "bfd": "bfd",
        "enable": "enable",
        "id": "id",
        "ip_address": "ipAddress",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
    },
)
class GoogleComputeRouterPeerConfig(cdktf.TerraformMetaArguments):
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
        interface: builtins.str,
        name: builtins.str,
        peer_asn: jsii.Number,
        peer_ip_address: builtins.str,
        router: builtins.str,
        advertised_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        advertised_ip_ranges: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeRouterPeerAdvertisedIpRanges, typing.Dict[str, typing.Any]]]]] = None,
        advertised_route_priority: typing.Optional[jsii.Number] = None,
        advertise_mode: typing.Optional[builtins.str] = None,
        bfd: typing.Optional[typing.Union[GoogleComputeRouterPeerBfd, typing.Dict[str, typing.Any]]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip_address: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeRouterPeerTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param interface: Name of the interface the BGP peer is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#interface GoogleComputeRouterPeer#interface}
        :param name: Name of this BGP peer. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#name GoogleComputeRouterPeer#name}
        :param peer_asn: Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#peer_asn GoogleComputeRouterPeer#peer_asn}
        :param peer_ip_address: IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#peer_ip_address GoogleComputeRouterPeer#peer_ip_address}
        :param router: The name of the Cloud Router in which this BgpPeer will be configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#router GoogleComputeRouterPeer#router}
        :param advertised_groups: User-specified list of prefix groups to advertise in custom mode, which can take one of the following options:. 'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets. 'ALL_VPC_SUBNETS': Advertises the router's own VPC subnets. 'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network. Note that this field can only be populated if advertiseMode is 'CUSTOM' and overrides the list defined for the router (in the "bgp" message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no custom groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_groups GoogleComputeRouterPeer#advertised_groups}
        :param advertised_ip_ranges: advertised_ip_ranges block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_ip_ranges GoogleComputeRouterPeer#advertised_ip_ranges}
        :param advertised_route_priority: The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the routes with the lowest priority value win. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_route_priority GoogleComputeRouterPeer#advertised_route_priority}
        :param advertise_mode: User-specified flag to indicate which mode to use for advertisement. Valid values of this enum field are: 'DEFAULT', 'CUSTOM' Default value: "DEFAULT" Possible values: ["DEFAULT", "CUSTOM"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertise_mode GoogleComputeRouterPeer#advertise_mode}
        :param bfd: bfd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#bfd GoogleComputeRouterPeer#bfd}
        :param enable: The status of the BGP peer connection. If set to false, any active session with the peer is terminated and all associated routing information is removed. If set to true, the peer connection can be established with routing information. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#enable GoogleComputeRouterPeer#enable}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#id GoogleComputeRouterPeer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_address: IP address of the interface inside Google Cloud Platform. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#ip_address GoogleComputeRouterPeer#ip_address}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#project GoogleComputeRouterPeer#project}.
        :param region: Region where the router and BgpPeer reside. If it is not provided, the provider region is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#region GoogleComputeRouterPeer#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#timeouts GoogleComputeRouterPeer#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(bfd, dict):
            bfd = GoogleComputeRouterPeerBfd(**bfd)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeRouterPeerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument peer_asn", value=peer_asn, expected_type=type_hints["peer_asn"])
            check_type(argname="argument peer_ip_address", value=peer_ip_address, expected_type=type_hints["peer_ip_address"])
            check_type(argname="argument router", value=router, expected_type=type_hints["router"])
            check_type(argname="argument advertised_groups", value=advertised_groups, expected_type=type_hints["advertised_groups"])
            check_type(argname="argument advertised_ip_ranges", value=advertised_ip_ranges, expected_type=type_hints["advertised_ip_ranges"])
            check_type(argname="argument advertised_route_priority", value=advertised_route_priority, expected_type=type_hints["advertised_route_priority"])
            check_type(argname="argument advertise_mode", value=advertise_mode, expected_type=type_hints["advertise_mode"])
            check_type(argname="argument bfd", value=bfd, expected_type=type_hints["bfd"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "interface": interface,
            "name": name,
            "peer_asn": peer_asn,
            "peer_ip_address": peer_ip_address,
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
        if advertised_groups is not None:
            self._values["advertised_groups"] = advertised_groups
        if advertised_ip_ranges is not None:
            self._values["advertised_ip_ranges"] = advertised_ip_ranges
        if advertised_route_priority is not None:
            self._values["advertised_route_priority"] = advertised_route_priority
        if advertise_mode is not None:
            self._values["advertise_mode"] = advertise_mode
        if bfd is not None:
            self._values["bfd"] = bfd
        if enable is not None:
            self._values["enable"] = enable
        if id is not None:
            self._values["id"] = id
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
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
    def interface(self) -> builtins.str:
        '''Name of the interface the BGP peer is associated with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#interface GoogleComputeRouterPeer#interface}
        '''
        result = self._values.get("interface")
        assert result is not None, "Required property 'interface' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of this BGP peer.

        The name must be 1-63 characters long,
        and comply with RFC1035. Specifically, the name must be 1-63 characters
        long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which
        means the first character must be a lowercase letter, and all
        following characters must be a dash, lowercase letter, or digit,
        except the last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#name GoogleComputeRouterPeer#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peer_asn(self) -> jsii.Number:
        '''Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#peer_asn GoogleComputeRouterPeer#peer_asn}
        '''
        result = self._values.get("peer_asn")
        assert result is not None, "Required property 'peer_asn' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def peer_ip_address(self) -> builtins.str:
        '''IP address of the BGP interface outside Google Cloud Platform. Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#peer_ip_address GoogleComputeRouterPeer#peer_ip_address}
        '''
        result = self._values.get("peer_ip_address")
        assert result is not None, "Required property 'peer_ip_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def router(self) -> builtins.str:
        '''The name of the Cloud Router in which this BgpPeer will be configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#router GoogleComputeRouterPeer#router}
        '''
        result = self._values.get("router")
        assert result is not None, "Required property 'router' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def advertised_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''User-specified list of prefix groups to advertise in custom mode, which can take one of the following options:.

        'ALL_SUBNETS': Advertises all available subnets, including peer VPC subnets.
        'ALL_VPC_SUBNETS': Advertises the router's own VPC subnets.
        'ALL_PEER_VPC_SUBNETS': Advertises peer subnets of the router's VPC network.

        Note that this field can only be populated if advertiseMode is 'CUSTOM'
        and overrides the list defined for the router (in the "bgp" message).
        These groups are advertised in addition to any specified prefixes.
        Leave this field blank to advertise no custom groups.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_groups GoogleComputeRouterPeer#advertised_groups}
        '''
        result = self._values.get("advertised_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def advertised_ip_ranges(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRouterPeerAdvertisedIpRanges]]]:
        '''advertised_ip_ranges block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_ip_ranges GoogleComputeRouterPeer#advertised_ip_ranges}
        '''
        result = self._values.get("advertised_ip_ranges")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeRouterPeerAdvertisedIpRanges]]], result)

    @builtins.property
    def advertised_route_priority(self) -> typing.Optional[jsii.Number]:
        '''The priority of routes advertised to this BGP peer.

        Where there is more than one matching route of maximum
        length, the routes with the lowest priority value win.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertised_route_priority GoogleComputeRouterPeer#advertised_route_priority}
        '''
        result = self._values.get("advertised_route_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def advertise_mode(self) -> typing.Optional[builtins.str]:
        '''User-specified flag to indicate which mode to use for advertisement.

        Valid values of this enum field are: 'DEFAULT', 'CUSTOM' Default value: "DEFAULT" Possible values: ["DEFAULT", "CUSTOM"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#advertise_mode GoogleComputeRouterPeer#advertise_mode}
        '''
        result = self._values.get("advertise_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bfd(self) -> typing.Optional[GoogleComputeRouterPeerBfd]:
        '''bfd block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#bfd GoogleComputeRouterPeer#bfd}
        '''
        result = self._values.get("bfd")
        return typing.cast(typing.Optional[GoogleComputeRouterPeerBfd], result)

    @builtins.property
    def enable(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The status of the BGP peer connection.

        If set to false, any active session
        with the peer is terminated and all associated routing information is removed.
        If set to true, the peer connection can be established with routing information.
        The default is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#enable GoogleComputeRouterPeer#enable}
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#id GoogleComputeRouterPeer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''IP address of the interface inside Google Cloud Platform. Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#ip_address GoogleComputeRouterPeer#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#project GoogleComputeRouterPeer#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the router and BgpPeer reside. If it is not provided, the provider region is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#region GoogleComputeRouterPeer#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeRouterPeerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#timeouts GoogleComputeRouterPeer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeRouterPeerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouterPeerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeRouterPeerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#create GoogleComputeRouterPeer#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#delete GoogleComputeRouterPeer#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#update GoogleComputeRouterPeer#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#create GoogleComputeRouterPeer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#delete GoogleComputeRouterPeer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_router_peer#update GoogleComputeRouterPeer#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeRouterPeerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeRouterPeerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeRouterPeer.GoogleComputeRouterPeerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeRouterPeerTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeRouterPeerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeRouterPeerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeRouterPeerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeRouterPeerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeRouterPeer",
    "GoogleComputeRouterPeerAdvertisedIpRanges",
    "GoogleComputeRouterPeerAdvertisedIpRangesList",
    "GoogleComputeRouterPeerAdvertisedIpRangesOutputReference",
    "GoogleComputeRouterPeerBfd",
    "GoogleComputeRouterPeerBfdOutputReference",
    "GoogleComputeRouterPeerConfig",
    "GoogleComputeRouterPeerTimeouts",
    "GoogleComputeRouterPeerTimeoutsOutputReference",
]

publication.publish()
