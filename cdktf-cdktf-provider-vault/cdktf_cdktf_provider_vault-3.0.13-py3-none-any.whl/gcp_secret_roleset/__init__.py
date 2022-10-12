'''
# `vault_gcp_secret_roleset`

Refer to the Terraform Registory for docs: [`vault_gcp_secret_roleset`](https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset).
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


class GcpSecretRoleset(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpSecretRoleset.GcpSecretRoleset",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset vault_gcp_secret_roleset}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: builtins.str,
        binding: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GcpSecretRolesetBinding", typing.Dict[str, typing.Any]]]],
        project: builtins.str,
        roleset: builtins.str,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        secret_type: typing.Optional[builtins.str] = None,
        token_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset vault_gcp_secret_roleset} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: Path where the GCP secrets engine is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#backend GcpSecretRoleset#backend}
        :param binding: binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#binding GcpSecretRoleset#binding}
        :param project: Name of the GCP project that this roleset's service account will belong to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#project GcpSecretRoleset#project}
        :param roleset: Name of the RoleSet to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#roleset GcpSecretRoleset#roleset}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#id GcpSecretRoleset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#namespace GcpSecretRoleset#namespace}
        :param secret_type: Type of secret generated for this role set. Defaults to ``access_token``. Accepted values: ``access_token``, ``service_account_key``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#secret_type GcpSecretRoleset#secret_type}
        :param token_scopes: List of OAuth scopes to assign to ``access_token`` secrets generated under this role set (``access_token`` role sets only). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#token_scopes GcpSecretRoleset#token_scopes}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretRoleset.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GcpSecretRolesetConfig(
            backend=backend,
            binding=binding,
            project=project,
            roleset=roleset,
            id=id,
            namespace=namespace,
            secret_type=secret_type,
            token_scopes=token_scopes,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBinding")
    def put_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GcpSecretRolesetBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretRoleset.put_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBinding", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetSecretType")
    def reset_secret_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretType", []))

    @jsii.member(jsii_name="resetTokenScopes")
    def reset_token_scopes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenScopes", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="binding")
    def binding(self) -> "GcpSecretRolesetBindingList":
        return typing.cast("GcpSecretRolesetBindingList", jsii.get(self, "binding"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmail")
    def service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmail"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="bindingInput")
    def binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GcpSecretRolesetBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GcpSecretRolesetBinding"]]], jsii.get(self, "bindingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesetInput")
    def roleset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rolesetInput"))

    @builtins.property
    @jsii.member(jsii_name="secretTypeInput")
    def secret_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenScopesInput")
    def token_scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tokenScopesInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRoleset, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRoleset, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRoleset, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRoleset, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="roleset")
    def roleset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleset"))

    @roleset.setter
    def roleset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRoleset, "roleset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleset", value)

    @builtins.property
    @jsii.member(jsii_name="secretType")
    def secret_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretType"))

    @secret_type.setter
    def secret_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRoleset, "secret_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretType", value)

    @builtins.property
    @jsii.member(jsii_name="tokenScopes")
    def token_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenScopes"))

    @token_scopes.setter
    def token_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRoleset, "token_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenScopes", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.gcpSecretRoleset.GcpSecretRolesetBinding",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource", "roles": "roles"},
)
class GcpSecretRolesetBinding:
    def __init__(
        self,
        *,
        resource: builtins.str,
        roles: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param resource: Resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#resource GcpSecretRoleset#resource}
        :param roles: List of roles to apply to the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#roles GcpSecretRoleset#roles}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretRolesetBinding.__init__)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource": resource,
            "roles": roles,
        }

    @builtins.property
    def resource(self) -> builtins.str:
        '''Resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#resource GcpSecretRoleset#resource}
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List[builtins.str]:
        '''List of roles to apply to the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#roles GcpSecretRoleset#roles}
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GcpSecretRolesetBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GcpSecretRolesetBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpSecretRoleset.GcpSecretRolesetBindingList",
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
            type_hints = typing.get_type_hints(GcpSecretRolesetBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GcpSecretRolesetBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretRolesetBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GcpSecretRolesetBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRolesetBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GcpSecretRolesetBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GcpSecretRolesetBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretRolesetBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretRolesetBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretRolesetBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRolesetBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GcpSecretRolesetBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpSecretRoleset.GcpSecretRolesetBindingOutputReference",
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
            type_hints = typing.get_type_hints(GcpSecretRolesetBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRolesetBindingOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRolesetBindingOutputReference, "roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GcpSecretRolesetBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GcpSecretRolesetBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GcpSecretRolesetBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretRolesetBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.gcpSecretRoleset.GcpSecretRolesetConfig",
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
        "binding": "binding",
        "project": "project",
        "roleset": "roleset",
        "id": "id",
        "namespace": "namespace",
        "secret_type": "secretType",
        "token_scopes": "tokenScopes",
    },
)
class GcpSecretRolesetConfig(cdktf.TerraformMetaArguments):
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
        binding: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GcpSecretRolesetBinding, typing.Dict[str, typing.Any]]]],
        project: builtins.str,
        roleset: builtins.str,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        secret_type: typing.Optional[builtins.str] = None,
        token_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend: Path where the GCP secrets engine is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#backend GcpSecretRoleset#backend}
        :param binding: binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#binding GcpSecretRoleset#binding}
        :param project: Name of the GCP project that this roleset's service account will belong to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#project GcpSecretRoleset#project}
        :param roleset: Name of the RoleSet to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#roleset GcpSecretRoleset#roleset}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#id GcpSecretRoleset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#namespace GcpSecretRoleset#namespace}
        :param secret_type: Type of secret generated for this role set. Defaults to ``access_token``. Accepted values: ``access_token``, ``service_account_key``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#secret_type GcpSecretRoleset#secret_type}
        :param token_scopes: List of OAuth scopes to assign to ``access_token`` secrets generated under this role set (``access_token`` role sets only). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#token_scopes GcpSecretRoleset#token_scopes}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretRolesetConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument binding", value=binding, expected_type=type_hints["binding"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument roleset", value=roleset, expected_type=type_hints["roleset"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument secret_type", value=secret_type, expected_type=type_hints["secret_type"])
            check_type(argname="argument token_scopes", value=token_scopes, expected_type=type_hints["token_scopes"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
            "binding": binding,
            "project": project,
            "roleset": roleset,
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
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if secret_type is not None:
            self._values["secret_type"] = secret_type
        if token_scopes is not None:
            self._values["token_scopes"] = token_scopes

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
        '''Path where the GCP secrets engine is mounted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#backend GcpSecretRoleset#backend}
        '''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def binding(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List[GcpSecretRolesetBinding]]:
        '''binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#binding GcpSecretRoleset#binding}
        '''
        result = self._values.get("binding")
        assert result is not None, "Required property 'binding' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[GcpSecretRolesetBinding]], result)

    @builtins.property
    def project(self) -> builtins.str:
        '''Name of the GCP project that this roleset's service account will belong to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#project GcpSecretRoleset#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roleset(self) -> builtins.str:
        '''Name of the RoleSet to create.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#roleset GcpSecretRoleset#roleset}
        '''
        result = self._values.get("roleset")
        assert result is not None, "Required property 'roleset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#id GcpSecretRoleset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#namespace GcpSecretRoleset#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_type(self) -> typing.Optional[builtins.str]:
        '''Type of secret generated for this role set. Defaults to ``access_token``. Accepted values: ``access_token``, ``service_account_key``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#secret_type GcpSecretRoleset#secret_type}
        '''
        result = self._values.get("secret_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of OAuth scopes to assign to ``access_token`` secrets generated under this role set (``access_token`` role sets only).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_roleset#token_scopes GcpSecretRoleset#token_scopes}
        '''
        result = self._values.get("token_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GcpSecretRolesetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GcpSecretRoleset",
    "GcpSecretRolesetBinding",
    "GcpSecretRolesetBindingList",
    "GcpSecretRolesetBindingOutputReference",
    "GcpSecretRolesetConfig",
]

publication.publish()
