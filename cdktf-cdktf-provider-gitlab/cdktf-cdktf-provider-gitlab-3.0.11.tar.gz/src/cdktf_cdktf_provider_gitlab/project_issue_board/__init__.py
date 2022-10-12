'''
# `gitlab_project_issue_board`

Refer to the Terraform Registory for docs: [`gitlab_project_issue_board`](https://www.terraform.io/docs/providers/gitlab/r/project_issue_board).
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


class ProjectIssueBoard(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectIssueBoard.ProjectIssueBoard",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board gitlab_project_issue_board}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        project: builtins.str,
        assignee_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        lists: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ProjectIssueBoardLists", typing.Dict[str, typing.Any]]]]] = None,
        milestone_id: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board gitlab_project_issue_board} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the board. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#name ProjectIssueBoard#name}
        :param project: The ID or full path of the project maintained by the authenticated user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#project ProjectIssueBoard#project}
        :param assignee_id: The assignee the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#assignee_id ProjectIssueBoard#assignee_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#id ProjectIssueBoard#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The list of label names which the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#labels ProjectIssueBoard#labels}
        :param lists: lists block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#lists ProjectIssueBoard#lists}
        :param milestone_id: The milestone the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#milestone_id ProjectIssueBoard#milestone_id}
        :param weight: The weight range from 0 to 9, to which the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#weight ProjectIssueBoard#weight}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProjectIssueBoard.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectIssueBoardConfig(
            name=name,
            project=project,
            assignee_id=assignee_id,
            id=id,
            labels=labels,
            lists=lists,
            milestone_id=milestone_id,
            weight=weight,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putLists")
    def put_lists(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ProjectIssueBoardLists", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProjectIssueBoard.put_lists)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLists", [value]))

    @jsii.member(jsii_name="resetAssigneeId")
    def reset_assignee_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssigneeId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLists")
    def reset_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLists", []))

    @jsii.member(jsii_name="resetMilestoneId")
    def reset_milestone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMilestoneId", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="lists")
    def lists(self) -> "ProjectIssueBoardListsList":
        return typing.cast("ProjectIssueBoardListsList", jsii.get(self, "lists"))

    @builtins.property
    @jsii.member(jsii_name="assigneeIdInput")
    def assignee_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "assigneeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="listsInput")
    def lists_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ProjectIssueBoardLists"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ProjectIssueBoardLists"]]], jsii.get(self, "listsInput"))

    @builtins.property
    @jsii.member(jsii_name="milestoneIdInput")
    def milestone_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "milestoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="assigneeId")
    def assignee_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "assigneeId"))

    @assignee_id.setter
    def assignee_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoard, "assignee_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assigneeId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoard, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoard, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="milestoneId")
    def milestone_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "milestoneId"))

    @milestone_id.setter
    def milestone_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoard, "milestone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "milestoneId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoard, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoard, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoard, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectIssueBoard.ProjectIssueBoardConfig",
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
        "project": "project",
        "assignee_id": "assigneeId",
        "id": "id",
        "labels": "labels",
        "lists": "lists",
        "milestone_id": "milestoneId",
        "weight": "weight",
    },
)
class ProjectIssueBoardConfig(cdktf.TerraformMetaArguments):
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
        project: builtins.str,
        assignee_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        lists: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ProjectIssueBoardLists", typing.Dict[str, typing.Any]]]]] = None,
        milestone_id: typing.Optional[jsii.Number] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the board. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#name ProjectIssueBoard#name}
        :param project: The ID or full path of the project maintained by the authenticated user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#project ProjectIssueBoard#project}
        :param assignee_id: The assignee the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#assignee_id ProjectIssueBoard#assignee_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#id ProjectIssueBoard#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: The list of label names which the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#labels ProjectIssueBoard#labels}
        :param lists: lists block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#lists ProjectIssueBoard#lists}
        :param milestone_id: The milestone the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#milestone_id ProjectIssueBoard#milestone_id}
        :param weight: The weight range from 0 to 9, to which the board should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#weight ProjectIssueBoard#weight}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ProjectIssueBoardConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument assignee_id", value=assignee_id, expected_type=type_hints["assignee_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument lists", value=lists, expected_type=type_hints["lists"])
            check_type(argname="argument milestone_id", value=milestone_id, expected_type=type_hints["milestone_id"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "project": project,
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
        if assignee_id is not None:
            self._values["assignee_id"] = assignee_id
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if lists is not None:
            self._values["lists"] = lists
        if milestone_id is not None:
            self._values["milestone_id"] = milestone_id
        if weight is not None:
            self._values["weight"] = weight

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
        '''The name of the board.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#name ProjectIssueBoard#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The ID or full path of the project maintained by the authenticated user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#project ProjectIssueBoard#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignee_id(self) -> typing.Optional[jsii.Number]:
        '''The assignee the board should be scoped to. Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#assignee_id ProjectIssueBoard#assignee_id}
        '''
        result = self._values.get("assignee_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#id ProjectIssueBoard#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of label names which the board should be scoped to. Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#labels ProjectIssueBoard#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def lists(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ProjectIssueBoardLists"]]]:
        '''lists block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#lists ProjectIssueBoard#lists}
        '''
        result = self._values.get("lists")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ProjectIssueBoardLists"]]], result)

    @builtins.property
    def milestone_id(self) -> typing.Optional[jsii.Number]:
        '''The milestone the board should be scoped to. Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#milestone_id ProjectIssueBoard#milestone_id}
        '''
        result = self._values.get("milestone_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''The weight range from 0 to 9, to which the board should be scoped to.

        Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#weight ProjectIssueBoard#weight}
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectIssueBoardConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.projectIssueBoard.ProjectIssueBoardLists",
    jsii_struct_bases=[],
    name_mapping={
        "assignee_id": "assigneeId",
        "iteration_id": "iterationId",
        "label_id": "labelId",
        "milestone_id": "milestoneId",
    },
)
class ProjectIssueBoardLists:
    def __init__(
        self,
        *,
        assignee_id: typing.Optional[jsii.Number] = None,
        iteration_id: typing.Optional[jsii.Number] = None,
        label_id: typing.Optional[jsii.Number] = None,
        milestone_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param assignee_id: The ID of the assignee the list should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#assignee_id ProjectIssueBoard#assignee_id}
        :param iteration_id: The ID of the iteration the list should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#iteration_id ProjectIssueBoard#iteration_id}
        :param label_id: The ID of the label the list should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#label_id ProjectIssueBoard#label_id}
        :param milestone_id: The ID of the milestone the list should be scoped to. Requires a GitLab EE license. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#milestone_id ProjectIssueBoard#milestone_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProjectIssueBoardLists.__init__)
            check_type(argname="argument assignee_id", value=assignee_id, expected_type=type_hints["assignee_id"])
            check_type(argname="argument iteration_id", value=iteration_id, expected_type=type_hints["iteration_id"])
            check_type(argname="argument label_id", value=label_id, expected_type=type_hints["label_id"])
            check_type(argname="argument milestone_id", value=milestone_id, expected_type=type_hints["milestone_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if assignee_id is not None:
            self._values["assignee_id"] = assignee_id
        if iteration_id is not None:
            self._values["iteration_id"] = iteration_id
        if label_id is not None:
            self._values["label_id"] = label_id
        if milestone_id is not None:
            self._values["milestone_id"] = milestone_id

    @builtins.property
    def assignee_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the assignee the list should be scoped to. Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#assignee_id ProjectIssueBoard#assignee_id}
        '''
        result = self._values.get("assignee_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def iteration_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the iteration the list should be scoped to. Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#iteration_id ProjectIssueBoard#iteration_id}
        '''
        result = self._values.get("iteration_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def label_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the label the list should be scoped to. Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#label_id ProjectIssueBoard#label_id}
        '''
        result = self._values.get("label_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def milestone_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the milestone the list should be scoped to. Requires a GitLab EE license.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project_issue_board#milestone_id ProjectIssueBoard#milestone_id}
        '''
        result = self._values.get("milestone_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectIssueBoardLists(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectIssueBoardListsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectIssueBoard.ProjectIssueBoardListsList",
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
            type_hints = typing.get_type_hints(ProjectIssueBoardListsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ProjectIssueBoardListsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProjectIssueBoardListsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ProjectIssueBoardListsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProjectIssueBoardLists]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProjectIssueBoardLists]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ProjectIssueBoardLists]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ProjectIssueBoardListsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.projectIssueBoard.ProjectIssueBoardListsOutputReference",
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
            type_hints = typing.get_type_hints(ProjectIssueBoardListsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAssigneeId")
    def reset_assignee_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssigneeId", []))

    @jsii.member(jsii_name="resetIterationId")
    def reset_iteration_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIterationId", []))

    @jsii.member(jsii_name="resetLabelId")
    def reset_label_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelId", []))

    @jsii.member(jsii_name="resetMilestoneId")
    def reset_milestone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMilestoneId", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "position"))

    @builtins.property
    @jsii.member(jsii_name="assigneeIdInput")
    def assignee_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "assigneeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iterationIdInput")
    def iteration_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "iterationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="labelIdInput")
    def label_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "labelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="milestoneIdInput")
    def milestone_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "milestoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="assigneeId")
    def assignee_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "assigneeId"))

    @assignee_id.setter
    def assignee_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsOutputReference, "assignee_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assigneeId", value)

    @builtins.property
    @jsii.member(jsii_name="iterationId")
    def iteration_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iterationId"))

    @iteration_id.setter
    def iteration_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsOutputReference, "iteration_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iterationId", value)

    @builtins.property
    @jsii.member(jsii_name="labelId")
    def label_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "labelId"))

    @label_id.setter
    def label_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsOutputReference, "label_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labelId", value)

    @builtins.property
    @jsii.member(jsii_name="milestoneId")
    def milestone_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "milestoneId"))

    @milestone_id.setter
    def milestone_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsOutputReference, "milestone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "milestoneId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ProjectIssueBoardLists, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ProjectIssueBoardLists, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ProjectIssueBoardLists, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectIssueBoardListsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ProjectIssueBoard",
    "ProjectIssueBoardConfig",
    "ProjectIssueBoardLists",
    "ProjectIssueBoardListsList",
    "ProjectIssueBoardListsOutputReference",
]

publication.publish()
