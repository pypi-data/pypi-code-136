'''
# `data_gitlab_project`

Refer to the Terraform Registory for docs: [`data_gitlab_project`](https://www.terraform.io/docs/providers/gitlab/d/project).
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


class DataGitlabProject(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProject",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/d/project gitlab_project}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        ci_default_git_depth: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        path_with_namespace: typing.Optional[builtins.str] = None,
        public_builds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/d/project gitlab_project} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param ci_default_git_depth: Default number of revisions for shallow cloning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#ci_default_git_depth DataGitlabProject#ci_default_git_depth}
        :param id: The integer or path with namespace that uniquely identifies the project within the gitlab install. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#id DataGitlabProject#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_with_namespace: The path of the repository with namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#path_with_namespace DataGitlabProject#path_with_namespace}
        :param public_builds: If true, jobs can be viewed by non-project members. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#public_builds DataGitlabProject#public_builds}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProject.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataGitlabProjectConfig(
            ci_default_git_depth=ci_default_git_depth,
            id=id,
            path_with_namespace=path_with_namespace,
            public_builds=public_builds,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCiDefaultGitDepth")
    def reset_ci_default_git_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCiDefaultGitDepth", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPathWithNamespace")
    def reset_path_with_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPathWithNamespace", []))

    @jsii.member(jsii_name="resetPublicBuilds")
    def reset_public_builds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicBuilds", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="analyticsAccessLevel")
    def analytics_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "analyticsAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="archived")
    def archived(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "archived"))

    @builtins.property
    @jsii.member(jsii_name="autoCancelPendingPipelines")
    def auto_cancel_pending_pipelines(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoCancelPendingPipelines"))

    @builtins.property
    @jsii.member(jsii_name="autocloseReferencedIssues")
    def autoclose_referenced_issues(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "autocloseReferencedIssues"))

    @builtins.property
    @jsii.member(jsii_name="autoDevopsDeployStrategy")
    def auto_devops_deploy_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoDevopsDeployStrategy"))

    @builtins.property
    @jsii.member(jsii_name="autoDevopsEnabled")
    def auto_devops_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "autoDevopsEnabled"))

    @builtins.property
    @jsii.member(jsii_name="buildGitStrategy")
    def build_git_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildGitStrategy"))

    @builtins.property
    @jsii.member(jsii_name="buildsAccessLevel")
    def builds_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildsAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="buildTimeout")
    def build_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "buildTimeout"))

    @builtins.property
    @jsii.member(jsii_name="ciConfigPath")
    def ci_config_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ciConfigPath"))

    @builtins.property
    @jsii.member(jsii_name="containerExpirationPolicy")
    def container_expiration_policy(
        self,
    ) -> "DataGitlabProjectContainerExpirationPolicyList":
        return typing.cast("DataGitlabProjectContainerExpirationPolicyList", jsii.get(self, "containerExpirationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryAccessLevel")
    def container_registry_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="defaultBranch")
    def default_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBranch"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="emailsDisabled")
    def emails_disabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "emailsDisabled"))

    @builtins.property
    @jsii.member(jsii_name="externalAuthorizationClassificationLabel")
    def external_authorization_classification_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalAuthorizationClassificationLabel"))

    @builtins.property
    @jsii.member(jsii_name="forkingAccessLevel")
    def forking_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forkingAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlToRepo")
    def http_url_to_repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpUrlToRepo"))

    @builtins.property
    @jsii.member(jsii_name="issuesAccessLevel")
    def issues_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuesAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="issuesEnabled")
    def issues_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "issuesEnabled"))

    @builtins.property
    @jsii.member(jsii_name="lfsEnabled")
    def lfs_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "lfsEnabled"))

    @builtins.property
    @jsii.member(jsii_name="mergeCommitTemplate")
    def merge_commit_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeCommitTemplate"))

    @builtins.property
    @jsii.member(jsii_name="mergePipelinesEnabled")
    def merge_pipelines_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "mergePipelinesEnabled"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsAccessLevel")
    def merge_requests_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeRequestsAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEnabled")
    def merge_requests_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "mergeRequestsEnabled"))

    @builtins.property
    @jsii.member(jsii_name="mergeTrainsEnabled")
    def merge_trains_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "mergeTrainsEnabled"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "namespaceId"))

    @builtins.property
    @jsii.member(jsii_name="operationsAccessLevel")
    def operations_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operationsAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="pipelinesEnabled")
    def pipelines_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "pipelinesEnabled"))

    @builtins.property
    @jsii.member(jsii_name="printingMergeRequestLinkEnabled")
    def printing_merge_request_link_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "printingMergeRequestLinkEnabled"))

    @builtins.property
    @jsii.member(jsii_name="pushRules")
    def push_rules(self) -> "DataGitlabProjectPushRulesList":
        return typing.cast("DataGitlabProjectPushRulesList", jsii.get(self, "pushRules"))

    @builtins.property
    @jsii.member(jsii_name="removeSourceBranchAfterMerge")
    def remove_source_branch_after_merge(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "removeSourceBranchAfterMerge"))

    @builtins.property
    @jsii.member(jsii_name="repositoryAccessLevel")
    def repository_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="repositoryStorage")
    def repository_storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryStorage"))

    @builtins.property
    @jsii.member(jsii_name="requestAccessEnabled")
    def request_access_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "requestAccessEnabled"))

    @builtins.property
    @jsii.member(jsii_name="requirementsAccessLevel")
    def requirements_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requirementsAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="resolveOutdatedDiffDiscussions")
    def resolve_outdated_diff_discussions(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "resolveOutdatedDiffDiscussions"))

    @builtins.property
    @jsii.member(jsii_name="runnersToken")
    def runners_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runnersToken"))

    @builtins.property
    @jsii.member(jsii_name="securityAndComplianceAccessLevel")
    def security_and_compliance_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityAndComplianceAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="snippetsAccessLevel")
    def snippets_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snippetsAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="snippetsEnabled")
    def snippets_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "snippetsEnabled"))

    @builtins.property
    @jsii.member(jsii_name="squashCommitTemplate")
    def squash_commit_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "squashCommitTemplate"))

    @builtins.property
    @jsii.member(jsii_name="sshUrlToRepo")
    def ssh_url_to_repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshUrlToRepo"))

    @builtins.property
    @jsii.member(jsii_name="topics")
    def topics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "topics"))

    @builtins.property
    @jsii.member(jsii_name="visibilityLevel")
    def visibility_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibilityLevel"))

    @builtins.property
    @jsii.member(jsii_name="webUrl")
    def web_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webUrl"))

    @builtins.property
    @jsii.member(jsii_name="wikiAccessLevel")
    def wiki_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wikiAccessLevel"))

    @builtins.property
    @jsii.member(jsii_name="wikiEnabled")
    def wiki_enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "wikiEnabled"))

    @builtins.property
    @jsii.member(jsii_name="ciDefaultGitDepthInput")
    def ci_default_git_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ciDefaultGitDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="pathWithNamespaceInput")
    def path_with_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathWithNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="publicBuildsInput")
    def public_builds_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicBuildsInput"))

    @builtins.property
    @jsii.member(jsii_name="ciDefaultGitDepth")
    def ci_default_git_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ciDefaultGitDepth"))

    @ci_default_git_depth.setter
    def ci_default_git_depth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProject, "ci_default_git_depth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ciDefaultGitDepth", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProject, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="pathWithNamespace")
    def path_with_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathWithNamespace"))

    @path_with_namespace.setter
    def path_with_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProject, "path_with_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathWithNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="publicBuilds")
    def public_builds(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "publicBuilds"))

    @public_builds.setter
    def public_builds(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProject, "public_builds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicBuilds", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProjectConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "ci_default_git_depth": "ciDefaultGitDepth",
        "id": "id",
        "path_with_namespace": "pathWithNamespace",
        "public_builds": "publicBuilds",
    },
)
class DataGitlabProjectConfig(cdktf.TerraformMetaArguments):
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
        ci_default_git_depth: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        path_with_namespace: typing.Optional[builtins.str] = None,
        public_builds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param ci_default_git_depth: Default number of revisions for shallow cloning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#ci_default_git_depth DataGitlabProject#ci_default_git_depth}
        :param id: The integer or path with namespace that uniquely identifies the project within the gitlab install. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#id DataGitlabProject#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param path_with_namespace: The path of the repository with namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#path_with_namespace DataGitlabProject#path_with_namespace}
        :param public_builds: If true, jobs can be viewed by non-project members. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#public_builds DataGitlabProject#public_builds}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument ci_default_git_depth", value=ci_default_git_depth, expected_type=type_hints["ci_default_git_depth"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path_with_namespace", value=path_with_namespace, expected_type=type_hints["path_with_namespace"])
            check_type(argname="argument public_builds", value=public_builds, expected_type=type_hints["public_builds"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if ci_default_git_depth is not None:
            self._values["ci_default_git_depth"] = ci_default_git_depth
        if id is not None:
            self._values["id"] = id
        if path_with_namespace is not None:
            self._values["path_with_namespace"] = path_with_namespace
        if public_builds is not None:
            self._values["public_builds"] = public_builds

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
    def ci_default_git_depth(self) -> typing.Optional[jsii.Number]:
        '''Default number of revisions for shallow cloning.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#ci_default_git_depth DataGitlabProject#ci_default_git_depth}
        '''
        result = self._values.get("ci_default_git_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''The integer or path with namespace that uniquely identifies the project within the gitlab install.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#id DataGitlabProject#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_with_namespace(self) -> typing.Optional[builtins.str]:
        '''The path of the repository with namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#path_with_namespace DataGitlabProject#path_with_namespace}
        '''
        result = self._values.get("path_with_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_builds(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, jobs can be viewed by non-project members.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/d/project#public_builds DataGitlabProject#public_builds}
        '''
        result = self._values.get("public_builds")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProjectContainerExpirationPolicy",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGitlabProjectContainerExpirationPolicy:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectContainerExpirationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGitlabProjectContainerExpirationPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProjectContainerExpirationPolicyList",
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
            type_hints = typing.get_type_hints(DataGitlabProjectContainerExpirationPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataGitlabProjectContainerExpirationPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectContainerExpirationPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGitlabProjectContainerExpirationPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectContainerExpirationPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectContainerExpirationPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectContainerExpirationPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGitlabProjectContainerExpirationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProjectContainerExpirationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(DataGitlabProjectContainerExpirationPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="cadence")
    def cadence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cadence"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "enabled"))

    @builtins.property
    @jsii.member(jsii_name="keepN")
    def keep_n(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keepN"))

    @builtins.property
    @jsii.member(jsii_name="nameRegexDelete")
    def name_regex_delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameRegexDelete"))

    @builtins.property
    @jsii.member(jsii_name="nameRegexKeep")
    def name_regex_keep(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameRegexKeep"))

    @builtins.property
    @jsii.member(jsii_name="nextRunAt")
    def next_run_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextRunAt"))

    @builtins.property
    @jsii.member(jsii_name="olderThan")
    def older_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "olderThan"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataGitlabProjectContainerExpirationPolicy]:
        return typing.cast(typing.Optional[DataGitlabProjectContainerExpirationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGitlabProjectContainerExpirationPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectContainerExpirationPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProjectPushRules",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataGitlabProjectPushRules:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGitlabProjectPushRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataGitlabProjectPushRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProjectPushRulesList",
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
            type_hints = typing.get_type_hints(DataGitlabProjectPushRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataGitlabProjectPushRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataGitlabProjectPushRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataGitlabProjectPushRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectPushRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectPushRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectPushRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class DataGitlabProjectPushRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.dataGitlabProject.DataGitlabProjectPushRulesOutputReference",
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
            type_hints = typing.get_type_hints(DataGitlabProjectPushRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="authorEmailRegex")
    def author_email_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorEmailRegex"))

    @builtins.property
    @jsii.member(jsii_name="branchNameRegex")
    def branch_name_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchNameRegex"))

    @builtins.property
    @jsii.member(jsii_name="commitCommitterCheck")
    def commit_committer_check(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "commitCommitterCheck"))

    @builtins.property
    @jsii.member(jsii_name="commitMessageNegativeRegex")
    def commit_message_negative_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitMessageNegativeRegex"))

    @builtins.property
    @jsii.member(jsii_name="commitMessageRegex")
    def commit_message_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitMessageRegex"))

    @builtins.property
    @jsii.member(jsii_name="denyDeleteTag")
    def deny_delete_tag(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "denyDeleteTag"))

    @builtins.property
    @jsii.member(jsii_name="fileNameRegex")
    def file_name_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileNameRegex"))

    @builtins.property
    @jsii.member(jsii_name="maxFileSize")
    def max_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFileSize"))

    @builtins.property
    @jsii.member(jsii_name="memberCheck")
    def member_check(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "memberCheck"))

    @builtins.property
    @jsii.member(jsii_name="preventSecrets")
    def prevent_secrets(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "preventSecrets"))

    @builtins.property
    @jsii.member(jsii_name="rejectUnsignedCommits")
    def reject_unsigned_commits(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "rejectUnsignedCommits"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataGitlabProjectPushRules]:
        return typing.cast(typing.Optional[DataGitlabProjectPushRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataGitlabProjectPushRules],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataGitlabProjectPushRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataGitlabProject",
    "DataGitlabProjectConfig",
    "DataGitlabProjectContainerExpirationPolicy",
    "DataGitlabProjectContainerExpirationPolicyList",
    "DataGitlabProjectContainerExpirationPolicyOutputReference",
    "DataGitlabProjectPushRules",
    "DataGitlabProjectPushRulesList",
    "DataGitlabProjectPushRulesOutputReference",
]

publication.publish()
