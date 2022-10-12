'''
# `okta_app_user_schema_property`

Refer to the Terraform Registory for docs: [`okta_app_user_schema_property`](https://www.terraform.io/docs/providers/okta/r/app_user_schema_property).
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


class AppUserSchemaProperty(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaProperty",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property okta_app_user_schema_property}.'''

    def __init__(
        self,
        scope_: constructs.Construct,
        id_: builtins.str,
        *,
        app_id: builtins.str,
        index: builtins.str,
        title: builtins.str,
        type: builtins.str,
        array_enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        array_one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppUserSchemaPropertyArrayOneOf", typing.Dict[str, typing.Any]]]]] = None,
        array_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        external_namespace: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        master: typing.Optional[builtins.str] = None,
        max_length: typing.Optional[jsii.Number] = None,
        min_length: typing.Optional[jsii.Number] = None,
        one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppUserSchemaPropertyOneOf", typing.Dict[str, typing.Any]]]]] = None,
        permissions: typing.Optional[builtins.str] = None,
        required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scope: typing.Optional[builtins.str] = None,
        union: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        unique: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property okta_app_user_schema_property} Resource.

        :param scope_: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#app_id AppUserSchemaProperty#app_id}.
        :param index: Subschema unique string identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#index AppUserSchemaProperty#index}
        :param title: Subschema title (display name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#title AppUserSchemaProperty#title}
        :param type: Subschema type: string, boolean, number, integer, array, or object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#type AppUserSchemaProperty#type}
        :param array_enum: Custom Subschema enumerated value of a property of type array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_enum AppUserSchemaProperty#array_enum}
        :param array_one_of: array_one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_one_of AppUserSchemaProperty#array_one_of}
        :param array_type: Subschema array type: string, number, integer, reference. Type field must be an array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_type AppUserSchemaProperty#array_type}
        :param description: Custom Subschema description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#description AppUserSchemaProperty#description}
        :param enum: Custom Subschema enumerated value of the property. see: developer.okta.com/docs/api/resources/schemas#user-profile-schema-property-object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#enum AppUserSchemaProperty#enum}
        :param external_name: Subschema external name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#external_name AppUserSchemaProperty#external_name}
        :param external_namespace: Subschema external namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#external_namespace AppUserSchemaProperty#external_namespace}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#id AppUserSchemaProperty#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param master: SubSchema profile manager, if not set it will inherit its setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#master AppUserSchemaProperty#master}
        :param max_length: Subschema of type string maximum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#max_length AppUserSchemaProperty#max_length}
        :param min_length: Subschema of type string minimum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#min_length AppUserSchemaProperty#min_length}
        :param one_of: one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#one_of AppUserSchemaProperty#one_of}
        :param permissions: SubSchema permissions: HIDE, READ_ONLY, or READ_WRITE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#permissions AppUserSchemaProperty#permissions}
        :param required: Whether the subschema is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#required AppUserSchemaProperty#required}
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#scope AppUserSchemaProperty#scope}.
        :param union: Allows to assign attribute's group priority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#union AppUserSchemaProperty#union}
        :param unique: Subschema unique restriction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#unique AppUserSchemaProperty#unique}
        :param user_type: Custom subschema user type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#user_type AppUserSchemaProperty#user_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaProperty.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppUserSchemaPropertyConfig(
            app_id=app_id,
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
            max_length=max_length,
            min_length=min_length,
            one_of=one_of,
            permissions=permissions,
            required=required,
            scope=scope,
            union=union,
            unique=unique,
            user_type=user_type,
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
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppUserSchemaPropertyArrayOneOf", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaProperty.put_array_one_of)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putArrayOneOf", [value]))

    @jsii.member(jsii_name="putOneOf")
    def put_one_of(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppUserSchemaPropertyOneOf", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaProperty.put_one_of)
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

    @jsii.member(jsii_name="resetUnion")
    def reset_union(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnion", []))

    @jsii.member(jsii_name="resetUnique")
    def reset_unique(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnique", []))

    @jsii.member(jsii_name="resetUserType")
    def reset_user_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arrayOneOf")
    def array_one_of(self) -> "AppUserSchemaPropertyArrayOneOfList":
        return typing.cast("AppUserSchemaPropertyArrayOneOfList", jsii.get(self, "arrayOneOf"))

    @builtins.property
    @jsii.member(jsii_name="oneOf")
    def one_of(self) -> "AppUserSchemaPropertyOneOfList":
        return typing.cast("AppUserSchemaPropertyOneOfList", jsii.get(self, "oneOf"))

    @builtins.property
    @jsii.member(jsii_name="appIdInput")
    def app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appIdInput"))

    @builtins.property
    @jsii.member(jsii_name="arrayEnumInput")
    def array_enum_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "arrayEnumInput"))

    @builtins.property
    @jsii.member(jsii_name="arrayOneOfInput")
    def array_one_of_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppUserSchemaPropertyArrayOneOf"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppUserSchemaPropertyArrayOneOf"]]], jsii.get(self, "arrayOneOfInput"))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppUserSchemaPropertyOneOf"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppUserSchemaPropertyOneOf"]]], jsii.get(self, "oneOfInput"))

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
    @jsii.member(jsii_name="unionInput")
    def union_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "unionInput"))

    @builtins.property
    @jsii.member(jsii_name="uniqueInput")
    def unique_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uniqueInput"))

    @builtins.property
    @jsii.member(jsii_name="userTypeInput")
    def user_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @app_id.setter
    def app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appId", value)

    @builtins.property
    @jsii.member(jsii_name="arrayEnum")
    def array_enum(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "arrayEnum"))

    @array_enum.setter
    def array_enum(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "array_enum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arrayEnum", value)

    @builtins.property
    @jsii.member(jsii_name="arrayType")
    def array_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arrayType"))

    @array_type.setter
    def array_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "array_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arrayType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="enum")
    def enum(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "enum"))

    @enum.setter
    def enum(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "enum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enum", value)

    @builtins.property
    @jsii.member(jsii_name="externalName")
    def external_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalName"))

    @external_name.setter
    def external_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "external_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalName", value)

    @builtins.property
    @jsii.member(jsii_name="externalNamespace")
    def external_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalNamespace"))

    @external_namespace.setter
    def external_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "external_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "index"))

    @index.setter
    def index(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "index").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="master")
    def master(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "master"))

    @master.setter
    def master(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "master").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "master", value)

    @builtins.property
    @jsii.member(jsii_name="maxLength")
    def max_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLength"))

    @max_length.setter
    def max_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "max_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLength", value)

    @builtins.property
    @jsii.member(jsii_name="minLength")
    def min_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minLength"))

    @min_length.setter
    def min_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "min_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLength", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "permissions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "required"))

    @required.setter
    def required(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "required", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="union")
    def union(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "union"))

    @union.setter
    def union(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "union").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "union", value)

    @builtins.property
    @jsii.member(jsii_name="unique")
    def unique(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unique"))

    @unique.setter
    def unique(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "unique").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unique", value)

    @builtins.property
    @jsii.member(jsii_name="userType")
    def user_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userType"))

    @user_type.setter
    def user_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaProperty, "user_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaPropertyArrayOneOf",
    jsii_struct_bases=[],
    name_mapping={"const": "const", "title": "title"},
)
class AppUserSchemaPropertyArrayOneOf:
    def __init__(self, *, const: builtins.str, title: builtins.str) -> None:
        '''
        :param const: Enum value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#const AppUserSchemaProperty#const}
        :param title: Enum title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#title AppUserSchemaProperty#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaPropertyArrayOneOf.__init__)
            check_type(argname="argument const", value=const, expected_type=type_hints["const"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "const": const,
            "title": title,
        }

    @builtins.property
    def const(self) -> builtins.str:
        '''Enum value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#const AppUserSchemaProperty#const}
        '''
        result = self._values.get("const")
        assert result is not None, "Required property 'const' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Enum title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#title AppUserSchemaProperty#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppUserSchemaPropertyArrayOneOf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppUserSchemaPropertyArrayOneOfList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaPropertyArrayOneOfList",
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
            type_hints = typing.get_type_hints(AppUserSchemaPropertyArrayOneOfList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppUserSchemaPropertyArrayOneOfOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaPropertyArrayOneOfList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppUserSchemaPropertyArrayOneOfOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyArrayOneOfList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyArrayOneOfList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyArrayOneOfList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyArrayOneOf]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyArrayOneOf]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyArrayOneOf]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyArrayOneOfList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppUserSchemaPropertyArrayOneOfOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaPropertyArrayOneOfOutputReference",
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
            type_hints = typing.get_type_hints(AppUserSchemaPropertyArrayOneOfOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyArrayOneOfOutputReference, "const").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "const", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyArrayOneOfOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppUserSchemaPropertyArrayOneOf, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppUserSchemaPropertyArrayOneOf, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppUserSchemaPropertyArrayOneOf, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyArrayOneOfOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaPropertyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "app_id": "appId",
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
        "max_length": "maxLength",
        "min_length": "minLength",
        "one_of": "oneOf",
        "permissions": "permissions",
        "required": "required",
        "scope": "scope",
        "union": "union",
        "unique": "unique",
        "user_type": "userType",
    },
)
class AppUserSchemaPropertyConfig(cdktf.TerraformMetaArguments):
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
        app_id: builtins.str,
        index: builtins.str,
        title: builtins.str,
        type: builtins.str,
        array_enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        array_one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppUserSchemaPropertyArrayOneOf, typing.Dict[str, typing.Any]]]]] = None,
        array_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        enum: typing.Optional[typing.Sequence[builtins.str]] = None,
        external_name: typing.Optional[builtins.str] = None,
        external_namespace: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        master: typing.Optional[builtins.str] = None,
        max_length: typing.Optional[jsii.Number] = None,
        min_length: typing.Optional[jsii.Number] = None,
        one_of: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppUserSchemaPropertyOneOf", typing.Dict[str, typing.Any]]]]] = None,
        permissions: typing.Optional[builtins.str] = None,
        required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        scope: typing.Optional[builtins.str] = None,
        union: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        unique: typing.Optional[builtins.str] = None,
        user_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param app_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#app_id AppUserSchemaProperty#app_id}.
        :param index: Subschema unique string identifier. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#index AppUserSchemaProperty#index}
        :param title: Subschema title (display name). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#title AppUserSchemaProperty#title}
        :param type: Subschema type: string, boolean, number, integer, array, or object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#type AppUserSchemaProperty#type}
        :param array_enum: Custom Subschema enumerated value of a property of type array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_enum AppUserSchemaProperty#array_enum}
        :param array_one_of: array_one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_one_of AppUserSchemaProperty#array_one_of}
        :param array_type: Subschema array type: string, number, integer, reference. Type field must be an array. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_type AppUserSchemaProperty#array_type}
        :param description: Custom Subschema description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#description AppUserSchemaProperty#description}
        :param enum: Custom Subschema enumerated value of the property. see: developer.okta.com/docs/api/resources/schemas#user-profile-schema-property-object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#enum AppUserSchemaProperty#enum}
        :param external_name: Subschema external name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#external_name AppUserSchemaProperty#external_name}
        :param external_namespace: Subschema external namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#external_namespace AppUserSchemaProperty#external_namespace}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#id AppUserSchemaProperty#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param master: SubSchema profile manager, if not set it will inherit its setting. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#master AppUserSchemaProperty#master}
        :param max_length: Subschema of type string maximum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#max_length AppUserSchemaProperty#max_length}
        :param min_length: Subschema of type string minimum length. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#min_length AppUserSchemaProperty#min_length}
        :param one_of: one_of block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#one_of AppUserSchemaProperty#one_of}
        :param permissions: SubSchema permissions: HIDE, READ_ONLY, or READ_WRITE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#permissions AppUserSchemaProperty#permissions}
        :param required: Whether the subschema is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#required AppUserSchemaProperty#required}
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#scope AppUserSchemaProperty#scope}.
        :param union: Allows to assign attribute's group priority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#union AppUserSchemaProperty#union}
        :param unique: Subschema unique restriction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#unique AppUserSchemaProperty#unique}
        :param user_type: Custom subschema user type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#user_type AppUserSchemaProperty#user_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaPropertyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
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
            check_type(argname="argument max_length", value=max_length, expected_type=type_hints["max_length"])
            check_type(argname="argument min_length", value=min_length, expected_type=type_hints["min_length"])
            check_type(argname="argument one_of", value=one_of, expected_type=type_hints["one_of"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument union", value=union, expected_type=type_hints["union"])
            check_type(argname="argument unique", value=unique, expected_type=type_hints["unique"])
            check_type(argname="argument user_type", value=user_type, expected_type=type_hints["user_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_id": app_id,
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
        if union is not None:
            self._values["union"] = union
        if unique is not None:
            self._values["unique"] = unique
        if user_type is not None:
            self._values["user_type"] = user_type

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
    def app_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#app_id AppUserSchemaProperty#app_id}.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index(self) -> builtins.str:
        '''Subschema unique string identifier.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#index AppUserSchemaProperty#index}
        '''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Subschema title (display name).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#title AppUserSchemaProperty#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Subschema type: string, boolean, number, integer, array, or object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#type AppUserSchemaProperty#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def array_enum(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Custom Subschema enumerated value of a property of type array.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_enum AppUserSchemaProperty#array_enum}
        '''
        result = self._values.get("array_enum")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def array_one_of(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyArrayOneOf]]]:
        '''array_one_of block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_one_of AppUserSchemaProperty#array_one_of}
        '''
        result = self._values.get("array_one_of")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyArrayOneOf]]], result)

    @builtins.property
    def array_type(self) -> typing.Optional[builtins.str]:
        '''Subschema array type: string, number, integer, reference. Type field must be an array.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#array_type AppUserSchemaProperty#array_type}
        '''
        result = self._values.get("array_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Custom Subschema description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#description AppUserSchemaProperty#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enum(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Custom Subschema enumerated value of the property. see: developer.okta.com/docs/api/resources/schemas#user-profile-schema-property-object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#enum AppUserSchemaProperty#enum}
        '''
        result = self._values.get("enum")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def external_name(self) -> typing.Optional[builtins.str]:
        '''Subschema external name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#external_name AppUserSchemaProperty#external_name}
        '''
        result = self._values.get("external_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_namespace(self) -> typing.Optional[builtins.str]:
        '''Subschema external namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#external_namespace AppUserSchemaProperty#external_namespace}
        '''
        result = self._values.get("external_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#id AppUserSchemaProperty#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def master(self) -> typing.Optional[builtins.str]:
        '''SubSchema profile manager, if not set it will inherit its setting.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#master AppUserSchemaProperty#master}
        '''
        result = self._values.get("master")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_length(self) -> typing.Optional[jsii.Number]:
        '''Subschema of type string maximum length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#max_length AppUserSchemaProperty#max_length}
        '''
        result = self._values.get("max_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_length(self) -> typing.Optional[jsii.Number]:
        '''Subschema of type string minimum length.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#min_length AppUserSchemaProperty#min_length}
        '''
        result = self._values.get("min_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def one_of(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppUserSchemaPropertyOneOf"]]]:
        '''one_of block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#one_of AppUserSchemaProperty#one_of}
        '''
        result = self._values.get("one_of")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppUserSchemaPropertyOneOf"]]], result)

    @builtins.property
    def permissions(self) -> typing.Optional[builtins.str]:
        '''SubSchema permissions: HIDE, READ_ONLY, or READ_WRITE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#permissions AppUserSchemaProperty#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the subschema is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#required AppUserSchemaProperty#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#scope AppUserSchemaProperty#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def union(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allows to assign attribute's group priority.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#union AppUserSchemaProperty#union}
        '''
        result = self._values.get("union")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def unique(self) -> typing.Optional[builtins.str]:
        '''Subschema unique restriction.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#unique AppUserSchemaProperty#unique}
        '''
        result = self._values.get("unique")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_type(self) -> typing.Optional[builtins.str]:
        '''Custom subschema user type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#user_type AppUserSchemaProperty#user_type}
        '''
        result = self._values.get("user_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppUserSchemaPropertyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaPropertyOneOf",
    jsii_struct_bases=[],
    name_mapping={"const": "const", "title": "title"},
)
class AppUserSchemaPropertyOneOf:
    def __init__(self, *, const: builtins.str, title: builtins.str) -> None:
        '''
        :param const: Enum value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#const AppUserSchemaProperty#const}
        :param title: Enum title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#title AppUserSchemaProperty#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaPropertyOneOf.__init__)
            check_type(argname="argument const", value=const, expected_type=type_hints["const"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "const": const,
            "title": title,
        }

    @builtins.property
    def const(self) -> builtins.str:
        '''Enum value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#const AppUserSchemaProperty#const}
        '''
        result = self._values.get("const")
        assert result is not None, "Required property 'const' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Enum title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/app_user_schema_property#title AppUserSchemaProperty#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppUserSchemaPropertyOneOf(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppUserSchemaPropertyOneOfList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaPropertyOneOfList",
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
            type_hints = typing.get_type_hints(AppUserSchemaPropertyOneOfList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppUserSchemaPropertyOneOfOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppUserSchemaPropertyOneOfList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppUserSchemaPropertyOneOfOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyOneOfList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyOneOfList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyOneOfList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyOneOf]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyOneOf]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppUserSchemaPropertyOneOf]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyOneOfList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppUserSchemaPropertyOneOfOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.appUserSchemaProperty.AppUserSchemaPropertyOneOfOutputReference",
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
            type_hints = typing.get_type_hints(AppUserSchemaPropertyOneOfOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyOneOfOutputReference, "const").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "const", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyOneOfOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppUserSchemaPropertyOneOf, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppUserSchemaPropertyOneOf, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppUserSchemaPropertyOneOf, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppUserSchemaPropertyOneOfOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "AppUserSchemaProperty",
    "AppUserSchemaPropertyArrayOneOf",
    "AppUserSchemaPropertyArrayOneOfList",
    "AppUserSchemaPropertyArrayOneOfOutputReference",
    "AppUserSchemaPropertyConfig",
    "AppUserSchemaPropertyOneOf",
    "AppUserSchemaPropertyOneOfList",
    "AppUserSchemaPropertyOneOfOutputReference",
]

publication.publish()
