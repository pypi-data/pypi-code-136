'''
# `github_actions_organization_secret`

Refer to the Terraform Registory for docs: [`github_actions_organization_secret`](https://www.terraform.io/docs/providers/github/r/actions_organization_secret).
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


class ActionsOrganizationSecret(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.actionsOrganizationSecret.ActionsOrganizationSecret",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret github_actions_organization_secret}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        secret_name: builtins.str,
        visibility: builtins.str,
        encrypted_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        plaintext_value: typing.Optional[builtins.str] = None,
        selected_repository_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret github_actions_organization_secret} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#secret_name ActionsOrganizationSecret#secret_name}.
        :param visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#visibility ActionsOrganizationSecret#visibility}.
        :param encrypted_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#encrypted_value ActionsOrganizationSecret#encrypted_value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#id ActionsOrganizationSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param plaintext_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#plaintext_value ActionsOrganizationSecret#plaintext_value}.
        :param selected_repository_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#selected_repository_ids ActionsOrganizationSecret#selected_repository_ids}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ActionsOrganizationSecret.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ActionsOrganizationSecretConfig(
            secret_name=secret_name,
            visibility=visibility,
            encrypted_value=encrypted_value,
            id=id,
            plaintext_value=plaintext_value,
            selected_repository_ids=selected_repository_ids,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetEncryptedValue")
    def reset_encrypted_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptedValue", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPlaintextValue")
    def reset_plaintext_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlaintextValue", []))

    @jsii.member(jsii_name="resetSelectedRepositoryIds")
    def reset_selected_repository_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectedRepositoryIds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="encryptedValueInput")
    def encrypted_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptedValueInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="plaintextValueInput")
    def plaintext_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "plaintextValueInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectedRepositoryIdsInput")
    def selected_repository_ids_input(
        self,
    ) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "selectedRepositoryIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityInput")
    def visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptedValue")
    def encrypted_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptedValue"))

    @encrypted_value.setter
    def encrypted_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationSecret, "encrypted_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptedValue", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationSecret, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="plaintextValue")
    def plaintext_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "plaintextValue"))

    @plaintext_value.setter
    def plaintext_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationSecret, "plaintext_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plaintextValue", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationSecret, "secret_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="selectedRepositoryIds")
    def selected_repository_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "selectedRepositoryIds"))

    @selected_repository_ids.setter
    def selected_repository_ids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationSecret, "selected_repository_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectedRepositoryIds", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ActionsOrganizationSecret, "visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.actionsOrganizationSecret.ActionsOrganizationSecretConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "secret_name": "secretName",
        "visibility": "visibility",
        "encrypted_value": "encryptedValue",
        "id": "id",
        "plaintext_value": "plaintextValue",
        "selected_repository_ids": "selectedRepositoryIds",
    },
)
class ActionsOrganizationSecretConfig(cdktf.TerraformMetaArguments):
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
        secret_name: builtins.str,
        visibility: builtins.str,
        encrypted_value: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        plaintext_value: typing.Optional[builtins.str] = None,
        selected_repository_ids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#secret_name ActionsOrganizationSecret#secret_name}.
        :param visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#visibility ActionsOrganizationSecret#visibility}.
        :param encrypted_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#encrypted_value ActionsOrganizationSecret#encrypted_value}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#id ActionsOrganizationSecret#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param plaintext_value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#plaintext_value ActionsOrganizationSecret#plaintext_value}.
        :param selected_repository_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#selected_repository_ids ActionsOrganizationSecret#selected_repository_ids}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ActionsOrganizationSecretConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
            check_type(argname="argument encrypted_value", value=encrypted_value, expected_type=type_hints["encrypted_value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument plaintext_value", value=plaintext_value, expected_type=type_hints["plaintext_value"])
            check_type(argname="argument selected_repository_ids", value=selected_repository_ids, expected_type=type_hints["selected_repository_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
            "visibility": visibility,
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
        if encrypted_value is not None:
            self._values["encrypted_value"] = encrypted_value
        if id is not None:
            self._values["id"] = id
        if plaintext_value is not None:
            self._values["plaintext_value"] = plaintext_value
        if selected_repository_ids is not None:
            self._values["selected_repository_ids"] = selected_repository_ids

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
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#secret_name ActionsOrganizationSecret#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def visibility(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#visibility ActionsOrganizationSecret#visibility}.'''
        result = self._values.get("visibility")
        assert result is not None, "Required property 'visibility' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encrypted_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#encrypted_value ActionsOrganizationSecret#encrypted_value}.'''
        result = self._values.get("encrypted_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#id ActionsOrganizationSecret#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plaintext_value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#plaintext_value ActionsOrganizationSecret#plaintext_value}.'''
        result = self._values.get("plaintext_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selected_repository_ids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/actions_organization_secret#selected_repository_ids ActionsOrganizationSecret#selected_repository_ids}.'''
        result = self._values.get("selected_repository_ids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionsOrganizationSecretConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ActionsOrganizationSecret",
    "ActionsOrganizationSecretConfig",
]

publication.publish()
