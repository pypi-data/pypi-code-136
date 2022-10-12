'''
# `datadog_synthetics_global_variable`

Refer to the Terraform Registory for docs: [`datadog_synthetics_global_variable`](https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable).
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


class SyntheticsGlobalVariable(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsGlobalVariable.SyntheticsGlobalVariable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable datadog_synthetics_global_variable}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        value: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parse_test_id: typing.Optional[builtins.str] = None,
        parse_test_options: typing.Optional[typing.Union["SyntheticsGlobalVariableParseTestOptions", typing.Dict[str, typing.Any]]] = None,
        restricted_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        secure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable datadog_synthetics_global_variable} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Synthetics global variable name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#name SyntheticsGlobalVariable#name}
        :param value: The value of the global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#value SyntheticsGlobalVariable#value}
        :param description: Description of the global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#description SyntheticsGlobalVariable#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#id SyntheticsGlobalVariable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parse_test_id: Id of the Synthetics test to use for a variable from test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parse_test_id SyntheticsGlobalVariable#parse_test_id}
        :param parse_test_options: parse_test_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parse_test_options SyntheticsGlobalVariable#parse_test_options}
        :param restricted_roles: A list of role identifiers to associate with the Synthetics global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#restricted_roles SyntheticsGlobalVariable#restricted_roles}
        :param secure: If set to true, the value of the global variable is hidden. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#secure SyntheticsGlobalVariable#secure}
        :param tags: A list of tags to associate with your synthetics global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#tags SyntheticsGlobalVariable#tags}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsGlobalVariable.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SyntheticsGlobalVariableConfig(
            name=name,
            value=value,
            description=description,
            id=id,
            parse_test_id=parse_test_id,
            parse_test_options=parse_test_options,
            restricted_roles=restricted_roles,
            secure=secure,
            tags=tags,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putParseTestOptions")
    def put_parse_test_options(
        self,
        *,
        type: builtins.str,
        field: typing.Optional[builtins.str] = None,
        local_variable_name: typing.Optional[builtins.str] = None,
        parser: typing.Optional[typing.Union["SyntheticsGlobalVariableParseTestOptionsParser", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Defines the source to use to extract the value. Valid values are ``http_body``, ``http_header``, ``local_variable``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#type SyntheticsGlobalVariable#type}
        :param field: Required when type = ``http_header``. Defines the header to use to extract the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#field SyntheticsGlobalVariable#field}
        :param local_variable_name: When type is ``local_variable``, name of the local variable to use to extract the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#local_variable_name SyntheticsGlobalVariable#local_variable_name}
        :param parser: parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parser SyntheticsGlobalVariable#parser}
        '''
        value = SyntheticsGlobalVariableParseTestOptions(
            type=type,
            field=field,
            local_variable_name=local_variable_name,
            parser=parser,
        )

        return typing.cast(None, jsii.invoke(self, "putParseTestOptions", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParseTestId")
    def reset_parse_test_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParseTestId", []))

    @jsii.member(jsii_name="resetParseTestOptions")
    def reset_parse_test_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParseTestOptions", []))

    @jsii.member(jsii_name="resetRestrictedRoles")
    def reset_restricted_roles(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictedRoles", []))

    @jsii.member(jsii_name="resetSecure")
    def reset_secure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecure", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="parseTestOptions")
    def parse_test_options(
        self,
    ) -> "SyntheticsGlobalVariableParseTestOptionsOutputReference":
        return typing.cast("SyntheticsGlobalVariableParseTestOptionsOutputReference", jsii.get(self, "parseTestOptions"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parseTestIdInput")
    def parse_test_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parseTestIdInput"))

    @builtins.property
    @jsii.member(jsii_name="parseTestOptionsInput")
    def parse_test_options_input(
        self,
    ) -> typing.Optional["SyntheticsGlobalVariableParseTestOptions"]:
        return typing.cast(typing.Optional["SyntheticsGlobalVariableParseTestOptions"], jsii.get(self, "parseTestOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictedRolesInput")
    def restricted_roles_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "restrictedRolesInput"))

    @builtins.property
    @jsii.member(jsii_name="secureInput")
    def secure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "secureInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parseTestId")
    def parse_test_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parseTestId"))

    @parse_test_id.setter
    def parse_test_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "parse_test_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parseTestId", value)

    @builtins.property
    @jsii.member(jsii_name="restrictedRoles")
    def restricted_roles(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "restrictedRoles"))

    @restricted_roles.setter
    def restricted_roles(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "restricted_roles").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictedRoles", value)

    @builtins.property
    @jsii.member(jsii_name="secure")
    def secure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "secure"))

    @secure.setter
    def secure(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "secure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secure", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariable, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsGlobalVariable.SyntheticsGlobalVariableConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "value": "value",
        "description": "description",
        "id": "id",
        "parse_test_id": "parseTestId",
        "parse_test_options": "parseTestOptions",
        "restricted_roles": "restrictedRoles",
        "secure": "secure",
        "tags": "tags",
    },
)
class SyntheticsGlobalVariableConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        value: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parse_test_id: typing.Optional[builtins.str] = None,
        parse_test_options: typing.Optional[typing.Union["SyntheticsGlobalVariableParseTestOptions", typing.Dict[str, typing.Any]]] = None,
        restricted_roles: typing.Optional[typing.Sequence[builtins.str]] = None,
        secure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Synthetics global variable name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#name SyntheticsGlobalVariable#name}
        :param value: The value of the global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#value SyntheticsGlobalVariable#value}
        :param description: Description of the global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#description SyntheticsGlobalVariable#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#id SyntheticsGlobalVariable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parse_test_id: Id of the Synthetics test to use for a variable from test. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parse_test_id SyntheticsGlobalVariable#parse_test_id}
        :param parse_test_options: parse_test_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parse_test_options SyntheticsGlobalVariable#parse_test_options}
        :param restricted_roles: A list of role identifiers to associate with the Synthetics global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#restricted_roles SyntheticsGlobalVariable#restricted_roles}
        :param secure: If set to true, the value of the global variable is hidden. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#secure SyntheticsGlobalVariable#secure}
        :param tags: A list of tags to associate with your synthetics global variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#tags SyntheticsGlobalVariable#tags}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(parse_test_options, dict):
            parse_test_options = SyntheticsGlobalVariableParseTestOptions(**parse_test_options)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsGlobalVariableConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parse_test_id", value=parse_test_id, expected_type=type_hints["parse_test_id"])
            check_type(argname="argument parse_test_options", value=parse_test_options, expected_type=type_hints["parse_test_options"])
            check_type(argname="argument restricted_roles", value=restricted_roles, expected_type=type_hints["restricted_roles"])
            check_type(argname="argument secure", value=secure, expected_type=type_hints["secure"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if parse_test_id is not None:
            self._values["parse_test_id"] = parse_test_id
        if parse_test_options is not None:
            self._values["parse_test_options"] = parse_test_options
        if restricted_roles is not None:
            self._values["restricted_roles"] = restricted_roles
        if secure is not None:
            self._values["secure"] = secure
        if tags is not None:
            self._values["tags"] = tags

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
    def name(self) -> builtins.str:
        '''Synthetics global variable name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#name SyntheticsGlobalVariable#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the global variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#value SyntheticsGlobalVariable#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the global variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#description SyntheticsGlobalVariable#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#id SyntheticsGlobalVariable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parse_test_id(self) -> typing.Optional[builtins.str]:
        '''Id of the Synthetics test to use for a variable from test.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parse_test_id SyntheticsGlobalVariable#parse_test_id}
        '''
        result = self._values.get("parse_test_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parse_test_options(
        self,
    ) -> typing.Optional["SyntheticsGlobalVariableParseTestOptions"]:
        '''parse_test_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parse_test_options SyntheticsGlobalVariable#parse_test_options}
        '''
        result = self._values.get("parse_test_options")
        return typing.cast(typing.Optional["SyntheticsGlobalVariableParseTestOptions"], result)

    @builtins.property
    def restricted_roles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of role identifiers to associate with the Synthetics global variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#restricted_roles SyntheticsGlobalVariable#restricted_roles}
        '''
        result = self._values.get("restricted_roles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def secure(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the value of the global variable is hidden. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#secure SyntheticsGlobalVariable#secure}
        '''
        result = self._values.get("secure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tags to associate with your synthetics global variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#tags SyntheticsGlobalVariable#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsGlobalVariableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsGlobalVariable.SyntheticsGlobalVariableParseTestOptions",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "field": "field",
        "local_variable_name": "localVariableName",
        "parser": "parser",
    },
)
class SyntheticsGlobalVariableParseTestOptions:
    def __init__(
        self,
        *,
        type: builtins.str,
        field: typing.Optional[builtins.str] = None,
        local_variable_name: typing.Optional[builtins.str] = None,
        parser: typing.Optional[typing.Union["SyntheticsGlobalVariableParseTestOptionsParser", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Defines the source to use to extract the value. Valid values are ``http_body``, ``http_header``, ``local_variable``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#type SyntheticsGlobalVariable#type}
        :param field: Required when type = ``http_header``. Defines the header to use to extract the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#field SyntheticsGlobalVariable#field}
        :param local_variable_name: When type is ``local_variable``, name of the local variable to use to extract the value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#local_variable_name SyntheticsGlobalVariable#local_variable_name}
        :param parser: parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parser SyntheticsGlobalVariable#parser}
        '''
        if isinstance(parser, dict):
            parser = SyntheticsGlobalVariableParseTestOptionsParser(**parser)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsGlobalVariableParseTestOptions.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument local_variable_name", value=local_variable_name, expected_type=type_hints["local_variable_name"])
            check_type(argname="argument parser", value=parser, expected_type=type_hints["parser"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if field is not None:
            self._values["field"] = field
        if local_variable_name is not None:
            self._values["local_variable_name"] = local_variable_name
        if parser is not None:
            self._values["parser"] = parser

    @builtins.property
    def type(self) -> builtins.str:
        '''Defines the source to use to extract the value. Valid values are ``http_body``, ``http_header``, ``local_variable``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#type SyntheticsGlobalVariable#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''Required when type = ``http_header``. Defines the header to use to extract the value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#field SyntheticsGlobalVariable#field}
        '''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def local_variable_name(self) -> typing.Optional[builtins.str]:
        '''When type is ``local_variable``, name of the local variable to use to extract the value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#local_variable_name SyntheticsGlobalVariable#local_variable_name}
        '''
        result = self._values.get("local_variable_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parser(
        self,
    ) -> typing.Optional["SyntheticsGlobalVariableParseTestOptionsParser"]:
        '''parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#parser SyntheticsGlobalVariable#parser}
        '''
        result = self._values.get("parser")
        return typing.cast(typing.Optional["SyntheticsGlobalVariableParseTestOptionsParser"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsGlobalVariableParseTestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsGlobalVariableParseTestOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsGlobalVariable.SyntheticsGlobalVariableParseTestOptionsOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsGlobalVariableParseTestOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putParser")
    def put_parser(
        self,
        *,
        type: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of parser to extract the value. Valid values are ``raw``, ``json_path``, ``regex``, ``x_path``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#type SyntheticsGlobalVariable#type}
        :param value: Value for the parser to use, required for type ``json_path`` or ``regex``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#value SyntheticsGlobalVariable#value}
        '''
        value_ = SyntheticsGlobalVariableParseTestOptionsParser(type=type, value=value)

        return typing.cast(None, jsii.invoke(self, "putParser", [value_]))

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @jsii.member(jsii_name="resetLocalVariableName")
    def reset_local_variable_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocalVariableName", []))

    @jsii.member(jsii_name="resetParser")
    def reset_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParser", []))

    @builtins.property
    @jsii.member(jsii_name="parser")
    def parser(self) -> "SyntheticsGlobalVariableParseTestOptionsParserOutputReference":
        return typing.cast("SyntheticsGlobalVariableParseTestOptionsParserOutputReference", jsii.get(self, "parser"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="localVariableNameInput")
    def local_variable_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "localVariableNameInput"))

    @builtins.property
    @jsii.member(jsii_name="parserInput")
    def parser_input(
        self,
    ) -> typing.Optional["SyntheticsGlobalVariableParseTestOptionsParser"]:
        return typing.cast(typing.Optional["SyntheticsGlobalVariableParseTestOptionsParser"], jsii.get(self, "parserInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariableParseTestOptionsOutputReference, "field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="localVariableName")
    def local_variable_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "localVariableName"))

    @local_variable_name.setter
    def local_variable_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariableParseTestOptionsOutputReference, "local_variable_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localVariableName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariableParseTestOptionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsGlobalVariableParseTestOptions]:
        return typing.cast(typing.Optional[SyntheticsGlobalVariableParseTestOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsGlobalVariableParseTestOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariableParseTestOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-datadog.syntheticsGlobalVariable.SyntheticsGlobalVariableParseTestOptionsParser",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class SyntheticsGlobalVariableParseTestOptionsParser:
    def __init__(
        self,
        *,
        type: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: Type of parser to extract the value. Valid values are ``raw``, ``json_path``, ``regex``, ``x_path``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#type SyntheticsGlobalVariable#type}
        :param value: Value for the parser to use, required for type ``json_path`` or ``regex``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#value SyntheticsGlobalVariable#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsGlobalVariableParseTestOptionsParser.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of parser to extract the value. Valid values are ``raw``, ``json_path``, ``regex``, ``x_path``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#type SyntheticsGlobalVariable#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Value for the parser to use, required for type ``json_path`` or ``regex``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/datadog/r/synthetics_global_variable#value SyntheticsGlobalVariable#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsGlobalVariableParseTestOptionsParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticsGlobalVariableParseTestOptionsParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-datadog.syntheticsGlobalVariable.SyntheticsGlobalVariableParseTestOptionsParserOutputReference",
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
            type_hints = typing.get_type_hints(SyntheticsGlobalVariableParseTestOptionsParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

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
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariableParseTestOptionsParserOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariableParseTestOptionsParserOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticsGlobalVariableParseTestOptionsParser]:
        return typing.cast(typing.Optional[SyntheticsGlobalVariableParseTestOptionsParser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticsGlobalVariableParseTestOptionsParser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsGlobalVariableParseTestOptionsParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SyntheticsGlobalVariable",
    "SyntheticsGlobalVariableConfig",
    "SyntheticsGlobalVariableParseTestOptions",
    "SyntheticsGlobalVariableParseTestOptionsOutputReference",
    "SyntheticsGlobalVariableParseTestOptionsParser",
    "SyntheticsGlobalVariableParseTestOptionsParserOutputReference",
]

publication.publish()
