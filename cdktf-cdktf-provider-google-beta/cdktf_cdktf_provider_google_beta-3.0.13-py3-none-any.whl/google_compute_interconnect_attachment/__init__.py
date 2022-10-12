'''
# `google_compute_interconnect_attachment`

Refer to the Terraform Registory for docs: [`google_compute_interconnect_attachment`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment).
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


class GoogleComputeInterconnectAttachment(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInterconnectAttachment.GoogleComputeInterconnectAttachment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment google_compute_interconnect_attachment}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        router: builtins.str,
        admin_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bandwidth: typing.Optional[builtins.str] = None,
        candidate_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        edge_availability_domain: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        interconnect: typing.Optional[builtins.str] = None,
        ipsec_internal_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        mtu: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeInterconnectAttachmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        vlan_tag8021_q: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment google_compute_interconnect_attachment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#name GoogleComputeInterconnectAttachment#name}
        :param router: URL of the cloud router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#router GoogleComputeInterconnectAttachment#router}
        :param admin_enabled: Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect attachment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#admin_enabled GoogleComputeInterconnectAttachment#admin_enabled}
        :param bandwidth: Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G Possible values: ["BPS_50M", "BPS_100M", "BPS_200M", "BPS_300M", "BPS_400M", "BPS_500M", "BPS_1G", "BPS_2G", "BPS_5G", "BPS_10G", "BPS_20G", "BPS_50G"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#bandwidth GoogleComputeInterconnectAttachment#bandwidth}
        :param candidate_subnets: Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will randomly select an unused /29 from all of link-local space. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#candidate_subnets GoogleComputeInterconnectAttachment#candidate_subnets}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#description GoogleComputeInterconnectAttachment#description}
        :param edge_availability_domain: Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved reliability, customers should configure a pair of attachments with one per availability domain. The selected availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#edge_availability_domain GoogleComputeInterconnectAttachment#edge_availability_domain}
        :param encryption: Indicates the user-supplied encryption option of this interconnect attachment:. NONE is the default value, which means that the attachment carries unencrypted traffic. VMs can send traffic to, or receive traffic from, this type of attachment. IPSEC indicates that the attachment carries only traffic encrypted by an IPsec device such as an HA VPN gateway. VMs cannot directly send traffic to, or receive traffic from, such an attachment. To use IPsec-encrypted Cloud Interconnect create the attachment using this option. Not currently available publicly. Default value: "NONE" Possible values: ["NONE", "IPSEC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#encryption GoogleComputeInterconnectAttachment#encryption}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#id GoogleComputeInterconnectAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interconnect: URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is DEDICATED, must not be set if type is PARTNER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#interconnect GoogleComputeInterconnectAttachment#interconnect}
        :param ipsec_internal_addresses: URL of addresses that have been reserved for the interconnect attachment, Used only for interconnect attachment that has the encryption option as IPSEC. The addresses must be RFC 1918 IP address ranges. When creating HA VPN gateway over the interconnect attachment, if the attachment is configured to use an RFC 1918 IP address, then the VPN gateway's IP address will be allocated from the IP address range specified here. For example, if the HA VPN gateway's interface 0 is paired to this interconnect attachment, then an RFC 1918 IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this interconnect attachment. If this field is not specified for interconnect attachment that has encryption option as IPSEC, later on when creating HA VPN gateway on this interconnect attachment, the HA VPN gateway's IP address will be allocated from regional external IP address pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#ipsec_internal_addresses GoogleComputeInterconnectAttachment#ipsec_internal_addresses}
        :param mtu: Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment. Currently, only 1440 and 1500 are allowed. If not specified, the value will default to 1440. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#mtu GoogleComputeInterconnectAttachment#mtu}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#project GoogleComputeInterconnectAttachment#project}.
        :param region: Region where the regional interconnect attachment resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#region GoogleComputeInterconnectAttachment#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#timeouts GoogleComputeInterconnectAttachment#timeouts}
        :param type: The type of InterconnectAttachment you wish to create. Defaults to DEDICATED. Possible values: ["DEDICATED", "PARTNER", "PARTNER_PROVIDER"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#type GoogleComputeInterconnectAttachment#type}
        :param vlan_tag8021_q: The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed upstream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#vlan_tag8021q GoogleComputeInterconnectAttachment#vlan_tag8021q}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInterconnectAttachment.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeInterconnectAttachmentConfig(
            name=name,
            router=router,
            admin_enabled=admin_enabled,
            bandwidth=bandwidth,
            candidate_subnets=candidate_subnets,
            description=description,
            edge_availability_domain=edge_availability_domain,
            encryption=encryption,
            id=id,
            interconnect=interconnect,
            ipsec_internal_addresses=ipsec_internal_addresses,
            mtu=mtu,
            project=project,
            region=region,
            timeouts=timeouts,
            type=type,
            vlan_tag8021_q=vlan_tag8021_q,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#create GoogleComputeInterconnectAttachment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#delete GoogleComputeInterconnectAttachment#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#update GoogleComputeInterconnectAttachment#update}.
        '''
        value = GoogleComputeInterconnectAttachmentTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdminEnabled")
    def reset_admin_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminEnabled", []))

    @jsii.member(jsii_name="resetBandwidth")
    def reset_bandwidth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBandwidth", []))

    @jsii.member(jsii_name="resetCandidateSubnets")
    def reset_candidate_subnets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCandidateSubnets", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEdgeAvailabilityDomain")
    def reset_edge_availability_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEdgeAvailabilityDomain", []))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInterconnect")
    def reset_interconnect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterconnect", []))

    @jsii.member(jsii_name="resetIpsecInternalAddresses")
    def reset_ipsec_internal_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpsecInternalAddresses", []))

    @jsii.member(jsii_name="resetMtu")
    def reset_mtu(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMtu", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetVlanTag8021Q")
    def reset_vlan_tag8021_q(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVlanTag8021Q", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cloudRouterIpAddress")
    def cloud_router_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudRouterIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="customerRouterIpAddress")
    def customer_router_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerRouterIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="googleReferenceId")
    def google_reference_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleReferenceId"))

    @builtins.property
    @jsii.member(jsii_name="pairingKey")
    def pairing_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pairingKey"))

    @builtins.property
    @jsii.member(jsii_name="partnerAsn")
    def partner_asn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "partnerAsn"))

    @builtins.property
    @jsii.member(jsii_name="privateInterconnectInfo")
    def private_interconnect_info(
        self,
    ) -> "GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList":
        return typing.cast("GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList", jsii.get(self, "privateInterconnectInfo"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeInterconnectAttachmentTimeoutsOutputReference":
        return typing.cast("GoogleComputeInterconnectAttachmentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="adminEnabledInput")
    def admin_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "adminEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="bandwidthInput")
    def bandwidth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bandwidthInput"))

    @builtins.property
    @jsii.member(jsii_name="candidateSubnetsInput")
    def candidate_subnets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "candidateSubnetsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="edgeAvailabilityDomainInput")
    def edge_availability_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "edgeAvailabilityDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interconnectInput")
    def interconnect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interconnectInput"))

    @builtins.property
    @jsii.member(jsii_name="ipsecInternalAddressesInput")
    def ipsec_internal_addresses_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipsecInternalAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="mtuInput")
    def mtu_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mtuInput"))

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
    ) -> typing.Optional[typing.Union["GoogleComputeInterconnectAttachmentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeInterconnectAttachmentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vlanTag8021QInput")
    def vlan_tag8021_q_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "vlanTag8021QInput"))

    @builtins.property
    @jsii.member(jsii_name="adminEnabled")
    def admin_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "adminEnabled"))

    @admin_enabled.setter
    def admin_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "admin_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="bandwidth")
    def bandwidth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bandwidth"))

    @bandwidth.setter
    def bandwidth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "bandwidth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="candidateSubnets")
    def candidate_subnets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "candidateSubnets"))

    @candidate_subnets.setter
    def candidate_subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "candidate_subnets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "candidateSubnets", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="edgeAvailabilityDomain")
    def edge_availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "edgeAvailabilityDomain"))

    @edge_availability_domain.setter
    def edge_availability_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "edge_availability_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeAvailabilityDomain", value)

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "encryption").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="interconnect")
    def interconnect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interconnect"))

    @interconnect.setter
    def interconnect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "interconnect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interconnect", value)

    @builtins.property
    @jsii.member(jsii_name="ipsecInternalAddresses")
    def ipsec_internal_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipsecInternalAddresses"))

    @ipsec_internal_addresses.setter
    def ipsec_internal_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "ipsec_internal_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipsecInternalAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="mtu")
    def mtu(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mtu"))

    @mtu.setter
    def mtu(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "mtu").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mtu", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="router")
    def router(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "router"))

    @router.setter
    def router(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "router").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "router", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="vlanTag8021Q")
    def vlan_tag8021_q(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "vlanTag8021Q"))

    @vlan_tag8021_q.setter
    def vlan_tag8021_q(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachment, "vlan_tag8021_q").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlanTag8021Q", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInterconnectAttachment.GoogleComputeInterconnectAttachmentConfig",
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
        "admin_enabled": "adminEnabled",
        "bandwidth": "bandwidth",
        "candidate_subnets": "candidateSubnets",
        "description": "description",
        "edge_availability_domain": "edgeAvailabilityDomain",
        "encryption": "encryption",
        "id": "id",
        "interconnect": "interconnect",
        "ipsec_internal_addresses": "ipsecInternalAddresses",
        "mtu": "mtu",
        "project": "project",
        "region": "region",
        "timeouts": "timeouts",
        "type": "type",
        "vlan_tag8021_q": "vlanTag8021Q",
    },
)
class GoogleComputeInterconnectAttachmentConfig(cdktf.TerraformMetaArguments):
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
        admin_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        bandwidth: typing.Optional[builtins.str] = None,
        candidate_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        edge_availability_domain: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        interconnect: typing.Optional[builtins.str] = None,
        ipsec_internal_addresses: typing.Optional[typing.Sequence[builtins.str]] = None,
        mtu: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeInterconnectAttachmentTimeouts", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        vlan_tag8021_q: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#name GoogleComputeInterconnectAttachment#name}
        :param router: URL of the cloud router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#router GoogleComputeInterconnectAttachment#router}
        :param admin_enabled: Whether the VLAN attachment is enabled or disabled. When using PARTNER type this will Pre-Activate the interconnect attachment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#admin_enabled GoogleComputeInterconnectAttachment#admin_enabled}
        :param bandwidth: Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, Defaults to BPS_10G Possible values: ["BPS_50M", "BPS_100M", "BPS_200M", "BPS_300M", "BPS_400M", "BPS_500M", "BPS_1G", "BPS_2G", "BPS_5G", "BPS_10G", "BPS_20G", "BPS_50G"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#bandwidth GoogleComputeInterconnectAttachment#bandwidth}
        :param candidate_subnets: Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will randomly select an unused /29 from all of link-local space. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#candidate_subnets GoogleComputeInterconnectAttachment#candidate_subnets}
        :param description: An optional description of this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#description GoogleComputeInterconnectAttachment#description}
        :param edge_availability_domain: Desired availability domain for the attachment. Only available for type PARTNER, at creation time. For improved reliability, customers should configure a pair of attachments with one per availability domain. The selected availability domain will be provided to the Partner via the pairing key so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#edge_availability_domain GoogleComputeInterconnectAttachment#edge_availability_domain}
        :param encryption: Indicates the user-supplied encryption option of this interconnect attachment:. NONE is the default value, which means that the attachment carries unencrypted traffic. VMs can send traffic to, or receive traffic from, this type of attachment. IPSEC indicates that the attachment carries only traffic encrypted by an IPsec device such as an HA VPN gateway. VMs cannot directly send traffic to, or receive traffic from, such an attachment. To use IPsec-encrypted Cloud Interconnect create the attachment using this option. Not currently available publicly. Default value: "NONE" Possible values: ["NONE", "IPSEC"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#encryption GoogleComputeInterconnectAttachment#encryption}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#id GoogleComputeInterconnectAttachment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interconnect: URL of the underlying Interconnect object that this attachment's traffic will traverse through. Required if type is DEDICATED, must not be set if type is PARTNER. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#interconnect GoogleComputeInterconnectAttachment#interconnect}
        :param ipsec_internal_addresses: URL of addresses that have been reserved for the interconnect attachment, Used only for interconnect attachment that has the encryption option as IPSEC. The addresses must be RFC 1918 IP address ranges. When creating HA VPN gateway over the interconnect attachment, if the attachment is configured to use an RFC 1918 IP address, then the VPN gateway's IP address will be allocated from the IP address range specified here. For example, if the HA VPN gateway's interface 0 is paired to this interconnect attachment, then an RFC 1918 IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this interconnect attachment. If this field is not specified for interconnect attachment that has encryption option as IPSEC, later on when creating HA VPN gateway on this interconnect attachment, the HA VPN gateway's IP address will be allocated from regional external IP address pool. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#ipsec_internal_addresses GoogleComputeInterconnectAttachment#ipsec_internal_addresses}
        :param mtu: Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment. Currently, only 1440 and 1500 are allowed. If not specified, the value will default to 1440. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#mtu GoogleComputeInterconnectAttachment#mtu}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#project GoogleComputeInterconnectAttachment#project}.
        :param region: Region where the regional interconnect attachment resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#region GoogleComputeInterconnectAttachment#region}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#timeouts GoogleComputeInterconnectAttachment#timeouts}
        :param type: The type of InterconnectAttachment you wish to create. Defaults to DEDICATED. Possible values: ["DEDICATED", "PARTNER", "PARTNER_PROVIDER"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#type GoogleComputeInterconnectAttachment#type}
        :param vlan_tag8021_q: The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed upstream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#vlan_tag8021q GoogleComputeInterconnectAttachment#vlan_tag8021q}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeInterconnectAttachmentTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInterconnectAttachmentConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument router", value=router, expected_type=type_hints["router"])
            check_type(argname="argument admin_enabled", value=admin_enabled, expected_type=type_hints["admin_enabled"])
            check_type(argname="argument bandwidth", value=bandwidth, expected_type=type_hints["bandwidth"])
            check_type(argname="argument candidate_subnets", value=candidate_subnets, expected_type=type_hints["candidate_subnets"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument edge_availability_domain", value=edge_availability_domain, expected_type=type_hints["edge_availability_domain"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument interconnect", value=interconnect, expected_type=type_hints["interconnect"])
            check_type(argname="argument ipsec_internal_addresses", value=ipsec_internal_addresses, expected_type=type_hints["ipsec_internal_addresses"])
            check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument vlan_tag8021_q", value=vlan_tag8021_q, expected_type=type_hints["vlan_tag8021_q"])
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
        if admin_enabled is not None:
            self._values["admin_enabled"] = admin_enabled
        if bandwidth is not None:
            self._values["bandwidth"] = bandwidth
        if candidate_subnets is not None:
            self._values["candidate_subnets"] = candidate_subnets
        if description is not None:
            self._values["description"] = description
        if edge_availability_domain is not None:
            self._values["edge_availability_domain"] = edge_availability_domain
        if encryption is not None:
            self._values["encryption"] = encryption
        if id is not None:
            self._values["id"] = id
        if interconnect is not None:
            self._values["interconnect"] = interconnect
        if ipsec_internal_addresses is not None:
            self._values["ipsec_internal_addresses"] = ipsec_internal_addresses
        if mtu is not None:
            self._values["mtu"] = mtu
        if project is not None:
            self._values["project"] = project
        if region is not None:
            self._values["region"] = region
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if type is not None:
            self._values["type"] = type
        if vlan_tag8021_q is not None:
            self._values["vlan_tag8021_q"] = vlan_tag8021_q

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
        '''Name of the resource.

        Provided by the client when the resource is created. The
        name must be 1-63 characters long, and comply with RFC1035. Specifically, the
        name must be 1-63 characters long and match the regular expression
        '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a
        lowercase letter, and all following characters must be a dash, lowercase
        letter, or digit, except the last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#name GoogleComputeInterconnectAttachment#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def router(self) -> builtins.str:
        '''URL of the cloud router to be used for dynamic routing.

        This router must be in
        the same region as this InterconnectAttachment. The InterconnectAttachment will
        automatically connect the Interconnect to the network & region within which the
        Cloud Router is configured.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#router GoogleComputeInterconnectAttachment#router}
        '''
        result = self._values.get("router")
        assert result is not None, "Required property 'router' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the VLAN attachment is enabled or disabled.  When using PARTNER type this will Pre-Activate the interconnect attachment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#admin_enabled GoogleComputeInterconnectAttachment#admin_enabled}
        '''
        result = self._values.get("admin_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def bandwidth(self) -> typing.Optional[builtins.str]:
        '''Provisioned bandwidth capacity for the interconnect attachment.

        For attachments of type DEDICATED, the user can set the bandwidth.
        For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth.
        Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED,
        Defaults to BPS_10G Possible values: ["BPS_50M", "BPS_100M", "BPS_200M", "BPS_300M", "BPS_400M", "BPS_500M", "BPS_1G", "BPS_2G", "BPS_5G", "BPS_10G", "BPS_20G", "BPS_50G"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#bandwidth GoogleComputeInterconnectAttachment#bandwidth}
        '''
        result = self._values.get("bandwidth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def candidate_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment.

        All prefixes must be within link-local address space (169.254.0.0/16)
        and must be /29 or shorter (/28, /27, etc). Google will attempt to select
        an unused /29 from the supplied candidate prefix(es). The request will
        fail if all possible /29s are in use on Google's edge. If not supplied,
        Google will randomly select an unused /29 from all of link-local space.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#candidate_subnets GoogleComputeInterconnectAttachment#candidate_subnets}
        '''
        result = self._values.get("candidate_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#description GoogleComputeInterconnectAttachment#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def edge_availability_domain(self) -> typing.Optional[builtins.str]:
        '''Desired availability domain for the attachment.

        Only available for type
        PARTNER, at creation time. For improved reliability, customers should
        configure a pair of attachments with one per availability domain. The
        selected availability domain will be provided to the Partner via the
        pairing key so that the provisioned circuit will lie in the specified
        domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#edge_availability_domain GoogleComputeInterconnectAttachment#edge_availability_domain}
        '''
        result = self._values.get("edge_availability_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(self) -> typing.Optional[builtins.str]:
        '''Indicates the user-supplied encryption option of this interconnect attachment:.

        NONE is the default value, which means that the attachment carries
        unencrypted traffic. VMs can send traffic to, or receive traffic
        from, this type of attachment.

        IPSEC indicates that the attachment carries only traffic encrypted by
        an IPsec device such as an HA VPN gateway. VMs cannot directly send
        traffic to, or receive traffic from, such an attachment. To use
        IPsec-encrypted Cloud Interconnect create the attachment using this
        option.

        Not currently available publicly. Default value: "NONE" Possible values: ["NONE", "IPSEC"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#encryption GoogleComputeInterconnectAttachment#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#id GoogleComputeInterconnectAttachment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interconnect(self) -> typing.Optional[builtins.str]:
        '''URL of the underlying Interconnect object that this attachment's traffic will traverse through.

        Required if type is DEDICATED, must not
        be set if type is PARTNER.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#interconnect GoogleComputeInterconnectAttachment#interconnect}
        '''
        result = self._values.get("interconnect")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ipsec_internal_addresses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''URL of addresses that have been reserved for the interconnect attachment, Used only for interconnect attachment that has the encryption option as IPSEC.

        The addresses must be RFC 1918 IP address ranges. When creating HA
        VPN gateway over the interconnect attachment, if the attachment is
        configured to use an RFC 1918 IP address, then the VPN gateway's IP
        address will be allocated from the IP address range specified
        here.

        For example, if the HA VPN gateway's interface 0 is paired to this
        interconnect attachment, then an RFC 1918 IP address for the VPN
        gateway interface 0 will be allocated from the IP address specified
        for this interconnect attachment.

        If this field is not specified for interconnect attachment that has
        encryption option as IPSEC, later on when creating HA VPN gateway on
        this interconnect attachment, the HA VPN gateway's IP address will be
        allocated from regional external IP address pool.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#ipsec_internal_addresses GoogleComputeInterconnectAttachment#ipsec_internal_addresses}
        '''
        result = self._values.get("ipsec_internal_addresses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def mtu(self) -> typing.Optional[builtins.str]:
        '''Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment.

        Currently, only 1440 and 1500 are allowed. If not specified, the value will default to 1440.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#mtu GoogleComputeInterconnectAttachment#mtu}
        '''
        result = self._values.get("mtu")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#project GoogleComputeInterconnectAttachment#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''Region where the regional interconnect attachment resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#region GoogleComputeInterconnectAttachment#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleComputeInterconnectAttachmentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#timeouts GoogleComputeInterconnectAttachment#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeInterconnectAttachmentTimeouts"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of InterconnectAttachment you wish to create. Defaults to DEDICATED. Possible values: ["DEDICATED", "PARTNER", "PARTNER_PROVIDER"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#type GoogleComputeInterconnectAttachment#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vlan_tag8021_q(self) -> typing.Optional[jsii.Number]:
        '''The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using PARTNER type this will be managed upstream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#vlan_tag8021q GoogleComputeInterconnectAttachment#vlan_tag8021q}
        '''
        result = self._values.get("vlan_tag8021_q")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInterconnectAttachmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInterconnectAttachment.GoogleComputeInterconnectAttachmentPrivateInterconnectInfo",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleComputeInterconnectAttachmentPrivateInterconnectInfo:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInterconnectAttachmentPrivateInterconnectInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInterconnectAttachment.GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList",
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
            type_hints = typing.get_type_hints(GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeInterconnectAttachmentPrivateInterconnectInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeInterconnectAttachmentPrivateInterconnectInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleComputeInterconnectAttachmentPrivateInterconnectInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInterconnectAttachment.GoogleComputeInterconnectAttachmentPrivateInterconnectInfoOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInterconnectAttachmentPrivateInterconnectInfoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="tag8021Q")
    def tag8021_q(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tag8021Q"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeInterconnectAttachmentPrivateInterconnectInfo]:
        return typing.cast(typing.Optional[GoogleComputeInterconnectAttachmentPrivateInterconnectInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeInterconnectAttachmentPrivateInterconnectInfo],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentPrivateInterconnectInfoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeInterconnectAttachment.GoogleComputeInterconnectAttachmentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeInterconnectAttachmentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#create GoogleComputeInterconnectAttachment#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#delete GoogleComputeInterconnectAttachment#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#update GoogleComputeInterconnectAttachment#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeInterconnectAttachmentTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#create GoogleComputeInterconnectAttachment#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#delete GoogleComputeInterconnectAttachment#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_interconnect_attachment#update GoogleComputeInterconnectAttachment#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeInterconnectAttachmentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeInterconnectAttachmentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeInterconnectAttachment.GoogleComputeInterconnectAttachmentTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeInterconnectAttachmentTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeInterconnectAttachmentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeInterconnectAttachmentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeInterconnectAttachmentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeInterconnectAttachmentTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeInterconnectAttachment",
    "GoogleComputeInterconnectAttachmentConfig",
    "GoogleComputeInterconnectAttachmentPrivateInterconnectInfo",
    "GoogleComputeInterconnectAttachmentPrivateInterconnectInfoList",
    "GoogleComputeInterconnectAttachmentPrivateInterconnectInfoOutputReference",
    "GoogleComputeInterconnectAttachmentTimeouts",
    "GoogleComputeInterconnectAttachmentTimeoutsOutputReference",
]

publication.publish()
