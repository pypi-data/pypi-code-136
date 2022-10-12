'''
# `google_compute_global_forwarding_rule`

Refer to the Terraform Registory for docs: [`google_compute_global_forwarding_rule`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule).
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


class GoogleComputeGlobalForwardingRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule google_compute_global_forwarding_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        target: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_address: typing.Optional[builtins.str] = None,
        ip_protocol: typing.Optional[builtins.str] = None,
        ip_version: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        load_balancing_scheme: typing.Optional[builtins.str] = None,
        metadata_filters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeGlobalForwardingRuleMetadataFilters", typing.Dict[str, typing.Any]]]]] = None,
        network: typing.Optional[builtins.str] = None,
        port_range: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeGlobalForwardingRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule google_compute_global_forwarding_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. Specifically, the name must be 1-63 characters long and match the regular expression ``[a-z]([-a-z0-9]*[a-z0-9])?`` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#name GoogleComputeGlobalForwardingRule#name}
        :param target: The URL of the target resource to receive the matched traffic. For regional forwarding rules, this target must live in the same region as the forwarding rule. For global forwarding rules, this target must be a global load balancing resource. The forwarded traffic must be of a type appropriate to the target object. For ``INTERNAL_SELF_MANAGED`` load balancing, only ``targetHttpProxy`` is valid, not ``targetHttpsProxy``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#target GoogleComputeGlobalForwardingRule#target}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#description GoogleComputeGlobalForwardingRule#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#id GoogleComputeGlobalForwardingRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_address: IP address that this forwarding rule serves. When a client sends traffic to this IP address, the forwarding rule directs the traffic to the target that you specify in the forwarding rule. If you don't specify a reserved IP address, an ephemeral IP address is assigned. Methods for specifying an IP address: * IPv4 dotted decimal, as in ``100.1.2.3`` * Full URL, as in ``https://www.googleapis.com/compute/v1/projects/project_id/regions/region/addresses/address-name`` * Partial URL or by name, as in: * ``projects/project_id/regions/region/addresses/address-name`` * ``regions/region/addresses/address-name`` * ``global/addresses/address-name`` * ``address-name`` The loadBalancingScheme and the forwarding rule's target determine the type of IP address that you can use. For detailed information, refer to `IP address specifications </load-balancing/docs/forwarding-rule-concepts#ip_address_specifications>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_address GoogleComputeGlobalForwardingRule#ip_address}
        :param ip_protocol: The IP protocol to which this rule applies. For protocol forwarding, valid options are ``TCP``, ``UDP``, ``ESP``, ``AH``, ``SCTP`` or ``ICMP``. For Internal TCP/UDP Load Balancing, the load balancing scheme is ``INTERNAL``, and one of ``TCP`` or ``UDP`` are valid. For Traffic Director, the load balancing scheme is ``INTERNAL_SELF_MANAGED``, and only ``TCP``is valid. For Internal HTTP(S) Load Balancing, the load balancing scheme is ``INTERNAL_MANAGED``, and only ``TCP`` is valid. For HTTP(S), SSL Proxy, and TCP Proxy Load Balancing, the load balancing scheme is ``EXTERNAL`` and only ``TCP`` is valid. For Network TCP/UDP Load Balancing, the load balancing scheme is ``EXTERNAL``, and one of ``TCP`` or ``UDP`` is valid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_protocol GoogleComputeGlobalForwardingRule#ip_protocol}
        :param ip_version: The IP Version that will be used by this forwarding rule. Valid options are ``IPV4`` or ``IPV6``. This can only be specified for an external global forwarding rule. Possible values: UNSPECIFIED_VERSION, IPV4, IPV6 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_version GoogleComputeGlobalForwardingRule#ip_version}
        :param labels: Labels to apply to this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#labels GoogleComputeGlobalForwardingRule#labels}
        :param load_balancing_scheme: Specifies the forwarding rule type. ``EXTERNAL`` is used for: Classic Cloud VPN gateways Protocol forwarding to VMs from an external IP address The following load balancers: HTTP(S), SSL Proxy, TCP Proxy, and Network TCP/UDP ``INTERNAL`` is used for: Protocol forwarding to VMs from an internal IP address Internal TCP/UDP load balancers ``INTERNAL_MANAGED`` is used for: Internal HTTP(S) load balancers ``INTERNAL_SELF_MANAGED`` is used for: Traffic Director ``EXTERNAL_MANAGED`` is used for: Global external HTTP(S) load balancers For more information about forwarding rules, refer to `Forwarding rule concepts </load-balancing/docs/forwarding-rule-concepts>`_. Possible values: INVALID, INTERNAL, INTERNAL_MANAGED, INTERNAL_SELF_MANAGED, EXTERNAL, EXTERNAL_MANAGED Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#load_balancing_scheme GoogleComputeGlobalForwardingRule#load_balancing_scheme}
        :param metadata_filters: metadata_filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#metadata_filters GoogleComputeGlobalForwardingRule#metadata_filters}
        :param network: This field is not used for external load balancing. For ``INTERNAL`` and ``INTERNAL_SELF_MANAGED`` load balancing, this field identifies the network that the load balanced IP should belong to for this Forwarding Rule. If this field is not specified, the default network will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#network GoogleComputeGlobalForwardingRule#network}
        :param port_range: When the load balancing scheme is ``EXTERNAL``, ``INTERNAL_SELF_MANAGED`` and ``INTERNAL_MANAGED``, you can specify a ``port_range``. Use with a forwarding rule that points to a target proxy or a target pool. Do not use with a forwarding rule that points to a backend service. This field is used along with the ``target`` field for TargetHttpProxy, TargetHttpsProxy, TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance. Applicable only when ``IPProtocol`` is ``TCP``, ``UDP``, or ``SCTP``, only packets addressed to ports in the specified range will be forwarded to ``target``. Forwarding rules with the same ``[IPAddress, IPProtocol]`` pair must have disjoint port ranges. Some types of forwarding target have constraints on the acceptable ports: TargetHttpProxy: 80, 8080 TargetHttpsProxy: 443 TargetTcpProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1688, 1883, 5222 TargetSslProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1688, 1883, 5222 TargetVpnGateway: 500, 4500
        :param project: The project this resource belongs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#project GoogleComputeGlobalForwardingRule#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#timeouts GoogleComputeGlobalForwardingRule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeGlobalForwardingRuleConfig(
            name=name,
            target=target,
            description=description,
            id=id,
            ip_address=ip_address,
            ip_protocol=ip_protocol,
            ip_version=ip_version,
            labels=labels,
            load_balancing_scheme=load_balancing_scheme,
            metadata_filters=metadata_filters,
            network=network,
            port_range=port_range,
            project=project,
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

    @jsii.member(jsii_name="putMetadataFilters")
    def put_metadata_filters(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeGlobalForwardingRuleMetadataFilters", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRule.put_metadata_filters)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetadataFilters", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#create GoogleComputeGlobalForwardingRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#delete GoogleComputeGlobalForwardingRule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#update GoogleComputeGlobalForwardingRule#update}.
        '''
        value = GoogleComputeGlobalForwardingRuleTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetIpProtocol")
    def reset_ip_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpProtocol", []))

    @jsii.member(jsii_name="resetIpVersion")
    def reset_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpVersion", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLoadBalancingScheme")
    def reset_load_balancing_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancingScheme", []))

    @jsii.member(jsii_name="resetMetadataFilters")
    def reset_metadata_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadataFilters", []))

    @jsii.member(jsii_name="resetNetwork")
    def reset_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetwork", []))

    @jsii.member(jsii_name="resetPortRange")
    def reset_port_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortRange", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="labelFingerprint")
    def label_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "labelFingerprint"))

    @builtins.property
    @jsii.member(jsii_name="metadataFilters")
    def metadata_filters(
        self,
    ) -> "GoogleComputeGlobalForwardingRuleMetadataFiltersList":
        return typing.cast("GoogleComputeGlobalForwardingRuleMetadataFiltersList", jsii.get(self, "metadataFilters"))

    @builtins.property
    @jsii.member(jsii_name="pscConnectionId")
    def psc_connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pscConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="pscConnectionStatus")
    def psc_connection_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pscConnectionStatus"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeGlobalForwardingRuleTimeoutsOutputReference":
        return typing.cast("GoogleComputeGlobalForwardingRuleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="ipProtocolInput")
    def ip_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ipVersionInput")
    def ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancingSchemeInput")
    def load_balancing_scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loadBalancingSchemeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataFiltersInput")
    def metadata_filters_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeGlobalForwardingRuleMetadataFilters"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeGlobalForwardingRuleMetadataFilters"]]], jsii.get(self, "metadataFiltersInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="portRangeInput")
    def port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeGlobalForwardingRuleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeGlobalForwardingRuleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="ipProtocol")
    def ip_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipProtocol"))

    @ip_protocol.setter
    def ip_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "ip_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="ipVersion")
    def ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipVersion"))

    @ip_version.setter
    def ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "ip_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipVersion", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancingScheme")
    def load_balancing_scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loadBalancingScheme"))

    @load_balancing_scheme.setter
    def load_balancing_scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "load_balancing_scheme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancingScheme", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="portRange")
    def port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portRange"))

    @port_range.setter
    def port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portRange", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRule, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleConfig",
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
        "target": "target",
        "description": "description",
        "id": "id",
        "ip_address": "ipAddress",
        "ip_protocol": "ipProtocol",
        "ip_version": "ipVersion",
        "labels": "labels",
        "load_balancing_scheme": "loadBalancingScheme",
        "metadata_filters": "metadataFilters",
        "network": "network",
        "port_range": "portRange",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleComputeGlobalForwardingRuleConfig(cdktf.TerraformMetaArguments):
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
        target: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ip_address: typing.Optional[builtins.str] = None,
        ip_protocol: typing.Optional[builtins.str] = None,
        ip_version: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        load_balancing_scheme: typing.Optional[builtins.str] = None,
        metadata_filters: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeGlobalForwardingRuleMetadataFilters", typing.Dict[str, typing.Any]]]]] = None,
        network: typing.Optional[builtins.str] = None,
        port_range: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeGlobalForwardingRuleTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. Specifically, the name must be 1-63 characters long and match the regular expression ``[a-z]([-a-z0-9]*[a-z0-9])?`` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#name GoogleComputeGlobalForwardingRule#name}
        :param target: The URL of the target resource to receive the matched traffic. For regional forwarding rules, this target must live in the same region as the forwarding rule. For global forwarding rules, this target must be a global load balancing resource. The forwarded traffic must be of a type appropriate to the target object. For ``INTERNAL_SELF_MANAGED`` load balancing, only ``targetHttpProxy`` is valid, not ``targetHttpsProxy``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#target GoogleComputeGlobalForwardingRule#target}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#description GoogleComputeGlobalForwardingRule#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#id GoogleComputeGlobalForwardingRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip_address: IP address that this forwarding rule serves. When a client sends traffic to this IP address, the forwarding rule directs the traffic to the target that you specify in the forwarding rule. If you don't specify a reserved IP address, an ephemeral IP address is assigned. Methods for specifying an IP address: * IPv4 dotted decimal, as in ``100.1.2.3`` * Full URL, as in ``https://www.googleapis.com/compute/v1/projects/project_id/regions/region/addresses/address-name`` * Partial URL or by name, as in: * ``projects/project_id/regions/region/addresses/address-name`` * ``regions/region/addresses/address-name`` * ``global/addresses/address-name`` * ``address-name`` The loadBalancingScheme and the forwarding rule's target determine the type of IP address that you can use. For detailed information, refer to `IP address specifications </load-balancing/docs/forwarding-rule-concepts#ip_address_specifications>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_address GoogleComputeGlobalForwardingRule#ip_address}
        :param ip_protocol: The IP protocol to which this rule applies. For protocol forwarding, valid options are ``TCP``, ``UDP``, ``ESP``, ``AH``, ``SCTP`` or ``ICMP``. For Internal TCP/UDP Load Balancing, the load balancing scheme is ``INTERNAL``, and one of ``TCP`` or ``UDP`` are valid. For Traffic Director, the load balancing scheme is ``INTERNAL_SELF_MANAGED``, and only ``TCP``is valid. For Internal HTTP(S) Load Balancing, the load balancing scheme is ``INTERNAL_MANAGED``, and only ``TCP`` is valid. For HTTP(S), SSL Proxy, and TCP Proxy Load Balancing, the load balancing scheme is ``EXTERNAL`` and only ``TCP`` is valid. For Network TCP/UDP Load Balancing, the load balancing scheme is ``EXTERNAL``, and one of ``TCP`` or ``UDP`` is valid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_protocol GoogleComputeGlobalForwardingRule#ip_protocol}
        :param ip_version: The IP Version that will be used by this forwarding rule. Valid options are ``IPV4`` or ``IPV6``. This can only be specified for an external global forwarding rule. Possible values: UNSPECIFIED_VERSION, IPV4, IPV6 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_version GoogleComputeGlobalForwardingRule#ip_version}
        :param labels: Labels to apply to this rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#labels GoogleComputeGlobalForwardingRule#labels}
        :param load_balancing_scheme: Specifies the forwarding rule type. ``EXTERNAL`` is used for: Classic Cloud VPN gateways Protocol forwarding to VMs from an external IP address The following load balancers: HTTP(S), SSL Proxy, TCP Proxy, and Network TCP/UDP ``INTERNAL`` is used for: Protocol forwarding to VMs from an internal IP address Internal TCP/UDP load balancers ``INTERNAL_MANAGED`` is used for: Internal HTTP(S) load balancers ``INTERNAL_SELF_MANAGED`` is used for: Traffic Director ``EXTERNAL_MANAGED`` is used for: Global external HTTP(S) load balancers For more information about forwarding rules, refer to `Forwarding rule concepts </load-balancing/docs/forwarding-rule-concepts>`_. Possible values: INVALID, INTERNAL, INTERNAL_MANAGED, INTERNAL_SELF_MANAGED, EXTERNAL, EXTERNAL_MANAGED Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#load_balancing_scheme GoogleComputeGlobalForwardingRule#load_balancing_scheme}
        :param metadata_filters: metadata_filters block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#metadata_filters GoogleComputeGlobalForwardingRule#metadata_filters}
        :param network: This field is not used for external load balancing. For ``INTERNAL`` and ``INTERNAL_SELF_MANAGED`` load balancing, this field identifies the network that the load balanced IP should belong to for this Forwarding Rule. If this field is not specified, the default network will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#network GoogleComputeGlobalForwardingRule#network}
        :param port_range: When the load balancing scheme is ``EXTERNAL``, ``INTERNAL_SELF_MANAGED`` and ``INTERNAL_MANAGED``, you can specify a ``port_range``. Use with a forwarding rule that points to a target proxy or a target pool. Do not use with a forwarding rule that points to a backend service. This field is used along with the ``target`` field for TargetHttpProxy, TargetHttpsProxy, TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance. Applicable only when ``IPProtocol`` is ``TCP``, ``UDP``, or ``SCTP``, only packets addressed to ports in the specified range will be forwarded to ``target``. Forwarding rules with the same ``[IPAddress, IPProtocol]`` pair must have disjoint port ranges. Some types of forwarding target have constraints on the acceptable ports: TargetHttpProxy: 80, 8080 TargetHttpsProxy: 443 TargetTcpProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1688, 1883, 5222 TargetSslProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1688, 1883, 5222 TargetVpnGateway: 500, 4500
        :param project: The project this resource belongs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#project GoogleComputeGlobalForwardingRule#project}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#timeouts GoogleComputeGlobalForwardingRule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeGlobalForwardingRuleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument ip_protocol", value=ip_protocol, expected_type=type_hints["ip_protocol"])
            check_type(argname="argument ip_version", value=ip_version, expected_type=type_hints["ip_version"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument load_balancing_scheme", value=load_balancing_scheme, expected_type=type_hints["load_balancing_scheme"])
            check_type(argname="argument metadata_filters", value=metadata_filters, expected_type=type_hints["metadata_filters"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "target": target,
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
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if ip_protocol is not None:
            self._values["ip_protocol"] = ip_protocol
        if ip_version is not None:
            self._values["ip_version"] = ip_version
        if labels is not None:
            self._values["labels"] = labels
        if load_balancing_scheme is not None:
            self._values["load_balancing_scheme"] = load_balancing_scheme
        if metadata_filters is not None:
            self._values["metadata_filters"] = metadata_filters
        if network is not None:
            self._values["network"] = network
        if port_range is not None:
            self._values["port_range"] = port_range
        if project is not None:
            self._values["project"] = project
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
        '''Name of the resource;

        provided by the client when the resource is created. The name must be 1-63 characters long, and comply with `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`_. Specifically, the name must be 1-63 characters long and match the regular expression ``[a-z]([-a-z0-9]*[a-z0-9])?`` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#name GoogleComputeGlobalForwardingRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''The URL of the target resource to receive the matched traffic.

        For regional forwarding rules, this target must live in the same region as the forwarding rule. For global forwarding rules, this target must be a global load balancing resource. The forwarded traffic must be of a type appropriate to the target object. For ``INTERNAL_SELF_MANAGED`` load balancing, only ``targetHttpProxy`` is valid, not ``targetHttpsProxy``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#target GoogleComputeGlobalForwardingRule#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#description GoogleComputeGlobalForwardingRule#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#id GoogleComputeGlobalForwardingRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''IP address that this forwarding rule serves.

        When a client sends traffic to this IP address, the forwarding rule directs the traffic to the target that you specify in the forwarding rule. If you don't specify a reserved IP address, an ephemeral IP address is assigned. Methods for specifying an IP address: * IPv4 dotted decimal, as in ``100.1.2.3`` * Full URL, as in ``https://www.googleapis.com/compute/v1/projects/project_id/regions/region/addresses/address-name`` * Partial URL or by name, as in: * ``projects/project_id/regions/region/addresses/address-name`` * ``regions/region/addresses/address-name`` * ``global/addresses/address-name`` * ``address-name`` The loadBalancingScheme and the forwarding rule's target determine the type of IP address that you can use. For detailed information, refer to `IP address specifications </load-balancing/docs/forwarding-rule-concepts#ip_address_specifications>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_address GoogleComputeGlobalForwardingRule#ip_address}
        '''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_protocol(self) -> typing.Optional[builtins.str]:
        '''The IP protocol to which this rule applies.

        For protocol forwarding, valid options are ``TCP``, ``UDP``, ``ESP``, ``AH``, ``SCTP`` or ``ICMP``. For Internal TCP/UDP Load Balancing, the load balancing scheme is ``INTERNAL``, and one of ``TCP`` or ``UDP`` are valid. For Traffic Director, the load balancing scheme is ``INTERNAL_SELF_MANAGED``, and only ``TCP``is valid. For Internal HTTP(S) Load Balancing, the load balancing scheme is ``INTERNAL_MANAGED``, and only ``TCP`` is valid. For HTTP(S), SSL Proxy, and TCP Proxy Load Balancing, the load balancing scheme is ``EXTERNAL`` and only ``TCP`` is valid. For Network TCP/UDP Load Balancing, the load balancing scheme is ``EXTERNAL``, and one of ``TCP`` or ``UDP`` is valid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_protocol GoogleComputeGlobalForwardingRule#ip_protocol}
        '''
        result = self._values.get("ip_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_version(self) -> typing.Optional[builtins.str]:
        '''The IP Version that will be used by this forwarding rule.

        Valid options are ``IPV4`` or ``IPV6``. This can only be specified for an external global forwarding rule. Possible values: UNSPECIFIED_VERSION, IPV4, IPV6

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#ip_version GoogleComputeGlobalForwardingRule#ip_version}
        '''
        result = self._values.get("ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Labels to apply to this rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#labels GoogleComputeGlobalForwardingRule#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def load_balancing_scheme(self) -> typing.Optional[builtins.str]:
        '''Specifies the forwarding rule type.

        ``EXTERNAL`` is used for:
        Classic Cloud VPN gateways
        Protocol forwarding to VMs from an external IP address
        The following load balancers: HTTP(S), SSL Proxy, TCP Proxy, and Network TCP/UDP
        ``INTERNAL`` is used for:
        Protocol forwarding to VMs from an internal IP address
        Internal TCP/UDP load balancers
        ``INTERNAL_MANAGED`` is used for:
        Internal HTTP(S) load balancers
        ``INTERNAL_SELF_MANAGED`` is used for:
        Traffic Director
        ``EXTERNAL_MANAGED`` is used for:
        Global external HTTP(S) load balancers

        For more information about forwarding rules, refer to `Forwarding rule concepts </load-balancing/docs/forwarding-rule-concepts>`_. Possible values: INVALID, INTERNAL, INTERNAL_MANAGED, INTERNAL_SELF_MANAGED, EXTERNAL, EXTERNAL_MANAGED

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#load_balancing_scheme GoogleComputeGlobalForwardingRule#load_balancing_scheme}
        '''
        result = self._values.get("load_balancing_scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_filters(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeGlobalForwardingRuleMetadataFilters"]]]:
        '''metadata_filters block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#metadata_filters GoogleComputeGlobalForwardingRule#metadata_filters}
        '''
        result = self._values.get("metadata_filters")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeGlobalForwardingRuleMetadataFilters"]]], result)

    @builtins.property
    def network(self) -> typing.Optional[builtins.str]:
        '''This field is not used for external load balancing.

        For ``INTERNAL`` and ``INTERNAL_SELF_MANAGED`` load balancing, this field identifies the network that the load balanced IP should belong to for this Forwarding Rule. If this field is not specified, the default network will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#network GoogleComputeGlobalForwardingRule#network}
        '''
        result = self._values.get("network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_range(self) -> typing.Optional[builtins.str]:
        '''When the load balancing scheme is ``EXTERNAL``, ``INTERNAL_SELF_MANAGED`` and ``INTERNAL_MANAGED``, you can specify a ``port_range``.

        Use with a forwarding rule that points to a target proxy or a target pool. Do not use with a forwarding rule that points to a backend service. This field is used along with the ``target`` field for TargetHttpProxy, TargetHttpsProxy, TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance. Applicable only when ``IPProtocol`` is ``TCP``, ``UDP``, or ``SCTP``, only packets addressed to ports in the specified range will be forwarded to ``target``. Forwarding rules with the same ``[IPAddress, IPProtocol]`` pair must have disjoint port ranges. Some types of forwarding target have constraints on the acceptable ports:

        TargetHttpProxy: 80, 8080
        TargetHttpsProxy: 443
        TargetTcpProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1688, 1883, 5222
        TargetSslProxy: 25, 43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1688, 1883, 5222
        TargetVpnGateway: 500, 4500

        :pattern:

        : d+(?:-d+)?

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#port_range GoogleComputeGlobalForwardingRule#port_range}
        '''
        result = self._values.get("port_range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project this resource belongs in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#project GoogleComputeGlobalForwardingRule#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeGlobalForwardingRuleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#timeouts GoogleComputeGlobalForwardingRule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeGlobalForwardingRuleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeGlobalForwardingRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleMetadataFilters",
    jsii_struct_bases=[],
    name_mapping={
        "filter_labels": "filterLabels",
        "filter_match_criteria": "filterMatchCriteria",
    },
)
class GoogleComputeGlobalForwardingRuleMetadataFilters:
    def __init__(
        self,
        *,
        filter_labels: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels", typing.Dict[str, typing.Any]]]],
        filter_match_criteria: builtins.str,
    ) -> None:
        '''
        :param filter_labels: filter_labels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#filter_labels GoogleComputeGlobalForwardingRule#filter_labels}
        :param filter_match_criteria: Specifies how individual ``filterLabel`` matches within the list of ``filterLabel``s contribute towards the overall ``metadataFilter`` match. Supported values are: MATCH_ANY: At least one of the ``filterLabels`` must have a matching label in the provided metadata. MATCH_ALL: All ``filterLabels`` must have matching labels in the provided metadata. Possible values: NOT_SET, MATCH_ALL, MATCH_ANY Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#filter_match_criteria GoogleComputeGlobalForwardingRule#filter_match_criteria}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFilters.__init__)
            check_type(argname="argument filter_labels", value=filter_labels, expected_type=type_hints["filter_labels"])
            check_type(argname="argument filter_match_criteria", value=filter_match_criteria, expected_type=type_hints["filter_match_criteria"])
        self._values: typing.Dict[str, typing.Any] = {
            "filter_labels": filter_labels,
            "filter_match_criteria": filter_match_criteria,
        }

    @builtins.property
    def filter_labels(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels"]]:
        '''filter_labels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#filter_labels GoogleComputeGlobalForwardingRule#filter_labels}
        '''
        result = self._values.get("filter_labels")
        assert result is not None, "Required property 'filter_labels' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels"]], result)

    @builtins.property
    def filter_match_criteria(self) -> builtins.str:
        '''Specifies how individual ``filterLabel`` matches within the list of ``filterLabel``s contribute towards the overall ``metadataFilter`` match.

        Supported values are:

        MATCH_ANY: At least one of the ``filterLabels`` must have a matching label in the provided metadata.
        MATCH_ALL: All ``filterLabels`` must have matching labels in the provided metadata. Possible values: NOT_SET, MATCH_ALL, MATCH_ANY

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#filter_match_criteria GoogleComputeGlobalForwardingRule#filter_match_criteria}
        '''
        result = self._values.get("filter_match_criteria")
        assert result is not None, "Required property 'filter_match_criteria' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeGlobalForwardingRuleMetadataFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Name of metadata label. The name can have a maximum length of 1024 characters and must be at least 1 character long. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#name GoogleComputeGlobalForwardingRule#name}
        :param value: The value of the label must match the specified value. value can have a maximum length of 1024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#value GoogleComputeGlobalForwardingRule#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of metadata label.

        The name can have a maximum length of 1024 characters and must be at least 1 character long.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#name GoogleComputeGlobalForwardingRule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the label must match the specified value.

        value can have a maximum length of 1024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#value GoogleComputeGlobalForwardingRule#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList",
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
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeGlobalForwardingRuleMetadataFiltersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleMetadataFiltersList",
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
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFilters]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFilters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFilters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilterLabels")
    def put_filter_labels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference.put_filter_labels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilterLabels", [value]))

    @builtins.property
    @jsii.member(jsii_name="filterLabels")
    def filter_labels(
        self,
    ) -> GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList:
        return typing.cast(GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList, jsii.get(self, "filterLabels"))

    @builtins.property
    @jsii.member(jsii_name="filterLabelsInput")
    def filter_labels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels]]], jsii.get(self, "filterLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="filterMatchCriteriaInput")
    def filter_match_criteria_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterMatchCriteriaInput"))

    @builtins.property
    @jsii.member(jsii_name="filterMatchCriteria")
    def filter_match_criteria(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filterMatchCriteria"))

    @filter_match_criteria.setter
    def filter_match_criteria(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference, "filter_match_criteria").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterMatchCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleMetadataFilters, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleMetadataFilters, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleMetadataFilters, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeGlobalForwardingRuleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#create GoogleComputeGlobalForwardingRule#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#delete GoogleComputeGlobalForwardingRule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#update GoogleComputeGlobalForwardingRule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#create GoogleComputeGlobalForwardingRule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#delete GoogleComputeGlobalForwardingRule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_global_forwarding_rule#update GoogleComputeGlobalForwardingRule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeGlobalForwardingRuleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeGlobalForwardingRuleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeGlobalForwardingRule.GoogleComputeGlobalForwardingRuleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeGlobalForwardingRuleTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeGlobalForwardingRuleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeGlobalForwardingRuleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeGlobalForwardingRule",
    "GoogleComputeGlobalForwardingRuleConfig",
    "GoogleComputeGlobalForwardingRuleMetadataFilters",
    "GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabels",
    "GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsList",
    "GoogleComputeGlobalForwardingRuleMetadataFiltersFilterLabelsOutputReference",
    "GoogleComputeGlobalForwardingRuleMetadataFiltersList",
    "GoogleComputeGlobalForwardingRuleMetadataFiltersOutputReference",
    "GoogleComputeGlobalForwardingRuleTimeouts",
    "GoogleComputeGlobalForwardingRuleTimeoutsOutputReference",
]

publication.publish()
