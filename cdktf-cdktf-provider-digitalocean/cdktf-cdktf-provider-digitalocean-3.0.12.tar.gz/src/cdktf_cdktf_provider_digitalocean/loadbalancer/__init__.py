'''
# `digitalocean_loadbalancer`

Refer to the Terraform Registory for docs: [`digitalocean_loadbalancer`](https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer).
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


class Loadbalancer(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.Loadbalancer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer digitalocean_loadbalancer}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        forwarding_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerForwardingRule", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        region: builtins.str,
        algorithm: typing.Optional[builtins.str] = None,
        disable_lets_encrypt_dns_records: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        droplet_tag: typing.Optional[builtins.str] = None,
        enable_backend_keepalive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_proxy_protocol: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        healthcheck: typing.Optional[typing.Union["LoadbalancerHealthcheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        redirect_http_to_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        size: typing.Optional[builtins.str] = None,
        size_unit: typing.Optional[jsii.Number] = None,
        sticky_sessions: typing.Optional[typing.Union["LoadbalancerStickySessions", typing.Dict[str, typing.Any]]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer digitalocean_loadbalancer} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param forwarding_rule: forwarding_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#forwarding_rule Loadbalancer#forwarding_rule}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#name Loadbalancer#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#region Loadbalancer#region}.
        :param algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#algorithm Loadbalancer#algorithm}.
        :param disable_lets_encrypt_dns_records: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#disable_lets_encrypt_dns_records Loadbalancer#disable_lets_encrypt_dns_records}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#droplet_ids Loadbalancer#droplet_ids}.
        :param droplet_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#droplet_tag Loadbalancer#droplet_tag}.
        :param enable_backend_keepalive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#enable_backend_keepalive Loadbalancer#enable_backend_keepalive}.
        :param enable_proxy_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#enable_proxy_protocol Loadbalancer#enable_proxy_protocol}.
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#healthcheck Loadbalancer#healthcheck}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#id Loadbalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param redirect_http_to_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#redirect_http_to_https Loadbalancer#redirect_http_to_https}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#size Loadbalancer#size}.
        :param size_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#size_unit Loadbalancer#size_unit}.
        :param sticky_sessions: sticky_sessions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#sticky_sessions Loadbalancer#sticky_sessions}
        :param vpc_uuid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#vpc_uuid Loadbalancer#vpc_uuid}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Loadbalancer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LoadbalancerConfig(
            forwarding_rule=forwarding_rule,
            name=name,
            region=region,
            algorithm=algorithm,
            disable_lets_encrypt_dns_records=disable_lets_encrypt_dns_records,
            droplet_ids=droplet_ids,
            droplet_tag=droplet_tag,
            enable_backend_keepalive=enable_backend_keepalive,
            enable_proxy_protocol=enable_proxy_protocol,
            healthcheck=healthcheck,
            id=id,
            redirect_http_to_https=redirect_http_to_https,
            size=size,
            size_unit=size_unit,
            sticky_sessions=sticky_sessions,
            vpc_uuid=vpc_uuid,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putForwardingRule")
    def put_forwarding_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerForwardingRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Loadbalancer.put_forwarding_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putForwardingRule", [value]))

    @jsii.member(jsii_name="putHealthcheck")
    def put_healthcheck(
        self,
        *,
        port: jsii.Number,
        protocol: builtins.str,
        check_interval_seconds: typing.Optional[jsii.Number] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        response_timeout_seconds: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#port Loadbalancer#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#protocol Loadbalancer#protocol}.
        :param check_interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#check_interval_seconds Loadbalancer#check_interval_seconds}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#healthy_threshold Loadbalancer#healthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#path Loadbalancer#path}.
        :param response_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#response_timeout_seconds Loadbalancer#response_timeout_seconds}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#unhealthy_threshold Loadbalancer#unhealthy_threshold}.
        '''
        value = LoadbalancerHealthcheck(
            port=port,
            protocol=protocol,
            check_interval_seconds=check_interval_seconds,
            healthy_threshold=healthy_threshold,
            path=path,
            response_timeout_seconds=response_timeout_seconds,
            unhealthy_threshold=unhealthy_threshold,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthcheck", [value]))

    @jsii.member(jsii_name="putStickySessions")
    def put_sticky_sessions(
        self,
        *,
        cookie_name: typing.Optional[builtins.str] = None,
        cookie_ttl_seconds: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#cookie_name Loadbalancer#cookie_name}.
        :param cookie_ttl_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#cookie_ttl_seconds Loadbalancer#cookie_ttl_seconds}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#type Loadbalancer#type}.
        '''
        value = LoadbalancerStickySessions(
            cookie_name=cookie_name, cookie_ttl_seconds=cookie_ttl_seconds, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putStickySessions", [value]))

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetDisableLetsEncryptDnsRecords")
    def reset_disable_lets_encrypt_dns_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableLetsEncryptDnsRecords", []))

    @jsii.member(jsii_name="resetDropletIds")
    def reset_droplet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropletIds", []))

    @jsii.member(jsii_name="resetDropletTag")
    def reset_droplet_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDropletTag", []))

    @jsii.member(jsii_name="resetEnableBackendKeepalive")
    def reset_enable_backend_keepalive(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableBackendKeepalive", []))

    @jsii.member(jsii_name="resetEnableProxyProtocol")
    def reset_enable_proxy_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableProxyProtocol", []))

    @jsii.member(jsii_name="resetHealthcheck")
    def reset_healthcheck(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthcheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRedirectHttpToHttps")
    def reset_redirect_http_to_https(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedirectHttpToHttps", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetSizeUnit")
    def reset_size_unit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizeUnit", []))

    @jsii.member(jsii_name="resetStickySessions")
    def reset_sticky_sessions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStickySessions", []))

    @jsii.member(jsii_name="resetVpcUuid")
    def reset_vpc_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcUuid", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="forwardingRule")
    def forwarding_rule(self) -> "LoadbalancerForwardingRuleList":
        return typing.cast("LoadbalancerForwardingRuleList", jsii.get(self, "forwardingRule"))

    @builtins.property
    @jsii.member(jsii_name="healthcheck")
    def healthcheck(self) -> "LoadbalancerHealthcheckOutputReference":
        return typing.cast("LoadbalancerHealthcheckOutputReference", jsii.get(self, "healthcheck"))

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="stickySessions")
    def sticky_sessions(self) -> "LoadbalancerStickySessionsOutputReference":
        return typing.cast("LoadbalancerStickySessionsOutputReference", jsii.get(self, "stickySessions"))

    @builtins.property
    @jsii.member(jsii_name="urn")
    def urn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urn"))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="disableLetsEncryptDnsRecordsInput")
    def disable_lets_encrypt_dns_records_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableLetsEncryptDnsRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="dropletIdsInput")
    def droplet_ids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "dropletIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="dropletTagInput")
    def droplet_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dropletTagInput"))

    @builtins.property
    @jsii.member(jsii_name="enableBackendKeepaliveInput")
    def enable_backend_keepalive_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableBackendKeepaliveInput"))

    @builtins.property
    @jsii.member(jsii_name="enableProxyProtocolInput")
    def enable_proxy_protocol_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableProxyProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingRuleInput")
    def forwarding_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerForwardingRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LoadbalancerForwardingRule"]]], jsii.get(self, "forwardingRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="healthcheckInput")
    def healthcheck_input(self) -> typing.Optional["LoadbalancerHealthcheck"]:
        return typing.cast(typing.Optional["LoadbalancerHealthcheck"], jsii.get(self, "healthcheckInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="redirectHttpToHttpsInput")
    def redirect_http_to_https_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "redirectHttpToHttpsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeUnitInput")
    def size_unit_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeUnitInput"))

    @builtins.property
    @jsii.member(jsii_name="stickySessionsInput")
    def sticky_sessions_input(self) -> typing.Optional["LoadbalancerStickySessions"]:
        return typing.cast(typing.Optional["LoadbalancerStickySessions"], jsii.get(self, "stickySessionsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcUuidInput")
    def vpc_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="disableLetsEncryptDnsRecords")
    def disable_lets_encrypt_dns_records(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableLetsEncryptDnsRecords"))

    @disable_lets_encrypt_dns_records.setter
    def disable_lets_encrypt_dns_records(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "disable_lets_encrypt_dns_records").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableLetsEncryptDnsRecords", value)

    @builtins.property
    @jsii.member(jsii_name="dropletIds")
    def droplet_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "dropletIds"))

    @droplet_ids.setter
    def droplet_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "droplet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dropletIds", value)

    @builtins.property
    @jsii.member(jsii_name="dropletTag")
    def droplet_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dropletTag"))

    @droplet_tag.setter
    def droplet_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "droplet_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dropletTag", value)

    @builtins.property
    @jsii.member(jsii_name="enableBackendKeepalive")
    def enable_backend_keepalive(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableBackendKeepalive"))

    @enable_backend_keepalive.setter
    def enable_backend_keepalive(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "enable_backend_keepalive").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableBackendKeepalive", value)

    @builtins.property
    @jsii.member(jsii_name="enableProxyProtocol")
    def enable_proxy_protocol(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableProxyProtocol"))

    @enable_proxy_protocol.setter
    def enable_proxy_protocol(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "enable_proxy_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableProxyProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="redirectHttpToHttps")
    def redirect_http_to_https(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "redirectHttpToHttps"))

    @redirect_http_to_https.setter
    def redirect_http_to_https(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "redirect_http_to_https").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redirectHttpToHttps", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "size"))

    @size.setter
    def size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="sizeUnit")
    def size_unit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "sizeUnit"))

    @size_unit.setter
    def size_unit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "size_unit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizeUnit", value)

    @builtins.property
    @jsii.member(jsii_name="vpcUuid")
    def vpc_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcUuid"))

    @vpc_uuid.setter
    def vpc_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Loadbalancer, "vpc_uuid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcUuid", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "forwarding_rule": "forwardingRule",
        "name": "name",
        "region": "region",
        "algorithm": "algorithm",
        "disable_lets_encrypt_dns_records": "disableLetsEncryptDnsRecords",
        "droplet_ids": "dropletIds",
        "droplet_tag": "dropletTag",
        "enable_backend_keepalive": "enableBackendKeepalive",
        "enable_proxy_protocol": "enableProxyProtocol",
        "healthcheck": "healthcheck",
        "id": "id",
        "redirect_http_to_https": "redirectHttpToHttps",
        "size": "size",
        "size_unit": "sizeUnit",
        "sticky_sessions": "stickySessions",
        "vpc_uuid": "vpcUuid",
    },
)
class LoadbalancerConfig(cdktf.TerraformMetaArguments):
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
        forwarding_rule: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LoadbalancerForwardingRule", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        region: builtins.str,
        algorithm: typing.Optional[builtins.str] = None,
        disable_lets_encrypt_dns_records: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        droplet_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        droplet_tag: typing.Optional[builtins.str] = None,
        enable_backend_keepalive: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_proxy_protocol: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        healthcheck: typing.Optional[typing.Union["LoadbalancerHealthcheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        redirect_http_to_https: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        size: typing.Optional[builtins.str] = None,
        size_unit: typing.Optional[jsii.Number] = None,
        sticky_sessions: typing.Optional[typing.Union["LoadbalancerStickySessions", typing.Dict[str, typing.Any]]] = None,
        vpc_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param forwarding_rule: forwarding_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#forwarding_rule Loadbalancer#forwarding_rule}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#name Loadbalancer#name}.
        :param region: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#region Loadbalancer#region}.
        :param algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#algorithm Loadbalancer#algorithm}.
        :param disable_lets_encrypt_dns_records: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#disable_lets_encrypt_dns_records Loadbalancer#disable_lets_encrypt_dns_records}.
        :param droplet_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#droplet_ids Loadbalancer#droplet_ids}.
        :param droplet_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#droplet_tag Loadbalancer#droplet_tag}.
        :param enable_backend_keepalive: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#enable_backend_keepalive Loadbalancer#enable_backend_keepalive}.
        :param enable_proxy_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#enable_proxy_protocol Loadbalancer#enable_proxy_protocol}.
        :param healthcheck: healthcheck block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#healthcheck Loadbalancer#healthcheck}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#id Loadbalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param redirect_http_to_https: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#redirect_http_to_https Loadbalancer#redirect_http_to_https}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#size Loadbalancer#size}.
        :param size_unit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#size_unit Loadbalancer#size_unit}.
        :param sticky_sessions: sticky_sessions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#sticky_sessions Loadbalancer#sticky_sessions}
        :param vpc_uuid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#vpc_uuid Loadbalancer#vpc_uuid}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(healthcheck, dict):
            healthcheck = LoadbalancerHealthcheck(**healthcheck)
        if isinstance(sticky_sessions, dict):
            sticky_sessions = LoadbalancerStickySessions(**sticky_sessions)
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument forwarding_rule", value=forwarding_rule, expected_type=type_hints["forwarding_rule"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument disable_lets_encrypt_dns_records", value=disable_lets_encrypt_dns_records, expected_type=type_hints["disable_lets_encrypt_dns_records"])
            check_type(argname="argument droplet_ids", value=droplet_ids, expected_type=type_hints["droplet_ids"])
            check_type(argname="argument droplet_tag", value=droplet_tag, expected_type=type_hints["droplet_tag"])
            check_type(argname="argument enable_backend_keepalive", value=enable_backend_keepalive, expected_type=type_hints["enable_backend_keepalive"])
            check_type(argname="argument enable_proxy_protocol", value=enable_proxy_protocol, expected_type=type_hints["enable_proxy_protocol"])
            check_type(argname="argument healthcheck", value=healthcheck, expected_type=type_hints["healthcheck"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument redirect_http_to_https", value=redirect_http_to_https, expected_type=type_hints["redirect_http_to_https"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument size_unit", value=size_unit, expected_type=type_hints["size_unit"])
            check_type(argname="argument sticky_sessions", value=sticky_sessions, expected_type=type_hints["sticky_sessions"])
            check_type(argname="argument vpc_uuid", value=vpc_uuid, expected_type=type_hints["vpc_uuid"])
        self._values: typing.Dict[str, typing.Any] = {
            "forwarding_rule": forwarding_rule,
            "name": name,
            "region": region,
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
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if disable_lets_encrypt_dns_records is not None:
            self._values["disable_lets_encrypt_dns_records"] = disable_lets_encrypt_dns_records
        if droplet_ids is not None:
            self._values["droplet_ids"] = droplet_ids
        if droplet_tag is not None:
            self._values["droplet_tag"] = droplet_tag
        if enable_backend_keepalive is not None:
            self._values["enable_backend_keepalive"] = enable_backend_keepalive
        if enable_proxy_protocol is not None:
            self._values["enable_proxy_protocol"] = enable_proxy_protocol
        if healthcheck is not None:
            self._values["healthcheck"] = healthcheck
        if id is not None:
            self._values["id"] = id
        if redirect_http_to_https is not None:
            self._values["redirect_http_to_https"] = redirect_http_to_https
        if size is not None:
            self._values["size"] = size
        if size_unit is not None:
            self._values["size_unit"] = size_unit
        if sticky_sessions is not None:
            self._values["sticky_sessions"] = sticky_sessions
        if vpc_uuid is not None:
            self._values["vpc_uuid"] = vpc_uuid

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
    def forwarding_rule(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LoadbalancerForwardingRule"]]:
        '''forwarding_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#forwarding_rule Loadbalancer#forwarding_rule}
        '''
        result = self._values.get("forwarding_rule")
        assert result is not None, "Required property 'forwarding_rule' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LoadbalancerForwardingRule"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#name Loadbalancer#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#region Loadbalancer#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#algorithm Loadbalancer#algorithm}.'''
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_lets_encrypt_dns_records(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#disable_lets_encrypt_dns_records Loadbalancer#disable_lets_encrypt_dns_records}.'''
        result = self._values.get("disable_lets_encrypt_dns_records")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def droplet_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#droplet_ids Loadbalancer#droplet_ids}.'''
        result = self._values.get("droplet_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def droplet_tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#droplet_tag Loadbalancer#droplet_tag}.'''
        result = self._values.get("droplet_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_backend_keepalive(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#enable_backend_keepalive Loadbalancer#enable_backend_keepalive}.'''
        result = self._values.get("enable_backend_keepalive")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_proxy_protocol(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#enable_proxy_protocol Loadbalancer#enable_proxy_protocol}.'''
        result = self._values.get("enable_proxy_protocol")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def healthcheck(self) -> typing.Optional["LoadbalancerHealthcheck"]:
        '''healthcheck block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#healthcheck Loadbalancer#healthcheck}
        '''
        result = self._values.get("healthcheck")
        return typing.cast(typing.Optional["LoadbalancerHealthcheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#id Loadbalancer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def redirect_http_to_https(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#redirect_http_to_https Loadbalancer#redirect_http_to_https}.'''
        result = self._values.get("redirect_http_to_https")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def size(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#size Loadbalancer#size}.'''
        result = self._values.get("size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size_unit(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#size_unit Loadbalancer#size_unit}.'''
        result = self._values.get("size_unit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sticky_sessions(self) -> typing.Optional["LoadbalancerStickySessions"]:
        '''sticky_sessions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#sticky_sessions Loadbalancer#sticky_sessions}
        '''
        result = self._values.get("sticky_sessions")
        return typing.cast(typing.Optional["LoadbalancerStickySessions"], result)

    @builtins.property
    def vpc_uuid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#vpc_uuid Loadbalancer#vpc_uuid}.'''
        result = self._values.get("vpc_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerForwardingRule",
    jsii_struct_bases=[],
    name_mapping={
        "entry_port": "entryPort",
        "entry_protocol": "entryProtocol",
        "target_port": "targetPort",
        "target_protocol": "targetProtocol",
        "certificate_id": "certificateId",
        "certificate_name": "certificateName",
        "tls_passthrough": "tlsPassthrough",
    },
)
class LoadbalancerForwardingRule:
    def __init__(
        self,
        *,
        entry_port: jsii.Number,
        entry_protocol: builtins.str,
        target_port: jsii.Number,
        target_protocol: builtins.str,
        certificate_id: typing.Optional[builtins.str] = None,
        certificate_name: typing.Optional[builtins.str] = None,
        tls_passthrough: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param entry_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#entry_port Loadbalancer#entry_port}.
        :param entry_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#entry_protocol Loadbalancer#entry_protocol}.
        :param target_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#target_port Loadbalancer#target_port}.
        :param target_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#target_protocol Loadbalancer#target_protocol}.
        :param certificate_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#certificate_id Loadbalancer#certificate_id}.
        :param certificate_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#certificate_name Loadbalancer#certificate_name}.
        :param tls_passthrough: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#tls_passthrough Loadbalancer#tls_passthrough}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerForwardingRule.__init__)
            check_type(argname="argument entry_port", value=entry_port, expected_type=type_hints["entry_port"])
            check_type(argname="argument entry_protocol", value=entry_protocol, expected_type=type_hints["entry_protocol"])
            check_type(argname="argument target_port", value=target_port, expected_type=type_hints["target_port"])
            check_type(argname="argument target_protocol", value=target_protocol, expected_type=type_hints["target_protocol"])
            check_type(argname="argument certificate_id", value=certificate_id, expected_type=type_hints["certificate_id"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument tls_passthrough", value=tls_passthrough, expected_type=type_hints["tls_passthrough"])
        self._values: typing.Dict[str, typing.Any] = {
            "entry_port": entry_port,
            "entry_protocol": entry_protocol,
            "target_port": target_port,
            "target_protocol": target_protocol,
        }
        if certificate_id is not None:
            self._values["certificate_id"] = certificate_id
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if tls_passthrough is not None:
            self._values["tls_passthrough"] = tls_passthrough

    @builtins.property
    def entry_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#entry_port Loadbalancer#entry_port}.'''
        result = self._values.get("entry_port")
        assert result is not None, "Required property 'entry_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def entry_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#entry_protocol Loadbalancer#entry_protocol}.'''
        result = self._values.get("entry_protocol")
        assert result is not None, "Required property 'entry_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#target_port Loadbalancer#target_port}.'''
        result = self._values.get("target_port")
        assert result is not None, "Required property 'target_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target_protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#target_protocol Loadbalancer#target_protocol}.'''
        result = self._values.get("target_protocol")
        assert result is not None, "Required property 'target_protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#certificate_id Loadbalancer#certificate_id}.'''
        result = self._values.get("certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#certificate_name Loadbalancer#certificate_name}.'''
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_passthrough(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#tls_passthrough Loadbalancer#tls_passthrough}.'''
        result = self._values.get("tls_passthrough")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerForwardingRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerForwardingRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerForwardingRuleList",
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
            type_hints = typing.get_type_hints(LoadbalancerForwardingRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "LoadbalancerForwardingRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerForwardingRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LoadbalancerForwardingRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerForwardingRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerForwardingRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LoadbalancerForwardingRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LoadbalancerForwardingRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerForwardingRuleOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerForwardingRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCertificateId")
    def reset_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateId", []))

    @jsii.member(jsii_name="resetCertificateName")
    def reset_certificate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateName", []))

    @jsii.member(jsii_name="resetTlsPassthrough")
    def reset_tls_passthrough(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsPassthrough", []))

    @builtins.property
    @jsii.member(jsii_name="certificateIdInput")
    def certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateNameInput")
    def certificate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="entryPortInput")
    def entry_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "entryPortInput"))

    @builtins.property
    @jsii.member(jsii_name="entryProtocolInput")
    def entry_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entryProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortInput")
    def target_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetPortInput"))

    @builtins.property
    @jsii.member(jsii_name="targetProtocolInput")
    def target_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsPassthroughInput")
    def tls_passthrough_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tlsPassthroughInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateId")
    def certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateId"))

    @certificate_id.setter
    def certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "certificate_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateId", value)

    @builtins.property
    @jsii.member(jsii_name="certificateName")
    def certificate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateName"))

    @certificate_name.setter
    def certificate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "certificate_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateName", value)

    @builtins.property
    @jsii.member(jsii_name="entryPort")
    def entry_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "entryPort"))

    @entry_port.setter
    def entry_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "entry_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entryPort", value)

    @builtins.property
    @jsii.member(jsii_name="entryProtocol")
    def entry_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entryProtocol"))

    @entry_protocol.setter
    def entry_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "entry_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entryProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="targetPort")
    def target_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetPort"))

    @target_port.setter
    def target_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "target_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPort", value)

    @builtins.property
    @jsii.member(jsii_name="targetProtocol")
    def target_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetProtocol"))

    @target_protocol.setter
    def target_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "target_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="tlsPassthrough")
    def tls_passthrough(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tlsPassthrough"))

    @tls_passthrough.setter
    def tls_passthrough(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "tls_passthrough").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsPassthrough", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LoadbalancerForwardingRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LoadbalancerForwardingRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LoadbalancerForwardingRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerForwardingRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerHealthcheck",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "protocol": "protocol",
        "check_interval_seconds": "checkIntervalSeconds",
        "healthy_threshold": "healthyThreshold",
        "path": "path",
        "response_timeout_seconds": "responseTimeoutSeconds",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class LoadbalancerHealthcheck:
    def __init__(
        self,
        *,
        port: jsii.Number,
        protocol: builtins.str,
        check_interval_seconds: typing.Optional[jsii.Number] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        path: typing.Optional[builtins.str] = None,
        response_timeout_seconds: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#port Loadbalancer#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#protocol Loadbalancer#protocol}.
        :param check_interval_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#check_interval_seconds Loadbalancer#check_interval_seconds}.
        :param healthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#healthy_threshold Loadbalancer#healthy_threshold}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#path Loadbalancer#path}.
        :param response_timeout_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#response_timeout_seconds Loadbalancer#response_timeout_seconds}.
        :param unhealthy_threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#unhealthy_threshold Loadbalancer#unhealthy_threshold}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerHealthcheck.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument check_interval_seconds", value=check_interval_seconds, expected_type=type_hints["check_interval_seconds"])
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument response_timeout_seconds", value=response_timeout_seconds, expected_type=type_hints["response_timeout_seconds"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "port": port,
            "protocol": protocol,
        }
        if check_interval_seconds is not None:
            self._values["check_interval_seconds"] = check_interval_seconds
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if path is not None:
            self._values["path"] = path
        if response_timeout_seconds is not None:
            self._values["response_timeout_seconds"] = response_timeout_seconds
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#port Loadbalancer#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#protocol Loadbalancer#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def check_interval_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#check_interval_seconds Loadbalancer#check_interval_seconds}.'''
        result = self._values.get("check_interval_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#healthy_threshold Loadbalancer#healthy_threshold}.'''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#path Loadbalancer#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#response_timeout_seconds Loadbalancer#response_timeout_seconds}.'''
        result = self._values.get("response_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#unhealthy_threshold Loadbalancer#unhealthy_threshold}.'''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerHealthcheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerHealthcheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerHealthcheckOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerHealthcheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheckIntervalSeconds")
    def reset_check_interval_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckIntervalSeconds", []))

    @jsii.member(jsii_name="resetHealthyThreshold")
    def reset_healthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthyThreshold", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetResponseTimeoutSeconds")
    def reset_response_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseTimeoutSeconds", []))

    @jsii.member(jsii_name="resetUnhealthyThreshold")
    def reset_unhealthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyThreshold", []))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalSecondsInput")
    def check_interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "checkIntervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="responseTimeoutSecondsInput")
    def response_timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "responseTimeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalSeconds")
    def check_interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "checkIntervalSeconds"))

    @check_interval_seconds.setter
    def check_interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "check_interval_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkIntervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "healthy_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="responseTimeoutSeconds")
    def response_timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "responseTimeoutSeconds"))

    @response_timeout_seconds.setter
    def response_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "response_timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "unhealthy_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerHealthcheck]:
        return typing.cast(typing.Optional[LoadbalancerHealthcheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LoadbalancerHealthcheck]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerHealthcheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerStickySessions",
    jsii_struct_bases=[],
    name_mapping={
        "cookie_name": "cookieName",
        "cookie_ttl_seconds": "cookieTtlSeconds",
        "type": "type",
    },
)
class LoadbalancerStickySessions:
    def __init__(
        self,
        *,
        cookie_name: typing.Optional[builtins.str] = None,
        cookie_ttl_seconds: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cookie_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#cookie_name Loadbalancer#cookie_name}.
        :param cookie_ttl_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#cookie_ttl_seconds Loadbalancer#cookie_ttl_seconds}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#type Loadbalancer#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerStickySessions.__init__)
            check_type(argname="argument cookie_name", value=cookie_name, expected_type=type_hints["cookie_name"])
            check_type(argname="argument cookie_ttl_seconds", value=cookie_ttl_seconds, expected_type=type_hints["cookie_ttl_seconds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cookie_name is not None:
            self._values["cookie_name"] = cookie_name
        if cookie_ttl_seconds is not None:
            self._values["cookie_ttl_seconds"] = cookie_ttl_seconds
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def cookie_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#cookie_name Loadbalancer#cookie_name}.'''
        result = self._values.get("cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cookie_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#cookie_ttl_seconds Loadbalancer#cookie_ttl_seconds}.'''
        result = self._values.get("cookie_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/loadbalancer#type Loadbalancer#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerStickySessions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadbalancerStickySessionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.loadbalancer.LoadbalancerStickySessionsOutputReference",
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
            type_hints = typing.get_type_hints(LoadbalancerStickySessionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCookieName")
    def reset_cookie_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieName", []))

    @jsii.member(jsii_name="resetCookieTtlSeconds")
    def reset_cookie_ttl_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCookieTtlSeconds", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="cookieNameInput")
    def cookie_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cookieNameInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieTtlSecondsInput")
    def cookie_ttl_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cookieTtlSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="cookieName")
    def cookie_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cookieName"))

    @cookie_name.setter
    def cookie_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerStickySessionsOutputReference, "cookie_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieName", value)

    @builtins.property
    @jsii.member(jsii_name="cookieTtlSeconds")
    def cookie_ttl_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cookieTtlSeconds"))

    @cookie_ttl_seconds.setter
    def cookie_ttl_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerStickySessionsOutputReference, "cookie_ttl_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieTtlSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerStickySessionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LoadbalancerStickySessions]:
        return typing.cast(typing.Optional[LoadbalancerStickySessions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LoadbalancerStickySessions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerStickySessionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Loadbalancer",
    "LoadbalancerConfig",
    "LoadbalancerForwardingRule",
    "LoadbalancerForwardingRuleList",
    "LoadbalancerForwardingRuleOutputReference",
    "LoadbalancerHealthcheck",
    "LoadbalancerHealthcheckOutputReference",
    "LoadbalancerStickySessions",
    "LoadbalancerStickySessionsOutputReference",
]

publication.publish()
