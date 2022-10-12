'''
# `spotinst_health_check`

Refer to the Terraform Registory for docs: [`spotinst_health_check`](https://www.terraform.io/docs/providers/spotinst/r/health_check).
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


class HealthCheck(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.healthCheck.HealthCheck",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/spotinst/r/health_check spotinst_health_check}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        proxy_address: builtins.str,
        resource_id: builtins.str,
        check: typing.Optional[typing.Union["HealthCheckCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        proxy_port: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/spotinst/r/health_check spotinst_health_check} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param proxy_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#proxy_address HealthCheck#proxy_address}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#resource_id HealthCheck#resource_id}.
        :param check: check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#check HealthCheck#check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#id HealthCheck#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#name HealthCheck#name}.
        :param proxy_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#proxy_port HealthCheck#proxy_port}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HealthCheck.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HealthCheckConfig(
            proxy_address=proxy_address,
            resource_id=resource_id,
            check=check,
            id=id,
            name=name,
            proxy_port=proxy_port,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCheck")
    def put_check(
        self,
        *,
        healthy: jsii.Number,
        interval: jsii.Number,
        port: jsii.Number,
        protocol: builtins.str,
        unhealthy: jsii.Number,
        endpoint: typing.Optional[builtins.str] = None,
        end_point: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        time_out: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#healthy HealthCheck#healthy}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#interval HealthCheck#interval}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#port HealthCheck#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#protocol HealthCheck#protocol}.
        :param unhealthy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#unhealthy HealthCheck#unhealthy}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#endpoint HealthCheck#endpoint}.
        :param end_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#end_point HealthCheck#end_point}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#timeout HealthCheck#timeout}.
        :param time_out: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#time_out HealthCheck#time_out}.
        '''
        value = HealthCheckCheck(
            healthy=healthy,
            interval=interval,
            port=port,
            protocol=protocol,
            unhealthy=unhealthy,
            endpoint=endpoint,
            end_point=end_point,
            timeout=timeout,
            time_out=time_out,
        )

        return typing.cast(None, jsii.invoke(self, "putCheck", [value]))

    @jsii.member(jsii_name="resetCheck")
    def reset_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProxyPort")
    def reset_proxy_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyPort", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="check")
    def check(self) -> "HealthCheckCheckOutputReference":
        return typing.cast("HealthCheckCheckOutputReference", jsii.get(self, "check"))

    @builtins.property
    @jsii.member(jsii_name="checkInput")
    def check_input(self) -> typing.Optional["HealthCheckCheck"]:
        return typing.cast(typing.Optional["HealthCheckCheck"], jsii.get(self, "checkInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyAddressInput")
    def proxy_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyPortInput")
    def proxy_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "proxyPortInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheck, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheck, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="proxyAddress")
    def proxy_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyAddress"))

    @proxy_address.setter
    def proxy_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheck, "proxy_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyAddress", value)

    @builtins.property
    @jsii.member(jsii_name="proxyPort")
    def proxy_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "proxyPort"))

    @proxy_port.setter
    def proxy_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheck, "proxy_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyPort", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheck, "resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.healthCheck.HealthCheckCheck",
    jsii_struct_bases=[],
    name_mapping={
        "healthy": "healthy",
        "interval": "interval",
        "port": "port",
        "protocol": "protocol",
        "unhealthy": "unhealthy",
        "endpoint": "endpoint",
        "end_point": "endPoint",
        "timeout": "timeout",
        "time_out": "timeOut",
    },
)
class HealthCheckCheck:
    def __init__(
        self,
        *,
        healthy: jsii.Number,
        interval: jsii.Number,
        port: jsii.Number,
        protocol: builtins.str,
        unhealthy: jsii.Number,
        endpoint: typing.Optional[builtins.str] = None,
        end_point: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[jsii.Number] = None,
        time_out: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param healthy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#healthy HealthCheck#healthy}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#interval HealthCheck#interval}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#port HealthCheck#port}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#protocol HealthCheck#protocol}.
        :param unhealthy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#unhealthy HealthCheck#unhealthy}.
        :param endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#endpoint HealthCheck#endpoint}.
        :param end_point: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#end_point HealthCheck#end_point}.
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#timeout HealthCheck#timeout}.
        :param time_out: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#time_out HealthCheck#time_out}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HealthCheckCheck.__init__)
            check_type(argname="argument healthy", value=healthy, expected_type=type_hints["healthy"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument unhealthy", value=unhealthy, expected_type=type_hints["unhealthy"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument end_point", value=end_point, expected_type=type_hints["end_point"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument time_out", value=time_out, expected_type=type_hints["time_out"])
        self._values: typing.Dict[str, typing.Any] = {
            "healthy": healthy,
            "interval": interval,
            "port": port,
            "protocol": protocol,
            "unhealthy": unhealthy,
        }
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if end_point is not None:
            self._values["end_point"] = end_point
        if timeout is not None:
            self._values["timeout"] = timeout
        if time_out is not None:
            self._values["time_out"] = time_out

    @builtins.property
    def healthy(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#healthy HealthCheck#healthy}.'''
        result = self._values.get("healthy")
        assert result is not None, "Required property 'healthy' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#interval HealthCheck#interval}.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#port HealthCheck#port}.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#protocol HealthCheck#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def unhealthy(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#unhealthy HealthCheck#unhealthy}.'''
        result = self._values.get("unhealthy")
        assert result is not None, "Required property 'unhealthy' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#endpoint HealthCheck#endpoint}.'''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_point(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#end_point HealthCheck#end_point}.'''
        result = self._values.get("end_point")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#timeout HealthCheck#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def time_out(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#time_out HealthCheck#time_out}.'''
        result = self._values.get("time_out")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HealthCheckCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-spotinst.healthCheck.HealthCheckCheckOutputReference",
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
            type_hints = typing.get_type_hints(HealthCheckCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetEndPoint")
    def reset_end_point(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndPoint", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetTimeOut")
    def reset_time_out(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeOut", []))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endPointInput")
    def end_point_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endPointInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyInput")
    def healthy_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timeOutInput")
    def time_out_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeOutInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyInput")
    def unhealthy_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="endPoint")
    def end_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endPoint"))

    @end_point.setter
    def end_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "end_point").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endPoint", value)

    @builtins.property
    @jsii.member(jsii_name="healthy")
    def healthy(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthy"))

    @healthy.setter
    def healthy(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "healthy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthy", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="timeOut")
    def time_out(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeOut"))

    @time_out.setter
    def time_out(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "time_out").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeOut", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthy")
    def unhealthy(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthy"))

    @unhealthy.setter
    def unhealthy(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "unhealthy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HealthCheckCheck]:
        return typing.cast(typing.Optional[HealthCheckCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[HealthCheckCheck]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HealthCheckCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-spotinst.healthCheck.HealthCheckConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "proxy_address": "proxyAddress",
        "resource_id": "resourceId",
        "check": "check",
        "id": "id",
        "name": "name",
        "proxy_port": "proxyPort",
    },
)
class HealthCheckConfig(cdktf.TerraformMetaArguments):
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
        proxy_address: builtins.str,
        resource_id: builtins.str,
        check: typing.Optional[typing.Union[HealthCheckCheck, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        proxy_port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param proxy_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#proxy_address HealthCheck#proxy_address}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#resource_id HealthCheck#resource_id}.
        :param check: check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#check HealthCheck#check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#id HealthCheck#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#name HealthCheck#name}.
        :param proxy_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#proxy_port HealthCheck#proxy_port}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(check, dict):
            check = HealthCheckCheck(**check)
        if __debug__:
            type_hints = typing.get_type_hints(HealthCheckConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument proxy_address", value=proxy_address, expected_type=type_hints["proxy_address"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument check", value=check, expected_type=type_hints["check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument proxy_port", value=proxy_port, expected_type=type_hints["proxy_port"])
        self._values: typing.Dict[str, typing.Any] = {
            "proxy_address": proxy_address,
            "resource_id": resource_id,
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
        if check is not None:
            self._values["check"] = check
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if proxy_port is not None:
            self._values["proxy_port"] = proxy_port

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
    def proxy_address(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#proxy_address HealthCheck#proxy_address}.'''
        result = self._values.get("proxy_address")
        assert result is not None, "Required property 'proxy_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#resource_id HealthCheck#resource_id}.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def check(self) -> typing.Optional[HealthCheckCheck]:
        '''check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#check HealthCheck#check}
        '''
        result = self._values.get("check")
        return typing.cast(typing.Optional[HealthCheckCheck], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#id HealthCheck#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#name HealthCheck#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/spotinst/r/health_check#proxy_port HealthCheck#proxy_port}.'''
        result = self._values.get("proxy_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HealthCheck",
    "HealthCheckCheck",
    "HealthCheckCheckOutputReference",
    "HealthCheckConfig",
]

publication.publish()
