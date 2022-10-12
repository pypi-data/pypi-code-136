'''
# `snowflake_table`

Refer to the Terraform Registory for docs: [`snowflake_table`](https://www.terraform.io/docs/providers/snowflake/r/table).
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


class Table(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.Table",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/table snowflake_table}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        column: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TableColumn", typing.Dict[str, typing.Any]]]],
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        change_tracking: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cluster_by: typing.Optional[typing.Sequence[builtins.str]] = None,
        comment: typing.Optional[builtins.str] = None,
        data_retention_days: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        primary_key: typing.Optional[typing.Union["TablePrimaryKey", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TableTag", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/table snowflake_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#column Table#column}
        :param database: The database in which to create the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#database Table#database}
        :param name: Specifies the identifier for the table; must be unique for the database and schema in which the table is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        :param schema: The schema in which to create the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#schema Table#schema}
        :param change_tracking: Specifies whether to enable change tracking on the table. Default false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#change_tracking Table#change_tracking}
        :param cluster_by: A list of one or more table columns/expressions to be used as clustering key(s) for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#cluster_by Table#cluster_by}
        :param comment: Specifies a comment for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#comment Table#comment}
        :param data_retention_days: Specifies the retention period for the table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed on historical data in the table. Default value is 1, if you wish to inherit the parent schema setting then pass in the schema attribute to this argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#data_retention_days Table#data_retention_days}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#id Table#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param primary_key: primary_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#primary_key Table#primary_key}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#tag Table#tag}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Table.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TableConfig(
            column=column,
            database=database,
            name=name,
            schema=schema,
            change_tracking=change_tracking,
            cluster_by=cluster_by,
            comment=comment,
            data_retention_days=data_retention_days,
            id=id,
            primary_key=primary_key,
            tag=tag,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putColumn")
    def put_column(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TableColumn", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Table.put_column)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putColumn", [value]))

    @jsii.member(jsii_name="putPrimaryKey")
    def put_primary_key(
        self,
        *,
        keys: typing.Sequence[builtins.str],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param keys: Columns to use in primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#keys Table#keys}
        :param name: Name of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        '''
        value = TablePrimaryKey(keys=keys, name=name)

        return typing.cast(None, jsii.invoke(self, "putPrimaryKey", [value]))

    @jsii.member(jsii_name="putTag")
    def put_tag(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TableTag", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Table.put_tag)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTag", [value]))

    @jsii.member(jsii_name="resetChangeTracking")
    def reset_change_tracking(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChangeTracking", []))

    @jsii.member(jsii_name="resetClusterBy")
    def reset_cluster_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterBy", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDataRetentionDays")
    def reset_data_retention_days(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataRetentionDays", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPrimaryKey")
    def reset_primary_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryKey", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="column")
    def column(self) -> "TableColumnList":
        return typing.cast("TableColumnList", jsii.get(self, "column"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> "TablePrimaryKeyOutputReference":
        return typing.cast("TablePrimaryKeyOutputReference", jsii.get(self, "primaryKey"))

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> "TableTagList":
        return typing.cast("TableTagList", jsii.get(self, "tag"))

    @builtins.property
    @jsii.member(jsii_name="changeTrackingInput")
    def change_tracking_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "changeTrackingInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterByInput")
    def cluster_by_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusterByInput"))

    @builtins.property
    @jsii.member(jsii_name="columnInput")
    def column_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TableColumn"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TableColumn"]]], jsii.get(self, "columnInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="dataRetentionDaysInput")
    def data_retention_days_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataRetentionDaysInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryKeyInput")
    def primary_key_input(self) -> typing.Optional["TablePrimaryKey"]:
        return typing.cast(typing.Optional["TablePrimaryKey"], jsii.get(self, "primaryKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TableTag"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TableTag"]]], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="changeTracking")
    def change_tracking(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "changeTracking"))

    @change_tracking.setter
    def change_tracking(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "change_tracking").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeTracking", value)

    @builtins.property
    @jsii.member(jsii_name="clusterBy")
    def cluster_by(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clusterBy"))

    @cluster_by.setter
    def cluster_by(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "cluster_by").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterBy", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="dataRetentionDays")
    def data_retention_days(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataRetentionDays"))

    @data_retention_days.setter
    def data_retention_days(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "data_retention_days").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRetentionDays", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Table, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.table.TableColumn",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "comment": "comment",
        "default": "default",
        "identity": "identity",
        "nullable": "nullable",
    },
)
class TableColumn:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        default: typing.Optional[typing.Union["TableColumnDefault", typing.Dict[str, typing.Any]]] = None,
        identity: typing.Optional[typing.Union["TableColumnIdentity", typing.Dict[str, typing.Any]]] = None,
        nullable: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param name: Column name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        :param type: Column type, e.g. VARIANT. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#type Table#type}
        :param comment: Column comment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#comment Table#comment}
        :param default: default block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#default Table#default}
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#identity Table#identity}
        :param nullable: Whether this column can contain null values. **Note**: Depending on your Snowflake version, the default value will not suffice if this column is used in a primary key constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#nullable Table#nullable}
        '''
        if isinstance(default, dict):
            default = TableColumnDefault(**default)
        if isinstance(identity, dict):
            identity = TableColumnIdentity(**identity)
        if __debug__:
            type_hints = typing.get_type_hints(TableColumn.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument nullable", value=nullable, expected_type=type_hints["nullable"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if comment is not None:
            self._values["comment"] = comment
        if default is not None:
            self._values["default"] = default
        if identity is not None:
            self._values["identity"] = identity
        if nullable is not None:
            self._values["nullable"] = nullable

    @builtins.property
    def name(self) -> builtins.str:
        '''Column name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Column type, e.g. VARIANT.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#type Table#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Column comment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#comment Table#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional["TableColumnDefault"]:
        '''default block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#default Table#default}
        '''
        result = self._values.get("default")
        return typing.cast(typing.Optional["TableColumnDefault"], result)

    @builtins.property
    def identity(self) -> typing.Optional["TableColumnIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#identity Table#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["TableColumnIdentity"], result)

    @builtins.property
    def nullable(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this column can contain null values.

        **Note**: Depending on your Snowflake version, the default value will not suffice if this column is used in a primary key constraint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#nullable Table#nullable}
        '''
        result = self._values.get("nullable")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableColumn(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.table.TableColumnDefault",
    jsii_struct_bases=[],
    name_mapping={
        "constant": "constant",
        "expression": "expression",
        "sequence": "sequence",
    },
)
class TableColumnDefault:
    def __init__(
        self,
        *,
        constant: typing.Optional[builtins.str] = None,
        expression: typing.Optional[builtins.str] = None,
        sequence: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param constant: The default constant value for the column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#constant Table#constant}
        :param expression: The default expression value for the column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#expression Table#expression}
        :param sequence: The default sequence to use for the column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#sequence Table#sequence}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TableColumnDefault.__init__)
            check_type(argname="argument constant", value=constant, expected_type=type_hints["constant"])
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument sequence", value=sequence, expected_type=type_hints["sequence"])
        self._values: typing.Dict[str, typing.Any] = {}
        if constant is not None:
            self._values["constant"] = constant
        if expression is not None:
            self._values["expression"] = expression
        if sequence is not None:
            self._values["sequence"] = sequence

    @builtins.property
    def constant(self) -> typing.Optional[builtins.str]:
        '''The default constant value for the column.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#constant Table#constant}
        '''
        result = self._values.get("constant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expression(self) -> typing.Optional[builtins.str]:
        '''The default expression value for the column.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#expression Table#expression}
        '''
        result = self._values.get("expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sequence(self) -> typing.Optional[builtins.str]:
        '''The default sequence to use for the column.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#sequence Table#sequence}
        '''
        result = self._values.get("sequence")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableColumnDefault(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TableColumnDefaultOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.TableColumnDefaultOutputReference",
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
            type_hints = typing.get_type_hints(TableColumnDefaultOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetConstant")
    def reset_constant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConstant", []))

    @jsii.member(jsii_name="resetExpression")
    def reset_expression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpression", []))

    @jsii.member(jsii_name="resetSequence")
    def reset_sequence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSequence", []))

    @builtins.property
    @jsii.member(jsii_name="constantInput")
    def constant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constantInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="sequenceInput")
    def sequence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sequenceInput"))

    @builtins.property
    @jsii.member(jsii_name="constant")
    def constant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "constant"))

    @constant.setter
    def constant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnDefaultOutputReference, "constant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constant", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnDefaultOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="sequence")
    def sequence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sequence"))

    @sequence.setter
    def sequence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnDefaultOutputReference, "sequence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sequence", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TableColumnDefault]:
        return typing.cast(typing.Optional[TableColumnDefault], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TableColumnDefault]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnDefaultOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.table.TableColumnIdentity",
    jsii_struct_bases=[],
    name_mapping={"start_num": "startNum", "step_num": "stepNum"},
)
class TableColumnIdentity:
    def __init__(
        self,
        *,
        start_num: typing.Optional[jsii.Number] = None,
        step_num: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param start_num: The number to start incrementing at. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#start_num Table#start_num}
        :param step_num: Step size to increment by. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#step_num Table#step_num}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TableColumnIdentity.__init__)
            check_type(argname="argument start_num", value=start_num, expected_type=type_hints["start_num"])
            check_type(argname="argument step_num", value=step_num, expected_type=type_hints["step_num"])
        self._values: typing.Dict[str, typing.Any] = {}
        if start_num is not None:
            self._values["start_num"] = start_num
        if step_num is not None:
            self._values["step_num"] = step_num

    @builtins.property
    def start_num(self) -> typing.Optional[jsii.Number]:
        '''The number to start incrementing at.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#start_num Table#start_num}
        '''
        result = self._values.get("start_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def step_num(self) -> typing.Optional[jsii.Number]:
        '''Step size to increment by.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#step_num Table#step_num}
        '''
        result = self._values.get("step_num")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableColumnIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TableColumnIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.TableColumnIdentityOutputReference",
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
            type_hints = typing.get_type_hints(TableColumnIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStartNum")
    def reset_start_num(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartNum", []))

    @jsii.member(jsii_name="resetStepNum")
    def reset_step_num(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStepNum", []))

    @builtins.property
    @jsii.member(jsii_name="startNumInput")
    def start_num_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startNumInput"))

    @builtins.property
    @jsii.member(jsii_name="stepNumInput")
    def step_num_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stepNumInput"))

    @builtins.property
    @jsii.member(jsii_name="startNum")
    def start_num(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startNum"))

    @start_num.setter
    def start_num(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnIdentityOutputReference, "start_num").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startNum", value)

    @builtins.property
    @jsii.member(jsii_name="stepNum")
    def step_num(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stepNum"))

    @step_num.setter
    def step_num(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnIdentityOutputReference, "step_num").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stepNum", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TableColumnIdentity]:
        return typing.cast(typing.Optional[TableColumnIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TableColumnIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TableColumnList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.TableColumnList",
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
            type_hints = typing.get_type_hints(TableColumnList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "TableColumnOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TableColumnList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TableColumnOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(TableColumnList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(TableColumnList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TableColumn]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TableColumn]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TableColumn]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TableColumnOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.TableColumnOutputReference",
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
            type_hints = typing.get_type_hints(TableColumnOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDefault")
    def put_default(
        self,
        *,
        constant: typing.Optional[builtins.str] = None,
        expression: typing.Optional[builtins.str] = None,
        sequence: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param constant: The default constant value for the column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#constant Table#constant}
        :param expression: The default expression value for the column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#expression Table#expression}
        :param sequence: The default sequence to use for the column. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#sequence Table#sequence}
        '''
        value = TableColumnDefault(
            constant=constant, expression=expression, sequence=sequence
        )

        return typing.cast(None, jsii.invoke(self, "putDefault", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        start_num: typing.Optional[jsii.Number] = None,
        step_num: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param start_num: The number to start incrementing at. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#start_num Table#start_num}
        :param step_num: Step size to increment by. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#step_num Table#step_num}
        '''
        value = TableColumnIdentity(start_num=start_num, step_num=step_num)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetNullable")
    def reset_nullable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullable", []))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> TableColumnDefaultOutputReference:
        return typing.cast(TableColumnDefaultOutputReference, jsii.get(self, "default"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> TableColumnIdentityOutputReference:
        return typing.cast(TableColumnIdentityOutputReference, jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[TableColumnDefault]:
        return typing.cast(typing.Optional[TableColumnDefault], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional[TableColumnIdentity]:
        return typing.cast(typing.Optional[TableColumnIdentity], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nullableInput")
    def nullable_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "nullableInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnOutputReference, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nullable")
    def nullable(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "nullable"))

    @nullable.setter
    def nullable(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnOutputReference, "nullable").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullable", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TableColumn, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TableColumn, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TableColumn, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableColumnOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.table.TableConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "column": "column",
        "database": "database",
        "name": "name",
        "schema": "schema",
        "change_tracking": "changeTracking",
        "cluster_by": "clusterBy",
        "comment": "comment",
        "data_retention_days": "dataRetentionDays",
        "id": "id",
        "primary_key": "primaryKey",
        "tag": "tag",
    },
)
class TableConfig(cdktf.TerraformMetaArguments):
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
        column: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[TableColumn, typing.Dict[str, typing.Any]]]],
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        change_tracking: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        cluster_by: typing.Optional[typing.Sequence[builtins.str]] = None,
        comment: typing.Optional[builtins.str] = None,
        data_retention_days: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        primary_key: typing.Optional[typing.Union["TablePrimaryKey", typing.Dict[str, typing.Any]]] = None,
        tag: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["TableTag", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param column: column block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#column Table#column}
        :param database: The database in which to create the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#database Table#database}
        :param name: Specifies the identifier for the table; must be unique for the database and schema in which the table is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        :param schema: The schema in which to create the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#schema Table#schema}
        :param change_tracking: Specifies whether to enable change tracking on the table. Default false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#change_tracking Table#change_tracking}
        :param cluster_by: A list of one or more table columns/expressions to be used as clustering key(s) for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#cluster_by Table#cluster_by}
        :param comment: Specifies a comment for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#comment Table#comment}
        :param data_retention_days: Specifies the retention period for the table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed on historical data in the table. Default value is 1, if you wish to inherit the parent schema setting then pass in the schema attribute to this argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#data_retention_days Table#data_retention_days}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#id Table#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param primary_key: primary_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#primary_key Table#primary_key}
        :param tag: tag block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#tag Table#tag}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(primary_key, dict):
            primary_key = TablePrimaryKey(**primary_key)
        if __debug__:
            type_hints = typing.get_type_hints(TableConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument column", value=column, expected_type=type_hints["column"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument change_tracking", value=change_tracking, expected_type=type_hints["change_tracking"])
            check_type(argname="argument cluster_by", value=cluster_by, expected_type=type_hints["cluster_by"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument data_retention_days", value=data_retention_days, expected_type=type_hints["data_retention_days"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "column": column,
            "database": database,
            "name": name,
            "schema": schema,
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
        if change_tracking is not None:
            self._values["change_tracking"] = change_tracking
        if cluster_by is not None:
            self._values["cluster_by"] = cluster_by
        if comment is not None:
            self._values["comment"] = comment
        if data_retention_days is not None:
            self._values["data_retention_days"] = data_retention_days
        if id is not None:
            self._values["id"] = id
        if primary_key is not None:
            self._values["primary_key"] = primary_key
        if tag is not None:
            self._values["tag"] = tag

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
    def column(self) -> typing.Union[cdktf.IResolvable, typing.List[TableColumn]]:
        '''column block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#column Table#column}
        '''
        result = self._values.get("column")
        assert result is not None, "Required property 'column' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List[TableColumn]], result)

    @builtins.property
    def database(self) -> builtins.str:
        '''The database in which to create the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#database Table#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the identifier for the table;

        must be unique for the database and schema in which the table is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema in which to create the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#schema Table#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def change_tracking(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to enable change tracking on the table. Default false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#change_tracking Table#change_tracking}
        '''
        result = self._values.get("change_tracking")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def cluster_by(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of one or more table columns/expressions to be used as clustering key(s) for the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#cluster_by Table#cluster_by}
        '''
        result = self._values.get("cluster_by")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Specifies a comment for the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#comment Table#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_retention_days(self) -> typing.Optional[jsii.Number]:
        '''Specifies the retention period for the table so that Time Travel actions (SELECT, CLONE, UNDROP) can be performed on historical data in the table.

        Default value is 1, if you wish to inherit the parent schema setting then pass in the schema attribute to this argument.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#data_retention_days Table#data_retention_days}
        '''
        result = self._values.get("data_retention_days")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#id Table#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_key(self) -> typing.Optional["TablePrimaryKey"]:
        '''primary_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#primary_key Table#primary_key}
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional["TablePrimaryKey"], result)

    @builtins.property
    def tag(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TableTag"]]]:
        '''tag block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#tag Table#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["TableTag"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.table.TablePrimaryKey",
    jsii_struct_bases=[],
    name_mapping={"keys": "keys", "name": "name"},
)
class TablePrimaryKey:
    def __init__(
        self,
        *,
        keys: typing.Sequence[builtins.str],
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param keys: Columns to use in primary key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#keys Table#keys}
        :param name: Name of constraint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TablePrimaryKey.__init__)
            check_type(argname="argument keys", value=keys, expected_type=type_hints["keys"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "keys": keys,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def keys(self) -> typing.List[builtins.str]:
        '''Columns to use in primary key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#keys Table#keys}
        '''
        result = self._values.get("keys")
        assert result is not None, "Required property 'keys' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of constraint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TablePrimaryKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TablePrimaryKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.TablePrimaryKeyOutputReference",
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
            type_hints = typing.get_type_hints(TablePrimaryKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="keysInput")
    def keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "keysInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="keys")
    def keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "keys"))

    @keys.setter
    def keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TablePrimaryKeyOutputReference, "keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keys", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TablePrimaryKeyOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[TablePrimaryKey]:
        return typing.cast(typing.Optional[TablePrimaryKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[TablePrimaryKey]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TablePrimaryKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.table.TableTag",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "value": "value",
        "database": "database",
        "schema": "schema",
    },
)
class TableTag:
    def __init__(
        self,
        *,
        name: builtins.str,
        value: builtins.str,
        database: typing.Optional[builtins.str] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Tag name, e.g. department. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        :param value: Tag value, e.g. marketing_info. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#value Table#value}
        :param database: Name of the database that the tag was created in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#database Table#database}
        :param schema: Name of the schema that the tag was created in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#schema Table#schema}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TableTag.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }
        if database is not None:
            self._values["database"] = database
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def name(self) -> builtins.str:
        '''Tag name, e.g. department.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#name Table#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Tag value, e.g. marketing_info.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#value Table#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''Name of the database that the tag was created in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#database Table#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''Name of the schema that the tag was created in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/table#schema Table#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableTag(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TableTagList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.TableTagList",
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
            type_hints = typing.get_type_hints(TableTagList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "TableTagOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TableTagList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("TableTagOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableTagList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(TableTagList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(TableTagList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TableTag]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TableTag]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[TableTag]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableTagList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class TableTagOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.table.TableTagOutputReference",
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
            type_hints = typing.get_type_hints(TableTagOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableTagOutputReference, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableTagOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableTagOutputReference, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableTagOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TableTag, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TableTag, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TableTag, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TableTagOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Table",
    "TableColumn",
    "TableColumnDefault",
    "TableColumnDefaultOutputReference",
    "TableColumnIdentity",
    "TableColumnIdentityOutputReference",
    "TableColumnList",
    "TableColumnOutputReference",
    "TableConfig",
    "TablePrimaryKey",
    "TablePrimaryKeyOutputReference",
    "TableTag",
    "TableTagList",
    "TableTagOutputReference",
]

publication.publish()
