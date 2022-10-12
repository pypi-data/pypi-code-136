'''
# `snowflake_role_ownership_grant`

Refer to the Terraform Registory for docs: [`snowflake_role_ownership_grant`](https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant).
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


class RoleOwnershipGrant(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.roleOwnershipGrant.RoleOwnershipGrant",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant snowflake_role_ownership_grant}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        on_role_name: builtins.str,
        to_role_name: builtins.str,
        current_grants: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant snowflake_role_ownership_grant} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param on_role_name: The name of the role ownership is granted on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#on_role_name RoleOwnershipGrant#on_role_name}
        :param to_role_name: The name of the role to grant ownership. Please ensure that the role that terraform is using is granted access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#to_role_name RoleOwnershipGrant#to_role_name}
        :param current_grants: Specifies whether to remove or transfer all existing outbound privileges on the object when ownership is transferred to a new role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#current_grants RoleOwnershipGrant#current_grants}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#id RoleOwnershipGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleOwnershipGrant.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RoleOwnershipGrantConfig(
            on_role_name=on_role_name,
            to_role_name=to_role_name,
            current_grants=current_grants,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCurrentGrants")
    def reset_current_grants(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCurrentGrants", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="currentGrantsInput")
    def current_grants_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentGrantsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="onRoleNameInput")
    def on_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="toRoleNameInput")
    def to_role_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "toRoleNameInput"))

    @builtins.property
    @jsii.member(jsii_name="currentGrants")
    def current_grants(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "currentGrants"))

    @current_grants.setter
    def current_grants(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleOwnershipGrant, "current_grants").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentGrants", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleOwnershipGrant, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="onRoleName")
    def on_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onRoleName"))

    @on_role_name.setter
    def on_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleOwnershipGrant, "on_role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onRoleName", value)

    @builtins.property
    @jsii.member(jsii_name="toRoleName")
    def to_role_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "toRoleName"))

    @to_role_name.setter
    def to_role_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleOwnershipGrant, "to_role_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "toRoleName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.roleOwnershipGrant.RoleOwnershipGrantConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "on_role_name": "onRoleName",
        "to_role_name": "toRoleName",
        "current_grants": "currentGrants",
        "id": "id",
    },
)
class RoleOwnershipGrantConfig(cdktf.TerraformMetaArguments):
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
        on_role_name: builtins.str,
        to_role_name: builtins.str,
        current_grants: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param on_role_name: The name of the role ownership is granted on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#on_role_name RoleOwnershipGrant#on_role_name}
        :param to_role_name: The name of the role to grant ownership. Please ensure that the role that terraform is using is granted access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#to_role_name RoleOwnershipGrant#to_role_name}
        :param current_grants: Specifies whether to remove or transfer all existing outbound privileges on the object when ownership is transferred to a new role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#current_grants RoleOwnershipGrant#current_grants}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#id RoleOwnershipGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(RoleOwnershipGrantConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument on_role_name", value=on_role_name, expected_type=type_hints["on_role_name"])
            check_type(argname="argument to_role_name", value=to_role_name, expected_type=type_hints["to_role_name"])
            check_type(argname="argument current_grants", value=current_grants, expected_type=type_hints["current_grants"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "on_role_name": on_role_name,
            "to_role_name": to_role_name,
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
        if current_grants is not None:
            self._values["current_grants"] = current_grants
        if id is not None:
            self._values["id"] = id

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
    def on_role_name(self) -> builtins.str:
        '''The name of the role ownership is granted on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#on_role_name RoleOwnershipGrant#on_role_name}
        '''
        result = self._values.get("on_role_name")
        assert result is not None, "Required property 'on_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def to_role_name(self) -> builtins.str:
        '''The name of the role to grant ownership.

        Please ensure that the role that terraform is using is granted access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#to_role_name RoleOwnershipGrant#to_role_name}
        '''
        result = self._values.get("to_role_name")
        assert result is not None, "Required property 'to_role_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def current_grants(self) -> typing.Optional[builtins.str]:
        '''Specifies whether to remove or transfer all existing outbound privileges on the object when ownership is transferred to a new role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#current_grants RoleOwnershipGrant#current_grants}
        '''
        result = self._values.get("current_grants")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/role_ownership_grant#id RoleOwnershipGrant#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleOwnershipGrantConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RoleOwnershipGrant",
    "RoleOwnershipGrantConfig",
]

publication.publish()
