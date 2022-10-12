'''
# `boundary_credential_library_vault`

Refer to the Terraform Registory for docs: [`boundary_credential_library_vault`](https://www.terraform.io/docs/providers/boundary/r/credential_library_vault).
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


class CredentialLibraryVault(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-boundary.credentialLibraryVault.CredentialLibraryVault",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault boundary_credential_library_vault}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        credential_store_id: builtins.str,
        path: builtins.str,
        credential_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        http_method: typing.Optional[builtins.str] = None,
        http_request_body: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault boundary_credential_library_vault} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param credential_store_id: The ID of the credential store that this library belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#credential_store_id CredentialLibraryVault#credential_store_id}
        :param path: The path in Vault to request credentials from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#path CredentialLibraryVault#path}
        :param credential_type: The type of credential the library generates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#credential_type CredentialLibraryVault#credential_type}
        :param description: The Vault credential library description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#description CredentialLibraryVault#description}
        :param http_method: The HTTP method the library uses when requesting credentials from Vault. Defaults to 'GET'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#http_method CredentialLibraryVault#http_method}
        :param http_request_body: The body of the HTTP request the library sends to Vault when requesting credentials. Only valid if ``http_method`` is set to ``POST``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#http_request_body CredentialLibraryVault#http_request_body}
        :param name: The Vault credential library name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#name CredentialLibraryVault#name}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CredentialLibraryVault.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = CredentialLibraryVaultConfig(
            credential_store_id=credential_store_id,
            path=path,
            credential_type=credential_type,
            description=description,
            http_method=http_method,
            http_request_body=http_request_body,
            name=name,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetCredentialType")
    def reset_credential_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentialType", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @jsii.member(jsii_name="resetHttpRequestBody")
    def reset_http_request_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpRequestBody", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="credentialStoreIdInput")
    def credential_store_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialStoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialTypeInput")
    def credential_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="httpRequestBodyInput")
    def http_request_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpRequestBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialStoreId")
    def credential_store_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialStoreId"))

    @credential_store_id.setter
    def credential_store_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CredentialLibraryVault, "credential_store_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialStoreId", value)

    @builtins.property
    @jsii.member(jsii_name="credentialType")
    def credential_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "credentialType"))

    @credential_type.setter
    def credential_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CredentialLibraryVault, "credential_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CredentialLibraryVault, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CredentialLibraryVault, "http_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="httpRequestBody")
    def http_request_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpRequestBody"))

    @http_request_body.setter
    def http_request_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CredentialLibraryVault, "http_request_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpRequestBody", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CredentialLibraryVault, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CredentialLibraryVault, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-boundary.credentialLibraryVault.CredentialLibraryVaultConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "credential_store_id": "credentialStoreId",
        "path": "path",
        "credential_type": "credentialType",
        "description": "description",
        "http_method": "httpMethod",
        "http_request_body": "httpRequestBody",
        "name": "name",
    },
)
class CredentialLibraryVaultConfig(cdktf.TerraformMetaArguments):
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
        credential_store_id: builtins.str,
        path: builtins.str,
        credential_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        http_method: typing.Optional[builtins.str] = None,
        http_request_body: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param credential_store_id: The ID of the credential store that this library belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#credential_store_id CredentialLibraryVault#credential_store_id}
        :param path: The path in Vault to request credentials from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#path CredentialLibraryVault#path}
        :param credential_type: The type of credential the library generates. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#credential_type CredentialLibraryVault#credential_type}
        :param description: The Vault credential library description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#description CredentialLibraryVault#description}
        :param http_method: The HTTP method the library uses when requesting credentials from Vault. Defaults to 'GET'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#http_method CredentialLibraryVault#http_method}
        :param http_request_body: The body of the HTTP request the library sends to Vault when requesting credentials. Only valid if ``http_method`` is set to ``POST``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#http_request_body CredentialLibraryVault#http_request_body}
        :param name: The Vault credential library name. Defaults to the resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#name CredentialLibraryVault#name}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(CredentialLibraryVaultConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument credential_store_id", value=credential_store_id, expected_type=type_hints["credential_store_id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument credential_type", value=credential_type, expected_type=type_hints["credential_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument http_request_body", value=http_request_body, expected_type=type_hints["http_request_body"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "credential_store_id": credential_store_id,
            "path": path,
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
        if credential_type is not None:
            self._values["credential_type"] = credential_type
        if description is not None:
            self._values["description"] = description
        if http_method is not None:
            self._values["http_method"] = http_method
        if http_request_body is not None:
            self._values["http_request_body"] = http_request_body
        if name is not None:
            self._values["name"] = name

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
    def credential_store_id(self) -> builtins.str:
        '''The ID of the credential store that this library belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#credential_store_id CredentialLibraryVault#credential_store_id}
        '''
        result = self._values.get("credential_store_id")
        assert result is not None, "Required property 'credential_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The path in Vault to request credentials from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#path CredentialLibraryVault#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def credential_type(self) -> typing.Optional[builtins.str]:
        '''The type of credential the library generates.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#credential_type CredentialLibraryVault#credential_type}
        '''
        result = self._values.get("credential_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The Vault credential library description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#description CredentialLibraryVault#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''The HTTP method the library uses when requesting credentials from Vault. Defaults to 'GET'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#http_method CredentialLibraryVault#http_method}
        '''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_request_body(self) -> typing.Optional[builtins.str]:
        '''The body of the HTTP request the library sends to Vault when requesting credentials.

        Only valid if ``http_method`` is set to ``POST``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#http_request_body CredentialLibraryVault#http_request_body}
        '''
        result = self._values.get("http_request_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The Vault credential library name. Defaults to the resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/boundary/r/credential_library_vault#name CredentialLibraryVault#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialLibraryVaultConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CredentialLibraryVault",
    "CredentialLibraryVaultConfig",
]

publication.publish()
