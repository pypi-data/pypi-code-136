'''
# `gitlab_branch_protection`

Refer to the Terraform Registory for docs: [`gitlab_branch_protection`](https://www.terraform.io/docs/providers/gitlab/r/branch_protection).
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
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection gitlab_branch_protection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        branch: builtins.str,
        project: builtins.str,
        allowed_to_merge: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionAllowedToMerge", typing.Dict[str, typing.Any]]]]] = None,
        allowed_to_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionAllowedToPush", typing.Dict[str, typing.Any]]]]] = None,
        allowed_to_unprotect: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionAllowedToUnprotect", typing.Dict[str, typing.Any]]]]] = None,
        allow_force_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        code_owner_approval_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        merge_access_level: typing.Optional[builtins.str] = None,
        push_access_level: typing.Optional[builtins.str] = None,
        unprotect_access_level: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection gitlab_branch_protection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param branch: Name of the branch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#branch BranchProtection#branch}
        :param project: The id of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#project BranchProtection#project}
        :param allowed_to_merge: allowed_to_merge block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_merge BranchProtection#allowed_to_merge}
        :param allowed_to_push: allowed_to_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_push BranchProtection#allowed_to_push}
        :param allowed_to_unprotect: allowed_to_unprotect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_unprotect BranchProtection#allowed_to_unprotect}
        :param allow_force_push: Can be set to true to allow users with push access to force push. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allow_force_push BranchProtection#allow_force_push}
        :param code_owner_approval_required: Can be set to true to require code owner approval before merging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#code_owner_approval_required BranchProtection#code_owner_approval_required}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#id BranchProtection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param merge_access_level: Access levels allowed to merge. Valid values are: ``no one``, ``developer``, ``maintainer``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#merge_access_level BranchProtection#merge_access_level}
        :param push_access_level: Access levels allowed to push. Valid values are: ``no one``, ``developer``, ``maintainer``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#push_access_level BranchProtection#push_access_level}
        :param unprotect_access_level: Access levels allowed to unprotect. Valid values are: ``developer``, ``maintainer``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#unprotect_access_level BranchProtection#unprotect_access_level}
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
            branch=branch,
            project=project,
            allowed_to_merge=allowed_to_merge,
            allowed_to_push=allowed_to_push,
            allowed_to_unprotect=allowed_to_unprotect,
            allow_force_push=allow_force_push,
            code_owner_approval_required=code_owner_approval_required,
            id=id,
            merge_access_level=merge_access_level,
            push_access_level=push_access_level,
            unprotect_access_level=unprotect_access_level,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAllowedToMerge")
    def put_allowed_to_merge(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionAllowedToMerge", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtection.put_allowed_to_merge)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedToMerge", [value]))

    @jsii.member(jsii_name="putAllowedToPush")
    def put_allowed_to_push(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionAllowedToPush", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtection.put_allowed_to_push)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedToPush", [value]))

    @jsii.member(jsii_name="putAllowedToUnprotect")
    def put_allowed_to_unprotect(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BranchProtectionAllowedToUnprotect", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtection.put_allowed_to_unprotect)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedToUnprotect", [value]))

    @jsii.member(jsii_name="resetAllowedToMerge")
    def reset_allowed_to_merge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedToMerge", []))

    @jsii.member(jsii_name="resetAllowedToPush")
    def reset_allowed_to_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedToPush", []))

    @jsii.member(jsii_name="resetAllowedToUnprotect")
    def reset_allowed_to_unprotect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedToUnprotect", []))

    @jsii.member(jsii_name="resetAllowForcePush")
    def reset_allow_force_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowForcePush", []))

    @jsii.member(jsii_name="resetCodeOwnerApprovalRequired")
    def reset_code_owner_approval_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeOwnerApprovalRequired", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMergeAccessLevel")
    def reset_merge_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeAccessLevel", []))

    @jsii.member(jsii_name="resetPushAccessLevel")
    def reset_push_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushAccessLevel", []))

    @jsii.member(jsii_name="resetUnprotectAccessLevel")
    def reset_unprotect_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnprotectAccessLevel", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="allowedToMerge")
    def allowed_to_merge(self) -> "BranchProtectionAllowedToMergeList":
        return typing.cast("BranchProtectionAllowedToMergeList", jsii.get(self, "allowedToMerge"))

    @builtins.property
    @jsii.member(jsii_name="allowedToPush")
    def allowed_to_push(self) -> "BranchProtectionAllowedToPushList":
        return typing.cast("BranchProtectionAllowedToPushList", jsii.get(self, "allowedToPush"))

    @builtins.property
    @jsii.member(jsii_name="allowedToUnprotect")
    def allowed_to_unprotect(self) -> "BranchProtectionAllowedToUnprotectList":
        return typing.cast("BranchProtectionAllowedToUnprotectList", jsii.get(self, "allowedToUnprotect"))

    @builtins.property
    @jsii.member(jsii_name="branchProtectionId")
    def branch_protection_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "branchProtectionId"))

    @builtins.property
    @jsii.member(jsii_name="allowedToMergeInput")
    def allowed_to_merge_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionAllowedToMerge"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionAllowedToMerge"]]], jsii.get(self, "allowedToMergeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedToPushInput")
    def allowed_to_push_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionAllowedToPush"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionAllowedToPush"]]], jsii.get(self, "allowedToPushInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedToUnprotectInput")
    def allowed_to_unprotect_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionAllowedToUnprotect"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BranchProtectionAllowedToUnprotect"]]], jsii.get(self, "allowedToUnprotectInput"))

    @builtins.property
    @jsii.member(jsii_name="allowForcePushInput")
    def allow_force_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowForcePushInput"))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="codeOwnerApprovalRequiredInput")
    def code_owner_approval_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "codeOwnerApprovalRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeAccessLevelInput")
    def merge_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pushAccessLevelInput")
    def push_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pushAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="unprotectAccessLevelInput")
    def unprotect_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "unprotectAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="allowForcePush")
    def allow_force_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowForcePush"))

    @allow_force_push.setter
    def allow_force_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "allow_force_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowForcePush", value)

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="codeOwnerApprovalRequired")
    def code_owner_approval_required(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "codeOwnerApprovalRequired"))

    @code_owner_approval_required.setter
    def code_owner_approval_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "code_owner_approval_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeOwnerApprovalRequired", value)

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
    @jsii.member(jsii_name="mergeAccessLevel")
    def merge_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeAccessLevel"))

    @merge_access_level.setter
    def merge_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "merge_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="pushAccessLevel")
    def push_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pushAccessLevel"))

    @push_access_level.setter
    def push_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "push_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="unprotectAccessLevel")
    def unprotect_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "unprotectAccessLevel"))

    @unprotect_access_level.setter
    def unprotect_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtection, "unprotect_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unprotectAccessLevel", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToMerge",
    jsii_struct_bases=[],
    name_mapping={"group_id": "groupId", "user_id": "userId"},
)
class BranchProtectionAllowedToMerge:
    def __init__(
        self,
        *,
        group_id: typing.Optional[jsii.Number] = None,
        user_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_id: The ID of a GitLab group allowed to perform the relevant action. Mutually exclusive with ``user_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#group_id BranchProtection#group_id}
        :param user_id: The ID of a GitLab user allowed to perform the relevant action. Mutually exclusive with ``group_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#user_id BranchProtection#user_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionAllowedToMerge.__init__)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if group_id is not None:
            self._values["group_id"] = group_id
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def group_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of a GitLab group allowed to perform the relevant action. Mutually exclusive with ``user_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#group_id BranchProtection#group_id}
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of a GitLab user allowed to perform the relevant action. Mutually exclusive with ``group_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#user_id BranchProtection#user_id}
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchProtectionAllowedToMerge(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BranchProtectionAllowedToMergeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToMergeList",
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
            type_hints = typing.get_type_hints(BranchProtectionAllowedToMergeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BranchProtectionAllowedToMergeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionAllowedToMergeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BranchProtectionAllowedToMergeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToMergeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToMergeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToMergeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToMerge]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToMerge]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToMerge]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToMergeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BranchProtectionAllowedToMergeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToMergeOutputReference",
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
            type_hints = typing.get_type_hints(BranchProtectionAllowedToMergeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelDescription")
    def access_level_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevelDescription"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToMergeOutputReference, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToMergeOutputReference, "user_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BranchProtectionAllowedToMerge, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BranchProtectionAllowedToMerge, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BranchProtectionAllowedToMerge, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToMergeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToPush",
    jsii_struct_bases=[],
    name_mapping={"group_id": "groupId", "user_id": "userId"},
)
class BranchProtectionAllowedToPush:
    def __init__(
        self,
        *,
        group_id: typing.Optional[jsii.Number] = None,
        user_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_id: The ID of a GitLab group allowed to perform the relevant action. Mutually exclusive with ``user_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#group_id BranchProtection#group_id}
        :param user_id: The ID of a GitLab user allowed to perform the relevant action. Mutually exclusive with ``group_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#user_id BranchProtection#user_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionAllowedToPush.__init__)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if group_id is not None:
            self._values["group_id"] = group_id
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def group_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of a GitLab group allowed to perform the relevant action. Mutually exclusive with ``user_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#group_id BranchProtection#group_id}
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of a GitLab user allowed to perform the relevant action. Mutually exclusive with ``group_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#user_id BranchProtection#user_id}
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchProtectionAllowedToPush(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BranchProtectionAllowedToPushList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToPushList",
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
            type_hints = typing.get_type_hints(BranchProtectionAllowedToPushList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BranchProtectionAllowedToPushOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionAllowedToPushList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BranchProtectionAllowedToPushOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToPushList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToPushList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToPushList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToPush]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToPush]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToPush]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToPushList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BranchProtectionAllowedToPushOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToPushOutputReference",
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
            type_hints = typing.get_type_hints(BranchProtectionAllowedToPushOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelDescription")
    def access_level_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevelDescription"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToPushOutputReference, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToPushOutputReference, "user_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BranchProtectionAllowedToPush, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BranchProtectionAllowedToPush, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BranchProtectionAllowedToPush, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToPushOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToUnprotect",
    jsii_struct_bases=[],
    name_mapping={"group_id": "groupId", "user_id": "userId"},
)
class BranchProtectionAllowedToUnprotect:
    def __init__(
        self,
        *,
        group_id: typing.Optional[jsii.Number] = None,
        user_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param group_id: The ID of a GitLab group allowed to perform the relevant action. Mutually exclusive with ``user_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#group_id BranchProtection#group_id}
        :param user_id: The ID of a GitLab user allowed to perform the relevant action. Mutually exclusive with ``group_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#user_id BranchProtection#user_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionAllowedToUnprotect.__init__)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if group_id is not None:
            self._values["group_id"] = group_id
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def group_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of a GitLab group allowed to perform the relevant action. Mutually exclusive with ``user_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#group_id BranchProtection#group_id}
        '''
        result = self._values.get("group_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of a GitLab user allowed to perform the relevant action. Mutually exclusive with ``group_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#user_id BranchProtection#user_id}
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchProtectionAllowedToUnprotect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BranchProtectionAllowedToUnprotectList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToUnprotectList",
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
            type_hints = typing.get_type_hints(BranchProtectionAllowedToUnprotectList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BranchProtectionAllowedToUnprotectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BranchProtectionAllowedToUnprotectList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BranchProtectionAllowedToUnprotectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToUnprotectList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToUnprotectList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToUnprotectList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToUnprotect]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToUnprotect]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToUnprotect]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToUnprotectList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BranchProtectionAllowedToUnprotectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionAllowedToUnprotectOutputReference",
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
            type_hints = typing.get_type_hints(BranchProtectionAllowedToUnprotectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGroupId")
    def reset_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupId", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

    @builtins.property
    @jsii.member(jsii_name="accessLevel")
    def access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevel"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelDescription")
    def access_level_description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessLevelDescription"))

    @builtins.property
    @jsii.member(jsii_name="groupIdInput")
    def group_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToUnprotectOutputReference, "group_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToUnprotectOutputReference, "user_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BranchProtectionAllowedToUnprotect, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BranchProtectionAllowedToUnprotect, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BranchProtectionAllowedToUnprotect, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BranchProtectionAllowedToUnprotectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.branchProtection.BranchProtectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "branch": "branch",
        "project": "project",
        "allowed_to_merge": "allowedToMerge",
        "allowed_to_push": "allowedToPush",
        "allowed_to_unprotect": "allowedToUnprotect",
        "allow_force_push": "allowForcePush",
        "code_owner_approval_required": "codeOwnerApprovalRequired",
        "id": "id",
        "merge_access_level": "mergeAccessLevel",
        "push_access_level": "pushAccessLevel",
        "unprotect_access_level": "unprotectAccessLevel",
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
        branch: builtins.str,
        project: builtins.str,
        allowed_to_merge: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BranchProtectionAllowedToMerge, typing.Dict[str, typing.Any]]]]] = None,
        allowed_to_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BranchProtectionAllowedToPush, typing.Dict[str, typing.Any]]]]] = None,
        allowed_to_unprotect: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BranchProtectionAllowedToUnprotect, typing.Dict[str, typing.Any]]]]] = None,
        allow_force_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        code_owner_approval_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        merge_access_level: typing.Optional[builtins.str] = None,
        push_access_level: typing.Optional[builtins.str] = None,
        unprotect_access_level: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param branch: Name of the branch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#branch BranchProtection#branch}
        :param project: The id of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#project BranchProtection#project}
        :param allowed_to_merge: allowed_to_merge block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_merge BranchProtection#allowed_to_merge}
        :param allowed_to_push: allowed_to_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_push BranchProtection#allowed_to_push}
        :param allowed_to_unprotect: allowed_to_unprotect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_unprotect BranchProtection#allowed_to_unprotect}
        :param allow_force_push: Can be set to true to allow users with push access to force push. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allow_force_push BranchProtection#allow_force_push}
        :param code_owner_approval_required: Can be set to true to require code owner approval before merging. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#code_owner_approval_required BranchProtection#code_owner_approval_required}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#id BranchProtection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param merge_access_level: Access levels allowed to merge. Valid values are: ``no one``, ``developer``, ``maintainer``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#merge_access_level BranchProtection#merge_access_level}
        :param push_access_level: Access levels allowed to push. Valid values are: ``no one``, ``developer``, ``maintainer``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#push_access_level BranchProtection#push_access_level}
        :param unprotect_access_level: Access levels allowed to unprotect. Valid values are: ``developer``, ``maintainer``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#unprotect_access_level BranchProtection#unprotect_access_level}
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
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument allowed_to_merge", value=allowed_to_merge, expected_type=type_hints["allowed_to_merge"])
            check_type(argname="argument allowed_to_push", value=allowed_to_push, expected_type=type_hints["allowed_to_push"])
            check_type(argname="argument allowed_to_unprotect", value=allowed_to_unprotect, expected_type=type_hints["allowed_to_unprotect"])
            check_type(argname="argument allow_force_push", value=allow_force_push, expected_type=type_hints["allow_force_push"])
            check_type(argname="argument code_owner_approval_required", value=code_owner_approval_required, expected_type=type_hints["code_owner_approval_required"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument merge_access_level", value=merge_access_level, expected_type=type_hints["merge_access_level"])
            check_type(argname="argument push_access_level", value=push_access_level, expected_type=type_hints["push_access_level"])
            check_type(argname="argument unprotect_access_level", value=unprotect_access_level, expected_type=type_hints["unprotect_access_level"])
        self._values: typing.Dict[str, typing.Any] = {
            "branch": branch,
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
        if allowed_to_merge is not None:
            self._values["allowed_to_merge"] = allowed_to_merge
        if allowed_to_push is not None:
            self._values["allowed_to_push"] = allowed_to_push
        if allowed_to_unprotect is not None:
            self._values["allowed_to_unprotect"] = allowed_to_unprotect
        if allow_force_push is not None:
            self._values["allow_force_push"] = allow_force_push
        if code_owner_approval_required is not None:
            self._values["code_owner_approval_required"] = code_owner_approval_required
        if id is not None:
            self._values["id"] = id
        if merge_access_level is not None:
            self._values["merge_access_level"] = merge_access_level
        if push_access_level is not None:
            self._values["push_access_level"] = push_access_level
        if unprotect_access_level is not None:
            self._values["unprotect_access_level"] = unprotect_access_level

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
    def branch(self) -> builtins.str:
        '''Name of the branch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#branch BranchProtection#branch}
        '''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The id of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#project BranchProtection#project}
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_to_merge(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToMerge]]]:
        '''allowed_to_merge block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_merge BranchProtection#allowed_to_merge}
        '''
        result = self._values.get("allowed_to_merge")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToMerge]]], result)

    @builtins.property
    def allowed_to_push(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToPush]]]:
        '''allowed_to_push block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_push BranchProtection#allowed_to_push}
        '''
        result = self._values.get("allowed_to_push")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToPush]]], result)

    @builtins.property
    def allowed_to_unprotect(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToUnprotect]]]:
        '''allowed_to_unprotect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allowed_to_unprotect BranchProtection#allowed_to_unprotect}
        '''
        result = self._values.get("allowed_to_unprotect")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BranchProtectionAllowedToUnprotect]]], result)

    @builtins.property
    def allow_force_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Can be set to true to allow users with push access to force push.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#allow_force_push BranchProtection#allow_force_push}
        '''
        result = self._values.get("allow_force_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def code_owner_approval_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Can be set to true to require code owner approval before merging.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#code_owner_approval_required BranchProtection#code_owner_approval_required}
        '''
        result = self._values.get("code_owner_approval_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#id BranchProtection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_access_level(self) -> typing.Optional[builtins.str]:
        '''Access levels allowed to merge. Valid values are: ``no one``, ``developer``, ``maintainer``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#merge_access_level BranchProtection#merge_access_level}
        '''
        result = self._values.get("merge_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def push_access_level(self) -> typing.Optional[builtins.str]:
        '''Access levels allowed to push. Valid values are: ``no one``, ``developer``, ``maintainer``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#push_access_level BranchProtection#push_access_level}
        '''
        result = self._values.get("push_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def unprotect_access_level(self) -> typing.Optional[builtins.str]:
        '''Access levels allowed to unprotect. Valid values are: ``developer``, ``maintainer``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/branch_protection#unprotect_access_level BranchProtection#unprotect_access_level}
        '''
        result = self._values.get("unprotect_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchProtectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BranchProtection",
    "BranchProtectionAllowedToMerge",
    "BranchProtectionAllowedToMergeList",
    "BranchProtectionAllowedToMergeOutputReference",
    "BranchProtectionAllowedToPush",
    "BranchProtectionAllowedToPushList",
    "BranchProtectionAllowedToPushOutputReference",
    "BranchProtectionAllowedToUnprotect",
    "BranchProtectionAllowedToUnprotectList",
    "BranchProtectionAllowedToUnprotectOutputReference",
    "BranchProtectionConfig",
]

publication.publish()
