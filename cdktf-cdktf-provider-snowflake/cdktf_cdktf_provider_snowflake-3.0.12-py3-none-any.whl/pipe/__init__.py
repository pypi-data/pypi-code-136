'''
# `snowflake_pipe`

Refer to the Terraform Registory for docs: [`snowflake_pipe`](https://www.terraform.io/docs/providers/snowflake/r/pipe).
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


class Pipe(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.pipe.Pipe",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/pipe snowflake_pipe}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        copy_statement: builtins.str,
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        auto_ingest: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_sns_topic_arn: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        error_integration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/pipe snowflake_pipe} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param copy_statement: Specifies the copy statement for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#copy_statement Pipe#copy_statement}
        :param database: The database in which to create the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#database Pipe#database}
        :param name: Specifies the identifier for the pipe; must be unique for the database and schema in which the pipe is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#name Pipe#name}
        :param schema: The schema in which to create the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#schema Pipe#schema}
        :param auto_ingest: Specifies a auto_ingest param for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#auto_ingest Pipe#auto_ingest}
        :param aws_sns_topic_arn: Specifies the Amazon Resource Name (ARN) for the SNS topic for your S3 bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#aws_sns_topic_arn Pipe#aws_sns_topic_arn}
        :param comment: Specifies a comment for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#comment Pipe#comment}
        :param error_integration: Specifies the name of the notification integration used for error notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#error_integration Pipe#error_integration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#id Pipe#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration: Specifies an integration for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#integration Pipe#integration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Pipe.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PipeConfig(
            copy_statement=copy_statement,
            database=database,
            name=name,
            schema=schema,
            auto_ingest=auto_ingest,
            aws_sns_topic_arn=aws_sns_topic_arn,
            comment=comment,
            error_integration=error_integration,
            id=id,
            integration=integration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAutoIngest")
    def reset_auto_ingest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoIngest", []))

    @jsii.member(jsii_name="resetAwsSnsTopicArn")
    def reset_aws_sns_topic_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsSnsTopicArn", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetErrorIntegration")
    def reset_error_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorIntegration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIntegration")
    def reset_integration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="notificationChannel")
    def notification_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notificationChannel"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="autoIngestInput")
    def auto_ingest_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoIngestInput"))

    @builtins.property
    @jsii.member(jsii_name="awsSnsTopicArnInput")
    def aws_sns_topic_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsSnsTopicArnInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="copyStatementInput")
    def copy_statement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "copyStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="errorIntegrationInput")
    def error_integration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationInput")
    def integration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="autoIngest")
    def auto_ingest(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoIngest"))

    @auto_ingest.setter
    def auto_ingest(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "auto_ingest").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoIngest", value)

    @builtins.property
    @jsii.member(jsii_name="awsSnsTopicArn")
    def aws_sns_topic_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsSnsTopicArn"))

    @aws_sns_topic_arn.setter
    def aws_sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "aws_sns_topic_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsSnsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="copyStatement")
    def copy_statement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "copyStatement"))

    @copy_statement.setter
    def copy_statement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "copy_statement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyStatement", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="errorIntegration")
    def error_integration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorIntegration"))

    @error_integration.setter
    def error_integration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "error_integration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorIntegration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integration")
    def integration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integration"))

    @integration.setter
    def integration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "integration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Pipe, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.pipe.PipeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "copy_statement": "copyStatement",
        "database": "database",
        "name": "name",
        "schema": "schema",
        "auto_ingest": "autoIngest",
        "aws_sns_topic_arn": "awsSnsTopicArn",
        "comment": "comment",
        "error_integration": "errorIntegration",
        "id": "id",
        "integration": "integration",
    },
)
class PipeConfig(cdktf.TerraformMetaArguments):
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
        copy_statement: builtins.str,
        database: builtins.str,
        name: builtins.str,
        schema: builtins.str,
        auto_ingest: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        aws_sns_topic_arn: typing.Optional[builtins.str] = None,
        comment: typing.Optional[builtins.str] = None,
        error_integration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param copy_statement: Specifies the copy statement for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#copy_statement Pipe#copy_statement}
        :param database: The database in which to create the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#database Pipe#database}
        :param name: Specifies the identifier for the pipe; must be unique for the database and schema in which the pipe is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#name Pipe#name}
        :param schema: The schema in which to create the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#schema Pipe#schema}
        :param auto_ingest: Specifies a auto_ingest param for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#auto_ingest Pipe#auto_ingest}
        :param aws_sns_topic_arn: Specifies the Amazon Resource Name (ARN) for the SNS topic for your S3 bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#aws_sns_topic_arn Pipe#aws_sns_topic_arn}
        :param comment: Specifies a comment for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#comment Pipe#comment}
        :param error_integration: Specifies the name of the notification integration used for error notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#error_integration Pipe#error_integration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#id Pipe#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration: Specifies an integration for the pipe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#integration Pipe#integration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(PipeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument copy_statement", value=copy_statement, expected_type=type_hints["copy_statement"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument auto_ingest", value=auto_ingest, expected_type=type_hints["auto_ingest"])
            check_type(argname="argument aws_sns_topic_arn", value=aws_sns_topic_arn, expected_type=type_hints["aws_sns_topic_arn"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument error_integration", value=error_integration, expected_type=type_hints["error_integration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration", value=integration, expected_type=type_hints["integration"])
        self._values: typing.Dict[str, typing.Any] = {
            "copy_statement": copy_statement,
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
        if auto_ingest is not None:
            self._values["auto_ingest"] = auto_ingest
        if aws_sns_topic_arn is not None:
            self._values["aws_sns_topic_arn"] = aws_sns_topic_arn
        if comment is not None:
            self._values["comment"] = comment
        if error_integration is not None:
            self._values["error_integration"] = error_integration
        if id is not None:
            self._values["id"] = id
        if integration is not None:
            self._values["integration"] = integration

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
    def copy_statement(self) -> builtins.str:
        '''Specifies the copy statement for the pipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#copy_statement Pipe#copy_statement}
        '''
        result = self._values.get("copy_statement")
        assert result is not None, "Required property 'copy_statement' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database(self) -> builtins.str:
        '''The database in which to create the pipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#database Pipe#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the identifier for the pipe;

        must be unique for the database and schema in which the pipe is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#name Pipe#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema in which to create the pipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#schema Pipe#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_ingest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies a auto_ingest param for the pipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#auto_ingest Pipe#auto_ingest}
        '''
        result = self._values.get("auto_ingest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def aws_sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the Amazon Resource Name (ARN) for the SNS topic for your S3 bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#aws_sns_topic_arn Pipe#aws_sns_topic_arn}
        '''
        result = self._values.get("aws_sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Specifies a comment for the pipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#comment Pipe#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_integration(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the notification integration used for error notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#error_integration Pipe#error_integration}
        '''
        result = self._values.get("error_integration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#id Pipe#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration(self) -> typing.Optional[builtins.str]:
        '''Specifies an integration for the pipe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/pipe#integration Pipe#integration}
        '''
        result = self._values.get("integration")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Pipe",
    "PipeConfig",
]

publication.publish()
