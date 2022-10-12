'''
# `snowflake_external_function`

Refer to the Terraform Registory for docs: [`snowflake_external_function`](https://www.terraform.io/docs/providers/snowflake/r/external_function).
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


class ExternalFunction(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunction",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/external_function snowflake_external_function}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        api_integration: builtins.str,
        database: builtins.str,
        name: builtins.str,
        return_behavior: builtins.str,
        return_type: builtins.str,
        schema: builtins.str,
        url_of_proxy_and_resource: builtins.str,
        arg: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ExternalFunctionArg", typing.Dict[str, typing.Any]]]]] = None,
        comment: typing.Optional[builtins.str] = None,
        compression: typing.Optional[builtins.str] = None,
        context_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ExternalFunctionHeader", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        max_batch_rows: typing.Optional[jsii.Number] = None,
        null_input_behavior: typing.Optional[builtins.str] = None,
        return_null_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/external_function snowflake_external_function} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param api_integration: The name of the API integration object that should be used to authenticate the call to the proxy service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#api_integration ExternalFunction#api_integration}
        :param database: The database in which to create the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#database ExternalFunction#database}
        :param name: Specifies the identifier for the external function. The identifier can contain the schema name and database name, as well as the function name. The function's signature (name and argument data types) must be unique within the schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#name ExternalFunction#name}
        :param return_behavior: Specifies the behavior of the function when returning results. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_behavior ExternalFunction#return_behavior}
        :param return_type: Specifies the data type returned by the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_type ExternalFunction#return_type}
        :param schema: The schema in which to create the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#schema ExternalFunction#schema}
        :param url_of_proxy_and_resource: This is the invocation URL of the proxy service and resource through which Snowflake calls the remote service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#url_of_proxy_and_resource ExternalFunction#url_of_proxy_and_resource}
        :param arg: arg block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#arg ExternalFunction#arg}
        :param comment: A description of the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#comment ExternalFunction#comment}
        :param compression: If specified, the JSON payload is compressed when sent from Snowflake to the proxy service, and when sent back from the proxy service to Snowflake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#compression ExternalFunction#compression}
        :param context_headers: Binds Snowflake context function results to HTTP headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#context_headers ExternalFunction#context_headers}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#header ExternalFunction#header}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#id ExternalFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_batch_rows: This specifies the maximum number of rows in each batch sent to the proxy service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#max_batch_rows ExternalFunction#max_batch_rows}
        :param null_input_behavior: Specifies the behavior of the external function when called with null inputs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#null_input_behavior ExternalFunction#null_input_behavior}
        :param return_null_allowed: Indicates whether the function can return NULL values or must return only NON-NULL values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_null_allowed ExternalFunction#return_null_allowed}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunction.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ExternalFunctionConfig(
            api_integration=api_integration,
            database=database,
            name=name,
            return_behavior=return_behavior,
            return_type=return_type,
            schema=schema,
            url_of_proxy_and_resource=url_of_proxy_and_resource,
            arg=arg,
            comment=comment,
            compression=compression,
            context_headers=context_headers,
            header=header,
            id=id,
            max_batch_rows=max_batch_rows,
            null_input_behavior=null_input_behavior,
            return_null_allowed=return_null_allowed,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putArg")
    def put_arg(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ExternalFunctionArg", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunction.put_arg)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putArg", [value]))

    @jsii.member(jsii_name="putHeader")
    def put_header(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ExternalFunctionHeader", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunction.put_header)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHeader", [value]))

    @jsii.member(jsii_name="resetArg")
    def reset_arg(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArg", []))

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetContextHeaders")
    def reset_context_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContextHeaders", []))

    @jsii.member(jsii_name="resetHeader")
    def reset_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeader", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxBatchRows")
    def reset_max_batch_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBatchRows", []))

    @jsii.member(jsii_name="resetNullInputBehavior")
    def reset_null_input_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullInputBehavior", []))

    @jsii.member(jsii_name="resetReturnNullAllowed")
    def reset_return_null_allowed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReturnNullAllowed", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arg")
    def arg(self) -> "ExternalFunctionArgList":
        return typing.cast("ExternalFunctionArgList", jsii.get(self, "arg"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> "ExternalFunctionHeaderList":
        return typing.cast("ExternalFunctionHeaderList", jsii.get(self, "header"))

    @builtins.property
    @jsii.member(jsii_name="apiIntegrationInput")
    def api_integration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiIntegrationInput"))

    @builtins.property
    @jsii.member(jsii_name="argInput")
    def arg_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ExternalFunctionArg"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ExternalFunctionArg"]]], jsii.get(self, "argInput"))

    @builtins.property
    @jsii.member(jsii_name="commentInput")
    def comment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="contextHeadersInput")
    def context_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contextHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ExternalFunctionHeader"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ExternalFunctionHeader"]]], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBatchRowsInput")
    def max_batch_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBatchRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nullInputBehaviorInput")
    def null_input_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nullInputBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="returnBehaviorInput")
    def return_behavior_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "returnBehaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="returnNullAllowedInput")
    def return_null_allowed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "returnNullAllowedInput"))

    @builtins.property
    @jsii.member(jsii_name="returnTypeInput")
    def return_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "returnTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="urlOfProxyAndResourceInput")
    def url_of_proxy_and_resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlOfProxyAndResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="apiIntegration")
    def api_integration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiIntegration"))

    @api_integration.setter
    def api_integration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "api_integration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiIntegration", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "compression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="contextHeaders")
    def context_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contextHeaders"))

    @context_headers.setter
    def context_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "context_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contextHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxBatchRows")
    def max_batch_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBatchRows"))

    @max_batch_rows.setter
    def max_batch_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "max_batch_rows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBatchRows", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nullInputBehavior")
    def null_input_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nullInputBehavior"))

    @null_input_behavior.setter
    def null_input_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "null_input_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullInputBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="returnBehavior")
    def return_behavior(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "returnBehavior"))

    @return_behavior.setter
    def return_behavior(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "return_behavior").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="returnNullAllowed")
    def return_null_allowed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "returnNullAllowed"))

    @return_null_allowed.setter
    def return_null_allowed(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "return_null_allowed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnNullAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="returnType")
    def return_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "returnType"))

    @return_type.setter
    def return_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "return_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnType", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="urlOfProxyAndResource")
    def url_of_proxy_and_resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlOfProxyAndResource"))

    @url_of_proxy_and_resource.setter
    def url_of_proxy_and_resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunction, "url_of_proxy_and_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlOfProxyAndResource", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunctionArg",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "type": "type"},
)
class ExternalFunctionArg:
    def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
        '''
        :param name: Argument name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#name ExternalFunction#name}
        :param type: Argument type, e.g. VARCHAR. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#type ExternalFunction#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunctionArg.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Argument name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#name ExternalFunction#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Argument type, e.g. VARCHAR.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#type ExternalFunction#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalFunctionArg(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalFunctionArgList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunctionArgList",
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
            type_hints = typing.get_type_hints(ExternalFunctionArgList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ExternalFunctionArgOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunctionArgList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ExternalFunctionArgOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionArgList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ExternalFunctionArgList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ExternalFunctionArgList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionArg]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionArg]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionArg]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionArgList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ExternalFunctionArgOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunctionArgOutputReference",
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
            type_hints = typing.get_type_hints(ExternalFunctionArgOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ExternalFunctionArgOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionArgOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ExternalFunctionArg, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ExternalFunctionArg, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ExternalFunctionArg, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionArgOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunctionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "api_integration": "apiIntegration",
        "database": "database",
        "name": "name",
        "return_behavior": "returnBehavior",
        "return_type": "returnType",
        "schema": "schema",
        "url_of_proxy_and_resource": "urlOfProxyAndResource",
        "arg": "arg",
        "comment": "comment",
        "compression": "compression",
        "context_headers": "contextHeaders",
        "header": "header",
        "id": "id",
        "max_batch_rows": "maxBatchRows",
        "null_input_behavior": "nullInputBehavior",
        "return_null_allowed": "returnNullAllowed",
    },
)
class ExternalFunctionConfig(cdktf.TerraformMetaArguments):
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
        api_integration: builtins.str,
        database: builtins.str,
        name: builtins.str,
        return_behavior: builtins.str,
        return_type: builtins.str,
        schema: builtins.str,
        url_of_proxy_and_resource: builtins.str,
        arg: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ExternalFunctionArg, typing.Dict[str, typing.Any]]]]] = None,
        comment: typing.Optional[builtins.str] = None,
        compression: typing.Optional[builtins.str] = None,
        context_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        header: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ExternalFunctionHeader", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        max_batch_rows: typing.Optional[jsii.Number] = None,
        null_input_behavior: typing.Optional[builtins.str] = None,
        return_null_allowed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param api_integration: The name of the API integration object that should be used to authenticate the call to the proxy service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#api_integration ExternalFunction#api_integration}
        :param database: The database in which to create the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#database ExternalFunction#database}
        :param name: Specifies the identifier for the external function. The identifier can contain the schema name and database name, as well as the function name. The function's signature (name and argument data types) must be unique within the schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#name ExternalFunction#name}
        :param return_behavior: Specifies the behavior of the function when returning results. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_behavior ExternalFunction#return_behavior}
        :param return_type: Specifies the data type returned by the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_type ExternalFunction#return_type}
        :param schema: The schema in which to create the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#schema ExternalFunction#schema}
        :param url_of_proxy_and_resource: This is the invocation URL of the proxy service and resource through which Snowflake calls the remote service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#url_of_proxy_and_resource ExternalFunction#url_of_proxy_and_resource}
        :param arg: arg block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#arg ExternalFunction#arg}
        :param comment: A description of the external function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#comment ExternalFunction#comment}
        :param compression: If specified, the JSON payload is compressed when sent from Snowflake to the proxy service, and when sent back from the proxy service to Snowflake. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#compression ExternalFunction#compression}
        :param context_headers: Binds Snowflake context function results to HTTP headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#context_headers ExternalFunction#context_headers}
        :param header: header block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#header ExternalFunction#header}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#id ExternalFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_batch_rows: This specifies the maximum number of rows in each batch sent to the proxy service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#max_batch_rows ExternalFunction#max_batch_rows}
        :param null_input_behavior: Specifies the behavior of the external function when called with null inputs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#null_input_behavior ExternalFunction#null_input_behavior}
        :param return_null_allowed: Indicates whether the function can return NULL values or must return only NON-NULL values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_null_allowed ExternalFunction#return_null_allowed}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunctionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument api_integration", value=api_integration, expected_type=type_hints["api_integration"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument return_behavior", value=return_behavior, expected_type=type_hints["return_behavior"])
            check_type(argname="argument return_type", value=return_type, expected_type=type_hints["return_type"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument url_of_proxy_and_resource", value=url_of_proxy_and_resource, expected_type=type_hints["url_of_proxy_and_resource"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument context_headers", value=context_headers, expected_type=type_hints["context_headers"])
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_batch_rows", value=max_batch_rows, expected_type=type_hints["max_batch_rows"])
            check_type(argname="argument null_input_behavior", value=null_input_behavior, expected_type=type_hints["null_input_behavior"])
            check_type(argname="argument return_null_allowed", value=return_null_allowed, expected_type=type_hints["return_null_allowed"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_integration": api_integration,
            "database": database,
            "name": name,
            "return_behavior": return_behavior,
            "return_type": return_type,
            "schema": schema,
            "url_of_proxy_and_resource": url_of_proxy_and_resource,
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
        if arg is not None:
            self._values["arg"] = arg
        if comment is not None:
            self._values["comment"] = comment
        if compression is not None:
            self._values["compression"] = compression
        if context_headers is not None:
            self._values["context_headers"] = context_headers
        if header is not None:
            self._values["header"] = header
        if id is not None:
            self._values["id"] = id
        if max_batch_rows is not None:
            self._values["max_batch_rows"] = max_batch_rows
        if null_input_behavior is not None:
            self._values["null_input_behavior"] = null_input_behavior
        if return_null_allowed is not None:
            self._values["return_null_allowed"] = return_null_allowed

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
    def api_integration(self) -> builtins.str:
        '''The name of the API integration object that should be used to authenticate the call to the proxy service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#api_integration ExternalFunction#api_integration}
        '''
        result = self._values.get("api_integration")
        assert result is not None, "Required property 'api_integration' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database(self) -> builtins.str:
        '''The database in which to create the external function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#database ExternalFunction#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the identifier for the external function.

        The identifier can contain the schema name and database name, as well as the function name. The function's signature (name and argument data types) must be unique within the schema.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#name ExternalFunction#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def return_behavior(self) -> builtins.str:
        '''Specifies the behavior of the function when returning results.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_behavior ExternalFunction#return_behavior}
        '''
        result = self._values.get("return_behavior")
        assert result is not None, "Required property 'return_behavior' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def return_type(self) -> builtins.str:
        '''Specifies the data type returned by the external function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_type ExternalFunction#return_type}
        '''
        result = self._values.get("return_type")
        assert result is not None, "Required property 'return_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema in which to create the external function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#schema ExternalFunction#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url_of_proxy_and_resource(self) -> builtins.str:
        '''This is the invocation URL of the proxy service and resource through which Snowflake calls the remote service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#url_of_proxy_and_resource ExternalFunction#url_of_proxy_and_resource}
        '''
        result = self._values.get("url_of_proxy_and_resource")
        assert result is not None, "Required property 'url_of_proxy_and_resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def arg(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionArg]]]:
        '''arg block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#arg ExternalFunction#arg}
        '''
        result = self._values.get("arg")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionArg]]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A description of the external function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#comment ExternalFunction#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''If specified, the JSON payload is compressed when sent from Snowflake to the proxy service, and when sent back from the proxy service to Snowflake.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#compression ExternalFunction#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def context_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Binds Snowflake context function results to HTTP headers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#context_headers ExternalFunction#context_headers}
        '''
        result = self._values.get("context_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def header(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ExternalFunctionHeader"]]]:
        '''header block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#header ExternalFunction#header}
        '''
        result = self._values.get("header")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ExternalFunctionHeader"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#id ExternalFunction#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_batch_rows(self) -> typing.Optional[jsii.Number]:
        '''This specifies the maximum number of rows in each batch sent to the proxy service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#max_batch_rows ExternalFunction#max_batch_rows}
        '''
        result = self._values.get("max_batch_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def null_input_behavior(self) -> typing.Optional[builtins.str]:
        '''Specifies the behavior of the external function when called with null inputs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#null_input_behavior ExternalFunction#null_input_behavior}
        '''
        result = self._values.get("null_input_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def return_null_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the function can return NULL values or must return only NON-NULL values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#return_null_allowed ExternalFunction#return_null_allowed}
        '''
        result = self._values.get("return_null_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalFunctionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunctionHeader",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class ExternalFunctionHeader:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: Header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#name ExternalFunction#name}
        :param value: Header value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#value ExternalFunction#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunctionHeader.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#name ExternalFunction#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Header value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/external_function#value ExternalFunction#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExternalFunctionHeader(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ExternalFunctionHeaderList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunctionHeaderList",
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
            type_hints = typing.get_type_hints(ExternalFunctionHeaderList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ExternalFunctionHeaderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ExternalFunctionHeaderList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ExternalFunctionHeaderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionHeaderList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ExternalFunctionHeaderList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ExternalFunctionHeaderList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionHeader]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionHeader]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ExternalFunctionHeader]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionHeaderList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ExternalFunctionHeaderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.externalFunction.ExternalFunctionHeaderOutputReference",
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
            type_hints = typing.get_type_hints(ExternalFunctionHeaderOutputReference.__init__)
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
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionHeaderOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionHeaderOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ExternalFunctionHeader, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ExternalFunctionHeader, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ExternalFunctionHeader, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ExternalFunctionHeaderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ExternalFunction",
    "ExternalFunctionArg",
    "ExternalFunctionArgList",
    "ExternalFunctionArgOutputReference",
    "ExternalFunctionConfig",
    "ExternalFunctionHeader",
    "ExternalFunctionHeaderList",
    "ExternalFunctionHeaderOutputReference",
]

publication.publish()
