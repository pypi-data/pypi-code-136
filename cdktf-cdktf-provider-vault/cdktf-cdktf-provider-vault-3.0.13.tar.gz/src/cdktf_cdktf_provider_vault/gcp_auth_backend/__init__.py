'''
# `vault_gcp_auth_backend`

Refer to the Terraform Registory for docs: [`vault_gcp_auth_backend`](https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend).
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


class GcpAuthBackend(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpAuthBackend.GcpAuthBackend",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend vault_gcp_auth_backend}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        client_email: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        custom_endpoint: typing.Optional[typing.Union["GcpAuthBackendCustomEndpoint", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        private_key_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend vault_gcp_auth_backend} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#client_email GcpAuthBackend#client_email}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#client_id GcpAuthBackend#client_id}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#credentials GcpAuthBackend#credentials}.
        :param custom_endpoint: custom_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#custom_endpoint GcpAuthBackend#custom_endpoint}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#description GcpAuthBackend#description}.
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#disable_remount GcpAuthBackend#disable_remount}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#id GcpAuthBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Specifies if the auth method is local only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#local GcpAuthBackend#local}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#namespace GcpAuthBackend#namespace}
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#path GcpAuthBackend#path}.
        :param private_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#private_key_id GcpAuthBackend#private_key_id}.
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#project_id GcpAuthBackend#project_id}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpAuthBackend.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GcpAuthBackendConfig(
            client_email=client_email,
            client_id=client_id,
            credentials=credentials,
            custom_endpoint=custom_endpoint,
            description=description,
            disable_remount=disable_remount,
            id=id,
            local=local,
            namespace=namespace,
            path=path,
            private_key_id=private_key_id,
            project_id=project_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCustomEndpoint")
    def put_custom_endpoint(
        self,
        *,
        api: typing.Optional[builtins.str] = None,
        compute: typing.Optional[builtins.str] = None,
        crm: typing.Optional[builtins.str] = None,
        iam: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api: Replaces the service endpoint used in API requests to https://www.googleapis.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#api GcpAuthBackend#api}
        :param compute: Replaces the service endpoint used in API requests to ``https://compute.googleapis.com``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#compute GcpAuthBackend#compute}
        :param crm: Replaces the service endpoint used in API requests to ``https://cloudresourcemanager.googleapis.com``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#crm GcpAuthBackend#crm}
        :param iam: Replaces the service endpoint used in API requests to ``https://iam.googleapis.com``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#iam GcpAuthBackend#iam}
        '''
        value = GcpAuthBackendCustomEndpoint(
            api=api, compute=compute, crm=crm, iam=iam
        )

        return typing.cast(None, jsii.invoke(self, "putCustomEndpoint", [value]))

    @jsii.member(jsii_name="resetClientEmail")
    def reset_client_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientEmail", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetCustomEndpoint")
    def reset_custom_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomEndpoint", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableRemount")
    def reset_disable_remount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableRemount", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPrivateKeyId")
    def reset_private_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKeyId", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customEndpoint")
    def custom_endpoint(self) -> "GcpAuthBackendCustomEndpointOutputReference":
        return typing.cast("GcpAuthBackendCustomEndpointOutputReference", jsii.get(self, "customEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clientEmailInput")
    def client_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="customEndpointInput")
    def custom_endpoint_input(self) -> typing.Optional["GcpAuthBackendCustomEndpoint"]:
        return typing.cast(typing.Optional["GcpAuthBackendCustomEndpoint"], jsii.get(self, "customEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableRemountInput")
    def disable_remount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableRemountInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyIdInput")
    def private_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientEmail")
    def client_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientEmail"))

    @client_email.setter
    def client_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "client_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientEmail", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentials"))

    @credentials.setter
    def credentials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentials", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableRemount")
    def disable_remount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableRemount"))

    @disable_remount.setter
    def disable_remount(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "disable_remount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableRemount", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "local"))

    @local.setter
    def local(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "local").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "local", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="privateKeyId")
    def private_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKeyId"))

    @private_key_id.setter
    def private_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "private_key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackend, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.gcpAuthBackend.GcpAuthBackendConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_email": "clientEmail",
        "client_id": "clientId",
        "credentials": "credentials",
        "custom_endpoint": "customEndpoint",
        "description": "description",
        "disable_remount": "disableRemount",
        "id": "id",
        "local": "local",
        "namespace": "namespace",
        "path": "path",
        "private_key_id": "privateKeyId",
        "project_id": "projectId",
    },
)
class GcpAuthBackendConfig(cdktf.TerraformMetaArguments):
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
        client_email: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[builtins.str] = None,
        custom_endpoint: typing.Optional[typing.Union["GcpAuthBackendCustomEndpoint", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_remount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        local: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        private_key_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param client_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#client_email GcpAuthBackend#client_email}.
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#client_id GcpAuthBackend#client_id}.
        :param credentials: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#credentials GcpAuthBackend#credentials}.
        :param custom_endpoint: custom_endpoint block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#custom_endpoint GcpAuthBackend#custom_endpoint}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#description GcpAuthBackend#description}.
        :param disable_remount: If set, opts out of mount migration on path updates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#disable_remount GcpAuthBackend#disable_remount}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#id GcpAuthBackend#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param local: Specifies if the auth method is local only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#local GcpAuthBackend#local}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#namespace GcpAuthBackend#namespace}
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#path GcpAuthBackend#path}.
        :param private_key_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#private_key_id GcpAuthBackend#private_key_id}.
        :param project_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#project_id GcpAuthBackend#project_id}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_endpoint, dict):
            custom_endpoint = GcpAuthBackendCustomEndpoint(**custom_endpoint)
        if __debug__:
            type_hints = typing.get_type_hints(GcpAuthBackendConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument client_email", value=client_email, expected_type=type_hints["client_email"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument custom_endpoint", value=custom_endpoint, expected_type=type_hints["custom_endpoint"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_remount", value=disable_remount, expected_type=type_hints["disable_remount"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument private_key_id", value=private_key_id, expected_type=type_hints["private_key_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if client_email is not None:
            self._values["client_email"] = client_email
        if client_id is not None:
            self._values["client_id"] = client_id
        if credentials is not None:
            self._values["credentials"] = credentials
        if custom_endpoint is not None:
            self._values["custom_endpoint"] = custom_endpoint
        if description is not None:
            self._values["description"] = description
        if disable_remount is not None:
            self._values["disable_remount"] = disable_remount
        if id is not None:
            self._values["id"] = id
        if local is not None:
            self._values["local"] = local
        if namespace is not None:
            self._values["namespace"] = namespace
        if path is not None:
            self._values["path"] = path
        if private_key_id is not None:
            self._values["private_key_id"] = private_key_id
        if project_id is not None:
            self._values["project_id"] = project_id

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
    def client_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#client_email GcpAuthBackend#client_email}.'''
        result = self._values.get("client_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#client_id GcpAuthBackend#client_id}.'''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#credentials GcpAuthBackend#credentials}.'''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_endpoint(self) -> typing.Optional["GcpAuthBackendCustomEndpoint"]:
        '''custom_endpoint block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#custom_endpoint GcpAuthBackend#custom_endpoint}
        '''
        result = self._values.get("custom_endpoint")
        return typing.cast(typing.Optional["GcpAuthBackendCustomEndpoint"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#description GcpAuthBackend#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_remount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set, opts out of mount migration on path updates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#disable_remount GcpAuthBackend#disable_remount}
        '''
        result = self._values.get("disable_remount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#id GcpAuthBackend#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if the auth method is local only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#local GcpAuthBackend#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#namespace GcpAuthBackend#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#path GcpAuthBackend#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#private_key_id GcpAuthBackend#private_key_id}.'''
        result = self._values.get("private_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#project_id GcpAuthBackend#project_id}.'''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GcpAuthBackendConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.gcpAuthBackend.GcpAuthBackendCustomEndpoint",
    jsii_struct_bases=[],
    name_mapping={"api": "api", "compute": "compute", "crm": "crm", "iam": "iam"},
)
class GcpAuthBackendCustomEndpoint:
    def __init__(
        self,
        *,
        api: typing.Optional[builtins.str] = None,
        compute: typing.Optional[builtins.str] = None,
        crm: typing.Optional[builtins.str] = None,
        iam: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api: Replaces the service endpoint used in API requests to https://www.googleapis.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#api GcpAuthBackend#api}
        :param compute: Replaces the service endpoint used in API requests to ``https://compute.googleapis.com``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#compute GcpAuthBackend#compute}
        :param crm: Replaces the service endpoint used in API requests to ``https://cloudresourcemanager.googleapis.com``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#crm GcpAuthBackend#crm}
        :param iam: Replaces the service endpoint used in API requests to ``https://iam.googleapis.com``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#iam GcpAuthBackend#iam}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpAuthBackendCustomEndpoint.__init__)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument compute", value=compute, expected_type=type_hints["compute"])
            check_type(argname="argument crm", value=crm, expected_type=type_hints["crm"])
            check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
        self._values: typing.Dict[str, typing.Any] = {}
        if api is not None:
            self._values["api"] = api
        if compute is not None:
            self._values["compute"] = compute
        if crm is not None:
            self._values["crm"] = crm
        if iam is not None:
            self._values["iam"] = iam

    @builtins.property
    def api(self) -> typing.Optional[builtins.str]:
        '''Replaces the service endpoint used in API requests to https://www.googleapis.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#api GcpAuthBackend#api}
        '''
        result = self._values.get("api")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute(self) -> typing.Optional[builtins.str]:
        '''Replaces the service endpoint used in API requests to ``https://compute.googleapis.com``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#compute GcpAuthBackend#compute}
        '''
        result = self._values.get("compute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def crm(self) -> typing.Optional[builtins.str]:
        '''Replaces the service endpoint used in API requests to ``https://cloudresourcemanager.googleapis.com``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#crm GcpAuthBackend#crm}
        '''
        result = self._values.get("crm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam(self) -> typing.Optional[builtins.str]:
        '''Replaces the service endpoint used in API requests to ``https://iam.googleapis.com``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_auth_backend#iam GcpAuthBackend#iam}
        '''
        result = self._values.get("iam")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GcpAuthBackendCustomEndpoint(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GcpAuthBackendCustomEndpointOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpAuthBackend.GcpAuthBackendCustomEndpointOutputReference",
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
            type_hints = typing.get_type_hints(GcpAuthBackendCustomEndpointOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApi")
    def reset_api(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApi", []))

    @jsii.member(jsii_name="resetCompute")
    def reset_compute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompute", []))

    @jsii.member(jsii_name="resetCrm")
    def reset_crm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrm", []))

    @jsii.member(jsii_name="resetIam")
    def reset_iam(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIam", []))

    @builtins.property
    @jsii.member(jsii_name="apiInput")
    def api_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiInput"))

    @builtins.property
    @jsii.member(jsii_name="computeInput")
    def compute_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeInput"))

    @builtins.property
    @jsii.member(jsii_name="crmInput")
    def crm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crmInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInput")
    def iam_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamInput"))

    @builtins.property
    @jsii.member(jsii_name="api")
    def api(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "api"))

    @api.setter
    def api(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackendCustomEndpointOutputReference, "api").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "api", value)

    @builtins.property
    @jsii.member(jsii_name="compute")
    def compute(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compute"))

    @compute.setter
    def compute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackendCustomEndpointOutputReference, "compute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compute", value)

    @builtins.property
    @jsii.member(jsii_name="crm")
    def crm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crm"))

    @crm.setter
    def crm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackendCustomEndpointOutputReference, "crm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crm", value)

    @builtins.property
    @jsii.member(jsii_name="iam")
    def iam(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iam"))

    @iam.setter
    def iam(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackendCustomEndpointOutputReference, "iam").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iam", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GcpAuthBackendCustomEndpoint]:
        return typing.cast(typing.Optional[GcpAuthBackendCustomEndpoint], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GcpAuthBackendCustomEndpoint],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpAuthBackendCustomEndpointOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GcpAuthBackend",
    "GcpAuthBackendConfig",
    "GcpAuthBackendCustomEndpoint",
    "GcpAuthBackendCustomEndpointOutputReference",
]

publication.publish()
