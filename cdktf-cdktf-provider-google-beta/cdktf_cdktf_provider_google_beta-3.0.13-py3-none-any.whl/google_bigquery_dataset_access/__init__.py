'''
# `google_bigquery_dataset_access`

Refer to the Terraform Registory for docs: [`google_bigquery_dataset_access`](https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access).
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


class GoogleBigqueryDatasetAccessA(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessA",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access google_bigquery_dataset_access}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dataset_id: builtins.str,
        dataset: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessDatasetA", typing.Dict[str, typing.Any]]] = None,
        domain: typing.Optional[builtins.str] = None,
        group_by_email: typing.Optional[builtins.str] = None,
        iam_member: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        special_group: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_by_email: typing.Optional[builtins.str] = None,
        view: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessViewA", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access google_bigquery_dataset_access} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataset_id: A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset GoogleBigqueryDatasetAccessA#dataset}
        :param domain: A domain to grant access to. Any users signed in with the domain specified will be granted the specified access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#domain GoogleBigqueryDatasetAccessA#domain}
        :param group_by_email: An email address of a Google Group to grant access to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#group_by_email GoogleBigqueryDatasetAccessA#group_by_email}
        :param iam_member: Some other type of member that appears in the IAM Policy but isn't a user, group, domain, or special group. For example: 'allUsers' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#iam_member GoogleBigqueryDatasetAccessA#iam_member}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#id GoogleBigqueryDatasetAccessA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project GoogleBigqueryDatasetAccessA#project}.
        :param role: Describes the rights granted to the user specified by the other member of the access object. Basic, predefined, and custom roles are supported. Predefined roles that have equivalent basic roles are swapped by the API to their basic counterparts, and will show a diff post-create. See `official docs <https://cloud.google.com/bigquery/docs/access-control>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#role GoogleBigqueryDatasetAccessA#role}
        :param special_group: A special group to grant access to. Possible values include:. 'projectOwners': Owners of the enclosing project. 'projectReaders': Readers of the enclosing project. 'projectWriters': Writers of the enclosing project. 'allAuthenticatedUsers': All authenticated BigQuery users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#special_group GoogleBigqueryDatasetAccessA#special_group}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#timeouts GoogleBigqueryDatasetAccessA#timeouts}
        :param user_by_email: An email address of a user to grant access to. For example: fred@example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#user_by_email GoogleBigqueryDatasetAccessA#user_by_email}
        :param view: view block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#view GoogleBigqueryDatasetAccessA#view}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessA.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigqueryDatasetAccessAConfig(
            dataset_id=dataset_id,
            dataset=dataset,
            domain=domain,
            group_by_email=group_by_email,
            iam_member=iam_member,
            id=id,
            project=project,
            role=role,
            special_group=special_group,
            timeouts=timeouts,
            user_by_email=user_by_email,
            view=view,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDataset")
    def put_dataset(
        self,
        *,
        dataset: typing.Union["GoogleBigqueryDatasetAccessDatasetDatasetA", typing.Dict[str, typing.Any]],
        target_types: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset GoogleBigqueryDatasetAccessA#dataset}
        :param target_types: Which resources in the dataset this entry applies to. Currently, only views are supported, but additional target types may be added in the future. Possible values: VIEWS Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#target_types GoogleBigqueryDatasetAccessA#target_types}
        '''
        value = GoogleBigqueryDatasetAccessDatasetA(
            dataset=dataset, target_types=target_types
        )

        return typing.cast(None, jsii.invoke(self, "putDataset", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#create GoogleBigqueryDatasetAccessA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#delete GoogleBigqueryDatasetAccessA#delete}.
        '''
        value = GoogleBigqueryDatasetAccessTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putView")
    def put_view(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project_id GoogleBigqueryDatasetAccessA#project_id}
        :param table_id: The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#table_id GoogleBigqueryDatasetAccessA#table_id}
        '''
        value = GoogleBigqueryDatasetAccessViewA(
            dataset_id=dataset_id, project_id=project_id, table_id=table_id
        )

        return typing.cast(None, jsii.invoke(self, "putView", [value]))

    @jsii.member(jsii_name="resetDataset")
    def reset_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataset", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetGroupByEmail")
    def reset_group_by_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupByEmail", []))

    @jsii.member(jsii_name="resetIamMember")
    def reset_iam_member(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamMember", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetSpecialGroup")
    def reset_special_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpecialGroup", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserByEmail")
    def reset_user_by_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserByEmail", []))

    @jsii.member(jsii_name="resetView")
    def reset_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetView", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="apiUpdatedMember")
    def api_updated_member(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "apiUpdatedMember"))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> "GoogleBigqueryDatasetAccessDatasetAOutputReference":
        return typing.cast("GoogleBigqueryDatasetAccessDatasetAOutputReference", jsii.get(self, "dataset"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleBigqueryDatasetAccessTimeoutsOutputReference":
        return typing.cast("GoogleBigqueryDatasetAccessTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="view")
    def view(self) -> "GoogleBigqueryDatasetAccessViewAOutputReference":
        return typing.cast("GoogleBigqueryDatasetAccessViewAOutputReference", jsii.get(self, "view"))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(self) -> typing.Optional["GoogleBigqueryDatasetAccessDatasetA"]:
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessDatasetA"], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByEmailInput")
    def group_by_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupByEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="iamMemberInput")
    def iam_member_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamMemberInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="specialGroupInput")
    def special_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "specialGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleBigqueryDatasetAccessTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleBigqueryDatasetAccessTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userByEmailInput")
    def user_by_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userByEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="viewInput")
    def view_input(self) -> typing.Optional["GoogleBigqueryDatasetAccessViewA"]:
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessViewA"], jsii.get(self, "viewInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="groupByEmail")
    def group_by_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupByEmail"))

    @group_by_email.setter
    def group_by_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "group_by_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByEmail", value)

    @builtins.property
    @jsii.member(jsii_name="iamMember")
    def iam_member(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamMember"))

    @iam_member.setter
    def iam_member(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "iam_member").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamMember", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="specialGroup")
    def special_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "specialGroup"))

    @special_group.setter
    def special_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "special_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "specialGroup", value)

    @builtins.property
    @jsii.member(jsii_name="userByEmail")
    def user_by_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userByEmail"))

    @user_by_email.setter
    def user_by_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessA, "user_by_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userByEmail", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessAConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataset_id": "datasetId",
        "dataset": "dataset",
        "domain": "domain",
        "group_by_email": "groupByEmail",
        "iam_member": "iamMember",
        "id": "id",
        "project": "project",
        "role": "role",
        "special_group": "specialGroup",
        "timeouts": "timeouts",
        "user_by_email": "userByEmail",
        "view": "view",
    },
)
class GoogleBigqueryDatasetAccessAConfig(cdktf.TerraformMetaArguments):
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
        dataset_id: builtins.str,
        dataset: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessDatasetA", typing.Dict[str, typing.Any]]] = None,
        domain: typing.Optional[builtins.str] = None,
        group_by_email: typing.Optional[builtins.str] = None,
        iam_member: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        special_group: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_by_email: typing.Optional[builtins.str] = None,
        view: typing.Optional[typing.Union["GoogleBigqueryDatasetAccessViewA", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataset_id: A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset GoogleBigqueryDatasetAccessA#dataset}
        :param domain: A domain to grant access to. Any users signed in with the domain specified will be granted the specified access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#domain GoogleBigqueryDatasetAccessA#domain}
        :param group_by_email: An email address of a Google Group to grant access to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#group_by_email GoogleBigqueryDatasetAccessA#group_by_email}
        :param iam_member: Some other type of member that appears in the IAM Policy but isn't a user, group, domain, or special group. For example: 'allUsers' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#iam_member GoogleBigqueryDatasetAccessA#iam_member}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#id GoogleBigqueryDatasetAccessA#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project GoogleBigqueryDatasetAccessA#project}.
        :param role: Describes the rights granted to the user specified by the other member of the access object. Basic, predefined, and custom roles are supported. Predefined roles that have equivalent basic roles are swapped by the API to their basic counterparts, and will show a diff post-create. See `official docs <https://cloud.google.com/bigquery/docs/access-control>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#role GoogleBigqueryDatasetAccessA#role}
        :param special_group: A special group to grant access to. Possible values include:. 'projectOwners': Owners of the enclosing project. 'projectReaders': Readers of the enclosing project. 'projectWriters': Writers of the enclosing project. 'allAuthenticatedUsers': All authenticated BigQuery users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#special_group GoogleBigqueryDatasetAccessA#special_group}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#timeouts GoogleBigqueryDatasetAccessA#timeouts}
        :param user_by_email: An email address of a user to grant access to. For example: fred@example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#user_by_email GoogleBigqueryDatasetAccessA#user_by_email}
        :param view: view block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#view GoogleBigqueryDatasetAccessA#view}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dataset, dict):
            dataset = GoogleBigqueryDatasetAccessDatasetA(**dataset)
        if isinstance(timeouts, dict):
            timeouts = GoogleBigqueryDatasetAccessTimeouts(**timeouts)
        if isinstance(view, dict):
            view = GoogleBigqueryDatasetAccessViewA(**view)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessAConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument group_by_email", value=group_by_email, expected_type=type_hints["group_by_email"])
            check_type(argname="argument iam_member", value=iam_member, expected_type=type_hints["iam_member"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument special_group", value=special_group, expected_type=type_hints["special_group"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_by_email", value=user_by_email, expected_type=type_hints["user_by_email"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
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
        if dataset is not None:
            self._values["dataset"] = dataset
        if domain is not None:
            self._values["domain"] = domain
        if group_by_email is not None:
            self._values["group_by_email"] = group_by_email
        if iam_member is not None:
            self._values["iam_member"] = iam_member
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if role is not None:
            self._values["role"] = role
        if special_group is not None:
            self._values["special_group"] = special_group
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_by_email is not None:
            self._values["user_by_email"] = user_by_email
        if view is not None:
            self._values["view"] = view

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
    def dataset_id(self) -> builtins.str:
        '''A unique ID for this dataset, without the project name.

        The ID
        must contain only letters (a-z, A-Z), numbers (0-9), or
        underscores (_). The maximum length is 1,024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset(self) -> typing.Optional["GoogleBigqueryDatasetAccessDatasetA"]:
        '''dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset GoogleBigqueryDatasetAccessA#dataset}
        '''
        result = self._values.get("dataset")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessDatasetA"], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''A domain to grant access to. Any users signed in with the domain specified will be granted the specified access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#domain GoogleBigqueryDatasetAccessA#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_by_email(self) -> typing.Optional[builtins.str]:
        '''An email address of a Google Group to grant access to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#group_by_email GoogleBigqueryDatasetAccessA#group_by_email}
        '''
        result = self._values.get("group_by_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_member(self) -> typing.Optional[builtins.str]:
        '''Some other type of member that appears in the IAM Policy but isn't a user, group, domain, or special group.

        For example: 'allUsers'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#iam_member GoogleBigqueryDatasetAccessA#iam_member}
        '''
        result = self._values.get("iam_member")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#id GoogleBigqueryDatasetAccessA#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project GoogleBigqueryDatasetAccessA#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Describes the rights granted to the user specified by the other member of the access object.

        Basic, predefined, and custom roles are
        supported. Predefined roles that have equivalent basic roles are
        swapped by the API to their basic counterparts, and will show a diff
        post-create. See
        `official docs <https://cloud.google.com/bigquery/docs/access-control>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#role GoogleBigqueryDatasetAccessA#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def special_group(self) -> typing.Optional[builtins.str]:
        '''A special group to grant access to. Possible values include:.

        'projectOwners': Owners of the enclosing project.

        'projectReaders': Readers of the enclosing project.

        'projectWriters': Writers of the enclosing project.

        'allAuthenticatedUsers': All authenticated BigQuery users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#special_group GoogleBigqueryDatasetAccessA#special_group}
        '''
        result = self._values.get("special_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleBigqueryDatasetAccessTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#timeouts GoogleBigqueryDatasetAccessA#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessTimeouts"], result)

    @builtins.property
    def user_by_email(self) -> typing.Optional[builtins.str]:
        '''An email address of a user to grant access to. For example: fred@example.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#user_by_email GoogleBigqueryDatasetAccessA#user_by_email}
        '''
        result = self._values.get("user_by_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view(self) -> typing.Optional["GoogleBigqueryDatasetAccessViewA"]:
        '''view block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#view GoogleBigqueryDatasetAccessA#view}
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessViewA"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessAConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessDatasetA",
    jsii_struct_bases=[],
    name_mapping={"dataset": "dataset", "target_types": "targetTypes"},
)
class GoogleBigqueryDatasetAccessDatasetA:
    def __init__(
        self,
        *,
        dataset: typing.Union["GoogleBigqueryDatasetAccessDatasetDatasetA", typing.Dict[str, typing.Any]],
        target_types: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param dataset: dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset GoogleBigqueryDatasetAccessA#dataset}
        :param target_types: Which resources in the dataset this entry applies to. Currently, only views are supported, but additional target types may be added in the future. Possible values: VIEWS Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#target_types GoogleBigqueryDatasetAccessA#target_types}
        '''
        if isinstance(dataset, dict):
            dataset = GoogleBigqueryDatasetAccessDatasetDatasetA(**dataset)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessDatasetA.__init__)
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument target_types", value=target_types, expected_type=type_hints["target_types"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset": dataset,
            "target_types": target_types,
        }

    @builtins.property
    def dataset(self) -> "GoogleBigqueryDatasetAccessDatasetDatasetA":
        '''dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset GoogleBigqueryDatasetAccessA#dataset}
        '''
        result = self._values.get("dataset")
        assert result is not None, "Required property 'dataset' is missing"
        return typing.cast("GoogleBigqueryDatasetAccessDatasetDatasetA", result)

    @builtins.property
    def target_types(self) -> typing.List[builtins.str]:
        '''Which resources in the dataset this entry applies to.

        Currently, only views are supported,
        but additional target types may be added in the future. Possible values: VIEWS

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#target_types GoogleBigqueryDatasetAccessA#target_types}
        '''
        result = self._values.get("target_types")
        assert result is not None, "Required property 'target_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessDatasetA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetAccessDatasetAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessDatasetAOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessDatasetAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDataset")
    def put_dataset(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project_id GoogleBigqueryDatasetAccessA#project_id}
        '''
        value = GoogleBigqueryDatasetAccessDatasetDatasetA(
            dataset_id=dataset_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putDataset", [value]))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> "GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference":
        return typing.cast("GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference", jsii.get(self, "dataset"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(
        self,
    ) -> typing.Optional["GoogleBigqueryDatasetAccessDatasetDatasetA"]:
        return typing.cast(typing.Optional["GoogleBigqueryDatasetAccessDatasetDatasetA"], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypesInput")
    def target_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTypes")
    def target_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetTypes"))

    @target_types.setter
    def target_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessDatasetAOutputReference, "target_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryDatasetAccessDatasetA]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessDatasetA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetAccessDatasetA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessDatasetAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessDatasetDatasetA",
    jsii_struct_bases=[],
    name_mapping={"dataset_id": "datasetId", "project_id": "projectId"},
)
class GoogleBigqueryDatasetAccessDatasetDatasetA:
    def __init__(self, *, dataset_id: builtins.str, project_id: builtins.str) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project_id GoogleBigqueryDatasetAccessA#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessDatasetDatasetA.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project_id GoogleBigqueryDatasetAccessA#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessDatasetDatasetA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryDatasetAccessDatasetDatasetA]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessDatasetDatasetA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetAccessDatasetDatasetA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleBigqueryDatasetAccessTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#create GoogleBigqueryDatasetAccessA#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#delete GoogleBigqueryDatasetAccessA#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#create GoogleBigqueryDatasetAccessA#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#delete GoogleBigqueryDatasetAccessA#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetAccessTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigqueryDatasetAccessTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigqueryDatasetAccessTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigqueryDatasetAccessTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessViewA",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "project_id": "projectId",
        "table_id": "tableId",
    },
)
class GoogleBigqueryDatasetAccessViewA:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: builtins.str,
        table_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project_id GoogleBigqueryDatasetAccessA#project_id}
        :param table_id: The ID of the table. The ID must contain only letters (a-z, A-Z), numbers (0-9), or underscores (_). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#table_id GoogleBigqueryDatasetAccessA#table_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessViewA.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
            "project_id": project_id,
            "table_id": table_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#dataset_id GoogleBigqueryDatasetAccessA#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#project_id GoogleBigqueryDatasetAccessA#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The ID of the table.

        The ID must contain only letters (a-z,
        A-Z), numbers (0-9), or underscores (_). The maximum length
        is 1,024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_dataset_access#table_id GoogleBigqueryDatasetAccessA#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryDatasetAccessViewA(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryDatasetAccessViewAOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryDatasetAccess.GoogleBigqueryDatasetAccessViewAOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryDatasetAccessViewAOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessViewAOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessViewAOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessViewAOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryDatasetAccessViewA]:
        return typing.cast(typing.Optional[GoogleBigqueryDatasetAccessViewA], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryDatasetAccessViewA],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryDatasetAccessViewAOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleBigqueryDatasetAccessA",
    "GoogleBigqueryDatasetAccessAConfig",
    "GoogleBigqueryDatasetAccessDatasetA",
    "GoogleBigqueryDatasetAccessDatasetAOutputReference",
    "GoogleBigqueryDatasetAccessDatasetDatasetA",
    "GoogleBigqueryDatasetAccessDatasetDatasetAOutputReference",
    "GoogleBigqueryDatasetAccessTimeouts",
    "GoogleBigqueryDatasetAccessTimeoutsOutputReference",
    "GoogleBigqueryDatasetAccessViewA",
    "GoogleBigqueryDatasetAccessViewAOutputReference",
]

publication.publish()
