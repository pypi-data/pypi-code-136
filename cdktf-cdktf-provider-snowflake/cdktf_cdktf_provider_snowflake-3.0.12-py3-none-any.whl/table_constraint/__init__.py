'''
# `snowflake_table_constraint`

Refer to the Terraform Registory for docs: [`snowflake_table_constraint`](https://www.terraform.io/docs/providers/snowflake/r/table_constraint).
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


class TableConstraint(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.tableConstraint.TableConstraint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint snowflake_table_constraint}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        columns: typing.Sequence[builtins.str],
        name: builtins.str,
        table_id: builtins.str,
        type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        deferrable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforced: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        foreign_key_properties: typing.Optional[typing.Union["TableConstraintForeignKeyProperties", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initially: typing.Optional[builtins.str] = None,
        rely: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint snowflake_table_constraint} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param columns: Columns to use in constraint key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#columns TableConstraint#columns}
        :param name: Name of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#name TableConstraint#name}
        :param table_id: Idenfifier for table to create constraint on. Must be of the form Note: format must follow: "<db_name>"."<schema_name>"."<table_name>" or "<db_name>.<schema_name>.<table_name>" or "<db_name>|<schema_name>.<table_name>" (snowflake_table.my_table.id) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#table_id TableConstraint#table_id}
        :param type: Type of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#type TableConstraint#type}
        :param comment: Comment for the table constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#comment TableConstraint#comment}
        :param deferrable: Whether the constraint is deferrable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#deferrable TableConstraint#deferrable}
        :param enable: Specifies whether the constraint is enabled or disabled. These properties are provided for compatibility with Oracle. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#enable TableConstraint#enable}
        :param enforced: Whether the constraint is enforced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#enforced TableConstraint#enforced}
        :param foreign_key_properties: foreign_key_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#foreign_key_properties TableConstraint#foreign_key_properties}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#id TableConstraint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initially: Whether the constraint is initially deferred or immediate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#initially TableConstraint#initially}
        :param rely: Specifies whether a constraint in NOVALIDATE mode is taken into account during query rewrite. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#rely TableConstraint#rely}
        :param validate: Specifies whether to validate existing data on the table when a constraint is created. Only used in conjunction with the ENABLE property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#validate TableConstraint#validate}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TableConstraint.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TableConstraintConfig(
            columns=columns,
            name=name,
            table_id=table_id,
            type=type,
            comment=comment,
            deferrable=deferrable,
            enable=enable,
            enforced=enforced,
            foreign_key_properties=foreign_key_properties,
            id=id,
            initially=initially,
            rely=rely,
            validate=validate,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putForeignKeyProperties")
    def put_foreign_key_properties(
        self,
        *,
        match: typing.Optional[builtins.str] = None,
        on_delete: typing.Optional[builtins.str] = None,
        on_update: typing.Optional[builtins.str] = None,
        references: typing.Optional[typing.Union["TableConstraintForeignKeyPropertiesReferences", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param match: The match type for the foreign key. Not applicable for primary/unique keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#match TableConstraint#match}
        :param on_delete: Specifies the action performed when the primary/unique key for the foreign key is deleted. Not applicable for primary/unique keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#on_delete TableConstraint#on_delete}
        :param on_update: Specifies the action performed when the primary/unique key for the foreign key is updated. Not applicable for primary/unique keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#on_update TableConstraint#on_update}
        :param references: references block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#references TableConstraint#references}
        '''
        value = TableConstraintForeignKeyProperties(
            match=match,
            on_delete=on_delete,
            on_update=on_update,
            references=references,
        )

        return typing.cast(None, jsii.invoke(self, "putForeignKeyProperties", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDeferrable")
    def reset_deferrable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeferrable", []))

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetEnforced")
    def reset_enforced(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforced", []))

    @jsii.member(jsii_name="resetForeignKeyProperties")
    def reset_foreign_key_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForeignKeyProperties", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitially")
    def reset_initially(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitially", []))

    @jsii.member(jsii_name="resetRely")
    def reset_rely(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRely", []))

    @jsii.member(jsii_name="resetValidate")
    def reset_validate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidate", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="foreignKeyProperties")
    def foreign_key_properties(
        self,
    ) -> "TableConstraintForeignKeyPropertiesOutputReference":
        return typing.cast("TableConstraintForeignKeyPropertiesOutputReference", jsii.get(self, "foreignKeyProperties"))

    @builtins.property
    @jsii.member(jsii_name="columnsInput")
    def columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnsInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="deferrableInput")
    def deferrable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deferrableInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="enforcedInput")
    def enforced_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforcedInput"))

    @builtins.property
    @jsii.member(jsii_name="foreignKeyPropertiesInput")
    def foreign_key_properties_input(
        self,
    ) -> typing.Optional["TableConstraintForeignKeyProperties"]:
        return typing.cast(typing.Optional["TableConstraintForeignKeyProperties"], jsii.get(self, "foreignKeyPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initiallyInput")
    def initially_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initiallyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="relyInput")
    def rely_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "relyInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="validateInput")
    def validate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "validateInput"))

    @builtins.property
    @jsii.member(jsii_name="columns")
    def columns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "columns"))

    @columns.setter
    def columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "columns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columns", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="deferrable")
    def deferrable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deferrable"))

    @deferrable.setter
    def deferrable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "deferrable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deferrable", value)

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "enable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="enforced")
    def enforced(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforced"))

    @enforced.setter
    def enforced(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "enforced").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforced", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initially")
    def initially(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initially"))

    @initially.setter
    def initially(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "initially").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initially", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rely")
    def rely(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rely"))

    @rely.setter
    def rely(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "rely").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rely", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="validate")
    def validate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "validate"))

    @validate.setter
    def validate(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraint, "validate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validate", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.tableConstraint.TableConstraintConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "columns": "columns",
        "name": "name",
        "table_id": "tableId",
        "type": "type",
        "comment": "comment",
        "deferrable": "deferrable",
        "enable": "enable",
        "enforced": "enforced",
        "foreign_key_properties": "foreignKeyProperties",
        "id": "id",
        "initially": "initially",
        "rely": "rely",
        "validate": "validate",
    },
)
class TableConstraintConfig(cdktf.TerraformMetaArguments):
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
        columns: typing.Sequence[builtins.str],
        name: builtins.str,
        table_id: builtins.str,
        type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        deferrable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforced: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        foreign_key_properties: typing.Optional[typing.Union["TableConstraintForeignKeyProperties", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        initially: typing.Optional[builtins.str] = None,
        rely: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        validate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param columns: Columns to use in constraint key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#columns TableConstraint#columns}
        :param name: Name of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#name TableConstraint#name}
        :param table_id: Idenfifier for table to create constraint on. Must be of the form Note: format must follow: "<db_name>"."<schema_name>"."<table_name>" or "<db_name>.<schema_name>.<table_name>" or "<db_name>|<schema_name>.<table_name>" (snowflake_table.my_table.id) Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#table_id TableConstraint#table_id}
        :param type: Type of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#type TableConstraint#type}
        :param comment: Comment for the table constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#comment TableConstraint#comment}
        :param deferrable: Whether the constraint is deferrable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#deferrable TableConstraint#deferrable}
        :param enable: Specifies whether the constraint is enabled or disabled. These properties are provided for compatibility with Oracle. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#enable TableConstraint#enable}
        :param enforced: Whether the constraint is enforced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#enforced TableConstraint#enforced}
        :param foreign_key_properties: foreign_key_properties block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#foreign_key_properties TableConstraint#foreign_key_properties}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#id TableConstraint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initially: Whether the constraint is initially deferred or immediate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#initially TableConstraint#initially}
        :param rely: Specifies whether a constraint in NOVALIDATE mode is taken into account during query rewrite. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#rely TableConstraint#rely}
        :param validate: Specifies whether to validate existing data on the table when a constraint is created. Only used in conjunction with the ENABLE property. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#validate TableConstraint#validate}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(foreign_key_properties, dict):
            foreign_key_properties = TableConstraintForeignKeyProperties(**foreign_key_properties)
        if __debug__:
            type_hints = typing.get_type_hints(TableConstraintConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument deferrable", value=deferrable, expected_type=type_hints["deferrable"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument enforced", value=enforced, expected_type=type_hints["enforced"])
            check_type(argname="argument foreign_key_properties", value=foreign_key_properties, expected_type=type_hints["foreign_key_properties"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initially", value=initially, expected_type=type_hints["initially"])
            check_type(argname="argument rely", value=rely, expected_type=type_hints["rely"])
            check_type(argname="argument validate", value=validate, expected_type=type_hints["validate"])
        self._values: typing.Dict[str, typing.Any] = {
            "columns": columns,
            "name": name,
            "table_id": table_id,
            "type": type,
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
        if comment is not None:
            self._values["comment"] = comment
        if deferrable is not None:
            self._values["deferrable"] = deferrable
        if enable is not None:
            self._values["enable"] = enable
        if enforced is not None:
            self._values["enforced"] = enforced
        if foreign_key_properties is not None:
            self._values["foreign_key_properties"] = foreign_key_properties
        if id is not None:
            self._values["id"] = id
        if initially is not None:
            self._values["initially"] = initially
        if rely is not None:
            self._values["rely"] = rely
        if validate is not None:
            self._values["validate"] = validate

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
    def columns(self) -> typing.List[builtins.str]:
        '''Columns to use in constraint key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#columns TableConstraint#columns}
        '''
        result = self._values.get("columns")
        assert result is not None, "Required property 'columns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of constraint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#name TableConstraint#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''Idenfifier for table to create constraint on.

        Must be of the form Note: format must follow: "<db_name>"."<schema_name>"."<table_name>" or "<db_name>.<schema_name>.<table_name>" or "<db_name>|<schema_name>.<table_name>" (snowflake_table.my_table.id)

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#table_id TableConstraint#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of constraint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#type TableConstraint#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Comment for the table constraint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#comment TableConstraint#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deferrable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the constraint is deferrable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#deferrable TableConstraint#deferrable}
        '''
        result = self._values.get("deferrable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether the constraint is enabled or disabled. These properties are provided for compatibility with Oracle.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#enable TableConstraint#enable}
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enforced(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the constraint is enforced.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#enforced TableConstraint#enforced}
        '''
        result = self._values.get("enforced")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def foreign_key_properties(
        self,
    ) -> typing.Optional["TableConstraintForeignKeyProperties"]:
        '''foreign_key_properties block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#foreign_key_properties TableConstraint#foreign_key_properties}
        '''
        result = self._values.get("foreign_key_properties")
        return typing.cast(typing.Optional["TableConstraintForeignKeyProperties"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#id TableConstraint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initially(self) -> typing.Optional[builtins.str]:
        '''Whether the constraint is initially deferred or immediate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#initially TableConstraint#initially}
        '''
        result = self._values.get("initially")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rely(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether a constraint in NOVALIDATE mode is taken into account during query rewrite.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#rely TableConstraint#rely}
        '''
        result = self._values.get("rely")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def validate(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to validate existing data on the table when a constraint is created.

        Only used in conjunction with the ENABLE property.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#validate TableConstraint#validate}
        '''
        result = self._values.get("validate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableConstraintConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.tableConstraint.TableConstraintForeignKeyProperties",
    jsii_struct_bases=[],
    name_mapping={
        "match": "match",
        "on_delete": "onDelete",
        "on_update": "onUpdate",
        "references": "references",
    },
)
class TableConstraintForeignKeyProperties:
    def __init__(
        self,
        *,
        match: typing.Optional[builtins.str] = None,
        on_delete: typing.Optional[builtins.str] = None,
        on_update: typing.Optional[builtins.str] = None,
        references: typing.Optional[typing.Union["TableConstraintForeignKeyPropertiesReferences", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param match: The match type for the foreign key. Not applicable for primary/unique keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#match TableConstraint#match}
        :param on_delete: Specifies the action performed when the primary/unique key for the foreign key is deleted. Not applicable for primary/unique keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#on_delete TableConstraint#on_delete}
        :param on_update: Specifies the action performed when the primary/unique key for the foreign key is updated. Not applicable for primary/unique keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#on_update TableConstraint#on_update}
        :param references: references block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#references TableConstraint#references}
        '''
        if isinstance(references, dict):
            references = TableConstraintForeignKeyPropertiesReferences(**references)
        if __debug__:
            type_hints = typing.get_type_hints(TableConstraintForeignKeyProperties.__init__)
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument on_delete", value=on_delete, expected_type=type_hints["on_delete"])
            check_type(argname="argument on_update", value=on_update, expected_type=type_hints["on_update"])
            check_type(argname="argument references", value=references, expected_type=type_hints["references"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match is not None:
            self._values["match"] = match
        if on_delete is not None:
            self._values["on_delete"] = on_delete
        if on_update is not None:
            self._values["on_update"] = on_update
        if references is not None:
            self._values["references"] = references

    @builtins.property
    def match(self) -> typing.Optional[builtins.str]:
        '''The match type for the foreign key. Not applicable for primary/unique keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#match TableConstraint#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_delete(self) -> typing.Optional[builtins.str]:
        '''Specifies the action performed when the primary/unique key for the foreign key is deleted. Not applicable for primary/unique keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#on_delete TableConstraint#on_delete}
        '''
        result = self._values.get("on_delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_update(self) -> typing.Optional[builtins.str]:
        '''Specifies the action performed when the primary/unique key for the foreign key is updated. Not applicable for primary/unique keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#on_update TableConstraint#on_update}
        '''
        result = self._values.get("on_update")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def references(
        self,
    ) -> typing.Optional["TableConstraintForeignKeyPropertiesReferences"]:
        '''references block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#references TableConstraint#references}
        '''
        result = self._values.get("references")
        return typing.cast(typing.Optional["TableConstraintForeignKeyPropertiesReferences"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableConstraintForeignKeyProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TableConstraintForeignKeyPropertiesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.tableConstraint.TableConstraintForeignKeyPropertiesOutputReference",
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
            type_hints = typing.get_type_hints(TableConstraintForeignKeyPropertiesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putReferences")
    def put_references(
        self,
        *,
        columns: typing.Sequence[builtins.str],
        table_id: builtins.str,
    ) -> None:
        '''
        :param columns: Columns to use in foreign key reference. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#columns TableConstraint#columns}
        :param table_id: Name of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#table_id TableConstraint#table_id}
        '''
        value = TableConstraintForeignKeyPropertiesReferences(
            columns=columns, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putReferences", [value]))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @jsii.member(jsii_name="resetOnDelete")
    def reset_on_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDelete", []))

    @jsii.member(jsii_name="resetOnUpdate")
    def reset_on_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnUpdate", []))

    @jsii.member(jsii_name="resetReferences")
    def reset_references(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReferences", []))

    @builtins.property
    @jsii.member(jsii_name="references")
    def references(
        self,
    ) -> "TableConstraintForeignKeyPropertiesReferencesOutputReference":
        return typing.cast("TableConstraintForeignKeyPropertiesReferencesOutputReference", jsii.get(self, "references"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="onDeleteInput")
    def on_delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="onUpdateInput")
    def on_update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onUpdateInput"))

    @builtins.property
    @jsii.member(jsii_name="referencesInput")
    def references_input(
        self,
    ) -> typing.Optional["TableConstraintForeignKeyPropertiesReferences"]:
        return typing.cast(typing.Optional["TableConstraintForeignKeyPropertiesReferences"], jsii.get(self, "referencesInput"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "match"))

    @match.setter
    def match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraintForeignKeyPropertiesOutputReference, "match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "match", value)

    @builtins.property
    @jsii.member(jsii_name="onDelete")
    def on_delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onDelete"))

    @on_delete.setter
    def on_delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraintForeignKeyPropertiesOutputReference, "on_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDelete", value)

    @builtins.property
    @jsii.member(jsii_name="onUpdate")
    def on_update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onUpdate"))

    @on_update.setter
    def on_update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraintForeignKeyPropertiesOutputReference, "on_update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TableConstraintForeignKeyProperties]:
        return typing.cast(typing.Optional[TableConstraintForeignKeyProperties], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TableConstraintForeignKeyProperties],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraintForeignKeyPropertiesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.tableConstraint.TableConstraintForeignKeyPropertiesReferences",
    jsii_struct_bases=[],
    name_mapping={"columns": "columns", "table_id": "tableId"},
)
class TableConstraintForeignKeyPropertiesReferences:
    def __init__(
        self,
        *,
        columns: typing.Sequence[builtins.str],
        table_id: builtins.str,
    ) -> None:
        '''
        :param columns: Columns to use in foreign key reference. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#columns TableConstraint#columns}
        :param table_id: Name of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#table_id TableConstraint#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TableConstraintForeignKeyPropertiesReferences.__init__)
            check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "columns": columns,
            "table_id": table_id,
        }

    @builtins.property
    def columns(self) -> typing.List[builtins.str]:
        '''Columns to use in foreign key reference.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#columns TableConstraint#columns}
        '''
        result = self._values.get("columns")
        assert result is not None, "Required property 'columns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''Name of constraint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table_constraint#table_id TableConstraint#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableConstraintForeignKeyPropertiesReferences(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TableConstraintForeignKeyPropertiesReferencesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.tableConstraint.TableConstraintForeignKeyPropertiesReferencesOutputReference",
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
            type_hints = typing.get_type_hints(TableConstraintForeignKeyPropertiesReferencesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="columnsInput")
    def columns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "columnsInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="columns")
    def columns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "columns"))

    @columns.setter
    def columns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraintForeignKeyPropertiesReferencesOutputReference, "columns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "columns", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraintForeignKeyPropertiesReferencesOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[TableConstraintForeignKeyPropertiesReferences]:
        return typing.cast(typing.Optional[TableConstraintForeignKeyPropertiesReferences], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[TableConstraintForeignKeyPropertiesReferences],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableConstraintForeignKeyPropertiesReferencesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TableConstraint",
    "TableConstraintConfig",
    "TableConstraintForeignKeyProperties",
    "TableConstraintForeignKeyPropertiesOutputReference",
    "TableConstraintForeignKeyPropertiesReferences",
    "TableConstraintForeignKeyPropertiesReferencesOutputReference",
]

publication.publish()
