'''
# `ionoscloud_networkloadbalancer_forwardingrule`

Refer to the Terraform Registory for docs: [`ionoscloud_networkloadbalancer_forwardingrule`](https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule).
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


class NetworkloadbalancerForwardingrule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingrule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule ionoscloud_networkloadbalancer_forwardingrule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        algorithm: builtins.str,
        datacenter_id: builtins.str,
        listener_ip: builtins.str,
        listener_port: jsii.Number,
        name: builtins.str,
        networkloadbalancer_id: builtins.str,
        protocol: builtins.str,
        targets: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkloadbalancerForwardingruleTargets", typing.Dict[str, typing.Any]]]],
        health_check: typing.Optional[typing.Union["NetworkloadbalancerForwardingruleHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["NetworkloadbalancerForwardingruleTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule ionoscloud_networkloadbalancer_forwardingrule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param algorithm: Algorithm for the balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#algorithm NetworkloadbalancerForwardingrule#algorithm}
        :param datacenter_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#datacenter_id NetworkloadbalancerForwardingrule#datacenter_id}.
        :param listener_ip: Listening IP. (inbound). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#listener_ip NetworkloadbalancerForwardingrule#listener_ip}
        :param listener_port: Listening port number. (inbound) (range: 1 to 65535). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#listener_port NetworkloadbalancerForwardingrule#listener_port}
        :param name: A name of that Network Load Balancer forwarding rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#name NetworkloadbalancerForwardingrule#name}
        :param networkloadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#networkloadbalancer_id NetworkloadbalancerForwardingrule#networkloadbalancer_id}.
        :param protocol: Protocol of the balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#protocol NetworkloadbalancerForwardingrule#protocol}
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#targets NetworkloadbalancerForwardingrule#targets}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#health_check NetworkloadbalancerForwardingrule#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#id NetworkloadbalancerForwardingrule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#timeouts NetworkloadbalancerForwardingrule#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingrule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NetworkloadbalancerForwardingruleConfig(
            algorithm=algorithm,
            datacenter_id=datacenter_id,
            listener_ip=listener_ip,
            listener_port=listener_port,
            name=name,
            networkloadbalancer_id=networkloadbalancer_id,
            protocol=protocol,
            targets=targets,
            health_check=health_check,
            id=id,
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

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        client_timeout: typing.Optional[jsii.Number] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        retries: typing.Optional[jsii.Number] = None,
        target_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_timeout: ClientTimeout is expressed in milliseconds. This inactivity timeout applies when the client is expected to acknowledge or send data. If unset the default of 50 seconds will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#client_timeout NetworkloadbalancerForwardingrule#client_timeout}
        :param connect_timeout: It specifies the maximum time (in milliseconds) to wait for a connection attempt to a target VM to succeed. If unset, the default of 5 seconds will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#connect_timeout NetworkloadbalancerForwardingrule#connect_timeout}
        :param retries: Retries specifies the number of retries to perform on a target VM after a connection failure. If unset, the default value of 3 will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#retries NetworkloadbalancerForwardingrule#retries}
        :param target_timeout: TargetTimeout specifies the maximum inactivity time (in milliseconds) on the target VM side. If unset, the default of 50 seconds will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#target_timeout NetworkloadbalancerForwardingrule#target_timeout}
        '''
        value = NetworkloadbalancerForwardingruleHealthCheck(
            client_timeout=client_timeout,
            connect_timeout=connect_timeout,
            retries=retries,
            target_timeout=target_timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putTargets")
    def put_targets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkloadbalancerForwardingruleTargets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingrule.put_targets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargets", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#create NetworkloadbalancerForwardingrule#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#default NetworkloadbalancerForwardingrule#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#delete NetworkloadbalancerForwardingrule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#update NetworkloadbalancerForwardingrule#update}.
        '''
        value = NetworkloadbalancerForwardingruleTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="healthCheck")
    def health_check(
        self,
    ) -> "NetworkloadbalancerForwardingruleHealthCheckOutputReference":
        return typing.cast("NetworkloadbalancerForwardingruleHealthCheckOutputReference", jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(self) -> "NetworkloadbalancerForwardingruleTargetsList":
        return typing.cast("NetworkloadbalancerForwardingruleTargetsList", jsii.get(self, "targets"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "NetworkloadbalancerForwardingruleTimeoutsOutputReference":
        return typing.cast("NetworkloadbalancerForwardingruleTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(
        self,
    ) -> typing.Optional["NetworkloadbalancerForwardingruleHealthCheck"]:
        return typing.cast(typing.Optional["NetworkloadbalancerForwardingruleHealthCheck"], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerIpInput")
    def listener_ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "listenerIpInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerPortInput")
    def listener_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "listenerPortInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkloadbalancerIdInput")
    def networkloadbalancer_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkloadbalancerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="targetsInput")
    def targets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkloadbalancerForwardingruleTargets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["NetworkloadbalancerForwardingruleTargets"]]], jsii.get(self, "targetsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["NetworkloadbalancerForwardingruleTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["NetworkloadbalancerForwardingruleTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "datacenter_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="listenerIp")
    def listener_ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "listenerIp"))

    @listener_ip.setter
    def listener_ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "listener_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerIp", value)

    @builtins.property
    @jsii.member(jsii_name="listenerPort")
    def listener_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "listenerPort"))

    @listener_port.setter
    def listener_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "listener_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerPort", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkloadbalancerId")
    def networkloadbalancer_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkloadbalancerId"))

    @networkloadbalancer_id.setter
    def networkloadbalancer_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "networkloadbalancer_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkloadbalancerId", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingrule, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "algorithm": "algorithm",
        "datacenter_id": "datacenterId",
        "listener_ip": "listenerIp",
        "listener_port": "listenerPort",
        "name": "name",
        "networkloadbalancer_id": "networkloadbalancerId",
        "protocol": "protocol",
        "targets": "targets",
        "health_check": "healthCheck",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class NetworkloadbalancerForwardingruleConfig(cdktf.TerraformMetaArguments):
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
        algorithm: builtins.str,
        datacenter_id: builtins.str,
        listener_ip: builtins.str,
        listener_port: jsii.Number,
        name: builtins.str,
        networkloadbalancer_id: builtins.str,
        protocol: builtins.str,
        targets: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["NetworkloadbalancerForwardingruleTargets", typing.Dict[str, typing.Any]]]],
        health_check: typing.Optional[typing.Union["NetworkloadbalancerForwardingruleHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["NetworkloadbalancerForwardingruleTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param algorithm: Algorithm for the balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#algorithm NetworkloadbalancerForwardingrule#algorithm}
        :param datacenter_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#datacenter_id NetworkloadbalancerForwardingrule#datacenter_id}.
        :param listener_ip: Listening IP. (inbound). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#listener_ip NetworkloadbalancerForwardingrule#listener_ip}
        :param listener_port: Listening port number. (inbound) (range: 1 to 65535). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#listener_port NetworkloadbalancerForwardingrule#listener_port}
        :param name: A name of that Network Load Balancer forwarding rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#name NetworkloadbalancerForwardingrule#name}
        :param networkloadbalancer_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#networkloadbalancer_id NetworkloadbalancerForwardingrule#networkloadbalancer_id}.
        :param protocol: Protocol of the balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#protocol NetworkloadbalancerForwardingrule#protocol}
        :param targets: targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#targets NetworkloadbalancerForwardingrule#targets}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#health_check NetworkloadbalancerForwardingrule#health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#id NetworkloadbalancerForwardingrule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#timeouts NetworkloadbalancerForwardingrule#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(health_check, dict):
            health_check = NetworkloadbalancerForwardingruleHealthCheck(**health_check)
        if isinstance(timeouts, dict):
            timeouts = NetworkloadbalancerForwardingruleTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument listener_ip", value=listener_ip, expected_type=type_hints["listener_ip"])
            check_type(argname="argument listener_port", value=listener_port, expected_type=type_hints["listener_port"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument networkloadbalancer_id", value=networkloadbalancer_id, expected_type=type_hints["networkloadbalancer_id"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "algorithm": algorithm,
            "datacenter_id": datacenter_id,
            "listener_ip": listener_ip,
            "listener_port": listener_port,
            "name": name,
            "networkloadbalancer_id": networkloadbalancer_id,
            "protocol": protocol,
            "targets": targets,
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
        if health_check is not None:
            self._values["health_check"] = health_check
        if id is not None:
            self._values["id"] = id
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
    def algorithm(self) -> builtins.str:
        '''Algorithm for the balancing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#algorithm NetworkloadbalancerForwardingrule#algorithm}
        '''
        result = self._values.get("algorithm")
        assert result is not None, "Required property 'algorithm' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datacenter_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#datacenter_id NetworkloadbalancerForwardingrule#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listener_ip(self) -> builtins.str:
        '''Listening IP. (inbound).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#listener_ip NetworkloadbalancerForwardingrule#listener_ip}
        '''
        result = self._values.get("listener_ip")
        assert result is not None, "Required property 'listener_ip' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def listener_port(self) -> jsii.Number:
        '''Listening port number. (inbound) (range: 1 to 65535).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#listener_port NetworkloadbalancerForwardingrule#listener_port}
        '''
        result = self._values.get("listener_port")
        assert result is not None, "Required property 'listener_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name of that Network Load Balancer forwarding rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#name NetworkloadbalancerForwardingrule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def networkloadbalancer_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#networkloadbalancer_id NetworkloadbalancerForwardingrule#networkloadbalancer_id}.'''
        result = self._values.get("networkloadbalancer_id")
        assert result is not None, "Required property 'networkloadbalancer_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Protocol of the balancing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#protocol NetworkloadbalancerForwardingrule#protocol}
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["NetworkloadbalancerForwardingruleTargets"]]:
        '''targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#targets NetworkloadbalancerForwardingrule#targets}
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["NetworkloadbalancerForwardingruleTargets"]], result)

    @builtins.property
    def health_check(
        self,
    ) -> typing.Optional["NetworkloadbalancerForwardingruleHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#health_check NetworkloadbalancerForwardingrule#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["NetworkloadbalancerForwardingruleHealthCheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#id NetworkloadbalancerForwardingrule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["NetworkloadbalancerForwardingruleTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#timeouts NetworkloadbalancerForwardingrule#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["NetworkloadbalancerForwardingruleTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkloadbalancerForwardingruleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "client_timeout": "clientTimeout",
        "connect_timeout": "connectTimeout",
        "retries": "retries",
        "target_timeout": "targetTimeout",
    },
)
class NetworkloadbalancerForwardingruleHealthCheck:
    def __init__(
        self,
        *,
        client_timeout: typing.Optional[jsii.Number] = None,
        connect_timeout: typing.Optional[jsii.Number] = None,
        retries: typing.Optional[jsii.Number] = None,
        target_timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param client_timeout: ClientTimeout is expressed in milliseconds. This inactivity timeout applies when the client is expected to acknowledge or send data. If unset the default of 50 seconds will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#client_timeout NetworkloadbalancerForwardingrule#client_timeout}
        :param connect_timeout: It specifies the maximum time (in milliseconds) to wait for a connection attempt to a target VM to succeed. If unset, the default of 5 seconds will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#connect_timeout NetworkloadbalancerForwardingrule#connect_timeout}
        :param retries: Retries specifies the number of retries to perform on a target VM after a connection failure. If unset, the default value of 3 will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#retries NetworkloadbalancerForwardingrule#retries}
        :param target_timeout: TargetTimeout specifies the maximum inactivity time (in milliseconds) on the target VM side. If unset, the default of 50 seconds will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#target_timeout NetworkloadbalancerForwardingrule#target_timeout}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleHealthCheck.__init__)
            check_type(argname="argument client_timeout", value=client_timeout, expected_type=type_hints["client_timeout"])
            check_type(argname="argument connect_timeout", value=connect_timeout, expected_type=type_hints["connect_timeout"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
            check_type(argname="argument target_timeout", value=target_timeout, expected_type=type_hints["target_timeout"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_timeout is not None:
            self._values["client_timeout"] = client_timeout
        if connect_timeout is not None:
            self._values["connect_timeout"] = connect_timeout
        if retries is not None:
            self._values["retries"] = retries
        if target_timeout is not None:
            self._values["target_timeout"] = target_timeout

    @builtins.property
    def client_timeout(self) -> typing.Optional[jsii.Number]:
        '''ClientTimeout is expressed in milliseconds.

        This inactivity timeout applies when the client is expected to acknowledge or send data. If unset the default of 50 seconds will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#client_timeout NetworkloadbalancerForwardingrule#client_timeout}
        '''
        result = self._values.get("client_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connect_timeout(self) -> typing.Optional[jsii.Number]:
        '''It specifies the maximum time (in milliseconds) to wait for a connection attempt to a target VM to succeed.

        If unset, the default of 5 seconds will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#connect_timeout NetworkloadbalancerForwardingrule#connect_timeout}
        '''
        result = self._values.get("connect_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''Retries specifies the number of retries to perform on a target VM after a connection failure.

        If unset, the default value of 3 will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#retries NetworkloadbalancerForwardingrule#retries}
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_timeout(self) -> typing.Optional[jsii.Number]:
        '''TargetTimeout specifies the maximum inactivity time (in milliseconds) on the target VM side.

        If unset, the default of 50 seconds will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#target_timeout NetworkloadbalancerForwardingrule#target_timeout}
        '''
        result = self._values.get("target_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkloadbalancerForwardingruleHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkloadbalancerForwardingruleHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetClientTimeout")
    def reset_client_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTimeout", []))

    @jsii.member(jsii_name="resetConnectTimeout")
    def reset_connect_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectTimeout", []))

    @jsii.member(jsii_name="resetRetries")
    def reset_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetries", []))

    @jsii.member(jsii_name="resetTargetTimeout")
    def reset_target_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="clientTimeoutInput")
    def client_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="connectTimeoutInput")
    def connect_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connectTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="retriesInput")
    def retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retriesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTimeoutInput")
    def target_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTimeout")
    def client_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientTimeout"))

    @client_timeout.setter
    def client_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleHealthCheckOutputReference, "client_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="connectTimeout")
    def connect_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connectTimeout"))

    @connect_timeout.setter
    def connect_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleHealthCheckOutputReference, "connect_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleHealthCheckOutputReference, "retries").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value)

    @builtins.property
    @jsii.member(jsii_name="targetTimeout")
    def target_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetTimeout"))

    @target_timeout.setter
    def target_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleHealthCheckOutputReference, "target_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkloadbalancerForwardingruleHealthCheck]:
        return typing.cast(typing.Optional[NetworkloadbalancerForwardingruleHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkloadbalancerForwardingruleHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleTargets",
    jsii_struct_bases=[],
    name_mapping={
        "ip": "ip",
        "port": "port",
        "weight": "weight",
        "health_check": "healthCheck",
    },
)
class NetworkloadbalancerForwardingruleTargets:
    def __init__(
        self,
        *,
        ip: builtins.str,
        port: jsii.Number,
        weight: jsii.Number,
        health_check: typing.Optional[typing.Union["NetworkloadbalancerForwardingruleTargetsHealthCheck", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ip: IP of a balanced target VM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#ip NetworkloadbalancerForwardingrule#ip}
        :param port: Port of the balanced target service. (range: 1 to 65535). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#port NetworkloadbalancerForwardingrule#port}
        :param weight: Weight parameter is used to adjust the target VM's weight relative to other target VMs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#weight NetworkloadbalancerForwardingrule#weight}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#health_check NetworkloadbalancerForwardingrule#health_check}
        '''
        if isinstance(health_check, dict):
            health_check = NetworkloadbalancerForwardingruleTargetsHealthCheck(**health_check)
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTargets.__init__)
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
        self._values: typing.Dict[str, typing.Any] = {
            "ip": ip,
            "port": port,
            "weight": weight,
        }
        if health_check is not None:
            self._values["health_check"] = health_check

    @builtins.property
    def ip(self) -> builtins.str:
        '''IP of a balanced target VM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#ip NetworkloadbalancerForwardingrule#ip}
        '''
        result = self._values.get("ip")
        assert result is not None, "Required property 'ip' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Port of the balanced target service. (range: 1 to 65535).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#port NetworkloadbalancerForwardingrule#port}
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Weight parameter is used to adjust the target VM's weight relative to other target VMs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#weight NetworkloadbalancerForwardingrule#weight}
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def health_check(
        self,
    ) -> typing.Optional["NetworkloadbalancerForwardingruleTargetsHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#health_check NetworkloadbalancerForwardingrule#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["NetworkloadbalancerForwardingruleTargetsHealthCheck"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkloadbalancerForwardingruleTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleTargetsHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "check": "check",
        "check_interval": "checkInterval",
        "maintenance": "maintenance",
    },
)
class NetworkloadbalancerForwardingruleTargetsHealthCheck:
    def __init__(
        self,
        *,
        check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_interval: typing.Optional[jsii.Number] = None,
        maintenance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param check: Check specifies whether the target VM's health is checked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#check NetworkloadbalancerForwardingrule#check}
        :param check_interval: CheckInterval determines the duration (in milliseconds) between consecutive health checks. If unspecified a default of 2000 ms is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#check_interval NetworkloadbalancerForwardingrule#check_interval}
        :param maintenance: Maintenance specifies if a target VM should be marked as down, even if it is not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#maintenance NetworkloadbalancerForwardingrule#maintenance}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTargetsHealthCheck.__init__)
            check_type(argname="argument check", value=check, expected_type=type_hints["check"])
            check_type(argname="argument check_interval", value=check_interval, expected_type=type_hints["check_interval"])
            check_type(argname="argument maintenance", value=maintenance, expected_type=type_hints["maintenance"])
        self._values: typing.Dict[str, typing.Any] = {}
        if check is not None:
            self._values["check"] = check
        if check_interval is not None:
            self._values["check_interval"] = check_interval
        if maintenance is not None:
            self._values["maintenance"] = maintenance

    @builtins.property
    def check(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Check specifies whether the target VM's health is checked.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#check NetworkloadbalancerForwardingrule#check}
        '''
        result = self._values.get("check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def check_interval(self) -> typing.Optional[jsii.Number]:
        '''CheckInterval determines the duration (in milliseconds) between consecutive health checks. If unspecified a default of 2000 ms is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#check_interval NetworkloadbalancerForwardingrule#check_interval}
        '''
        result = self._values.get("check_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maintenance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Maintenance specifies if a target VM should be marked as down, even if it is not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#maintenance NetworkloadbalancerForwardingrule#maintenance}
        '''
        result = self._values.get("maintenance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkloadbalancerForwardingruleTargetsHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCheck")
    def reset_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheck", []))

    @jsii.member(jsii_name="resetCheckInterval")
    def reset_check_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckInterval", []))

    @jsii.member(jsii_name="resetMaintenance")
    def reset_maintenance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenance", []))

    @builtins.property
    @jsii.member(jsii_name="checkInput")
    def check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "checkInput"))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalInput")
    def check_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "checkIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceInput")
    def maintenance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "maintenanceInput"))

    @builtins.property
    @jsii.member(jsii_name="check")
    def check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "check"))

    @check.setter
    def check(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference, "check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "check", value)

    @builtins.property
    @jsii.member(jsii_name="checkInterval")
    def check_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "checkInterval"))

    @check_interval.setter
    def check_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference, "check_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkInterval", value)

    @builtins.property
    @jsii.member(jsii_name="maintenance")
    def maintenance(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "maintenance"))

    @maintenance.setter
    def maintenance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference, "maintenance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenance", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[NetworkloadbalancerForwardingruleTargetsHealthCheck]:
        return typing.cast(typing.Optional[NetworkloadbalancerForwardingruleTargetsHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[NetworkloadbalancerForwardingruleTargetsHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkloadbalancerForwardingruleTargetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleTargetsList",
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
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTargetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NetworkloadbalancerForwardingruleTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTargetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NetworkloadbalancerForwardingruleTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkloadbalancerForwardingruleTargets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkloadbalancerForwardingruleTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[NetworkloadbalancerForwardingruleTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NetworkloadbalancerForwardingruleTargetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleTargetsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTargetsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        check_interval: typing.Optional[jsii.Number] = None,
        maintenance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param check: Check specifies whether the target VM's health is checked. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#check NetworkloadbalancerForwardingrule#check}
        :param check_interval: CheckInterval determines the duration (in milliseconds) between consecutive health checks. If unspecified a default of 2000 ms is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#check_interval NetworkloadbalancerForwardingrule#check_interval}
        :param maintenance: Maintenance specifies if a target VM should be marked as down, even if it is not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#maintenance NetworkloadbalancerForwardingrule#maintenance}
        '''
        value = NetworkloadbalancerForwardingruleTargetsHealthCheck(
            check=check, check_interval=check_interval, maintenance=maintenance
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(
        self,
    ) -> NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference:
        return typing.cast(NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference, jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(
        self,
    ) -> typing.Optional[NetworkloadbalancerForwardingruleTargetsHealthCheck]:
        return typing.cast(typing.Optional[NetworkloadbalancerForwardingruleTargetsHealthCheck], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsOutputReference, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkloadbalancerForwardingruleTargets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkloadbalancerForwardingruleTargets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkloadbalancerForwardingruleTargets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTargetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class NetworkloadbalancerForwardingruleTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#create NetworkloadbalancerForwardingrule#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#default NetworkloadbalancerForwardingrule#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#delete NetworkloadbalancerForwardingrule#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#update NetworkloadbalancerForwardingrule#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#create NetworkloadbalancerForwardingrule#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#default NetworkloadbalancerForwardingrule#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#delete NetworkloadbalancerForwardingrule#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/networkloadbalancer_forwardingrule#update NetworkloadbalancerForwardingrule#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkloadbalancerForwardingruleTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NetworkloadbalancerForwardingruleTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.networkloadbalancerForwardingrule.NetworkloadbalancerForwardingruleTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(NetworkloadbalancerForwardingruleTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

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
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

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
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NetworkloadbalancerForwardingruleTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NetworkloadbalancerForwardingruleTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NetworkloadbalancerForwardingruleTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(NetworkloadbalancerForwardingruleTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NetworkloadbalancerForwardingrule",
    "NetworkloadbalancerForwardingruleConfig",
    "NetworkloadbalancerForwardingruleHealthCheck",
    "NetworkloadbalancerForwardingruleHealthCheckOutputReference",
    "NetworkloadbalancerForwardingruleTargets",
    "NetworkloadbalancerForwardingruleTargetsHealthCheck",
    "NetworkloadbalancerForwardingruleTargetsHealthCheckOutputReference",
    "NetworkloadbalancerForwardingruleTargetsList",
    "NetworkloadbalancerForwardingruleTargetsOutputReference",
    "NetworkloadbalancerForwardingruleTimeouts",
    "NetworkloadbalancerForwardingruleTimeoutsOutputReference",
]

publication.publish()
