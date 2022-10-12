'''
# `snowflake_masking_policy`

Refer to the Terraform Registory for docs: [`snowflake_masking_policy`](https://www.terraform.io/docs/providers/snowflake/r/masking_policy).
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


class MaskingPolicy(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.maskingPolicy.MaskingPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy snowflake_masking_policy}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        database: builtins.str,
        masking_expression: builtins.str,
        name: builtins.str,
        return_data_type: builtins.str,
        schema: builtins.str,
        value_data_type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy snowflake_masking_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param database: The database in which to create the masking policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#database MaskingPolicy#database}
        :param masking_expression: Specifies the SQL expression that transforms the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#masking_expression MaskingPolicy#masking_expression}
        :param name: Specifies the identifier for the masking policy; must be unique for the database and schema in which the masking policy is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#name MaskingPolicy#name}
        :param return_data_type: Specifies the data type to return. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#return_data_type MaskingPolicy#return_data_type}
        :param schema: The schema in which to create the masking policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#schema MaskingPolicy#schema}
        :param value_data_type: Specifies the data type to mask. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#value_data_type MaskingPolicy#value_data_type}
        :param comment: Specifies a comment for the masking policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#comment MaskingPolicy#comment}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#id MaskingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MaskingPolicy.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MaskingPolicyConfig(
            database=database,
            masking_expression=masking_expression,
            name=name,
            return_data_type=return_data_type,
            schema=schema,
            value_data_type=value_data_type,
            comment=comment,
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

    @jsii.member(jsii_name="resetComment")
    def reset_comment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComment", []))

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
    @jsii.member(jsii_name="maskingExpressionInput")
    def masking_expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maskingExpressionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="returnDataTypeInput")
    def return_data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "returnDataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="valueDataTypeInput")
    def value_data_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueDataTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "comment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maskingExpression")
    def masking_expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maskingExpression"))

    @masking_expression.setter
    def masking_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "masking_expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maskingExpression", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="returnDataType")
    def return_data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "returnDataType"))

    @return_data_type.setter
    def return_data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "return_data_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "returnDataType", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="valueDataType")
    def value_data_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueDataType"))

    @value_data_type.setter
    def value_data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MaskingPolicy, "value_data_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueDataType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.maskingPolicy.MaskingPolicyConfig",
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
        "masking_expression": "maskingExpression",
        "name": "name",
        "return_data_type": "returnDataType",
        "schema": "schema",
        "value_data_type": "valueDataType",
        "comment": "comment",
        "id": "id",
    },
)
class MaskingPolicyConfig(cdktf.TerraformMetaArguments):
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
        masking_expression: builtins.str,
        name: builtins.str,
        return_data_type: builtins.str,
        schema: builtins.str,
        value_data_type: builtins.str,
        comment: typing.Optional[builtins.str] = None,
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
        :param database: The database in which to create the masking policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#database MaskingPolicy#database}
        :param masking_expression: Specifies the SQL expression that transforms the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#masking_expression MaskingPolicy#masking_expression}
        :param name: Specifies the identifier for the masking policy; must be unique for the database and schema in which the masking policy is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#name MaskingPolicy#name}
        :param return_data_type: Specifies the data type to return. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#return_data_type MaskingPolicy#return_data_type}
        :param schema: The schema in which to create the masking policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#schema MaskingPolicy#schema}
        :param value_data_type: Specifies the data type to mask. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#value_data_type MaskingPolicy#value_data_type}
        :param comment: Specifies a comment for the masking policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#comment MaskingPolicy#comment}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#id MaskingPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(MaskingPolicyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument masking_expression", value=masking_expression, expected_type=type_hints["masking_expression"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument return_data_type", value=return_data_type, expected_type=type_hints["return_data_type"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument value_data_type", value=value_data_type, expected_type=type_hints["value_data_type"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
            "masking_expression": masking_expression,
            "name": name,
            "return_data_type": return_data_type,
            "schema": schema,
            "value_data_type": value_data_type,
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
    def database(self) -> builtins.str:
        '''The database in which to create the masking policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#database MaskingPolicy#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def masking_expression(self) -> builtins.str:
        '''Specifies the SQL expression that transforms the data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#masking_expression MaskingPolicy#masking_expression}
        '''
        result = self._values.get("masking_expression")
        assert result is not None, "Required property 'masking_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the identifier for the masking policy;

        must be unique for the database and schema in which the masking policy is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#name MaskingPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def return_data_type(self) -> builtins.str:
        '''Specifies the data type to return.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#return_data_type MaskingPolicy#return_data_type}
        '''
        result = self._values.get("return_data_type")
        assert result is not None, "Required property 'return_data_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> builtins.str:
        '''The schema in which to create the masking policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#schema MaskingPolicy#schema}
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value_data_type(self) -> builtins.str:
        '''Specifies the data type to mask.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#value_data_type MaskingPolicy#value_data_type}
        '''
        result = self._values.get("value_data_type")
        assert result is not None, "Required property 'value_data_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Specifies a comment for the masking policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#comment MaskingPolicy#comment}
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/masking_policy#id MaskingPolicy#id}.

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
        return "MaskingPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MaskingPolicy",
    "MaskingPolicyConfig",
]

publication.publish()
