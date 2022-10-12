'''
# `data_vault_identity_group`

Refer to the Terraform Registory for docs: [`data_vault_identity_group`](https://www.terraform.io/docs/providers/vault/d/identity_group).
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


class DataVaultIdentityGroup(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.dataVaultIdentityGroup.DataVaultIdentityGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/d/identity_group vault_identity_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        alias_id: typing.Optional[builtins.str] = None,
        alias_mount_accessor: typing.Optional[builtins.str] = None,
        alias_name: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/d/identity_group vault_identity_group} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias_id: ID of the alias. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_id DataVaultIdentityGroup#alias_id}
        :param alias_mount_accessor: Accessor of the mount to which the alias belongs to. This should be supplied in conjunction with ``alias_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_mount_accessor DataVaultIdentityGroup#alias_mount_accessor}
        :param alias_name: Name of the alias. This should be supplied in conjunction with ``alias_mount_accessor``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_name DataVaultIdentityGroup#alias_name}
        :param group_id: ID of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#group_id DataVaultIdentityGroup#group_id}
        :param group_name: Name of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#group_name DataVaultIdentityGroup#group_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#id DataVaultIdentityGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#namespace DataVaultIdentityGroup#namespace}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataVaultIdentityGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataVaultIdentityGroupConfig(
            alias_id=alias_id,
            alias_mount_accessor=alias_mount_accessor,
            alias_name=alias_name,
            group_id=group_id,
            group_name=group_name,
            id=id,
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

    @jsii.member(jsii_name="resetAliasId")
    def reset_alias_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliasId", []))

    @jsii.member(jsii_name="resetAliasMountAccessor")
    def reset_alias_mount_accessor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliasMountAccessor", []))

    @jsii.member(jsii_name="resetAliasName")
    def reset_alias_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAliasName", []))

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetGroupName")
    def reset_group_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="aliasCanonicalId")
    def alias_canonical_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasCanonicalId"))

    @builtins.property
    @jsii.member(jsii_name="aliasCreationTime")
    def alias_creation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="aliasLastUpdateTime")
    def alias_last_update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasLastUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="aliasMergedFromCanonicalIds")
    def alias_merged_from_canonical_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "aliasMergedFromCanonicalIds"))

    @builtins.property
    @jsii.member(jsii_name="aliasMetadata")
    def alias_metadata(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "aliasMetadata"))

    @builtins.property
    @jsii.member(jsii_name="aliasMountPath")
    def alias_mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasMountPath"))

    @builtins.property
    @jsii.member(jsii_name="aliasMountType")
    def alias_mount_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasMountType"))

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="dataJson")
    def data_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataJson"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdateTime")
    def last_update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="memberEntityIds")
    def member_entity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "memberEntityIds"))

    @builtins.property
    @jsii.member(jsii_name="memberGroupIds")
    def member_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "memberGroupIds"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="modifyIndex")
    def modify_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "modifyIndex"))

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @builtins.property
    @jsii.member(jsii_name="parentGroupIds")
    def parent_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "parentGroupIds"))

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="aliasIdInput")
    def alias_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasIdInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasMountAccessorInput")
    def alias_mount_accessor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasMountAccessorInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasNameInput")
    def alias_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasNameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNameInput")
    def group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="aliasId")
    def alias_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasId"))

    @alias_id.setter
    def alias_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultIdentityGroup, "alias_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliasId", value)

    @builtins.property
    @jsii.member(jsii_name="aliasMountAccessor")
    def alias_mount_accessor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasMountAccessor"))

    @alias_mount_accessor.setter
    def alias_mount_accessor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultIdentityGroup, "alias_mount_accessor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliasMountAccessor", value)

    @builtins.property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aliasName"))

    @alias_name.setter
    def alias_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultIdentityGroup, "alias_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliasName", value)

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultIdentityGroup, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="groupName")
    def group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupName"))

    @group_name.setter
    def group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultIdentityGroup, "group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultIdentityGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataVaultIdentityGroup, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.dataVaultIdentityGroup.DataVaultIdentityGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "alias_id": "aliasId",
        "alias_mount_accessor": "aliasMountAccessor",
        "alias_name": "aliasName",
        "group_id": "groupId",
        "group_name": "groupName",
        "id": "id",
        "namespace": "namespace",
    },
)
class DataVaultIdentityGroupConfig(cdktf.TerraformMetaArguments):
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
        alias_id: typing.Optional[builtins.str] = None,
        alias_mount_accessor: typing.Optional[builtins.str] = None,
        alias_name: typing.Optional[builtins.str] = None,
        group_id: typing.Optional[builtins.str] = None,
        group_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
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
        :param alias_id: ID of the alias. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_id DataVaultIdentityGroup#alias_id}
        :param alias_mount_accessor: Accessor of the mount to which the alias belongs to. This should be supplied in conjunction with ``alias_name``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_mount_accessor DataVaultIdentityGroup#alias_mount_accessor}
        :param alias_name: Name of the alias. This should be supplied in conjunction with ``alias_mount_accessor``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_name DataVaultIdentityGroup#alias_name}
        :param group_id: ID of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#group_id DataVaultIdentityGroup#group_id}
        :param group_name: Name of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#group_name DataVaultIdentityGroup#group_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#id DataVaultIdentityGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#namespace DataVaultIdentityGroup#namespace}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataVaultIdentityGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument alias_id", value=alias_id, expected_type=type_hints["alias_id"])
            check_type(argname="argument alias_mount_accessor", value=alias_mount_accessor, expected_type=type_hints["alias_mount_accessor"])
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
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
        if alias_id is not None:
            self._values["alias_id"] = alias_id
        if alias_mount_accessor is not None:
            self._values["alias_mount_accessor"] = alias_mount_accessor
        if alias_name is not None:
            self._values["alias_name"] = alias_name
        if group_id is not None:
            self._values["group_id"] = group_id
        if group_name is not None:
            self._values["group_name"] = group_name
        if id is not None:
            self._values["id"] = id
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
    def alias_id(self) -> typing.Optional[builtins.str]:
        '''ID of the alias.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_id DataVaultIdentityGroup#alias_id}
        '''
        result = self._values.get("alias_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias_mount_accessor(self) -> typing.Optional[builtins.str]:
        '''Accessor of the mount to which the alias belongs to. This should be supplied in conjunction with ``alias_name``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_mount_accessor DataVaultIdentityGroup#alias_mount_accessor}
        '''
        result = self._values.get("alias_mount_accessor")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias_name(self) -> typing.Optional[builtins.str]:
        '''Name of the alias. This should be supplied in conjunction with ``alias_mount_accessor``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#alias_name DataVaultIdentityGroup#alias_name}
        '''
        result = self._values.get("alias_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_id(self) -> typing.Optional[builtins.str]:
        '''ID of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#group_id DataVaultIdentityGroup#group_id}
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_name(self) -> typing.Optional[builtins.str]:
        '''Name of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#group_name DataVaultIdentityGroup#group_name}
        '''
        result = self._values.get("group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#id DataVaultIdentityGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/d/identity_group#namespace DataVaultIdentityGroup#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataVaultIdentityGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataVaultIdentityGroup",
    "DataVaultIdentityGroupConfig",
]

publication.publish()
