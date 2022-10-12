'''
# `snowflake_tag_association`

Refer to the Terraform Registory for docs: [`snowflake_tag_association`](https://www.terraform.io/docs/providers/snowflake/r/tag_association).
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


class TagAssociation(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.tagAssociation.TagAssociation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association snowflake_tag_association}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        object_name: builtins.str,
        object_type: builtins.str,
        tag_id: builtins.str,
        tag_value: builtins.str,
        id: typing.Optional[builtins.str] = None,
        skip_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["TagAssociationTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association snowflake_tag_association} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param object_name: Specifies the object identifier for the tag association. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#object_name TagAssociation#object_name}
        :param object_type: Specifies the type of object to add a tag to. ex: 'ACCOUNT', 'COLUMN', 'DATABASE', etc. For more information: https://docs.snowflake.com/en/user-guide/object-tagging.html#supported-objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#object_type TagAssociation#object_type}
        :param tag_id: Specifies the identifier for the tag. Note: format must follow: "databaseName"."schemaName"."tagName" or "databaseName.schemaName.tagName" or "databaseName|schemaName.tagName" (snowflake_tag.tag.id). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#tag_id TagAssociation#tag_id}
        :param tag_value: Specifies the value of the tag, (e.g. 'finance' or 'engineering'). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#tag_value TagAssociation#tag_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#id TagAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param skip_validation: If true, skips validation of the tag association. It can take up to an hour for the SNOWFLAKE.TAG_REFERENCES table to update, and also requires ACCOUNT_ADMIN role to read from. https://docs.snowflake.com/en/sql-reference/account-usage/tag_references.html Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#skip_validation TagAssociation#skip_validation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#timeouts TagAssociation#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TagAssociation.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TagAssociationConfig(
            object_name=object_name,
            object_type=object_type,
            tag_id=tag_id,
            tag_value=tag_value,
            id=id,
            skip_validation=skip_validation,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#create TagAssociation#create}.
        '''
        value = TagAssociationTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSkipValidation")
    def reset_skip_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipValidation", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "TagAssociationTimeoutsOutputReference":
        return typing.cast("TagAssociationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="objectNameInput")
    def object_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectNameInput"))

    @builtins.property
    @jsii.member(jsii_name="objectTypeInput")
    def object_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="skipValidationInput")
    def skip_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagIdInput")
    def tag_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["TagAssociationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["TagAssociationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociation, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="objectName")
    def object_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectName"))

    @object_name.setter
    def object_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociation, "object_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectName", value)

    @builtins.property
    @jsii.member(jsii_name="objectType")
    def object_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectType"))

    @object_type.setter
    def object_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociation, "object_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectType", value)

    @builtins.property
    @jsii.member(jsii_name="skipValidation")
    def skip_validation(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipValidation"))

    @skip_validation.setter
    def skip_validation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociation, "skip_validation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipValidation", value)

    @builtins.property
    @jsii.member(jsii_name="tagId")
    def tag_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagId"))

    @tag_id.setter
    def tag_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociation, "tag_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagId", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociation, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.tagAssociation.TagAssociationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "object_name": "objectName",
        "object_type": "objectType",
        "tag_id": "tagId",
        "tag_value": "tagValue",
        "id": "id",
        "skip_validation": "skipValidation",
        "timeouts": "timeouts",
    },
)
class TagAssociationConfig(cdktf.TerraformMetaArguments):
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
        object_name: builtins.str,
        object_type: builtins.str,
        tag_id: builtins.str,
        tag_value: builtins.str,
        id: typing.Optional[builtins.str] = None,
        skip_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["TagAssociationTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param object_name: Specifies the object identifier for the tag association. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#object_name TagAssociation#object_name}
        :param object_type: Specifies the type of object to add a tag to. ex: 'ACCOUNT', 'COLUMN', 'DATABASE', etc. For more information: https://docs.snowflake.com/en/user-guide/object-tagging.html#supported-objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#object_type TagAssociation#object_type}
        :param tag_id: Specifies the identifier for the tag. Note: format must follow: "databaseName"."schemaName"."tagName" or "databaseName.schemaName.tagName" or "databaseName|schemaName.tagName" (snowflake_tag.tag.id). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#tag_id TagAssociation#tag_id}
        :param tag_value: Specifies the value of the tag, (e.g. 'finance' or 'engineering'). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#tag_value TagAssociation#tag_value}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#id TagAssociation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param skip_validation: If true, skips validation of the tag association. It can take up to an hour for the SNOWFLAKE.TAG_REFERENCES table to update, and also requires ACCOUNT_ADMIN role to read from. https://docs.snowflake.com/en/sql-reference/account-usage/tag_references.html Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#skip_validation TagAssociation#skip_validation}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#timeouts TagAssociation#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = TagAssociationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(TagAssociationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument object_name", value=object_name, expected_type=type_hints["object_name"])
            check_type(argname="argument object_type", value=object_type, expected_type=type_hints["object_type"])
            check_type(argname="argument tag_id", value=tag_id, expected_type=type_hints["tag_id"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument skip_validation", value=skip_validation, expected_type=type_hints["skip_validation"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "object_name": object_name,
            "object_type": object_type,
            "tag_id": tag_id,
            "tag_value": tag_value,
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
        if id is not None:
            self._values["id"] = id
        if skip_validation is not None:
            self._values["skip_validation"] = skip_validation
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def object_name(self) -> builtins.str:
        '''Specifies the object identifier for the tag association.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#object_name TagAssociation#object_name}
        '''
        result = self._values.get("object_name")
        assert result is not None, "Required property 'object_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type(self) -> builtins.str:
        '''Specifies the type of object to add a tag to. ex: 'ACCOUNT', 'COLUMN', 'DATABASE', etc. For more information: https://docs.snowflake.com/en/user-guide/object-tagging.html#supported-objects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#object_type TagAssociation#object_type}
        '''
        result = self._values.get("object_type")
        assert result is not None, "Required property 'object_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_id(self) -> builtins.str:
        '''Specifies the identifier for the tag. Note: format must follow: "databaseName"."schemaName"."tagName" or "databaseName.schemaName.tagName" or "databaseName|schemaName.tagName" (snowflake_tag.tag.id).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#tag_id TagAssociation#tag_id}
        '''
        result = self._values.get("tag_id")
        assert result is not None, "Required property 'tag_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_value(self) -> builtins.str:
        '''Specifies the value of the tag, (e.g. 'finance' or 'engineering').

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#tag_value TagAssociation#tag_value}
        '''
        result = self._values.get("tag_value")
        assert result is not None, "Required property 'tag_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#id TagAssociation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, skips validation of the tag association.

        It can take up to an hour for the SNOWFLAKE.TAG_REFERENCES table to update, and also requires ACCOUNT_ADMIN role to read from. https://docs.snowflake.com/en/sql-reference/account-usage/tag_references.html

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#skip_validation TagAssociation#skip_validation}
        '''
        result = self._values.get("skip_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["TagAssociationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#timeouts TagAssociation#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["TagAssociationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagAssociationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-snowflake.tagAssociation.TagAssociationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class TagAssociationTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#create TagAssociation#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(TagAssociationTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/snowflake/r/tag_association#create TagAssociation#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagAssociationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TagAssociationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-snowflake.tagAssociation.TagAssociationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(TagAssociationTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[TagAssociationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[TagAssociationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[TagAssociationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(TagAssociationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "TagAssociation",
    "TagAssociationConfig",
    "TagAssociationTimeouts",
    "TagAssociationTimeoutsOutputReference",
]

publication.publish()
