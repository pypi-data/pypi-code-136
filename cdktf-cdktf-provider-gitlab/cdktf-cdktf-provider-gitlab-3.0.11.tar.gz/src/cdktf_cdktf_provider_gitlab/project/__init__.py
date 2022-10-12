'''
# `gitlab_project`

Refer to the Terraform Registory for docs: [`gitlab_project`](https://www.terraform.io/docs/providers/gitlab/r/project).
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


class Project(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.project.Project",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/project gitlab_project}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        allow_merge_on_skipped_pipeline: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        analytics_access_level: typing.Optional[builtins.str] = None,
        approvals_before_merge: typing.Optional[jsii.Number] = None,
        archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archive_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_cancel_pending_pipelines: typing.Optional[builtins.str] = None,
        autoclose_referenced_issues: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_devops_deploy_strategy: typing.Optional[builtins.str] = None,
        auto_devops_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        build_coverage_regex: typing.Optional[builtins.str] = None,
        build_git_strategy: typing.Optional[builtins.str] = None,
        builds_access_level: typing.Optional[builtins.str] = None,
        build_timeout: typing.Optional[jsii.Number] = None,
        ci_config_path: typing.Optional[builtins.str] = None,
        ci_default_git_depth: typing.Optional[jsii.Number] = None,
        ci_forward_deployment_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        container_expiration_policy: typing.Optional[typing.Union["ProjectContainerExpirationPolicy", typing.Dict[str, typing.Any]]] = None,
        container_registry_access_level: typing.Optional[builtins.str] = None,
        container_registry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_branch: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        emails_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_authorization_classification_label: typing.Optional[builtins.str] = None,
        forking_access_level: typing.Optional[builtins.str] = None,
        group_with_project_templates_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        import_url: typing.Optional[builtins.str] = None,
        initialize_with_readme: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        issues_access_level: typing.Optional[builtins.str] = None,
        issues_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        issues_template: typing.Optional[builtins.str] = None,
        lfs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_commit_template: typing.Optional[builtins.str] = None,
        merge_method: typing.Optional[builtins.str] = None,
        merge_pipelines_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_requests_access_level: typing.Optional[builtins.str] = None,
        merge_requests_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_requests_template: typing.Optional[builtins.str] = None,
        merge_trains_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mirror: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mirror_overwrites_diverged_branches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mirror_trigger_builds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace_id: typing.Optional[jsii.Number] = None,
        only_allow_merge_if_all_discussions_are_resolved: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_allow_merge_if_pipeline_succeeds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_mirror_protected_branches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operations_access_level: typing.Optional[builtins.str] = None,
        packages_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pages_access_level: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        pipelines_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        printing_merge_request_link_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_builds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_rules: typing.Optional[typing.Union["ProjectPushRules", typing.Dict[str, typing.Any]]] = None,
        remove_source_branch_after_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repository_access_level: typing.Optional[builtins.str] = None,
        repository_storage: typing.Optional[builtins.str] = None,
        request_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        requirements_access_level: typing.Optional[builtins.str] = None,
        resolve_outdated_diff_discussions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_and_compliance_access_level: typing.Optional[builtins.str] = None,
        shared_runners_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_wait_for_default_branch_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snippets_access_level: typing.Optional[builtins.str] = None,
        snippets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        squash_commit_template: typing.Optional[builtins.str] = None,
        squash_option: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_name: typing.Optional[builtins.str] = None,
        template_project_id: typing.Optional[jsii.Number] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        use_custom_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        visibility_level: typing.Optional[builtins.str] = None,
        wiki_access_level: typing.Optional[builtins.str] = None,
        wiki_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/project gitlab_project} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name Project#name}
        :param allow_merge_on_skipped_pipeline: Set to true if you want to treat skipped pipelines as if they finished with success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#allow_merge_on_skipped_pipeline Project#allow_merge_on_skipped_pipeline}
        :param analytics_access_level: Set the analytics access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#analytics_access_level Project#analytics_access_level}
        :param approvals_before_merge: Number of merge request approvals required for merging. Default is 0. This field **does not** work well in combination with the ``gitlab_project_approval_rule`` resource and is most likely gonna be deprecated in a future GitLab version (see `this upstream epic <https://gitlab.com/groups/gitlab-org/-/epics/7572>`_). In the meantime we recommend against using this attribute and use ``gitlab_project_approval_rule`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#approvals_before_merge Project#approvals_before_merge}
        :param archived: Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#archived Project#archived}
        :param archive_on_destroy: Set to ``true`` to archive the project instead of deleting on destroy. If set to ``true`` it will entire omit the ``DELETE`` operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#archive_on_destroy Project#archive_on_destroy}
        :param auto_cancel_pending_pipelines: Auto-cancel pending pipelines. This isn’t a boolean, but enabled/disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_cancel_pending_pipelines Project#auto_cancel_pending_pipelines}
        :param autoclose_referenced_issues: Set whether auto-closing referenced issues on default branch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#autoclose_referenced_issues Project#autoclose_referenced_issues}
        :param auto_devops_deploy_strategy: Auto Deploy strategy. Valid values are ``continuous``, ``manual``, ``timed_incremental``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_devops_deploy_strategy Project#auto_devops_deploy_strategy}
        :param auto_devops_enabled: Enable Auto DevOps for this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_devops_enabled Project#auto_devops_enabled}
        :param build_coverage_regex: Test coverage parsing for the project. This is deprecated feature in GitLab 15.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_coverage_regex Project#build_coverage_regex}
        :param build_git_strategy: The Git strategy. Defaults to fetch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_git_strategy Project#build_git_strategy}
        :param builds_access_level: Set the builds access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#builds_access_level Project#builds_access_level}
        :param build_timeout: The maximum amount of time, in seconds, that a job can run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_timeout Project#build_timeout}
        :param ci_config_path: Custom Path to CI config file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_config_path Project#ci_config_path}
        :param ci_default_git_depth: Default number of revisions for shallow cloning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_default_git_depth Project#ci_default_git_depth}
        :param ci_forward_deployment_enabled: When a new deployment job starts, skip older deployment jobs that are still pending. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_forward_deployment_enabled Project#ci_forward_deployment_enabled}
        :param container_expiration_policy: container_expiration_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_expiration_policy Project#container_expiration_policy}
        :param container_registry_access_level: Set visibility of container registry, for this project. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_registry_access_level Project#container_registry_access_level}
        :param container_registry_enabled: Enable container registry for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_registry_enabled Project#container_registry_enabled}
        :param default_branch: The default branch for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#default_branch Project#default_branch}
        :param description: A description of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#description Project#description}
        :param emails_disabled: Disable email notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#emails_disabled Project#emails_disabled}
        :param external_authorization_classification_label: The classification label for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#external_authorization_classification_label Project#external_authorization_classification_label}
        :param forking_access_level: Set the forking access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#forking_access_level Project#forking_access_level}
        :param group_with_project_templates_id: For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true (enterprise edition). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#group_with_project_templates_id Project#group_with_project_templates_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#id Project#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_url: Git URL to a repository to be imported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#import_url Project#import_url}
        :param initialize_with_readme: Create main branch with first commit containing a README.md file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#initialize_with_readme Project#initialize_with_readme}
        :param issues_access_level: Set the issues access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_access_level Project#issues_access_level}
        :param issues_enabled: Enable issue tracking for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_enabled Project#issues_enabled}
        :param issues_template: Sets the template for new issues in the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_template Project#issues_template}
        :param lfs_enabled: Enable LFS for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#lfs_enabled Project#lfs_enabled}
        :param merge_commit_template: Template used to create merge commit message in merge requests. (Introduced in GitLab 14.5.). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_commit_template Project#merge_commit_template}
        :param merge_method: Set to ``ff`` to create fast-forward merges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_method Project#merge_method}
        :param merge_pipelines_enabled: Enable or disable merge pipelines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_pipelines_enabled Project#merge_pipelines_enabled}
        :param merge_requests_access_level: Set the merge requests access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_access_level Project#merge_requests_access_level}
        :param merge_requests_enabled: Enable merge requests for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_enabled Project#merge_requests_enabled}
        :param merge_requests_template: Sets the template for new merge requests in the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_template Project#merge_requests_template}
        :param merge_trains_enabled: Enable or disable merge trains. Requires ``merge_pipelines_enabled`` to be set to ``true`` to take effect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_trains_enabled Project#merge_trains_enabled}
        :param mirror: Enable project pull mirror. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror Project#mirror}
        :param mirror_overwrites_diverged_branches: Enable overwrite diverged branches for a mirrored project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror_overwrites_diverged_branches Project#mirror_overwrites_diverged_branches}
        :param mirror_trigger_builds: Enable trigger builds on pushes for a mirrored project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror_trigger_builds Project#mirror_trigger_builds}
        :param namespace_id: The namespace (group or user) of the project. Defaults to your user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#namespace_id Project#namespace_id}
        :param only_allow_merge_if_all_discussions_are_resolved: Set to true if you want allow merges only if all discussions are resolved. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_allow_merge_if_all_discussions_are_resolved Project#only_allow_merge_if_all_discussions_are_resolved}
        :param only_allow_merge_if_pipeline_succeeds: Set to true if you want allow merges only if a pipeline succeeds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_allow_merge_if_pipeline_succeeds Project#only_allow_merge_if_pipeline_succeeds}
        :param only_mirror_protected_branches: Enable only mirror protected branches for a mirrored project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_mirror_protected_branches Project#only_mirror_protected_branches}
        :param operations_access_level: Set the operations access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#operations_access_level Project#operations_access_level}
        :param packages_enabled: Enable packages repository for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#packages_enabled Project#packages_enabled}
        :param pages_access_level: Enable pages access control. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#pages_access_level Project#pages_access_level}
        :param path: The path of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#path Project#path}
        :param pipelines_enabled: Enable pipelines for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#pipelines_enabled Project#pipelines_enabled}
        :param printing_merge_request_link_enabled: Show link to create/view merge request when pushing from the command line. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#printing_merge_request_link_enabled Project#printing_merge_request_link_enabled}
        :param public_builds: If true, jobs can be viewed by non-project members. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#public_builds Project#public_builds}
        :param push_rules: push_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#push_rules Project#push_rules}
        :param remove_source_branch_after_merge: Enable ``Delete source branch`` option by default for all new merge requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#remove_source_branch_after_merge Project#remove_source_branch_after_merge}
        :param repository_access_level: Set the repository access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#repository_access_level Project#repository_access_level}
        :param repository_storage: Which storage shard the repository is on. (administrator only). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#repository_storage Project#repository_storage}
        :param request_access_enabled: Allow users to request member access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#request_access_enabled Project#request_access_enabled}
        :param requirements_access_level: Set the requirements access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#requirements_access_level Project#requirements_access_level}
        :param resolve_outdated_diff_discussions: Automatically resolve merge request diffs discussions on lines changed with a push. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#resolve_outdated_diff_discussions Project#resolve_outdated_diff_discussions}
        :param security_and_compliance_access_level: Set the security and compliance access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#security_and_compliance_access_level Project#security_and_compliance_access_level}
        :param shared_runners_enabled: Enable shared runners for this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#shared_runners_enabled Project#shared_runners_enabled}
        :param skip_wait_for_default_branch_protection: If ``true``, the default behavior to wait for the default branch protection to be created is skipped. This is necessary if the current user is not an admin and the default branch protection is disabled on an instance-level. There is currently no known way to determine if the default branch protection is disabled on an instance-level for non-admin users. This attribute is only used during resource creation, thus changes are suppressed and the attribute cannot be imported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#skip_wait_for_default_branch_protection Project#skip_wait_for_default_branch_protection}
        :param snippets_access_level: Set the snippets access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#snippets_access_level Project#snippets_access_level}
        :param snippets_enabled: Enable snippets for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#snippets_enabled Project#snippets_enabled}
        :param squash_commit_template: Template used to create squash commit message in merge requests. (Introduced in GitLab 14.6.). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#squash_commit_template Project#squash_commit_template}
        :param squash_option: Squash commits when merge request. Valid values are ``never``, ``always``, ``default_on``, or ``default_off``. The default value is ``default_off``. [GitLab >= 14.1] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#squash_option Project#squash_option}
        :param tags: The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#tags Project#tags}
        :param template_name: When used without use_custom_template, name of a built-in project template. When used with use_custom_template, name of a custom project template. This option is mutually exclusive with ``template_project_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#template_name Project#template_name}
        :param template_project_id: When used with use_custom_template, project ID of a custom project template. This is preferable to using template_name since template_name may be ambiguous (enterprise edition). This option is mutually exclusive with ``template_name``. See ``gitlab_group_project_file_template`` to set a project as a template project. If a project has not been set as a template, using it here will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#template_project_id Project#template_project_id}
        :param topics: The list of topics for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#topics Project#topics}
        :param use_custom_template: Use either custom instance or group (with group_with_project_templates_id) project template (enterprise edition). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#use_custom_template Project#use_custom_template}
        :param visibility_level: Set to ``public`` to create a public project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#visibility_level Project#visibility_level}
        :param wiki_access_level: Set the wiki access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#wiki_access_level Project#wiki_access_level}
        :param wiki_enabled: Enable wiki for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#wiki_enabled Project#wiki_enabled}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Project.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ProjectConfig(
            name=name,
            allow_merge_on_skipped_pipeline=allow_merge_on_skipped_pipeline,
            analytics_access_level=analytics_access_level,
            approvals_before_merge=approvals_before_merge,
            archived=archived,
            archive_on_destroy=archive_on_destroy,
            auto_cancel_pending_pipelines=auto_cancel_pending_pipelines,
            autoclose_referenced_issues=autoclose_referenced_issues,
            auto_devops_deploy_strategy=auto_devops_deploy_strategy,
            auto_devops_enabled=auto_devops_enabled,
            build_coverage_regex=build_coverage_regex,
            build_git_strategy=build_git_strategy,
            builds_access_level=builds_access_level,
            build_timeout=build_timeout,
            ci_config_path=ci_config_path,
            ci_default_git_depth=ci_default_git_depth,
            ci_forward_deployment_enabled=ci_forward_deployment_enabled,
            container_expiration_policy=container_expiration_policy,
            container_registry_access_level=container_registry_access_level,
            container_registry_enabled=container_registry_enabled,
            default_branch=default_branch,
            description=description,
            emails_disabled=emails_disabled,
            external_authorization_classification_label=external_authorization_classification_label,
            forking_access_level=forking_access_level,
            group_with_project_templates_id=group_with_project_templates_id,
            id=id,
            import_url=import_url,
            initialize_with_readme=initialize_with_readme,
            issues_access_level=issues_access_level,
            issues_enabled=issues_enabled,
            issues_template=issues_template,
            lfs_enabled=lfs_enabled,
            merge_commit_template=merge_commit_template,
            merge_method=merge_method,
            merge_pipelines_enabled=merge_pipelines_enabled,
            merge_requests_access_level=merge_requests_access_level,
            merge_requests_enabled=merge_requests_enabled,
            merge_requests_template=merge_requests_template,
            merge_trains_enabled=merge_trains_enabled,
            mirror=mirror,
            mirror_overwrites_diverged_branches=mirror_overwrites_diverged_branches,
            mirror_trigger_builds=mirror_trigger_builds,
            namespace_id=namespace_id,
            only_allow_merge_if_all_discussions_are_resolved=only_allow_merge_if_all_discussions_are_resolved,
            only_allow_merge_if_pipeline_succeeds=only_allow_merge_if_pipeline_succeeds,
            only_mirror_protected_branches=only_mirror_protected_branches,
            operations_access_level=operations_access_level,
            packages_enabled=packages_enabled,
            pages_access_level=pages_access_level,
            path=path,
            pipelines_enabled=pipelines_enabled,
            printing_merge_request_link_enabled=printing_merge_request_link_enabled,
            public_builds=public_builds,
            push_rules=push_rules,
            remove_source_branch_after_merge=remove_source_branch_after_merge,
            repository_access_level=repository_access_level,
            repository_storage=repository_storage,
            request_access_enabled=request_access_enabled,
            requirements_access_level=requirements_access_level,
            resolve_outdated_diff_discussions=resolve_outdated_diff_discussions,
            security_and_compliance_access_level=security_and_compliance_access_level,
            shared_runners_enabled=shared_runners_enabled,
            skip_wait_for_default_branch_protection=skip_wait_for_default_branch_protection,
            snippets_access_level=snippets_access_level,
            snippets_enabled=snippets_enabled,
            squash_commit_template=squash_commit_template,
            squash_option=squash_option,
            tags=tags,
            template_name=template_name,
            template_project_id=template_project_id,
            topics=topics,
            use_custom_template=use_custom_template,
            visibility_level=visibility_level,
            wiki_access_level=wiki_access_level,
            wiki_enabled=wiki_enabled,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putContainerExpirationPolicy")
    def put_container_expiration_policy(
        self,
        *,
        cadence: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        keep_n: typing.Optional[jsii.Number] = None,
        name_regex_delete: typing.Optional[builtins.str] = None,
        name_regex_keep: typing.Optional[builtins.str] = None,
        older_than: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cadence: The cadence of the policy. Valid values are: ``1d``, ``7d``, ``14d``, ``1month``, ``3month``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#cadence Project#cadence}
        :param enabled: If true, the policy is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#enabled Project#enabled}
        :param keep_n: The number of images to keep. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#keep_n Project#keep_n}
        :param name_regex_delete: The regular expression to match image names to delete. **Note**: the upstream API has some inconsistencies with the ``name_regex`` field here. It's basically unusable at the moment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name_regex_delete Project#name_regex_delete}
        :param name_regex_keep: The regular expression to match image names to keep. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name_regex_keep Project#name_regex_keep}
        :param older_than: The number of days to keep images. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#older_than Project#older_than}
        '''
        value = ProjectContainerExpirationPolicy(
            cadence=cadence,
            enabled=enabled,
            keep_n=keep_n,
            name_regex_delete=name_regex_delete,
            name_regex_keep=name_regex_keep,
            older_than=older_than,
        )

        return typing.cast(None, jsii.invoke(self, "putContainerExpirationPolicy", [value]))

    @jsii.member(jsii_name="putPushRules")
    def put_push_rules(
        self,
        *,
        author_email_regex: typing.Optional[builtins.str] = None,
        branch_name_regex: typing.Optional[builtins.str] = None,
        commit_committer_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        commit_message_negative_regex: typing.Optional[builtins.str] = None,
        commit_message_regex: typing.Optional[builtins.str] = None,
        deny_delete_tag: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        file_name_regex: typing.Optional[builtins.str] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        member_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        prevent_secrets: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reject_unsigned_commits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param author_email_regex: All commit author emails must match this regex, e.g. ``@my-company.com$``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#author_email_regex Project#author_email_regex}
        :param branch_name_regex: All branch names must match this regex, e.g. ``(feature|hotfix)\\/*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#branch_name_regex Project#branch_name_regex}
        :param commit_committer_check: Users can only push commits to this repository that were committed with one of their own verified emails. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_committer_check Project#commit_committer_check}
        :param commit_message_negative_regex: No commit message is allowed to match this regex, for example ``ssh\\:\\/\\/``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_message_negative_regex Project#commit_message_negative_regex}
        :param commit_message_regex: All commit messages must match this regex, e.g. ``Fixed \\d+\\..*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_message_regex Project#commit_message_regex}
        :param deny_delete_tag: Deny deleting a tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#deny_delete_tag Project#deny_delete_tag}
        :param file_name_regex: All commited filenames must not match this regex, e.g. ``(jar|exe)$``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#file_name_regex Project#file_name_regex}
        :param max_file_size: Maximum file size (MB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#max_file_size Project#max_file_size}
        :param member_check: Restrict commits by author (email) to existing GitLab users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#member_check Project#member_check}
        :param prevent_secrets: GitLab will reject any files that are likely to contain secrets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#prevent_secrets Project#prevent_secrets}
        :param reject_unsigned_commits: Reject commit when it’s not signed through GPG. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#reject_unsigned_commits Project#reject_unsigned_commits}
        '''
        value = ProjectPushRules(
            author_email_regex=author_email_regex,
            branch_name_regex=branch_name_regex,
            commit_committer_check=commit_committer_check,
            commit_message_negative_regex=commit_message_negative_regex,
            commit_message_regex=commit_message_regex,
            deny_delete_tag=deny_delete_tag,
            file_name_regex=file_name_regex,
            max_file_size=max_file_size,
            member_check=member_check,
            prevent_secrets=prevent_secrets,
            reject_unsigned_commits=reject_unsigned_commits,
        )

        return typing.cast(None, jsii.invoke(self, "putPushRules", [value]))

    @jsii.member(jsii_name="resetAllowMergeOnSkippedPipeline")
    def reset_allow_merge_on_skipped_pipeline(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMergeOnSkippedPipeline", []))

    @jsii.member(jsii_name="resetAnalyticsAccessLevel")
    def reset_analytics_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnalyticsAccessLevel", []))

    @jsii.member(jsii_name="resetApprovalsBeforeMerge")
    def reset_approvals_before_merge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovalsBeforeMerge", []))

    @jsii.member(jsii_name="resetArchived")
    def reset_archived(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchived", []))

    @jsii.member(jsii_name="resetArchiveOnDestroy")
    def reset_archive_on_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveOnDestroy", []))

    @jsii.member(jsii_name="resetAutoCancelPendingPipelines")
    def reset_auto_cancel_pending_pipelines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoCancelPendingPipelines", []))

    @jsii.member(jsii_name="resetAutocloseReferencedIssues")
    def reset_autoclose_referenced_issues(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutocloseReferencedIssues", []))

    @jsii.member(jsii_name="resetAutoDevopsDeployStrategy")
    def reset_auto_devops_deploy_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDevopsDeployStrategy", []))

    @jsii.member(jsii_name="resetAutoDevopsEnabled")
    def reset_auto_devops_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoDevopsEnabled", []))

    @jsii.member(jsii_name="resetBuildCoverageRegex")
    def reset_build_coverage_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCoverageRegex", []))

    @jsii.member(jsii_name="resetBuildGitStrategy")
    def reset_build_git_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildGitStrategy", []))

    @jsii.member(jsii_name="resetBuildsAccessLevel")
    def reset_builds_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildsAccessLevel", []))

    @jsii.member(jsii_name="resetBuildTimeout")
    def reset_build_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildTimeout", []))

    @jsii.member(jsii_name="resetCiConfigPath")
    def reset_ci_config_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCiConfigPath", []))

    @jsii.member(jsii_name="resetCiDefaultGitDepth")
    def reset_ci_default_git_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCiDefaultGitDepth", []))

    @jsii.member(jsii_name="resetCiForwardDeploymentEnabled")
    def reset_ci_forward_deployment_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCiForwardDeploymentEnabled", []))

    @jsii.member(jsii_name="resetContainerExpirationPolicy")
    def reset_container_expiration_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerExpirationPolicy", []))

    @jsii.member(jsii_name="resetContainerRegistryAccessLevel")
    def reset_container_registry_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistryAccessLevel", []))

    @jsii.member(jsii_name="resetContainerRegistryEnabled")
    def reset_container_registry_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistryEnabled", []))

    @jsii.member(jsii_name="resetDefaultBranch")
    def reset_default_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBranch", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEmailsDisabled")
    def reset_emails_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailsDisabled", []))

    @jsii.member(jsii_name="resetExternalAuthorizationClassificationLabel")
    def reset_external_authorization_classification_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalAuthorizationClassificationLabel", []))

    @jsii.member(jsii_name="resetForkingAccessLevel")
    def reset_forking_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForkingAccessLevel", []))

    @jsii.member(jsii_name="resetGroupWithProjectTemplatesId")
    def reset_group_with_project_templates_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupWithProjectTemplatesId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportUrl")
    def reset_import_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportUrl", []))

    @jsii.member(jsii_name="resetInitializeWithReadme")
    def reset_initialize_with_readme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitializeWithReadme", []))

    @jsii.member(jsii_name="resetIssuesAccessLevel")
    def reset_issues_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuesAccessLevel", []))

    @jsii.member(jsii_name="resetIssuesEnabled")
    def reset_issues_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuesEnabled", []))

    @jsii.member(jsii_name="resetIssuesTemplate")
    def reset_issues_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuesTemplate", []))

    @jsii.member(jsii_name="resetLfsEnabled")
    def reset_lfs_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLfsEnabled", []))

    @jsii.member(jsii_name="resetMergeCommitTemplate")
    def reset_merge_commit_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeCommitTemplate", []))

    @jsii.member(jsii_name="resetMergeMethod")
    def reset_merge_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeMethod", []))

    @jsii.member(jsii_name="resetMergePipelinesEnabled")
    def reset_merge_pipelines_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergePipelinesEnabled", []))

    @jsii.member(jsii_name="resetMergeRequestsAccessLevel")
    def reset_merge_requests_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsAccessLevel", []))

    @jsii.member(jsii_name="resetMergeRequestsEnabled")
    def reset_merge_requests_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsEnabled", []))

    @jsii.member(jsii_name="resetMergeRequestsTemplate")
    def reset_merge_requests_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeRequestsTemplate", []))

    @jsii.member(jsii_name="resetMergeTrainsEnabled")
    def reset_merge_trains_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMergeTrainsEnabled", []))

    @jsii.member(jsii_name="resetMirror")
    def reset_mirror(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMirror", []))

    @jsii.member(jsii_name="resetMirrorOverwritesDivergedBranches")
    def reset_mirror_overwrites_diverged_branches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMirrorOverwritesDivergedBranches", []))

    @jsii.member(jsii_name="resetMirrorTriggerBuilds")
    def reset_mirror_trigger_builds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMirrorTriggerBuilds", []))

    @jsii.member(jsii_name="resetNamespaceId")
    def reset_namespace_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespaceId", []))

    @jsii.member(jsii_name="resetOnlyAllowMergeIfAllDiscussionsAreResolved")
    def reset_only_allow_merge_if_all_discussions_are_resolved(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyAllowMergeIfAllDiscussionsAreResolved", []))

    @jsii.member(jsii_name="resetOnlyAllowMergeIfPipelineSucceeds")
    def reset_only_allow_merge_if_pipeline_succeeds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyAllowMergeIfPipelineSucceeds", []))

    @jsii.member(jsii_name="resetOnlyMirrorProtectedBranches")
    def reset_only_mirror_protected_branches(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyMirrorProtectedBranches", []))

    @jsii.member(jsii_name="resetOperationsAccessLevel")
    def reset_operations_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperationsAccessLevel", []))

    @jsii.member(jsii_name="resetPackagesEnabled")
    def reset_packages_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPackagesEnabled", []))

    @jsii.member(jsii_name="resetPagesAccessLevel")
    def reset_pages_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPagesAccessLevel", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPipelinesEnabled")
    def reset_pipelines_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPipelinesEnabled", []))

    @jsii.member(jsii_name="resetPrintingMergeRequestLinkEnabled")
    def reset_printing_merge_request_link_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrintingMergeRequestLinkEnabled", []))

    @jsii.member(jsii_name="resetPublicBuilds")
    def reset_public_builds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicBuilds", []))

    @jsii.member(jsii_name="resetPushRules")
    def reset_push_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushRules", []))

    @jsii.member(jsii_name="resetRemoveSourceBranchAfterMerge")
    def reset_remove_source_branch_after_merge(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRemoveSourceBranchAfterMerge", []))

    @jsii.member(jsii_name="resetRepositoryAccessLevel")
    def reset_repository_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepositoryAccessLevel", []))

    @jsii.member(jsii_name="resetRepositoryStorage")
    def reset_repository_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepositoryStorage", []))

    @jsii.member(jsii_name="resetRequestAccessEnabled")
    def reset_request_access_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestAccessEnabled", []))

    @jsii.member(jsii_name="resetRequirementsAccessLevel")
    def reset_requirements_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirementsAccessLevel", []))

    @jsii.member(jsii_name="resetResolveOutdatedDiffDiscussions")
    def reset_resolve_outdated_diff_discussions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolveOutdatedDiffDiscussions", []))

    @jsii.member(jsii_name="resetSecurityAndComplianceAccessLevel")
    def reset_security_and_compliance_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityAndComplianceAccessLevel", []))

    @jsii.member(jsii_name="resetSharedRunnersEnabled")
    def reset_shared_runners_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedRunnersEnabled", []))

    @jsii.member(jsii_name="resetSkipWaitForDefaultBranchProtection")
    def reset_skip_wait_for_default_branch_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipWaitForDefaultBranchProtection", []))

    @jsii.member(jsii_name="resetSnippetsAccessLevel")
    def reset_snippets_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnippetsAccessLevel", []))

    @jsii.member(jsii_name="resetSnippetsEnabled")
    def reset_snippets_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnippetsEnabled", []))

    @jsii.member(jsii_name="resetSquashCommitTemplate")
    def reset_squash_commit_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSquashCommitTemplate", []))

    @jsii.member(jsii_name="resetSquashOption")
    def reset_squash_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSquashOption", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTemplateName")
    def reset_template_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateName", []))

    @jsii.member(jsii_name="resetTemplateProjectId")
    def reset_template_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplateProjectId", []))

    @jsii.member(jsii_name="resetTopics")
    def reset_topics(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTopics", []))

    @jsii.member(jsii_name="resetUseCustomTemplate")
    def reset_use_custom_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseCustomTemplate", []))

    @jsii.member(jsii_name="resetVisibilityLevel")
    def reset_visibility_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibilityLevel", []))

    @jsii.member(jsii_name="resetWikiAccessLevel")
    def reset_wiki_access_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWikiAccessLevel", []))

    @jsii.member(jsii_name="resetWikiEnabled")
    def reset_wiki_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWikiEnabled", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="containerExpirationPolicy")
    def container_expiration_policy(
        self,
    ) -> "ProjectContainerExpirationPolicyOutputReference":
        return typing.cast("ProjectContainerExpirationPolicyOutputReference", jsii.get(self, "containerExpirationPolicy"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlToRepo")
    def http_url_to_repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpUrlToRepo"))

    @builtins.property
    @jsii.member(jsii_name="pathWithNamespace")
    def path_with_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathWithNamespace"))

    @builtins.property
    @jsii.member(jsii_name="pushRules")
    def push_rules(self) -> "ProjectPushRulesOutputReference":
        return typing.cast("ProjectPushRulesOutputReference", jsii.get(self, "pushRules"))

    @builtins.property
    @jsii.member(jsii_name="runnersToken")
    def runners_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runnersToken"))

    @builtins.property
    @jsii.member(jsii_name="sshUrlToRepo")
    def ssh_url_to_repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshUrlToRepo"))

    @builtins.property
    @jsii.member(jsii_name="webUrl")
    def web_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "webUrl"))

    @builtins.property
    @jsii.member(jsii_name="allowMergeOnSkippedPipelineInput")
    def allow_merge_on_skipped_pipeline_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowMergeOnSkippedPipelineInput"))

    @builtins.property
    @jsii.member(jsii_name="analyticsAccessLevelInput")
    def analytics_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "analyticsAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="approvalsBeforeMergeInput")
    def approvals_before_merge_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "approvalsBeforeMergeInput"))

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
    @jsii.member(jsii_name="autoCancelPendingPipelinesInput")
    def auto_cancel_pending_pipelines_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoCancelPendingPipelinesInput"))

    @builtins.property
    @jsii.member(jsii_name="autocloseReferencedIssuesInput")
    def autoclose_referenced_issues_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autocloseReferencedIssuesInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDevopsDeployStrategyInput")
    def auto_devops_deploy_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoDevopsDeployStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoDevopsEnabledInput")
    def auto_devops_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoDevopsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCoverageRegexInput")
    def build_coverage_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCoverageRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="buildGitStrategyInput")
    def build_git_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildGitStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="buildsAccessLevelInput")
    def builds_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildsAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="buildTimeoutInput")
    def build_timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "buildTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="ciConfigPathInput")
    def ci_config_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ciConfigPathInput"))

    @builtins.property
    @jsii.member(jsii_name="ciDefaultGitDepthInput")
    def ci_default_git_depth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ciDefaultGitDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="ciForwardDeploymentEnabledInput")
    def ci_forward_deployment_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ciForwardDeploymentEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="containerExpirationPolicyInput")
    def container_expiration_policy_input(
        self,
    ) -> typing.Optional["ProjectContainerExpirationPolicy"]:
        return typing.cast(typing.Optional["ProjectContainerExpirationPolicy"], jsii.get(self, "containerExpirationPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryAccessLevelInput")
    def container_registry_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistryEnabledInput")
    def container_registry_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "containerRegistryEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBranchInput")
    def default_branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBranchInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="emailsDisabledInput")
    def emails_disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "emailsDisabledInput"))

    @builtins.property
    @jsii.member(jsii_name="externalAuthorizationClassificationLabelInput")
    def external_authorization_classification_label_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalAuthorizationClassificationLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="forkingAccessLevelInput")
    def forking_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forkingAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="groupWithProjectTemplatesIdInput")
    def group_with_project_templates_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupWithProjectTemplatesIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importUrlInput")
    def import_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "importUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="initializeWithReadmeInput")
    def initialize_with_readme_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "initializeWithReadmeInput"))

    @builtins.property
    @jsii.member(jsii_name="issuesAccessLevelInput")
    def issues_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuesAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="issuesEnabledInput")
    def issues_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "issuesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="issuesTemplateInput")
    def issues_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuesTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="lfsEnabledInput")
    def lfs_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "lfsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeCommitTemplateInput")
    def merge_commit_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeCommitTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeMethodInput")
    def merge_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="mergePipelinesEnabledInput")
    def merge_pipelines_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mergePipelinesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsAccessLevelInput")
    def merge_requests_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeRequestsAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEnabledInput")
    def merge_requests_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mergeRequestsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsTemplateInput")
    def merge_requests_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mergeRequestsTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="mergeTrainsEnabledInput")
    def merge_trains_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mergeTrainsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="mirrorInput")
    def mirror_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mirrorInput"))

    @builtins.property
    @jsii.member(jsii_name="mirrorOverwritesDivergedBranchesInput")
    def mirror_overwrites_diverged_branches_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mirrorOverwritesDivergedBranchesInput"))

    @builtins.property
    @jsii.member(jsii_name="mirrorTriggerBuildsInput")
    def mirror_trigger_builds_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "mirrorTriggerBuildsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceIdInput")
    def namespace_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "namespaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyAllowMergeIfAllDiscussionsAreResolvedInput")
    def only_allow_merge_if_all_discussions_are_resolved_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyAllowMergeIfAllDiscussionsAreResolvedInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyAllowMergeIfPipelineSucceedsInput")
    def only_allow_merge_if_pipeline_succeeds_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyAllowMergeIfPipelineSucceedsInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyMirrorProtectedBranchesInput")
    def only_mirror_protected_branches_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyMirrorProtectedBranchesInput"))

    @builtins.property
    @jsii.member(jsii_name="operationsAccessLevelInput")
    def operations_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationsAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="packagesEnabledInput")
    def packages_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "packagesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="pagesAccessLevelInput")
    def pages_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pagesAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="pipelinesEnabledInput")
    def pipelines_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "pipelinesEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="printingMergeRequestLinkEnabledInput")
    def printing_merge_request_link_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "printingMergeRequestLinkEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="publicBuildsInput")
    def public_builds_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publicBuildsInput"))

    @builtins.property
    @jsii.member(jsii_name="pushRulesInput")
    def push_rules_input(self) -> typing.Optional["ProjectPushRules"]:
        return typing.cast(typing.Optional["ProjectPushRules"], jsii.get(self, "pushRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="removeSourceBranchAfterMergeInput")
    def remove_source_branch_after_merge_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "removeSourceBranchAfterMergeInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryAccessLevelInput")
    def repository_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryStorageInput")
    def repository_storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryStorageInput"))

    @builtins.property
    @jsii.member(jsii_name="requestAccessEnabledInput")
    def request_access_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requestAccessEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="requirementsAccessLevelInput")
    def requirements_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requirementsAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="resolveOutdatedDiffDiscussionsInput")
    def resolve_outdated_diff_discussions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "resolveOutdatedDiffDiscussionsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityAndComplianceAccessLevelInput")
    def security_and_compliance_access_level_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityAndComplianceAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedRunnersEnabledInput")
    def shared_runners_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sharedRunnersEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="skipWaitForDefaultBranchProtectionInput")
    def skip_wait_for_default_branch_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "skipWaitForDefaultBranchProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="snippetsAccessLevelInput")
    def snippets_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snippetsAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="snippetsEnabledInput")
    def snippets_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "snippetsEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="squashCommitTemplateInput")
    def squash_commit_template_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "squashCommitTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="squashOptionInput")
    def squash_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "squashOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="templateNameInput")
    def template_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateNameInput"))

    @builtins.property
    @jsii.member(jsii_name="templateProjectIdInput")
    def template_project_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "templateProjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="topicsInput")
    def topics_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "topicsInput"))

    @builtins.property
    @jsii.member(jsii_name="useCustomTemplateInput")
    def use_custom_template_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useCustomTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityLevelInput")
    def visibility_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="wikiAccessLevelInput")
    def wiki_access_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "wikiAccessLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="wikiEnabledInput")
    def wiki_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "wikiEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMergeOnSkippedPipeline")
    def allow_merge_on_skipped_pipeline(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowMergeOnSkippedPipeline"))

    @allow_merge_on_skipped_pipeline.setter
    def allow_merge_on_skipped_pipeline(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "allow_merge_on_skipped_pipeline").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMergeOnSkippedPipeline", value)

    @builtins.property
    @jsii.member(jsii_name="analyticsAccessLevel")
    def analytics_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "analyticsAccessLevel"))

    @analytics_access_level.setter
    def analytics_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "analytics_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "analyticsAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="approvalsBeforeMerge")
    def approvals_before_merge(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "approvalsBeforeMerge"))

    @approvals_before_merge.setter
    def approvals_before_merge(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "approvals_before_merge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalsBeforeMerge", value)

    @builtins.property
    @jsii.member(jsii_name="archived")
    def archived(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "archived"))

    @archived.setter
    def archived(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "archived").fset)
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
            type_hints = typing.get_type_hints(getattr(Project, "archive_on_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveOnDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="autoCancelPendingPipelines")
    def auto_cancel_pending_pipelines(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoCancelPendingPipelines"))

    @auto_cancel_pending_pipelines.setter
    def auto_cancel_pending_pipelines(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "auto_cancel_pending_pipelines").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoCancelPendingPipelines", value)

    @builtins.property
    @jsii.member(jsii_name="autocloseReferencedIssues")
    def autoclose_referenced_issues(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autocloseReferencedIssues"))

    @autoclose_referenced_issues.setter
    def autoclose_referenced_issues(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "autoclose_referenced_issues").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autocloseReferencedIssues", value)

    @builtins.property
    @jsii.member(jsii_name="autoDevopsDeployStrategy")
    def auto_devops_deploy_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoDevopsDeployStrategy"))

    @auto_devops_deploy_strategy.setter
    def auto_devops_deploy_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "auto_devops_deploy_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDevopsDeployStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="autoDevopsEnabled")
    def auto_devops_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoDevopsEnabled"))

    @auto_devops_enabled.setter
    def auto_devops_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "auto_devops_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDevopsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="buildCoverageRegex")
    def build_coverage_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCoverageRegex"))

    @build_coverage_regex.setter
    def build_coverage_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "build_coverage_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCoverageRegex", value)

    @builtins.property
    @jsii.member(jsii_name="buildGitStrategy")
    def build_git_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildGitStrategy"))

    @build_git_strategy.setter
    def build_git_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "build_git_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildGitStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="buildsAccessLevel")
    def builds_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildsAccessLevel"))

    @builds_access_level.setter
    def builds_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "builds_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildsAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="buildTimeout")
    def build_timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "buildTimeout"))

    @build_timeout.setter
    def build_timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "build_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="ciConfigPath")
    def ci_config_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ciConfigPath"))

    @ci_config_path.setter
    def ci_config_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "ci_config_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ciConfigPath", value)

    @builtins.property
    @jsii.member(jsii_name="ciDefaultGitDepth")
    def ci_default_git_depth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ciDefaultGitDepth"))

    @ci_default_git_depth.setter
    def ci_default_git_depth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "ci_default_git_depth").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ciDefaultGitDepth", value)

    @builtins.property
    @jsii.member(jsii_name="ciForwardDeploymentEnabled")
    def ci_forward_deployment_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ciForwardDeploymentEnabled"))

    @ci_forward_deployment_enabled.setter
    def ci_forward_deployment_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "ci_forward_deployment_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ciForwardDeploymentEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryAccessLevel")
    def container_registry_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerRegistryAccessLevel"))

    @container_registry_access_level.setter
    def container_registry_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "container_registry_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="containerRegistryEnabled")
    def container_registry_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "containerRegistryEnabled"))

    @container_registry_enabled.setter
    def container_registry_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "container_registry_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="defaultBranch")
    def default_branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBranch"))

    @default_branch.setter
    def default_branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "default_branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBranch", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="emailsDisabled")
    def emails_disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "emailsDisabled"))

    @emails_disabled.setter
    def emails_disabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "emails_disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailsDisabled", value)

    @builtins.property
    @jsii.member(jsii_name="externalAuthorizationClassificationLabel")
    def external_authorization_classification_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalAuthorizationClassificationLabel"))

    @external_authorization_classification_label.setter
    def external_authorization_classification_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "external_authorization_classification_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalAuthorizationClassificationLabel", value)

    @builtins.property
    @jsii.member(jsii_name="forkingAccessLevel")
    def forking_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forkingAccessLevel"))

    @forking_access_level.setter
    def forking_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "forking_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forkingAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="groupWithProjectTemplatesId")
    def group_with_project_templates_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupWithProjectTemplatesId"))

    @group_with_project_templates_id.setter
    def group_with_project_templates_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "group_with_project_templates_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupWithProjectTemplatesId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="importUrl")
    def import_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "importUrl"))

    @import_url.setter
    def import_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "import_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "importUrl", value)

    @builtins.property
    @jsii.member(jsii_name="initializeWithReadme")
    def initialize_with_readme(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "initializeWithReadme"))

    @initialize_with_readme.setter
    def initialize_with_readme(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "initialize_with_readme").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initializeWithReadme", value)

    @builtins.property
    @jsii.member(jsii_name="issuesAccessLevel")
    def issues_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuesAccessLevel"))

    @issues_access_level.setter
    def issues_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "issues_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuesAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="issuesEnabled")
    def issues_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "issuesEnabled"))

    @issues_enabled.setter
    def issues_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "issues_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="issuesTemplate")
    def issues_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuesTemplate"))

    @issues_template.setter
    def issues_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "issues_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuesTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="lfsEnabled")
    def lfs_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "lfsEnabled"))

    @lfs_enabled.setter
    def lfs_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "lfs_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lfsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mergeCommitTemplate")
    def merge_commit_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeCommitTemplate"))

    @merge_commit_template.setter
    def merge_commit_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "merge_commit_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeCommitTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="mergeMethod")
    def merge_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeMethod"))

    @merge_method.setter
    def merge_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "merge_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeMethod", value)

    @builtins.property
    @jsii.member(jsii_name="mergePipelinesEnabled")
    def merge_pipelines_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mergePipelinesEnabled"))

    @merge_pipelines_enabled.setter
    def merge_pipelines_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "merge_pipelines_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergePipelinesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsAccessLevel")
    def merge_requests_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeRequestsAccessLevel"))

    @merge_requests_access_level.setter
    def merge_requests_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "merge_requests_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsEnabled")
    def merge_requests_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mergeRequestsEnabled"))

    @merge_requests_enabled.setter
    def merge_requests_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "merge_requests_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mergeRequestsTemplate")
    def merge_requests_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mergeRequestsTemplate"))

    @merge_requests_template.setter
    def merge_requests_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "merge_requests_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeRequestsTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="mergeTrainsEnabled")
    def merge_trains_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mergeTrainsEnabled"))

    @merge_trains_enabled.setter
    def merge_trains_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "merge_trains_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mergeTrainsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="mirror")
    def mirror(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mirror"))

    @mirror.setter
    def mirror(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "mirror").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mirror", value)

    @builtins.property
    @jsii.member(jsii_name="mirrorOverwritesDivergedBranches")
    def mirror_overwrites_diverged_branches(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mirrorOverwritesDivergedBranches"))

    @mirror_overwrites_diverged_branches.setter
    def mirror_overwrites_diverged_branches(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "mirror_overwrites_diverged_branches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mirrorOverwritesDivergedBranches", value)

    @builtins.property
    @jsii.member(jsii_name="mirrorTriggerBuilds")
    def mirror_trigger_builds(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "mirrorTriggerBuilds"))

    @mirror_trigger_builds.setter
    def mirror_trigger_builds(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "mirror_trigger_builds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mirrorTriggerBuilds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "namespaceId"))

    @namespace_id.setter
    def namespace_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "namespace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceId", value)

    @builtins.property
    @jsii.member(jsii_name="onlyAllowMergeIfAllDiscussionsAreResolved")
    def only_allow_merge_if_all_discussions_are_resolved(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyAllowMergeIfAllDiscussionsAreResolved"))

    @only_allow_merge_if_all_discussions_are_resolved.setter
    def only_allow_merge_if_all_discussions_are_resolved(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "only_allow_merge_if_all_discussions_are_resolved").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyAllowMergeIfAllDiscussionsAreResolved", value)

    @builtins.property
    @jsii.member(jsii_name="onlyAllowMergeIfPipelineSucceeds")
    def only_allow_merge_if_pipeline_succeeds(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyAllowMergeIfPipelineSucceeds"))

    @only_allow_merge_if_pipeline_succeeds.setter
    def only_allow_merge_if_pipeline_succeeds(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "only_allow_merge_if_pipeline_succeeds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyAllowMergeIfPipelineSucceeds", value)

    @builtins.property
    @jsii.member(jsii_name="onlyMirrorProtectedBranches")
    def only_mirror_protected_branches(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyMirrorProtectedBranches"))

    @only_mirror_protected_branches.setter
    def only_mirror_protected_branches(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "only_mirror_protected_branches").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyMirrorProtectedBranches", value)

    @builtins.property
    @jsii.member(jsii_name="operationsAccessLevel")
    def operations_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operationsAccessLevel"))

    @operations_access_level.setter
    def operations_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "operations_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationsAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="packagesEnabled")
    def packages_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "packagesEnabled"))

    @packages_enabled.setter
    def packages_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "packages_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packagesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="pagesAccessLevel")
    def pages_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pagesAccessLevel"))

    @pages_access_level.setter
    def pages_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "pages_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pagesAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="pipelinesEnabled")
    def pipelines_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "pipelinesEnabled"))

    @pipelines_enabled.setter
    def pipelines_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "pipelines_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelinesEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="printingMergeRequestLinkEnabled")
    def printing_merge_request_link_enabled(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "printingMergeRequestLinkEnabled"))

    @printing_merge_request_link_enabled.setter
    def printing_merge_request_link_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "printing_merge_request_link_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "printingMergeRequestLinkEnabled", value)

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
            type_hints = typing.get_type_hints(getattr(Project, "public_builds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicBuilds", value)

    @builtins.property
    @jsii.member(jsii_name="removeSourceBranchAfterMerge")
    def remove_source_branch_after_merge(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "removeSourceBranchAfterMerge"))

    @remove_source_branch_after_merge.setter
    def remove_source_branch_after_merge(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "remove_source_branch_after_merge").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeSourceBranchAfterMerge", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryAccessLevel")
    def repository_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryAccessLevel"))

    @repository_access_level.setter
    def repository_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "repository_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryStorage")
    def repository_storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryStorage"))

    @repository_storage.setter
    def repository_storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "repository_storage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryStorage", value)

    @builtins.property
    @jsii.member(jsii_name="requestAccessEnabled")
    def request_access_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requestAccessEnabled"))

    @request_access_enabled.setter
    def request_access_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "request_access_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestAccessEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="requirementsAccessLevel")
    def requirements_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requirementsAccessLevel"))

    @requirements_access_level.setter
    def requirements_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "requirements_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirementsAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="resolveOutdatedDiffDiscussions")
    def resolve_outdated_diff_discussions(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "resolveOutdatedDiffDiscussions"))

    @resolve_outdated_diff_discussions.setter
    def resolve_outdated_diff_discussions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "resolve_outdated_diff_discussions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolveOutdatedDiffDiscussions", value)

    @builtins.property
    @jsii.member(jsii_name="securityAndComplianceAccessLevel")
    def security_and_compliance_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityAndComplianceAccessLevel"))

    @security_and_compliance_access_level.setter
    def security_and_compliance_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "security_and_compliance_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityAndComplianceAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="sharedRunnersEnabled")
    def shared_runners_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sharedRunnersEnabled"))

    @shared_runners_enabled.setter
    def shared_runners_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "shared_runners_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedRunnersEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="skipWaitForDefaultBranchProtection")
    def skip_wait_for_default_branch_protection(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "skipWaitForDefaultBranchProtection"))

    @skip_wait_for_default_branch_protection.setter
    def skip_wait_for_default_branch_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "skip_wait_for_default_branch_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipWaitForDefaultBranchProtection", value)

    @builtins.property
    @jsii.member(jsii_name="snippetsAccessLevel")
    def snippets_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snippetsAccessLevel"))

    @snippets_access_level.setter
    def snippets_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "snippets_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snippetsAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="snippetsEnabled")
    def snippets_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "snippetsEnabled"))

    @snippets_enabled.setter
    def snippets_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "snippets_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snippetsEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="squashCommitTemplate")
    def squash_commit_template(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "squashCommitTemplate"))

    @squash_commit_template.setter
    def squash_commit_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "squash_commit_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "squashCommitTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="squashOption")
    def squash_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "squashOption"))

    @squash_option.setter
    def squash_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "squash_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "squashOption", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="templateName")
    def template_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "templateName"))

    @template_name.setter
    def template_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "template_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateName", value)

    @builtins.property
    @jsii.member(jsii_name="templateProjectId")
    def template_project_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "templateProjectId"))

    @template_project_id.setter
    def template_project_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "template_project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateProjectId", value)

    @builtins.property
    @jsii.member(jsii_name="topics")
    def topics(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "topics"))

    @topics.setter
    def topics(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "topics").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topics", value)

    @builtins.property
    @jsii.member(jsii_name="useCustomTemplate")
    def use_custom_template(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useCustomTemplate"))

    @use_custom_template.setter
    def use_custom_template(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "use_custom_template").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useCustomTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="visibilityLevel")
    def visibility_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibilityLevel"))

    @visibility_level.setter
    def visibility_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "visibility_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibilityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="wikiAccessLevel")
    def wiki_access_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "wikiAccessLevel"))

    @wiki_access_level.setter
    def wiki_access_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "wiki_access_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wikiAccessLevel", value)

    @builtins.property
    @jsii.member(jsii_name="wikiEnabled")
    def wiki_enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "wikiEnabled"))

    @wiki_enabled.setter
    def wiki_enabled(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Project, "wiki_enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wikiEnabled", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.project.ProjectConfig",
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
        "allow_merge_on_skipped_pipeline": "allowMergeOnSkippedPipeline",
        "analytics_access_level": "analyticsAccessLevel",
        "approvals_before_merge": "approvalsBeforeMerge",
        "archived": "archived",
        "archive_on_destroy": "archiveOnDestroy",
        "auto_cancel_pending_pipelines": "autoCancelPendingPipelines",
        "autoclose_referenced_issues": "autocloseReferencedIssues",
        "auto_devops_deploy_strategy": "autoDevopsDeployStrategy",
        "auto_devops_enabled": "autoDevopsEnabled",
        "build_coverage_regex": "buildCoverageRegex",
        "build_git_strategy": "buildGitStrategy",
        "builds_access_level": "buildsAccessLevel",
        "build_timeout": "buildTimeout",
        "ci_config_path": "ciConfigPath",
        "ci_default_git_depth": "ciDefaultGitDepth",
        "ci_forward_deployment_enabled": "ciForwardDeploymentEnabled",
        "container_expiration_policy": "containerExpirationPolicy",
        "container_registry_access_level": "containerRegistryAccessLevel",
        "container_registry_enabled": "containerRegistryEnabled",
        "default_branch": "defaultBranch",
        "description": "description",
        "emails_disabled": "emailsDisabled",
        "external_authorization_classification_label": "externalAuthorizationClassificationLabel",
        "forking_access_level": "forkingAccessLevel",
        "group_with_project_templates_id": "groupWithProjectTemplatesId",
        "id": "id",
        "import_url": "importUrl",
        "initialize_with_readme": "initializeWithReadme",
        "issues_access_level": "issuesAccessLevel",
        "issues_enabled": "issuesEnabled",
        "issues_template": "issuesTemplate",
        "lfs_enabled": "lfsEnabled",
        "merge_commit_template": "mergeCommitTemplate",
        "merge_method": "mergeMethod",
        "merge_pipelines_enabled": "mergePipelinesEnabled",
        "merge_requests_access_level": "mergeRequestsAccessLevel",
        "merge_requests_enabled": "mergeRequestsEnabled",
        "merge_requests_template": "mergeRequestsTemplate",
        "merge_trains_enabled": "mergeTrainsEnabled",
        "mirror": "mirror",
        "mirror_overwrites_diverged_branches": "mirrorOverwritesDivergedBranches",
        "mirror_trigger_builds": "mirrorTriggerBuilds",
        "namespace_id": "namespaceId",
        "only_allow_merge_if_all_discussions_are_resolved": "onlyAllowMergeIfAllDiscussionsAreResolved",
        "only_allow_merge_if_pipeline_succeeds": "onlyAllowMergeIfPipelineSucceeds",
        "only_mirror_protected_branches": "onlyMirrorProtectedBranches",
        "operations_access_level": "operationsAccessLevel",
        "packages_enabled": "packagesEnabled",
        "pages_access_level": "pagesAccessLevel",
        "path": "path",
        "pipelines_enabled": "pipelinesEnabled",
        "printing_merge_request_link_enabled": "printingMergeRequestLinkEnabled",
        "public_builds": "publicBuilds",
        "push_rules": "pushRules",
        "remove_source_branch_after_merge": "removeSourceBranchAfterMerge",
        "repository_access_level": "repositoryAccessLevel",
        "repository_storage": "repositoryStorage",
        "request_access_enabled": "requestAccessEnabled",
        "requirements_access_level": "requirementsAccessLevel",
        "resolve_outdated_diff_discussions": "resolveOutdatedDiffDiscussions",
        "security_and_compliance_access_level": "securityAndComplianceAccessLevel",
        "shared_runners_enabled": "sharedRunnersEnabled",
        "skip_wait_for_default_branch_protection": "skipWaitForDefaultBranchProtection",
        "snippets_access_level": "snippetsAccessLevel",
        "snippets_enabled": "snippetsEnabled",
        "squash_commit_template": "squashCommitTemplate",
        "squash_option": "squashOption",
        "tags": "tags",
        "template_name": "templateName",
        "template_project_id": "templateProjectId",
        "topics": "topics",
        "use_custom_template": "useCustomTemplate",
        "visibility_level": "visibilityLevel",
        "wiki_access_level": "wikiAccessLevel",
        "wiki_enabled": "wikiEnabled",
    },
)
class ProjectConfig(cdktf.TerraformMetaArguments):
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
        allow_merge_on_skipped_pipeline: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        analytics_access_level: typing.Optional[builtins.str] = None,
        approvals_before_merge: typing.Optional[jsii.Number] = None,
        archived: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        archive_on_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_cancel_pending_pipelines: typing.Optional[builtins.str] = None,
        autoclose_referenced_issues: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auto_devops_deploy_strategy: typing.Optional[builtins.str] = None,
        auto_devops_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        build_coverage_regex: typing.Optional[builtins.str] = None,
        build_git_strategy: typing.Optional[builtins.str] = None,
        builds_access_level: typing.Optional[builtins.str] = None,
        build_timeout: typing.Optional[jsii.Number] = None,
        ci_config_path: typing.Optional[builtins.str] = None,
        ci_default_git_depth: typing.Optional[jsii.Number] = None,
        ci_forward_deployment_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        container_expiration_policy: typing.Optional[typing.Union["ProjectContainerExpirationPolicy", typing.Dict[str, typing.Any]]] = None,
        container_registry_access_level: typing.Optional[builtins.str] = None,
        container_registry_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_branch: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        emails_disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        external_authorization_classification_label: typing.Optional[builtins.str] = None,
        forking_access_level: typing.Optional[builtins.str] = None,
        group_with_project_templates_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        import_url: typing.Optional[builtins.str] = None,
        initialize_with_readme: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        issues_access_level: typing.Optional[builtins.str] = None,
        issues_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        issues_template: typing.Optional[builtins.str] = None,
        lfs_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_commit_template: typing.Optional[builtins.str] = None,
        merge_method: typing.Optional[builtins.str] = None,
        merge_pipelines_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_requests_access_level: typing.Optional[builtins.str] = None,
        merge_requests_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        merge_requests_template: typing.Optional[builtins.str] = None,
        merge_trains_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mirror: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mirror_overwrites_diverged_branches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mirror_trigger_builds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        namespace_id: typing.Optional[jsii.Number] = None,
        only_allow_merge_if_all_discussions_are_resolved: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_allow_merge_if_pipeline_succeeds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        only_mirror_protected_branches: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        operations_access_level: typing.Optional[builtins.str] = None,
        packages_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        pages_access_level: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        pipelines_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        printing_merge_request_link_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        public_builds: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        push_rules: typing.Optional[typing.Union["ProjectPushRules", typing.Dict[str, typing.Any]]] = None,
        remove_source_branch_after_merge: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repository_access_level: typing.Optional[builtins.str] = None,
        repository_storage: typing.Optional[builtins.str] = None,
        request_access_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        requirements_access_level: typing.Optional[builtins.str] = None,
        resolve_outdated_diff_discussions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        security_and_compliance_access_level: typing.Optional[builtins.str] = None,
        shared_runners_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        skip_wait_for_default_branch_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        snippets_access_level: typing.Optional[builtins.str] = None,
        snippets_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        squash_commit_template: typing.Optional[builtins.str] = None,
        squash_option: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_name: typing.Optional[builtins.str] = None,
        template_project_id: typing.Optional[jsii.Number] = None,
        topics: typing.Optional[typing.Sequence[builtins.str]] = None,
        use_custom_template: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        visibility_level: typing.Optional[builtins.str] = None,
        wiki_access_level: typing.Optional[builtins.str] = None,
        wiki_enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name Project#name}
        :param allow_merge_on_skipped_pipeline: Set to true if you want to treat skipped pipelines as if they finished with success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#allow_merge_on_skipped_pipeline Project#allow_merge_on_skipped_pipeline}
        :param analytics_access_level: Set the analytics access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#analytics_access_level Project#analytics_access_level}
        :param approvals_before_merge: Number of merge request approvals required for merging. Default is 0. This field **does not** work well in combination with the ``gitlab_project_approval_rule`` resource and is most likely gonna be deprecated in a future GitLab version (see `this upstream epic <https://gitlab.com/groups/gitlab-org/-/epics/7572>`_). In the meantime we recommend against using this attribute and use ``gitlab_project_approval_rule`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#approvals_before_merge Project#approvals_before_merge}
        :param archived: Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#archived Project#archived}
        :param archive_on_destroy: Set to ``true`` to archive the project instead of deleting on destroy. If set to ``true`` it will entire omit the ``DELETE`` operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#archive_on_destroy Project#archive_on_destroy}
        :param auto_cancel_pending_pipelines: Auto-cancel pending pipelines. This isn’t a boolean, but enabled/disabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_cancel_pending_pipelines Project#auto_cancel_pending_pipelines}
        :param autoclose_referenced_issues: Set whether auto-closing referenced issues on default branch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#autoclose_referenced_issues Project#autoclose_referenced_issues}
        :param auto_devops_deploy_strategy: Auto Deploy strategy. Valid values are ``continuous``, ``manual``, ``timed_incremental``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_devops_deploy_strategy Project#auto_devops_deploy_strategy}
        :param auto_devops_enabled: Enable Auto DevOps for this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_devops_enabled Project#auto_devops_enabled}
        :param build_coverage_regex: Test coverage parsing for the project. This is deprecated feature in GitLab 15.0. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_coverage_regex Project#build_coverage_regex}
        :param build_git_strategy: The Git strategy. Defaults to fetch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_git_strategy Project#build_git_strategy}
        :param builds_access_level: Set the builds access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#builds_access_level Project#builds_access_level}
        :param build_timeout: The maximum amount of time, in seconds, that a job can run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_timeout Project#build_timeout}
        :param ci_config_path: Custom Path to CI config file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_config_path Project#ci_config_path}
        :param ci_default_git_depth: Default number of revisions for shallow cloning. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_default_git_depth Project#ci_default_git_depth}
        :param ci_forward_deployment_enabled: When a new deployment job starts, skip older deployment jobs that are still pending. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_forward_deployment_enabled Project#ci_forward_deployment_enabled}
        :param container_expiration_policy: container_expiration_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_expiration_policy Project#container_expiration_policy}
        :param container_registry_access_level: Set visibility of container registry, for this project. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_registry_access_level Project#container_registry_access_level}
        :param container_registry_enabled: Enable container registry for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_registry_enabled Project#container_registry_enabled}
        :param default_branch: The default branch for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#default_branch Project#default_branch}
        :param description: A description of the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#description Project#description}
        :param emails_disabled: Disable email notifications. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#emails_disabled Project#emails_disabled}
        :param external_authorization_classification_label: The classification label for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#external_authorization_classification_label Project#external_authorization_classification_label}
        :param forking_access_level: Set the forking access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#forking_access_level Project#forking_access_level}
        :param group_with_project_templates_id: For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true (enterprise edition). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#group_with_project_templates_id Project#group_with_project_templates_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#id Project#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_url: Git URL to a repository to be imported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#import_url Project#import_url}
        :param initialize_with_readme: Create main branch with first commit containing a README.md file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#initialize_with_readme Project#initialize_with_readme}
        :param issues_access_level: Set the issues access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_access_level Project#issues_access_level}
        :param issues_enabled: Enable issue tracking for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_enabled Project#issues_enabled}
        :param issues_template: Sets the template for new issues in the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_template Project#issues_template}
        :param lfs_enabled: Enable LFS for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#lfs_enabled Project#lfs_enabled}
        :param merge_commit_template: Template used to create merge commit message in merge requests. (Introduced in GitLab 14.5.). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_commit_template Project#merge_commit_template}
        :param merge_method: Set to ``ff`` to create fast-forward merges. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_method Project#merge_method}
        :param merge_pipelines_enabled: Enable or disable merge pipelines. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_pipelines_enabled Project#merge_pipelines_enabled}
        :param merge_requests_access_level: Set the merge requests access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_access_level Project#merge_requests_access_level}
        :param merge_requests_enabled: Enable merge requests for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_enabled Project#merge_requests_enabled}
        :param merge_requests_template: Sets the template for new merge requests in the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_template Project#merge_requests_template}
        :param merge_trains_enabled: Enable or disable merge trains. Requires ``merge_pipelines_enabled`` to be set to ``true`` to take effect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_trains_enabled Project#merge_trains_enabled}
        :param mirror: Enable project pull mirror. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror Project#mirror}
        :param mirror_overwrites_diverged_branches: Enable overwrite diverged branches for a mirrored project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror_overwrites_diverged_branches Project#mirror_overwrites_diverged_branches}
        :param mirror_trigger_builds: Enable trigger builds on pushes for a mirrored project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror_trigger_builds Project#mirror_trigger_builds}
        :param namespace_id: The namespace (group or user) of the project. Defaults to your user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#namespace_id Project#namespace_id}
        :param only_allow_merge_if_all_discussions_are_resolved: Set to true if you want allow merges only if all discussions are resolved. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_allow_merge_if_all_discussions_are_resolved Project#only_allow_merge_if_all_discussions_are_resolved}
        :param only_allow_merge_if_pipeline_succeeds: Set to true if you want allow merges only if a pipeline succeeds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_allow_merge_if_pipeline_succeeds Project#only_allow_merge_if_pipeline_succeeds}
        :param only_mirror_protected_branches: Enable only mirror protected branches for a mirrored project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_mirror_protected_branches Project#only_mirror_protected_branches}
        :param operations_access_level: Set the operations access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#operations_access_level Project#operations_access_level}
        :param packages_enabled: Enable packages repository for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#packages_enabled Project#packages_enabled}
        :param pages_access_level: Enable pages access control. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#pages_access_level Project#pages_access_level}
        :param path: The path of the repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#path Project#path}
        :param pipelines_enabled: Enable pipelines for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#pipelines_enabled Project#pipelines_enabled}
        :param printing_merge_request_link_enabled: Show link to create/view merge request when pushing from the command line. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#printing_merge_request_link_enabled Project#printing_merge_request_link_enabled}
        :param public_builds: If true, jobs can be viewed by non-project members. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#public_builds Project#public_builds}
        :param push_rules: push_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#push_rules Project#push_rules}
        :param remove_source_branch_after_merge: Enable ``Delete source branch`` option by default for all new merge requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#remove_source_branch_after_merge Project#remove_source_branch_after_merge}
        :param repository_access_level: Set the repository access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#repository_access_level Project#repository_access_level}
        :param repository_storage: Which storage shard the repository is on. (administrator only). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#repository_storage Project#repository_storage}
        :param request_access_enabled: Allow users to request member access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#request_access_enabled Project#request_access_enabled}
        :param requirements_access_level: Set the requirements access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#requirements_access_level Project#requirements_access_level}
        :param resolve_outdated_diff_discussions: Automatically resolve merge request diffs discussions on lines changed with a push. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#resolve_outdated_diff_discussions Project#resolve_outdated_diff_discussions}
        :param security_and_compliance_access_level: Set the security and compliance access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#security_and_compliance_access_level Project#security_and_compliance_access_level}
        :param shared_runners_enabled: Enable shared runners for this project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#shared_runners_enabled Project#shared_runners_enabled}
        :param skip_wait_for_default_branch_protection: If ``true``, the default behavior to wait for the default branch protection to be created is skipped. This is necessary if the current user is not an admin and the default branch protection is disabled on an instance-level. There is currently no known way to determine if the default branch protection is disabled on an instance-level for non-admin users. This attribute is only used during resource creation, thus changes are suppressed and the attribute cannot be imported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#skip_wait_for_default_branch_protection Project#skip_wait_for_default_branch_protection}
        :param snippets_access_level: Set the snippets access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#snippets_access_level Project#snippets_access_level}
        :param snippets_enabled: Enable snippets for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#snippets_enabled Project#snippets_enabled}
        :param squash_commit_template: Template used to create squash commit message in merge requests. (Introduced in GitLab 14.6.). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#squash_commit_template Project#squash_commit_template}
        :param squash_option: Squash commits when merge request. Valid values are ``never``, ``always``, ``default_on``, or ``default_off``. The default value is ``default_off``. [GitLab >= 14.1] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#squash_option Project#squash_option}
        :param tags: The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#tags Project#tags}
        :param template_name: When used without use_custom_template, name of a built-in project template. When used with use_custom_template, name of a custom project template. This option is mutually exclusive with ``template_project_id``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#template_name Project#template_name}
        :param template_project_id: When used with use_custom_template, project ID of a custom project template. This is preferable to using template_name since template_name may be ambiguous (enterprise edition). This option is mutually exclusive with ``template_name``. See ``gitlab_group_project_file_template`` to set a project as a template project. If a project has not been set as a template, using it here will result in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#template_project_id Project#template_project_id}
        :param topics: The list of topics for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#topics Project#topics}
        :param use_custom_template: Use either custom instance or group (with group_with_project_templates_id) project template (enterprise edition). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#use_custom_template Project#use_custom_template}
        :param visibility_level: Set to ``public`` to create a public project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#visibility_level Project#visibility_level}
        :param wiki_access_level: Set the wiki access level. Valid values are ``disabled``, ``private``, ``enabled``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#wiki_access_level Project#wiki_access_level}
        :param wiki_enabled: Enable wiki for the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#wiki_enabled Project#wiki_enabled}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(container_expiration_policy, dict):
            container_expiration_policy = ProjectContainerExpirationPolicy(**container_expiration_policy)
        if isinstance(push_rules, dict):
            push_rules = ProjectPushRules(**push_rules)
        if __debug__:
            type_hints = typing.get_type_hints(ProjectConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allow_merge_on_skipped_pipeline", value=allow_merge_on_skipped_pipeline, expected_type=type_hints["allow_merge_on_skipped_pipeline"])
            check_type(argname="argument analytics_access_level", value=analytics_access_level, expected_type=type_hints["analytics_access_level"])
            check_type(argname="argument approvals_before_merge", value=approvals_before_merge, expected_type=type_hints["approvals_before_merge"])
            check_type(argname="argument archived", value=archived, expected_type=type_hints["archived"])
            check_type(argname="argument archive_on_destroy", value=archive_on_destroy, expected_type=type_hints["archive_on_destroy"])
            check_type(argname="argument auto_cancel_pending_pipelines", value=auto_cancel_pending_pipelines, expected_type=type_hints["auto_cancel_pending_pipelines"])
            check_type(argname="argument autoclose_referenced_issues", value=autoclose_referenced_issues, expected_type=type_hints["autoclose_referenced_issues"])
            check_type(argname="argument auto_devops_deploy_strategy", value=auto_devops_deploy_strategy, expected_type=type_hints["auto_devops_deploy_strategy"])
            check_type(argname="argument auto_devops_enabled", value=auto_devops_enabled, expected_type=type_hints["auto_devops_enabled"])
            check_type(argname="argument build_coverage_regex", value=build_coverage_regex, expected_type=type_hints["build_coverage_regex"])
            check_type(argname="argument build_git_strategy", value=build_git_strategy, expected_type=type_hints["build_git_strategy"])
            check_type(argname="argument builds_access_level", value=builds_access_level, expected_type=type_hints["builds_access_level"])
            check_type(argname="argument build_timeout", value=build_timeout, expected_type=type_hints["build_timeout"])
            check_type(argname="argument ci_config_path", value=ci_config_path, expected_type=type_hints["ci_config_path"])
            check_type(argname="argument ci_default_git_depth", value=ci_default_git_depth, expected_type=type_hints["ci_default_git_depth"])
            check_type(argname="argument ci_forward_deployment_enabled", value=ci_forward_deployment_enabled, expected_type=type_hints["ci_forward_deployment_enabled"])
            check_type(argname="argument container_expiration_policy", value=container_expiration_policy, expected_type=type_hints["container_expiration_policy"])
            check_type(argname="argument container_registry_access_level", value=container_registry_access_level, expected_type=type_hints["container_registry_access_level"])
            check_type(argname="argument container_registry_enabled", value=container_registry_enabled, expected_type=type_hints["container_registry_enabled"])
            check_type(argname="argument default_branch", value=default_branch, expected_type=type_hints["default_branch"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument emails_disabled", value=emails_disabled, expected_type=type_hints["emails_disabled"])
            check_type(argname="argument external_authorization_classification_label", value=external_authorization_classification_label, expected_type=type_hints["external_authorization_classification_label"])
            check_type(argname="argument forking_access_level", value=forking_access_level, expected_type=type_hints["forking_access_level"])
            check_type(argname="argument group_with_project_templates_id", value=group_with_project_templates_id, expected_type=type_hints["group_with_project_templates_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument import_url", value=import_url, expected_type=type_hints["import_url"])
            check_type(argname="argument initialize_with_readme", value=initialize_with_readme, expected_type=type_hints["initialize_with_readme"])
            check_type(argname="argument issues_access_level", value=issues_access_level, expected_type=type_hints["issues_access_level"])
            check_type(argname="argument issues_enabled", value=issues_enabled, expected_type=type_hints["issues_enabled"])
            check_type(argname="argument issues_template", value=issues_template, expected_type=type_hints["issues_template"])
            check_type(argname="argument lfs_enabled", value=lfs_enabled, expected_type=type_hints["lfs_enabled"])
            check_type(argname="argument merge_commit_template", value=merge_commit_template, expected_type=type_hints["merge_commit_template"])
            check_type(argname="argument merge_method", value=merge_method, expected_type=type_hints["merge_method"])
            check_type(argname="argument merge_pipelines_enabled", value=merge_pipelines_enabled, expected_type=type_hints["merge_pipelines_enabled"])
            check_type(argname="argument merge_requests_access_level", value=merge_requests_access_level, expected_type=type_hints["merge_requests_access_level"])
            check_type(argname="argument merge_requests_enabled", value=merge_requests_enabled, expected_type=type_hints["merge_requests_enabled"])
            check_type(argname="argument merge_requests_template", value=merge_requests_template, expected_type=type_hints["merge_requests_template"])
            check_type(argname="argument merge_trains_enabled", value=merge_trains_enabled, expected_type=type_hints["merge_trains_enabled"])
            check_type(argname="argument mirror", value=mirror, expected_type=type_hints["mirror"])
            check_type(argname="argument mirror_overwrites_diverged_branches", value=mirror_overwrites_diverged_branches, expected_type=type_hints["mirror_overwrites_diverged_branches"])
            check_type(argname="argument mirror_trigger_builds", value=mirror_trigger_builds, expected_type=type_hints["mirror_trigger_builds"])
            check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
            check_type(argname="argument only_allow_merge_if_all_discussions_are_resolved", value=only_allow_merge_if_all_discussions_are_resolved, expected_type=type_hints["only_allow_merge_if_all_discussions_are_resolved"])
            check_type(argname="argument only_allow_merge_if_pipeline_succeeds", value=only_allow_merge_if_pipeline_succeeds, expected_type=type_hints["only_allow_merge_if_pipeline_succeeds"])
            check_type(argname="argument only_mirror_protected_branches", value=only_mirror_protected_branches, expected_type=type_hints["only_mirror_protected_branches"])
            check_type(argname="argument operations_access_level", value=operations_access_level, expected_type=type_hints["operations_access_level"])
            check_type(argname="argument packages_enabled", value=packages_enabled, expected_type=type_hints["packages_enabled"])
            check_type(argname="argument pages_access_level", value=pages_access_level, expected_type=type_hints["pages_access_level"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument pipelines_enabled", value=pipelines_enabled, expected_type=type_hints["pipelines_enabled"])
            check_type(argname="argument printing_merge_request_link_enabled", value=printing_merge_request_link_enabled, expected_type=type_hints["printing_merge_request_link_enabled"])
            check_type(argname="argument public_builds", value=public_builds, expected_type=type_hints["public_builds"])
            check_type(argname="argument push_rules", value=push_rules, expected_type=type_hints["push_rules"])
            check_type(argname="argument remove_source_branch_after_merge", value=remove_source_branch_after_merge, expected_type=type_hints["remove_source_branch_after_merge"])
            check_type(argname="argument repository_access_level", value=repository_access_level, expected_type=type_hints["repository_access_level"])
            check_type(argname="argument repository_storage", value=repository_storage, expected_type=type_hints["repository_storage"])
            check_type(argname="argument request_access_enabled", value=request_access_enabled, expected_type=type_hints["request_access_enabled"])
            check_type(argname="argument requirements_access_level", value=requirements_access_level, expected_type=type_hints["requirements_access_level"])
            check_type(argname="argument resolve_outdated_diff_discussions", value=resolve_outdated_diff_discussions, expected_type=type_hints["resolve_outdated_diff_discussions"])
            check_type(argname="argument security_and_compliance_access_level", value=security_and_compliance_access_level, expected_type=type_hints["security_and_compliance_access_level"])
            check_type(argname="argument shared_runners_enabled", value=shared_runners_enabled, expected_type=type_hints["shared_runners_enabled"])
            check_type(argname="argument skip_wait_for_default_branch_protection", value=skip_wait_for_default_branch_protection, expected_type=type_hints["skip_wait_for_default_branch_protection"])
            check_type(argname="argument snippets_access_level", value=snippets_access_level, expected_type=type_hints["snippets_access_level"])
            check_type(argname="argument snippets_enabled", value=snippets_enabled, expected_type=type_hints["snippets_enabled"])
            check_type(argname="argument squash_commit_template", value=squash_commit_template, expected_type=type_hints["squash_commit_template"])
            check_type(argname="argument squash_option", value=squash_option, expected_type=type_hints["squash_option"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
            check_type(argname="argument template_project_id", value=template_project_id, expected_type=type_hints["template_project_id"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
            check_type(argname="argument use_custom_template", value=use_custom_template, expected_type=type_hints["use_custom_template"])
            check_type(argname="argument visibility_level", value=visibility_level, expected_type=type_hints["visibility_level"])
            check_type(argname="argument wiki_access_level", value=wiki_access_level, expected_type=type_hints["wiki_access_level"])
            check_type(argname="argument wiki_enabled", value=wiki_enabled, expected_type=type_hints["wiki_enabled"])
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
        if allow_merge_on_skipped_pipeline is not None:
            self._values["allow_merge_on_skipped_pipeline"] = allow_merge_on_skipped_pipeline
        if analytics_access_level is not None:
            self._values["analytics_access_level"] = analytics_access_level
        if approvals_before_merge is not None:
            self._values["approvals_before_merge"] = approvals_before_merge
        if archived is not None:
            self._values["archived"] = archived
        if archive_on_destroy is not None:
            self._values["archive_on_destroy"] = archive_on_destroy
        if auto_cancel_pending_pipelines is not None:
            self._values["auto_cancel_pending_pipelines"] = auto_cancel_pending_pipelines
        if autoclose_referenced_issues is not None:
            self._values["autoclose_referenced_issues"] = autoclose_referenced_issues
        if auto_devops_deploy_strategy is not None:
            self._values["auto_devops_deploy_strategy"] = auto_devops_deploy_strategy
        if auto_devops_enabled is not None:
            self._values["auto_devops_enabled"] = auto_devops_enabled
        if build_coverage_regex is not None:
            self._values["build_coverage_regex"] = build_coverage_regex
        if build_git_strategy is not None:
            self._values["build_git_strategy"] = build_git_strategy
        if builds_access_level is not None:
            self._values["builds_access_level"] = builds_access_level
        if build_timeout is not None:
            self._values["build_timeout"] = build_timeout
        if ci_config_path is not None:
            self._values["ci_config_path"] = ci_config_path
        if ci_default_git_depth is not None:
            self._values["ci_default_git_depth"] = ci_default_git_depth
        if ci_forward_deployment_enabled is not None:
            self._values["ci_forward_deployment_enabled"] = ci_forward_deployment_enabled
        if container_expiration_policy is not None:
            self._values["container_expiration_policy"] = container_expiration_policy
        if container_registry_access_level is not None:
            self._values["container_registry_access_level"] = container_registry_access_level
        if container_registry_enabled is not None:
            self._values["container_registry_enabled"] = container_registry_enabled
        if default_branch is not None:
            self._values["default_branch"] = default_branch
        if description is not None:
            self._values["description"] = description
        if emails_disabled is not None:
            self._values["emails_disabled"] = emails_disabled
        if external_authorization_classification_label is not None:
            self._values["external_authorization_classification_label"] = external_authorization_classification_label
        if forking_access_level is not None:
            self._values["forking_access_level"] = forking_access_level
        if group_with_project_templates_id is not None:
            self._values["group_with_project_templates_id"] = group_with_project_templates_id
        if id is not None:
            self._values["id"] = id
        if import_url is not None:
            self._values["import_url"] = import_url
        if initialize_with_readme is not None:
            self._values["initialize_with_readme"] = initialize_with_readme
        if issues_access_level is not None:
            self._values["issues_access_level"] = issues_access_level
        if issues_enabled is not None:
            self._values["issues_enabled"] = issues_enabled
        if issues_template is not None:
            self._values["issues_template"] = issues_template
        if lfs_enabled is not None:
            self._values["lfs_enabled"] = lfs_enabled
        if merge_commit_template is not None:
            self._values["merge_commit_template"] = merge_commit_template
        if merge_method is not None:
            self._values["merge_method"] = merge_method
        if merge_pipelines_enabled is not None:
            self._values["merge_pipelines_enabled"] = merge_pipelines_enabled
        if merge_requests_access_level is not None:
            self._values["merge_requests_access_level"] = merge_requests_access_level
        if merge_requests_enabled is not None:
            self._values["merge_requests_enabled"] = merge_requests_enabled
        if merge_requests_template is not None:
            self._values["merge_requests_template"] = merge_requests_template
        if merge_trains_enabled is not None:
            self._values["merge_trains_enabled"] = merge_trains_enabled
        if mirror is not None:
            self._values["mirror"] = mirror
        if mirror_overwrites_diverged_branches is not None:
            self._values["mirror_overwrites_diverged_branches"] = mirror_overwrites_diverged_branches
        if mirror_trigger_builds is not None:
            self._values["mirror_trigger_builds"] = mirror_trigger_builds
        if namespace_id is not None:
            self._values["namespace_id"] = namespace_id
        if only_allow_merge_if_all_discussions_are_resolved is not None:
            self._values["only_allow_merge_if_all_discussions_are_resolved"] = only_allow_merge_if_all_discussions_are_resolved
        if only_allow_merge_if_pipeline_succeeds is not None:
            self._values["only_allow_merge_if_pipeline_succeeds"] = only_allow_merge_if_pipeline_succeeds
        if only_mirror_protected_branches is not None:
            self._values["only_mirror_protected_branches"] = only_mirror_protected_branches
        if operations_access_level is not None:
            self._values["operations_access_level"] = operations_access_level
        if packages_enabled is not None:
            self._values["packages_enabled"] = packages_enabled
        if pages_access_level is not None:
            self._values["pages_access_level"] = pages_access_level
        if path is not None:
            self._values["path"] = path
        if pipelines_enabled is not None:
            self._values["pipelines_enabled"] = pipelines_enabled
        if printing_merge_request_link_enabled is not None:
            self._values["printing_merge_request_link_enabled"] = printing_merge_request_link_enabled
        if public_builds is not None:
            self._values["public_builds"] = public_builds
        if push_rules is not None:
            self._values["push_rules"] = push_rules
        if remove_source_branch_after_merge is not None:
            self._values["remove_source_branch_after_merge"] = remove_source_branch_after_merge
        if repository_access_level is not None:
            self._values["repository_access_level"] = repository_access_level
        if repository_storage is not None:
            self._values["repository_storage"] = repository_storage
        if request_access_enabled is not None:
            self._values["request_access_enabled"] = request_access_enabled
        if requirements_access_level is not None:
            self._values["requirements_access_level"] = requirements_access_level
        if resolve_outdated_diff_discussions is not None:
            self._values["resolve_outdated_diff_discussions"] = resolve_outdated_diff_discussions
        if security_and_compliance_access_level is not None:
            self._values["security_and_compliance_access_level"] = security_and_compliance_access_level
        if shared_runners_enabled is not None:
            self._values["shared_runners_enabled"] = shared_runners_enabled
        if skip_wait_for_default_branch_protection is not None:
            self._values["skip_wait_for_default_branch_protection"] = skip_wait_for_default_branch_protection
        if snippets_access_level is not None:
            self._values["snippets_access_level"] = snippets_access_level
        if snippets_enabled is not None:
            self._values["snippets_enabled"] = snippets_enabled
        if squash_commit_template is not None:
            self._values["squash_commit_template"] = squash_commit_template
        if squash_option is not None:
            self._values["squash_option"] = squash_option
        if tags is not None:
            self._values["tags"] = tags
        if template_name is not None:
            self._values["template_name"] = template_name
        if template_project_id is not None:
            self._values["template_project_id"] = template_project_id
        if topics is not None:
            self._values["topics"] = topics
        if use_custom_template is not None:
            self._values["use_custom_template"] = use_custom_template
        if visibility_level is not None:
            self._values["visibility_level"] = visibility_level
        if wiki_access_level is not None:
            self._values["wiki_access_level"] = wiki_access_level
        if wiki_enabled is not None:
            self._values["wiki_enabled"] = wiki_enabled

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
        '''The name of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name Project#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_merge_on_skipped_pipeline(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to true if you want to treat skipped pipelines as if they finished with success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#allow_merge_on_skipped_pipeline Project#allow_merge_on_skipped_pipeline}
        '''
        result = self._values.get("allow_merge_on_skipped_pipeline")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def analytics_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the analytics access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#analytics_access_level Project#analytics_access_level}
        '''
        result = self._values.get("analytics_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def approvals_before_merge(self) -> typing.Optional[jsii.Number]:
        '''Number of merge request approvals required for merging.

        Default is 0.
        This field **does not** work well in combination with the ``gitlab_project_approval_rule`` resource
        and is most likely gonna be deprecated in a future GitLab version (see `this upstream epic <https://gitlab.com/groups/gitlab-org/-/epics/7572>`_).
        In the meantime we recommend against using this attribute and use ``gitlab_project_approval_rule`` instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#approvals_before_merge Project#approvals_before_merge}
        '''
        result = self._values.get("approvals_before_merge")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def archived(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#archived Project#archived}
        '''
        result = self._values.get("archived")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def archive_on_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to ``true`` to archive the project instead of deleting on destroy.

        If set to ``true`` it will entire omit the ``DELETE`` operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#archive_on_destroy Project#archive_on_destroy}
        '''
        result = self._values.get("archive_on_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_cancel_pending_pipelines(self) -> typing.Optional[builtins.str]:
        '''Auto-cancel pending pipelines. This isn’t a boolean, but enabled/disabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_cancel_pending_pipelines Project#auto_cancel_pending_pipelines}
        '''
        result = self._values.get("auto_cancel_pending_pipelines")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def autoclose_referenced_issues(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set whether auto-closing referenced issues on default branch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#autoclose_referenced_issues Project#autoclose_referenced_issues}
        '''
        result = self._values.get("autoclose_referenced_issues")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auto_devops_deploy_strategy(self) -> typing.Optional[builtins.str]:
        '''Auto Deploy strategy. Valid values are ``continuous``, ``manual``, ``timed_incremental``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_devops_deploy_strategy Project#auto_devops_deploy_strategy}
        '''
        result = self._values.get("auto_devops_deploy_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_devops_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable Auto DevOps for this project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#auto_devops_enabled Project#auto_devops_enabled}
        '''
        result = self._values.get("auto_devops_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def build_coverage_regex(self) -> typing.Optional[builtins.str]:
        '''Test coverage parsing for the project. This is deprecated feature in GitLab 15.0.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_coverage_regex Project#build_coverage_regex}
        '''
        result = self._values.get("build_coverage_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_git_strategy(self) -> typing.Optional[builtins.str]:
        '''The Git strategy. Defaults to fetch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_git_strategy Project#build_git_strategy}
        '''
        result = self._values.get("build_git_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def builds_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the builds access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#builds_access_level Project#builds_access_level}
        '''
        result = self._values.get("builds_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_timeout(self) -> typing.Optional[jsii.Number]:
        '''The maximum amount of time, in seconds, that a job can run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#build_timeout Project#build_timeout}
        '''
        result = self._values.get("build_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ci_config_path(self) -> typing.Optional[builtins.str]:
        '''Custom Path to CI config file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_config_path Project#ci_config_path}
        '''
        result = self._values.get("ci_config_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ci_default_git_depth(self) -> typing.Optional[jsii.Number]:
        '''Default number of revisions for shallow cloning.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_default_git_depth Project#ci_default_git_depth}
        '''
        result = self._values.get("ci_default_git_depth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ci_forward_deployment_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When a new deployment job starts, skip older deployment jobs that are still pending.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#ci_forward_deployment_enabled Project#ci_forward_deployment_enabled}
        '''
        result = self._values.get("ci_forward_deployment_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def container_expiration_policy(
        self,
    ) -> typing.Optional["ProjectContainerExpirationPolicy"]:
        '''container_expiration_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_expiration_policy Project#container_expiration_policy}
        '''
        result = self._values.get("container_expiration_policy")
        return typing.cast(typing.Optional["ProjectContainerExpirationPolicy"], result)

    @builtins.property
    def container_registry_access_level(self) -> typing.Optional[builtins.str]:
        '''Set visibility of container registry, for this project. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_registry_access_level Project#container_registry_access_level}
        '''
        result = self._values.get("container_registry_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable container registry for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#container_registry_enabled Project#container_registry_enabled}
        '''
        result = self._values.get("container_registry_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def default_branch(self) -> typing.Optional[builtins.str]:
        '''The default branch for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#default_branch Project#default_branch}
        '''
        result = self._values.get("default_branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#description Project#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def emails_disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Disable email notifications.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#emails_disabled Project#emails_disabled}
        '''
        result = self._values.get("emails_disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def external_authorization_classification_label(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The classification label for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#external_authorization_classification_label Project#external_authorization_classification_label}
        '''
        result = self._values.get("external_authorization_classification_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forking_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the forking access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#forking_access_level Project#forking_access_level}
        '''
        result = self._values.get("forking_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_with_project_templates_id(self) -> typing.Optional[jsii.Number]:
        '''For group-level custom templates, specifies ID of group from which all the custom project templates are sourced.

        Leave empty for instance-level templates. Requires use_custom_template to be true (enterprise edition).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#group_with_project_templates_id Project#group_with_project_templates_id}
        '''
        result = self._values.get("group_with_project_templates_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#id Project#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_url(self) -> typing.Optional[builtins.str]:
        '''Git URL to a repository to be imported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#import_url Project#import_url}
        '''
        result = self._values.get("import_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initialize_with_readme(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Create main branch with first commit containing a README.md file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#initialize_with_readme Project#initialize_with_readme}
        '''
        result = self._values.get("initialize_with_readme")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def issues_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the issues access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_access_level Project#issues_access_level}
        '''
        result = self._values.get("issues_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issues_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable issue tracking for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_enabled Project#issues_enabled}
        '''
        result = self._values.get("issues_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def issues_template(self) -> typing.Optional[builtins.str]:
        '''Sets the template for new issues in the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#issues_template Project#issues_template}
        '''
        result = self._values.get("issues_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lfs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable LFS for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#lfs_enabled Project#lfs_enabled}
        '''
        result = self._values.get("lfs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def merge_commit_template(self) -> typing.Optional[builtins.str]:
        '''Template used to create merge commit message in merge requests. (Introduced in GitLab 14.5.).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_commit_template Project#merge_commit_template}
        '''
        result = self._values.get("merge_commit_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_method(self) -> typing.Optional[builtins.str]:
        '''Set to ``ff`` to create fast-forward merges.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_method Project#merge_method}
        '''
        result = self._values.get("merge_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_pipelines_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable or disable merge pipelines.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_pipelines_enabled Project#merge_pipelines_enabled}
        '''
        result = self._values.get("merge_pipelines_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def merge_requests_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the merge requests access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_access_level Project#merge_requests_access_level}
        '''
        result = self._values.get("merge_requests_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_requests_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable merge requests for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_enabled Project#merge_requests_enabled}
        '''
        result = self._values.get("merge_requests_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def merge_requests_template(self) -> typing.Optional[builtins.str]:
        '''Sets the template for new merge requests in the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_requests_template Project#merge_requests_template}
        '''
        result = self._values.get("merge_requests_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def merge_trains_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable or disable merge trains. Requires ``merge_pipelines_enabled`` to be set to ``true`` to take effect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#merge_trains_enabled Project#merge_trains_enabled}
        '''
        result = self._values.get("merge_trains_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def mirror(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable project pull mirror.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror Project#mirror}
        '''
        result = self._values.get("mirror")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def mirror_overwrites_diverged_branches(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable overwrite diverged branches for a mirrored project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror_overwrites_diverged_branches Project#mirror_overwrites_diverged_branches}
        '''
        result = self._values.get("mirror_overwrites_diverged_branches")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def mirror_trigger_builds(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable trigger builds on pushes for a mirrored project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#mirror_trigger_builds Project#mirror_trigger_builds}
        '''
        result = self._values.get("mirror_trigger_builds")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def namespace_id(self) -> typing.Optional[jsii.Number]:
        '''The namespace (group or user) of the project. Defaults to your user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#namespace_id Project#namespace_id}
        '''
        result = self._values.get("namespace_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def only_allow_merge_if_all_discussions_are_resolved(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to true if you want allow merges only if all discussions are resolved.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_allow_merge_if_all_discussions_are_resolved Project#only_allow_merge_if_all_discussions_are_resolved}
        '''
        result = self._values.get("only_allow_merge_if_all_discussions_are_resolved")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def only_allow_merge_if_pipeline_succeeds(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Set to true if you want allow merges only if a pipeline succeeds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_allow_merge_if_pipeline_succeeds Project#only_allow_merge_if_pipeline_succeeds}
        '''
        result = self._values.get("only_allow_merge_if_pipeline_succeeds")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def only_mirror_protected_branches(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable only mirror protected branches for a mirrored project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#only_mirror_protected_branches Project#only_mirror_protected_branches}
        '''
        result = self._values.get("only_mirror_protected_branches")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def operations_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the operations access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#operations_access_level Project#operations_access_level}
        '''
        result = self._values.get("operations_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def packages_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable packages repository for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#packages_enabled Project#packages_enabled}
        '''
        result = self._values.get("packages_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def pages_access_level(self) -> typing.Optional[builtins.str]:
        '''Enable pages access control.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#pages_access_level Project#pages_access_level}
        '''
        result = self._values.get("pages_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path of the repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#path Project#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipelines_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable pipelines for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#pipelines_enabled Project#pipelines_enabled}
        '''
        result = self._values.get("pipelines_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def printing_merge_request_link_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Show link to create/view merge request when pushing from the command line.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#printing_merge_request_link_enabled Project#printing_merge_request_link_enabled}
        '''
        result = self._values.get("printing_merge_request_link_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def public_builds(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, jobs can be viewed by non-project members.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#public_builds Project#public_builds}
        '''
        result = self._values.get("public_builds")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def push_rules(self) -> typing.Optional["ProjectPushRules"]:
        '''push_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#push_rules Project#push_rules}
        '''
        result = self._values.get("push_rules")
        return typing.cast(typing.Optional["ProjectPushRules"], result)

    @builtins.property
    def remove_source_branch_after_merge(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable ``Delete source branch`` option by default for all new merge requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#remove_source_branch_after_merge Project#remove_source_branch_after_merge}
        '''
        result = self._values.get("remove_source_branch_after_merge")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repository_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the repository access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#repository_access_level Project#repository_access_level}
        '''
        result = self._values.get("repository_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repository_storage(self) -> typing.Optional[builtins.str]:
        '''Which storage shard the repository is on. (administrator only).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#repository_storage Project#repository_storage}
        '''
        result = self._values.get("repository_storage")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_access_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow users to request member access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#request_access_enabled Project#request_access_enabled}
        '''
        result = self._values.get("request_access_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def requirements_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the requirements access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#requirements_access_level Project#requirements_access_level}
        '''
        result = self._values.get("requirements_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolve_outdated_diff_discussions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Automatically resolve merge request diffs discussions on lines changed with a push.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#resolve_outdated_diff_discussions Project#resolve_outdated_diff_discussions}
        '''
        result = self._values.get("resolve_outdated_diff_discussions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def security_and_compliance_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the security and compliance access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#security_and_compliance_access_level Project#security_and_compliance_access_level}
        '''
        result = self._values.get("security_and_compliance_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shared_runners_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable shared runners for this project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#shared_runners_enabled Project#shared_runners_enabled}
        '''
        result = self._values.get("shared_runners_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def skip_wait_for_default_branch_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If ``true``, the default behavior to wait for the default branch protection to be created is skipped.

        This is necessary if the current user is not an admin and the default branch protection is disabled on an instance-level.
        There is currently no known way to determine if the default branch protection is disabled on an instance-level for non-admin users.
        This attribute is only used during resource creation, thus changes are suppressed and the attribute cannot be imported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#skip_wait_for_default_branch_protection Project#skip_wait_for_default_branch_protection}
        '''
        result = self._values.get("skip_wait_for_default_branch_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def snippets_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the snippets access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#snippets_access_level Project#snippets_access_level}
        '''
        result = self._values.get("snippets_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snippets_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable snippets for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#snippets_enabled Project#snippets_enabled}
        '''
        result = self._values.get("snippets_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def squash_commit_template(self) -> typing.Optional[builtins.str]:
        '''Template used to create squash commit message in merge requests. (Introduced in GitLab 14.6.).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#squash_commit_template Project#squash_commit_template}
        '''
        result = self._values.get("squash_commit_template")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def squash_option(self) -> typing.Optional[builtins.str]:
        '''Squash commits when merge request.

        Valid values are ``never``, ``always``, ``default_on``, or ``default_off``. The default value is ``default_off``. [GitLab >= 14.1]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#squash_option Project#squash_option}
        '''
        result = self._values.get("squash_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of tags for a project;

        put array of tags, that should be finally assigned to a project. Use topics instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#tags Project#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template_name(self) -> typing.Optional[builtins.str]:
        '''When used without use_custom_template, name of a built-in project template.

        When used with use_custom_template, name of a custom project template. This option is mutually exclusive with ``template_project_id``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#template_name Project#template_name}
        '''
        result = self._values.get("template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_project_id(self) -> typing.Optional[jsii.Number]:
        '''When used with use_custom_template, project ID of a custom project template.

        This is preferable to using template_name since template_name may be ambiguous (enterprise edition). This option is mutually exclusive with ``template_name``. See ``gitlab_group_project_file_template`` to set a project as a template project. If a project has not been set as a template, using it here will result in an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#template_project_id Project#template_project_id}
        '''
        result = self._values.get("template_project_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of topics for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#topics Project#topics}
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def use_custom_template(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Use either custom instance or group (with group_with_project_templates_id) project template (enterprise edition).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#use_custom_template Project#use_custom_template}
        '''
        result = self._values.get("use_custom_template")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def visibility_level(self) -> typing.Optional[builtins.str]:
        '''Set to ``public`` to create a public project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#visibility_level Project#visibility_level}
        '''
        result = self._values.get("visibility_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wiki_access_level(self) -> typing.Optional[builtins.str]:
        '''Set the wiki access level. Valid values are ``disabled``, ``private``, ``enabled``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#wiki_access_level Project#wiki_access_level}
        '''
        result = self._values.get("wiki_access_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wiki_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enable wiki for the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#wiki_enabled Project#wiki_enabled}
        '''
        result = self._values.get("wiki_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.project.ProjectContainerExpirationPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "cadence": "cadence",
        "enabled": "enabled",
        "keep_n": "keepN",
        "name_regex_delete": "nameRegexDelete",
        "name_regex_keep": "nameRegexKeep",
        "older_than": "olderThan",
    },
)
class ProjectContainerExpirationPolicy:
    def __init__(
        self,
        *,
        cadence: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        keep_n: typing.Optional[jsii.Number] = None,
        name_regex_delete: typing.Optional[builtins.str] = None,
        name_regex_keep: typing.Optional[builtins.str] = None,
        older_than: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cadence: The cadence of the policy. Valid values are: ``1d``, ``7d``, ``14d``, ``1month``, ``3month``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#cadence Project#cadence}
        :param enabled: If true, the policy is enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#enabled Project#enabled}
        :param keep_n: The number of images to keep. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#keep_n Project#keep_n}
        :param name_regex_delete: The regular expression to match image names to delete. **Note**: the upstream API has some inconsistencies with the ``name_regex`` field here. It's basically unusable at the moment. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name_regex_delete Project#name_regex_delete}
        :param name_regex_keep: The regular expression to match image names to keep. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name_regex_keep Project#name_regex_keep}
        :param older_than: The number of days to keep images. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#older_than Project#older_than}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProjectContainerExpirationPolicy.__init__)
            check_type(argname="argument cadence", value=cadence, expected_type=type_hints["cadence"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument keep_n", value=keep_n, expected_type=type_hints["keep_n"])
            check_type(argname="argument name_regex_delete", value=name_regex_delete, expected_type=type_hints["name_regex_delete"])
            check_type(argname="argument name_regex_keep", value=name_regex_keep, expected_type=type_hints["name_regex_keep"])
            check_type(argname="argument older_than", value=older_than, expected_type=type_hints["older_than"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cadence is not None:
            self._values["cadence"] = cadence
        if enabled is not None:
            self._values["enabled"] = enabled
        if keep_n is not None:
            self._values["keep_n"] = keep_n
        if name_regex_delete is not None:
            self._values["name_regex_delete"] = name_regex_delete
        if name_regex_keep is not None:
            self._values["name_regex_keep"] = name_regex_keep
        if older_than is not None:
            self._values["older_than"] = older_than

    @builtins.property
    def cadence(self) -> typing.Optional[builtins.str]:
        '''The cadence of the policy. Valid values are: ``1d``, ``7d``, ``14d``, ``1month``, ``3month``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#cadence Project#cadence}
        '''
        result = self._values.get("cadence")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the policy is enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#enabled Project#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def keep_n(self) -> typing.Optional[jsii.Number]:
        '''The number of images to keep.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#keep_n Project#keep_n}
        '''
        result = self._values.get("keep_n")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name_regex_delete(self) -> typing.Optional[builtins.str]:
        '''The regular expression to match image names to delete.

        **Note**: the upstream API has some inconsistencies with the ``name_regex`` field here. It's basically unusable at the moment.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name_regex_delete Project#name_regex_delete}
        '''
        result = self._values.get("name_regex_delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_regex_keep(self) -> typing.Optional[builtins.str]:
        '''The regular expression to match image names to keep.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#name_regex_keep Project#name_regex_keep}
        '''
        result = self._values.get("name_regex_keep")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def older_than(self) -> typing.Optional[builtins.str]:
        '''The number of days to keep images.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#older_than Project#older_than}
        '''
        result = self._values.get("older_than")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectContainerExpirationPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectContainerExpirationPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.project.ProjectContainerExpirationPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ProjectContainerExpirationPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCadence")
    def reset_cadence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCadence", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetKeepN")
    def reset_keep_n(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeepN", []))

    @jsii.member(jsii_name="resetNameRegexDelete")
    def reset_name_regex_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameRegexDelete", []))

    @jsii.member(jsii_name="resetNameRegexKeep")
    def reset_name_regex_keep(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameRegexKeep", []))

    @jsii.member(jsii_name="resetOlderThan")
    def reset_older_than(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOlderThan", []))

    @builtins.property
    @jsii.member(jsii_name="nextRunAt")
    def next_run_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextRunAt"))

    @builtins.property
    @jsii.member(jsii_name="cadenceInput")
    def cadence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cadenceInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="keepNInput")
    def keep_n_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keepNInput"))

    @builtins.property
    @jsii.member(jsii_name="nameRegexDeleteInput")
    def name_regex_delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameRegexDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="nameRegexKeepInput")
    def name_regex_keep_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameRegexKeepInput"))

    @builtins.property
    @jsii.member(jsii_name="olderThanInput")
    def older_than_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "olderThanInput"))

    @builtins.property
    @jsii.member(jsii_name="cadence")
    def cadence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cadence"))

    @cadence.setter
    def cadence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectContainerExpirationPolicyOutputReference, "cadence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cadence", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectContainerExpirationPolicyOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="keepN")
    def keep_n(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keepN"))

    @keep_n.setter
    def keep_n(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectContainerExpirationPolicyOutputReference, "keep_n").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keepN", value)

    @builtins.property
    @jsii.member(jsii_name="nameRegexDelete")
    def name_regex_delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameRegexDelete"))

    @name_regex_delete.setter
    def name_regex_delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectContainerExpirationPolicyOutputReference, "name_regex_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameRegexDelete", value)

    @builtins.property
    @jsii.member(jsii_name="nameRegexKeep")
    def name_regex_keep(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nameRegexKeep"))

    @name_regex_keep.setter
    def name_regex_keep(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectContainerExpirationPolicyOutputReference, "name_regex_keep").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameRegexKeep", value)

    @builtins.property
    @jsii.member(jsii_name="olderThan")
    def older_than(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "olderThan"))

    @older_than.setter
    def older_than(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectContainerExpirationPolicyOutputReference, "older_than").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "olderThan", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ProjectContainerExpirationPolicy]:
        return typing.cast(typing.Optional[ProjectContainerExpirationPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ProjectContainerExpirationPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectContainerExpirationPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.project.ProjectPushRules",
    jsii_struct_bases=[],
    name_mapping={
        "author_email_regex": "authorEmailRegex",
        "branch_name_regex": "branchNameRegex",
        "commit_committer_check": "commitCommitterCheck",
        "commit_message_negative_regex": "commitMessageNegativeRegex",
        "commit_message_regex": "commitMessageRegex",
        "deny_delete_tag": "denyDeleteTag",
        "file_name_regex": "fileNameRegex",
        "max_file_size": "maxFileSize",
        "member_check": "memberCheck",
        "prevent_secrets": "preventSecrets",
        "reject_unsigned_commits": "rejectUnsignedCommits",
    },
)
class ProjectPushRules:
    def __init__(
        self,
        *,
        author_email_regex: typing.Optional[builtins.str] = None,
        branch_name_regex: typing.Optional[builtins.str] = None,
        commit_committer_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        commit_message_negative_regex: typing.Optional[builtins.str] = None,
        commit_message_regex: typing.Optional[builtins.str] = None,
        deny_delete_tag: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        file_name_regex: typing.Optional[builtins.str] = None,
        max_file_size: typing.Optional[jsii.Number] = None,
        member_check: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        prevent_secrets: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reject_unsigned_commits: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param author_email_regex: All commit author emails must match this regex, e.g. ``@my-company.com$``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#author_email_regex Project#author_email_regex}
        :param branch_name_regex: All branch names must match this regex, e.g. ``(feature|hotfix)\\/*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#branch_name_regex Project#branch_name_regex}
        :param commit_committer_check: Users can only push commits to this repository that were committed with one of their own verified emails. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_committer_check Project#commit_committer_check}
        :param commit_message_negative_regex: No commit message is allowed to match this regex, for example ``ssh\\:\\/\\/``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_message_negative_regex Project#commit_message_negative_regex}
        :param commit_message_regex: All commit messages must match this regex, e.g. ``Fixed \\d+\\..*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_message_regex Project#commit_message_regex}
        :param deny_delete_tag: Deny deleting a tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#deny_delete_tag Project#deny_delete_tag}
        :param file_name_regex: All commited filenames must not match this regex, e.g. ``(jar|exe)$``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#file_name_regex Project#file_name_regex}
        :param max_file_size: Maximum file size (MB). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#max_file_size Project#max_file_size}
        :param member_check: Restrict commits by author (email) to existing GitLab users. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#member_check Project#member_check}
        :param prevent_secrets: GitLab will reject any files that are likely to contain secrets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#prevent_secrets Project#prevent_secrets}
        :param reject_unsigned_commits: Reject commit when it’s not signed through GPG. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#reject_unsigned_commits Project#reject_unsigned_commits}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ProjectPushRules.__init__)
            check_type(argname="argument author_email_regex", value=author_email_regex, expected_type=type_hints["author_email_regex"])
            check_type(argname="argument branch_name_regex", value=branch_name_regex, expected_type=type_hints["branch_name_regex"])
            check_type(argname="argument commit_committer_check", value=commit_committer_check, expected_type=type_hints["commit_committer_check"])
            check_type(argname="argument commit_message_negative_regex", value=commit_message_negative_regex, expected_type=type_hints["commit_message_negative_regex"])
            check_type(argname="argument commit_message_regex", value=commit_message_regex, expected_type=type_hints["commit_message_regex"])
            check_type(argname="argument deny_delete_tag", value=deny_delete_tag, expected_type=type_hints["deny_delete_tag"])
            check_type(argname="argument file_name_regex", value=file_name_regex, expected_type=type_hints["file_name_regex"])
            check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
            check_type(argname="argument member_check", value=member_check, expected_type=type_hints["member_check"])
            check_type(argname="argument prevent_secrets", value=prevent_secrets, expected_type=type_hints["prevent_secrets"])
            check_type(argname="argument reject_unsigned_commits", value=reject_unsigned_commits, expected_type=type_hints["reject_unsigned_commits"])
        self._values: typing.Dict[str, typing.Any] = {}
        if author_email_regex is not None:
            self._values["author_email_regex"] = author_email_regex
        if branch_name_regex is not None:
            self._values["branch_name_regex"] = branch_name_regex
        if commit_committer_check is not None:
            self._values["commit_committer_check"] = commit_committer_check
        if commit_message_negative_regex is not None:
            self._values["commit_message_negative_regex"] = commit_message_negative_regex
        if commit_message_regex is not None:
            self._values["commit_message_regex"] = commit_message_regex
        if deny_delete_tag is not None:
            self._values["deny_delete_tag"] = deny_delete_tag
        if file_name_regex is not None:
            self._values["file_name_regex"] = file_name_regex
        if max_file_size is not None:
            self._values["max_file_size"] = max_file_size
        if member_check is not None:
            self._values["member_check"] = member_check
        if prevent_secrets is not None:
            self._values["prevent_secrets"] = prevent_secrets
        if reject_unsigned_commits is not None:
            self._values["reject_unsigned_commits"] = reject_unsigned_commits

    @builtins.property
    def author_email_regex(self) -> typing.Optional[builtins.str]:
        '''All commit author emails must match this regex, e.g. ``@my-company.com$``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#author_email_regex Project#author_email_regex}
        '''
        result = self._values.get("author_email_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def branch_name_regex(self) -> typing.Optional[builtins.str]:
        '''All branch names must match this regex, e.g. ``(feature|hotfix)\\/*``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#branch_name_regex Project#branch_name_regex}
        '''
        result = self._values.get("branch_name_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_committer_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Users can only push commits to this repository that were committed with one of their own verified emails.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_committer_check Project#commit_committer_check}
        '''
        result = self._values.get("commit_committer_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def commit_message_negative_regex(self) -> typing.Optional[builtins.str]:
        '''No commit message is allowed to match this regex, for example ``ssh\\:\\/\\/``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_message_negative_regex Project#commit_message_negative_regex}
        '''
        result = self._values.get("commit_message_negative_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_message_regex(self) -> typing.Optional[builtins.str]:
        '''All commit messages must match this regex, e.g. ``Fixed \\d+\\..*``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#commit_message_regex Project#commit_message_regex}
        '''
        result = self._values.get("commit_message_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deny_delete_tag(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Deny deleting a tag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#deny_delete_tag Project#deny_delete_tag}
        '''
        result = self._values.get("deny_delete_tag")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def file_name_regex(self) -> typing.Optional[builtins.str]:
        '''All commited filenames must not match this regex, e.g. ``(jar|exe)$``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#file_name_regex Project#file_name_regex}
        '''
        result = self._values.get("file_name_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_file_size(self) -> typing.Optional[jsii.Number]:
        '''Maximum file size (MB).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#max_file_size Project#max_file_size}
        '''
        result = self._values.get("max_file_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def member_check(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Restrict commits by author (email) to existing GitLab users.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#member_check Project#member_check}
        '''
        result = self._values.get("member_check")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def prevent_secrets(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''GitLab will reject any files that are likely to contain secrets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#prevent_secrets Project#prevent_secrets}
        '''
        result = self._values.get("prevent_secrets")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def reject_unsigned_commits(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Reject commit when it’s not signed through GPG.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/project#reject_unsigned_commits Project#reject_unsigned_commits}
        '''
        result = self._values.get("reject_unsigned_commits")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectPushRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ProjectPushRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.project.ProjectPushRulesOutputReference",
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
            type_hints = typing.get_type_hints(ProjectPushRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthorEmailRegex")
    def reset_author_email_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorEmailRegex", []))

    @jsii.member(jsii_name="resetBranchNameRegex")
    def reset_branch_name_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranchNameRegex", []))

    @jsii.member(jsii_name="resetCommitCommitterCheck")
    def reset_commit_committer_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitCommitterCheck", []))

    @jsii.member(jsii_name="resetCommitMessageNegativeRegex")
    def reset_commit_message_negative_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitMessageNegativeRegex", []))

    @jsii.member(jsii_name="resetCommitMessageRegex")
    def reset_commit_message_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitMessageRegex", []))

    @jsii.member(jsii_name="resetDenyDeleteTag")
    def reset_deny_delete_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDenyDeleteTag", []))

    @jsii.member(jsii_name="resetFileNameRegex")
    def reset_file_name_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileNameRegex", []))

    @jsii.member(jsii_name="resetMaxFileSize")
    def reset_max_file_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFileSize", []))

    @jsii.member(jsii_name="resetMemberCheck")
    def reset_member_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemberCheck", []))

    @jsii.member(jsii_name="resetPreventSecrets")
    def reset_prevent_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreventSecrets", []))

    @jsii.member(jsii_name="resetRejectUnsignedCommits")
    def reset_reject_unsigned_commits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectUnsignedCommits", []))

    @builtins.property
    @jsii.member(jsii_name="authorEmailRegexInput")
    def author_email_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorEmailRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="branchNameRegexInput")
    def branch_name_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchNameRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="commitCommitterCheckInput")
    def commit_committer_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "commitCommitterCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="commitMessageNegativeRegexInput")
    def commit_message_negative_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitMessageNegativeRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="commitMessageRegexInput")
    def commit_message_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitMessageRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="denyDeleteTagInput")
    def deny_delete_tag_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "denyDeleteTagInput"))

    @builtins.property
    @jsii.member(jsii_name="fileNameRegexInput")
    def file_name_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileNameRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFileSizeInput")
    def max_file_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFileSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="memberCheckInput")
    def member_check_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "memberCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="preventSecretsInput")
    def prevent_secrets_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preventSecretsInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectUnsignedCommitsInput")
    def reject_unsigned_commits_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "rejectUnsignedCommitsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorEmailRegex")
    def author_email_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorEmailRegex"))

    @author_email_regex.setter
    def author_email_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "author_email_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorEmailRegex", value)

    @builtins.property
    @jsii.member(jsii_name="branchNameRegex")
    def branch_name_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchNameRegex"))

    @branch_name_regex.setter
    def branch_name_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "branch_name_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branchNameRegex", value)

    @builtins.property
    @jsii.member(jsii_name="commitCommitterCheck")
    def commit_committer_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "commitCommitterCheck"))

    @commit_committer_check.setter
    def commit_committer_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "commit_committer_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitCommitterCheck", value)

    @builtins.property
    @jsii.member(jsii_name="commitMessageNegativeRegex")
    def commit_message_negative_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitMessageNegativeRegex"))

    @commit_message_negative_regex.setter
    def commit_message_negative_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "commit_message_negative_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitMessageNegativeRegex", value)

    @builtins.property
    @jsii.member(jsii_name="commitMessageRegex")
    def commit_message_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitMessageRegex"))

    @commit_message_regex.setter
    def commit_message_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "commit_message_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitMessageRegex", value)

    @builtins.property
    @jsii.member(jsii_name="denyDeleteTag")
    def deny_delete_tag(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "denyDeleteTag"))

    @deny_delete_tag.setter
    def deny_delete_tag(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "deny_delete_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "denyDeleteTag", value)

    @builtins.property
    @jsii.member(jsii_name="fileNameRegex")
    def file_name_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileNameRegex"))

    @file_name_regex.setter
    def file_name_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "file_name_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileNameRegex", value)

    @builtins.property
    @jsii.member(jsii_name="maxFileSize")
    def max_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFileSize"))

    @max_file_size.setter
    def max_file_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "max_file_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFileSize", value)

    @builtins.property
    @jsii.member(jsii_name="memberCheck")
    def member_check(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "memberCheck"))

    @member_check.setter
    def member_check(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "member_check").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberCheck", value)

    @builtins.property
    @jsii.member(jsii_name="preventSecrets")
    def prevent_secrets(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preventSecrets"))

    @prevent_secrets.setter
    def prevent_secrets(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "prevent_secrets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preventSecrets", value)

    @builtins.property
    @jsii.member(jsii_name="rejectUnsignedCommits")
    def reject_unsigned_commits(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "rejectUnsignedCommits"))

    @reject_unsigned_commits.setter
    def reject_unsigned_commits(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "reject_unsigned_commits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rejectUnsignedCommits", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ProjectPushRules]:
        return typing.cast(typing.Optional[ProjectPushRules], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ProjectPushRules]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ProjectPushRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Project",
    "ProjectConfig",
    "ProjectContainerExpirationPolicy",
    "ProjectContainerExpirationPolicyOutputReference",
    "ProjectPushRules",
    "ProjectPushRulesOutputReference",
]

publication.publish()
