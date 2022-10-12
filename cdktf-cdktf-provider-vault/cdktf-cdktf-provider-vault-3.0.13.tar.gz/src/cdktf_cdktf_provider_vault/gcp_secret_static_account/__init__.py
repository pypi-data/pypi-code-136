'''
# `vault_gcp_secret_static_account`

Refer to the Terraform Registory for docs: [`vault_gcp_secret_static_account`](https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account).
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


class GcpSecretStaticAccount(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpSecretStaticAccount.GcpSecretStaticAccount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account vault_gcp_secret_static_account}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: builtins.str,
        service_account_email: builtins.str,
        static_account: builtins.str,
        binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GcpSecretStaticAccountBinding", typing.Dict[str, typing.Any]]]]] = None,
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
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account vault_gcp_secret_static_account} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: Path where the GCP secrets engine is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#backend GcpSecretStaticAccount#backend}
        :param service_account_email: Email of the GCP service account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#service_account_email GcpSecretStaticAccount#service_account_email}
        :param static_account: Name of the Static Account to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#static_account GcpSecretStaticAccount#static_account}
        :param binding: binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#binding GcpSecretStaticAccount#binding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#id GcpSecretStaticAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#namespace GcpSecretStaticAccount#namespace}
        :param secret_type: Type of secret generated for this static account. Defaults to ``access_token``. Accepted values: ``access_token``, ``service_account_key``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#secret_type GcpSecretStaticAccount#secret_type}
        :param token_scopes: List of OAuth scopes to assign to ``access_token`` secrets generated under this static account (``access_token`` static accounts only). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#token_scopes GcpSecretStaticAccount#token_scopes}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretStaticAccount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GcpSecretStaticAccountConfig(
            backend=backend,
            service_account_email=service_account_email,
            static_account=static_account,
            binding=binding,
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GcpSecretStaticAccountBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretStaticAccount.put_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBinding", [value]))

    @jsii.member(jsii_name="resetBinding")
    def reset_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBinding", []))

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
    def binding(self) -> "GcpSecretStaticAccountBindingList":
        return typing.cast("GcpSecretStaticAccountBindingList", jsii.get(self, "binding"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountProject")
    def service_account_project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountProject"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="bindingInput")
    def binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GcpSecretStaticAccountBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GcpSecretStaticAccountBinding"]]], jsii.get(self, "bindingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="secretTypeInput")
    def secret_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmailInput")
    def service_account_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="staticAccountInput")
    def static_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "staticAccountInput"))

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
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccount, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccount, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccount, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="secretType")
    def secret_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretType"))

    @secret_type.setter
    def secret_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccount, "secret_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretType", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmail")
    def service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmail"))

    @service_account_email.setter
    def service_account_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccount, "service_account_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountEmail", value)

    @builtins.property
    @jsii.member(jsii_name="staticAccount")
    def static_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "staticAccount"))

    @static_account.setter
    def static_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccount, "static_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "staticAccount", value)

    @builtins.property
    @jsii.member(jsii_name="tokenScopes")
    def token_scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenScopes"))

    @token_scopes.setter
    def token_scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccount, "token_scopes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenScopes", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.gcpSecretStaticAccount.GcpSecretStaticAccountBinding",
    jsii_struct_bases=[],
    name_mapping={"resource": "resource", "roles": "roles"},
)
class GcpSecretStaticAccountBinding:
    def __init__(
        self,
        *,
        resource: builtins.str,
        roles: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param resource: Resource name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#resource GcpSecretStaticAccount#resource}
        :param roles: List of roles to apply to the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#roles GcpSecretStaticAccount#roles}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretStaticAccountBinding.__init__)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
        self._values: typing.Dict[str, typing.Any] = {
            "resource": resource,
            "roles": roles,
        }

    @builtins.property
    def resource(self) -> builtins.str:
        '''Resource name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#resource GcpSecretStaticAccount#resource}
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(self) -> typing.List[builtins.str]:
        '''List of roles to apply to the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#roles GcpSecretStaticAccount#roles}
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GcpSecretStaticAccountBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GcpSecretStaticAccountBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpSecretStaticAccount.GcpSecretStaticAccountBindingList",
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
            type_hints = typing.get_type_hints(GcpSecretStaticAccountBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GcpSecretStaticAccountBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretStaticAccountBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GcpSecretStaticAccountBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccountBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccountBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccountBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretStaticAccountBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretStaticAccountBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretStaticAccountBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccountBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GcpSecretStaticAccountBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.gcpSecretStaticAccount.GcpSecretStaticAccountBindingOutputReference",
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
            type_hints = typing.get_type_hints(GcpSecretStaticAccountBindingOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccountBindingOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccountBindingOutputReference, "roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GcpSecretStaticAccountBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GcpSecretStaticAccountBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GcpSecretStaticAccountBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GcpSecretStaticAccountBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.gcpSecretStaticAccount.GcpSecretStaticAccountConfig",
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
        "service_account_email": "serviceAccountEmail",
        "static_account": "staticAccount",
        "binding": "binding",
        "id": "id",
        "namespace": "namespace",
        "secret_type": "secretType",
        "token_scopes": "tokenScopes",
    },
)
class GcpSecretStaticAccountConfig(cdktf.TerraformMetaArguments):
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
        service_account_email: builtins.str,
        static_account: builtins.str,
        binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GcpSecretStaticAccountBinding, typing.Dict[str, typing.Any]]]]] = None,
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
        :param backend: Path where the GCP secrets engine is mounted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#backend GcpSecretStaticAccount#backend}
        :param service_account_email: Email of the GCP service account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#service_account_email GcpSecretStaticAccount#service_account_email}
        :param static_account: Name of the Static Account to create. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#static_account GcpSecretStaticAccount#static_account}
        :param binding: binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#binding GcpSecretStaticAccount#binding}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#id GcpSecretStaticAccount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#namespace GcpSecretStaticAccount#namespace}
        :param secret_type: Type of secret generated for this static account. Defaults to ``access_token``. Accepted values: ``access_token``, ``service_account_key``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#secret_type GcpSecretStaticAccount#secret_type}
        :param token_scopes: List of OAuth scopes to assign to ``access_token`` secrets generated under this static account (``access_token`` static accounts only). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#token_scopes GcpSecretStaticAccount#token_scopes}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GcpSecretStaticAccountConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument service_account_email", value=service_account_email, expected_type=type_hints["service_account_email"])
            check_type(argname="argument static_account", value=static_account, expected_type=type_hints["static_account"])
            check_type(argname="argument binding", value=binding, expected_type=type_hints["binding"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument secret_type", value=secret_type, expected_type=type_hints["secret_type"])
            check_type(argname="argument token_scopes", value=token_scopes, expected_type=type_hints["token_scopes"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend": backend,
            "service_account_email": service_account_email,
            "static_account": static_account,
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
        if binding is not None:
            self._values["binding"] = binding
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#backend GcpSecretStaticAccount#backend}
        '''
        result = self._values.get("backend")
        assert result is not None, "Required property 'backend' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_account_email(self) -> builtins.str:
        '''Email of the GCP service account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#service_account_email GcpSecretStaticAccount#service_account_email}
        '''
        result = self._values.get("service_account_email")
        assert result is not None, "Required property 'service_account_email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def static_account(self) -> builtins.str:
        '''Name of the Static Account to create.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#static_account GcpSecretStaticAccount#static_account}
        '''
        result = self._values.get("static_account")
        assert result is not None, "Required property 'static_account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretStaticAccountBinding]]]:
        '''binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#binding GcpSecretStaticAccount#binding}
        '''
        result = self._values.get("binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GcpSecretStaticAccountBinding]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#id GcpSecretStaticAccount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#namespace GcpSecretStaticAccount#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_type(self) -> typing.Optional[builtins.str]:
        '''Type of secret generated for this static account. Defaults to ``access_token``. Accepted values: ``access_token``, ``service_account_key``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#secret_type GcpSecretStaticAccount#secret_type}
        '''
        result = self._values.get("secret_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of OAuth scopes to assign to ``access_token`` secrets generated under this static account (``access_token`` static accounts only).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/gcp_secret_static_account#token_scopes GcpSecretStaticAccount#token_scopes}
        '''
        result = self._values.get("token_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GcpSecretStaticAccountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GcpSecretStaticAccount",
    "GcpSecretStaticAccountBinding",
    "GcpSecretStaticAccountBindingList",
    "GcpSecretStaticAccountBindingOutputReference",
    "GcpSecretStaticAccountConfig",
]

publication.publish()
