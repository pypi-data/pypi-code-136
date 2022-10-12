'''
# `vault_identity_mfa_login_enforcement`

Refer to the Terraform Registory for docs: [`vault_identity_mfa_login_enforcement`](https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement).
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


class IdentityMfaLoginEnforcement(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.identityMfaLoginEnforcement.IdentityMfaLoginEnforcement",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement vault_identity_mfa_login_enforcement}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        mfa_method_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        auth_method_accessors: typing.Optional[typing.Sequence[builtins.str]] = None,
        auth_method_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        identity_entity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement vault_identity_mfa_login_enforcement} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param mfa_method_ids: Set of MFA method UUIDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#mfa_method_ids IdentityMfaLoginEnforcement#mfa_method_ids}
        :param name: Login enforcement name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#name IdentityMfaLoginEnforcement#name}
        :param auth_method_accessors: Set of auth method accessor IDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#auth_method_accessors IdentityMfaLoginEnforcement#auth_method_accessors}
        :param auth_method_types: Set of auth method types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#auth_method_types IdentityMfaLoginEnforcement#auth_method_types}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#id IdentityMfaLoginEnforcement#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_entity_ids: Set of identity entity IDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#identity_entity_ids IdentityMfaLoginEnforcement#identity_entity_ids}
        :param identity_group_ids: Set of identity group IDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#identity_group_ids IdentityMfaLoginEnforcement#identity_group_ids}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#namespace IdentityMfaLoginEnforcement#namespace}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(IdentityMfaLoginEnforcement.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = IdentityMfaLoginEnforcementConfig(
            mfa_method_ids=mfa_method_ids,
            name=name,
            auth_method_accessors=auth_method_accessors,
            auth_method_types=auth_method_types,
            id=id,
            identity_entity_ids=identity_entity_ids,
            identity_group_ids=identity_group_ids,
            namespace=namespace,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAuthMethodAccessors")
    def reset_auth_method_accessors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethodAccessors", []))

    @jsii.member(jsii_name="resetAuthMethodTypes")
    def reset_auth_method_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthMethodTypes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentityEntityIds")
    def reset_identity_entity_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityEntityIds", []))

    @jsii.member(jsii_name="resetIdentityGroupIds")
    def reset_identity_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityGroupIds", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @builtins.property
    @jsii.member(jsii_name="namespacePath")
    def namespace_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespacePath"))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="authMethodAccessorsInput")
    def auth_method_accessors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authMethodAccessorsInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodTypesInput")
    def auth_method_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authMethodTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="identityEntityIdsInput")
    def identity_entity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityEntityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityGroupIdsInput")
    def identity_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mfaMethodIdsInput")
    def mfa_method_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mfaMethodIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="authMethodAccessors")
    def auth_method_accessors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authMethodAccessors"))

    @auth_method_accessors.setter
    def auth_method_accessors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "auth_method_accessors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethodAccessors", value)

    @builtins.property
    @jsii.member(jsii_name="authMethodTypes")
    def auth_method_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authMethodTypes"))

    @auth_method_types.setter
    def auth_method_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "auth_method_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMethodTypes", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identityEntityIds")
    def identity_entity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityEntityIds"))

    @identity_entity_ids.setter
    def identity_entity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "identity_entity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityEntityIds", value)

    @builtins.property
    @jsii.member(jsii_name="identityGroupIds")
    def identity_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityGroupIds"))

    @identity_group_ids.setter
    def identity_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "identity_group_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="mfaMethodIds")
    def mfa_method_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mfaMethodIds"))

    @mfa_method_ids.setter
    def mfa_method_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "mfa_method_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mfaMethodIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(IdentityMfaLoginEnforcement, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.identityMfaLoginEnforcement.IdentityMfaLoginEnforcementConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "mfa_method_ids": "mfaMethodIds",
        "name": "name",
        "auth_method_accessors": "authMethodAccessors",
        "auth_method_types": "authMethodTypes",
        "id": "id",
        "identity_entity_ids": "identityEntityIds",
        "identity_group_ids": "identityGroupIds",
        "namespace": "namespace",
    },
)
class IdentityMfaLoginEnforcementConfig(cdktf.TerraformMetaArguments):
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
        mfa_method_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        auth_method_accessors: typing.Optional[typing.Sequence[builtins.str]] = None,
        auth_method_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        identity_entity_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param mfa_method_ids: Set of MFA method UUIDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#mfa_method_ids IdentityMfaLoginEnforcement#mfa_method_ids}
        :param name: Login enforcement name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#name IdentityMfaLoginEnforcement#name}
        :param auth_method_accessors: Set of auth method accessor IDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#auth_method_accessors IdentityMfaLoginEnforcement#auth_method_accessors}
        :param auth_method_types: Set of auth method types. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#auth_method_types IdentityMfaLoginEnforcement#auth_method_types}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#id IdentityMfaLoginEnforcement#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity_entity_ids: Set of identity entity IDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#identity_entity_ids IdentityMfaLoginEnforcement#identity_entity_ids}
        :param identity_group_ids: Set of identity group IDs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#identity_group_ids IdentityMfaLoginEnforcement#identity_group_ids}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#namespace IdentityMfaLoginEnforcement#namespace}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(IdentityMfaLoginEnforcementConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument mfa_method_ids", value=mfa_method_ids, expected_type=type_hints["mfa_method_ids"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument auth_method_accessors", value=auth_method_accessors, expected_type=type_hints["auth_method_accessors"])
            check_type(argname="argument auth_method_types", value=auth_method_types, expected_type=type_hints["auth_method_types"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity_entity_ids", value=identity_entity_ids, expected_type=type_hints["identity_entity_ids"])
            check_type(argname="argument identity_group_ids", value=identity_group_ids, expected_type=type_hints["identity_group_ids"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "mfa_method_ids": mfa_method_ids,
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
        if auth_method_accessors is not None:
            self._values["auth_method_accessors"] = auth_method_accessors
        if auth_method_types is not None:
            self._values["auth_method_types"] = auth_method_types
        if id is not None:
            self._values["id"] = id
        if identity_entity_ids is not None:
            self._values["identity_entity_ids"] = identity_entity_ids
        if identity_group_ids is not None:
            self._values["identity_group_ids"] = identity_group_ids
        if namespace is not None:
            self._values["namespace"] = namespace

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
    def mfa_method_ids(self) -> typing.List[builtins.str]:
        '''Set of MFA method UUIDs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#mfa_method_ids IdentityMfaLoginEnforcement#mfa_method_ids}
        '''
        result = self._values.get("mfa_method_ids")
        assert result is not None, "Required property 'mfa_method_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Login enforcement name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#name IdentityMfaLoginEnforcement#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_method_accessors(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of auth method accessor IDs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#auth_method_accessors IdentityMfaLoginEnforcement#auth_method_accessors}
        '''
        result = self._values.get("auth_method_accessors")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def auth_method_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of auth method types.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#auth_method_types IdentityMfaLoginEnforcement#auth_method_types}
        '''
        result = self._values.get("auth_method_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#id IdentityMfaLoginEnforcement#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_entity_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of identity entity IDs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#identity_entity_ids IdentityMfaLoginEnforcement#identity_entity_ids}
        '''
        result = self._values.get("identity_entity_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of identity group IDs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#identity_group_ids IdentityMfaLoginEnforcement#identity_group_ids}
        '''
        result = self._values.get("identity_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/identity_mfa_login_enforcement#namespace IdentityMfaLoginEnforcement#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityMfaLoginEnforcementConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IdentityMfaLoginEnforcement",
    "IdentityMfaLoginEnforcementConfig",
]

publication.publish()
