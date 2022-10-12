'''
# `github_repository`

Refer to the Terraform Registory for docs: [`github_repository`](https://www.terraform.io/docs/providers/github/r/repository).
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


class Repository(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repository.Repository",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/github/r/repository github_repository}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        allow_auto_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_merge_commit: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_rebase_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_squash_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archive_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_init: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_branch: typing.Optional[builtins.str] = None,
        delete_branch_on_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        gitignore_template: typing.Optional[builtins.str] = None,
        has_downloads: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        has_issues: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        has_projects: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        has_wiki: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        homepage_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_vulnerability_alerts_during_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        license_template: typing.Optional[builtins.str] = None,
        merge_commit_message: typing.Optional[builtins.str] = None,
        merge_commit_title: typing.Optional[builtins.str] = None,
        pages: typing.Optional[typing.Union["RepositoryPages", typing.Dict[str, typing.Any]]] = None,
        private: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        squash_merge_commit_message: typing.Optional[builtins.str] = None,
        squash_merge_commit_title: typing.Optional[builtins.str] = None,
        template: typing.Optional[typing.Union["RepositoryTemplate", typing.Dict[str, typing.Any]]] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
        vulnerability_alerts: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/github/r/repository github_repository} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#name Repository#name}.
        :param allow_auto_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_auto_merge Repository#allow_auto_merge}.
        :param allow_merge_commit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_merge_commit Repository#allow_merge_commit}.
        :param allow_rebase_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_rebase_merge Repository#allow_rebase_merge}.
        :param allow_squash_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_squash_merge Repository#allow_squash_merge}.
        :param archived: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#archived Repository#archived}.
        :param archive_on_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#archive_on_destroy Repository#archive_on_destroy}.
        :param auto_init: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#auto_init Repository#auto_init}.
        :param default_branch: Can only be set after initial repository creation, and only if the target branch exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#default_branch Repository#default_branch}
        :param delete_branch_on_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#delete_branch_on_merge Repository#delete_branch_on_merge}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#description Repository#description}.
        :param gitignore_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#gitignore_template Repository#gitignore_template}.
        :param has_downloads: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_downloads Repository#has_downloads}.
        :param has_issues: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_issues Repository#has_issues}.
        :param has_projects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_projects Repository#has_projects}.
        :param has_wiki: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_wiki Repository#has_wiki}.
        :param homepage_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#homepage_url Repository#homepage_url}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#id Repository#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_vulnerability_alerts_during_read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#ignore_vulnerability_alerts_during_read Repository#ignore_vulnerability_alerts_during_read}.
        :param is_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#is_template Repository#is_template}.
        :param license_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#license_template Repository#license_template}.
        :param merge_commit_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#merge_commit_message Repository#merge_commit_message}.
        :param merge_commit_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#merge_commit_title Repository#merge_commit_title}.
        :param pages: pages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#pages Repository#pages}
        :param private: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#private Repository#private}.
        :param squash_merge_commit_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#squash_merge_commit_message Repository#squash_merge_commit_message}.
        :param squash_merge_commit_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#squash_merge_commit_title Repository#squash_merge_commit_title}.
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#template Repository#template}
        :param topics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#topics Repository#topics}.
        :param visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#visibility Repository#visibility}.
        :param vulnerability_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#vulnerability_alerts Repository#vulnerability_alerts}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Repository.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RepositoryConfig(
            name=name,
            allow_auto_merge=allow_auto_merge,
            allow_merge_commit=allow_merge_commit,
            allow_rebase_merge=allow_rebase_merge,
            allow_squash_merge=allow_squash_merge,
            archived=archived,
            archive_on_destroy=archive_on_destroy,
            auto_init=auto_init,
            default_branch=default_branch,
            delete_branch_on_merge=delete_branch_on_merge,
            description=description,
            gitignore_template=gitignore_template,
            has_downloads=has_downloads,
            has_issues=has_issues,
            has_projects=has_projects,
            has_wiki=has_wiki,
            homepage_url=homepage_url,
            id=id,
            ignore_vulnerability_alerts_during_read=ignore_vulnerability_alerts_during_read,
            is_template=is_template,
            license_template=license_template,
            merge_commit_message=merge_commit_message,
            merge_commit_title=merge_commit_title,
            pages=pages,
            private=private,
            squash_merge_commit_message=squash_merge_commit_message,
            squash_merge_commit_title=squash_merge_commit_title,
            template=template,
            topics=topics,
            visibility=visibility,
            vulnerability_alerts=vulnerability_alerts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPages")
    def put_pages(
        self,
        *,
        source: typing.Union["RepositoryPagesSource", typing.Dict[str, typing.Any]],
        cname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#source Repository#source}
        :param cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#cname Repository#cname}.
        '''
        value = RepositoryPages(source=source, cname=cname)

        return typing.cast(None, jsii.invoke(self, "putPages", [value]))

    @jsii.member(jsii_name="putTemplate")
    def put_template(self, *, owner: builtins.str, repository: builtins.str) -> None:
        '''
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#owner Repository#owner}.
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#repository Repository#repository}.
        '''
        value = RepositoryTemplate(owner=owner, repository=repository)

        return typing.cast(None, jsii.invoke(self, "putTemplate", [value]))

    @jsii.member(jsii_name="resetAllowAutoMerge")
    def reset_allow_auto_merge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowAutoMerge", []))

    @jsii.member(jsii_name="resetAllowMergeCommit")
    def reset_allow_merge_commit(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMergeCommit", []))

    @jsii.member(jsii_name="resetAllowRebaseMerge")
    def reset_allow_rebase_merge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowRebaseMerge", []))

    @jsii.member(jsii_name="resetAllowSquashMerge")
    def reset_allow_squash_merge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowSquashMerge", []))

    @jsii.member(jsii_name="resetArchived")
    def reset_archived(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchived", []))

    @jsii.member(jsii_name="resetArchiveOnDestroy")
    def reset_archive_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveOnDestroy", []))

    @jsii.member(jsii_name="resetAutoInit")
    def reset_auto_init(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoInit", []))

    @jsii.member(jsii_name="resetDefaultBranch")
    def reset_default_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBranch", []))

    @jsii.member(jsii_name="resetDeleteBranchOnMerge")
    def reset_delete_branch_on_merge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteBranchOnMerge", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetGitignoreTemplate")
    def reset_gitignore_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitignoreTemplate", []))

    @jsii.member(jsii_name="resetHasDownloads")
    def reset_has_downloads(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHasDownloads", []))

    @jsii.member(jsii_name="resetHasIssues")
    def reset_has_issues(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHasIssues", []))

    @jsii.member(jsii_name="resetHasProjects")
    def reset_has_projects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHasProjects", []))

    @jsii.member(jsii_name="resetHasWiki")
    def reset_has_wiki(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHasWiki", []))

    @jsii.member(jsii_name="resetHomepageUrl")
    def reset_homepage_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomepageUrl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreVulnerabilityAlertsDuringRead")
    def reset_ignore_vulnerability_alerts_during_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreVulnerabilityAlertsDuringRead", []))

    @jsii.member(jsii_name="resetIsTemplate")
    def reset_is_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsTemplate", []))

    @jsii.member(jsii_name="resetLicenseTemplate")
    def reset_license_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseTemplate", []))

    @jsii.member(jsii_name="resetMergeCommitMessage")
    def reset_merge_commit_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeCommitMessage", []))

    @jsii.member(jsii_name="resetMergeCommitTitle")
    def reset_merge_commit_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeCommitTitle", []))

    @jsii.member(jsii_name="resetPages")
    def reset_pages(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPages", []))

    @jsii.member(jsii_name="resetPrivate")
    def reset_private(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivate", []))

    @jsii.member(jsii_name="resetSquashMergeCommitMessage")
    def reset_squash_merge_commit_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSquashMergeCommitMessage", []))

    @jsii.member(jsii_name="resetSquashMergeCommitTitle")
    def reset_squash_merge_commit_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSquashMergeCommitTitle", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @jsii.member(jsii_name="resetTopics")
    def reset_topics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopics", []))

    @jsii.member(jsii_name="resetVisibility")
    def reset_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibility", []))

    @jsii.member(jsii_name="resetVulnerabilityAlerts")
    def reset_vulnerability_alerts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVulnerabilityAlerts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="branches")
    def branches(self) -> "RepositoryBranchesList":
        return typing.cast("RepositoryBranchesList", jsii.get(self, "branches"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="fullName")
    def full_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullName"))

    @builtins.property
    @jsii.member(jsii_name="gitCloneUrl")
    def git_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitCloneUrl"))

    @builtins.property
    @jsii.member(jsii_name="htmlUrl")
    def html_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlUrl"))

    @builtins.property
    @jsii.member(jsii_name="httpCloneUrl")
    def http_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpCloneUrl"))

    @builtins.property
    @jsii.member(jsii_name="nodeId")
    def node_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeId"))

    @builtins.property
    @jsii.member(jsii_name="pages")
    def pages(self) -> "RepositoryPagesOutputReference":
        return typing.cast("RepositoryPagesOutputReference", jsii.get(self, "pages"))

    @builtins.property
    @jsii.member(jsii_name="repoId")
    def repo_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "repoId"))

    @builtins.property
    @jsii.member(jsii_name="sshCloneUrl")
    def ssh_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshCloneUrl"))

    @builtins.property
    @jsii.member(jsii_name="svnUrl")
    def svn_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "svnUrl"))

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> "RepositoryTemplateOutputReference":
        return typing.cast("RepositoryTemplateOutputReference", jsii.get(self, "template"))

    @builtins.property
    @jsii.member(jsii_name="allowAutoMergeInput")
    def allow_auto_merge_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowAutoMergeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMergeCommitInput")
    def allow_merge_commit_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowMergeCommitInput"))

    @builtins.property
    @jsii.member(jsii_name="allowRebaseMergeInput")
    def allow_rebase_merge_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowRebaseMergeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowSquashMergeInput")
    def allow_squash_merge_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowSquashMergeInput"))

    @builtins.property
    @jsii.member(jsii_name="archivedInput")
    def archived_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "archivedInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveOnDestroyInput")
    def archive_on_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "archiveOnDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoInitInput")
    def auto_init_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoInitInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBranchInput")
    def default_branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteBranchOnMergeInput")
    def delete_branch_on_merge_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteBranchOnMergeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="gitignoreTemplateInput")
    def gitignore_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gitignoreTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="hasDownloadsInput")
    def has_downloads_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hasDownloadsInput"))

    @builtins.property
    @jsii.member(jsii_name="hasIssuesInput")
    def has_issues_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hasIssuesInput"))

    @builtins.property
    @jsii.member(jsii_name="hasProjectsInput")
    def has_projects_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hasProjectsInput"))

    @builtins.property
    @jsii.member(jsii_name="hasWikiInput")
    def has_wiki_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hasWikiInput"))

    @builtins.property
    @jsii.member(jsii_name="homepageUrlInput")
    def homepage_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homepageUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreVulnerabilityAlertsDuringReadInput")
    def ignore_vulnerability_alerts_during_read_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreVulnerabilityAlertsDuringReadInput"))

    @builtins.property
    @jsii.member(jsii_name="isTemplateInput")
    def is_template_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseTemplateInput")
    def license_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeCommitMessageInput")
    def merge_commit_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeCommitMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeCommitTitleInput")
    def merge_commit_title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeCommitTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pagesInput")
    def pages_input(self) -> typing.Optional["RepositoryPages"]:
        return typing.cast(typing.Optional["RepositoryPages"], jsii.get(self, "pagesInput"))

    @builtins.property
    @jsii.member(jsii_name="privateInput")
    def private_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privateInput"))

    @builtins.property
    @jsii.member(jsii_name="squashMergeCommitMessageInput")
    def squash_merge_commit_message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "squashMergeCommitMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="squashMergeCommitTitleInput")
    def squash_merge_commit_title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "squashMergeCommitTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional["RepositoryTemplate"]:
        return typing.cast(typing.Optional["RepositoryTemplate"], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="topicsInput")
    def topics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "topicsInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityInput")
    def visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="vulnerabilityAlertsInput")
    def vulnerability_alerts_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "vulnerabilityAlertsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowAutoMerge")
    def allow_auto_merge(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowAutoMerge"))

    @allow_auto_merge.setter
    def allow_auto_merge(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "allow_auto_merge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowAutoMerge", value)

    @builtins.property
    @jsii.member(jsii_name="allowMergeCommit")
    def allow_merge_commit(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowMergeCommit"))

    @allow_merge_commit.setter
    def allow_merge_commit(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "allow_merge_commit").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMergeCommit", value)

    @builtins.property
    @jsii.member(jsii_name="allowRebaseMerge")
    def allow_rebase_merge(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowRebaseMerge"))

    @allow_rebase_merge.setter
    def allow_rebase_merge(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "allow_rebase_merge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowRebaseMerge", value)

    @builtins.property
    @jsii.member(jsii_name="allowSquashMerge")
    def allow_squash_merge(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowSquashMerge"))

    @allow_squash_merge.setter
    def allow_squash_merge(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "allow_squash_merge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowSquashMerge", value)

    @builtins.property
    @jsii.member(jsii_name="archived")
    def archived(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "archived"))

    @archived.setter
    def archived(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "archived").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archived", value)

    @builtins.property
    @jsii.member(jsii_name="archiveOnDestroy")
    def archive_on_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "archiveOnDestroy"))

    @archive_on_destroy.setter
    def archive_on_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "archive_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="autoInit")
    def auto_init(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoInit"))

    @auto_init.setter
    def auto_init(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "auto_init").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoInit", value)

    @builtins.property
    @jsii.member(jsii_name="defaultBranch")
    def default_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBranch"))

    @default_branch.setter
    def default_branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "default_branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBranch", value)

    @builtins.property
    @jsii.member(jsii_name="deleteBranchOnMerge")
    def delete_branch_on_merge(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deleteBranchOnMerge"))

    @delete_branch_on_merge.setter
    def delete_branch_on_merge(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "delete_branch_on_merge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteBranchOnMerge", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="gitignoreTemplate")
    def gitignore_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gitignoreTemplate"))

    @gitignore_template.setter
    def gitignore_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "gitignore_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gitignoreTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="hasDownloads")
    def has_downloads(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hasDownloads"))

    @has_downloads.setter
    def has_downloads(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "has_downloads").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hasDownloads", value)

    @builtins.property
    @jsii.member(jsii_name="hasIssues")
    def has_issues(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hasIssues"))

    @has_issues.setter
    def has_issues(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "has_issues").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hasIssues", value)

    @builtins.property
    @jsii.member(jsii_name="hasProjects")
    def has_projects(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hasProjects"))

    @has_projects.setter
    def has_projects(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "has_projects").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hasProjects", value)

    @builtins.property
    @jsii.member(jsii_name="hasWiki")
    def has_wiki(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hasWiki"))

    @has_wiki.setter
    def has_wiki(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "has_wiki").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hasWiki", value)

    @builtins.property
    @jsii.member(jsii_name="homepageUrl")
    def homepage_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homepageUrl"))

    @homepage_url.setter
    def homepage_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "homepage_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homepageUrl", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreVulnerabilityAlertsDuringRead")
    def ignore_vulnerability_alerts_during_read(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreVulnerabilityAlertsDuringRead"))

    @ignore_vulnerability_alerts_during_read.setter
    def ignore_vulnerability_alerts_during_read(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "ignore_vulnerability_alerts_during_read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreVulnerabilityAlertsDuringRead", value)

    @builtins.property
    @jsii.member(jsii_name="isTemplate")
    def is_template(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isTemplate"))

    @is_template.setter
    def is_template(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "is_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="licenseTemplate")
    def license_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseTemplate"))

    @license_template.setter
    def license_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "license_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="mergeCommitMessage")
    def merge_commit_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeCommitMessage"))

    @merge_commit_message.setter
    def merge_commit_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "merge_commit_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeCommitMessage", value)

    @builtins.property
    @jsii.member(jsii_name="mergeCommitTitle")
    def merge_commit_title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeCommitTitle"))

    @merge_commit_title.setter
    def merge_commit_title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "merge_commit_title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeCommitTitle", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="private")
    def private(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "private"))

    @private.setter
    def private(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "private").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "private", value)

    @builtins.property
    @jsii.member(jsii_name="squashMergeCommitMessage")
    def squash_merge_commit_message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "squashMergeCommitMessage"))

    @squash_merge_commit_message.setter
    def squash_merge_commit_message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "squash_merge_commit_message").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "squashMergeCommitMessage", value)

    @builtins.property
    @jsii.member(jsii_name="squashMergeCommitTitle")
    def squash_merge_commit_title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "squashMergeCommitTitle"))

    @squash_merge_commit_title.setter
    def squash_merge_commit_title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "squash_merge_commit_title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "squashMergeCommitTitle", value)

    @builtins.property
    @jsii.member(jsii_name="topics")
    def topics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "topics"))

    @topics.setter
    def topics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "topics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topics", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)

    @builtins.property
    @jsii.member(jsii_name="vulnerabilityAlerts")
    def vulnerability_alerts(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "vulnerabilityAlerts"))

    @vulnerability_alerts.setter
    def vulnerability_alerts(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Repository, "vulnerability_alerts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vulnerabilityAlerts", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repository.RepositoryBranches",
    jsii_struct_bases=[],
    name_mapping={},
)
class RepositoryBranches:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryBranches(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryBranchesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repository.RepositoryBranchesList",
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
            type_hints = typing.get_type_hints(RepositoryBranchesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RepositoryBranchesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryBranchesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RepositoryBranchesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryBranchesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(RepositoryBranchesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(RepositoryBranchesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class RepositoryBranchesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repository.RepositoryBranchesOutputReference",
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
            type_hints = typing.get_type_hints(RepositoryBranchesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="protected")
    def protected(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "protected"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RepositoryBranches]:
        return typing.cast(typing.Optional[RepositoryBranches], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RepositoryBranches]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryBranchesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repository.RepositoryConfig",
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
        "allow_auto_merge": "allowAutoMerge",
        "allow_merge_commit": "allowMergeCommit",
        "allow_rebase_merge": "allowRebaseMerge",
        "allow_squash_merge": "allowSquashMerge",
        "archived": "archived",
        "archive_on_destroy": "archiveOnDestroy",
        "auto_init": "autoInit",
        "default_branch": "defaultBranch",
        "delete_branch_on_merge": "deleteBranchOnMerge",
        "description": "description",
        "gitignore_template": "gitignoreTemplate",
        "has_downloads": "hasDownloads",
        "has_issues": "hasIssues",
        "has_projects": "hasProjects",
        "has_wiki": "hasWiki",
        "homepage_url": "homepageUrl",
        "id": "id",
        "ignore_vulnerability_alerts_during_read": "ignoreVulnerabilityAlertsDuringRead",
        "is_template": "isTemplate",
        "license_template": "licenseTemplate",
        "merge_commit_message": "mergeCommitMessage",
        "merge_commit_title": "mergeCommitTitle",
        "pages": "pages",
        "private": "private",
        "squash_merge_commit_message": "squashMergeCommitMessage",
        "squash_merge_commit_title": "squashMergeCommitTitle",
        "template": "template",
        "topics": "topics",
        "visibility": "visibility",
        "vulnerability_alerts": "vulnerabilityAlerts",
    },
)
class RepositoryConfig(cdktf.TerraformMetaArguments):
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
        allow_auto_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_merge_commit: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_rebase_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_squash_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archive_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_init: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_branch: typing.Optional[builtins.str] = None,
        delete_branch_on_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        gitignore_template: typing.Optional[builtins.str] = None,
        has_downloads: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        has_issues: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        has_projects: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        has_wiki: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        homepage_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_vulnerability_alerts_during_read: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        is_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        license_template: typing.Optional[builtins.str] = None,
        merge_commit_message: typing.Optional[builtins.str] = None,
        merge_commit_title: typing.Optional[builtins.str] = None,
        pages: typing.Optional[typing.Union["RepositoryPages", typing.Dict[str, typing.Any]]] = None,
        private: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        squash_merge_commit_message: typing.Optional[builtins.str] = None,
        squash_merge_commit_title: typing.Optional[builtins.str] = None,
        template: typing.Optional[typing.Union["RepositoryTemplate", typing.Dict[str, typing.Any]]] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        visibility: typing.Optional[builtins.str] = None,
        vulnerability_alerts: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#name Repository#name}.
        :param allow_auto_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_auto_merge Repository#allow_auto_merge}.
        :param allow_merge_commit: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_merge_commit Repository#allow_merge_commit}.
        :param allow_rebase_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_rebase_merge Repository#allow_rebase_merge}.
        :param allow_squash_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_squash_merge Repository#allow_squash_merge}.
        :param archived: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#archived Repository#archived}.
        :param archive_on_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#archive_on_destroy Repository#archive_on_destroy}.
        :param auto_init: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#auto_init Repository#auto_init}.
        :param default_branch: Can only be set after initial repository creation, and only if the target branch exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#default_branch Repository#default_branch}
        :param delete_branch_on_merge: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#delete_branch_on_merge Repository#delete_branch_on_merge}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#description Repository#description}.
        :param gitignore_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#gitignore_template Repository#gitignore_template}.
        :param has_downloads: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_downloads Repository#has_downloads}.
        :param has_issues: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_issues Repository#has_issues}.
        :param has_projects: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_projects Repository#has_projects}.
        :param has_wiki: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_wiki Repository#has_wiki}.
        :param homepage_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#homepage_url Repository#homepage_url}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#id Repository#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_vulnerability_alerts_during_read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#ignore_vulnerability_alerts_during_read Repository#ignore_vulnerability_alerts_during_read}.
        :param is_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#is_template Repository#is_template}.
        :param license_template: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#license_template Repository#license_template}.
        :param merge_commit_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#merge_commit_message Repository#merge_commit_message}.
        :param merge_commit_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#merge_commit_title Repository#merge_commit_title}.
        :param pages: pages block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#pages Repository#pages}
        :param private: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#private Repository#private}.
        :param squash_merge_commit_message: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#squash_merge_commit_message Repository#squash_merge_commit_message}.
        :param squash_merge_commit_title: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#squash_merge_commit_title Repository#squash_merge_commit_title}.
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#template Repository#template}
        :param topics: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#topics Repository#topics}.
        :param visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#visibility Repository#visibility}.
        :param vulnerability_alerts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#vulnerability_alerts Repository#vulnerability_alerts}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(pages, dict):
            pages = RepositoryPages(**pages)
        if isinstance(template, dict):
            template = RepositoryTemplate(**template)
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allow_auto_merge", value=allow_auto_merge, expected_type=type_hints["allow_auto_merge"])
            check_type(argname="argument allow_merge_commit", value=allow_merge_commit, expected_type=type_hints["allow_merge_commit"])
            check_type(argname="argument allow_rebase_merge", value=allow_rebase_merge, expected_type=type_hints["allow_rebase_merge"])
            check_type(argname="argument allow_squash_merge", value=allow_squash_merge, expected_type=type_hints["allow_squash_merge"])
            check_type(argname="argument archived", value=archived, expected_type=type_hints["archived"])
            check_type(argname="argument archive_on_destroy", value=archive_on_destroy, expected_type=type_hints["archive_on_destroy"])
            check_type(argname="argument auto_init", value=auto_init, expected_type=type_hints["auto_init"])
            check_type(argname="argument default_branch", value=default_branch, expected_type=type_hints["default_branch"])
            check_type(argname="argument delete_branch_on_merge", value=delete_branch_on_merge, expected_type=type_hints["delete_branch_on_merge"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument gitignore_template", value=gitignore_template, expected_type=type_hints["gitignore_template"])
            check_type(argname="argument has_downloads", value=has_downloads, expected_type=type_hints["has_downloads"])
            check_type(argname="argument has_issues", value=has_issues, expected_type=type_hints["has_issues"])
            check_type(argname="argument has_projects", value=has_projects, expected_type=type_hints["has_projects"])
            check_type(argname="argument has_wiki", value=has_wiki, expected_type=type_hints["has_wiki"])
            check_type(argname="argument homepage_url", value=homepage_url, expected_type=type_hints["homepage_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_vulnerability_alerts_during_read", value=ignore_vulnerability_alerts_during_read, expected_type=type_hints["ignore_vulnerability_alerts_during_read"])
            check_type(argname="argument is_template", value=is_template, expected_type=type_hints["is_template"])
            check_type(argname="argument license_template", value=license_template, expected_type=type_hints["license_template"])
            check_type(argname="argument merge_commit_message", value=merge_commit_message, expected_type=type_hints["merge_commit_message"])
            check_type(argname="argument merge_commit_title", value=merge_commit_title, expected_type=type_hints["merge_commit_title"])
            check_type(argname="argument pages", value=pages, expected_type=type_hints["pages"])
            check_type(argname="argument private", value=private, expected_type=type_hints["private"])
            check_type(argname="argument squash_merge_commit_message", value=squash_merge_commit_message, expected_type=type_hints["squash_merge_commit_message"])
            check_type(argname="argument squash_merge_commit_title", value=squash_merge_commit_title, expected_type=type_hints["squash_merge_commit_title"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
            check_type(argname="argument vulnerability_alerts", value=vulnerability_alerts, expected_type=type_hints["vulnerability_alerts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
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
        if allow_auto_merge is not None:
            self._values["allow_auto_merge"] = allow_auto_merge
        if allow_merge_commit is not None:
            self._values["allow_merge_commit"] = allow_merge_commit
        if allow_rebase_merge is not None:
            self._values["allow_rebase_merge"] = allow_rebase_merge
        if allow_squash_merge is not None:
            self._values["allow_squash_merge"] = allow_squash_merge
        if archived is not None:
            self._values["archived"] = archived
        if archive_on_destroy is not None:
            self._values["archive_on_destroy"] = archive_on_destroy
        if auto_init is not None:
            self._values["auto_init"] = auto_init
        if default_branch is not None:
            self._values["default_branch"] = default_branch
        if delete_branch_on_merge is not None:
            self._values["delete_branch_on_merge"] = delete_branch_on_merge
        if description is not None:
            self._values["description"] = description
        if gitignore_template is not None:
            self._values["gitignore_template"] = gitignore_template
        if has_downloads is not None:
            self._values["has_downloads"] = has_downloads
        if has_issues is not None:
            self._values["has_issues"] = has_issues
        if has_projects is not None:
            self._values["has_projects"] = has_projects
        if has_wiki is not None:
            self._values["has_wiki"] = has_wiki
        if homepage_url is not None:
            self._values["homepage_url"] = homepage_url
        if id is not None:
            self._values["id"] = id
        if ignore_vulnerability_alerts_during_read is not None:
            self._values["ignore_vulnerability_alerts_during_read"] = ignore_vulnerability_alerts_during_read
        if is_template is not None:
            self._values["is_template"] = is_template
        if license_template is not None:
            self._values["license_template"] = license_template
        if merge_commit_message is not None:
            self._values["merge_commit_message"] = merge_commit_message
        if merge_commit_title is not None:
            self._values["merge_commit_title"] = merge_commit_title
        if pages is not None:
            self._values["pages"] = pages
        if private is not None:
            self._values["private"] = private
        if squash_merge_commit_message is not None:
            self._values["squash_merge_commit_message"] = squash_merge_commit_message
        if squash_merge_commit_title is not None:
            self._values["squash_merge_commit_title"] = squash_merge_commit_title
        if template is not None:
            self._values["template"] = template
        if topics is not None:
            self._values["topics"] = topics
        if visibility is not None:
            self._values["visibility"] = visibility
        if vulnerability_alerts is not None:
            self._values["vulnerability_alerts"] = vulnerability_alerts

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#name Repository#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_auto_merge(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_auto_merge Repository#allow_auto_merge}.'''
        result = self._values.get("allow_auto_merge")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_merge_commit(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_merge_commit Repository#allow_merge_commit}.'''
        result = self._values.get("allow_merge_commit")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_rebase_merge(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_rebase_merge Repository#allow_rebase_merge}.'''
        result = self._values.get("allow_rebase_merge")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_squash_merge(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#allow_squash_merge Repository#allow_squash_merge}.'''
        result = self._values.get("allow_squash_merge")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def archived(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#archived Repository#archived}.'''
        result = self._values.get("archived")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def archive_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#archive_on_destroy Repository#archive_on_destroy}.'''
        result = self._values.get("archive_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_init(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#auto_init Repository#auto_init}.'''
        result = self._values.get("auto_init")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def default_branch(self) -> typing.Optional[builtins.str]:
        '''Can only be set after initial repository creation, and only if the target branch exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#default_branch Repository#default_branch}
        '''
        result = self._values.get("default_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_branch_on_merge(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#delete_branch_on_merge Repository#delete_branch_on_merge}.'''
        result = self._values.get("delete_branch_on_merge")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#description Repository#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gitignore_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#gitignore_template Repository#gitignore_template}.'''
        result = self._values.get("gitignore_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def has_downloads(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_downloads Repository#has_downloads}.'''
        result = self._values.get("has_downloads")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def has_issues(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_issues Repository#has_issues}.'''
        result = self._values.get("has_issues")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def has_projects(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_projects Repository#has_projects}.'''
        result = self._values.get("has_projects")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def has_wiki(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#has_wiki Repository#has_wiki}.'''
        result = self._values.get("has_wiki")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def homepage_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#homepage_url Repository#homepage_url}.'''
        result = self._values.get("homepage_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#id Repository#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_vulnerability_alerts_during_read(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#ignore_vulnerability_alerts_during_read Repository#ignore_vulnerability_alerts_during_read}.'''
        result = self._values.get("ignore_vulnerability_alerts_during_read")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def is_template(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#is_template Repository#is_template}.'''
        result = self._values.get("is_template")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def license_template(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#license_template Repository#license_template}.'''
        result = self._values.get("license_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_commit_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#merge_commit_message Repository#merge_commit_message}.'''
        result = self._values.get("merge_commit_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_commit_title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#merge_commit_title Repository#merge_commit_title}.'''
        result = self._values.get("merge_commit_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pages(self) -> typing.Optional["RepositoryPages"]:
        '''pages block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#pages Repository#pages}
        '''
        result = self._values.get("pages")
        return typing.cast(typing.Optional["RepositoryPages"], result)

    @builtins.property
    def private(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#private Repository#private}.'''
        result = self._values.get("private")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def squash_merge_commit_message(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#squash_merge_commit_message Repository#squash_merge_commit_message}.'''
        result = self._values.get("squash_merge_commit_message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def squash_merge_commit_title(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#squash_merge_commit_title Repository#squash_merge_commit_title}.'''
        result = self._values.get("squash_merge_commit_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template(self) -> typing.Optional["RepositoryTemplate"]:
        '''template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#template Repository#template}
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional["RepositoryTemplate"], result)

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#topics Repository#topics}.'''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#visibility Repository#visibility}.'''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vulnerability_alerts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#vulnerability_alerts Repository#vulnerability_alerts}.'''
        result = self._values.get("vulnerability_alerts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repository.RepositoryPages",
    jsii_struct_bases=[],
    name_mapping={"source": "source", "cname": "cname"},
)
class RepositoryPages:
    def __init__(
        self,
        *,
        source: typing.Union["RepositoryPagesSource", typing.Dict[str, typing.Any]],
        cname: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#source Repository#source}
        :param cname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#cname Repository#cname}.
        '''
        if isinstance(source, dict):
            source = RepositoryPagesSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryPages.__init__)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument cname", value=cname, expected_type=type_hints["cname"])
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
        }
        if cname is not None:
            self._values["cname"] = cname

    @builtins.property
    def source(self) -> "RepositoryPagesSource":
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#source Repository#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("RepositoryPagesSource", result)

    @builtins.property
    def cname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#cname Repository#cname}.'''
        result = self._values.get("cname")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryPages(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryPagesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repository.RepositoryPagesOutputReference",
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
            type_hints = typing.get_type_hints(RepositoryPagesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        branch: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#branch Repository#branch}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#path Repository#path}.
        '''
        value = RepositoryPagesSource(branch=branch, path=path)

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="resetCname")
    def reset_cname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCname", []))

    @builtins.property
    @jsii.member(jsii_name="custom404")
    def custom404(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "custom404"))

    @builtins.property
    @jsii.member(jsii_name="htmlUrl")
    def html_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlUrl"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "RepositoryPagesSourceOutputReference":
        return typing.cast("RepositoryPagesSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="cnameInput")
    def cname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cnameInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["RepositoryPagesSource"]:
        return typing.cast(typing.Optional["RepositoryPagesSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="cname")
    def cname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cname"))

    @cname.setter
    def cname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPagesOutputReference, "cname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cname", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RepositoryPages]:
        return typing.cast(typing.Optional[RepositoryPages], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RepositoryPages]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPagesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repository.RepositoryPagesSource",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "path": "path"},
)
class RepositoryPagesSource:
    def __init__(
        self,
        *,
        branch: builtins.str,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#branch Repository#branch}.
        :param path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#path Repository#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryPagesSource.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "branch": branch,
        }
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def branch(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#branch Repository#branch}.'''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#path Repository#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryPagesSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryPagesSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repository.RepositoryPagesSourceOutputReference",
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
            type_hints = typing.get_type_hints(RepositoryPagesSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPagesSourceOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPagesSourceOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RepositoryPagesSource]:
        return typing.cast(typing.Optional[RepositoryPagesSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RepositoryPagesSource]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryPagesSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-github.repository.RepositoryTemplate",
    jsii_struct_bases=[],
    name_mapping={"owner": "owner", "repository": "repository"},
)
class RepositoryTemplate:
    def __init__(self, *, owner: builtins.str, repository: builtins.str) -> None:
        '''
        :param owner: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#owner Repository#owner}.
        :param repository: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#repository Repository#repository}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RepositoryTemplate.__init__)
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
        self._values: typing.Dict[str, typing.Any] = {
            "owner": owner,
            "repository": repository,
        }

    @builtins.property
    def owner(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#owner Repository#owner}.'''
        result = self._values.get("owner")
        assert result is not None, "Required property 'owner' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/github/r/repository#repository Repository#repository}.'''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RepositoryTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-github.repository.RepositoryTemplateOutputReference",
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
            type_hints = typing.get_type_hints(RepositoryTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryTemplateOutputReference, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryTemplateOutputReference, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RepositoryTemplate]:
        return typing.cast(typing.Optional[RepositoryTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RepositoryTemplate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RepositoryTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Repository",
    "RepositoryBranches",
    "RepositoryBranchesList",
    "RepositoryBranchesOutputReference",
    "RepositoryConfig",
    "RepositoryPages",
    "RepositoryPagesOutputReference",
    "RepositoryPagesSource",
    "RepositoryPagesSourceOutputReference",
    "RepositoryTemplate",
    "RepositoryTemplateOutputReference",
]

publication.publish()
