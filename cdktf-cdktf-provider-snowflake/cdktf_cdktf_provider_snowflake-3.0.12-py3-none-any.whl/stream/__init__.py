'''
# `snowflake_stream`

Refer to the Terraform Registory for docs: [`snowflake_stream`](https://www.terraform.io/docs/providers/snowflake/r/stream).
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


class Stream(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.stream.Stream",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/stream snowflake_stream}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        append_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insert_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        on_table: typing.Optional[builtins.str] = None,
        on_view: typing.Optional[builtins.str] = None,
        show_initial_rows: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/stream snowflake_stream} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database: The database in which to create the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#database Stream#database}
        :param name: Specifies the identifier for the stream; must be unique for the database and schema in which the stream is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#name Stream#name}
        :param schema: The schema in which to create the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#schema Stream#schema}
        :param append_only: Type of the stream that will be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#append_only Stream#append_only}
        :param comment: Specifies a comment for the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#comment Stream#comment}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#id Stream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insert_only: Create an insert only stream type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#insert_only Stream#insert_only}
        :param on_table: Name of the table the stream will monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#on_table Stream#on_table}
        :param on_view: Name of the view the stream will monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#on_view Stream#on_view}
        :param show_initial_rows: Specifies whether to return all existing rows in the source table as row inserts the first time the stream is consumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#show_initial_rows Stream#show_initial_rows}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Stream.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StreamConfig(
            database=database,
            name=name,
            schema=schema,
            append_only=append_only,
            comment=comment,
            id=id,
            insert_only=insert_only,
            on_table=on_table,
            on_view=on_view,
            show_initial_rows=show_initial_rows,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAppendOnly")
    def reset_append_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppendOnly", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInsertOnly")
    def reset_insert_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsertOnly", []))

    @jsii.member(jsii_name="resetOnTable")
    def reset_on_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnTable", []))

    @jsii.member(jsii_name="resetOnView")
    def reset_on_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnView", []))

    @jsii.member(jsii_name="resetShowInitialRows")
    def reset_show_initial_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShowInitialRows", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="appendOnlyInput")
    def append_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "appendOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="insertOnlyInput")
    def insert_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "insertOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="onTableInput")
    def on_table_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onTableInput"))

    @builtins.property
    @jsii.member(jsii_name="onViewInput")
    def on_view_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "onViewInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="showInitialRowsInput")
    def show_initial_rows_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "showInitialRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="appendOnly")
    def append_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "appendOnly"))

    @append_only.setter
    def append_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "append_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appendOnly", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="insertOnly")
    def insert_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "insertOnly"))

    @insert_only.setter
    def insert_only(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "insert_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insertOnly", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="onTable")
    def on_table(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onTable"))

    @on_table.setter
    def on_table(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "on_table").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onTable", value)

    @builtins.property
    @jsii.member(jsii_name="onView")
    def on_view(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "onView"))

    @on_view.setter
    def on_view(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "on_view").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onView", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="showInitialRows")
    def show_initial_rows(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "showInitialRows"))

    @show_initial_rows.setter
    def show_initial_rows(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Stream, "show_initial_rows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "showInitialRows", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.stream.StreamConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "database": "database",
        "name": "name",
        "schema": "schema",
        "append_only": "appendOnly",
        "comment": "comment",
        "id": "id",
        "insert_only": "insertOnly",
        "on_table": "onTable",
        "on_view": "onView",
        "show_initial_rows": "showInitialRows",
    },
)
class StreamConfig(cdktf.TerraformMetaArguments):
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
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        append_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        insert_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        on_table: typing.Optional[builtins.str] = None,
        on_view: typing.Optional[builtins.str] = None,
        show_initial_rows: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param database: The database in which to create the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#database Stream#database}
        :param name: Specifies the identifier for the stream; must be unique for the database and schema in which the stream is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#name Stream#name}
        :param schema: The schema in which to create the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#schema Stream#schema}
        :param append_only: Type of the stream that will be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#append_only Stream#append_only}
        :param comment: Specifies a comment for the stream. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#comment Stream#comment}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#id Stream#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param insert_only: Create an insert only stream type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#insert_only Stream#insert_only}
        :param on_table: Name of the table the stream will monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#on_table Stream#on_table}
        :param on_view: Name of the view the stream will monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#on_view Stream#on_view}
        :param show_initial_rows: Specifies whether to return all existing rows in the source table as row inserts the first time the stream is consumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#show_initial_rows Stream#show_initial_rows}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(StreamConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument append_only", value=append_only, expected_type=type_hints["append_only"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument insert_only", value=insert_only, expected_type=type_hints["insert_only"])
            check_type(argname="argument on_table", value=on_table, expected_type=type_hints["on_table"])
            check_type(argname="argument on_view", value=on_view, expected_type=type_hints["on_view"])
            check_type(argname="argument show_initial_rows", value=show_initial_rows, expected_type=type_hints["show_initial_rows"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if append_only is not None:
            self._values["append_only"] = append_only
        if comment is not None:
            self._values["comment"] = comment
        if id is not None:
            self._values["id"] = id
        if insert_only is not None:
            self._values["insert_only"] = insert_only
        if on_table is not None:
            self._values["on_table"] = on_table
        if on_view is not None:
            self._values["on_view"] = on_view
        if show_initial_rows is not None:
            self._values["show_initial_rows"] = show_initial_rows

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
    def database(self) -> builtins.str:
        '''The database in which to create the stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#database Stream#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the identifier for the stream;

        must be unique for the database and schema in which the stream is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#name Stream#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema in which to create the stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#schema Stream#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def append_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Type of the stream that will be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#append_only Stream#append_only}
        '''
        result = self._values.get("append_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Specifies a comment for the stream.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#comment Stream#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#id Stream#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insert_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Create an insert only stream type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#insert_only Stream#insert_only}
        '''
        result = self._values.get("insert_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def on_table(self) -> typing.Optional[builtins.str]:
        '''Name of the table the stream will monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#on_table Stream#on_table}
        '''
        result = self._values.get("on_table")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_view(self) -> typing.Optional[builtins.str]:
        '''Name of the view the stream will monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#on_view Stream#on_view}
        '''
        result = self._values.get("on_view")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def show_initial_rows(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to return all existing rows in the source table as row inserts the first time the stream is consumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/stream#show_initial_rows Stream#show_initial_rows}
        '''
        result = self._values.get("show_initial_rows")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Stream",
    "StreamConfig",
]

publication.publish()
