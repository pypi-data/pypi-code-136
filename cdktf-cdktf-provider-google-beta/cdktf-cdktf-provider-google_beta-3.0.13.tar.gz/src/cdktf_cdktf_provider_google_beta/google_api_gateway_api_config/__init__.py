'''
# `google_api_gateway_api_config`

Refer to the Terraform Registory for docs: [`google_api_gateway_api_config`](https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config).
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


class GoogleApiGatewayApiConfigA(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigA",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config google_api_gateway_api_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api: builtins.str,
        api_config_id: typing.Optional[builtins.str] = None,
        api_config_id_prefix: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        gateway_config: typing.Optional[typing.Union["GoogleApiGatewayApiConfigGatewayConfig", typing.Dict[str, typing.Any]]] = None,
        grpc_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigGrpcServices", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        managed_service_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigManagedServiceConfigs", typing.Dict[str, typing.Any]]]]] = None,
        openapi_documents: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigOpenapiDocuments", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleApiGatewayApiConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config google_api_gateway_api_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api: The API to attach the config to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api GoogleApiGatewayApiConfigA#api}
        :param api_config_id: Identifier to assign to the API Config. Must be unique within scope of the parent resource(api). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api_config_id GoogleApiGatewayApiConfigA#api_config_id}
        :param api_config_id_prefix: Creates a unique name beginning with the specified prefix. If this and api_config_id are unspecified, a random value is chosen for the name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api_config_id_prefix GoogleApiGatewayApiConfigA#api_config_id_prefix}
        :param display_name: A user-visible name for the API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#display_name GoogleApiGatewayApiConfigA#display_name}
        :param gateway_config: gateway_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#gateway_config GoogleApiGatewayApiConfigA#gateway_config}
        :param grpc_services: grpc_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#grpc_services GoogleApiGatewayApiConfigA#grpc_services}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#id GoogleApiGatewayApiConfigA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Resource labels to represent user-provided metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#labels GoogleApiGatewayApiConfigA#labels}
        :param managed_service_configs: managed_service_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#managed_service_configs GoogleApiGatewayApiConfigA#managed_service_configs}
        :param openapi_documents: openapi_documents block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#openapi_documents GoogleApiGatewayApiConfigA#openapi_documents}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#project GoogleApiGatewayApiConfigA#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#timeouts GoogleApiGatewayApiConfigA#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigA.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleApiGatewayApiConfigAConfig(
            api=api,
            api_config_id=api_config_id,
            api_config_id_prefix=api_config_id_prefix,
            display_name=display_name,
            gateway_config=gateway_config,
            grpc_services=grpc_services,
            id=id,
            labels=labels,
            managed_service_configs=managed_service_configs,
            openapi_documents=openapi_documents,
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

    @jsii.member(jsii_name="putGatewayConfig")
    def put_gateway_config(
        self,
        *,
        backend_config: typing.Union["GoogleApiGatewayApiConfigGatewayConfigBackendConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param backend_config: backend_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#backend_config GoogleApiGatewayApiConfigA#backend_config}
        '''
        value = GoogleApiGatewayApiConfigGatewayConfig(backend_config=backend_config)

        return typing.cast(None, jsii.invoke(self, "putGatewayConfig", [value]))

    @jsii.member(jsii_name="putGrpcServices")
    def put_grpc_services(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigGrpcServices", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigA.put_grpc_services)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGrpcServices", [value]))

    @jsii.member(jsii_name="putManagedServiceConfigs")
    def put_managed_service_configs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigManagedServiceConfigs", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigA.put_managed_service_configs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putManagedServiceConfigs", [value]))

    @jsii.member(jsii_name="putOpenapiDocuments")
    def put_openapi_documents(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigOpenapiDocuments", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigA.put_openapi_documents)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOpenapiDocuments", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#create GoogleApiGatewayApiConfigA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#delete GoogleApiGatewayApiConfigA#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#update GoogleApiGatewayApiConfigA#update}.
        '''
        value = GoogleApiGatewayApiConfigTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApiConfigId")
    def reset_api_config_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiConfigId", []))

    @jsii.member(jsii_name="resetApiConfigIdPrefix")
    def reset_api_config_id_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiConfigIdPrefix", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetGatewayConfig")
    def reset_gateway_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGatewayConfig", []))

    @jsii.member(jsii_name="resetGrpcServices")
    def reset_grpc_services(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGrpcServices", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetManagedServiceConfigs")
    def reset_managed_service_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagedServiceConfigs", []))

    @jsii.member(jsii_name="resetOpenapiDocuments")
    def reset_openapi_documents(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpenapiDocuments", []))

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
    @jsii.member(jsii_name="gatewayConfig")
    def gateway_config(self) -> "GoogleApiGatewayApiConfigGatewayConfigOutputReference":
        return typing.cast("GoogleApiGatewayApiConfigGatewayConfigOutputReference", jsii.get(self, "gatewayConfig"))

    @builtins.property
    @jsii.member(jsii_name="grpcServices")
    def grpc_services(self) -> "GoogleApiGatewayApiConfigGrpcServicesList":
        return typing.cast("GoogleApiGatewayApiConfigGrpcServicesList", jsii.get(self, "grpcServices"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceConfigs")
    def managed_service_configs(
        self,
    ) -> "GoogleApiGatewayApiConfigManagedServiceConfigsList":
        return typing.cast("GoogleApiGatewayApiConfigManagedServiceConfigsList", jsii.get(self, "managedServiceConfigs"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="openapiDocuments")
    def openapi_documents(self) -> "GoogleApiGatewayApiConfigOpenapiDocumentsList":
        return typing.cast("GoogleApiGatewayApiConfigOpenapiDocumentsList", jsii.get(self, "openapiDocuments"))

    @builtins.property
    @jsii.member(jsii_name="serviceConfigId")
    def service_config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceConfigId"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleApiGatewayApiConfigTimeoutsOutputReference":
        return typing.cast("GoogleApiGatewayApiConfigTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="apiConfigIdInput")
    def api_config_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiConfigIdInput"))

    @builtins.property
    @jsii.member(jsii_name="apiConfigIdPrefixInput")
    def api_config_id_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiConfigIdPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="apiInput")
    def api_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayConfigInput")
    def gateway_config_input(
        self,
    ) -> typing.Optional["GoogleApiGatewayApiConfigGatewayConfig"]:
        return typing.cast(typing.Optional["GoogleApiGatewayApiConfigGatewayConfig"], jsii.get(self, "gatewayConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="grpcServicesInput")
    def grpc_services_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServices"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServices"]]], jsii.get(self, "grpcServicesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="managedServiceConfigsInput")
    def managed_service_configs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigManagedServiceConfigs"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigManagedServiceConfigs"]]], jsii.get(self, "managedServiceConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="openapiDocumentsInput")
    def openapi_documents_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigOpenapiDocuments"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigOpenapiDocuments"]]], jsii.get(self, "openapiDocumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleApiGatewayApiConfigTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleApiGatewayApiConfigTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="api")
    def api(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "api"))

    @api.setter
    def api(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigA, "api").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "api", value)

    @builtins.property
    @jsii.member(jsii_name="apiConfigId")
    def api_config_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiConfigId"))

    @api_config_id.setter
    def api_config_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigA, "api_config_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiConfigId", value)

    @builtins.property
    @jsii.member(jsii_name="apiConfigIdPrefix")
    def api_config_id_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiConfigIdPrefix"))

    @api_config_id_prefix.setter
    def api_config_id_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigA, "api_config_id_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiConfigIdPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigA, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigA, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigA, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigA, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigAConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api": "api",
        "api_config_id": "apiConfigId",
        "api_config_id_prefix": "apiConfigIdPrefix",
        "display_name": "displayName",
        "gateway_config": "gatewayConfig",
        "grpc_services": "grpcServices",
        "id": "id",
        "labels": "labels",
        "managed_service_configs": "managedServiceConfigs",
        "openapi_documents": "openapiDocuments",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleApiGatewayApiConfigAConfig(cdktf.TerraformMetaArguments):
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
        api: builtins.str,
        api_config_id: typing.Optional[builtins.str] = None,
        api_config_id_prefix: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        gateway_config: typing.Optional[typing.Union["GoogleApiGatewayApiConfigGatewayConfig", typing.Dict[str, typing.Any]]] = None,
        grpc_services: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigGrpcServices", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        managed_service_configs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigManagedServiceConfigs", typing.Dict[str, typing.Any]]]]] = None,
        openapi_documents: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigOpenapiDocuments", typing.Dict[str, typing.Any]]]]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleApiGatewayApiConfigTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api: The API to attach the config to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api GoogleApiGatewayApiConfigA#api}
        :param api_config_id: Identifier to assign to the API Config. Must be unique within scope of the parent resource(api). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api_config_id GoogleApiGatewayApiConfigA#api_config_id}
        :param api_config_id_prefix: Creates a unique name beginning with the specified prefix. If this and api_config_id are unspecified, a random value is chosen for the name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api_config_id_prefix GoogleApiGatewayApiConfigA#api_config_id_prefix}
        :param display_name: A user-visible name for the API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#display_name GoogleApiGatewayApiConfigA#display_name}
        :param gateway_config: gateway_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#gateway_config GoogleApiGatewayApiConfigA#gateway_config}
        :param grpc_services: grpc_services block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#grpc_services GoogleApiGatewayApiConfigA#grpc_services}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#id GoogleApiGatewayApiConfigA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Resource labels to represent user-provided metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#labels GoogleApiGatewayApiConfigA#labels}
        :param managed_service_configs: managed_service_configs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#managed_service_configs GoogleApiGatewayApiConfigA#managed_service_configs}
        :param openapi_documents: openapi_documents block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#openapi_documents GoogleApiGatewayApiConfigA#openapi_documents}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#project GoogleApiGatewayApiConfigA#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#timeouts GoogleApiGatewayApiConfigA#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(gateway_config, dict):
            gateway_config = GoogleApiGatewayApiConfigGatewayConfig(**gateway_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleApiGatewayApiConfigTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigAConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument api_config_id", value=api_config_id, expected_type=type_hints["api_config_id"])
            check_type(argname="argument api_config_id_prefix", value=api_config_id_prefix, expected_type=type_hints["api_config_id_prefix"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument gateway_config", value=gateway_config, expected_type=type_hints["gateway_config"])
            check_type(argname="argument grpc_services", value=grpc_services, expected_type=type_hints["grpc_services"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument managed_service_configs", value=managed_service_configs, expected_type=type_hints["managed_service_configs"])
            check_type(argname="argument openapi_documents", value=openapi_documents, expected_type=type_hints["openapi_documents"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "api": api,
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
        if api_config_id is not None:
            self._values["api_config_id"] = api_config_id
        if api_config_id_prefix is not None:
            self._values["api_config_id_prefix"] = api_config_id_prefix
        if display_name is not None:
            self._values["display_name"] = display_name
        if gateway_config is not None:
            self._values["gateway_config"] = gateway_config
        if grpc_services is not None:
            self._values["grpc_services"] = grpc_services
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if managed_service_configs is not None:
            self._values["managed_service_configs"] = managed_service_configs
        if openapi_documents is not None:
            self._values["openapi_documents"] = openapi_documents
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
    def api(self) -> builtins.str:
        '''The API to attach the config to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api GoogleApiGatewayApiConfigA#api}
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_config_id(self) -> typing.Optional[builtins.str]:
        '''Identifier to assign to the API Config. Must be unique within scope of the parent resource(api).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api_config_id GoogleApiGatewayApiConfigA#api_config_id}
        '''
        result = self._values.get("api_config_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def api_config_id_prefix(self) -> typing.Optional[builtins.str]:
        '''Creates a unique name beginning with the specified prefix.

        If this and api_config_id are unspecified, a random value is chosen for the name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#api_config_id_prefix GoogleApiGatewayApiConfigA#api_config_id_prefix}
        '''
        result = self._values.get("api_config_id_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''A user-visible name for the API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#display_name GoogleApiGatewayApiConfigA#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_config(
        self,
    ) -> typing.Optional["GoogleApiGatewayApiConfigGatewayConfig"]:
        '''gateway_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#gateway_config GoogleApiGatewayApiConfigA#gateway_config}
        '''
        result = self._values.get("gateway_config")
        return typing.cast(typing.Optional["GoogleApiGatewayApiConfigGatewayConfig"], result)

    @builtins.property
    def grpc_services(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServices"]]]:
        '''grpc_services block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#grpc_services GoogleApiGatewayApiConfigA#grpc_services}
        '''
        result = self._values.get("grpc_services")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServices"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#id GoogleApiGatewayApiConfigA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Resource labels to represent user-provided metadata.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#labels GoogleApiGatewayApiConfigA#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def managed_service_configs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigManagedServiceConfigs"]]]:
        '''managed_service_configs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#managed_service_configs GoogleApiGatewayApiConfigA#managed_service_configs}
        '''
        result = self._values.get("managed_service_configs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigManagedServiceConfigs"]]], result)

    @builtins.property
    def openapi_documents(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigOpenapiDocuments"]]]:
        '''openapi_documents block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#openapi_documents GoogleApiGatewayApiConfigA#openapi_documents}
        '''
        result = self._values.get("openapi_documents")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigOpenapiDocuments"]]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#project GoogleApiGatewayApiConfigA#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleApiGatewayApiConfigTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#timeouts GoogleApiGatewayApiConfigA#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleApiGatewayApiConfigTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigAConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGatewayConfig",
    jsii_struct_bases=[],
    name_mapping={"backend_config": "backendConfig"},
)
class GoogleApiGatewayApiConfigGatewayConfig:
    def __init__(
        self,
        *,
        backend_config: typing.Union["GoogleApiGatewayApiConfigGatewayConfigBackendConfig", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param backend_config: backend_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#backend_config GoogleApiGatewayApiConfigA#backend_config}
        '''
        if isinstance(backend_config, dict):
            backend_config = GoogleApiGatewayApiConfigGatewayConfigBackendConfig(**backend_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGatewayConfig.__init__)
            check_type(argname="argument backend_config", value=backend_config, expected_type=type_hints["backend_config"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_config": backend_config,
        }

    @builtins.property
    def backend_config(self) -> "GoogleApiGatewayApiConfigGatewayConfigBackendConfig":
        '''backend_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#backend_config GoogleApiGatewayApiConfigA#backend_config}
        '''
        result = self._values.get("backend_config")
        assert result is not None, "Required property 'backend_config' is missing"
        return typing.cast("GoogleApiGatewayApiConfigGatewayConfigBackendConfig", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigGatewayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGatewayConfigBackendConfig",
    jsii_struct_bases=[],
    name_mapping={"google_service_account": "googleServiceAccount"},
)
class GoogleApiGatewayApiConfigGatewayConfigBackendConfig:
    def __init__(self, *, google_service_account: builtins.str) -> None:
        '''
        :param google_service_account: Google Cloud IAM service account used to sign OIDC tokens for backends that have authentication configured (https://cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#backend). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#google_service_account GoogleApiGatewayApiConfigA#google_service_account}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGatewayConfigBackendConfig.__init__)
            check_type(argname="argument google_service_account", value=google_service_account, expected_type=type_hints["google_service_account"])
        self._values: typing.Dict[str, typing.Any] = {
            "google_service_account": google_service_account,
        }

    @builtins.property
    def google_service_account(self) -> builtins.str:
        '''Google Cloud IAM service account used to sign OIDC tokens for backends that have authentication configured (https://cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#backend).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#google_service_account GoogleApiGatewayApiConfigA#google_service_account}
        '''
        result = self._values.get("google_service_account")
        assert result is not None, "Required property 'google_service_account' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigGatewayConfigBackendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccountInput")
    def google_service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "googleServiceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="googleServiceAccount")
    def google_service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "googleServiceAccount"))

    @google_service_account.setter
    def google_service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference, "google_service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "googleServiceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleApiGatewayApiConfigGatewayConfigBackendConfig]:
        return typing.cast(typing.Optional[GoogleApiGatewayApiConfigGatewayConfigBackendConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApiGatewayApiConfigGatewayConfigBackendConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApiGatewayApiConfigGatewayConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGatewayConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGatewayConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBackendConfig")
    def put_backend_config(self, *, google_service_account: builtins.str) -> None:
        '''
        :param google_service_account: Google Cloud IAM service account used to sign OIDC tokens for backends that have authentication configured (https://cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.configs#backend). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#google_service_account GoogleApiGatewayApiConfigA#google_service_account}
        '''
        value = GoogleApiGatewayApiConfigGatewayConfigBackendConfig(
            google_service_account=google_service_account
        )

        return typing.cast(None, jsii.invoke(self, "putBackendConfig", [value]))

    @builtins.property
    @jsii.member(jsii_name="backendConfig")
    def backend_config(
        self,
    ) -> GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference:
        return typing.cast(GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference, jsii.get(self, "backendConfig"))

    @builtins.property
    @jsii.member(jsii_name="backendConfigInput")
    def backend_config_input(
        self,
    ) -> typing.Optional[GoogleApiGatewayApiConfigGatewayConfigBackendConfig]:
        return typing.cast(typing.Optional[GoogleApiGatewayApiConfigGatewayConfigBackendConfig], jsii.get(self, "backendConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleApiGatewayApiConfigGatewayConfig]:
        return typing.cast(typing.Optional[GoogleApiGatewayApiConfigGatewayConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApiGatewayApiConfigGatewayConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGatewayConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServices",
    jsii_struct_bases=[],
    name_mapping={"file_descriptor_set": "fileDescriptorSet", "source": "source"},
)
class GoogleApiGatewayApiConfigGrpcServices:
    def __init__(
        self,
        *,
        file_descriptor_set: typing.Union["GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet", typing.Dict[str, typing.Any]],
        source: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigGrpcServicesSource", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param file_descriptor_set: file_descriptor_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#file_descriptor_set GoogleApiGatewayApiConfigA#file_descriptor_set}
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#source GoogleApiGatewayApiConfigA#source}
        '''
        if isinstance(file_descriptor_set, dict):
            file_descriptor_set = GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet(**file_descriptor_set)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServices.__init__)
            check_type(argname="argument file_descriptor_set", value=file_descriptor_set, expected_type=type_hints["file_descriptor_set"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[str, typing.Any] = {
            "file_descriptor_set": file_descriptor_set,
        }
        if source is not None:
            self._values["source"] = source

    @builtins.property
    def file_descriptor_set(
        self,
    ) -> "GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet":
        '''file_descriptor_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#file_descriptor_set GoogleApiGatewayApiConfigA#file_descriptor_set}
        '''
        result = self._values.get("file_descriptor_set")
        assert result is not None, "Required property 'file_descriptor_set' is missing"
        return typing.cast("GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet", result)

    @builtins.property
    def source(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServicesSource"]]]:
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#source GoogleApiGatewayApiConfigA#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServicesSource"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigGrpcServices(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet",
    jsii_struct_bases=[],
    name_mapping={"contents": "contents", "path": "path"},
)
class GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet:
    def __init__(self, *, contents: builtins.str, path: builtins.str) -> None:
        '''
        :param contents: Base64 encoded content of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        :param path: The file path (full or relative path). This is typically the path of the file when it is uploaded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet.__init__)
            check_type(argname="argument contents", value=contents, expected_type=type_hints["contents"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "contents": contents,
            "path": path,
        }

    @builtins.property
    def contents(self) -> builtins.str:
        '''Base64 encoded content of the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        '''
        result = self._values.get("contents")
        assert result is not None, "Required property 'contents' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The file path (full or relative path). This is typically the path of the file when it is uploaded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="contentsInput")
    def contents_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="contents")
    def contents(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contents"))

    @contents.setter
    def contents(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference, "contents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contents", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet]:
        return typing.cast(typing.Optional[GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApiGatewayApiConfigGrpcServicesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServicesList",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleApiGatewayApiConfigGrpcServicesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleApiGatewayApiConfigGrpcServicesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigGrpcServices]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigGrpcServices]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigGrpcServices]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApiGatewayApiConfigGrpcServicesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServicesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFileDescriptorSet")
    def put_file_descriptor_set(
        self,
        *,
        contents: builtins.str,
        path: builtins.str,
    ) -> None:
        '''
        :param contents: Base64 encoded content of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        :param path: The file path (full or relative path). This is typically the path of the file when it is uploaded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        value = GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet(
            contents=contents, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putFileDescriptorSet", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApiGatewayApiConfigGrpcServicesSource", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesOutputReference.put_source)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @builtins.property
    @jsii.member(jsii_name="fileDescriptorSet")
    def file_descriptor_set(
        self,
    ) -> GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference:
        return typing.cast(GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference, jsii.get(self, "fileDescriptorSet"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "GoogleApiGatewayApiConfigGrpcServicesSourceList":
        return typing.cast("GoogleApiGatewayApiConfigGrpcServicesSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="fileDescriptorSetInput")
    def file_descriptor_set_input(
        self,
    ) -> typing.Optional[GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet]:
        return typing.cast(typing.Optional[GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet], jsii.get(self, "fileDescriptorSetInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServicesSource"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApiGatewayApiConfigGrpcServicesSource"]]], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApiGatewayApiConfigGrpcServices, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApiGatewayApiConfigGrpcServices, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApiGatewayApiConfigGrpcServices, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServicesSource",
    jsii_struct_bases=[],
    name_mapping={"contents": "contents", "path": "path"},
)
class GoogleApiGatewayApiConfigGrpcServicesSource:
    def __init__(self, *, contents: builtins.str, path: builtins.str) -> None:
        '''
        :param contents: Base64 encoded content of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        :param path: The file path (full or relative path). This is typically the path of the file when it is uploaded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesSource.__init__)
            check_type(argname="argument contents", value=contents, expected_type=type_hints["contents"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "contents": contents,
            "path": path,
        }

    @builtins.property
    def contents(self) -> builtins.str:
        '''Base64 encoded content of the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        '''
        result = self._values.get("contents")
        assert result is not None, "Required property 'contents' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The file path (full or relative path). This is typically the path of the file when it is uploaded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigGrpcServicesSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApiGatewayApiConfigGrpcServicesSourceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServicesSourceList",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesSourceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesSourceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesSourceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesSourceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesSourceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigGrpcServicesSource]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigGrpcServicesSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigGrpcServicesSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesSourceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentsInput")
    def contents_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="contents")
    def contents(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contents"))

    @contents.setter
    def contents(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference, "contents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contents", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApiGatewayApiConfigGrpcServicesSource, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApiGatewayApiConfigGrpcServicesSource, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApiGatewayApiConfigGrpcServicesSource, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigManagedServiceConfigs",
    jsii_struct_bases=[],
    name_mapping={"contents": "contents", "path": "path"},
)
class GoogleApiGatewayApiConfigManagedServiceConfigs:
    def __init__(self, *, contents: builtins.str, path: builtins.str) -> None:
        '''
        :param contents: Base64 encoded content of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        :param path: The file path (full or relative path). This is typically the path of the file when it is uploaded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigManagedServiceConfigs.__init__)
            check_type(argname="argument contents", value=contents, expected_type=type_hints["contents"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "contents": contents,
            "path": path,
        }

    @builtins.property
    def contents(self) -> builtins.str:
        '''Base64 encoded content of the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        '''
        result = self._values.get("contents")
        assert result is not None, "Required property 'contents' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The file path (full or relative path). This is typically the path of the file when it is uploaded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigManagedServiceConfigs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApiGatewayApiConfigManagedServiceConfigsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigManagedServiceConfigsList",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigManagedServiceConfigsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigManagedServiceConfigsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigManagedServiceConfigsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigManagedServiceConfigsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigManagedServiceConfigsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigManagedServiceConfigs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigManagedServiceConfigs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigManagedServiceConfigs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigManagedServiceConfigsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentsInput")
    def contents_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="contents")
    def contents(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contents"))

    @contents.setter
    def contents(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference, "contents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contents", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApiGatewayApiConfigManagedServiceConfigs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApiGatewayApiConfigManagedServiceConfigs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApiGatewayApiConfigManagedServiceConfigs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigOpenapiDocuments",
    jsii_struct_bases=[],
    name_mapping={"document": "document"},
)
class GoogleApiGatewayApiConfigOpenapiDocuments:
    def __init__(
        self,
        *,
        document: typing.Union["GoogleApiGatewayApiConfigOpenapiDocumentsDocument", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param document: document block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#document GoogleApiGatewayApiConfigA#document}
        '''
        if isinstance(document, dict):
            document = GoogleApiGatewayApiConfigOpenapiDocumentsDocument(**document)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigOpenapiDocuments.__init__)
            check_type(argname="argument document", value=document, expected_type=type_hints["document"])
        self._values: typing.Dict[str, typing.Any] = {
            "document": document,
        }

    @builtins.property
    def document(self) -> "GoogleApiGatewayApiConfigOpenapiDocumentsDocument":
        '''document block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#document GoogleApiGatewayApiConfigA#document}
        '''
        result = self._values.get("document")
        assert result is not None, "Required property 'document' is missing"
        return typing.cast("GoogleApiGatewayApiConfigOpenapiDocumentsDocument", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigOpenapiDocuments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigOpenapiDocumentsDocument",
    jsii_struct_bases=[],
    name_mapping={"contents": "contents", "path": "path"},
)
class GoogleApiGatewayApiConfigOpenapiDocumentsDocument:
    def __init__(self, *, contents: builtins.str, path: builtins.str) -> None:
        '''
        :param contents: Base64 encoded content of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        :param path: The file path (full or relative path). This is typically the path of the file when it is uploaded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigOpenapiDocumentsDocument.__init__)
            check_type(argname="argument contents", value=contents, expected_type=type_hints["contents"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "contents": contents,
            "path": path,
        }

    @builtins.property
    def contents(self) -> builtins.str:
        '''Base64 encoded content of the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        '''
        result = self._values.get("contents")
        assert result is not None, "Required property 'contents' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The file path (full or relative path). This is typically the path of the file when it is uploaded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigOpenapiDocumentsDocument(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="contentsInput")
    def contents_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="contents")
    def contents(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contents"))

    @contents.setter
    def contents(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference, "contents").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contents", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleApiGatewayApiConfigOpenapiDocumentsDocument]:
        return typing.cast(typing.Optional[GoogleApiGatewayApiConfigOpenapiDocumentsDocument], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApiGatewayApiConfigOpenapiDocumentsDocument],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApiGatewayApiConfigOpenapiDocumentsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigOpenapiDocumentsList",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigOpenapiDocumentsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleApiGatewayApiConfigOpenapiDocumentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigOpenapiDocumentsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleApiGatewayApiConfigOpenapiDocumentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigOpenapiDocuments]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigOpenapiDocuments]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApiGatewayApiConfigOpenapiDocuments]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApiGatewayApiConfigOpenapiDocumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigOpenapiDocumentsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigOpenapiDocumentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDocument")
    def put_document(self, *, contents: builtins.str, path: builtins.str) -> None:
        '''
        :param contents: Base64 encoded content of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#contents GoogleApiGatewayApiConfigA#contents}
        :param path: The file path (full or relative path). This is typically the path of the file when it is uploaded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#path GoogleApiGatewayApiConfigA#path}
        '''
        value = GoogleApiGatewayApiConfigOpenapiDocumentsDocument(
            contents=contents, path=path
        )

        return typing.cast(None, jsii.invoke(self, "putDocument", [value]))

    @builtins.property
    @jsii.member(jsii_name="document")
    def document(
        self,
    ) -> GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference:
        return typing.cast(GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference, jsii.get(self, "document"))

    @builtins.property
    @jsii.member(jsii_name="documentInput")
    def document_input(
        self,
    ) -> typing.Optional[GoogleApiGatewayApiConfigOpenapiDocumentsDocument]:
        return typing.cast(typing.Optional[GoogleApiGatewayApiConfigOpenapiDocumentsDocument], jsii.get(self, "documentInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApiGatewayApiConfigOpenapiDocuments, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApiGatewayApiConfigOpenapiDocuments, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApiGatewayApiConfigOpenapiDocuments, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigOpenapiDocumentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleApiGatewayApiConfigTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#create GoogleApiGatewayApiConfigA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#delete GoogleApiGatewayApiConfigA#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#update GoogleApiGatewayApiConfigA#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#create GoogleApiGatewayApiConfigA#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#delete GoogleApiGatewayApiConfigA#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_api_gateway_api_config#update GoogleApiGatewayApiConfigA#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApiGatewayApiConfigTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApiGatewayApiConfigTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApiGatewayApiConfig.GoogleApiGatewayApiConfigTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApiGatewayApiConfigTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApiGatewayApiConfigTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApiGatewayApiConfigTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApiGatewayApiConfigTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApiGatewayApiConfigTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleApiGatewayApiConfigA",
    "GoogleApiGatewayApiConfigAConfig",
    "GoogleApiGatewayApiConfigGatewayConfig",
    "GoogleApiGatewayApiConfigGatewayConfigBackendConfig",
    "GoogleApiGatewayApiConfigGatewayConfigBackendConfigOutputReference",
    "GoogleApiGatewayApiConfigGatewayConfigOutputReference",
    "GoogleApiGatewayApiConfigGrpcServices",
    "GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSet",
    "GoogleApiGatewayApiConfigGrpcServicesFileDescriptorSetOutputReference",
    "GoogleApiGatewayApiConfigGrpcServicesList",
    "GoogleApiGatewayApiConfigGrpcServicesOutputReference",
    "GoogleApiGatewayApiConfigGrpcServicesSource",
    "GoogleApiGatewayApiConfigGrpcServicesSourceList",
    "GoogleApiGatewayApiConfigGrpcServicesSourceOutputReference",
    "GoogleApiGatewayApiConfigManagedServiceConfigs",
    "GoogleApiGatewayApiConfigManagedServiceConfigsList",
    "GoogleApiGatewayApiConfigManagedServiceConfigsOutputReference",
    "GoogleApiGatewayApiConfigOpenapiDocuments",
    "GoogleApiGatewayApiConfigOpenapiDocumentsDocument",
    "GoogleApiGatewayApiConfigOpenapiDocumentsDocumentOutputReference",
    "GoogleApiGatewayApiConfigOpenapiDocumentsList",
    "GoogleApiGatewayApiConfigOpenapiDocumentsOutputReference",
    "GoogleApiGatewayApiConfigTimeouts",
    "GoogleApiGatewayApiConfigTimeoutsOutputReference",
]

publication.publish()
