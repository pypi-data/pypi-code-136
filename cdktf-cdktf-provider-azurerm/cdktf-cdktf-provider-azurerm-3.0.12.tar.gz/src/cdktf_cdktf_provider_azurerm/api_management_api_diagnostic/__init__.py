'''
# `azurerm_api_management_api_diagnostic`

Refer to the Terraform Registory for docs: [`azurerm_api_management_api_diagnostic`](https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic).
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


class ApiManagementApiDiagnostic(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnostic",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic azurerm_api_management_api_diagnostic}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_management_logger_id: builtins.str,
        api_management_name: builtins.str,
        api_name: builtins.str,
        identifier: builtins.str,
        resource_group_name: builtins.str,
        always_log_errors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backend_request: typing.Optional[typing.Union["ApiManagementApiDiagnosticBackendRequest", typing.Dict[str, typing.Any]]] = None,
        backend_response: typing.Optional[typing.Union["ApiManagementApiDiagnosticBackendResponse", typing.Dict[str, typing.Any]]] = None,
        frontend_request: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendRequest", typing.Dict[str, typing.Any]]] = None,
        frontend_response: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendResponse", typing.Dict[str, typing.Any]]] = None,
        http_correlation_protocol: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_client_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operation_name_format: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementApiDiagnosticTimeouts", typing.Dict[str, typing.Any]]] = None,
        verbosity: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic azurerm_api_management_api_diagnostic} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_management_logger_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_management_logger_id ApiManagementApiDiagnostic#api_management_logger_id}.
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_management_name ApiManagementApiDiagnostic#api_management_name}.
        :param api_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_name ApiManagementApiDiagnostic#api_name}.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#identifier ApiManagementApiDiagnostic#identifier}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#resource_group_name ApiManagementApiDiagnostic#resource_group_name}.
        :param always_log_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#always_log_errors ApiManagementApiDiagnostic#always_log_errors}.
        :param backend_request: backend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#backend_request ApiManagementApiDiagnostic#backend_request}
        :param backend_response: backend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#backend_response ApiManagementApiDiagnostic#backend_response}
        :param frontend_request: frontend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#frontend_request ApiManagementApiDiagnostic#frontend_request}
        :param frontend_response: frontend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#frontend_response ApiManagementApiDiagnostic#frontend_response}
        :param http_correlation_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#http_correlation_protocol ApiManagementApiDiagnostic#http_correlation_protocol}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#id ApiManagementApiDiagnostic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_client_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#log_client_ip ApiManagementApiDiagnostic#log_client_ip}.
        :param operation_name_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#operation_name_format ApiManagementApiDiagnostic#operation_name_format}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#sampling_percentage ApiManagementApiDiagnostic#sampling_percentage}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#timeouts ApiManagementApiDiagnostic#timeouts}
        :param verbosity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#verbosity ApiManagementApiDiagnostic#verbosity}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnostic.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiManagementApiDiagnosticConfig(
            api_management_logger_id=api_management_logger_id,
            api_management_name=api_management_name,
            api_name=api_name,
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
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticBackendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        value = ApiManagementApiDiagnosticBackendRequest(
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
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticBackendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        value = ApiManagementApiDiagnosticBackendResponse(
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
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        value = ApiManagementApiDiagnosticFrontendRequest(
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
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        value = ApiManagementApiDiagnosticFrontendResponse(
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#create ApiManagementApiDiagnostic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#delete ApiManagementApiDiagnostic#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#read ApiManagementApiDiagnostic#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#update ApiManagementApiDiagnostic#update}.
        '''
        value = ApiManagementApiDiagnosticTimeouts(
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
    def backend_request(
        self,
    ) -> "ApiManagementApiDiagnosticBackendRequestOutputReference":
        return typing.cast("ApiManagementApiDiagnosticBackendRequestOutputReference", jsii.get(self, "backendRequest"))

    @builtins.property
    @jsii.member(jsii_name="backendResponse")
    def backend_response(
        self,
    ) -> "ApiManagementApiDiagnosticBackendResponseOutputReference":
        return typing.cast("ApiManagementApiDiagnosticBackendResponseOutputReference", jsii.get(self, "backendResponse"))

    @builtins.property
    @jsii.member(jsii_name="frontendRequest")
    def frontend_request(
        self,
    ) -> "ApiManagementApiDiagnosticFrontendRequestOutputReference":
        return typing.cast("ApiManagementApiDiagnosticFrontendRequestOutputReference", jsii.get(self, "frontendRequest"))

    @builtins.property
    @jsii.member(jsii_name="frontendResponse")
    def frontend_response(
        self,
    ) -> "ApiManagementApiDiagnosticFrontendResponseOutputReference":
        return typing.cast("ApiManagementApiDiagnosticFrontendResponseOutputReference", jsii.get(self, "frontendResponse"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ApiManagementApiDiagnosticTimeoutsOutputReference":
        return typing.cast("ApiManagementApiDiagnosticTimeoutsOutputReference", jsii.get(self, "timeouts"))

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
    @jsii.member(jsii_name="apiNameInput")
    def api_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiNameInput"))

    @builtins.property
    @jsii.member(jsii_name="backendRequestInput")
    def backend_request_input(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticBackendRequest"]:
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticBackendRequest"], jsii.get(self, "backendRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="backendResponseInput")
    def backend_response_input(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticBackendResponse"]:
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticBackendResponse"], jsii.get(self, "backendResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendRequestInput")
    def frontend_request_input(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticFrontendRequest"]:
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticFrontendRequest"], jsii.get(self, "frontendRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendResponseInput")
    def frontend_response_input(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticFrontendResponse"]:
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticFrontendResponse"], jsii.get(self, "frontendResponseInput"))

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
    ) -> typing.Optional[typing.Union["ApiManagementApiDiagnosticTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ApiManagementApiDiagnosticTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "always_log_errors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysLogErrors", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementLoggerId")
    def api_management_logger_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementLoggerId"))

    @api_management_logger_id.setter
    def api_management_logger_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "api_management_logger_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementLoggerId", value)

    @builtins.property
    @jsii.member(jsii_name="apiManagementName")
    def api_management_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiManagementName"))

    @api_management_name.setter
    def api_management_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "api_management_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiManagementName", value)

    @builtins.property
    @jsii.member(jsii_name="apiName")
    def api_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiName"))

    @api_name.setter
    def api_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "api_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiName", value)

    @builtins.property
    @jsii.member(jsii_name="httpCorrelationProtocol")
    def http_correlation_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpCorrelationProtocol"))

    @http_correlation_protocol.setter
    def http_correlation_protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "http_correlation_protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpCorrelationProtocol", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "identifier").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "log_client_ip").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logClientIp", value)

    @builtins.property
    @jsii.member(jsii_name="operationNameFormat")
    def operation_name_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operationNameFormat"))

    @operation_name_format.setter
    def operation_name_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "operation_name_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationNameFormat", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="samplingPercentage")
    def sampling_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "samplingPercentage"))

    @sampling_percentage.setter
    def sampling_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "sampling_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="verbosity")
    def verbosity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verbosity"))

    @verbosity.setter
    def verbosity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnostic, "verbosity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verbosity", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequest",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementApiDiagnosticBackendRequest:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticBackendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementApiDiagnosticBackendRequestDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequest.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticBackendRequestDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticBackendRequestDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementApiDiagnosticBackendRequestDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMasking.__init__)
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendRequestDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference.put_query_params)
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
    def headers(self) -> ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList:
        return typing.cast(ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList":
        return typing.cast("ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendRequestDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticBackendRequestDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendRequestOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        value = ApiManagementApiDiagnosticBackendRequestDataMasking(
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
    ) -> ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference:
        return typing.cast(ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendRequestDataMasking], jsii.get(self, "dataMaskingInput"))

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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendRequest]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticBackendRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponse",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementApiDiagnosticBackendResponse:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticBackendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementApiDiagnosticBackendResponseDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponse.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticBackendResponseDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticBackendResponseDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementApiDiagnosticBackendResponseDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMasking.__init__)
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendResponseDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference.put_query_params)
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
    def headers(
        self,
    ) -> ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList:
        return typing.cast(ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList":
        return typing.cast("ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendResponseDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticBackendResponseDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticBackendResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticBackendResponseOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticBackendResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        value = ApiManagementApiDiagnosticBackendResponseDataMasking(
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
    ) -> ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference:
        return typing.cast(ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendResponseDataMasking], jsii.get(self, "dataMaskingInput"))

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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendResponse]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticBackendResponse],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticBackendResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticConfig",
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
        "api_name": "apiName",
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
class ApiManagementApiDiagnosticConfig(cdktf.TerraformMetaArguments):
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
        api_name: builtins.str,
        identifier: builtins.str,
        resource_group_name: builtins.str,
        always_log_errors: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        backend_request: typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendRequest, typing.Dict[str, typing.Any]]] = None,
        backend_response: typing.Optional[typing.Union[ApiManagementApiDiagnosticBackendResponse, typing.Dict[str, typing.Any]]] = None,
        frontend_request: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendRequest", typing.Dict[str, typing.Any]]] = None,
        frontend_response: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendResponse", typing.Dict[str, typing.Any]]] = None,
        http_correlation_protocol: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        log_client_ip: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operation_name_format: typing.Optional[builtins.str] = None,
        sampling_percentage: typing.Optional[jsii.Number] = None,
        timeouts: typing.Optional[typing.Union["ApiManagementApiDiagnosticTimeouts", typing.Dict[str, typing.Any]]] = None,
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
        :param api_management_logger_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_management_logger_id ApiManagementApiDiagnostic#api_management_logger_id}.
        :param api_management_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_management_name ApiManagementApiDiagnostic#api_management_name}.
        :param api_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_name ApiManagementApiDiagnostic#api_name}.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#identifier ApiManagementApiDiagnostic#identifier}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#resource_group_name ApiManagementApiDiagnostic#resource_group_name}.
        :param always_log_errors: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#always_log_errors ApiManagementApiDiagnostic#always_log_errors}.
        :param backend_request: backend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#backend_request ApiManagementApiDiagnostic#backend_request}
        :param backend_response: backend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#backend_response ApiManagementApiDiagnostic#backend_response}
        :param frontend_request: frontend_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#frontend_request ApiManagementApiDiagnostic#frontend_request}
        :param frontend_response: frontend_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#frontend_response ApiManagementApiDiagnostic#frontend_response}
        :param http_correlation_protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#http_correlation_protocol ApiManagementApiDiagnostic#http_correlation_protocol}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#id ApiManagementApiDiagnostic#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_client_ip: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#log_client_ip ApiManagementApiDiagnostic#log_client_ip}.
        :param operation_name_format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#operation_name_format ApiManagementApiDiagnostic#operation_name_format}.
        :param sampling_percentage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#sampling_percentage ApiManagementApiDiagnostic#sampling_percentage}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#timeouts ApiManagementApiDiagnostic#timeouts}
        :param verbosity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#verbosity ApiManagementApiDiagnostic#verbosity}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(backend_request, dict):
            backend_request = ApiManagementApiDiagnosticBackendRequest(**backend_request)
        if isinstance(backend_response, dict):
            backend_response = ApiManagementApiDiagnosticBackendResponse(**backend_response)
        if isinstance(frontend_request, dict):
            frontend_request = ApiManagementApiDiagnosticFrontendRequest(**frontend_request)
        if isinstance(frontend_response, dict):
            frontend_response = ApiManagementApiDiagnosticFrontendResponse(**frontend_response)
        if isinstance(timeouts, dict):
            timeouts = ApiManagementApiDiagnosticTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_management_logger_id", value=api_management_logger_id, expected_type=type_hints["api_management_logger_id"])
            check_type(argname="argument api_management_name", value=api_management_name, expected_type=type_hints["api_management_name"])
            check_type(argname="argument api_name", value=api_name, expected_type=type_hints["api_name"])
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
            "api_name": api_name,
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_management_logger_id ApiManagementApiDiagnostic#api_management_logger_id}.'''
        result = self._values.get("api_management_logger_id")
        assert result is not None, "Required property 'api_management_logger_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_management_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_management_name ApiManagementApiDiagnostic#api_management_name}.'''
        result = self._values.get("api_management_name")
        assert result is not None, "Required property 'api_management_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#api_name ApiManagementApiDiagnostic#api_name}.'''
        result = self._values.get("api_name")
        assert result is not None, "Required property 'api_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#identifier ApiManagementApiDiagnostic#identifier}.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#resource_group_name ApiManagementApiDiagnostic#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def always_log_errors(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#always_log_errors ApiManagementApiDiagnostic#always_log_errors}.'''
        result = self._values.get("always_log_errors")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def backend_request(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendRequest]:
        '''backend_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#backend_request ApiManagementApiDiagnostic#backend_request}
        '''
        result = self._values.get("backend_request")
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendRequest], result)

    @builtins.property
    def backend_response(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticBackendResponse]:
        '''backend_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#backend_response ApiManagementApiDiagnostic#backend_response}
        '''
        result = self._values.get("backend_response")
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticBackendResponse], result)

    @builtins.property
    def frontend_request(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticFrontendRequest"]:
        '''frontend_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#frontend_request ApiManagementApiDiagnostic#frontend_request}
        '''
        result = self._values.get("frontend_request")
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticFrontendRequest"], result)

    @builtins.property
    def frontend_response(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticFrontendResponse"]:
        '''frontend_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#frontend_response ApiManagementApiDiagnostic#frontend_response}
        '''
        result = self._values.get("frontend_response")
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticFrontendResponse"], result)

    @builtins.property
    def http_correlation_protocol(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#http_correlation_protocol ApiManagementApiDiagnostic#http_correlation_protocol}.'''
        result = self._values.get("http_correlation_protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#id ApiManagementApiDiagnostic#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_client_ip(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#log_client_ip ApiManagementApiDiagnostic#log_client_ip}.'''
        result = self._values.get("log_client_ip")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operation_name_format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#operation_name_format ApiManagementApiDiagnostic#operation_name_format}.'''
        result = self._values.get("operation_name_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sampling_percentage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#sampling_percentage ApiManagementApiDiagnostic#sampling_percentage}.'''
        result = self._values.get("sampling_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ApiManagementApiDiagnosticTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#timeouts ApiManagementApiDiagnostic#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticTimeouts"], result)

    @builtins.property
    def verbosity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#verbosity ApiManagementApiDiagnostic#verbosity}.'''
        result = self._values.get("verbosity")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequest",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementApiDiagnosticFrontendRequest:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendRequestDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementApiDiagnosticFrontendRequestDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequest.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticFrontendRequestDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticFrontendRequestDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementApiDiagnosticFrontendRequestDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMasking.__init__)
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendRequestDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference.put_query_params)
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
    def headers(
        self,
    ) -> ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList:
        return typing.cast(ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList":
        return typing.cast("ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticFrontendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticFrontendRequestDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticFrontendRequestDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendRequestOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        value = ApiManagementApiDiagnosticFrontendRequestDataMasking(
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
    ) -> ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference:
        return typing.cast(ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticFrontendRequestDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticFrontendRequestDataMasking], jsii.get(self, "dataMaskingInput"))

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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticFrontendRequest]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticFrontendRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticFrontendRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponse",
    jsii_struct_bases=[],
    name_mapping={
        "body_bytes": "bodyBytes",
        "data_masking": "dataMasking",
        "headers_to_log": "headersToLog",
    },
)
class ApiManagementApiDiagnosticFrontendResponse:
    def __init__(
        self,
        *,
        body_bytes: typing.Optional[jsii.Number] = None,
        data_masking: typing.Optional[typing.Union["ApiManagementApiDiagnosticFrontendResponseDataMasking", typing.Dict[str, typing.Any]]] = None,
        headers_to_log: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param body_bytes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.
        :param data_masking: data_masking block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        :param headers_to_log: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.
        '''
        if isinstance(data_masking, dict):
            data_masking = ApiManagementApiDiagnosticFrontendResponseDataMasking(**data_masking)
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponse.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#body_bytes ApiManagementApiDiagnostic#body_bytes}.'''
        result = self._values.get("body_bytes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def data_masking(
        self,
    ) -> typing.Optional["ApiManagementApiDiagnosticFrontendResponseDataMasking"]:
        '''data_masking block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#data_masking ApiManagementApiDiagnostic#data_masking}
        '''
        result = self._values.get("data_masking")
        return typing.cast(typing.Optional["ApiManagementApiDiagnosticFrontendResponseDataMasking"], result)

    @builtins.property
    def headers_to_log(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers_to_log ApiManagementApiDiagnostic#headers_to_log}.'''
        result = self._values.get("headers_to_log")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMasking",
    jsii_struct_bases=[],
    name_mapping={"headers": "headers", "query_params": "queryParams"},
)
class ApiManagementApiDiagnosticFrontendResponseDataMasking:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders", typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMasking.__init__)
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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders"]]]:
        '''headers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders"]]], result)

    @builtins.property
    def query_params(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams"]]]:
        '''query_params block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        result = self._values.get("query_params")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendResponseDataMasking(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putHeaders")
    def put_headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference.put_headers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeaders", [value]))

    @jsii.member(jsii_name="putQueryParams")
    def put_query_params(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference.put_query_params)
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
    def headers(
        self,
    ) -> ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList:
        return typing.cast(ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList, jsii.get(self, "headers"))

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(
        self,
    ) -> "ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList":
        return typing.cast("ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList", jsii.get(self, "queryParams"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams"]]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticFrontendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticFrontendResponseDataMasking], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticFrontendResponseDataMasking],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "value": "value"},
)
class ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams:
    def __init__(self, *, mode: builtins.str, value: builtins.str) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
            "value": value,
        }

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#mode ApiManagementApiDiagnostic#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#value ApiManagementApiDiagnostic#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiManagementApiDiagnosticFrontendResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticFrontendResponseOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticFrontendResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataMasking")
    def put_data_masking(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders, typing.Dict[str, typing.Any]]]]] = None,
        query_params: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param headers: headers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#headers ApiManagementApiDiagnostic#headers}
        :param query_params: query_params block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#query_params ApiManagementApiDiagnostic#query_params}
        '''
        value = ApiManagementApiDiagnosticFrontendResponseDataMasking(
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
    ) -> ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference:
        return typing.cast(ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference, jsii.get(self, "dataMasking"))

    @builtins.property
    @jsii.member(jsii_name="bodyBytesInput")
    def body_bytes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "bodyBytesInput"))

    @builtins.property
    @jsii.member(jsii_name="dataMaskingInput")
    def data_masking_input(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticFrontendResponseDataMasking]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticFrontendResponseDataMasking], jsii.get(self, "dataMaskingInput"))

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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseOutputReference, "body_bytes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyBytes", value)

    @builtins.property
    @jsii.member(jsii_name="headersToLog")
    def headers_to_log(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headersToLog"))

    @headers_to_log.setter
    def headers_to_log(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseOutputReference, "headers_to_log").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headersToLog", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ApiManagementApiDiagnosticFrontendResponse]:
        return typing.cast(typing.Optional[ApiManagementApiDiagnosticFrontendResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiManagementApiDiagnosticFrontendResponse],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticFrontendResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class ApiManagementApiDiagnosticTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#create ApiManagementApiDiagnostic#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#delete ApiManagementApiDiagnostic#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#read ApiManagementApiDiagnostic#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#update ApiManagementApiDiagnostic#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#create ApiManagementApiDiagnostic#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#delete ApiManagementApiDiagnostic#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#read ApiManagementApiDiagnostic#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/api_management_api_diagnostic#update ApiManagementApiDiagnostic#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiManagementApiDiagnosticTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiManagementApiDiagnosticTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.apiManagementApiDiagnostic.ApiManagementApiDiagnosticTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ApiManagementApiDiagnosticTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiManagementApiDiagnosticTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiManagementApiDiagnosticTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiManagementApiDiagnosticTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiManagementApiDiagnosticTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiManagementApiDiagnostic",
    "ApiManagementApiDiagnosticBackendRequest",
    "ApiManagementApiDiagnosticBackendRequestDataMasking",
    "ApiManagementApiDiagnosticBackendRequestDataMaskingHeaders",
    "ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersList",
    "ApiManagementApiDiagnosticBackendRequestDataMaskingHeadersOutputReference",
    "ApiManagementApiDiagnosticBackendRequestDataMaskingOutputReference",
    "ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParams",
    "ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsList",
    "ApiManagementApiDiagnosticBackendRequestDataMaskingQueryParamsOutputReference",
    "ApiManagementApiDiagnosticBackendRequestOutputReference",
    "ApiManagementApiDiagnosticBackendResponse",
    "ApiManagementApiDiagnosticBackendResponseDataMasking",
    "ApiManagementApiDiagnosticBackendResponseDataMaskingHeaders",
    "ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersList",
    "ApiManagementApiDiagnosticBackendResponseDataMaskingHeadersOutputReference",
    "ApiManagementApiDiagnosticBackendResponseDataMaskingOutputReference",
    "ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParams",
    "ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsList",
    "ApiManagementApiDiagnosticBackendResponseDataMaskingQueryParamsOutputReference",
    "ApiManagementApiDiagnosticBackendResponseOutputReference",
    "ApiManagementApiDiagnosticConfig",
    "ApiManagementApiDiagnosticFrontendRequest",
    "ApiManagementApiDiagnosticFrontendRequestDataMasking",
    "ApiManagementApiDiagnosticFrontendRequestDataMaskingHeaders",
    "ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersList",
    "ApiManagementApiDiagnosticFrontendRequestDataMaskingHeadersOutputReference",
    "ApiManagementApiDiagnosticFrontendRequestDataMaskingOutputReference",
    "ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParams",
    "ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsList",
    "ApiManagementApiDiagnosticFrontendRequestDataMaskingQueryParamsOutputReference",
    "ApiManagementApiDiagnosticFrontendRequestOutputReference",
    "ApiManagementApiDiagnosticFrontendResponse",
    "ApiManagementApiDiagnosticFrontendResponseDataMasking",
    "ApiManagementApiDiagnosticFrontendResponseDataMaskingHeaders",
    "ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersList",
    "ApiManagementApiDiagnosticFrontendResponseDataMaskingHeadersOutputReference",
    "ApiManagementApiDiagnosticFrontendResponseDataMaskingOutputReference",
    "ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParams",
    "ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsList",
    "ApiManagementApiDiagnosticFrontendResponseDataMaskingQueryParamsOutputReference",
    "ApiManagementApiDiagnosticFrontendResponseOutputReference",
    "ApiManagementApiDiagnosticTimeouts",
    "ApiManagementApiDiagnosticTimeoutsOutputReference",
]

publication.publish()
