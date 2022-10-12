'''
# `okta_group_schema_property`

Refer to the Terraform Registory for docs: [`okta_group_schema_property`](https://www.terraform.io/docs/providers/okta/r/group_schema_property).
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


class GroupSchemaProperty(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaProperty",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property okta_group_schema_property}.'''

    def __init__(
        self,
        scope_: constructs.Construct,
        id_: builtins.str,
        *,
        index: builtins.str,
        title: builtins.str,
        type: builtins.str,
        array_enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        array_one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyArrayOneOf", typing.Dict[str, typing.Any]]]]] = None,
        array_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        external_namespace: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        master: typing.Optional[builtins.str] = None,
        master_override_priority: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyMasterOverridePriority", typing.Dict[str, typing.Any]]]]] = None,
        max_length: typing.Optional[jsii.Number] = None,
        min_length: typing.Optional[jsii.Number] = None,
        one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyOneOf", typing.Dict[str, typing.Any]]]]] = None,
        permissions: typing.Optional[builtins.str] = None,
        required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scope: typing.Optional[builtins.str] = None,
        unique: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property okta_group_schema_property} Resource.

        :param scope_: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param index: Subschema unique string identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#index GroupSchemaProperty#index}
        :param title: Subschema title (display name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#title GroupSchemaProperty#title}
        :param type: Subschema type: string, boolean, number, integer, array, or object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#type GroupSchemaProperty#type}
        :param array_enum: Custom Subschema enumerated value of a property of type array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_enum GroupSchemaProperty#array_enum}
        :param array_one_of: array_one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_one_of GroupSchemaProperty#array_one_of}
        :param array_type: Subschema array type: string, number, integer, reference. Type field must be an array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_type GroupSchemaProperty#array_type}
        :param description: Custom Subschema description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#description GroupSchemaProperty#description}
        :param enum: Custom Subschema enumerated value of the property. see: developer.okta.com/docs/api/resources/schemas#user-profile-schema-property-object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#enum GroupSchemaProperty#enum}
        :param external_name: Subschema external name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#external_name GroupSchemaProperty#external_name}
        :param external_namespace: Subschema external namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#external_namespace GroupSchemaProperty#external_namespace}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#id GroupSchemaProperty#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param master: SubSchema profile manager, if not set it will inherit its setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#master GroupSchemaProperty#master}
        :param master_override_priority: master_override_priority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#master_override_priority GroupSchemaProperty#master_override_priority}
        :param max_length: Subschema of type string maximum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#max_length GroupSchemaProperty#max_length}
        :param min_length: Subschema of type string minimum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#min_length GroupSchemaProperty#min_length}
        :param one_of: one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#one_of GroupSchemaProperty#one_of}
        :param permissions: SubSchema permissions: HIDE, READ_ONLY, or READ_WRITE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#permissions GroupSchemaProperty#permissions}
        :param required: Whether the subschema is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#required GroupSchemaProperty#required}
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#scope GroupSchemaProperty#scope}.
        :param unique: Subschema unique restriction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#unique GroupSchemaProperty#unique}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaProperty.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupSchemaPropertyConfig(
            index=index,
            title=title,
            type=type,
            array_enum=array_enum,
            array_one_of=array_one_of,
            array_type=array_type,
            description=description,
            enum=enum,
            external_name=external_name,
            external_namespace=external_namespace,
            id=id,
            master=master,
            master_override_priority=master_override_priority,
            max_length=max_length,
            min_length=min_length,
            one_of=one_of,
            permissions=permissions,
            required=required,
            scope=scope,
            unique=unique,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope_, id_, config])

    @jsii.member(jsii_name="putArrayOneOf")
    def put_array_one_of(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyArrayOneOf", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaProperty.put_array_one_of)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putArrayOneOf", [value]))

    @jsii.member(jsii_name="putMasterOverridePriority")
    def put_master_override_priority(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyMasterOverridePriority", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaProperty.put_master_override_priority)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMasterOverridePriority", [value]))

    @jsii.member(jsii_name="putOneOf")
    def put_one_of(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyOneOf", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaProperty.put_one_of)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOneOf", [value]))

    @jsii.member(jsii_name="resetArrayEnum")
    def reset_array_enum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArrayEnum", []))

    @jsii.member(jsii_name="resetArrayOneOf")
    def reset_array_one_of(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArrayOneOf", []))

    @jsii.member(jsii_name="resetArrayType")
    def reset_array_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArrayType", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEnum")
    def reset_enum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnum", []))

    @jsii.member(jsii_name="resetExternalName")
    def reset_external_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalName", []))

    @jsii.member(jsii_name="resetExternalNamespace")
    def reset_external_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalNamespace", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaster")
    def reset_master(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaster", []))

    @jsii.member(jsii_name="resetMasterOverridePriority")
    def reset_master_override_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMasterOverridePriority", []))

    @jsii.member(jsii_name="resetMaxLength")
    def reset_max_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLength", []))

    @jsii.member(jsii_name="resetMinLength")
    def reset_min_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinLength", []))

    @jsii.member(jsii_name="resetOneOf")
    def reset_one_of(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOneOf", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetUnique")
    def reset_unique(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnique", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arrayOneOf")
    def array_one_of(self) -> "GroupSchemaPropertyArrayOneOfList":
        return typing.cast("GroupSchemaPropertyArrayOneOfList", jsii.get(self, "arrayOneOf"))

    @builtins.property
    @jsii.member(jsii_name="masterOverridePriority")
    def master_override_priority(
        self,
    ) -> "GroupSchemaPropertyMasterOverridePriorityList":
        return typing.cast("GroupSchemaPropertyMasterOverridePriorityList", jsii.get(self, "masterOverridePriority"))

    @builtins.property
    @jsii.member(jsii_name="oneOf")
    def one_of(self) -> "GroupSchemaPropertyOneOfList":
        return typing.cast("GroupSchemaPropertyOneOfList", jsii.get(self, "oneOf"))

    @builtins.property
    @jsii.member(jsii_name="arrayEnumInput")
    def array_enum_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "arrayEnumInput"))

    @builtins.property
    @jsii.member(jsii_name="arrayOneOfInput")
    def array_one_of_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyArrayOneOf"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyArrayOneOf"]]], jsii.get(self, "arrayOneOfInput"))

    @builtins.property
    @jsii.member(jsii_name="arrayTypeInput")
    def array_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arrayTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="enumInput")
    def enum_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "enumInput"))

    @builtins.property
    @jsii.member(jsii_name="externalNameInput")
    def external_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalNameInput"))

    @builtins.property
    @jsii.member(jsii_name="externalNamespaceInput")
    def external_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="indexInput")
    def index_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="masterInput")
    def master_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "masterInput"))

    @builtins.property
    @jsii.member(jsii_name="masterOverridePriorityInput")
    def master_override_priority_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyMasterOverridePriority"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyMasterOverridePriority"]]], jsii.get(self, "masterOverridePriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLengthInput")
    def max_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="minLengthInput")
    def min_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="oneOfInput")
    def one_of_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyOneOf"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyOneOf"]]], jsii.get(self, "oneOfInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uniqueInput")
    def unique_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uniqueInput"))

    @builtins.property
    @jsii.member(jsii_name="arrayEnum")
    def array_enum(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "arrayEnum"))

    @array_enum.setter
    def array_enum(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "array_enum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arrayEnum", value)

    @builtins.property
    @jsii.member(jsii_name="arrayType")
    def array_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arrayType"))

    @array_type.setter
    def array_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "array_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arrayType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enum")
    def enum(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enum"))

    @enum.setter
    def enum(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "enum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enum", value)

    @builtins.property
    @jsii.member(jsii_name="externalName")
    def external_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalName"))

    @external_name.setter
    def external_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "external_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalName", value)

    @builtins.property
    @jsii.member(jsii_name="externalNamespace")
    def external_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalNamespace"))

    @external_namespace.setter
    def external_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "external_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "index"))

    @index.setter
    def index(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "index").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="master")
    def master(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "master"))

    @master.setter
    def master(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "master").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "master", value)

    @builtins.property
    @jsii.member(jsii_name="maxLength")
    def max_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLength"))

    @max_length.setter
    def max_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "max_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLength", value)

    @builtins.property
    @jsii.member(jsii_name="minLength")
    def min_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minLength"))

    @min_length.setter
    def min_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "min_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLength", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="unique")
    def unique(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unique"))

    @unique.setter
    def unique(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaProperty, "unique").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unique", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyArrayOneOf",
    jsii_struct_bases=[],
    name_mapping={"const": "const", "title": "title"},
)
class GroupSchemaPropertyArrayOneOf:
    def __init__(self, *, const: builtins.str, title: builtins.str) -> None:
        '''
        :param const: Enum value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#const GroupSchemaProperty#const}
        :param title: Enum title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#title GroupSchemaProperty#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaPropertyArrayOneOf.__init__)
            check_type(argname="argument const", value=const, expected_type=type_hints["const"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "const": const,
            "title": title,
        }

    @builtins.property
    def const(self) -> builtins.str:
        '''Enum value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#const GroupSchemaProperty#const}
        '''
        result = self._values.get("const")
        assert result is not None, "Required property 'const' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Enum title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#title GroupSchemaProperty#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupSchemaPropertyArrayOneOf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupSchemaPropertyArrayOneOfList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyArrayOneOfList",
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
            type_hints = typing.get_type_hints(GroupSchemaPropertyArrayOneOfList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GroupSchemaPropertyArrayOneOfOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaPropertyArrayOneOfList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GroupSchemaPropertyArrayOneOfOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyArrayOneOfList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyArrayOneOfList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyArrayOneOfList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyArrayOneOf]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyArrayOneOf]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyArrayOneOf]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyArrayOneOfList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GroupSchemaPropertyArrayOneOfOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyArrayOneOfOutputReference",
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
            type_hints = typing.get_type_hints(GroupSchemaPropertyArrayOneOfOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="constInput")
    def const_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="const")
    def const(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "const"))

    @const.setter
    def const(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyArrayOneOfOutputReference, "const").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "const", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyArrayOneOfOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GroupSchemaPropertyArrayOneOf, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GroupSchemaPropertyArrayOneOf, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GroupSchemaPropertyArrayOneOf, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyArrayOneOfOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "index": "index",
        "title": "title",
        "type": "type",
        "array_enum": "arrayEnum",
        "array_one_of": "arrayOneOf",
        "array_type": "arrayType",
        "description": "description",
        "enum": "enum",
        "external_name": "externalName",
        "external_namespace": "externalNamespace",
        "id": "id",
        "master": "master",
        "master_override_priority": "masterOverridePriority",
        "max_length": "maxLength",
        "min_length": "minLength",
        "one_of": "oneOf",
        "permissions": "permissions",
        "required": "required",
        "scope": "scope",
        "unique": "unique",
    },
)
class GroupSchemaPropertyConfig(cdktf.TerraformMetaArguments):
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
        index: builtins.str,
        title: builtins.str,
        type: builtins.str,
        array_enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        array_one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GroupSchemaPropertyArrayOneOf, typing.Dict[str, typing.Any]]]]] = None,
        array_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        external_namespace: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        master: typing.Optional[builtins.str] = None,
        master_override_priority: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyMasterOverridePriority", typing.Dict[str, typing.Any]]]]] = None,
        max_length: typing.Optional[jsii.Number] = None,
        min_length: typing.Optional[jsii.Number] = None,
        one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GroupSchemaPropertyOneOf", typing.Dict[str, typing.Any]]]]] = None,
        permissions: typing.Optional[builtins.str] = None,
        required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scope: typing.Optional[builtins.str] = None,
        unique: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param index: Subschema unique string identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#index GroupSchemaProperty#index}
        :param title: Subschema title (display name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#title GroupSchemaProperty#title}
        :param type: Subschema type: string, boolean, number, integer, array, or object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#type GroupSchemaProperty#type}
        :param array_enum: Custom Subschema enumerated value of a property of type array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_enum GroupSchemaProperty#array_enum}
        :param array_one_of: array_one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_one_of GroupSchemaProperty#array_one_of}
        :param array_type: Subschema array type: string, number, integer, reference. Type field must be an array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_type GroupSchemaProperty#array_type}
        :param description: Custom Subschema description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#description GroupSchemaProperty#description}
        :param enum: Custom Subschema enumerated value of the property. see: developer.okta.com/docs/api/resources/schemas#user-profile-schema-property-object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#enum GroupSchemaProperty#enum}
        :param external_name: Subschema external name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#external_name GroupSchemaProperty#external_name}
        :param external_namespace: Subschema external namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#external_namespace GroupSchemaProperty#external_namespace}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#id GroupSchemaProperty#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param master: SubSchema profile manager, if not set it will inherit its setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#master GroupSchemaProperty#master}
        :param master_override_priority: master_override_priority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#master_override_priority GroupSchemaProperty#master_override_priority}
        :param max_length: Subschema of type string maximum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#max_length GroupSchemaProperty#max_length}
        :param min_length: Subschema of type string minimum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#min_length GroupSchemaProperty#min_length}
        :param one_of: one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#one_of GroupSchemaProperty#one_of}
        :param permissions: SubSchema permissions: HIDE, READ_ONLY, or READ_WRITE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#permissions GroupSchemaProperty#permissions}
        :param required: Whether the subschema is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#required GroupSchemaProperty#required}
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#scope GroupSchemaProperty#scope}.
        :param unique: Subschema unique restriction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#unique GroupSchemaProperty#unique}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaPropertyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument array_enum", value=array_enum, expected_type=type_hints["array_enum"])
            check_type(argname="argument array_one_of", value=array_one_of, expected_type=type_hints["array_one_of"])
            check_type(argname="argument array_type", value=array_type, expected_type=type_hints["array_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument enum", value=enum, expected_type=type_hints["enum"])
            check_type(argname="argument external_name", value=external_name, expected_type=type_hints["external_name"])
            check_type(argname="argument external_namespace", value=external_namespace, expected_type=type_hints["external_namespace"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument master", value=master, expected_type=type_hints["master"])
            check_type(argname="argument master_override_priority", value=master_override_priority, expected_type=type_hints["master_override_priority"])
            check_type(argname="argument max_length", value=max_length, expected_type=type_hints["max_length"])
            check_type(argname="argument min_length", value=min_length, expected_type=type_hints["min_length"])
            check_type(argname="argument one_of", value=one_of, expected_type=type_hints["one_of"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument unique", value=unique, expected_type=type_hints["unique"])
        self._values: typing.Dict[str, typing.Any] = {
            "index": index,
            "title": title,
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
        if array_enum is not None:
            self._values["array_enum"] = array_enum
        if array_one_of is not None:
            self._values["array_one_of"] = array_one_of
        if array_type is not None:
            self._values["array_type"] = array_type
        if description is not None:
            self._values["description"] = description
        if enum is not None:
            self._values["enum"] = enum
        if external_name is not None:
            self._values["external_name"] = external_name
        if external_namespace is not None:
            self._values["external_namespace"] = external_namespace
        if id is not None:
            self._values["id"] = id
        if master is not None:
            self._values["master"] = master
        if master_override_priority is not None:
            self._values["master_override_priority"] = master_override_priority
        if max_length is not None:
            self._values["max_length"] = max_length
        if min_length is not None:
            self._values["min_length"] = min_length
        if one_of is not None:
            self._values["one_of"] = one_of
        if permissions is not None:
            self._values["permissions"] = permissions
        if required is not None:
            self._values["required"] = required
        if scope is not None:
            self._values["scope"] = scope
        if unique is not None:
            self._values["unique"] = unique

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
    def index(self) -> builtins.str:
        '''Subschema unique string identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#index GroupSchemaProperty#index}
        '''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Subschema title (display name).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#title GroupSchemaProperty#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Subschema type: string, boolean, number, integer, array, or object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#type GroupSchemaProperty#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def array_enum(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Custom Subschema enumerated value of a property of type array.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_enum GroupSchemaProperty#array_enum}
        '''
        result = self._values.get("array_enum")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def array_one_of(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyArrayOneOf]]]:
        '''array_one_of block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_one_of GroupSchemaProperty#array_one_of}
        '''
        result = self._values.get("array_one_of")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyArrayOneOf]]], result)

    @builtins.property
    def array_type(self) -> typing.Optional[builtins.str]:
        '''Subschema array type: string, number, integer, reference. Type field must be an array.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#array_type GroupSchemaProperty#array_type}
        '''
        result = self._values.get("array_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Custom Subschema description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#description GroupSchemaProperty#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enum(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Custom Subschema enumerated value of the property. see: developer.okta.com/docs/api/resources/schemas#user-profile-schema-property-object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#enum GroupSchemaProperty#enum}
        '''
        result = self._values.get("enum")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_name(self) -> typing.Optional[builtins.str]:
        '''Subschema external name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#external_name GroupSchemaProperty#external_name}
        '''
        result = self._values.get("external_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_namespace(self) -> typing.Optional[builtins.str]:
        '''Subschema external namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#external_namespace GroupSchemaProperty#external_namespace}
        '''
        result = self._values.get("external_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#id GroupSchemaProperty#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master(self) -> typing.Optional[builtins.str]:
        '''SubSchema profile manager, if not set it will inherit its setting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#master GroupSchemaProperty#master}
        '''
        result = self._values.get("master")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master_override_priority(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyMasterOverridePriority"]]]:
        '''master_override_priority block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#master_override_priority GroupSchemaProperty#master_override_priority}
        '''
        result = self._values.get("master_override_priority")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyMasterOverridePriority"]]], result)

    @builtins.property
    def max_length(self) -> typing.Optional[jsii.Number]:
        '''Subschema of type string maximum length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#max_length GroupSchemaProperty#max_length}
        '''
        result = self._values.get("max_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_length(self) -> typing.Optional[jsii.Number]:
        '''Subschema of type string minimum length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#min_length GroupSchemaProperty#min_length}
        '''
        result = self._values.get("min_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def one_of(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyOneOf"]]]:
        '''one_of block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#one_of GroupSchemaProperty#one_of}
        '''
        result = self._values.get("one_of")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GroupSchemaPropertyOneOf"]]], result)

    @builtins.property
    def permissions(self) -> typing.Optional[builtins.str]:
        '''SubSchema permissions: HIDE, READ_ONLY, or READ_WRITE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#permissions GroupSchemaProperty#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the subschema is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#required GroupSchemaProperty#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#scope GroupSchemaProperty#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unique(self) -> typing.Optional[builtins.str]:
        '''Subschema unique restriction.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#unique GroupSchemaProperty#unique}
        '''
        result = self._values.get("unique")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupSchemaPropertyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyMasterOverridePriority",
    jsii_struct_bases=[],
    name_mapping={"value": "value", "type": "type"},
)
class GroupSchemaPropertyMasterOverridePriority:
    def __init__(
        self,
        *,
        value: builtins.str,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#value GroupSchemaProperty#value}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#type GroupSchemaProperty#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaPropertyMasterOverridePriority.__init__)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "value": value,
        }
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def value(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#value GroupSchemaProperty#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#type GroupSchemaProperty#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupSchemaPropertyMasterOverridePriority(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupSchemaPropertyMasterOverridePriorityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyMasterOverridePriorityList",
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
            type_hints = typing.get_type_hints(GroupSchemaPropertyMasterOverridePriorityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GroupSchemaPropertyMasterOverridePriorityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaPropertyMasterOverridePriorityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GroupSchemaPropertyMasterOverridePriorityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyMasterOverridePriorityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyMasterOverridePriorityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyMasterOverridePriorityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyMasterOverridePriority]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyMasterOverridePriority]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyMasterOverridePriority]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyMasterOverridePriorityList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GroupSchemaPropertyMasterOverridePriorityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyMasterOverridePriorityOutputReference",
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
            type_hints = typing.get_type_hints(GroupSchemaPropertyMasterOverridePriorityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyMasterOverridePriorityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyMasterOverridePriorityOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GroupSchemaPropertyMasterOverridePriority, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GroupSchemaPropertyMasterOverridePriority, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GroupSchemaPropertyMasterOverridePriority, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyMasterOverridePriorityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyOneOf",
    jsii_struct_bases=[],
    name_mapping={"const": "const", "title": "title"},
)
class GroupSchemaPropertyOneOf:
    def __init__(self, *, const: builtins.str, title: builtins.str) -> None:
        '''
        :param const: Enum value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#const GroupSchemaProperty#const}
        :param title: Enum title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#title GroupSchemaProperty#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaPropertyOneOf.__init__)
            check_type(argname="argument const", value=const, expected_type=type_hints["const"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "const": const,
            "title": title,
        }

    @builtins.property
    def const(self) -> builtins.str:
        '''Enum value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#const GroupSchemaProperty#const}
        '''
        result = self._values.get("const")
        assert result is not None, "Required property 'const' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Enum title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/group_schema_property#title GroupSchemaProperty#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupSchemaPropertyOneOf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GroupSchemaPropertyOneOfList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyOneOfList",
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
            type_hints = typing.get_type_hints(GroupSchemaPropertyOneOfList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GroupSchemaPropertyOneOfOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupSchemaPropertyOneOfList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GroupSchemaPropertyOneOfOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyOneOfList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyOneOfList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyOneOfList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyOneOf]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyOneOf]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GroupSchemaPropertyOneOf]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyOneOfList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GroupSchemaPropertyOneOfOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.groupSchemaProperty.GroupSchemaPropertyOneOfOutputReference",
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
            type_hints = typing.get_type_hints(GroupSchemaPropertyOneOfOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="constInput")
    def const_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "constInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="const")
    def const(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "const"))

    @const.setter
    def const(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyOneOfOutputReference, "const").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "const", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyOneOfOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GroupSchemaPropertyOneOf, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GroupSchemaPropertyOneOf, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GroupSchemaPropertyOneOf, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupSchemaPropertyOneOfOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GroupSchemaProperty",
    "GroupSchemaPropertyArrayOneOf",
    "GroupSchemaPropertyArrayOneOfList",
    "GroupSchemaPropertyArrayOneOfOutputReference",
    "GroupSchemaPropertyConfig",
    "GroupSchemaPropertyMasterOverridePriority",
    "GroupSchemaPropertyMasterOverridePriorityList",
    "GroupSchemaPropertyMasterOverridePriorityOutputReference",
    "GroupSchemaPropertyOneOf",
    "GroupSchemaPropertyOneOfList",
    "GroupSchemaPropertyOneOfOutputReference",
]

publication.publish()
