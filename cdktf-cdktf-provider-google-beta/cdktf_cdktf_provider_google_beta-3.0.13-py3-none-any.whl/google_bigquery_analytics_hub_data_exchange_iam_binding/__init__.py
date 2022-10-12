'''
# `google_bigquery_analytics_hub_data_exchange_iam_binding`

Refer to the Terraform Registory for docs: [`google_bigquery_analytics_hub_data_exchange_iam_binding`](https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding).
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


class GoogleBigqueryAnalyticsHubDataExchangeIamBinding(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryAnalyticsHubDataExchangeIamBinding.GoogleBigqueryAnalyticsHubDataExchangeIamBinding",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding google_bigquery_analytics_hub_data_exchange_iam_binding}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_exchange_id: builtins.str,
        members: typing.Sequence[builtins.str],
        role: builtins.str,
        condition: typing.Optional[typing.Union["GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding google_bigquery_analytics_hub_data_exchange_iam_binding} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_exchange_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#data_exchange_id GoogleBigqueryAnalyticsHubDataExchangeIamBinding#data_exchange_id}.
        :param members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#members GoogleBigqueryAnalyticsHubDataExchangeIamBinding#members}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#role GoogleBigqueryAnalyticsHubDataExchangeIamBinding#role}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#condition GoogleBigqueryAnalyticsHubDataExchangeIamBinding#condition}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#id GoogleBigqueryAnalyticsHubDataExchangeIamBinding#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#location GoogleBigqueryAnalyticsHubDataExchangeIamBinding#location}.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#project GoogleBigqueryAnalyticsHubDataExchangeIamBinding#project}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryAnalyticsHubDataExchangeIamBinding.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigqueryAnalyticsHubDataExchangeIamBindingConfig(
            data_exchange_id=data_exchange_id,
            members=members,
            role=role,
            condition=condition,
            id=id,
            location=location,
            project=project,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#expression GoogleBigqueryAnalyticsHubDataExchangeIamBinding#expression}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#title GoogleBigqueryAnalyticsHubDataExchangeIamBinding#title}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#description GoogleBigqueryAnalyticsHubDataExchangeIamBinding#description}.
        '''
        value = GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition(
            expression=expression, title=title, description=description
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(
        self,
    ) -> "GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference":
        return typing.cast("GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional["GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition"]:
        return typing.cast(typing.Optional["GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition"], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="dataExchangeIdInput")
    def data_exchange_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataExchangeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="membersInput")
    def members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "membersInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="dataExchangeId")
    def data_exchange_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataExchangeId"))

    @data_exchange_id.setter
    def data_exchange_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBinding, "data_exchange_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataExchangeId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBinding, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBinding, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "members"))

    @members.setter
    def members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBinding, "members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBinding, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBinding, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryAnalyticsHubDataExchangeIamBinding.GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "title": "title",
        "description": "description",
    },
)
class GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition:
    def __init__(
        self,
        *,
        expression: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#expression GoogleBigqueryAnalyticsHubDataExchangeIamBinding#expression}.
        :param title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#title GoogleBigqueryAnalyticsHubDataExchangeIamBinding#title}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#description GoogleBigqueryAnalyticsHubDataExchangeIamBinding#description}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
            "title": title,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def expression(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#expression GoogleBigqueryAnalyticsHubDataExchangeIamBinding#expression}.'''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#title GoogleBigqueryAnalyticsHubDataExchangeIamBinding#title}.'''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#description GoogleBigqueryAnalyticsHubDataExchangeIamBinding#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryAnalyticsHubDataExchangeIamBinding.GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition]:
        return typing.cast(typing.Optional[GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryAnalyticsHubDataExchangeIamBinding.GoogleBigqueryAnalyticsHubDataExchangeIamBindingConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_exchange_id": "dataExchangeId",
        "members": "members",
        "role": "role",
        "condition": "condition",
        "id": "id",
        "location": "location",
        "project": "project",
    },
)
class GoogleBigqueryAnalyticsHubDataExchangeIamBindingConfig(
    cdktf.TerraformMetaArguments,
):
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
        data_exchange_id: builtins.str,
        members: typing.Sequence[builtins.str],
        role: builtins.str,
        condition: typing.Optional[typing.Union[GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition, typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_exchange_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#data_exchange_id GoogleBigqueryAnalyticsHubDataExchangeIamBinding#data_exchange_id}.
        :param members: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#members GoogleBigqueryAnalyticsHubDataExchangeIamBinding#members}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#role GoogleBigqueryAnalyticsHubDataExchangeIamBinding#role}.
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#condition GoogleBigqueryAnalyticsHubDataExchangeIamBinding#condition}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#id GoogleBigqueryAnalyticsHubDataExchangeIamBinding#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#location GoogleBigqueryAnalyticsHubDataExchangeIamBinding#location}.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#project GoogleBigqueryAnalyticsHubDataExchangeIamBinding#project}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(condition, dict):
            condition = GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryAnalyticsHubDataExchangeIamBindingConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_exchange_id", value=data_exchange_id, expected_type=type_hints["data_exchange_id"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_exchange_id": data_exchange_id,
            "members": members,
            "role": role,
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
        if condition is not None:
            self._values["condition"] = condition
        if id is not None:
            self._values["id"] = id
        if location is not None:
            self._values["location"] = location
        if project is not None:
            self._values["project"] = project

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
    def data_exchange_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#data_exchange_id GoogleBigqueryAnalyticsHubDataExchangeIamBinding#data_exchange_id}.'''
        result = self._values.get("data_exchange_id")
        assert result is not None, "Required property 'data_exchange_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def members(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#members GoogleBigqueryAnalyticsHubDataExchangeIamBinding#members}.'''
        result = self._values.get("members")
        assert result is not None, "Required property 'members' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#role GoogleBigqueryAnalyticsHubDataExchangeIamBinding#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def condition(
        self,
    ) -> typing.Optional[GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#condition GoogleBigqueryAnalyticsHubDataExchangeIamBinding#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#id GoogleBigqueryAnalyticsHubDataExchangeIamBinding#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#location GoogleBigqueryAnalyticsHubDataExchangeIamBinding#location}.'''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_analytics_hub_data_exchange_iam_binding#project GoogleBigqueryAnalyticsHubDataExchangeIamBinding#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryAnalyticsHubDataExchangeIamBindingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GoogleBigqueryAnalyticsHubDataExchangeIamBinding",
    "GoogleBigqueryAnalyticsHubDataExchangeIamBindingCondition",
    "GoogleBigqueryAnalyticsHubDataExchangeIamBindingConditionOutputReference",
    "GoogleBigqueryAnalyticsHubDataExchangeIamBindingConfig",
]

publication.publish()
