'''
# `google_compute_health_check`

Refer to the Terraform Registory for docs: [`google_compute_health_check`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check).
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


class GoogleComputeHealthCheck(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheck",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check google_compute_health_check}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        check_interval_sec: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        grpc_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckGrpcHealthCheck", typing.Dict[str, typing.Any]]] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        http2_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckHttp2HealthCheck", typing.Dict[str, typing.Any]]] = None,
        http_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckHttpHealthCheck", typing.Dict[str, typing.Any]]] = None,
        https_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckHttpsHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeHealthCheckLogConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        ssl_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckSslHealthCheck", typing.Dict[str, typing.Any]]] = None,
        tcp_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckTcpHealthCheck", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeHealthCheckTimeouts", typing.Dict[str, typing.Any]]] = None,
        timeout_sec: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check google_compute_health_check} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#name GoogleComputeHealthCheck#name}
        :param check_interval_sec: How often (in seconds) to send a health check. The default value is 5 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#check_interval_sec GoogleComputeHealthCheck#check_interval_sec}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#description GoogleComputeHealthCheck#description}
        :param grpc_health_check: grpc_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#grpc_health_check GoogleComputeHealthCheck#grpc_health_check}
        :param healthy_threshold: A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#healthy_threshold GoogleComputeHealthCheck#healthy_threshold}
        :param http2_health_check: http2_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#http2_health_check GoogleComputeHealthCheck#http2_health_check}
        :param http_health_check: http_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#http_health_check GoogleComputeHealthCheck#http_health_check}
        :param https_health_check: https_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#https_health_check GoogleComputeHealthCheck#https_health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#id GoogleComputeHealthCheck#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#log_config GoogleComputeHealthCheck#log_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#project GoogleComputeHealthCheck#project}.
        :param ssl_health_check: ssl_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#ssl_health_check GoogleComputeHealthCheck#ssl_health_check}
        :param tcp_health_check: tcp_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#tcp_health_check GoogleComputeHealthCheck#tcp_health_check}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#timeouts GoogleComputeHealthCheck#timeouts}
        :param timeout_sec: How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#timeout_sec GoogleComputeHealthCheck#timeout_sec}
        :param unhealthy_threshold: A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#unhealthy_threshold GoogleComputeHealthCheck#unhealthy_threshold}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheck.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeHealthCheckConfig(
            name=name,
            check_interval_sec=check_interval_sec,
            description=description,
            grpc_health_check=grpc_health_check,
            healthy_threshold=healthy_threshold,
            http2_health_check=http2_health_check,
            http_health_check=http_health_check,
            https_health_check=https_health_check,
            id=id,
            log_config=log_config,
            project=project,
            ssl_health_check=ssl_health_check,
            tcp_health_check=tcp_health_check,
            timeouts=timeouts,
            timeout_sec=timeout_sec,
            unhealthy_threshold=unhealthy_threshold,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putGrpcHealthCheck")
    def put_grpc_health_check(
        self,
        *,
        grpc_service_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param grpc_service_name: The gRPC service name for the health check. The value of grpcServiceName has the following meanings by convention: - Empty serviceName means the overall status of all services at the backend. - Non-empty serviceName means the health of that gRPC service, as defined by the owner of the service. The grpcServiceName can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#grpc_service_name GoogleComputeHealthCheck#grpc_service_name}
        :param port: The port number for the health check request. Must be specified if portName and portSpecification are not set or if port_specification is USE_FIXED_PORT. Valid values are 1 through 65535. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, gRPC health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        value = GoogleComputeHealthCheckGrpcHealthCheck(
            grpc_service_name=grpc_service_name,
            port=port,
            port_name=port_name,
            port_specification=port_specification,
        )

        return typing.cast(None, jsii.invoke(self, "putGrpcHealthCheck", [value]))

    @jsii.member(jsii_name="putHttp2HealthCheck")
    def put_http2_health_check(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request_path: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The value of the host header in the HTTP2 health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        :param port: The TCP port number for the HTTP2 health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, HTTP2 health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request_path: The request path of the HTTP2 health check request. The default value is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        value = GoogleComputeHealthCheckHttp2HealthCheck(
            host=host,
            port=port,
            port_name=port_name,
            port_specification=port_specification,
            proxy_header=proxy_header,
            request_path=request_path,
            response=response,
        )

        return typing.cast(None, jsii.invoke(self, "putHttp2HealthCheck", [value]))

    @jsii.member(jsii_name="putHttpHealthCheck")
    def put_http_health_check(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request_path: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        :param port: The TCP port number for the HTTP health check request. The default value is 80. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, HTTP health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request_path: The request path of the HTTP health check request. The default value is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        value = GoogleComputeHealthCheckHttpHealthCheck(
            host=host,
            port=port,
            port_name=port_name,
            port_specification=port_specification,
            proxy_header=proxy_header,
            request_path=request_path,
            response=response,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpHealthCheck", [value]))

    @jsii.member(jsii_name="putHttpsHealthCheck")
    def put_https_health_check(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request_path: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The value of the host header in the HTTPS health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        :param port: The TCP port number for the HTTPS health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, HTTPS health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request_path: The request path of the HTTPS health check request. The default value is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        value = GoogleComputeHealthCheckHttpsHealthCheck(
            host=host,
            port=port,
            port_name=port_name,
            port_specification=port_specification,
            proxy_header=proxy_header,
            request_path=request_path,
            response=response,
        )

        return typing.cast(None, jsii.invoke(self, "putHttpsHealthCheck", [value]))

    @jsii.member(jsii_name="putLogConfig")
    def put_log_config(
        self,
        *,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable: Indicates whether or not to export logs. This is false by default, which means no health check logging will be done. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#enable GoogleComputeHealthCheck#enable}
        '''
        value = GoogleComputeHealthCheckLogConfig(enable=enable)

        return typing.cast(None, jsii.invoke(self, "putLogConfig", [value]))

    @jsii.member(jsii_name="putSslHealthCheck")
    def put_ssl_health_check(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: The TCP port number for the SSL health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, SSL health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request: The application data to send once the SSL connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request GoogleComputeHealthCheck#request}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        value = GoogleComputeHealthCheckSslHealthCheck(
            port=port,
            port_name=port_name,
            port_specification=port_specification,
            proxy_header=proxy_header,
            request=request,
            response=response,
        )

        return typing.cast(None, jsii.invoke(self, "putSslHealthCheck", [value]))

    @jsii.member(jsii_name="putTcpHealthCheck")
    def put_tcp_health_check(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: The TCP port number for the TCP health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, TCP health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request: The application data to send once the TCP connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request GoogleComputeHealthCheck#request}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        value = GoogleComputeHealthCheckTcpHealthCheck(
            port=port,
            port_name=port_name,
            port_specification=port_specification,
            proxy_header=proxy_header,
            request=request,
            response=response,
        )

        return typing.cast(None, jsii.invoke(self, "putTcpHealthCheck", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#create GoogleComputeHealthCheck#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#delete GoogleComputeHealthCheck#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#update GoogleComputeHealthCheck#update}.
        '''
        value = GoogleComputeHealthCheckTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCheckIntervalSec")
    def reset_check_interval_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheckIntervalSec", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetGrpcHealthCheck")
    def reset_grpc_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcHealthCheck", []))

    @jsii.member(jsii_name="resetHealthyThreshold")
    def reset_healthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthyThreshold", []))

    @jsii.member(jsii_name="resetHttp2HealthCheck")
    def reset_http2_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp2HealthCheck", []))

    @jsii.member(jsii_name="resetHttpHealthCheck")
    def reset_http_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHealthCheck", []))

    @jsii.member(jsii_name="resetHttpsHealthCheck")
    def reset_https_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpsHealthCheck", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogConfig")
    def reset_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSslHealthCheck")
    def reset_ssl_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslHealthCheck", []))

    @jsii.member(jsii_name="resetTcpHealthCheck")
    def reset_tcp_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcpHealthCheck", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTimeoutSec")
    def reset_timeout_sec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSec", []))

    @jsii.member(jsii_name="resetUnhealthyThreshold")
    def reset_unhealthy_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnhealthyThreshold", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="grpcHealthCheck")
    def grpc_health_check(
        self,
    ) -> "GoogleComputeHealthCheckGrpcHealthCheckOutputReference":
        return typing.cast("GoogleComputeHealthCheckGrpcHealthCheckOutputReference", jsii.get(self, "grpcHealthCheck"))

    @builtins.property
    @jsii.member(jsii_name="http2HealthCheck")
    def http2_health_check(
        self,
    ) -> "GoogleComputeHealthCheckHttp2HealthCheckOutputReference":
        return typing.cast("GoogleComputeHealthCheckHttp2HealthCheckOutputReference", jsii.get(self, "http2HealthCheck"))

    @builtins.property
    @jsii.member(jsii_name="httpHealthCheck")
    def http_health_check(
        self,
    ) -> "GoogleComputeHealthCheckHttpHealthCheckOutputReference":
        return typing.cast("GoogleComputeHealthCheckHttpHealthCheckOutputReference", jsii.get(self, "httpHealthCheck"))

    @builtins.property
    @jsii.member(jsii_name="httpsHealthCheck")
    def https_health_check(
        self,
    ) -> "GoogleComputeHealthCheckHttpsHealthCheckOutputReference":
        return typing.cast("GoogleComputeHealthCheckHttpsHealthCheckOutputReference", jsii.get(self, "httpsHealthCheck"))

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(self) -> "GoogleComputeHealthCheckLogConfigOutputReference":
        return typing.cast("GoogleComputeHealthCheckLogConfigOutputReference", jsii.get(self, "logConfig"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="sslHealthCheck")
    def ssl_health_check(
        self,
    ) -> "GoogleComputeHealthCheckSslHealthCheckOutputReference":
        return typing.cast("GoogleComputeHealthCheckSslHealthCheckOutputReference", jsii.get(self, "sslHealthCheck"))

    @builtins.property
    @jsii.member(jsii_name="tcpHealthCheck")
    def tcp_health_check(
        self,
    ) -> "GoogleComputeHealthCheckTcpHealthCheckOutputReference":
        return typing.cast("GoogleComputeHealthCheckTcpHealthCheckOutputReference", jsii.get(self, "tcpHealthCheck"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeHealthCheckTimeoutsOutputReference":
        return typing.cast("GoogleComputeHealthCheckTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalSecInput")
    def check_interval_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "checkIntervalSecInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="grpcHealthCheckInput")
    def grpc_health_check_input(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckGrpcHealthCheck"]:
        return typing.cast(typing.Optional["GoogleComputeHealthCheckGrpcHealthCheck"], jsii.get(self, "grpcHealthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="healthyThresholdInput")
    def healthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "healthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="http2HealthCheckInput")
    def http2_health_check_input(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckHttp2HealthCheck"]:
        return typing.cast(typing.Optional["GoogleComputeHealthCheckHttp2HealthCheck"], jsii.get(self, "http2HealthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHealthCheckInput")
    def http_health_check_input(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckHttpHealthCheck"]:
        return typing.cast(typing.Optional["GoogleComputeHealthCheckHttpHealthCheck"], jsii.get(self, "httpHealthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="httpsHealthCheckInput")
    def https_health_check_input(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckHttpsHealthCheck"]:
        return typing.cast(typing.Optional["GoogleComputeHealthCheckHttpsHealthCheck"], jsii.get(self, "httpsHealthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigInput")
    def log_config_input(self) -> typing.Optional["GoogleComputeHealthCheckLogConfig"]:
        return typing.cast(typing.Optional["GoogleComputeHealthCheckLogConfig"], jsii.get(self, "logConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="sslHealthCheckInput")
    def ssl_health_check_input(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckSslHealthCheck"]:
        return typing.cast(typing.Optional["GoogleComputeHealthCheckSslHealthCheck"], jsii.get(self, "sslHealthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpHealthCheckInput")
    def tcp_health_check_input(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckTcpHealthCheck"]:
        return typing.cast(typing.Optional["GoogleComputeHealthCheckTcpHealthCheck"], jsii.get(self, "tcpHealthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecInput")
    def timeout_sec_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeHealthCheckTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeHealthCheckTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="unhealthyThresholdInput")
    def unhealthy_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "unhealthyThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="checkIntervalSec")
    def check_interval_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "checkIntervalSec"))

    @check_interval_sec.setter
    def check_interval_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "check_interval_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "checkIntervalSec", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="healthyThreshold")
    def healthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "healthyThreshold"))

    @healthy_threshold.setter
    def healthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "healthy_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthyThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSec")
    def timeout_sec(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSec"))

    @timeout_sec.setter
    def timeout_sec(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "timeout_sec").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSec", value)

    @builtins.property
    @jsii.member(jsii_name="unhealthyThreshold")
    def unhealthy_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "unhealthyThreshold"))

    @unhealthy_threshold.setter
    def unhealthy_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheck, "unhealthy_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unhealthyThreshold", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckConfig",
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
        "check_interval_sec": "checkIntervalSec",
        "description": "description",
        "grpc_health_check": "grpcHealthCheck",
        "healthy_threshold": "healthyThreshold",
        "http2_health_check": "http2HealthCheck",
        "http_health_check": "httpHealthCheck",
        "https_health_check": "httpsHealthCheck",
        "id": "id",
        "log_config": "logConfig",
        "project": "project",
        "ssl_health_check": "sslHealthCheck",
        "tcp_health_check": "tcpHealthCheck",
        "timeouts": "timeouts",
        "timeout_sec": "timeoutSec",
        "unhealthy_threshold": "unhealthyThreshold",
    },
)
class GoogleComputeHealthCheckConfig(cdktf.TerraformMetaArguments):
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
        check_interval_sec: typing.Optional[jsii.Number] = None,
        description: typing.Optional[builtins.str] = None,
        grpc_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckGrpcHealthCheck", typing.Dict[str, typing.Any]]] = None,
        healthy_threshold: typing.Optional[jsii.Number] = None,
        http2_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckHttp2HealthCheck", typing.Dict[str, typing.Any]]] = None,
        http_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckHttpHealthCheck", typing.Dict[str, typing.Any]]] = None,
        https_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckHttpsHealthCheck", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeHealthCheckLogConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        ssl_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckSslHealthCheck", typing.Dict[str, typing.Any]]] = None,
        tcp_health_check: typing.Optional[typing.Union["GoogleComputeHealthCheckTcpHealthCheck", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeHealthCheckTimeouts", typing.Dict[str, typing.Any]]] = None,
        timeout_sec: typing.Optional[jsii.Number] = None,
        unhealthy_threshold: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#name GoogleComputeHealthCheck#name}
        :param check_interval_sec: How often (in seconds) to send a health check. The default value is 5 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#check_interval_sec GoogleComputeHealthCheck#check_interval_sec}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#description GoogleComputeHealthCheck#description}
        :param grpc_health_check: grpc_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#grpc_health_check GoogleComputeHealthCheck#grpc_health_check}
        :param healthy_threshold: A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#healthy_threshold GoogleComputeHealthCheck#healthy_threshold}
        :param http2_health_check: http2_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#http2_health_check GoogleComputeHealthCheck#http2_health_check}
        :param http_health_check: http_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#http_health_check GoogleComputeHealthCheck#http_health_check}
        :param https_health_check: https_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#https_health_check GoogleComputeHealthCheck#https_health_check}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#id GoogleComputeHealthCheck#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#log_config GoogleComputeHealthCheck#log_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#project GoogleComputeHealthCheck#project}.
        :param ssl_health_check: ssl_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#ssl_health_check GoogleComputeHealthCheck#ssl_health_check}
        :param tcp_health_check: tcp_health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#tcp_health_check GoogleComputeHealthCheck#tcp_health_check}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#timeouts GoogleComputeHealthCheck#timeouts}
        :param timeout_sec: How long (in seconds) to wait before claiming failure. The default value is 5 seconds. It is invalid for timeoutSec to have greater value than checkIntervalSec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#timeout_sec GoogleComputeHealthCheck#timeout_sec}
        :param unhealthy_threshold: A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#unhealthy_threshold GoogleComputeHealthCheck#unhealthy_threshold}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(grpc_health_check, dict):
            grpc_health_check = GoogleComputeHealthCheckGrpcHealthCheck(**grpc_health_check)
        if isinstance(http2_health_check, dict):
            http2_health_check = GoogleComputeHealthCheckHttp2HealthCheck(**http2_health_check)
        if isinstance(http_health_check, dict):
            http_health_check = GoogleComputeHealthCheckHttpHealthCheck(**http_health_check)
        if isinstance(https_health_check, dict):
            https_health_check = GoogleComputeHealthCheckHttpsHealthCheck(**https_health_check)
        if isinstance(log_config, dict):
            log_config = GoogleComputeHealthCheckLogConfig(**log_config)
        if isinstance(ssl_health_check, dict):
            ssl_health_check = GoogleComputeHealthCheckSslHealthCheck(**ssl_health_check)
        if isinstance(tcp_health_check, dict):
            tcp_health_check = GoogleComputeHealthCheckTcpHealthCheck(**tcp_health_check)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeHealthCheckTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument check_interval_sec", value=check_interval_sec, expected_type=type_hints["check_interval_sec"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument grpc_health_check", value=grpc_health_check, expected_type=type_hints["grpc_health_check"])
            check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
            check_type(argname="argument http2_health_check", value=http2_health_check, expected_type=type_hints["http2_health_check"])
            check_type(argname="argument http_health_check", value=http_health_check, expected_type=type_hints["http_health_check"])
            check_type(argname="argument https_health_check", value=https_health_check, expected_type=type_hints["https_health_check"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument ssl_health_check", value=ssl_health_check, expected_type=type_hints["ssl_health_check"])
            check_type(argname="argument tcp_health_check", value=tcp_health_check, expected_type=type_hints["tcp_health_check"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument timeout_sec", value=timeout_sec, expected_type=type_hints["timeout_sec"])
            check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if check_interval_sec is not None:
            self._values["check_interval_sec"] = check_interval_sec
        if description is not None:
            self._values["description"] = description
        if grpc_health_check is not None:
            self._values["grpc_health_check"] = grpc_health_check
        if healthy_threshold is not None:
            self._values["healthy_threshold"] = healthy_threshold
        if http2_health_check is not None:
            self._values["http2_health_check"] = http2_health_check
        if http_health_check is not None:
            self._values["http_health_check"] = http_health_check
        if https_health_check is not None:
            self._values["https_health_check"] = https_health_check
        if id is not None:
            self._values["id"] = id
        if log_config is not None:
            self._values["log_config"] = log_config
        if project is not None:
            self._values["project"] = project
        if ssl_health_check is not None:
            self._values["ssl_health_check"] = ssl_health_check
        if tcp_health_check is not None:
            self._values["tcp_health_check"] = tcp_health_check
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if timeout_sec is not None:
            self._values["timeout_sec"] = timeout_sec
        if unhealthy_threshold is not None:
            self._values["unhealthy_threshold"] = unhealthy_threshold

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

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035.  Specifically, the name must be 1-63 characters long and
        match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means
        the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the
        last character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#name GoogleComputeHealthCheck#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def check_interval_sec(self) -> typing.Optional[jsii.Number]:
        '''How often (in seconds) to send a health check. The default value is 5 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#check_interval_sec GoogleComputeHealthCheck#check_interval_sec}
        '''
        result = self._values.get("check_interval_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#description GoogleComputeHealthCheck#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def grpc_health_check(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckGrpcHealthCheck"]:
        '''grpc_health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#grpc_health_check GoogleComputeHealthCheck#grpc_health_check}
        '''
        result = self._values.get("grpc_health_check")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckGrpcHealthCheck"], result)

    @builtins.property
    def healthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''A so-far unhealthy instance will be marked healthy after this many consecutive successes. The default value is 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#healthy_threshold GoogleComputeHealthCheck#healthy_threshold}
        '''
        result = self._values.get("healthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http2_health_check(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckHttp2HealthCheck"]:
        '''http2_health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#http2_health_check GoogleComputeHealthCheck#http2_health_check}
        '''
        result = self._values.get("http2_health_check")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckHttp2HealthCheck"], result)

    @builtins.property
    def http_health_check(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckHttpHealthCheck"]:
        '''http_health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#http_health_check GoogleComputeHealthCheck#http_health_check}
        '''
        result = self._values.get("http_health_check")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckHttpHealthCheck"], result)

    @builtins.property
    def https_health_check(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckHttpsHealthCheck"]:
        '''https_health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#https_health_check GoogleComputeHealthCheck#https_health_check}
        '''
        result = self._values.get("https_health_check")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckHttpsHealthCheck"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#id GoogleComputeHealthCheck#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_config(self) -> typing.Optional["GoogleComputeHealthCheckLogConfig"]:
        '''log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#log_config GoogleComputeHealthCheck#log_config}
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckLogConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#project GoogleComputeHealthCheck#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_health_check(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckSslHealthCheck"]:
        '''ssl_health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#ssl_health_check GoogleComputeHealthCheck#ssl_health_check}
        '''
        result = self._values.get("ssl_health_check")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckSslHealthCheck"], result)

    @builtins.property
    def tcp_health_check(
        self,
    ) -> typing.Optional["GoogleComputeHealthCheckTcpHealthCheck"]:
        '''tcp_health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#tcp_health_check GoogleComputeHealthCheck#tcp_health_check}
        '''
        result = self._values.get("tcp_health_check")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckTcpHealthCheck"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeHealthCheckTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#timeouts GoogleComputeHealthCheck#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeHealthCheckTimeouts"], result)

    @builtins.property
    def timeout_sec(self) -> typing.Optional[jsii.Number]:
        '''How long (in seconds) to wait before claiming failure.

        The default value is 5 seconds.  It is invalid for timeoutSec to have
        greater value than checkIntervalSec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#timeout_sec GoogleComputeHealthCheck#timeout_sec}
        '''
        result = self._values.get("timeout_sec")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
        '''A so-far healthy instance will be marked unhealthy after this many consecutive failures. The default value is 2.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#unhealthy_threshold GoogleComputeHealthCheck#unhealthy_threshold}
        '''
        result = self._values.get("unhealthy_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckGrpcHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "grpc_service_name": "grpcServiceName",
        "port": "port",
        "port_name": "portName",
        "port_specification": "portSpecification",
    },
)
class GoogleComputeHealthCheckGrpcHealthCheck:
    def __init__(
        self,
        *,
        grpc_service_name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param grpc_service_name: The gRPC service name for the health check. The value of grpcServiceName has the following meanings by convention: - Empty serviceName means the overall status of all services at the backend. - Non-empty serviceName means the health of that gRPC service, as defined by the owner of the service. The grpcServiceName can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#grpc_service_name GoogleComputeHealthCheck#grpc_service_name}
        :param port: The port number for the health check request. Must be specified if portName and portSpecification are not set or if port_specification is USE_FIXED_PORT. Valid values are 1 through 65535. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, gRPC health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckGrpcHealthCheck.__init__)
            check_type(argname="argument grpc_service_name", value=grpc_service_name, expected_type=type_hints["grpc_service_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument port_specification", value=port_specification, expected_type=type_hints["port_specification"])
        self._values: typing.Dict[str, typing.Any] = {}
        if grpc_service_name is not None:
            self._values["grpc_service_name"] = grpc_service_name
        if port is not None:
            self._values["port"] = port
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_specification is not None:
            self._values["port_specification"] = port_specification

    @builtins.property
    def grpc_service_name(self) -> typing.Optional[builtins.str]:
        '''The gRPC service name for the health check.

        The value of grpcServiceName has the following meanings by convention:

        - Empty serviceName means the overall status of all services at the backend.
        - Non-empty serviceName means the health of that gRPC service, as defined by the owner of the service.
          The grpcServiceName can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#grpc_service_name GoogleComputeHealthCheck#grpc_service_name}
        '''
        result = self._values.get("grpc_service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port number for the health check request.

        Must be specified if portName and portSpecification are not set
        or if port_specification is USE_FIXED_PORT. Valid values are 1 through 65535.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_specification(self) -> typing.Optional[builtins.str]:
        '''Specifies how port is selected for health checking, can be one of the following values:.

        'USE_FIXED_PORT': The port number in 'port' is used for health checking.

        'USE_NAMED_PORT': The 'portName' is used for health checking.

        'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each
        network endpoint is used for health checking. For other backends, the
        port or named port specified in the Backend Service is used for health
        checking.

        If not specified, gRPC health check follows behavior specified in 'port' and
        'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        result = self._values.get("port_specification")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckGrpcHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckGrpcHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckGrpcHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckGrpcHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGrpcServiceName")
    def reset_grpc_service_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcServiceName", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPortName")
    def reset_port_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortName", []))

    @jsii.member(jsii_name="resetPortSpecification")
    def reset_port_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortSpecification", []))

    @builtins.property
    @jsii.member(jsii_name="grpcServiceNameInput")
    def grpc_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "grpcServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portSpecificationInput")
    def port_specification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="grpcServiceName")
    def grpc_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "grpcServiceName"))

    @grpc_service_name.setter
    def grpc_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckGrpcHealthCheckOutputReference, "grpc_service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "grpcServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckGrpcHealthCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckGrpcHealthCheckOutputReference, "port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="portSpecification")
    def port_specification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portSpecification"))

    @port_specification.setter
    def port_specification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckGrpcHealthCheckOutputReference, "port_specification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeHealthCheckGrpcHealthCheck]:
        return typing.cast(typing.Optional[GoogleComputeHealthCheckGrpcHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeHealthCheckGrpcHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckGrpcHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckHttp2HealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "port": "port",
        "port_name": "portName",
        "port_specification": "portSpecification",
        "proxy_header": "proxyHeader",
        "request_path": "requestPath",
        "response": "response",
    },
)
class GoogleComputeHealthCheckHttp2HealthCheck:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request_path: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The value of the host header in the HTTP2 health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        :param port: The TCP port number for the HTTP2 health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, HTTP2 health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request_path: The request path of the HTTP2 health check request. The default value is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckHttp2HealthCheck.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument port_specification", value=port_specification, expected_type=type_hints["port_specification"])
            check_type(argname="argument proxy_header", value=proxy_header, expected_type=type_hints["proxy_header"])
            check_type(argname="argument request_path", value=request_path, expected_type=type_hints["request_path"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_specification is not None:
            self._values["port_specification"] = port_specification
        if proxy_header is not None:
            self._values["proxy_header"] = proxy_header
        if request_path is not None:
            self._values["request_path"] = request_path
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The value of the host header in the HTTP2 health check request.

        If left empty (default value), the public IP on behalf of which this health
        check is performed will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port number for the HTTP2 health check request. The default value is 443.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_specification(self) -> typing.Optional[builtins.str]:
        '''Specifies how port is selected for health checking, can be one of the following values:.

        'USE_FIXED_PORT': The port number in 'port' is used for health checking.

        'USE_NAMED_PORT': The 'portName' is used for health checking.

        'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each
        network endpoint is used for health checking. For other backends, the
        port or named port specified in the Backend Service is used for health
        checking.

        If not specified, HTTP2 health check follows behavior specified in 'port' and
        'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        result = self._values.get("port_specification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_header(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of proxy header to append before sending data to the backend.

        Default value: "NONE" Possible values: ["NONE", "PROXY_V1"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        '''
        result = self._values.get("proxy_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_path(self) -> typing.Optional[builtins.str]:
        '''The request path of the HTTP2 health check request. The default value is /.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        '''
        result = self._values.get("request_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response(self) -> typing.Optional[builtins.str]:
        '''The bytes to match against the beginning of the response data.

        If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckHttp2HealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckHttp2HealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckHttp2HealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckHttp2HealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPortName")
    def reset_port_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortName", []))

    @jsii.member(jsii_name="resetPortSpecification")
    def reset_port_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortSpecification", []))

    @jsii.member(jsii_name="resetProxyHeader")
    def reset_proxy_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyHeader", []))

    @jsii.member(jsii_name="resetRequestPath")
    def reset_request_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestPath", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portSpecificationInput")
    def port_specification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyHeaderInput")
    def proxy_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="requestPathInput")
    def request_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestPathInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="portSpecification")
    def port_specification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portSpecification"))

    @port_specification.setter
    def port_specification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "port_specification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="proxyHeader")
    def proxy_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyHeader"))

    @proxy_header.setter
    def proxy_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "proxy_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyHeader", value)

    @builtins.property
    @jsii.member(jsii_name="requestPath")
    def request_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestPath"))

    @request_path.setter
    def request_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "request_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestPath", value)

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "response"))

    @response.setter
    def response(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "response").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "response", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeHealthCheckHttp2HealthCheck]:
        return typing.cast(typing.Optional[GoogleComputeHealthCheckHttp2HealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeHealthCheckHttp2HealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttp2HealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckHttpHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "port": "port",
        "port_name": "portName",
        "port_specification": "portSpecification",
        "proxy_header": "proxyHeader",
        "request_path": "requestPath",
        "response": "response",
    },
)
class GoogleComputeHealthCheckHttpHealthCheck:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request_path: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        :param port: The TCP port number for the HTTP health check request. The default value is 80. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, HTTP health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request_path: The request path of the HTTP health check request. The default value is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckHttpHealthCheck.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument port_specification", value=port_specification, expected_type=type_hints["port_specification"])
            check_type(argname="argument proxy_header", value=proxy_header, expected_type=type_hints["proxy_header"])
            check_type(argname="argument request_path", value=request_path, expected_type=type_hints["request_path"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_specification is not None:
            self._values["port_specification"] = port_specification
        if proxy_header is not None:
            self._values["proxy_header"] = proxy_header
        if request_path is not None:
            self._values["request_path"] = request_path
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The value of the host header in the HTTP health check request.

        If left empty (default value), the public IP on behalf of which this health
        check is performed will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port number for the HTTP health check request. The default value is 80.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_specification(self) -> typing.Optional[builtins.str]:
        '''Specifies how port is selected for health checking, can be one of the following values:.

        'USE_FIXED_PORT': The port number in 'port' is used for health checking.

        'USE_NAMED_PORT': The 'portName' is used for health checking.

        'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each
        network endpoint is used for health checking. For other backends, the
        port or named port specified in the Backend Service is used for health
        checking.

        If not specified, HTTP health check follows behavior specified in 'port' and
        'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        result = self._values.get("port_specification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_header(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of proxy header to append before sending data to the backend.

        Default value: "NONE" Possible values: ["NONE", "PROXY_V1"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        '''
        result = self._values.get("proxy_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_path(self) -> typing.Optional[builtins.str]:
        '''The request path of the HTTP health check request. The default value is /.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        '''
        result = self._values.get("request_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response(self) -> typing.Optional[builtins.str]:
        '''The bytes to match against the beginning of the response data.

        If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckHttpHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckHttpHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckHttpHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckHttpHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPortName")
    def reset_port_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortName", []))

    @jsii.member(jsii_name="resetPortSpecification")
    def reset_port_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortSpecification", []))

    @jsii.member(jsii_name="resetProxyHeader")
    def reset_proxy_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyHeader", []))

    @jsii.member(jsii_name="resetRequestPath")
    def reset_request_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestPath", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portSpecificationInput")
    def port_specification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyHeaderInput")
    def proxy_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="requestPathInput")
    def request_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestPathInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="portSpecification")
    def port_specification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portSpecification"))

    @port_specification.setter
    def port_specification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "port_specification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="proxyHeader")
    def proxy_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyHeader"))

    @proxy_header.setter
    def proxy_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "proxy_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyHeader", value)

    @builtins.property
    @jsii.member(jsii_name="requestPath")
    def request_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestPath"))

    @request_path.setter
    def request_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "request_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestPath", value)

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "response"))

    @response.setter
    def response(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "response").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "response", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeHealthCheckHttpHealthCheck]:
        return typing.cast(typing.Optional[GoogleComputeHealthCheckHttpHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeHealthCheckHttpHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckHttpsHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "port": "port",
        "port_name": "portName",
        "port_specification": "portSpecification",
        "proxy_header": "proxyHeader",
        "request_path": "requestPath",
        "response": "response",
    },
)
class GoogleComputeHealthCheckHttpsHealthCheck:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request_path: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param host: The value of the host header in the HTTPS health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        :param port: The TCP port number for the HTTPS health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, HTTPS health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request_path: The request path of the HTTPS health check request. The default value is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckHttpsHealthCheck.__init__)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument port_specification", value=port_specification, expected_type=type_hints["port_specification"])
            check_type(argname="argument proxy_header", value=proxy_header, expected_type=type_hints["proxy_header"])
            check_type(argname="argument request_path", value=request_path, expected_type=type_hints["request_path"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
        self._values: typing.Dict[str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if port is not None:
            self._values["port"] = port
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_specification is not None:
            self._values["port_specification"] = port_specification
        if proxy_header is not None:
            self._values["proxy_header"] = proxy_header
        if request_path is not None:
            self._values["request_path"] = request_path
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The value of the host header in the HTTPS health check request.

        If left empty (default value), the public IP on behalf of which this health
        check is performed will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#host GoogleComputeHealthCheck#host}
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port number for the HTTPS health check request. The default value is 443.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_specification(self) -> typing.Optional[builtins.str]:
        '''Specifies how port is selected for health checking, can be one of the following values:.

        'USE_FIXED_PORT': The port number in 'port' is used for health checking.

        'USE_NAMED_PORT': The 'portName' is used for health checking.

        'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each
        network endpoint is used for health checking. For other backends, the
        port or named port specified in the Backend Service is used for health
        checking.

        If not specified, HTTPS health check follows behavior specified in 'port' and
        'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        result = self._values.get("port_specification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_header(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of proxy header to append before sending data to the backend.

        Default value: "NONE" Possible values: ["NONE", "PROXY_V1"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        '''
        result = self._values.get("proxy_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_path(self) -> typing.Optional[builtins.str]:
        '''The request path of the HTTPS health check request. The default value is /.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request_path GoogleComputeHealthCheck#request_path}
        '''
        result = self._values.get("request_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response(self) -> typing.Optional[builtins.str]:
        '''The bytes to match against the beginning of the response data.

        If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckHttpsHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckHttpsHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckHttpsHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckHttpsHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHost")
    def reset_host(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHost", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPortName")
    def reset_port_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortName", []))

    @jsii.member(jsii_name="resetPortSpecification")
    def reset_port_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortSpecification", []))

    @jsii.member(jsii_name="resetProxyHeader")
    def reset_proxy_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyHeader", []))

    @jsii.member(jsii_name="resetRequestPath")
    def reset_request_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestPath", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @builtins.property
    @jsii.member(jsii_name="hostInput")
    def host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portSpecificationInput")
    def port_specification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyHeaderInput")
    def proxy_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="requestPathInput")
    def request_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestPathInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="host")
    def host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "host"))

    @host.setter
    def host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="portSpecification")
    def port_specification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portSpecification"))

    @port_specification.setter
    def port_specification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "port_specification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="proxyHeader")
    def proxy_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyHeader"))

    @proxy_header.setter
    def proxy_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "proxy_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyHeader", value)

    @builtins.property
    @jsii.member(jsii_name="requestPath")
    def request_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestPath"))

    @request_path.setter
    def request_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "request_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestPath", value)

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "response"))

    @response.setter
    def response(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "response").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "response", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleComputeHealthCheckHttpsHealthCheck]:
        return typing.cast(typing.Optional[GoogleComputeHealthCheckHttpsHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeHealthCheckHttpsHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckHttpsHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckLogConfig",
    jsii_struct_bases=[],
    name_mapping={"enable": "enable"},
)
class GoogleComputeHealthCheckLogConfig:
    def __init__(
        self,
        *,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable: Indicates whether or not to export logs. This is false by default, which means no health check logging will be done. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#enable GoogleComputeHealthCheck#enable}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckLogConfig.__init__)
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable is not None:
            self._values["enable"] = enable

    @builtins.property
    def enable(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether or not to export logs.

        This is false by default,
        which means no health check logging will be done.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#enable GoogleComputeHealthCheck#enable}
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckLogConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckLogConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckLogConfigOutputReference, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeHealthCheckLogConfig]:
        return typing.cast(typing.Optional[GoogleComputeHealthCheckLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeHealthCheckLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckLogConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckSslHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "port_name": "portName",
        "port_specification": "portSpecification",
        "proxy_header": "proxyHeader",
        "request": "request",
        "response": "response",
    },
)
class GoogleComputeHealthCheckSslHealthCheck:
    def __init__(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: The TCP port number for the SSL health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, SSL health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request: The application data to send once the SSL connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request GoogleComputeHealthCheck#request}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckSslHealthCheck.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument port_specification", value=port_specification, expected_type=type_hints["port_specification"])
            check_type(argname="argument proxy_header", value=proxy_header, expected_type=type_hints["proxy_header"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_specification is not None:
            self._values["port_specification"] = port_specification
        if proxy_header is not None:
            self._values["proxy_header"] = proxy_header
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port number for the SSL health check request. The default value is 443.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_specification(self) -> typing.Optional[builtins.str]:
        '''Specifies how port is selected for health checking, can be one of the following values:.

        'USE_FIXED_PORT': The port number in 'port' is used for health checking.

        'USE_NAMED_PORT': The 'portName' is used for health checking.

        'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each
        network endpoint is used for health checking. For other backends, the
        port or named port specified in the Backend Service is used for health
        checking.

        If not specified, SSL health check follows behavior specified in 'port' and
        'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        result = self._values.get("port_specification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_header(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of proxy header to append before sending data to the backend.

        Default value: "NONE" Possible values: ["NONE", "PROXY_V1"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        '''
        result = self._values.get("proxy_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request(self) -> typing.Optional[builtins.str]:
        '''The application data to send once the SSL connection has been established (default value is empty).

        If both request and response are
        empty, the connection establishment alone will indicate health. The request
        data can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request GoogleComputeHealthCheck#request}
        '''
        result = self._values.get("request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response(self) -> typing.Optional[builtins.str]:
        '''The bytes to match against the beginning of the response data.

        If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckSslHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckSslHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckSslHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckSslHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPortName")
    def reset_port_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortName", []))

    @jsii.member(jsii_name="resetPortSpecification")
    def reset_port_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortSpecification", []))

    @jsii.member(jsii_name="resetProxyHeader")
    def reset_proxy_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyHeader", []))

    @jsii.member(jsii_name="resetRequest")
    def reset_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequest", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portSpecificationInput")
    def port_specification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyHeaderInput")
    def proxy_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="requestInput")
    def request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckSslHealthCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckSslHealthCheckOutputReference, "port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="portSpecification")
    def port_specification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portSpecification"))

    @port_specification.setter
    def port_specification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckSslHealthCheckOutputReference, "port_specification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="proxyHeader")
    def proxy_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyHeader"))

    @proxy_header.setter
    def proxy_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckSslHealthCheckOutputReference, "proxy_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyHeader", value)

    @builtins.property
    @jsii.member(jsii_name="request")
    def request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "request"))

    @request.setter
    def request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckSslHealthCheckOutputReference, "request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "request", value)

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "response"))

    @response.setter
    def response(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckSslHealthCheckOutputReference, "response").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "response", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeHealthCheckSslHealthCheck]:
        return typing.cast(typing.Optional[GoogleComputeHealthCheckSslHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeHealthCheckSslHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckSslHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckTcpHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "port_name": "portName",
        "port_specification": "portSpecification",
        "proxy_header": "proxyHeader",
        "request": "request",
        "response": "response",
    },
)
class GoogleComputeHealthCheckTcpHealthCheck:
    def __init__(
        self,
        *,
        port: typing.Optional[jsii.Number] = None,
        port_name: typing.Optional[builtins.str] = None,
        port_specification: typing.Optional[builtins.str] = None,
        proxy_header: typing.Optional[builtins.str] = None,
        request: typing.Optional[builtins.str] = None,
        response: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param port: The TCP port number for the TCP health check request. The default value is 443. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        :param port_name: Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        :param port_specification: Specifies how port is selected for health checking, can be one of the following values:. 'USE_FIXED_PORT': The port number in 'port' is used for health checking. 'USE_NAMED_PORT': The 'portName' is used for health checking. 'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each network endpoint is used for health checking. For other backends, the port or named port specified in the Backend Service is used for health checking. If not specified, TCP health check follows behavior specified in 'port' and 'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        :param proxy_header: Specifies the type of proxy header to append before sending data to the backend. Default value: "NONE" Possible values: ["NONE", "PROXY_V1"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        :param request: The application data to send once the TCP connection has been established (default value is empty). If both request and response are empty, the connection establishment alone will indicate health. The request data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request GoogleComputeHealthCheck#request}
        :param response: The bytes to match against the beginning of the response data. If left empty (the default value), any response will indicate health. The response data can only be ASCII. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckTcpHealthCheck.__init__)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument port_name", value=port_name, expected_type=type_hints["port_name"])
            check_type(argname="argument port_specification", value=port_specification, expected_type=type_hints["port_specification"])
            check_type(argname="argument proxy_header", value=proxy_header, expected_type=type_hints["proxy_header"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
        self._values: typing.Dict[str, typing.Any] = {}
        if port is not None:
            self._values["port"] = port
        if port_name is not None:
            self._values["port_name"] = port_name
        if port_specification is not None:
            self._values["port_specification"] = port_specification
        if proxy_header is not None:
            self._values["proxy_header"] = proxy_header
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The TCP port number for the TCP health check request. The default value is 443.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port GoogleComputeHealthCheck#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port_name(self) -> typing.Optional[builtins.str]:
        '''Port name as defined in InstanceGroup#NamedPort#name. If both port and port_name are defined, port takes precedence.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_name GoogleComputeHealthCheck#port_name}
        '''
        result = self._values.get("port_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port_specification(self) -> typing.Optional[builtins.str]:
        '''Specifies how port is selected for health checking, can be one of the following values:.

        'USE_FIXED_PORT': The port number in 'port' is used for health checking.

        'USE_NAMED_PORT': The 'portName' is used for health checking.

        'USE_SERVING_PORT': For NetworkEndpointGroup, the port specified for each
        network endpoint is used for health checking. For other backends, the
        port or named port specified in the Backend Service is used for health
        checking.

        If not specified, TCP health check follows behavior specified in 'port' and
        'portName' fields. Possible values: ["USE_FIXED_PORT", "USE_NAMED_PORT", "USE_SERVING_PORT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#port_specification GoogleComputeHealthCheck#port_specification}
        '''
        result = self._values.get("port_specification")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def proxy_header(self) -> typing.Optional[builtins.str]:
        '''Specifies the type of proxy header to append before sending data to the backend.

        Default value: "NONE" Possible values: ["NONE", "PROXY_V1"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#proxy_header GoogleComputeHealthCheck#proxy_header}
        '''
        result = self._values.get("proxy_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request(self) -> typing.Optional[builtins.str]:
        '''The application data to send once the TCP connection has been established (default value is empty).

        If both request and response are
        empty, the connection establishment alone will indicate health. The request
        data can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#request GoogleComputeHealthCheck#request}
        '''
        result = self._values.get("request")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response(self) -> typing.Optional[builtins.str]:
        '''The bytes to match against the beginning of the response data.

        If left empty
        (the default value), any response will indicate health. The response data
        can only be ASCII.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#response GoogleComputeHealthCheck#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckTcpHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckTcpHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckTcpHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckTcpHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPortName")
    def reset_port_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortName", []))

    @jsii.member(jsii_name="resetPortSpecification")
    def reset_port_specification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPortSpecification", []))

    @jsii.member(jsii_name="resetProxyHeader")
    def reset_proxy_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyHeader", []))

    @jsii.member(jsii_name="resetRequest")
    def reset_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequest", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="portNameInput")
    def port_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portNameInput"))

    @builtins.property
    @jsii.member(jsii_name="portSpecificationInput")
    def port_specification_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portSpecificationInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyHeaderInput")
    def proxy_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="requestInput")
    def request_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTcpHealthCheckOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="portName")
    def port_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portName"))

    @port_name.setter
    def port_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTcpHealthCheckOutputReference, "port_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portName", value)

    @builtins.property
    @jsii.member(jsii_name="portSpecification")
    def port_specification(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "portSpecification"))

    @port_specification.setter
    def port_specification(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTcpHealthCheckOutputReference, "port_specification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="proxyHeader")
    def proxy_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyHeader"))

    @proxy_header.setter
    def proxy_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTcpHealthCheckOutputReference, "proxy_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyHeader", value)

    @builtins.property
    @jsii.member(jsii_name="request")
    def request(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "request"))

    @request.setter
    def request(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTcpHealthCheckOutputReference, "request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "request", value)

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "response"))

    @response.setter
    def response(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTcpHealthCheckOutputReference, "response").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "response", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeHealthCheckTcpHealthCheck]:
        return typing.cast(typing.Optional[GoogleComputeHealthCheckTcpHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeHealthCheckTcpHealthCheck],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTcpHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeHealthCheckTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#create GoogleComputeHealthCheck#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#delete GoogleComputeHealthCheck#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#update GoogleComputeHealthCheck#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#create GoogleComputeHealthCheck#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#delete GoogleComputeHealthCheck#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_health_check#update GoogleComputeHealthCheck#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeHealthCheckTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeHealthCheckTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeHealthCheck.GoogleComputeHealthCheckTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeHealthCheckTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeHealthCheckTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeHealthCheckTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeHealthCheckTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeHealthCheckTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeHealthCheck",
    "GoogleComputeHealthCheckConfig",
    "GoogleComputeHealthCheckGrpcHealthCheck",
    "GoogleComputeHealthCheckGrpcHealthCheckOutputReference",
    "GoogleComputeHealthCheckHttp2HealthCheck",
    "GoogleComputeHealthCheckHttp2HealthCheckOutputReference",
    "GoogleComputeHealthCheckHttpHealthCheck",
    "GoogleComputeHealthCheckHttpHealthCheckOutputReference",
    "GoogleComputeHealthCheckHttpsHealthCheck",
    "GoogleComputeHealthCheckHttpsHealthCheckOutputReference",
    "GoogleComputeHealthCheckLogConfig",
    "GoogleComputeHealthCheckLogConfigOutputReference",
    "GoogleComputeHealthCheckSslHealthCheck",
    "GoogleComputeHealthCheckSslHealthCheckOutputReference",
    "GoogleComputeHealthCheckTcpHealthCheck",
    "GoogleComputeHealthCheckTcpHealthCheckOutputReference",
    "GoogleComputeHealthCheckTimeouts",
    "GoogleComputeHealthCheckTimeoutsOutputReference",
]

publication.publish()
