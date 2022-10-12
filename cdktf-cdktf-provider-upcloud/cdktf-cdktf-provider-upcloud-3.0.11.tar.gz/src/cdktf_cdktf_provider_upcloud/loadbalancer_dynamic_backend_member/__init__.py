'''
# `upcloud_loadbalancer_dynamic_backend_member`

Refer to the Terraform Registory for docs: [`upcloud_loadbalancer_dynamic_backend_member`](https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member).
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


class LoadbalancerDynamicBackendMember(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.loadbalancerDynamicBackendMember.LoadbalancerDynamicBackendMember",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member upcloud_loadbalancer_dynamic_backend_member}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: builtins.str,
        max_sessions: jsii.Number,
        name: builtins.str,
        weight: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member upcloud_loadbalancer_dynamic_backend_member} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: ID of the load balancer backend to which the member is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#backend LoadbalancerDynamicBackendMember#backend}
        :param max_sessions: Maximum number of sessions before queueing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#max_sessions LoadbalancerDynamicBackendMember#max_sessions}
        :param name: The name of the member must be unique within the load balancer backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#name LoadbalancerDynamicBackendMember#name}
        :param weight: Used to adjust the server's weight relative to other servers. All servers will receive a load proportional to their weight relative to the sum of all weights, so the higher the weight, the higher the load. A value of 0 means the server will not participate in load balancing but will still accept persistent connections. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#weight LoadbalancerDynamicBackendMember#weight}
        :param enabled: Indicates if the member is enabled. Disabled members are excluded from load balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#enabled LoadbalancerDynamicBackendMember#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#id LoadbalancerDynamicBackendMember#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip: Optional fallback IP address in case of failure on DNS resolving. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#ip LoadbalancerDynamicBackendMember#ip}
        :param port: Server port. Port is optional and can be specified in DNS SRV record. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#port LoadbalancerDynamicBackendMember#port}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerDynamicBackendMember.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = LoadbalancerDynamicBackendMemberConfig(
            backend=backend,
            max_sessions=max_sessions,
            name=name,
            weight=weight,
            enabled=enabled,
            id=id,
            ip=ip,
            port=port,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIp")
    def reset_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIp", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ipInput")
    def ip_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipInput"))

    @builtins.property
    @jsii.member(jsii_name="maxSessionsInput")
    def max_sessions_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSessionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ip")
    def ip(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ip"))

    @ip.setter
    def ip(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ip", value)

    @builtins.property
    @jsii.member(jsii_name="maxSessions")
    def max_sessions(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxSessions"))

    @max_sessions.setter
    def max_sessions(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "max_sessions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSessions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(LoadbalancerDynamicBackendMember, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.loadbalancerDynamicBackendMember.LoadbalancerDynamicBackendMemberConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend": "backend",
        "max_sessions": "maxSessions",
        "name": "name",
        "weight": "weight",
        "enabled": "enabled",
        "id": "id",
        "ip": "ip",
        "port": "port",
    },
)
class LoadbalancerDynamicBackendMemberConfig(cdktf.TerraformMetaArguments):
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
        backend: builtins.str,
        max_sessions: jsii.Number,
        name: builtins.str,
        weight: jsii.Number,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        ip: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend: ID of the load balancer backend to which the member is connected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#backend LoadbalancerDynamicBackendMember#backend}
        :param max_sessions: Maximum number of sessions before queueing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#max_sessions LoadbalancerDynamicBackendMember#max_sessions}
        :param name: The name of the member must be unique within the load balancer backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#name LoadbalancerDynamicBackendMember#name}
        :param weight: Used to adjust the server's weight relative to other servers. All servers will receive a load proportional to their weight relative to the sum of all weights, so the higher the weight, the higher the load. A value of 0 means the server will not participate in load balancing but will still accept persistent connections. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#weight LoadbalancerDynamicBackendMember#weight}
        :param enabled: Indicates if the member is enabled. Disabled members are excluded from load balancing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#enabled LoadbalancerDynamicBackendMember#enabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#id LoadbalancerDynamicBackendMember#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ip: Optional fallback IP address in case of failure on DNS resolving. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#ip LoadbalancerDynamicBackendMember#ip}
        :param port: Server port. Port is optional and can be specified in DNS SRV record. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#port LoadbalancerDynamicBackendMember#port}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(LoadbalancerDynamicBackendMemberConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument max_sessions", value=max_sessions, expected_type=type_hints["max_sessions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
            "max_sessions": max_sessions,
            "name": name,
            "weight": weight,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if ip is not None:
            self._values["ip"] = ip
        if port is not None:
            self._values["port"] = port

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
    def backend(self) -> builtins.str:
        '''ID of the load balancer backend to which the member is connected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#backend LoadbalancerDynamicBackendMember#backend}
        '''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_sessions(self) -> jsii.Number:
        '''Maximum number of sessions before queueing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#max_sessions LoadbalancerDynamicBackendMember#max_sessions}
        '''
        result = self._values.get("max_sessions")
        assert result is not None, "Required property 'max_sessions' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the member must be unique within the load balancer backend service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#name LoadbalancerDynamicBackendMember#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Used to adjust the server's weight relative to other servers.

        All servers will receive a load proportional to their weight relative to the sum of all weights, so the higher the weight, the higher the load.
        A value of 0 means the server will not participate in load balancing but will still accept persistent connections.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#weight LoadbalancerDynamicBackendMember#weight}
        '''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if the member is enabled. Disabled members are excluded from load balancing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#enabled LoadbalancerDynamicBackendMember#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#id LoadbalancerDynamicBackendMember#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip(self) -> typing.Optional[builtins.str]:
        '''Optional fallback IP address in case of failure on DNS resolving.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#ip LoadbalancerDynamicBackendMember#ip}
        '''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Server port. Port is optional and can be specified in DNS SRV record.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/loadbalancer_dynamic_backend_member#port LoadbalancerDynamicBackendMember#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadbalancerDynamicBackendMemberConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "LoadbalancerDynamicBackendMember",
    "LoadbalancerDynamicBackendMemberConfig",
]

publication.publish()
