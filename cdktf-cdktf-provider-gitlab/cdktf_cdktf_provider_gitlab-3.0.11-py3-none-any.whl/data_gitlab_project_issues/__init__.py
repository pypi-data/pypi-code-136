'''
# `data_gitlab_project_issues`

Refer to the Terraform Registory for docs: [`data_gitlab_project_issues`](https://www.terraform.io/docs/providers/gitlab/d/project_issues).
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


class DataGitlabProjectIssues(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssues",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues gitlab_project_issues}.'''

    def __init__(
        self,
        scope_: constructs.Construct,
        id_: builtins.str,
        *,
        project: builtins.str,
        assignee_id: typing.Optional[jsii.Number] = None,
        assignee_username: typing.Optional[builtins.str] = None,
        author_id: typing.Optional[jsii.Number] = None,
        confidential: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        created_after: typing.Optional[builtins.str] = None,
        created_before: typing.Optional[builtins.str] = None,
        due_date: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        iids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        issue_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        milestone: typing.Optional[builtins.str] = None,
        my_reaction_emoji: typing.Optional[builtins.str] = None,
        not_assignee_id: typing.Optional[typing.Sequence[jsii.Number]] = None,
        not_author_id: typing.Optional[typing.Sequence[jsii.Number]] = None,
        not_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_milestone: typing.Optional[builtins.str] = None,
        not_my_reaction_emoji: typing.Optional[typing.Sequence[builtins.str]] = None,
        order_by: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        search: typing.Optional[builtins.str] = None,
        sort: typing.Optional[builtins.str] = None,
        updated_after: typing.Optional[builtins.str] = None,
        updated_before: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
        with_labels_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues gitlab_project_issues} Data Source.

        :param scope_: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param project: The name or id of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#project DataGitlabProjectIssues#project}
        :param assignee_id: Return issues assigned to the given user id. Mutually exclusive with assignee_username. None returns unassigned issues. Any returns issues with an assignee. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#assignee_id DataGitlabProjectIssues#assignee_id}
        :param assignee_username: Return issues assigned to the given username. Similar to assignee_id and mutually exclusive with assignee_id. In GitLab CE, the assignee_username array should only contain a single value. Otherwise, an invalid parameter error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#assignee_username DataGitlabProjectIssues#assignee_username}
        :param author_id: Return issues created by the given user id. Combine with scope=all or scope=assigned_to_me. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#author_id DataGitlabProjectIssues#author_id}
        :param confidential: Filter confidential or public issues. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#confidential DataGitlabProjectIssues#confidential}
        :param created_after: Return issues created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#created_after DataGitlabProjectIssues#created_after}
        :param created_before: Return issues created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#created_before DataGitlabProjectIssues#created_before}
        :param due_date: Return issues that have no due date, are overdue, or whose due date is this week, this month, or between two weeks ago and next month. Accepts: 0 (no due date), any, today, tomorrow, overdue, week, month, next_month_and_previous_two_weeks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#due_date DataGitlabProjectIssues#due_date}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#id DataGitlabProjectIssues#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iids: Return only the issues having the given iid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#iids DataGitlabProjectIssues#iids}
        :param issue_type: Filter to a given type of issue. Valid values are [issue incident test_case]. (Introduced in GitLab 13.12). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#issue_type DataGitlabProjectIssues#issue_type}
        :param labels: Return issues with labels. Issues must have all labels to be returned. None lists all issues with no labels. Any lists all issues with at least one label. No+Label (Deprecated) lists all issues with no labels. Predefined names are case-insensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#labels DataGitlabProjectIssues#labels}
        :param milestone: The milestone title. None lists all issues with no milestone. Any lists all issues that have an assigned milestone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#milestone DataGitlabProjectIssues#milestone}
        :param my_reaction_emoji: Return issues reacted by the authenticated user by the given emoji. None returns issues not given a reaction. Any returns issues given at least one reaction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#my_reaction_emoji DataGitlabProjectIssues#my_reaction_emoji}
        :param not_assignee_id: Return issues that do not match the assignee id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_assignee_id DataGitlabProjectIssues#not_assignee_id}
        :param not_author_id: Return issues that do not match the author id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_author_id DataGitlabProjectIssues#not_author_id}
        :param not_labels: Return issues that do not match the labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_labels DataGitlabProjectIssues#not_labels}
        :param not_milestone: Return issues that do not match the milestone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_milestone DataGitlabProjectIssues#not_milestone}
        :param not_my_reaction_emoji: Return issues not reacted by the authenticated user by the given emoji. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_my_reaction_emoji DataGitlabProjectIssues#not_my_reaction_emoji}
        :param order_by: Return issues ordered by. Valid values are ``created_at``, ``updated_at``, ``priority``, ``due_date``, ``relative_position``, ``label_priority``, ``milestone_due``, ``popularity``, ``weight``. Default is created_at. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#order_by DataGitlabProjectIssues#order_by}
        :param scope: Return issues for the given scope. Valid values are ``created_by_me``, ``assigned_to_me``, ``all``. Defaults to all. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#scope DataGitlabProjectIssues#scope}
        :param search: Search project issues against their title and description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#search DataGitlabProjectIssues#search}
        :param sort: Return issues sorted in asc or desc order. Default is desc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#sort DataGitlabProjectIssues#sort}
        :param updated_after: Return issues updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#updated_after DataGitlabProjectIssues#updated_after}
        :param updated_before: Return issues updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#updated_before DataGitlabProjectIssues#updated_before}
        :param weight: Return issues with the specified weight. None returns issues with no weight assigned. Any returns issues with a weight assigned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#weight DataGitlabProjectIssues#weight}
        :param with_labels_details: If true, the response returns more details for each label in labels field: :name, :color, :description, :description_html, :text_color. Default is false. description_html was introduced in GitLab 12.7 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#with_labels_details DataGitlabProjectIssues#with_labels_details}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectIssues.__init__)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGitlabProjectIssuesConfig(
            project=project,
            assignee_id=assignee_id,
            assignee_username=assignee_username,
            author_id=author_id,
            confidential=confidential,
            created_after=created_after,
            created_before=created_before,
            due_date=due_date,
            id=id,
            iids=iids,
            issue_type=issue_type,
            labels=labels,
            milestone=milestone,
            my_reaction_emoji=my_reaction_emoji,
            not_assignee_id=not_assignee_id,
            not_author_id=not_author_id,
            not_labels=not_labels,
            not_milestone=not_milestone,
            not_my_reaction_emoji=not_my_reaction_emoji,
            order_by=order_by,
            scope=scope,
            search=search,
            sort=sort,
            updated_after=updated_after,
            updated_before=updated_before,
            weight=weight,
            with_labels_details=with_labels_details,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope_, id_, config])

    @jsii.member(jsii_name="resetAssigneeId")
    def reset_assignee_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssigneeId", []))

    @jsii.member(jsii_name="resetAssigneeUsername")
    def reset_assignee_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssigneeUsername", []))

    @jsii.member(jsii_name="resetAuthorId")
    def reset_author_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorId", []))

    @jsii.member(jsii_name="resetConfidential")
    def reset_confidential(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidential", []))

    @jsii.member(jsii_name="resetCreatedAfter")
    def reset_created_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedAfter", []))

    @jsii.member(jsii_name="resetCreatedBefore")
    def reset_created_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedBefore", []))

    @jsii.member(jsii_name="resetDueDate")
    def reset_due_date(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDueDate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIids")
    def reset_iids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIids", []))

    @jsii.member(jsii_name="resetIssueType")
    def reset_issue_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssueType", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMilestone")
    def reset_milestone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMilestone", []))

    @jsii.member(jsii_name="resetMyReactionEmoji")
    def reset_my_reaction_emoji(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMyReactionEmoji", []))

    @jsii.member(jsii_name="resetNotAssigneeId")
    def reset_not_assignee_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotAssigneeId", []))

    @jsii.member(jsii_name="resetNotAuthorId")
    def reset_not_author_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotAuthorId", []))

    @jsii.member(jsii_name="resetNotLabels")
    def reset_not_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotLabels", []))

    @jsii.member(jsii_name="resetNotMilestone")
    def reset_not_milestone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotMilestone", []))

    @jsii.member(jsii_name="resetNotMyReactionEmoji")
    def reset_not_my_reaction_emoji(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotMyReactionEmoji", []))

    @jsii.member(jsii_name="resetOrderBy")
    def reset_order_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrderBy", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetSearch")
    def reset_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearch", []))

    @jsii.member(jsii_name="resetSort")
    def reset_sort(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSort", []))

    @jsii.member(jsii_name="resetUpdatedAfter")
    def reset_updated_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatedAfter", []))

    @jsii.member(jsii_name="resetUpdatedBefore")
    def reset_updated_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdatedBefore", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @jsii.member(jsii_name="resetWithLabelsDetails")
    def reset_with_labels_details(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithLabelsDetails", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="issues")
    def issues(self) -> "DataGitlabProjectIssuesIssuesList":
        return typing.cast("DataGitlabProjectIssuesIssuesList", jsii.get(self, "issues"))

    @builtins.property
    @jsii.member(jsii_name="assigneeIdInput")
    def assignee_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "assigneeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="assigneeUsernameInput")
    def assignee_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assigneeUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="authorIdInput")
    def author_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialInput")
    def confidential_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "confidentialInput"))

    @builtins.property
    @jsii.member(jsii_name="createdAfterInput")
    def created_after_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="createdBeforeInput")
    def created_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="dueDateInput")
    def due_date_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dueDateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="iidsInput")
    def iids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "iidsInput"))

    @builtins.property
    @jsii.member(jsii_name="issueTypeInput")
    def issue_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issueTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="milestoneInput")
    def milestone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "milestoneInput"))

    @builtins.property
    @jsii.member(jsii_name="myReactionEmojiInput")
    def my_reaction_emoji_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "myReactionEmojiInput"))

    @builtins.property
    @jsii.member(jsii_name="notAssigneeIdInput")
    def not_assignee_id_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "notAssigneeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="notAuthorIdInput")
    def not_author_id_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "notAuthorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="notLabelsInput")
    def not_labels_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="notMilestoneInput")
    def not_milestone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notMilestoneInput"))

    @builtins.property
    @jsii.member(jsii_name="notMyReactionEmojiInput")
    def not_my_reaction_emoji_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notMyReactionEmojiInput"))

    @builtins.property
    @jsii.member(jsii_name="orderByInput")
    def order_by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orderByInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="searchInput")
    def search_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "searchInput"))

    @builtins.property
    @jsii.member(jsii_name="sortInput")
    def sort_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sortInput"))

    @builtins.property
    @jsii.member(jsii_name="updatedAfterInput")
    def updated_after_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updatedAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="updatedBeforeInput")
    def updated_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updatedBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="withLabelsDetailsInput")
    def with_labels_details_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "withLabelsDetailsInput"))

    @builtins.property
    @jsii.member(jsii_name="assigneeId")
    def assignee_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "assigneeId"))

    @assignee_id.setter
    def assignee_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "assignee_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assigneeId", value)

    @builtins.property
    @jsii.member(jsii_name="assigneeUsername")
    def assignee_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assigneeUsername"))

    @assignee_username.setter
    def assignee_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "assignee_username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assigneeUsername", value)

    @builtins.property
    @jsii.member(jsii_name="authorId")
    def author_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authorId"))

    @author_id.setter
    def author_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "author_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorId", value)

    @builtins.property
    @jsii.member(jsii_name="confidential")
    def confidential(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "confidential"))

    @confidential.setter
    def confidential(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "confidential").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidential", value)

    @builtins.property
    @jsii.member(jsii_name="createdAfter")
    def created_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAfter"))

    @created_after.setter
    def created_after(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "created_after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdAfter", value)

    @builtins.property
    @jsii.member(jsii_name="createdBefore")
    def created_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBefore"))

    @created_before.setter
    def created_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "created_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBefore", value)

    @builtins.property
    @jsii.member(jsii_name="dueDate")
    def due_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dueDate"))

    @due_date.setter
    def due_date(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "due_date").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dueDate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="iids")
    def iids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "iids"))

    @iids.setter
    def iids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "iids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iids", value)

    @builtins.property
    @jsii.member(jsii_name="issueType")
    def issue_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issueType"))

    @issue_type.setter
    def issue_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "issue_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issueType", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="milestone")
    def milestone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "milestone"))

    @milestone.setter
    def milestone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "milestone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "milestone", value)

    @builtins.property
    @jsii.member(jsii_name="myReactionEmoji")
    def my_reaction_emoji(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "myReactionEmoji"))

    @my_reaction_emoji.setter
    def my_reaction_emoji(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "my_reaction_emoji").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "myReactionEmoji", value)

    @builtins.property
    @jsii.member(jsii_name="notAssigneeId")
    def not_assignee_id(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "notAssigneeId"))

    @not_assignee_id.setter
    def not_assignee_id(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "not_assignee_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notAssigneeId", value)

    @builtins.property
    @jsii.member(jsii_name="notAuthorId")
    def not_author_id(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "notAuthorId"))

    @not_author_id.setter
    def not_author_id(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "not_author_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notAuthorId", value)

    @builtins.property
    @jsii.member(jsii_name="notLabels")
    def not_labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notLabels"))

    @not_labels.setter
    def not_labels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "not_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notLabels", value)

    @builtins.property
    @jsii.member(jsii_name="notMilestone")
    def not_milestone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notMilestone"))

    @not_milestone.setter
    def not_milestone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "not_milestone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notMilestone", value)

    @builtins.property
    @jsii.member(jsii_name="notMyReactionEmoji")
    def not_my_reaction_emoji(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notMyReactionEmoji"))

    @not_my_reaction_emoji.setter
    def not_my_reaction_emoji(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "not_my_reaction_emoji").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notMyReactionEmoji", value)

    @builtins.property
    @jsii.member(jsii_name="orderBy")
    def order_by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orderBy"))

    @order_by.setter
    def order_by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "order_by").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orderBy", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="search")
    def search(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "search"))

    @search.setter
    def search(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "search").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "search", value)

    @builtins.property
    @jsii.member(jsii_name="sort")
    def sort(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sort"))

    @sort.setter
    def sort(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "sort").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sort", value)

    @builtins.property
    @jsii.member(jsii_name="updatedAfter")
    def updated_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAfter"))

    @updated_after.setter
    def updated_after(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "updated_after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatedAfter", value)

    @builtins.property
    @jsii.member(jsii_name="updatedBefore")
    def updated_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedBefore"))

    @updated_before.setter
    def updated_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "updated_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updatedBefore", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="withLabelsDetails")
    def with_labels_details(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "withLabelsDetails"))

    @with_labels_details.setter
    def with_labels_details(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssues, "with_labels_details").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withLabelsDetails", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssuesConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "project": "project",
        "assignee_id": "assigneeId",
        "assignee_username": "assigneeUsername",
        "author_id": "authorId",
        "confidential": "confidential",
        "created_after": "createdAfter",
        "created_before": "createdBefore",
        "due_date": "dueDate",
        "id": "id",
        "iids": "iids",
        "issue_type": "issueType",
        "labels": "labels",
        "milestone": "milestone",
        "my_reaction_emoji": "myReactionEmoji",
        "not_assignee_id": "notAssigneeId",
        "not_author_id": "notAuthorId",
        "not_labels": "notLabels",
        "not_milestone": "notMilestone",
        "not_my_reaction_emoji": "notMyReactionEmoji",
        "order_by": "orderBy",
        "scope": "scope",
        "search": "search",
        "sort": "sort",
        "updated_after": "updatedAfter",
        "updated_before": "updatedBefore",
        "weight": "weight",
        "with_labels_details": "withLabelsDetails",
    },
)
class DataGitlabProjectIssuesConfig(cdktf.TerraformMetaArguments):
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
        project: builtins.str,
        assignee_id: typing.Optional[jsii.Number] = None,
        assignee_username: typing.Optional[builtins.str] = None,
        author_id: typing.Optional[jsii.Number] = None,
        confidential: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        created_after: typing.Optional[builtins.str] = None,
        created_before: typing.Optional[builtins.str] = None,
        due_date: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        iids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        issue_type: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        milestone: typing.Optional[builtins.str] = None,
        my_reaction_emoji: typing.Optional[builtins.str] = None,
        not_assignee_id: typing.Optional[typing.Sequence[jsii.Number]] = None,
        not_author_id: typing.Optional[typing.Sequence[jsii.Number]] = None,
        not_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_milestone: typing.Optional[builtins.str] = None,
        not_my_reaction_emoji: typing.Optional[typing.Sequence[builtins.str]] = None,
        order_by: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        search: typing.Optional[builtins.str] = None,
        sort: typing.Optional[builtins.str] = None,
        updated_after: typing.Optional[builtins.str] = None,
        updated_before: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
        with_labels_details: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param project: The name or id of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#project DataGitlabProjectIssues#project}
        :param assignee_id: Return issues assigned to the given user id. Mutually exclusive with assignee_username. None returns unassigned issues. Any returns issues with an assignee. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#assignee_id DataGitlabProjectIssues#assignee_id}
        :param assignee_username: Return issues assigned to the given username. Similar to assignee_id and mutually exclusive with assignee_id. In GitLab CE, the assignee_username array should only contain a single value. Otherwise, an invalid parameter error is returned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#assignee_username DataGitlabProjectIssues#assignee_username}
        :param author_id: Return issues created by the given user id. Combine with scope=all or scope=assigned_to_me. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#author_id DataGitlabProjectIssues#author_id}
        :param confidential: Filter confidential or public issues. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#confidential DataGitlabProjectIssues#confidential}
        :param created_after: Return issues created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#created_after DataGitlabProjectIssues#created_after}
        :param created_before: Return issues created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#created_before DataGitlabProjectIssues#created_before}
        :param due_date: Return issues that have no due date, are overdue, or whose due date is this week, this month, or between two weeks ago and next month. Accepts: 0 (no due date), any, today, tomorrow, overdue, week, month, next_month_and_previous_two_weeks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#due_date DataGitlabProjectIssues#due_date}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#id DataGitlabProjectIssues#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param iids: Return only the issues having the given iid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#iids DataGitlabProjectIssues#iids}
        :param issue_type: Filter to a given type of issue. Valid values are [issue incident test_case]. (Introduced in GitLab 13.12). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#issue_type DataGitlabProjectIssues#issue_type}
        :param labels: Return issues with labels. Issues must have all labels to be returned. None lists all issues with no labels. Any lists all issues with at least one label. No+Label (Deprecated) lists all issues with no labels. Predefined names are case-insensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#labels DataGitlabProjectIssues#labels}
        :param milestone: The milestone title. None lists all issues with no milestone. Any lists all issues that have an assigned milestone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#milestone DataGitlabProjectIssues#milestone}
        :param my_reaction_emoji: Return issues reacted by the authenticated user by the given emoji. None returns issues not given a reaction. Any returns issues given at least one reaction. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#my_reaction_emoji DataGitlabProjectIssues#my_reaction_emoji}
        :param not_assignee_id: Return issues that do not match the assignee id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_assignee_id DataGitlabProjectIssues#not_assignee_id}
        :param not_author_id: Return issues that do not match the author id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_author_id DataGitlabProjectIssues#not_author_id}
        :param not_labels: Return issues that do not match the labels. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_labels DataGitlabProjectIssues#not_labels}
        :param not_milestone: Return issues that do not match the milestone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_milestone DataGitlabProjectIssues#not_milestone}
        :param not_my_reaction_emoji: Return issues not reacted by the authenticated user by the given emoji. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_my_reaction_emoji DataGitlabProjectIssues#not_my_reaction_emoji}
        :param order_by: Return issues ordered by. Valid values are ``created_at``, ``updated_at``, ``priority``, ``due_date``, ``relative_position``, ``label_priority``, ``milestone_due``, ``popularity``, ``weight``. Default is created_at. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#order_by DataGitlabProjectIssues#order_by}
        :param scope: Return issues for the given scope. Valid values are ``created_by_me``, ``assigned_to_me``, ``all``. Defaults to all. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#scope DataGitlabProjectIssues#scope}
        :param search: Search project issues against their title and description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#search DataGitlabProjectIssues#search}
        :param sort: Return issues sorted in asc or desc order. Default is desc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#sort DataGitlabProjectIssues#sort}
        :param updated_after: Return issues updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#updated_after DataGitlabProjectIssues#updated_after}
        :param updated_before: Return issues updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#updated_before DataGitlabProjectIssues#updated_before}
        :param weight: Return issues with the specified weight. None returns issues with no weight assigned. Any returns issues with a weight assigned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#weight DataGitlabProjectIssues#weight}
        :param with_labels_details: If true, the response returns more details for each label in labels field: :name, :color, :description, :description_html, :text_color. Default is false. description_html was introduced in GitLab 12.7 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#with_labels_details DataGitlabProjectIssues#with_labels_details}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectIssuesConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument assignee_id", value=assignee_id, expected_type=type_hints["assignee_id"])
            check_type(argname="argument assignee_username", value=assignee_username, expected_type=type_hints["assignee_username"])
            check_type(argname="argument author_id", value=author_id, expected_type=type_hints["author_id"])
            check_type(argname="argument confidential", value=confidential, expected_type=type_hints["confidential"])
            check_type(argname="argument created_after", value=created_after, expected_type=type_hints["created_after"])
            check_type(argname="argument created_before", value=created_before, expected_type=type_hints["created_before"])
            check_type(argname="argument due_date", value=due_date, expected_type=type_hints["due_date"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument iids", value=iids, expected_type=type_hints["iids"])
            check_type(argname="argument issue_type", value=issue_type, expected_type=type_hints["issue_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument milestone", value=milestone, expected_type=type_hints["milestone"])
            check_type(argname="argument my_reaction_emoji", value=my_reaction_emoji, expected_type=type_hints["my_reaction_emoji"])
            check_type(argname="argument not_assignee_id", value=not_assignee_id, expected_type=type_hints["not_assignee_id"])
            check_type(argname="argument not_author_id", value=not_author_id, expected_type=type_hints["not_author_id"])
            check_type(argname="argument not_labels", value=not_labels, expected_type=type_hints["not_labels"])
            check_type(argname="argument not_milestone", value=not_milestone, expected_type=type_hints["not_milestone"])
            check_type(argname="argument not_my_reaction_emoji", value=not_my_reaction_emoji, expected_type=type_hints["not_my_reaction_emoji"])
            check_type(argname="argument order_by", value=order_by, expected_type=type_hints["order_by"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument search", value=search, expected_type=type_hints["search"])
            check_type(argname="argument sort", value=sort, expected_type=type_hints["sort"])
            check_type(argname="argument updated_after", value=updated_after, expected_type=type_hints["updated_after"])
            check_type(argname="argument updated_before", value=updated_before, expected_type=type_hints["updated_before"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument with_labels_details", value=with_labels_details, expected_type=type_hints["with_labels_details"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if assignee_username is not None:
            self._values["assignee_username"] = assignee_username
        if author_id is not None:
            self._values["author_id"] = author_id
        if confidential is not None:
            self._values["confidential"] = confidential
        if created_after is not None:
            self._values["created_after"] = created_after
        if created_before is not None:
            self._values["created_before"] = created_before
        if due_date is not None:
            self._values["due_date"] = due_date
        if id is not None:
            self._values["id"] = id
        if iids is not None:
            self._values["iids"] = iids
        if issue_type is not None:
            self._values["issue_type"] = issue_type
        if labels is not None:
            self._values["labels"] = labels
        if milestone is not None:
            self._values["milestone"] = milestone
        if my_reaction_emoji is not None:
            self._values["my_reaction_emoji"] = my_reaction_emoji
        if not_assignee_id is not None:
            self._values["not_assignee_id"] = not_assignee_id
        if not_author_id is not None:
            self._values["not_author_id"] = not_author_id
        if not_labels is not None:
            self._values["not_labels"] = not_labels
        if not_milestone is not None:
            self._values["not_milestone"] = not_milestone
        if not_my_reaction_emoji is not None:
            self._values["not_my_reaction_emoji"] = not_my_reaction_emoji
        if order_by is not None:
            self._values["order_by"] = order_by
        if scope is not None:
            self._values["scope"] = scope
        if search is not None:
            self._values["search"] = search
        if sort is not None:
            self._values["sort"] = sort
        if updated_after is not None:
            self._values["updated_after"] = updated_after
        if updated_before is not None:
            self._values["updated_before"] = updated_before
        if weight is not None:
            self._values["weight"] = weight
        if with_labels_details is not None:
            self._values["with_labels_details"] = with_labels_details

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
    def project(self) -> builtins.str:
        '''The name or id of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#project DataGitlabProjectIssues#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assignee_id(self) -> typing.Optional[jsii.Number]:
        '''Return issues assigned to the given user id.

        Mutually exclusive with assignee_username. None returns unassigned issues. Any returns issues with an assignee.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#assignee_id DataGitlabProjectIssues#assignee_id}
        '''
        result = self._values.get("assignee_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def assignee_username(self) -> typing.Optional[builtins.str]:
        '''Return issues assigned to the given username.

        Similar to assignee_id and mutually exclusive with assignee_id. In GitLab CE, the assignee_username array should only contain a single value. Otherwise, an invalid parameter error is returned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#assignee_username DataGitlabProjectIssues#assignee_username}
        '''
        result = self._values.get("assignee_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def author_id(self) -> typing.Optional[jsii.Number]:
        '''Return issues created by the given user id. Combine with scope=all or scope=assigned_to_me.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#author_id DataGitlabProjectIssues#author_id}
        '''
        result = self._values.get("author_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def confidential(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Filter confidential or public issues.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#confidential DataGitlabProjectIssues#confidential}
        '''
        result = self._values.get("confidential")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def created_after(self) -> typing.Optional[builtins.str]:
        '''Return issues created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#created_after DataGitlabProjectIssues#created_after}
        '''
        result = self._values.get("created_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def created_before(self) -> typing.Optional[builtins.str]:
        '''Return issues created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#created_before DataGitlabProjectIssues#created_before}
        '''
        result = self._values.get("created_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def due_date(self) -> typing.Optional[builtins.str]:
        '''Return issues that have no due date, are overdue, or whose due date is this week, this month, or between two weeks ago and next month.

        Accepts: 0 (no due date), any, today, tomorrow, overdue, week, month, next_month_and_previous_two_weeks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#due_date DataGitlabProjectIssues#due_date}
        '''
        result = self._values.get("due_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#id DataGitlabProjectIssues#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return only the issues having the given iid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#iids DataGitlabProjectIssues#iids}
        '''
        result = self._values.get("iids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def issue_type(self) -> typing.Optional[builtins.str]:
        '''Filter to a given type of issue. Valid values are [issue incident test_case]. (Introduced in GitLab 13.12).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#issue_type DataGitlabProjectIssues#issue_type}
        '''
        result = self._values.get("issue_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Return issues with labels.

        Issues must have all labels to be returned. None lists all issues with no labels. Any lists all issues with at least one label. No+Label (Deprecated) lists all issues with no labels. Predefined names are case-insensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#labels DataGitlabProjectIssues#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def milestone(self) -> typing.Optional[builtins.str]:
        '''The milestone title. None lists all issues with no milestone. Any lists all issues that have an assigned milestone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#milestone DataGitlabProjectIssues#milestone}
        '''
        result = self._values.get("milestone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def my_reaction_emoji(self) -> typing.Optional[builtins.str]:
        '''Return issues reacted by the authenticated user by the given emoji.

        None returns issues not given a reaction. Any returns issues given at least one reaction.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#my_reaction_emoji DataGitlabProjectIssues#my_reaction_emoji}
        '''
        result = self._values.get("my_reaction_emoji")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_assignee_id(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return issues that do not match the assignee id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_assignee_id DataGitlabProjectIssues#not_assignee_id}
        '''
        result = self._values.get("not_assignee_id")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def not_author_id(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Return issues that do not match the author id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_author_id DataGitlabProjectIssues#not_author_id}
        '''
        result = self._values.get("not_author_id")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def not_labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Return issues that do not match the labels.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_labels DataGitlabProjectIssues#not_labels}
        '''
        result = self._values.get("not_labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_milestone(self) -> typing.Optional[builtins.str]:
        '''Return issues that do not match the milestone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_milestone DataGitlabProjectIssues#not_milestone}
        '''
        result = self._values.get("not_milestone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_my_reaction_emoji(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Return issues not reacted by the authenticated user by the given emoji.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#not_my_reaction_emoji DataGitlabProjectIssues#not_my_reaction_emoji}
        '''
        result = self._values.get("not_my_reaction_emoji")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def order_by(self) -> typing.Optional[builtins.str]:
        '''Return issues ordered by. Valid values are ``created_at``, ``updated_at``, ``priority``, ``due_date``, ``relative_position``, ``label_priority``, ``milestone_due``, ``popularity``, ``weight``. Default is created_at.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#order_by DataGitlabProjectIssues#order_by}
        '''
        result = self._values.get("order_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Return issues for the given scope. Valid values are ``created_by_me``, ``assigned_to_me``, ``all``. Defaults to all.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#scope DataGitlabProjectIssues#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def search(self) -> typing.Optional[builtins.str]:
        '''Search project issues against their title and description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#search DataGitlabProjectIssues#search}
        '''
        result = self._values.get("search")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sort(self) -> typing.Optional[builtins.str]:
        '''Return issues sorted in asc or desc order. Default is desc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#sort DataGitlabProjectIssues#sort}
        '''
        result = self._values.get("sort")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def updated_after(self) -> typing.Optional[builtins.str]:
        '''Return issues updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#updated_after DataGitlabProjectIssues#updated_after}
        '''
        result = self._values.get("updated_after")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def updated_before(self) -> typing.Optional[builtins.str]:
        '''Return issues updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#updated_before DataGitlabProjectIssues#updated_before}
        '''
        result = self._values.get("updated_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Return issues with the specified weight.

        None returns issues with no weight assigned. Any returns issues with a weight assigned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#weight DataGitlabProjectIssues#weight}
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def with_labels_details(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the response returns more details for each label in labels field: :name, :color, :description, :description_html, :text_color.

        Default is false. description_html was introduced in GitLab 12.7

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project_issues#with_labels_details DataGitlabProjectIssues#with_labels_details}
        '''
        result = self._values.get("with_labels_details")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectIssuesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssuesIssues",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGitlabProjectIssuesIssues:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectIssuesIssues(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGitlabProjectIssuesIssuesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssuesIssuesList",
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
            type_hints = typing.get_type_hints(DataGitlabProjectIssuesIssuesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataGitlabProjectIssuesIssuesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectIssuesIssuesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGitlabProjectIssuesIssuesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGitlabProjectIssuesIssuesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssuesIssuesOutputReference",
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
            type_hints = typing.get_type_hints(DataGitlabProjectIssuesIssuesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="assigneeIds")
    def assignee_ids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "assigneeIds"))

    @builtins.property
    @jsii.member(jsii_name="authorId")
    def author_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "authorId"))

    @builtins.property
    @jsii.member(jsii_name="closedAt")
    def closed_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "closedAt"))

    @builtins.property
    @jsii.member(jsii_name="closedByUserId")
    def closed_by_user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "closedByUserId"))

    @builtins.property
    @jsii.member(jsii_name="confidential")
    def confidential(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "confidential"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="discussionLocked")
    def discussion_locked(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "discussionLocked"))

    @builtins.property
    @jsii.member(jsii_name="discussionToResolve")
    def discussion_to_resolve(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "discussionToResolve"))

    @builtins.property
    @jsii.member(jsii_name="downvotes")
    def downvotes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "downvotes"))

    @builtins.property
    @jsii.member(jsii_name="dueDate")
    def due_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dueDate"))

    @builtins.property
    @jsii.member(jsii_name="epicId")
    def epic_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "epicId"))

    @builtins.property
    @jsii.member(jsii_name="epicIssueId")
    def epic_issue_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "epicIssueId"))

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @builtins.property
    @jsii.member(jsii_name="humanTimeEstimate")
    def human_time_estimate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "humanTimeEstimate"))

    @builtins.property
    @jsii.member(jsii_name="humanTotalTimeSpent")
    def human_total_time_spent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "humanTotalTimeSpent"))

    @builtins.property
    @jsii.member(jsii_name="iid")
    def iid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "iid"))

    @builtins.property
    @jsii.member(jsii_name="issueId")
    def issue_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "issueId"))

    @builtins.property
    @jsii.member(jsii_name="issueLinkId")
    def issue_link_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "issueLinkId"))

    @builtins.property
    @jsii.member(jsii_name="issueType")
    def issue_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issueType"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsCount")
    def merge_requests_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mergeRequestsCount"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestToResolveDiscussionsOf")
    def merge_request_to_resolve_discussions_of(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "mergeRequestToResolveDiscussionsOf"))

    @builtins.property
    @jsii.member(jsii_name="milestoneId")
    def milestone_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "milestoneId"))

    @builtins.property
    @jsii.member(jsii_name="movedToId")
    def moved_to_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "movedToId"))

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @builtins.property
    @jsii.member(jsii_name="references")
    def references(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "references"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="subscribed")
    def subscribed(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "subscribed"))

    @builtins.property
    @jsii.member(jsii_name="taskCompletionStatus")
    def task_completion_status(
        self,
    ) -> "DataGitlabProjectIssuesIssuesTaskCompletionStatusList":
        return typing.cast("DataGitlabProjectIssuesIssuesTaskCompletionStatusList", jsii.get(self, "taskCompletionStatus"))

    @builtins.property
    @jsii.member(jsii_name="timeEstimate")
    def time_estimate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeEstimate"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="totalTimeSpent")
    def total_time_spent(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "totalTimeSpent"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="upvotes")
    def upvotes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "upvotes"))

    @builtins.property
    @jsii.member(jsii_name="userNotesCount")
    def user_notes_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userNotesCount"))

    @builtins.property
    @jsii.member(jsii_name="webUrl")
    def web_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webUrl"))

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataGitlabProjectIssuesIssues]:
        return typing.cast(typing.Optional[DataGitlabProjectIssuesIssues], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGitlabProjectIssuesIssues],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssuesIssuesTaskCompletionStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGitlabProjectIssuesIssuesTaskCompletionStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectIssuesIssuesTaskCompletionStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGitlabProjectIssuesIssuesTaskCompletionStatusList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssuesIssuesTaskCompletionStatusList",
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
            type_hints = typing.get_type_hints(DataGitlabProjectIssuesIssuesTaskCompletionStatusList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGitlabProjectIssuesIssuesTaskCompletionStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectIssuesIssuesTaskCompletionStatusList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGitlabProjectIssuesIssuesTaskCompletionStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesTaskCompletionStatusList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesTaskCompletionStatusList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesTaskCompletionStatusList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGitlabProjectIssuesIssuesTaskCompletionStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProjectIssues.DataGitlabProjectIssuesIssuesTaskCompletionStatusOutputReference",
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
            type_hints = typing.get_type_hints(DataGitlabProjectIssuesIssuesTaskCompletionStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="completedCount")
    def completed_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "completedCount"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGitlabProjectIssuesIssuesTaskCompletionStatus]:
        return typing.cast(typing.Optional[DataGitlabProjectIssuesIssuesTaskCompletionStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGitlabProjectIssuesIssuesTaskCompletionStatus],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectIssuesIssuesTaskCompletionStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGitlabProjectIssues",
    "DataGitlabProjectIssuesConfig",
    "DataGitlabProjectIssuesIssues",
    "DataGitlabProjectIssuesIssuesList",
    "DataGitlabProjectIssuesIssuesOutputReference",
    "DataGitlabProjectIssuesIssuesTaskCompletionStatus",
    "DataGitlabProjectIssuesIssuesTaskCompletionStatusList",
    "DataGitlabProjectIssuesIssuesTaskCompletionStatusOutputReference",
]

publication.publish()
