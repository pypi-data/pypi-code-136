'''
# `snowflake_procedure_grant`

Refer to the Terraform Registory for docs: [`snowflake_procedure_grant`](https://www.terraform.io/docs/providers/snowflake/r/procedure_grant).
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


class ProcedureGrant(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.procedureGrant.ProcedureGrant",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant snowflake_procedure_grant}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        database_name: builtins.str,
        schema_name: builtins.str,
        arguments: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ProcedureGrantArguments", typing.Dict[str, typing.Any]]]]] = None,
        enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        on_future: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        privilege: typing.Optional[builtins.str] = None,
        procedure_name: typing.Optional[builtins.str] = None,
        return_type: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        shares: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_grant_option: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant snowflake_procedure_grant} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database_name: The name of the database containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#database_name ProcedureGrant#database_name}
        :param schema_name: The name of the schema containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#schema_name ProcedureGrant#schema_name}
        :param arguments: arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#arguments ProcedureGrant#arguments}
        :param enable_multiple_grants: When this is set to true, multiple grants of the same type can be created. This will cause Terraform to not revoke grants applied to roles and objects outside Terraform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#enable_multiple_grants ProcedureGrant#enable_multiple_grants}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#id ProcedureGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_future: When this is set to true and a schema_name is provided, apply this grant on all future procedures in the given schema. When this is true and no schema_name is provided apply this grant on all future procedures in the given database. The procedure_name and shares fields must be unset in order to use on_future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#on_future ProcedureGrant#on_future}
        :param privilege: The privilege to grant on the current or future procedure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#privilege ProcedureGrant#privilege}
        :param procedure_name: The name of the procedure on which to grant privileges immediately (only valid if on_future is false). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#procedure_name ProcedureGrant#procedure_name}
        :param return_type: The return type of the procedure (must be present if procedure_name is present). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#return_type ProcedureGrant#return_type}
        :param roles: Grants privilege to these roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#roles ProcedureGrant#roles}
        :param shares: Grants privilege to these shares (only valid if on_future is false). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#shares ProcedureGrant#shares}
        :param with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#with_grant_option ProcedureGrant#with_grant_option}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProcedureGrant.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProcedureGrantConfig(
            database_name=database_name,
            schema_name=schema_name,
            arguments=arguments,
            enable_multiple_grants=enable_multiple_grants,
            id=id,
            on_future=on_future,
            privilege=privilege,
            procedure_name=procedure_name,
            return_type=return_type,
            roles=roles,
            shares=shares,
            with_grant_option=with_grant_option,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putArguments")
    def put_arguments(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ProcedureGrantArguments", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProcedureGrant.put_arguments)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putArguments", [value]))

    @jsii.member(jsii_name="resetArguments")
    def reset_arguments(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArguments", []))

    @jsii.member(jsii_name="resetEnableMultipleGrants")
    def reset_enable_multiple_grants(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableMultipleGrants", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOnFuture")
    def reset_on_future(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnFuture", []))

    @jsii.member(jsii_name="resetPrivilege")
    def reset_privilege(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivilege", []))

    @jsii.member(jsii_name="resetProcedureName")
    def reset_procedure_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProcedureName", []))

    @jsii.member(jsii_name="resetReturnType")
    def reset_return_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnType", []))

    @jsii.member(jsii_name="resetRoles")
    def reset_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoles", []))

    @jsii.member(jsii_name="resetShares")
    def reset_shares(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShares", []))

    @jsii.member(jsii_name="resetWithGrantOption")
    def reset_with_grant_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithGrantOption", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arguments")
    def arguments(self) -> "ProcedureGrantArgumentsList":
        return typing.cast("ProcedureGrantArgumentsList", jsii.get(self, "arguments"))

    @builtins.property
    @jsii.member(jsii_name="argumentsInput")
    def arguments_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ProcedureGrantArguments"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ProcedureGrantArguments"]]], jsii.get(self, "argumentsInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableMultipleGrantsInput")
    def enable_multiple_grants_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableMultipleGrantsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="onFutureInput")
    def on_future_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onFutureInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegeInput")
    def privilege_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privilegeInput"))

    @builtins.property
    @jsii.member(jsii_name="procedureNameInput")
    def procedure_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "procedureNameInput"))

    @builtins.property
    @jsii.member(jsii_name="returnTypeInput")
    def return_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "returnTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaNameInput")
    def schema_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sharesInput")
    def shares_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sharesInput"))

    @builtins.property
    @jsii.member(jsii_name="withGrantOptionInput")
    def with_grant_option_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withGrantOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="enableMultipleGrants")
    def enable_multiple_grants(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableMultipleGrants"))

    @enable_multiple_grants.setter
    def enable_multiple_grants(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "enable_multiple_grants").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableMultipleGrants", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="onFuture")
    def on_future(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onFuture"))

    @on_future.setter
    def on_future(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "on_future").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onFuture", value)

    @builtins.property
    @jsii.member(jsii_name="privilege")
    def privilege(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privilege"))

    @privilege.setter
    def privilege(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "privilege").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privilege", value)

    @builtins.property
    @jsii.member(jsii_name="procedureName")
    def procedure_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "procedureName"))

    @procedure_name.setter
    def procedure_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "procedure_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "procedureName", value)

    @builtins.property
    @jsii.member(jsii_name="returnType")
    def return_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "returnType"))

    @return_type.setter
    def return_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "return_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnType", value)

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roles"))

    @roles.setter
    def roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roles", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "schema_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="shares")
    def shares(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "shares"))

    @shares.setter
    def shares(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "shares").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shares", value)

    @builtins.property
    @jsii.member(jsii_name="withGrantOption")
    def with_grant_option(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withGrantOption"))

    @with_grant_option.setter
    def with_grant_option(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrant, "with_grant_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withGrantOption", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.procedureGrant.ProcedureGrantArguments",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class ProcedureGrantArguments:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: The argument name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#name ProcedureGrant#name}
        :param type: The argument type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#type ProcedureGrant#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProcedureGrantArguments.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The argument name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#name ProcedureGrant#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The argument type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#type ProcedureGrant#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcedureGrantArguments(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProcedureGrantArgumentsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.procedureGrant.ProcedureGrantArgumentsList",
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
            type_hints = typing.get_type_hints(ProcedureGrantArgumentsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProcedureGrantArgumentsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProcedureGrantArgumentsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProcedureGrantArgumentsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrantArgumentsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ProcedureGrantArgumentsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ProcedureGrantArgumentsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProcedureGrantArguments]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProcedureGrantArguments]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProcedureGrantArguments]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrantArgumentsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProcedureGrantArgumentsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.procedureGrant.ProcedureGrantArgumentsOutputReference",
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
            type_hints = typing.get_type_hints(ProcedureGrantArgumentsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrantArgumentsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrantArgumentsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ProcedureGrantArguments, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ProcedureGrantArguments, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ProcedureGrantArguments, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProcedureGrantArgumentsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.procedureGrant.ProcedureGrantConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database_name": "databaseName",
        "schema_name": "schemaName",
        "arguments": "arguments",
        "enable_multiple_grants": "enableMultipleGrants",
        "id": "id",
        "on_future": "onFuture",
        "privilege": "privilege",
        "procedure_name": "procedureName",
        "return_type": "returnType",
        "roles": "roles",
        "shares": "shares",
        "with_grant_option": "withGrantOption",
    },
)
class ProcedureGrantConfig(cdktf.TerraformMetaArguments):
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
        database_name: builtins.str,
        schema_name: builtins.str,
        arguments: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ProcedureGrantArguments, typing.Dict[str, typing.Any]]]]] = None,
        enable_multiple_grants: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        on_future: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        privilege: typing.Optional[builtins.str] = None,
        procedure_name: typing.Optional[builtins.str] = None,
        return_type: typing.Optional[builtins.str] = None,
        roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        shares: typing.Optional[typing.Sequence[builtins.str]] = None,
        with_grant_option: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database_name: The name of the database containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#database_name ProcedureGrant#database_name}
        :param schema_name: The name of the schema containing the current or future procedures on which to grant privileges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#schema_name ProcedureGrant#schema_name}
        :param arguments: arguments block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#arguments ProcedureGrant#arguments}
        :param enable_multiple_grants: When this is set to true, multiple grants of the same type can be created. This will cause Terraform to not revoke grants applied to roles and objects outside Terraform. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#enable_multiple_grants ProcedureGrant#enable_multiple_grants}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#id ProcedureGrant#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param on_future: When this is set to true and a schema_name is provided, apply this grant on all future procedures in the given schema. When this is true and no schema_name is provided apply this grant on all future procedures in the given database. The procedure_name and shares fields must be unset in order to use on_future. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#on_future ProcedureGrant#on_future}
        :param privilege: The privilege to grant on the current or future procedure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#privilege ProcedureGrant#privilege}
        :param procedure_name: The name of the procedure on which to grant privileges immediately (only valid if on_future is false). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#procedure_name ProcedureGrant#procedure_name}
        :param return_type: The return type of the procedure (must be present if procedure_name is present). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#return_type ProcedureGrant#return_type}
        :param roles: Grants privilege to these roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#roles ProcedureGrant#roles}
        :param shares: Grants privilege to these shares (only valid if on_future is false). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#shares ProcedureGrant#shares}
        :param with_grant_option: When this is set to true, allows the recipient role to grant the privileges to other roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#with_grant_option ProcedureGrant#with_grant_option}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ProcedureGrantConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument arguments", value=arguments, expected_type=type_hints["arguments"])
            check_type(argname="argument enable_multiple_grants", value=enable_multiple_grants, expected_type=type_hints["enable_multiple_grants"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument on_future", value=on_future, expected_type=type_hints["on_future"])
            check_type(argname="argument privilege", value=privilege, expected_type=type_hints["privilege"])
            check_type(argname="argument procedure_name", value=procedure_name, expected_type=type_hints["procedure_name"])
            check_type(argname="argument return_type", value=return_type, expected_type=type_hints["return_type"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument shares", value=shares, expected_type=type_hints["shares"])
            check_type(argname="argument with_grant_option", value=with_grant_option, expected_type=type_hints["with_grant_option"])
        self._values: typing.Dict[str, typing.Any] = {
            "database_name": database_name,
            "schema_name": schema_name,
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
        if arguments is not None:
            self._values["arguments"] = arguments
        if enable_multiple_grants is not None:
            self._values["enable_multiple_grants"] = enable_multiple_grants
        if id is not None:
            self._values["id"] = id
        if on_future is not None:
            self._values["on_future"] = on_future
        if privilege is not None:
            self._values["privilege"] = privilege
        if procedure_name is not None:
            self._values["procedure_name"] = procedure_name
        if return_type is not None:
            self._values["return_type"] = return_type
        if roles is not None:
            self._values["roles"] = roles
        if shares is not None:
            self._values["shares"] = shares
        if with_grant_option is not None:
            self._values["with_grant_option"] = with_grant_option

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
    def database_name(self) -> builtins.str:
        '''The name of the database containing the current or future procedures on which to grant privileges.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#database_name ProcedureGrant#database_name}
        '''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_name(self) -> builtins.str:
        '''The name of the schema containing the current or future procedures on which to grant privileges.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#schema_name ProcedureGrant#schema_name}
        '''
        result = self._values.get("schema_name")
        assert result is not None, "Required property 'schema_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arguments(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProcedureGrantArguments]]]:
        '''arguments block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#arguments ProcedureGrant#arguments}
        '''
        result = self._values.get("arguments")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProcedureGrantArguments]]], result)

    @builtins.property
    def enable_multiple_grants(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When this is set to true, multiple grants of the same type can be created.

        This will cause Terraform to not revoke grants applied to roles and objects outside Terraform.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#enable_multiple_grants ProcedureGrant#enable_multiple_grants}
        '''
        result = self._values.get("enable_multiple_grants")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#id ProcedureGrant#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_future(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When this is set to true and a schema_name is provided, apply this grant on all future procedures in the given schema.

        When this is true and no schema_name is provided apply this grant on all future procedures in the given database. The procedure_name and shares fields must be unset in order to use on_future.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#on_future ProcedureGrant#on_future}
        '''
        result = self._values.get("on_future")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def privilege(self) -> typing.Optional[builtins.str]:
        '''The privilege to grant on the current or future procedure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#privilege ProcedureGrant#privilege}
        '''
        result = self._values.get("privilege")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def procedure_name(self) -> typing.Optional[builtins.str]:
        '''The name of the procedure on which to grant privileges immediately (only valid if on_future is false).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#procedure_name ProcedureGrant#procedure_name}
        '''
        result = self._values.get("procedure_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def return_type(self) -> typing.Optional[builtins.str]:
        '''The return type of the procedure (must be present if procedure_name is present).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#return_type ProcedureGrant#return_type}
        '''
        result = self._values.get("return_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Grants privilege to these roles.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#roles ProcedureGrant#roles}
        '''
        result = self._values.get("roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shares(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Grants privilege to these shares (only valid if on_future is false).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#shares ProcedureGrant#shares}
        '''
        result = self._values.get("shares")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def with_grant_option(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When this is set to true, allows the recipient role to grant the privileges to other roles.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/procedure_grant#with_grant_option ProcedureGrant#with_grant_option}
        '''
        result = self._values.get("with_grant_option")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcedureGrantConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ProcedureGrant",
    "ProcedureGrantArguments",
    "ProcedureGrantArgumentsList",
    "ProcedureGrantArgumentsOutputReference",
    "ProcedureGrantConfig",
]

publication.publish()
