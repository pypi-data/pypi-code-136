'''
# `github_branch_protection`

Refer to the Terraform Registory for docs: [`github_branch_protection`](https://www.terraform.io/docs/providers/github/r/branch_protection).
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


class BranchProtection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/branch_protection github_branch_protection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        pattern: builtins.str,
        repository_id: builtins.str,
        allows_deletions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allows_force_pushes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        blocks_creations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforce_admins: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        push_restrictions: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_conversation_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required_linear_history: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required_pull_request_reviews: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionRequiredPullRequestReviews", typing.Dict[str, typing.Any]]]]] = None,
        required_status_checks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionRequiredStatusChecks", typing.Dict[str, typing.Any]]]]] = None,
        require_signed_commits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/branch_protection github_branch_protection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#pattern BranchProtection#pattern}.
        :param repository_id: Node ID or name of repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#repository_id BranchProtection#repository_id}
        :param allows_deletions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#allows_deletions BranchProtection#allows_deletions}.
        :param allows_force_pushes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#allows_force_pushes BranchProtection#allows_force_pushes}.
        :param blocks_creations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#blocks_creations BranchProtection#blocks_creations}.
        :param enforce_admins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#enforce_admins BranchProtection#enforce_admins}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#id BranchProtection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param push_restrictions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#push_restrictions BranchProtection#push_restrictions}.
        :param require_conversation_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_conversation_resolution BranchProtection#require_conversation_resolution}.
        :param required_linear_history: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_linear_history BranchProtection#required_linear_history}.
        :param required_pull_request_reviews: required_pull_request_reviews block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_pull_request_reviews BranchProtection#required_pull_request_reviews}
        :param required_status_checks: required_status_checks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_status_checks BranchProtection#required_status_checks}
        :param require_signed_commits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_signed_commits BranchProtection#require_signed_commits}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BranchProtectionConfig(
            pattern=pattern,
            repository_id=repository_id,
            allows_deletions=allows_deletions,
            allows_force_pushes=allows_force_pushes,
            blocks_creations=blocks_creations,
            enforce_admins=enforce_admins,
            id=id,
            push_restrictions=push_restrictions,
            require_conversation_resolution=require_conversation_resolution,
            required_linear_history=required_linear_history,
            required_pull_request_reviews=required_pull_request_reviews,
            required_status_checks=required_status_checks,
            require_signed_commits=require_signed_commits,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRequiredPullRequestReviews")
    def put_required_pull_request_reviews(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionRequiredPullRequestReviews", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtection.put_required_pull_request_reviews)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequiredPullRequestReviews", [value]))

    @jsii.member(jsii_name="putRequiredStatusChecks")
    def put_required_status_checks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionRequiredStatusChecks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtection.put_required_status_checks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRequiredStatusChecks", [value]))

    @jsii.member(jsii_name="resetAllowsDeletions")
    def reset_allows_deletions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowsDeletions", []))

    @jsii.member(jsii_name="resetAllowsForcePushes")
    def reset_allows_force_pushes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowsForcePushes", []))

    @jsii.member(jsii_name="resetBlocksCreations")
    def reset_blocks_creations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlocksCreations", []))

    @jsii.member(jsii_name="resetEnforceAdmins")
    def reset_enforce_admins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforceAdmins", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPushRestrictions")
    def reset_push_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushRestrictions", []))

    @jsii.member(jsii_name="resetRequireConversationResolution")
    def reset_require_conversation_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireConversationResolution", []))

    @jsii.member(jsii_name="resetRequiredLinearHistory")
    def reset_required_linear_history(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredLinearHistory", []))

    @jsii.member(jsii_name="resetRequiredPullRequestReviews")
    def reset_required_pull_request_reviews(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredPullRequestReviews", []))

    @jsii.member(jsii_name="resetRequiredStatusChecks")
    def reset_required_status_checks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredStatusChecks", []))

    @jsii.member(jsii_name="resetRequireSignedCommits")
    def reset_require_signed_commits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireSignedCommits", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="requiredPullRequestReviews")
    def required_pull_request_reviews(
        self,
    ) -> "BranchProtectionRequiredPullRequestReviewsList":
        return typing.cast("BranchProtectionRequiredPullRequestReviewsList", jsii.get(self, "requiredPullRequestReviews"))

    @builtins.property
    @jsii.member(jsii_name="requiredStatusChecks")
    def required_status_checks(self) -> "BranchProtectionRequiredStatusChecksList":
        return typing.cast("BranchProtectionRequiredStatusChecksList", jsii.get(self, "requiredStatusChecks"))

    @builtins.property
    @jsii.member(jsii_name="allowsDeletionsInput")
    def allows_deletions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowsDeletionsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowsForcePushesInput")
    def allows_force_pushes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowsForcePushesInput"))

    @builtins.property
    @jsii.member(jsii_name="blocksCreationsInput")
    def blocks_creations_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blocksCreationsInput"))

    @builtins.property
    @jsii.member(jsii_name="enforceAdminsInput")
    def enforce_admins_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enforceAdminsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="patternInput")
    def pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "patternInput"))

    @builtins.property
    @jsii.member(jsii_name="pushRestrictionsInput")
    def push_restrictions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pushRestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryIdInput")
    def repository_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="requireConversationResolutionInput")
    def require_conversation_resolution_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireConversationResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredLinearHistoryInput")
    def required_linear_history_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requiredLinearHistoryInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredPullRequestReviewsInput")
    def required_pull_request_reviews_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredPullRequestReviews"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredPullRequestReviews"]]], jsii.get(self, "requiredPullRequestReviewsInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredStatusChecksInput")
    def required_status_checks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredStatusChecks"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredStatusChecks"]]], jsii.get(self, "requiredStatusChecksInput"))

    @builtins.property
    @jsii.member(jsii_name="requireSignedCommitsInput")
    def require_signed_commits_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireSignedCommitsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowsDeletions")
    def allows_deletions(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowsDeletions"))

    @allows_deletions.setter
    def allows_deletions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "allows_deletions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowsDeletions", value)

    @builtins.property
    @jsii.member(jsii_name="allowsForcePushes")
    def allows_force_pushes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowsForcePushes"))

    @allows_force_pushes.setter
    def allows_force_pushes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "allows_force_pushes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowsForcePushes", value)

    @builtins.property
    @jsii.member(jsii_name="blocksCreations")
    def blocks_creations(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blocksCreations"))

    @blocks_creations.setter
    def blocks_creations(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "blocks_creations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blocksCreations", value)

    @builtins.property
    @jsii.member(jsii_name="enforceAdmins")
    def enforce_admins(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enforceAdmins"))

    @enforce_admins.setter
    def enforce_admins(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "enforce_admins").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforceAdmins", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="pushRestrictions")
    def push_restrictions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pushRestrictions"))

    @push_restrictions.setter
    def push_restrictions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "push_restrictions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushRestrictions", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryId")
    def repository_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryId"))

    @repository_id.setter
    def repository_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "repository_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryId", value)

    @builtins.property
    @jsii.member(jsii_name="requireConversationResolution")
    def require_conversation_resolution(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireConversationResolution"))

    @require_conversation_resolution.setter
    def require_conversation_resolution(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "require_conversation_resolution").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireConversationResolution", value)

    @builtins.property
    @jsii.member(jsii_name="requiredLinearHistory")
    def required_linear_history(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requiredLinearHistory"))

    @required_linear_history.setter
    def required_linear_history(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "required_linear_history").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredLinearHistory", value)

    @builtins.property
    @jsii.member(jsii_name="requireSignedCommits")
    def require_signed_commits(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireSignedCommits"))

    @require_signed_commits.setter
    def require_signed_commits(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "require_signed_commits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireSignedCommits", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "pattern": "pattern",
        "repository_id": "repositoryId",
        "allows_deletions": "allowsDeletions",
        "allows_force_pushes": "allowsForcePushes",
        "blocks_creations": "blocksCreations",
        "enforce_admins": "enforceAdmins",
        "id": "id",
        "push_restrictions": "pushRestrictions",
        "require_conversation_resolution": "requireConversationResolution",
        "required_linear_history": "requiredLinearHistory",
        "required_pull_request_reviews": "requiredPullRequestReviews",
        "required_status_checks": "requiredStatusChecks",
        "require_signed_commits": "requireSignedCommits",
    },
)
class BranchProtectionConfig(cdktf.TerraformMetaArguments):
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
        pattern: builtins.str,
        repository_id: builtins.str,
        allows_deletions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allows_force_pushes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        blocks_creations: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enforce_admins: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        push_restrictions: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_conversation_resolution: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required_linear_history: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required_pull_request_reviews: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionRequiredPullRequestReviews", typing.Dict[str, typing.Any]]]]] = None,
        required_status_checks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionRequiredStatusChecks", typing.Dict[str, typing.Any]]]]] = None,
        require_signed_commits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#pattern BranchProtection#pattern}.
        :param repository_id: Node ID or name of repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#repository_id BranchProtection#repository_id}
        :param allows_deletions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#allows_deletions BranchProtection#allows_deletions}.
        :param allows_force_pushes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#allows_force_pushes BranchProtection#allows_force_pushes}.
        :param blocks_creations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#blocks_creations BranchProtection#blocks_creations}.
        :param enforce_admins: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#enforce_admins BranchProtection#enforce_admins}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#id BranchProtection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param push_restrictions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#push_restrictions BranchProtection#push_restrictions}.
        :param require_conversation_resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_conversation_resolution BranchProtection#require_conversation_resolution}.
        :param required_linear_history: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_linear_history BranchProtection#required_linear_history}.
        :param required_pull_request_reviews: required_pull_request_reviews block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_pull_request_reviews BranchProtection#required_pull_request_reviews}
        :param required_status_checks: required_status_checks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_status_checks BranchProtection#required_status_checks}
        :param require_signed_commits: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_signed_commits BranchProtection#require_signed_commits}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument repository_id", value=repository_id, expected_type=type_hints["repository_id"])
            check_type(argname="argument allows_deletions", value=allows_deletions, expected_type=type_hints["allows_deletions"])
            check_type(argname="argument allows_force_pushes", value=allows_force_pushes, expected_type=type_hints["allows_force_pushes"])
            check_type(argname="argument blocks_creations", value=blocks_creations, expected_type=type_hints["blocks_creations"])
            check_type(argname="argument enforce_admins", value=enforce_admins, expected_type=type_hints["enforce_admins"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument push_restrictions", value=push_restrictions, expected_type=type_hints["push_restrictions"])
            check_type(argname="argument require_conversation_resolution", value=require_conversation_resolution, expected_type=type_hints["require_conversation_resolution"])
            check_type(argname="argument required_linear_history", value=required_linear_history, expected_type=type_hints["required_linear_history"])
            check_type(argname="argument required_pull_request_reviews", value=required_pull_request_reviews, expected_type=type_hints["required_pull_request_reviews"])
            check_type(argname="argument required_status_checks", value=required_status_checks, expected_type=type_hints["required_status_checks"])
            check_type(argname="argument require_signed_commits", value=require_signed_commits, expected_type=type_hints["require_signed_commits"])
        self._values: typing.Dict[str, typing.Any] = {
            "pattern": pattern,
            "repository_id": repository_id,
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
        if allows_deletions is not None:
            self._values["allows_deletions"] = allows_deletions
        if allows_force_pushes is not None:
            self._values["allows_force_pushes"] = allows_force_pushes
        if blocks_creations is not None:
            self._values["blocks_creations"] = blocks_creations
        if enforce_admins is not None:
            self._values["enforce_admins"] = enforce_admins
        if id is not None:
            self._values["id"] = id
        if push_restrictions is not None:
            self._values["push_restrictions"] = push_restrictions
        if require_conversation_resolution is not None:
            self._values["require_conversation_resolution"] = require_conversation_resolution
        if required_linear_history is not None:
            self._values["required_linear_history"] = required_linear_history
        if required_pull_request_reviews is not None:
            self._values["required_pull_request_reviews"] = required_pull_request_reviews
        if required_status_checks is not None:
            self._values["required_status_checks"] = required_status_checks
        if require_signed_commits is not None:
            self._values["require_signed_commits"] = require_signed_commits

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
    def pattern(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#pattern BranchProtection#pattern}.'''
        result = self._values.get("pattern")
        assert result is not None, "Required property 'pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_id(self) -> builtins.str:
        '''Node ID or name of repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#repository_id BranchProtection#repository_id}
        '''
        result = self._values.get("repository_id")
        assert result is not None, "Required property 'repository_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allows_deletions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#allows_deletions BranchProtection#allows_deletions}.'''
        result = self._values.get("allows_deletions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allows_force_pushes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#allows_force_pushes BranchProtection#allows_force_pushes}.'''
        result = self._values.get("allows_force_pushes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def blocks_creations(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#blocks_creations BranchProtection#blocks_creations}.'''
        result = self._values.get("blocks_creations")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enforce_admins(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#enforce_admins BranchProtection#enforce_admins}.'''
        result = self._values.get("enforce_admins")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#id BranchProtection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def push_restrictions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#push_restrictions BranchProtection#push_restrictions}.'''
        result = self._values.get("push_restrictions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def require_conversation_resolution(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_conversation_resolution BranchProtection#require_conversation_resolution}.'''
        result = self._values.get("require_conversation_resolution")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def required_linear_history(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_linear_history BranchProtection#required_linear_history}.'''
        result = self._values.get("required_linear_history")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def required_pull_request_reviews(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredPullRequestReviews"]]]:
        '''required_pull_request_reviews block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_pull_request_reviews BranchProtection#required_pull_request_reviews}
        '''
        result = self._values.get("required_pull_request_reviews")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredPullRequestReviews"]]], result)

    @builtins.property
    def required_status_checks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredStatusChecks"]]]:
        '''required_status_checks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_status_checks BranchProtection#required_status_checks}
        '''
        result = self._values.get("required_status_checks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionRequiredStatusChecks"]]], result)

    @builtins.property
    def require_signed_commits(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_signed_commits BranchProtection#require_signed_commits}.'''
        result = self._values.get("require_signed_commits")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchProtectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtectionRequiredPullRequestReviews",
    jsii_struct_bases=[],
    name_mapping={
        "dismissal_restrictions": "dismissalRestrictions",
        "dismiss_stale_reviews": "dismissStaleReviews",
        "pull_request_bypassers": "pullRequestBypassers",
        "require_code_owner_reviews": "requireCodeOwnerReviews",
        "required_approving_review_count": "requiredApprovingReviewCount",
        "restrict_dismissals": "restrictDismissals",
    },
)
class BranchProtectionRequiredPullRequestReviews:
    def __init__(
        self,
        *,
        dismissal_restrictions: typing.Optional[typing.Sequence[builtins.str]] = None,
        dismiss_stale_reviews: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pull_request_bypassers: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_code_owner_reviews: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required_approving_review_count: typing.Optional[jsii.Number] = None,
        restrict_dismissals: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param dismissal_restrictions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#dismissal_restrictions BranchProtection#dismissal_restrictions}.
        :param dismiss_stale_reviews: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#dismiss_stale_reviews BranchProtection#dismiss_stale_reviews}.
        :param pull_request_bypassers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#pull_request_bypassers BranchProtection#pull_request_bypassers}.
        :param require_code_owner_reviews: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_code_owner_reviews BranchProtection#require_code_owner_reviews}.
        :param required_approving_review_count: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_approving_review_count BranchProtection#required_approving_review_count}.
        :param restrict_dismissals: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#restrict_dismissals BranchProtection#restrict_dismissals}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionRequiredPullRequestReviews.__init__)
            check_type(argname="argument dismissal_restrictions", value=dismissal_restrictions, expected_type=type_hints["dismissal_restrictions"])
            check_type(argname="argument dismiss_stale_reviews", value=dismiss_stale_reviews, expected_type=type_hints["dismiss_stale_reviews"])
            check_type(argname="argument pull_request_bypassers", value=pull_request_bypassers, expected_type=type_hints["pull_request_bypassers"])
            check_type(argname="argument require_code_owner_reviews", value=require_code_owner_reviews, expected_type=type_hints["require_code_owner_reviews"])
            check_type(argname="argument required_approving_review_count", value=required_approving_review_count, expected_type=type_hints["required_approving_review_count"])
            check_type(argname="argument restrict_dismissals", value=restrict_dismissals, expected_type=type_hints["restrict_dismissals"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dismissal_restrictions is not None:
            self._values["dismissal_restrictions"] = dismissal_restrictions
        if dismiss_stale_reviews is not None:
            self._values["dismiss_stale_reviews"] = dismiss_stale_reviews
        if pull_request_bypassers is not None:
            self._values["pull_request_bypassers"] = pull_request_bypassers
        if require_code_owner_reviews is not None:
            self._values["require_code_owner_reviews"] = require_code_owner_reviews
        if required_approving_review_count is not None:
            self._values["required_approving_review_count"] = required_approving_review_count
        if restrict_dismissals is not None:
            self._values["restrict_dismissals"] = restrict_dismissals

    @builtins.property
    def dismissal_restrictions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#dismissal_restrictions BranchProtection#dismissal_restrictions}.'''
        result = self._values.get("dismissal_restrictions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dismiss_stale_reviews(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#dismiss_stale_reviews BranchProtection#dismiss_stale_reviews}.'''
        result = self._values.get("dismiss_stale_reviews")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pull_request_bypassers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#pull_request_bypassers BranchProtection#pull_request_bypassers}.'''
        result = self._values.get("pull_request_bypassers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def require_code_owner_reviews(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#require_code_owner_reviews BranchProtection#require_code_owner_reviews}.'''
        result = self._values.get("require_code_owner_reviews")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def required_approving_review_count(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#required_approving_review_count BranchProtection#required_approving_review_count}.'''
        result = self._values.get("required_approving_review_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def restrict_dismissals(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#restrict_dismissals BranchProtection#restrict_dismissals}.'''
        result = self._values.get("restrict_dismissals")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchProtectionRequiredPullRequestReviews(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BranchProtectionRequiredPullRequestReviewsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtectionRequiredPullRequestReviewsList",
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
            type_hints = typing.get_type_hints(BranchProtectionRequiredPullRequestReviewsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BranchProtectionRequiredPullRequestReviewsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionRequiredPullRequestReviewsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BranchProtectionRequiredPullRequestReviewsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionRequiredPullRequestReviews]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionRequiredPullRequestReviews]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionRequiredPullRequestReviews]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BranchProtectionRequiredPullRequestReviewsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtectionRequiredPullRequestReviewsOutputReference",
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
            type_hints = typing.get_type_hints(BranchProtectionRequiredPullRequestReviewsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDismissalRestrictions")
    def reset_dismissal_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDismissalRestrictions", []))

    @jsii.member(jsii_name="resetDismissStaleReviews")
    def reset_dismiss_stale_reviews(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDismissStaleReviews", []))

    @jsii.member(jsii_name="resetPullRequestBypassers")
    def reset_pull_request_bypassers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPullRequestBypassers", []))

    @jsii.member(jsii_name="resetRequireCodeOwnerReviews")
    def reset_require_code_owner_reviews(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireCodeOwnerReviews", []))

    @jsii.member(jsii_name="resetRequiredApprovingReviewCount")
    def reset_required_approving_review_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredApprovingReviewCount", []))

    @jsii.member(jsii_name="resetRestrictDismissals")
    def reset_restrict_dismissals(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictDismissals", []))

    @builtins.property
    @jsii.member(jsii_name="dismissalRestrictionsInput")
    def dismissal_restrictions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dismissalRestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="dismissStaleReviewsInput")
    def dismiss_stale_reviews_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dismissStaleReviewsInput"))

    @builtins.property
    @jsii.member(jsii_name="pullRequestBypassersInput")
    def pull_request_bypassers_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pullRequestBypassersInput"))

    @builtins.property
    @jsii.member(jsii_name="requireCodeOwnerReviewsInput")
    def require_code_owner_reviews_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireCodeOwnerReviewsInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredApprovingReviewCountInput")
    def required_approving_review_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "requiredApprovingReviewCountInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictDismissalsInput")
    def restrict_dismissals_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "restrictDismissalsInput"))

    @builtins.property
    @jsii.member(jsii_name="dismissalRestrictions")
    def dismissal_restrictions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dismissalRestrictions"))

    @dismissal_restrictions.setter
    def dismissal_restrictions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsOutputReference, "dismissal_restrictions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dismissalRestrictions", value)

    @builtins.property
    @jsii.member(jsii_name="dismissStaleReviews")
    def dismiss_stale_reviews(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dismissStaleReviews"))

    @dismiss_stale_reviews.setter
    def dismiss_stale_reviews(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsOutputReference, "dismiss_stale_reviews").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dismissStaleReviews", value)

    @builtins.property
    @jsii.member(jsii_name="pullRequestBypassers")
    def pull_request_bypassers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pullRequestBypassers"))

    @pull_request_bypassers.setter
    def pull_request_bypassers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsOutputReference, "pull_request_bypassers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pullRequestBypassers", value)

    @builtins.property
    @jsii.member(jsii_name="requireCodeOwnerReviews")
    def require_code_owner_reviews(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireCodeOwnerReviews"))

    @require_code_owner_reviews.setter
    def require_code_owner_reviews(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsOutputReference, "require_code_owner_reviews").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireCodeOwnerReviews", value)

    @builtins.property
    @jsii.member(jsii_name="requiredApprovingReviewCount")
    def required_approving_review_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "requiredApprovingReviewCount"))

    @required_approving_review_count.setter
    def required_approving_review_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsOutputReference, "required_approving_review_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredApprovingReviewCount", value)

    @builtins.property
    @jsii.member(jsii_name="restrictDismissals")
    def restrict_dismissals(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "restrictDismissals"))

    @restrict_dismissals.setter
    def restrict_dismissals(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsOutputReference, "restrict_dismissals").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restrictDismissals", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BranchProtectionRequiredPullRequestReviews, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BranchProtectionRequiredPullRequestReviews, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BranchProtectionRequiredPullRequestReviews, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredPullRequestReviewsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtectionRequiredStatusChecks",
    jsii_struct_bases=[],
    name_mapping={"contexts": "contexts", "strict": "strict"},
)
class BranchProtectionRequiredStatusChecks:
    def __init__(
        self,
        *,
        contexts: typing.Optional[typing.Sequence[builtins.str]] = None,
        strict: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param contexts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#contexts BranchProtection#contexts}.
        :param strict: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#strict BranchProtection#strict}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionRequiredStatusChecks.__init__)
            check_type(argname="argument contexts", value=contexts, expected_type=type_hints["contexts"])
            check_type(argname="argument strict", value=strict, expected_type=type_hints["strict"])
        self._values: typing.Dict[str, typing.Any] = {}
        if contexts is not None:
            self._values["contexts"] = contexts
        if strict is not None:
            self._values["strict"] = strict

    @builtins.property
    def contexts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#contexts BranchProtection#contexts}.'''
        result = self._values.get("contexts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def strict(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/branch_protection#strict BranchProtection#strict}.'''
        result = self._values.get("strict")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchProtectionRequiredStatusChecks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BranchProtectionRequiredStatusChecksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtectionRequiredStatusChecksList",
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
            type_hints = typing.get_type_hints(BranchProtectionRequiredStatusChecksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BranchProtectionRequiredStatusChecksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionRequiredStatusChecksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BranchProtectionRequiredStatusChecksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredStatusChecksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredStatusChecksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredStatusChecksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionRequiredStatusChecks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionRequiredStatusChecks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionRequiredStatusChecks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredStatusChecksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BranchProtectionRequiredStatusChecksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.branchProtection.BranchProtectionRequiredStatusChecksOutputReference",
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
            type_hints = typing.get_type_hints(BranchProtectionRequiredStatusChecksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetContexts")
    def reset_contexts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContexts", []))

    @jsii.member(jsii_name="resetStrict")
    def reset_strict(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStrict", []))

    @builtins.property
    @jsii.member(jsii_name="contextsInput")
    def contexts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "contextsInput"))

    @builtins.property
    @jsii.member(jsii_name="strictInput")
    def strict_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "strictInput"))

    @builtins.property
    @jsii.member(jsii_name="contexts")
    def contexts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "contexts"))

    @contexts.setter
    def contexts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredStatusChecksOutputReference, "contexts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contexts", value)

    @builtins.property
    @jsii.member(jsii_name="strict")
    def strict(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "strict"))

    @strict.setter
    def strict(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredStatusChecksOutputReference, "strict").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "strict", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BranchProtectionRequiredStatusChecks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BranchProtectionRequiredStatusChecks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BranchProtectionRequiredStatusChecks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionRequiredStatusChecksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BranchProtection",
    "BranchProtectionConfig",
    "BranchProtectionRequiredPullRequestReviews",
    "BranchProtectionRequiredPullRequestReviewsList",
    "BranchProtectionRequiredPullRequestReviewsOutputReference",
    "BranchProtectionRequiredStatusChecks",
    "BranchProtectionRequiredStatusChecksList",
    "BranchProtectionRequiredStatusChecksOutputReference",
]

publication.publish()
