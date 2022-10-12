'''
# `data_google_iam_testable_permissions`

Refer to the Terraform Registory for docs: [`data_google_iam_testable_permissions`](https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions).
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


class DataGoogleIamTestablePermissions(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamTestablePermissions.DataGoogleIamTestablePermissions",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions google_iam_testable_permissions}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        full_resource_name: builtins.str,
        custom_support_level: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        stages: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions google_iam_testable_permissions} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param full_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#full_resource_name DataGoogleIamTestablePermissions#full_resource_name}.
        :param custom_support_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#custom_support_level DataGoogleIamTestablePermissions#custom_support_level}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#id DataGoogleIamTestablePermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param stages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#stages DataGoogleIamTestablePermissions#stages}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamTestablePermissions.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGoogleIamTestablePermissionsConfig(
            full_resource_name=full_resource_name,
            custom_support_level=custom_support_level,
            id=id,
            stages=stages,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCustomSupportLevel")
    def reset_custom_support_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSupportLevel", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStages")
    def reset_stages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStages", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> "DataGoogleIamTestablePermissionsPermissionsList":
        return typing.cast("DataGoogleIamTestablePermissionsPermissionsList", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="customSupportLevelInput")
    def custom_support_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customSupportLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="fullResourceNameInput")
    def full_resource_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fullResourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="stagesInput")
    def stages_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stagesInput"))

    @builtins.property
    @jsii.member(jsii_name="customSupportLevel")
    def custom_support_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customSupportLevel"))

    @custom_support_level.setter
    def custom_support_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissions, "custom_support_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customSupportLevel", value)

    @builtins.property
    @jsii.member(jsii_name="fullResourceName")
    def full_resource_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullResourceName"))

    @full_resource_name.setter
    def full_resource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissions, "full_resource_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullResourceName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissions, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="stages")
    def stages(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stages"))

    @stages.setter
    def stages(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissions, "stages").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stages", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamTestablePermissions.DataGoogleIamTestablePermissionsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "full_resource_name": "fullResourceName",
        "custom_support_level": "customSupportLevel",
        "id": "id",
        "stages": "stages",
    },
)
class DataGoogleIamTestablePermissionsConfig(cdktf.TerraformMetaArguments):
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
        full_resource_name: builtins.str,
        custom_support_level: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        stages: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param full_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#full_resource_name DataGoogleIamTestablePermissions#full_resource_name}.
        :param custom_support_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#custom_support_level DataGoogleIamTestablePermissions#custom_support_level}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#id DataGoogleIamTestablePermissions#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param stages: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#stages DataGoogleIamTestablePermissions#stages}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamTestablePermissionsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument full_resource_name", value=full_resource_name, expected_type=type_hints["full_resource_name"])
            check_type(argname="argument custom_support_level", value=custom_support_level, expected_type=type_hints["custom_support_level"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument stages", value=stages, expected_type=type_hints["stages"])
        self._values: typing.Dict[str, typing.Any] = {
            "full_resource_name": full_resource_name,
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
        if custom_support_level is not None:
            self._values["custom_support_level"] = custom_support_level
        if id is not None:
            self._values["id"] = id
        if stages is not None:
            self._values["stages"] = stages

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
    def full_resource_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#full_resource_name DataGoogleIamTestablePermissions#full_resource_name}.'''
        result = self._values.get("full_resource_name")
        assert result is not None, "Required property 'full_resource_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_support_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#custom_support_level DataGoogleIamTestablePermissions#custom_support_level}.'''
        result = self._values.get("custom_support_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#id DataGoogleIamTestablePermissions#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stages(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/d/google_iam_testable_permissions#stages DataGoogleIamTestablePermissions#stages}.'''
        result = self._values.get("stages")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleIamTestablePermissionsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamTestablePermissions.DataGoogleIamTestablePermissionsPermissions",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGoogleIamTestablePermissionsPermissions:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGoogleIamTestablePermissionsPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGoogleIamTestablePermissionsPermissionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamTestablePermissions.DataGoogleIamTestablePermissionsPermissionsList",
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
            type_hints = typing.get_type_hints(DataGoogleIamTestablePermissionsPermissionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGoogleIamTestablePermissionsPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGoogleIamTestablePermissionsPermissionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGoogleIamTestablePermissionsPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissionsPermissionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissionsPermissionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissionsPermissionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGoogleIamTestablePermissionsPermissionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.dataGoogleIamTestablePermissions.DataGoogleIamTestablePermissionsPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(DataGoogleIamTestablePermissionsPermissionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="apiDisabled")
    def api_disabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "apiDisabled"))

    @builtins.property
    @jsii.member(jsii_name="customSupportLevel")
    def custom_support_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customSupportLevel"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stage"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGoogleIamTestablePermissionsPermissions]:
        return typing.cast(typing.Optional[DataGoogleIamTestablePermissionsPermissions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGoogleIamTestablePermissionsPermissions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGoogleIamTestablePermissionsPermissionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGoogleIamTestablePermissions",
    "DataGoogleIamTestablePermissionsConfig",
    "DataGoogleIamTestablePermissionsPermissions",
    "DataGoogleIamTestablePermissionsPermissionsList",
    "DataGoogleIamTestablePermissionsPermissionsOutputReference",
]

publication.publish()
