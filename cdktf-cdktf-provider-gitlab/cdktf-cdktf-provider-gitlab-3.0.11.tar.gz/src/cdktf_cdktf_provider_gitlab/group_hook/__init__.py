'''
# `gitlab_group_hook`

Refer to the Terraform Registory for docs: [`gitlab_group_hook`](https://www.terraform.io/docs/providers/gitlab/r/group_hook).
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


class GroupHook(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.groupHook.GroupHook",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook gitlab_group_hook}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        group: builtins.str,
        url: builtins.str,
        confidential_issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        deployment_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        job_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_events_branch_filter: typing.Optional[builtins.str] = None,
        releases_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subgroup_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        wiki_page_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook gitlab_group_hook} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group: The ID or full path of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#group GroupHook#group}
        :param url: The url of the hook to invoke. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#url GroupHook#url}
        :param confidential_issues_events: Invoke the hook for confidential issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#confidential_issues_events GroupHook#confidential_issues_events}
        :param confidential_note_events: Invoke the hook for confidential notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#confidential_note_events GroupHook#confidential_note_events}
        :param deployment_events: Invoke the hook for deployment events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#deployment_events GroupHook#deployment_events}
        :param enable_ssl_verification: Enable ssl verification when invoking the hook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#enable_ssl_verification GroupHook#enable_ssl_verification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#id GroupHook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issues_events: Invoke the hook for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#issues_events GroupHook#issues_events}
        :param job_events: Invoke the hook for job events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#job_events GroupHook#job_events}
        :param merge_requests_events: Invoke the hook for merge requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#merge_requests_events GroupHook#merge_requests_events}
        :param note_events: Invoke the hook for notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#note_events GroupHook#note_events}
        :param pipeline_events: Invoke the hook for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#pipeline_events GroupHook#pipeline_events}
        :param push_events: Invoke the hook for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#push_events GroupHook#push_events}
        :param push_events_branch_filter: Invoke the hook for push events on matching branches only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#push_events_branch_filter GroupHook#push_events_branch_filter}
        :param releases_events: Invoke the hook for releases events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#releases_events GroupHook#releases_events}
        :param subgroup_events: Invoke the hook for subgroup events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#subgroup_events GroupHook#subgroup_events}
        :param tag_push_events: Invoke the hook for tag push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#tag_push_events GroupHook#tag_push_events}
        :param token: A token to present when invoking the hook. The token is not available for imported resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#token GroupHook#token}
        :param wiki_page_events: Invoke the hook for wiki page events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#wiki_page_events GroupHook#wiki_page_events}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupHook.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupHookConfig(
            group=group,
            url=url,
            confidential_issues_events=confidential_issues_events,
            confidential_note_events=confidential_note_events,
            deployment_events=deployment_events,
            enable_ssl_verification=enable_ssl_verification,
            id=id,
            issues_events=issues_events,
            job_events=job_events,
            merge_requests_events=merge_requests_events,
            note_events=note_events,
            pipeline_events=pipeline_events,
            push_events=push_events,
            push_events_branch_filter=push_events_branch_filter,
            releases_events=releases_events,
            subgroup_events=subgroup_events,
            tag_push_events=tag_push_events,
            token=token,
            wiki_page_events=wiki_page_events,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetConfidentialIssuesEvents")
    def reset_confidential_issues_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialIssuesEvents", []))

    @jsii.member(jsii_name="resetConfidentialNoteEvents")
    def reset_confidential_note_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfidentialNoteEvents", []))

    @jsii.member(jsii_name="resetDeploymentEvents")
    def reset_deployment_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentEvents", []))

    @jsii.member(jsii_name="resetEnableSslVerification")
    def reset_enable_ssl_verification(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableSslVerification", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssuesEvents")
    def reset_issues_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuesEvents", []))

    @jsii.member(jsii_name="resetJobEvents")
    def reset_job_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobEvents", []))

    @jsii.member(jsii_name="resetMergeRequestsEvents")
    def reset_merge_requests_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsEvents", []))

    @jsii.member(jsii_name="resetNoteEvents")
    def reset_note_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoteEvents", []))

    @jsii.member(jsii_name="resetPipelineEvents")
    def reset_pipeline_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelineEvents", []))

    @jsii.member(jsii_name="resetPushEvents")
    def reset_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushEvents", []))

    @jsii.member(jsii_name="resetPushEventsBranchFilter")
    def reset_push_events_branch_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushEventsBranchFilter", []))

    @jsii.member(jsii_name="resetReleasesEvents")
    def reset_releases_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReleasesEvents", []))

    @jsii.member(jsii_name="resetSubgroupEvents")
    def reset_subgroup_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubgroupEvents", []))

    @jsii.member(jsii_name="resetTagPushEvents")
    def reset_tag_push_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagPushEvents", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetWikiPageEvents")
    def reset_wiki_page_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWikiPageEvents", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupId"))

    @builtins.property
    @jsii.member(jsii_name="hookId")
    def hook_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "hookId"))

    @builtins.property
    @jsii.member(jsii_name="confidentialIssuesEventsInput")
    def confidential_issues_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "confidentialIssuesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialNoteEventsInput")
    def confidential_note_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "confidentialNoteEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentEventsInput")
    def deployment_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deploymentEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableSslVerificationInput")
    def enable_ssl_verification_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableSslVerificationInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuesEventsInput")
    def issues_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "issuesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="jobEventsInput")
    def job_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "jobEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEventsInput")
    def merge_requests_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mergeRequestsEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="noteEventsInput")
    def note_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "noteEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelineEventsInput")
    def pipeline_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pipelineEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="pushEventsBranchFilterInput")
    def push_events_branch_filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pushEventsBranchFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="pushEventsInput")
    def push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="releasesEventsInput")
    def releases_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "releasesEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="subgroupEventsInput")
    def subgroup_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "subgroupEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagPushEventsInput")
    def tag_push_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tagPushEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="wikiPageEventsInput")
    def wiki_page_events_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "wikiPageEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="confidentialIssuesEvents")
    def confidential_issues_events(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "confidentialIssuesEvents"))

    @confidential_issues_events.setter
    def confidential_issues_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "confidential_issues_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidentialIssuesEvents", value)

    @builtins.property
    @jsii.member(jsii_name="confidentialNoteEvents")
    def confidential_note_events(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "confidentialNoteEvents"))

    @confidential_note_events.setter
    def confidential_note_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "confidential_note_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "confidentialNoteEvents", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentEvents")
    def deployment_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deploymentEvents"))

    @deployment_events.setter
    def deployment_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "deployment_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentEvents", value)

    @builtins.property
    @jsii.member(jsii_name="enableSslVerification")
    def enable_ssl_verification(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableSslVerification"))

    @enable_ssl_verification.setter
    def enable_ssl_verification(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "enable_ssl_verification").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSslVerification", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issuesEvents")
    def issues_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "issuesEvents"))

    @issues_events.setter
    def issues_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "issues_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuesEvents", value)

    @builtins.property
    @jsii.member(jsii_name="jobEvents")
    def job_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "jobEvents"))

    @job_events.setter
    def job_events(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "job_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobEvents", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEvents")
    def merge_requests_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mergeRequestsEvents"))

    @merge_requests_events.setter
    def merge_requests_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "merge_requests_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsEvents", value)

    @builtins.property
    @jsii.member(jsii_name="noteEvents")
    def note_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "noteEvents"))

    @note_events.setter
    def note_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "note_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noteEvents", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineEvents")
    def pipeline_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pipelineEvents"))

    @pipeline_events.setter
    def pipeline_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "pipeline_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineEvents", value)

    @builtins.property
    @jsii.member(jsii_name="pushEvents")
    def push_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pushEvents"))

    @push_events.setter
    def push_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "push_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="pushEventsBranchFilter")
    def push_events_branch_filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pushEventsBranchFilter"))

    @push_events_branch_filter.setter
    def push_events_branch_filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "push_events_branch_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pushEventsBranchFilter", value)

    @builtins.property
    @jsii.member(jsii_name="releasesEvents")
    def releases_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "releasesEvents"))

    @releases_events.setter
    def releases_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "releases_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releasesEvents", value)

    @builtins.property
    @jsii.member(jsii_name="subgroupEvents")
    def subgroup_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "subgroupEvents"))

    @subgroup_events.setter
    def subgroup_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "subgroup_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subgroupEvents", value)

    @builtins.property
    @jsii.member(jsii_name="tagPushEvents")
    def tag_push_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tagPushEvents"))

    @tag_push_events.setter
    def tag_push_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "tag_push_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagPushEvents", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="wikiPageEvents")
    def wiki_page_events(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "wikiPageEvents"))

    @wiki_page_events.setter
    def wiki_page_events(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupHook, "wiki_page_events").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wikiPageEvents", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.groupHook.GroupHookConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group": "group",
        "url": "url",
        "confidential_issues_events": "confidentialIssuesEvents",
        "confidential_note_events": "confidentialNoteEvents",
        "deployment_events": "deploymentEvents",
        "enable_ssl_verification": "enableSslVerification",
        "id": "id",
        "issues_events": "issuesEvents",
        "job_events": "jobEvents",
        "merge_requests_events": "mergeRequestsEvents",
        "note_events": "noteEvents",
        "pipeline_events": "pipelineEvents",
        "push_events": "pushEvents",
        "push_events_branch_filter": "pushEventsBranchFilter",
        "releases_events": "releasesEvents",
        "subgroup_events": "subgroupEvents",
        "tag_push_events": "tagPushEvents",
        "token": "token",
        "wiki_page_events": "wikiPageEvents",
    },
)
class GroupHookConfig(cdktf.TerraformMetaArguments):
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
        group: builtins.str,
        url: builtins.str,
        confidential_issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        confidential_note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        deployment_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_ssl_verification: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issues_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        job_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_requests_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        note_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pipeline_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_events_branch_filter: typing.Optional[builtins.str] = None,
        releases_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        subgroup_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag_push_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token: typing.Optional[builtins.str] = None,
        wiki_page_events: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group: The ID or full path of the group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#group GroupHook#group}
        :param url: The url of the hook to invoke. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#url GroupHook#url}
        :param confidential_issues_events: Invoke the hook for confidential issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#confidential_issues_events GroupHook#confidential_issues_events}
        :param confidential_note_events: Invoke the hook for confidential notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#confidential_note_events GroupHook#confidential_note_events}
        :param deployment_events: Invoke the hook for deployment events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#deployment_events GroupHook#deployment_events}
        :param enable_ssl_verification: Enable ssl verification when invoking the hook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#enable_ssl_verification GroupHook#enable_ssl_verification}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#id GroupHook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issues_events: Invoke the hook for issues events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#issues_events GroupHook#issues_events}
        :param job_events: Invoke the hook for job events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#job_events GroupHook#job_events}
        :param merge_requests_events: Invoke the hook for merge requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#merge_requests_events GroupHook#merge_requests_events}
        :param note_events: Invoke the hook for notes events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#note_events GroupHook#note_events}
        :param pipeline_events: Invoke the hook for pipeline events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#pipeline_events GroupHook#pipeline_events}
        :param push_events: Invoke the hook for push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#push_events GroupHook#push_events}
        :param push_events_branch_filter: Invoke the hook for push events on matching branches only. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#push_events_branch_filter GroupHook#push_events_branch_filter}
        :param releases_events: Invoke the hook for releases events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#releases_events GroupHook#releases_events}
        :param subgroup_events: Invoke the hook for subgroup events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#subgroup_events GroupHook#subgroup_events}
        :param tag_push_events: Invoke the hook for tag push events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#tag_push_events GroupHook#tag_push_events}
        :param token: A token to present when invoking the hook. The token is not available for imported resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#token GroupHook#token}
        :param wiki_page_events: Invoke the hook for wiki page events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#wiki_page_events GroupHook#wiki_page_events}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GroupHookConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument confidential_issues_events", value=confidential_issues_events, expected_type=type_hints["confidential_issues_events"])
            check_type(argname="argument confidential_note_events", value=confidential_note_events, expected_type=type_hints["confidential_note_events"])
            check_type(argname="argument deployment_events", value=deployment_events, expected_type=type_hints["deployment_events"])
            check_type(argname="argument enable_ssl_verification", value=enable_ssl_verification, expected_type=type_hints["enable_ssl_verification"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issues_events", value=issues_events, expected_type=type_hints["issues_events"])
            check_type(argname="argument job_events", value=job_events, expected_type=type_hints["job_events"])
            check_type(argname="argument merge_requests_events", value=merge_requests_events, expected_type=type_hints["merge_requests_events"])
            check_type(argname="argument note_events", value=note_events, expected_type=type_hints["note_events"])
            check_type(argname="argument pipeline_events", value=pipeline_events, expected_type=type_hints["pipeline_events"])
            check_type(argname="argument push_events", value=push_events, expected_type=type_hints["push_events"])
            check_type(argname="argument push_events_branch_filter", value=push_events_branch_filter, expected_type=type_hints["push_events_branch_filter"])
            check_type(argname="argument releases_events", value=releases_events, expected_type=type_hints["releases_events"])
            check_type(argname="argument subgroup_events", value=subgroup_events, expected_type=type_hints["subgroup_events"])
            check_type(argname="argument tag_push_events", value=tag_push_events, expected_type=type_hints["tag_push_events"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument wiki_page_events", value=wiki_page_events, expected_type=type_hints["wiki_page_events"])
        self._values: typing.Dict[str, typing.Any] = {
            "group": group,
            "url": url,
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
        if confidential_issues_events is not None:
            self._values["confidential_issues_events"] = confidential_issues_events
        if confidential_note_events is not None:
            self._values["confidential_note_events"] = confidential_note_events
        if deployment_events is not None:
            self._values["deployment_events"] = deployment_events
        if enable_ssl_verification is not None:
            self._values["enable_ssl_verification"] = enable_ssl_verification
        if id is not None:
            self._values["id"] = id
        if issues_events is not None:
            self._values["issues_events"] = issues_events
        if job_events is not None:
            self._values["job_events"] = job_events
        if merge_requests_events is not None:
            self._values["merge_requests_events"] = merge_requests_events
        if note_events is not None:
            self._values["note_events"] = note_events
        if pipeline_events is not None:
            self._values["pipeline_events"] = pipeline_events
        if push_events is not None:
            self._values["push_events"] = push_events
        if push_events_branch_filter is not None:
            self._values["push_events_branch_filter"] = push_events_branch_filter
        if releases_events is not None:
            self._values["releases_events"] = releases_events
        if subgroup_events is not None:
            self._values["subgroup_events"] = subgroup_events
        if tag_push_events is not None:
            self._values["tag_push_events"] = tag_push_events
        if token is not None:
            self._values["token"] = token
        if wiki_page_events is not None:
            self._values["wiki_page_events"] = wiki_page_events

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
    def group(self) -> builtins.str:
        '''The ID or full path of the group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#group GroupHook#group}
        '''
        result = self._values.get("group")
        assert result is not None, "Required property 'group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The url of the hook to invoke.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#url GroupHook#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def confidential_issues_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for confidential issues events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#confidential_issues_events GroupHook#confidential_issues_events}
        '''
        result = self._values.get("confidential_issues_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def confidential_note_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for confidential notes events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#confidential_note_events GroupHook#confidential_note_events}
        '''
        result = self._values.get("confidential_note_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def deployment_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for deployment events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#deployment_events GroupHook#deployment_events}
        '''
        result = self._values.get("deployment_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_ssl_verification(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable ssl verification when invoking the hook.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#enable_ssl_verification GroupHook#enable_ssl_verification}
        '''
        result = self._values.get("enable_ssl_verification")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#id GroupHook#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issues_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for issues events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#issues_events GroupHook#issues_events}
        '''
        result = self._values.get("issues_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def job_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for job events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#job_events GroupHook#job_events}
        '''
        result = self._values.get("job_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def merge_requests_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for merge requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#merge_requests_events GroupHook#merge_requests_events}
        '''
        result = self._values.get("merge_requests_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def note_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for notes events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#note_events GroupHook#note_events}
        '''
        result = self._values.get("note_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pipeline_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for pipeline events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#pipeline_events GroupHook#pipeline_events}
        '''
        result = self._values.get("pipeline_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#push_events GroupHook#push_events}
        '''
        result = self._values.get("push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def push_events_branch_filter(self) -> typing.Optional[builtins.str]:
        '''Invoke the hook for push events on matching branches only.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#push_events_branch_filter GroupHook#push_events_branch_filter}
        '''
        result = self._values.get("push_events_branch_filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def releases_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for releases events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#releases_events GroupHook#releases_events}
        '''
        result = self._values.get("releases_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def subgroup_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for subgroup events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#subgroup_events GroupHook#subgroup_events}
        '''
        result = self._values.get("subgroup_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag_push_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for tag push events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#tag_push_events GroupHook#tag_push_events}
        '''
        result = self._values.get("tag_push_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''A token to present when invoking the hook. The token is not available for imported resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#token GroupHook#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wiki_page_events(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Invoke the hook for wiki page events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_hook#wiki_page_events GroupHook#wiki_page_events}
        '''
        result = self._values.get("wiki_page_events")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupHookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GroupHook",
    "GroupHookConfig",
]

publication.publish()
