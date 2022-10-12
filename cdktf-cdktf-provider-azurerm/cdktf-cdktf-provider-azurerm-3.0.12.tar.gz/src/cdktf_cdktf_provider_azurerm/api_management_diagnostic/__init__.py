'''
# `azurerm_api_management_diagnostic`

Refer to the Terraform Registory for docs: [`azurerm_api_management_diagnostic`](https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic).
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


class ApiManagementDiagnostic(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnostic",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic azurerm_api_management_diagnostic}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_management_logger_id: builtins.str,
        api_management_name: builtins.str,
        identifier: builtins.str,
        resource_group_name: builtins.str,
        always_log_errors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backend_request: typing.Optional[typing.Union["ApiManagementDiagnosticBackendRequest", typing.Dict[str, typing.Any]]] = None,
        backend_response: typing.Optional[typing.Union["ApiManagementDiagnosticBackendResponse", typing.Dict[str, typing.Any]]] = None,
        frontend_request: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendRequest", typing.Dict[str, typing.Any]]] = None,
        frontend_response: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendResponse", typing.Dict[str, typing.Any]]] = None,
        http_correlation_protocol: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_client_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operation_name_format: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementDiagnosticTimeouts", typing.Dict[str, typing.Any]]] = None,
        verbosity: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic azurerm_api_management_diagnostic} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_management_logger_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#api_management_logger_id ApiManagementDiagnostic#api_management_logger_id}.
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#api_management_name ApiManagementDiagnostic#api_management_name}.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#identifier ApiManagementDiagnostic#identifier}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#resource_group_name ApiManagementDiagnostic#resource_group_name}.
        :param always_log_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#always_log_errors ApiManagementDiagnostic#always_log_errors}.
        :param backend_request: backend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#backend_request ApiManagementDiagnostic#backend_request}
        :param backend_response: backend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#backend_response ApiManagementDiagnostic#backend_response}
        :param frontend_request: frontend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#frontend_request ApiManagementDiagnostic#frontend_request}
        :param frontend_response: frontend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#frontend_response ApiManagementDiagnostic#frontend_response}
        :param http_correlation_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#http_correlation_protocol ApiManagementDiagnostic#http_correlation_protocol}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#id ApiManagementDiagnostic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_client_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#log_client_ip ApiManagementDiagnostic#log_client_ip}.
        :param operation_name_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#operation_name_format ApiManagementDiagnostic#operation_name_format}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#sampling_percentage ApiManagementDiagnostic#sampling_percentage}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#timeouts ApiManagementDiagnostic#timeouts}
        :param verbosity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#verbosity ApiManagementDiagnostic#verbosity}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnostic.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiManagementDiagnosticConfig(
            api_management_logger_id=api_management_logger_id,
            api_management_name=api_management_name,
            identifier=identifier,
            resource_group_name=resource_group_name,
            always_log_errors=always_log_errors,
            backend_request=backend_request,
            backend_response=backend_response,
            frontend_request=frontend_request,
            frontend_response=frontend_response,
            http_correlation_protocol=http_correlation_protocol,
            id=id,
            log_client_ip=log_client_ip,
            operation_name_format=operation_name_format,
            sampling_percentage=sampling_percentage,
            timeouts=timeouts,
            verbosity=verbosity,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBackendRequest")
    def put_backend_request(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticBackendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        value = ApiManagementDiagnosticBackendRequest(
            body_bytes=body_bytes,
            data_masking=data_masking,
            headers_to_log=headers_to_log,
        )

        return typing.cast(None, jsii.invoke(self, "putBackendRequest", [value]))

    @jsii.member(jsii_name="putBackendResponse")
    def put_backend_response(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticBackendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        value = ApiManagementDiagnosticBackendResponse(
            body_bytes=body_bytes,
            data_masking=data_masking,
            headers_to_log=headers_to_log,
        )

        return typing.cast(None, jsii.invoke(self, "putBackendResponse", [value]))

    @jsii.member(jsii_name="putFrontendRequest")
    def put_frontend_request(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        value = ApiManagementDiagnosticFrontendRequest(
            body_bytes=body_bytes,
            data_masking=data_masking,
            headers_to_log=headers_to_log,
        )

        return typing.cast(None, jsii.invoke(self, "putFrontendRequest", [value]))

    @jsii.member(jsii_name="putFrontendResponse")
    def put_frontend_response(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        value = ApiManagementDiagnosticFrontendResponse(
            body_bytes=body_bytes,
            data_masking=data_masking,
            headers_to_log=headers_to_log,
        )

        return typing.cast(None, jsii.invoke(self, "putFrontendResponse", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#create ApiManagementDiagnostic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#delete ApiManagementDiagnostic#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#read ApiManagementDiagnostic#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#update ApiManagementDiagnostic#update}.
        '''
        value = ApiManagementDiagnosticTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAlwaysLogErrors")
    def reset_always_log_errors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlwaysLogErrors", []))

    @jsii.member(jsii_name="resetBackendRequest")
    def reset_backend_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendRequest", []))

    @jsii.member(jsii_name="resetBackendResponse")
    def reset_backend_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackendResponse", []))

    @jsii.member(jsii_name="resetFrontendRequest")
    def reset_frontend_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrontendRequest", []))

    @jsii.member(jsii_name="resetFrontendResponse")
    def reset_frontend_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrontendResponse", []))

    @jsii.member(jsii_name="resetHttpCorrelationProtocol")
    def reset_http_correlation_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpCorrelationProtocol", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogClientIp")
    def reset_log_client_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogClientIp", []))

    @jsii.member(jsii_name="resetOperationNameFormat")
    def reset_operation_name_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperationNameFormat", []))

    @jsii.member(jsii_name="resetSamplingPercentage")
    def reset_sampling_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSamplingPercentage", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVerbosity")
    def reset_verbosity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerbosity", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backendRequest")
    def backend_request(self) -> "ApiManagementDiagnosticBackendRequestOutputReference":
        return typing.cast("ApiManagementDiagnosticBackendRequestOutputReference", jsii.get(self, "backendRequest"))

    @builtins.property
    @jsii.member(jsii_name="backendResponse")
    def backend_response(
        self,
    ) -> "ApiManagementDiagnosticBackendResponseOutputReference":
        return typing.cast("ApiManagementDiagnosticBackendResponseOutputReference", jsii.get(self, "backendResponse"))

    @builtins.property
    @jsii.member(jsii_name="frontendRequest")
    def frontend_request(
        self,
    ) -> "ApiManagementDiagnosticFrontendRequestOutputReference":
        return typing.cast("ApiManagementDiagnosticFrontendRequestOutputReference", jsii.get(self, "frontendRequest"))

    @builtins.property
    @jsii.member(jsii_name="frontendResponse")
    def frontend_response(
        self,
    ) -> "ApiManagementDiagnosticFrontendResponseOutputReference":
        return typing.cast("ApiManagementDiagnosticFrontendResponseOutputReference", jsii.get(self, "frontendResponse"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementDiagnosticTimeoutsOutputReference":
        return typing.cast("ApiManagementDiagnosticTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="alwaysLogErrorsInput")
    def always_log_errors_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "alwaysLogErrorsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementLoggerIdInput")
    def api_management_logger_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementLoggerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="apiManagementNameInput")
    def api_management_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiManagementNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendRequestInput")
    def backend_request_input(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticBackendRequest"]:
        return typing.cast(typing.Optional["ApiManagementDiagnosticBackendRequest"], jsii.get(self, "backendRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="backendResponseInput")
    def backend_response_input(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticBackendResponse"]:
        return typing.cast(typing.Optional["ApiManagementDiagnosticBackendResponse"], jsii.get(self, "backendResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendRequestInput")
    def frontend_request_input(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticFrontendRequest"]:
        return typing.cast(typing.Optional["ApiManagementDiagnosticFrontendRequest"], jsii.get(self, "frontendRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendResponseInput")
    def frontend_response_input(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticFrontendResponse"]:
        return typing.cast(typing.Optional["ApiManagementDiagnosticFrontendResponse"], jsii.get(self, "frontendResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="httpCorrelationProtocolInput")
    def http_correlation_protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpCorrelationProtocolInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logClientIpInput")
    def log_client_ip_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "logClientIpInput"))

    @builtins.property
    @jsii.member(jsii_name="operationNameFormatInput")
    def operation_name_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationNameFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="samplingPercentageInput")
    def sampling_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ApiManagementDiagnosticTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementDiagnosticTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="verbosityInput")
    def verbosity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verbosityInput"))

    @builtins.property
    @jsii.member(jsii_name="alwaysLogErrors")
    def always_log_errors(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "alwaysLogErrors"))

    @always_log_errors.setter
    def always_log_errors(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "always_log_errors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysLogErrors", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementLoggerId")
    def api_management_logger_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementLoggerId"))

    @api_management_logger_id.setter
    def api_management_logger_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "api_management_logger_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementLoggerId", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementName")
    def api_management_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementName"))

    @api_management_name.setter
    def api_management_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "api_management_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementName", value)

    @builtins.property
    @jsii.member(jsii_name="httpCorrelationProtocol")
    def http_correlation_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpCorrelationProtocol"))

    @http_correlation_protocol.setter
    def http_correlation_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "http_correlation_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpCorrelationProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="logClientIp")
    def log_client_ip(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "logClientIp"))

    @log_client_ip.setter
    def log_client_ip(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "log_client_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logClientIp", value)

    @builtins.property
    @jsii.member(jsii_name="operationNameFormat")
    def operation_name_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operationNameFormat"))

    @operation_name_format.setter
    def operation_name_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "operation_name_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationNameFormat", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="samplingPercentage")
    def sampling_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingPercentage"))

    @sampling_percentage.setter
    def sampling_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "sampling_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="verbosity")
    def verbosity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verbosity"))

    @verbosity.setter
    def verbosity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnostic, "verbosity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verbosity", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequest",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementDiagnosticBackendRequest:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticBackendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementDiagnosticBackendRequestDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequest.__init__)
            check_type(argname="argument body_bytes", value=body_bytes, expected_type=type_hints["body_bytes"])
            check_type(argname="argument data_masking", value=data_masking, expected_type=type_hints["data_masking"])
            check_type(argname="argument headers_to_log", value=headers_to_log, expected_type=type_hints["headers_to_log"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body_bytes is not None:
            self._values["body_bytes"] = body_bytes
        if data_masking is not None:
            self._values["data_masking"] = data_masking
        if headers_to_log is not None:
            self._values["headers_to_log"] = headers_to_log

    @builtins.property
    def body_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticBackendRequestDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementDiagnosticBackendRequestDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementDiagnosticBackendRequestDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticBackendRequestDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticBackendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMasking.__init__)
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument query_params", value=query_params, expected_type=type_hints["query_params"])
        self._values: typing.Dict[str, typing.Any] = {}
        if headers is not None:
            self._values["headers"] = headers
        if query_params is not None:
            self._values["query_params"] = query_params

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendRequestDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendRequestDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendRequestDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendRequestDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendRequestDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticBackendRequestDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendRequestDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticBackendRequestDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendRequestDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticBackendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingOutputReference.put_query_params)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryParams", [value]))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetQueryParams")
    def reset_query_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryParams", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> ApiManagementDiagnosticBackendRequestDataMaskingHeadersList:
        return typing.cast(ApiManagementDiagnosticBackendRequestDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList":
        return typing.cast("ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendRequestDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendRequestDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticBackendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendRequestDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticBackendRequestDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticBackendRequestDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendRequestDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendRequestDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendRequestOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticBackendRequestDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        value = ApiManagementDiagnosticBackendRequestDataMasking(
            headers=headers, query_params=query_params
        )

        return typing.cast(None, jsii.invoke(self, "putDataMasking", [value]))

    @jsii.member(jsii_name="resetBodyBytes")
    def reset_body_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodyBytes", []))

    @jsii.member(jsii_name="resetDataMasking")
    def reset_data_masking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataMasking", []))

    @jsii.member(jsii_name="resetHeadersToLog")
    def reset_headers_to_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeadersToLog", []))

    @builtins.property
    @jsii.member(jsii_name="dataMasking")
    def data_masking(
        self,
    ) -> ApiManagementDiagnosticBackendRequestDataMaskingOutputReference:
        return typing.cast(ApiManagementDiagnosticBackendRequestDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticBackendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendRequestDataMasking], jsii.get(self, "dataMaskingInput"))

    @builtins.property
    @jsii.member(jsii_name="headersToLogInput")
    def headers_to_log_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersToLogInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytes")
    def body_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bodyBytes"))

    @body_bytes.setter
    def body_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementDiagnosticBackendRequest]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticBackendRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponse",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementDiagnosticBackendResponse:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticBackendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementDiagnosticBackendResponseDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponse.__init__)
            check_type(argname="argument body_bytes", value=body_bytes, expected_type=type_hints["body_bytes"])
            check_type(argname="argument data_masking", value=data_masking, expected_type=type_hints["data_masking"])
            check_type(argname="argument headers_to_log", value=headers_to_log, expected_type=type_hints["headers_to_log"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body_bytes is not None:
            self._values["body_bytes"] = body_bytes
        if data_masking is not None:
            self._values["data_masking"] = data_masking
        if headers_to_log is not None:
            self._values["headers_to_log"] = headers_to_log

    @builtins.property
    def body_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticBackendResponseDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementDiagnosticBackendResponseDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementDiagnosticBackendResponseDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticBackendResponseDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticBackendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMasking.__init__)
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument query_params", value=query_params, expected_type=type_hints["query_params"])
        self._values: typing.Dict[str, typing.Any] = {}
        if headers is not None:
            self._values["headers"] = headers
        if query_params is not None:
            self._values["query_params"] = query_params

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendResponseDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendResponseDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendResponseDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendResponseDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendResponseDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticBackendResponseDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendResponseDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticBackendResponseDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendResponseDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticBackendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingOutputReference.put_query_params)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryParams", [value]))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetQueryParams")
    def reset_query_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryParams", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> ApiManagementDiagnosticBackendResponseDataMaskingHeadersList:
        return typing.cast(ApiManagementDiagnosticBackendResponseDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList":
        return typing.cast("ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendResponseDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticBackendResponseDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticBackendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendResponseDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticBackendResponseDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticBackendResponseDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticBackendResponseDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticBackendResponseDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticBackendResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticBackendResponseOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticBackendResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticBackendResponseDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        value = ApiManagementDiagnosticBackendResponseDataMasking(
            headers=headers, query_params=query_params
        )

        return typing.cast(None, jsii.invoke(self, "putDataMasking", [value]))

    @jsii.member(jsii_name="resetBodyBytes")
    def reset_body_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodyBytes", []))

    @jsii.member(jsii_name="resetDataMasking")
    def reset_data_masking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataMasking", []))

    @jsii.member(jsii_name="resetHeadersToLog")
    def reset_headers_to_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeadersToLog", []))

    @builtins.property
    @jsii.member(jsii_name="dataMasking")
    def data_masking(
        self,
    ) -> ApiManagementDiagnosticBackendResponseDataMaskingOutputReference:
        return typing.cast(ApiManagementDiagnosticBackendResponseDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticBackendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendResponseDataMasking], jsii.get(self, "dataMaskingInput"))

    @builtins.property
    @jsii.member(jsii_name="headersToLogInput")
    def headers_to_log_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersToLogInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytes")
    def body_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bodyBytes"))

    @body_bytes.setter
    def body_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementDiagnosticBackendResponse]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticBackendResponse],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticBackendResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_management_logger_id": "apiManagementLoggerId",
        "api_management_name": "apiManagementName",
        "identifier": "identifier",
        "resource_group_name": "resourceGroupName",
        "always_log_errors": "alwaysLogErrors",
        "backend_request": "backendRequest",
        "backend_response": "backendResponse",
        "frontend_request": "frontendRequest",
        "frontend_response": "frontendResponse",
        "http_correlation_protocol": "httpCorrelationProtocol",
        "id": "id",
        "log_client_ip": "logClientIp",
        "operation_name_format": "operationNameFormat",
        "sampling_percentage": "samplingPercentage",
        "timeouts": "timeouts",
        "verbosity": "verbosity",
    },
)
class ApiManagementDiagnosticConfig(cdktf.TerraformMetaArguments):
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
        api_management_logger_id: builtins.str,
        api_management_name: builtins.str,
        identifier: builtins.str,
        resource_group_name: builtins.str,
        always_log_errors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backend_request: typing.Optional[typing.Union[ApiManagementDiagnosticBackendRequest, typing.Dict[str, typing.Any]]] = None,
        backend_response: typing.Optional[typing.Union[ApiManagementDiagnosticBackendResponse, typing.Dict[str, typing.Any]]] = None,
        frontend_request: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendRequest", typing.Dict[str, typing.Any]]] = None,
        frontend_response: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendResponse", typing.Dict[str, typing.Any]]] = None,
        http_correlation_protocol: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_client_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operation_name_format: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementDiagnosticTimeouts", typing.Dict[str, typing.Any]]] = None,
        verbosity: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_management_logger_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#api_management_logger_id ApiManagementDiagnostic#api_management_logger_id}.
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#api_management_name ApiManagementDiagnostic#api_management_name}.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#identifier ApiManagementDiagnostic#identifier}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#resource_group_name ApiManagementDiagnostic#resource_group_name}.
        :param always_log_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#always_log_errors ApiManagementDiagnostic#always_log_errors}.
        :param backend_request: backend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#backend_request ApiManagementDiagnostic#backend_request}
        :param backend_response: backend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#backend_response ApiManagementDiagnostic#backend_response}
        :param frontend_request: frontend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#frontend_request ApiManagementDiagnostic#frontend_request}
        :param frontend_response: frontend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#frontend_response ApiManagementDiagnostic#frontend_response}
        :param http_correlation_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#http_correlation_protocol ApiManagementDiagnostic#http_correlation_protocol}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#id ApiManagementDiagnostic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_client_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#log_client_ip ApiManagementDiagnostic#log_client_ip}.
        :param operation_name_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#operation_name_format ApiManagementDiagnostic#operation_name_format}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#sampling_percentage ApiManagementDiagnostic#sampling_percentage}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#timeouts ApiManagementDiagnostic#timeouts}
        :param verbosity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#verbosity ApiManagementDiagnostic#verbosity}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(backend_request, dict):
            backend_request = ApiManagementDiagnosticBackendRequest(**backend_request)
        if isinstance(backend_response, dict):
            backend_response = ApiManagementDiagnosticBackendResponse(**backend_response)
        if isinstance(frontend_request, dict):
            frontend_request = ApiManagementDiagnosticFrontendRequest(**frontend_request)
        if isinstance(frontend_response, dict):
            frontend_response = ApiManagementDiagnosticFrontendResponse(**frontend_response)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementDiagnosticTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_management_logger_id", value=api_management_logger_id, expected_type=type_hints["api_management_logger_id"])
            check_type(argname="argument api_management_name", value=api_management_name, expected_type=type_hints["api_management_name"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument always_log_errors", value=always_log_errors, expected_type=type_hints["always_log_errors"])
            check_type(argname="argument backend_request", value=backend_request, expected_type=type_hints["backend_request"])
            check_type(argname="argument backend_response", value=backend_response, expected_type=type_hints["backend_response"])
            check_type(argname="argument frontend_request", value=frontend_request, expected_type=type_hints["frontend_request"])
            check_type(argname="argument frontend_response", value=frontend_response, expected_type=type_hints["frontend_response"])
            check_type(argname="argument http_correlation_protocol", value=http_correlation_protocol, expected_type=type_hints["http_correlation_protocol"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_client_ip", value=log_client_ip, expected_type=type_hints["log_client_ip"])
            check_type(argname="argument operation_name_format", value=operation_name_format, expected_type=type_hints["operation_name_format"])
            check_type(argname="argument sampling_percentage", value=sampling_percentage, expected_type=type_hints["sampling_percentage"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument verbosity", value=verbosity, expected_type=type_hints["verbosity"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_management_logger_id": api_management_logger_id,
            "api_management_name": api_management_name,
            "identifier": identifier,
            "resource_group_name": resource_group_name,
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
        if always_log_errors is not None:
            self._values["always_log_errors"] = always_log_errors
        if backend_request is not None:
            self._values["backend_request"] = backend_request
        if backend_response is not None:
            self._values["backend_response"] = backend_response
        if frontend_request is not None:
            self._values["frontend_request"] = frontend_request
        if frontend_response is not None:
            self._values["frontend_response"] = frontend_response
        if http_correlation_protocol is not None:
            self._values["http_correlation_protocol"] = http_correlation_protocol
        if id is not None:
            self._values["id"] = id
        if log_client_ip is not None:
            self._values["log_client_ip"] = log_client_ip
        if operation_name_format is not None:
            self._values["operation_name_format"] = operation_name_format
        if sampling_percentage is not None:
            self._values["sampling_percentage"] = sampling_percentage
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if verbosity is not None:
            self._values["verbosity"] = verbosity

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
    def api_management_logger_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#api_management_logger_id ApiManagementDiagnostic#api_management_logger_id}.'''
        result = self._values.get("api_management_logger_id")
        assert result is not None, "Required property 'api_management_logger_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_management_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#api_management_name ApiManagementDiagnostic#api_management_name}.'''
        result = self._values.get("api_management_name")
        assert result is not None, "Required property 'api_management_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#identifier ApiManagementDiagnostic#identifier}.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#resource_group_name ApiManagementDiagnostic#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def always_log_errors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#always_log_errors ApiManagementDiagnostic#always_log_errors}.'''
        result = self._values.get("always_log_errors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def backend_request(self) -> typing.Optional[ApiManagementDiagnosticBackendRequest]:
        '''backend_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#backend_request ApiManagementDiagnostic#backend_request}
        '''
        result = self._values.get("backend_request")
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendRequest], result)

    @builtins.property
    def backend_response(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticBackendResponse]:
        '''backend_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#backend_response ApiManagementDiagnostic#backend_response}
        '''
        result = self._values.get("backend_response")
        return typing.cast(typing.Optional[ApiManagementDiagnosticBackendResponse], result)

    @builtins.property
    def frontend_request(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticFrontendRequest"]:
        '''frontend_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#frontend_request ApiManagementDiagnostic#frontend_request}
        '''
        result = self._values.get("frontend_request")
        return typing.cast(typing.Optional["ApiManagementDiagnosticFrontendRequest"], result)

    @builtins.property
    def frontend_response(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticFrontendResponse"]:
        '''frontend_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#frontend_response ApiManagementDiagnostic#frontend_response}
        '''
        result = self._values.get("frontend_response")
        return typing.cast(typing.Optional["ApiManagementDiagnosticFrontendResponse"], result)

    @builtins.property
    def http_correlation_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#http_correlation_protocol ApiManagementDiagnostic#http_correlation_protocol}.'''
        result = self._values.get("http_correlation_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#id ApiManagementDiagnostic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_client_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#log_client_ip ApiManagementDiagnostic#log_client_ip}.'''
        result = self._values.get("log_client_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operation_name_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#operation_name_format ApiManagementDiagnostic#operation_name_format}.'''
        result = self._values.get("operation_name_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sampling_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#sampling_percentage ApiManagementDiagnostic#sampling_percentage}.'''
        result = self._values.get("sampling_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementDiagnosticTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#timeouts ApiManagementDiagnostic#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementDiagnosticTimeouts"], result)

    @builtins.property
    def verbosity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#verbosity ApiManagementDiagnostic#verbosity}.'''
        result = self._values.get("verbosity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequest",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementDiagnosticFrontendRequest:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementDiagnosticFrontendRequestDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequest.__init__)
            check_type(argname="argument body_bytes", value=body_bytes, expected_type=type_hints["body_bytes"])
            check_type(argname="argument data_masking", value=data_masking, expected_type=type_hints["data_masking"])
            check_type(argname="argument headers_to_log", value=headers_to_log, expected_type=type_hints["headers_to_log"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body_bytes is not None:
            self._values["body_bytes"] = body_bytes
        if data_masking is not None:
            self._values["data_masking"] = data_masking
        if headers_to_log is not None:
            self._values["headers_to_log"] = headers_to_log

    @builtins.property
    def body_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticFrontendRequestDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementDiagnosticFrontendRequestDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementDiagnosticFrontendRequestDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticFrontendRequestDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMasking.__init__)
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument query_params", value=query_params, expected_type=type_hints["query_params"])
        self._values: typing.Dict[str, typing.Any] = {}
        if headers is not None:
            self._values["headers"] = headers
        if query_params is not None:
            self._values["query_params"] = query_params

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendRequestDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendRequestDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendRequestDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticFrontendRequestDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendRequestDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference.put_query_params)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryParams", [value]))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetQueryParams")
    def reset_query_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryParams", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList:
        return typing.cast(ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList":
        return typing.cast("ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticFrontendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticFrontendRequestDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticFrontendRequestDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendRequestOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        value = ApiManagementDiagnosticFrontendRequestDataMasking(
            headers=headers, query_params=query_params
        )

        return typing.cast(None, jsii.invoke(self, "putDataMasking", [value]))

    @jsii.member(jsii_name="resetBodyBytes")
    def reset_body_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodyBytes", []))

    @jsii.member(jsii_name="resetDataMasking")
    def reset_data_masking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataMasking", []))

    @jsii.member(jsii_name="resetHeadersToLog")
    def reset_headers_to_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeadersToLog", []))

    @builtins.property
    @jsii.member(jsii_name="dataMasking")
    def data_masking(
        self,
    ) -> ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference:
        return typing.cast(ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticFrontendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticFrontendRequestDataMasking], jsii.get(self, "dataMaskingInput"))

    @builtins.property
    @jsii.member(jsii_name="headersToLogInput")
    def headers_to_log_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersToLogInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytes")
    def body_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bodyBytes"))

    @body_bytes.setter
    def body_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiManagementDiagnosticFrontendRequest]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticFrontendRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticFrontendRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponse",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementDiagnosticFrontendResponse:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementDiagnosticFrontendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementDiagnosticFrontendResponseDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponse.__init__)
            check_type(argname="argument body_bytes", value=body_bytes, expected_type=type_hints["body_bytes"])
            check_type(argname="argument data_masking", value=data_masking, expected_type=type_hints["data_masking"])
            check_type(argname="argument headers_to_log", value=headers_to_log, expected_type=type_hints["headers_to_log"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body_bytes is not None:
            self._values["body_bytes"] = body_bytes
        if data_masking is not None:
            self._values["data_masking"] = data_masking
        if headers_to_log is not None:
            self._values["headers_to_log"] = headers_to_log

    @builtins.property
    def body_bytes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#body_bytes ApiManagementDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementDiagnosticFrontendResponseDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#data_masking ApiManagementDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementDiagnosticFrontendResponseDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers_to_log ApiManagementDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementDiagnosticFrontendResponseDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticFrontendResponseDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMasking.__init__)
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument query_params", value=query_params, expected_type=type_hints["query_params"])
        self._values: typing.Dict[str, typing.Any] = {}
        if headers is not None:
            self._values["headers"] = headers
        if query_params is not None:
            self._values["query_params"] = query_params

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendResponseDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendResponseDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendResponseDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticFrontendResponseDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendResponseDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference.put_query_params)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryParams", [value]))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetQueryParams")
    def reset_query_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryParams", []))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList:
        return typing.cast(ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList":
        return typing.cast("ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticFrontendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticFrontendResponseDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticFrontendResponseDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#mode ApiManagementDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#value ApiManagementDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementDiagnosticFrontendResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticFrontendResponseOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticFrontendResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#headers ApiManagementDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#query_params ApiManagementDiagnostic#query_params}
        '''
        value = ApiManagementDiagnosticFrontendResponseDataMasking(
            headers=headers, query_params=query_params
        )

        return typing.cast(None, jsii.invoke(self, "putDataMasking", [value]))

    @jsii.member(jsii_name="resetBodyBytes")
    def reset_body_bytes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodyBytes", []))

    @jsii.member(jsii_name="resetDataMasking")
    def reset_data_masking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataMasking", []))

    @jsii.member(jsii_name="resetHeadersToLog")
    def reset_headers_to_log(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeadersToLog", []))

    @builtins.property
    @jsii.member(jsii_name="dataMasking")
    def data_masking(
        self,
    ) -> ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference:
        return typing.cast(ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticFrontendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticFrontendResponseDataMasking], jsii.get(self, "dataMaskingInput"))

    @builtins.property
    @jsii.member(jsii_name="headersToLogInput")
    def headers_to_log_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersToLogInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytes")
    def body_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "bodyBytes"))

    @body_bytes.setter
    def body_bytes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementDiagnosticFrontendResponse]:
        return typing.cast(typing.Optional[ApiManagementDiagnosticFrontendResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementDiagnosticFrontendResponse],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticFrontendResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementDiagnosticTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#create ApiManagementDiagnostic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#delete ApiManagementDiagnostic#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#read ApiManagementDiagnostic#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#update ApiManagementDiagnostic#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementDiagnosticTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#create ApiManagementDiagnostic#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#delete ApiManagementDiagnostic#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#read ApiManagementDiagnostic#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_diagnostic#update ApiManagementDiagnostic#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementDiagnosticTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementDiagnosticTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementDiagnostic.ApiManagementDiagnosticTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementDiagnosticTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementDiagnosticTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementDiagnosticTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementDiagnosticTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementDiagnosticTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagementDiagnostic",
    "ApiManagementDiagnosticBackendRequest",
    "ApiManagementDiagnosticBackendRequestDataMasking",
    "ApiManagementDiagnosticBackendRequestDataMaskingHeaders",
    "ApiManagementDiagnosticBackendRequestDataMaskingHeadersList",
    "ApiManagementDiagnosticBackendRequestDataMaskingHeadersOutputReference",
    "ApiManagementDiagnosticBackendRequestDataMaskingOutputReference",
    "ApiManagementDiagnosticBackendRequestDataMaskingQueryParams",
    "ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsList",
    "ApiManagementDiagnosticBackendRequestDataMaskingQueryParamsOutputReference",
    "ApiManagementDiagnosticBackendRequestOutputReference",
    "ApiManagementDiagnosticBackendResponse",
    "ApiManagementDiagnosticBackendResponseDataMasking",
    "ApiManagementDiagnosticBackendResponseDataMaskingHeaders",
    "ApiManagementDiagnosticBackendResponseDataMaskingHeadersList",
    "ApiManagementDiagnosticBackendResponseDataMaskingHeadersOutputReference",
    "ApiManagementDiagnosticBackendResponseDataMaskingOutputReference",
    "ApiManagementDiagnosticBackendResponseDataMaskingQueryParams",
    "ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsList",
    "ApiManagementDiagnosticBackendResponseDataMaskingQueryParamsOutputReference",
    "ApiManagementDiagnosticBackendResponseOutputReference",
    "ApiManagementDiagnosticConfig",
    "ApiManagementDiagnosticFrontendRequest",
    "ApiManagementDiagnosticFrontendRequestDataMasking",
    "ApiManagementDiagnosticFrontendRequestDataMaskingHeaders",
    "ApiManagementDiagnosticFrontendRequestDataMaskingHeadersList",
    "ApiManagementDiagnosticFrontendRequestDataMaskingHeadersOutputReference",
    "ApiManagementDiagnosticFrontendRequestDataMaskingOutputReference",
    "ApiManagementDiagnosticFrontendRequestDataMaskingQueryParams",
    "ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsList",
    "ApiManagementDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference",
    "ApiManagementDiagnosticFrontendRequestOutputReference",
    "ApiManagementDiagnosticFrontendResponse",
    "ApiManagementDiagnosticFrontendResponseDataMasking",
    "ApiManagementDiagnosticFrontendResponseDataMaskingHeaders",
    "ApiManagementDiagnosticFrontendResponseDataMaskingHeadersList",
    "ApiManagementDiagnosticFrontendResponseDataMaskingHeadersOutputReference",
    "ApiManagementDiagnosticFrontendResponseDataMaskingOutputReference",
    "ApiManagementDiagnosticFrontendResponseDataMaskingQueryParams",
    "ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsList",
    "ApiManagementDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference",
    "ApiManagementDiagnosticFrontendResponseOutputReference",
    "ApiManagementDiagnosticTimeouts",
    "ApiManagementDiagnosticTimeoutsOutputReference",
]

publication.publish()
