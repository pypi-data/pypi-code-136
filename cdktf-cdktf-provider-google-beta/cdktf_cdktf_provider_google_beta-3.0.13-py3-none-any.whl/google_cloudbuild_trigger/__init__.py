'''
# `google_cloudbuild_trigger`

Refer to the Terraform Registory for docs: [`google_cloudbuild_trigger`](https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger).
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


class GoogleCloudbuildTrigger(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTrigger",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger google_cloudbuild_trigger}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        approval_config: typing.Optional[typing.Union["GoogleCloudbuildTriggerApprovalConfig", typing.Dict[str, typing.Any]]] = None,
        build_attribute: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuild", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filename: typing.Optional[builtins.str] = None,
        filter: typing.Optional[builtins.str] = None,
        git_file_source: typing.Optional[typing.Union["GoogleCloudbuildTriggerGitFileSource", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["GoogleCloudbuildTriggerGithub", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ignored_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_build_logs: typing.Optional[builtins.str] = None,
        included_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        pubsub_config: typing.Optional[typing.Union["GoogleCloudbuildTriggerPubsubConfig", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        source_to_build: typing.Optional[typing.Union["GoogleCloudbuildTriggerSourceToBuild", typing.Dict[str, typing.Any]]] = None,
        substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleCloudbuildTriggerTimeouts", typing.Dict[str, typing.Any]]] = None,
        trigger_template: typing.Optional[typing.Union["GoogleCloudbuildTriggerTriggerTemplate", typing.Dict[str, typing.Any]]] = None,
        webhook_config: typing.Optional[typing.Union["GoogleCloudbuildTriggerWebhookConfig", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger google_cloudbuild_trigger} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param approval_config: approval_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#approval_config GoogleCloudbuildTrigger#approval_config}
        :param build_attribute: build block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#build GoogleCloudbuildTrigger#build}
        :param description: Human-readable description of the trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#description GoogleCloudbuildTrigger#description}
        :param disabled: Whether the trigger is disabled or not. If true, the trigger will never result in a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#disabled GoogleCloudbuildTrigger#disabled}
        :param filename: Path, from the source root, to a file whose contents is used for the template. Either a filename or build template must be provided. Set this only when using trigger_template or github. When using Pub/Sub, Webhook or Manual set the file name using git_file_source instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#filename GoogleCloudbuildTrigger#filename}
        :param filter: A Common Expression Language string. Used only with Pub/Sub and Webhook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#filter GoogleCloudbuildTrigger#filter}
        :param git_file_source: git_file_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#git_file_source GoogleCloudbuildTrigger#git_file_source}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#github GoogleCloudbuildTrigger#github}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#id GoogleCloudbuildTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignored_files: ignoredFiles and includedFiles are file glob matches using https://golang.org/pkg/path/filepath/#Match extended with support for '**'. If ignoredFiles and changed files are both empty, then they are not used to determine whether or not to trigger a build. If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignoredFiles globs, then we do not trigger a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#ignored_files GoogleCloudbuildTrigger#ignored_files}
        :param include_build_logs: Build logs will be sent back to GitHub as part of the checkrun result. Values can be INCLUDE_BUILD_LOGS_UNSPECIFIED or INCLUDE_BUILD_LOGS_WITH_STATUS Possible values: ["INCLUDE_BUILD_LOGS_UNSPECIFIED", "INCLUDE_BUILD_LOGS_WITH_STATUS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#include_build_logs GoogleCloudbuildTrigger#include_build_logs}
        :param included_files: ignoredFiles and includedFiles are file glob matches using https://golang.org/pkg/path/filepath/#Match extended with support for '**'. If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is empty, then as far as this filter is concerned, we should trigger the build. If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is not empty, then we make sure that at least one of those files matches a includedFiles glob. If not, then we do not trigger a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#included_files GoogleCloudbuildTrigger#included_files}
        :param location: The `Cloud Build location <https://cloud.google.com/build/docs/locations>`_ for the trigger. If not specified, "global" is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#location GoogleCloudbuildTrigger#location}
        :param name: Name of the trigger. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project GoogleCloudbuildTrigger#project}.
        :param pubsub_config: pubsub_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#pubsub_config GoogleCloudbuildTrigger#pubsub_config}
        :param service_account: The service account used for all user-controlled operations including triggers.patch, triggers.run, builds.create, and builds.cancel. If no service account is set, then the standard Cloud Build service account ([PROJECT_NUM]@system.gserviceaccount.com) will be used instead. Format: projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#service_account GoogleCloudbuildTrigger#service_account}
        :param source_to_build: source_to_build block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source_to_build GoogleCloudbuildTrigger#source_to_build}
        :param substitutions: Substitutions data for Build resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        :param tags: Tags for annotation of a BuildTrigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tags GoogleCloudbuildTrigger#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeouts GoogleCloudbuildTrigger#timeouts}
        :param trigger_template: trigger_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#trigger_template GoogleCloudbuildTrigger#trigger_template}
        :param webhook_config: webhook_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#webhook_config GoogleCloudbuildTrigger#webhook_config}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTrigger.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleCloudbuildTriggerConfig(
            approval_config=approval_config,
            build_attribute=build_attribute,
            description=description,
            disabled=disabled,
            filename=filename,
            filter=filter,
            git_file_source=git_file_source,
            github=github,
            id=id,
            ignored_files=ignored_files,
            include_build_logs=include_build_logs,
            included_files=included_files,
            location=location,
            name=name,
            project=project,
            pubsub_config=pubsub_config,
            service_account=service_account,
            source_to_build=source_to_build,
            substitutions=substitutions,
            tags=tags,
            timeouts=timeouts,
            trigger_template=trigger_template,
            webhook_config=webhook_config,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putApprovalConfig")
    def put_approval_config(
        self,
        *,
        approval_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param approval_required: Whether or not approval is needed. If this is set on a build, it will become pending when run, and will need to be explicitly approved to start. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#approval_required GoogleCloudbuildTrigger#approval_required}
        '''
        value = GoogleCloudbuildTriggerApprovalConfig(
            approval_required=approval_required
        )

        return typing.cast(None, jsii.invoke(self, "putApprovalConfig", [value]))

    @jsii.member(jsii_name="putBuildAttribute")
    def put_build_attribute(
        self,
        *,
        step: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildStep", typing.Dict[str, typing.Any]]]],
        artifacts: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildArtifacts", typing.Dict[str, typing.Any]]] = None,
        available_secrets: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildAvailableSecrets", typing.Dict[str, typing.Any]]] = None,
        images: typing.Optional[typing.Sequence[builtins.str]] = None,
        logs_bucket: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildOptions", typing.Dict[str, typing.Any]]] = None,
        queue_ttl: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildSecret", typing.Dict[str, typing.Any]]]]] = None,
        source: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildSource", typing.Dict[str, typing.Any]]] = None,
        substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param step: step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#step GoogleCloudbuildTrigger#step}
        :param artifacts: artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#artifacts GoogleCloudbuildTrigger#artifacts}
        :param available_secrets: available_secrets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#available_secrets GoogleCloudbuildTrigger#available_secrets}
        :param images: A list of images to be pushed upon the successful completion of all build steps. The images are pushed using the builder service account's credentials. The digests of the pushed images will be stored in the Build resource's results field. If any of the images fail to be pushed, the build status is marked FAILURE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#images GoogleCloudbuildTrigger#images}
        :param logs_bucket: Google Cloud Storage bucket where logs should be written. Logs file names will be of the format ${logsBucket}/log-${build_id}.txt. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#logs_bucket GoogleCloudbuildTrigger#logs_bucket}
        :param options: options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#options GoogleCloudbuildTrigger#options}
        :param queue_ttl: TTL in queue for this build. If provided and the build is enqueued longer than this value, the build will expire and the build status will be EXPIRED. The TTL starts ticking from createTime. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#queue_ttl GoogleCloudbuildTrigger#queue_ttl}
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret GoogleCloudbuildTrigger#secret}
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source GoogleCloudbuildTrigger#source}
        :param substitutions: Substitutions data for Build resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        :param tags: Tags for annotation of a Build. These are not docker tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tags GoogleCloudbuildTrigger#tags}
        :param timeout: Amount of time that this build should be allowed to run, to second granularity. If this amount of time elapses, work on the build will cease and the build status will be TIMEOUT. This timeout must be equal to or greater than the sum of the timeouts for build steps within the build. The expected format is the number of seconds followed by s. Default time is ten minutes (600s). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeout GoogleCloudbuildTrigger#timeout}
        '''
        value = GoogleCloudbuildTriggerBuild(
            step=step,
            artifacts=artifacts,
            available_secrets=available_secrets,
            images=images,
            logs_bucket=logs_bucket,
            options=options,
            queue_ttl=queue_ttl,
            secret=secret,
            source=source,
            substitutions=substitutions,
            tags=tags,
            timeout=timeout,
        )

        return typing.cast(None, jsii.invoke(self, "putBuildAttribute", [value]))

    @jsii.member(jsii_name="putGitFileSource")
    def put_git_file_source(
        self,
        *,
        path: builtins.str,
        repo_type: builtins.str,
        revision: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: The path of the file, with the repo root as the root of the path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#path GoogleCloudbuildTrigger#path}
        :param repo_type: The type of the repo, since it may not be explicit from the repo field (e.g from a URL). Values can be UNKNOWN, CLOUD_SOURCE_REPOSITORIES, GITHUB, BITBUCKET Possible values: ["UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB", "BITBUCKET"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_type GoogleCloudbuildTrigger#repo_type}
        :param revision: The branch, tag, arbitrary ref, or SHA version of the repo to use when resolving the filename (optional). This field respects the same syntax/resolution as described here: https://git-scm.com/docs/gitrevisions If unspecified, the revision from which the trigger invocation originated is assumed to be the revision from which to read the specified path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#revision GoogleCloudbuildTrigger#revision}
        :param uri: The URI of the repo (optional). If unspecified, the repo from which the trigger invocation originated is assumed to be the repo from which to read the specified path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#uri GoogleCloudbuildTrigger#uri}
        '''
        value = GoogleCloudbuildTriggerGitFileSource(
            path=path, repo_type=repo_type, revision=revision, uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putGitFileSource", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        pull_request: typing.Optional[typing.Union["GoogleCloudbuildTriggerGithubPullRequest", typing.Dict[str, typing.Any]]] = None,
        push: typing.Optional[typing.Union["GoogleCloudbuildTriggerGithubPush", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the repository. For example: The name for https://github.com/googlecloudplatform/cloud-builders is "cloud-builders". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        :param owner: Owner of the repository. For example: The owner for https://github.com/googlecloudplatform/cloud-builders is "googlecloudplatform". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#owner GoogleCloudbuildTrigger#owner}
        :param pull_request: pull_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#pull_request GoogleCloudbuildTrigger#pull_request}
        :param push: push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#push GoogleCloudbuildTrigger#push}
        '''
        value = GoogleCloudbuildTriggerGithub(
            name=name, owner=owner, pull_request=pull_request, push=push
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putPubsubConfig")
    def put_pubsub_config(
        self,
        *,
        topic: builtins.str,
        service_account_email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param topic: The name of the topic from which this subscription is receiving messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#topic GoogleCloudbuildTrigger#topic}
        :param service_account_email: Service account that will make the push request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#service_account_email GoogleCloudbuildTrigger#service_account_email}
        '''
        value = GoogleCloudbuildTriggerPubsubConfig(
            topic=topic, service_account_email=service_account_email
        )

        return typing.cast(None, jsii.invoke(self, "putPubsubConfig", [value]))

    @jsii.member(jsii_name="putSourceToBuild")
    def put_source_to_build(
        self,
        *,
        ref: builtins.str,
        repo_type: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param ref: The branch or tag to use. Must start with "refs/" (required). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#ref GoogleCloudbuildTrigger#ref}
        :param repo_type: The type of the repo, since it may not be explicit from the repo field (e.g from a URL). Values can be UNKNOWN, CLOUD_SOURCE_REPOSITORIES, GITHUB, BITBUCKET Possible values: ["UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB", "BITBUCKET"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_type GoogleCloudbuildTrigger#repo_type}
        :param uri: The URI of the repo (required). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#uri GoogleCloudbuildTrigger#uri}
        '''
        value = GoogleCloudbuildTriggerSourceToBuild(
            ref=ref, repo_type=repo_type, uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putSourceToBuild", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#create GoogleCloudbuildTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#delete GoogleCloudbuildTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#update GoogleCloudbuildTrigger#update}.
        '''
        value = GoogleCloudbuildTriggerTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTriggerTemplate")
    def put_trigger_template(
        self,
        *,
        branch_name: typing.Optional[builtins.str] = None,
        commit_sha: typing.Optional[builtins.str] = None,
        dir: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project_id: typing.Optional[builtins.str] = None,
        repo_name: typing.Optional[builtins.str] = None,
        tag_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch_name: Name of the branch to build. Exactly one a of branch name, tag, or commit SHA must be provided. This field is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch_name GoogleCloudbuildTrigger#branch_name}
        :param commit_sha: Explicit commit SHA to build. Exactly one of a branch name, tag, or commit SHA must be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#commit_sha GoogleCloudbuildTrigger#commit_sha}
        :param dir: Directory, relative to the source root, in which to run the build. This must be a relative path. If a step's dir is specified and is an absolute path, this value is ignored for that step's execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        :param invert_regex: Only trigger a build if the revision regex does NOT match the revision regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        :param project_id: ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project_id GoogleCloudbuildTrigger#project_id}
        :param repo_name: Name of the Cloud Source Repository. If omitted, the name "default" is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_name GoogleCloudbuildTrigger#repo_name}
        :param tag_name: Name of the tag to build. Exactly one of a branch name, tag, or commit SHA must be provided. This field is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag_name GoogleCloudbuildTrigger#tag_name}
        '''
        value = GoogleCloudbuildTriggerTriggerTemplate(
            branch_name=branch_name,
            commit_sha=commit_sha,
            dir=dir,
            invert_regex=invert_regex,
            project_id=project_id,
            repo_name=repo_name,
            tag_name=tag_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTriggerTemplate", [value]))

    @jsii.member(jsii_name="putWebhookConfig")
    def put_webhook_config(self, *, secret: builtins.str) -> None:
        '''
        :param secret: Resource name for the secret required as a URL parameter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret GoogleCloudbuildTrigger#secret}
        '''
        value = GoogleCloudbuildTriggerWebhookConfig(secret=secret)

        return typing.cast(None, jsii.invoke(self, "putWebhookConfig", [value]))

    @jsii.member(jsii_name="resetApprovalConfig")
    def reset_approval_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovalConfig", []))

    @jsii.member(jsii_name="resetBuildAttribute")
    def reset_build_attribute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildAttribute", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetFilename")
    def reset_filename(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilename", []))

    @jsii.member(jsii_name="resetFilter")
    def reset_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilter", []))

    @jsii.member(jsii_name="resetGitFileSource")
    def reset_git_file_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitFileSource", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoredFiles")
    def reset_ignored_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoredFiles", []))

    @jsii.member(jsii_name="resetIncludeBuildLogs")
    def reset_include_build_logs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeBuildLogs", []))

    @jsii.member(jsii_name="resetIncludedFiles")
    def reset_included_files(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludedFiles", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPubsubConfig")
    def reset_pubsub_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPubsubConfig", []))

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @jsii.member(jsii_name="resetSourceToBuild")
    def reset_source_to_build(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceToBuild", []))

    @jsii.member(jsii_name="resetSubstitutions")
    def reset_substitutions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubstitutions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTriggerTemplate")
    def reset_trigger_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerTemplate", []))

    @jsii.member(jsii_name="resetWebhookConfig")
    def reset_webhook_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhookConfig", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="approvalConfig")
    def approval_config(self) -> "GoogleCloudbuildTriggerApprovalConfigOutputReference":
        return typing.cast("GoogleCloudbuildTriggerApprovalConfigOutputReference", jsii.get(self, "approvalConfig"))

    @builtins.property
    @jsii.member(jsii_name="buildAttribute")
    def build_attribute(self) -> "GoogleCloudbuildTriggerBuildOutputReference":
        return typing.cast("GoogleCloudbuildTriggerBuildOutputReference", jsii.get(self, "buildAttribute"))

    @builtins.property
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="gitFileSource")
    def git_file_source(self) -> "GoogleCloudbuildTriggerGitFileSourceOutputReference":
        return typing.cast("GoogleCloudbuildTriggerGitFileSourceOutputReference", jsii.get(self, "gitFileSource"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> "GoogleCloudbuildTriggerGithubOutputReference":
        return typing.cast("GoogleCloudbuildTriggerGithubOutputReference", jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="pubsubConfig")
    def pubsub_config(self) -> "GoogleCloudbuildTriggerPubsubConfigOutputReference":
        return typing.cast("GoogleCloudbuildTriggerPubsubConfigOutputReference", jsii.get(self, "pubsubConfig"))

    @builtins.property
    @jsii.member(jsii_name="sourceToBuild")
    def source_to_build(self) -> "GoogleCloudbuildTriggerSourceToBuildOutputReference":
        return typing.cast("GoogleCloudbuildTriggerSourceToBuildOutputReference", jsii.get(self, "sourceToBuild"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleCloudbuildTriggerTimeoutsOutputReference":
        return typing.cast("GoogleCloudbuildTriggerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="triggerId")
    def trigger_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerId"))

    @builtins.property
    @jsii.member(jsii_name="triggerTemplate")
    def trigger_template(
        self,
    ) -> "GoogleCloudbuildTriggerTriggerTemplateOutputReference":
        return typing.cast("GoogleCloudbuildTriggerTriggerTemplateOutputReference", jsii.get(self, "triggerTemplate"))

    @builtins.property
    @jsii.member(jsii_name="webhookConfig")
    def webhook_config(self) -> "GoogleCloudbuildTriggerWebhookConfigOutputReference":
        return typing.cast("GoogleCloudbuildTriggerWebhookConfigOutputReference", jsii.get(self, "webhookConfig"))

    @builtins.property
    @jsii.member(jsii_name="approvalConfigInput")
    def approval_config_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerApprovalConfig"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerApprovalConfig"], jsii.get(self, "approvalConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="buildAttributeInput")
    def build_attribute_input(self) -> typing.Optional["GoogleCloudbuildTriggerBuild"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuild"], jsii.get(self, "buildAttributeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="filenameInput")
    def filename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filenameInput"))

    @builtins.property
    @jsii.member(jsii_name="filterInput")
    def filter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filterInput"))

    @builtins.property
    @jsii.member(jsii_name="gitFileSourceInput")
    def git_file_source_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerGitFileSource"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGitFileSource"], jsii.get(self, "gitFileSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional["GoogleCloudbuildTriggerGithub"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGithub"], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoredFilesInput")
    def ignored_files_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoredFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="includeBuildLogsInput")
    def include_build_logs_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "includeBuildLogsInput"))

    @builtins.property
    @jsii.member(jsii_name="includedFilesInput")
    def included_files_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "includedFilesInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pubsubConfigInput")
    def pubsub_config_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerPubsubConfig"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerPubsubConfig"], jsii.get(self, "pubsubConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceToBuildInput")
    def source_to_build_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerSourceToBuild"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerSourceToBuild"], jsii.get(self, "sourceToBuildInput"))

    @builtins.property
    @jsii.member(jsii_name="substitutionsInput")
    def substitutions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "substitutionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleCloudbuildTriggerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleCloudbuildTriggerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerTemplateInput")
    def trigger_template_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerTriggerTemplate"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerTriggerTemplate"], jsii.get(self, "triggerTemplateInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookConfigInput")
    def webhook_config_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerWebhookConfig"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerWebhookConfig"], jsii.get(self, "webhookConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="filename")
    def filename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filename"))

    @filename.setter
    def filename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "filename").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filename", value)

    @builtins.property
    @jsii.member(jsii_name="filter")
    def filter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filter"))

    @filter.setter
    def filter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoredFiles")
    def ignored_files(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ignoredFiles"))

    @ignored_files.setter
    def ignored_files(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "ignored_files").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoredFiles", value)

    @builtins.property
    @jsii.member(jsii_name="includeBuildLogs")
    def include_build_logs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "includeBuildLogs"))

    @include_build_logs.setter
    def include_build_logs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "include_build_logs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeBuildLogs", value)

    @builtins.property
    @jsii.member(jsii_name="includedFiles")
    def included_files(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "includedFiles"))

    @included_files.setter
    def included_files(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "included_files").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includedFiles", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="substitutions")
    def substitutions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "substitutions"))

    @substitutions.setter
    def substitutions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "substitutions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "substitutions", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTrigger, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerApprovalConfig",
    jsii_struct_bases=[],
    name_mapping={"approval_required": "approvalRequired"},
)
class GoogleCloudbuildTriggerApprovalConfig:
    def __init__(
        self,
        *,
        approval_required: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param approval_required: Whether or not approval is needed. If this is set on a build, it will become pending when run, and will need to be explicitly approved to start. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#approval_required GoogleCloudbuildTrigger#approval_required}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerApprovalConfig.__init__)
            check_type(argname="argument approval_required", value=approval_required, expected_type=type_hints["approval_required"])
        self._values: typing.Dict[str, typing.Any] = {}
        if approval_required is not None:
            self._values["approval_required"] = approval_required

    @builtins.property
    def approval_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not approval is needed.

        If this is set on a build, it will become pending when run,
        and will need to be explicitly approved to start.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#approval_required GoogleCloudbuildTrigger#approval_required}
        '''
        result = self._values.get("approval_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerApprovalConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerApprovalConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerApprovalConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerApprovalConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApprovalRequired")
    def reset_approval_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApprovalRequired", []))

    @builtins.property
    @jsii.member(jsii_name="approvalRequiredInput")
    def approval_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "approvalRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="approvalRequired")
    def approval_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "approvalRequired"))

    @approval_required.setter
    def approval_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerApprovalConfigOutputReference, "approval_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalRequired", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerApprovalConfig]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerApprovalConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerApprovalConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerApprovalConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuild",
    jsii_struct_bases=[],
    name_mapping={
        "step": "step",
        "artifacts": "artifacts",
        "available_secrets": "availableSecrets",
        "images": "images",
        "logs_bucket": "logsBucket",
        "options": "options",
        "queue_ttl": "queueTtl",
        "secret": "secret",
        "source": "source",
        "substitutions": "substitutions",
        "tags": "tags",
        "timeout": "timeout",
    },
)
class GoogleCloudbuildTriggerBuild:
    def __init__(
        self,
        *,
        step: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildStep", typing.Dict[str, typing.Any]]]],
        artifacts: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildArtifacts", typing.Dict[str, typing.Any]]] = None,
        available_secrets: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildAvailableSecrets", typing.Dict[str, typing.Any]]] = None,
        images: typing.Optional[typing.Sequence[builtins.str]] = None,
        logs_bucket: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildOptions", typing.Dict[str, typing.Any]]] = None,
        queue_ttl: typing.Optional[builtins.str] = None,
        secret: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildSecret", typing.Dict[str, typing.Any]]]]] = None,
        source: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildSource", typing.Dict[str, typing.Any]]] = None,
        substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param step: step block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#step GoogleCloudbuildTrigger#step}
        :param artifacts: artifacts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#artifacts GoogleCloudbuildTrigger#artifacts}
        :param available_secrets: available_secrets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#available_secrets GoogleCloudbuildTrigger#available_secrets}
        :param images: A list of images to be pushed upon the successful completion of all build steps. The images are pushed using the builder service account's credentials. The digests of the pushed images will be stored in the Build resource's results field. If any of the images fail to be pushed, the build status is marked FAILURE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#images GoogleCloudbuildTrigger#images}
        :param logs_bucket: Google Cloud Storage bucket where logs should be written. Logs file names will be of the format ${logsBucket}/log-${build_id}.txt. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#logs_bucket GoogleCloudbuildTrigger#logs_bucket}
        :param options: options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#options GoogleCloudbuildTrigger#options}
        :param queue_ttl: TTL in queue for this build. If provided and the build is enqueued longer than this value, the build will expire and the build status will be EXPIRED. The TTL starts ticking from createTime. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#queue_ttl GoogleCloudbuildTrigger#queue_ttl}
        :param secret: secret block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret GoogleCloudbuildTrigger#secret}
        :param source: source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source GoogleCloudbuildTrigger#source}
        :param substitutions: Substitutions data for Build resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        :param tags: Tags for annotation of a Build. These are not docker tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tags GoogleCloudbuildTrigger#tags}
        :param timeout: Amount of time that this build should be allowed to run, to second granularity. If this amount of time elapses, work on the build will cease and the build status will be TIMEOUT. This timeout must be equal to or greater than the sum of the timeouts for build steps within the build. The expected format is the number of seconds followed by s. Default time is ten minutes (600s). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeout GoogleCloudbuildTrigger#timeout}
        '''
        if isinstance(artifacts, dict):
            artifacts = GoogleCloudbuildTriggerBuildArtifacts(**artifacts)
        if isinstance(available_secrets, dict):
            available_secrets = GoogleCloudbuildTriggerBuildAvailableSecrets(**available_secrets)
        if isinstance(options, dict):
            options = GoogleCloudbuildTriggerBuildOptions(**options)
        if isinstance(source, dict):
            source = GoogleCloudbuildTriggerBuildSource(**source)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuild.__init__)
            check_type(argname="argument step", value=step, expected_type=type_hints["step"])
            check_type(argname="argument artifacts", value=artifacts, expected_type=type_hints["artifacts"])
            check_type(argname="argument available_secrets", value=available_secrets, expected_type=type_hints["available_secrets"])
            check_type(argname="argument images", value=images, expected_type=type_hints["images"])
            check_type(argname="argument logs_bucket", value=logs_bucket, expected_type=type_hints["logs_bucket"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument queue_ttl", value=queue_ttl, expected_type=type_hints["queue_ttl"])
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument substitutions", value=substitutions, expected_type=type_hints["substitutions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "step": step,
        }
        if artifacts is not None:
            self._values["artifacts"] = artifacts
        if available_secrets is not None:
            self._values["available_secrets"] = available_secrets
        if images is not None:
            self._values["images"] = images
        if logs_bucket is not None:
            self._values["logs_bucket"] = logs_bucket
        if options is not None:
            self._values["options"] = options
        if queue_ttl is not None:
            self._values["queue_ttl"] = queue_ttl
        if secret is not None:
            self._values["secret"] = secret
        if source is not None:
            self._values["source"] = source
        if substitutions is not None:
            self._values["substitutions"] = substitutions
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def step(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStep"]]:
        '''step block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#step GoogleCloudbuildTrigger#step}
        '''
        result = self._values.get("step")
        assert result is not None, "Required property 'step' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStep"]], result)

    @builtins.property
    def artifacts(self) -> typing.Optional["GoogleCloudbuildTriggerBuildArtifacts"]:
        '''artifacts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#artifacts GoogleCloudbuildTrigger#artifacts}
        '''
        result = self._values.get("artifacts")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildArtifacts"], result)

    @builtins.property
    def available_secrets(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerBuildAvailableSecrets"]:
        '''available_secrets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#available_secrets GoogleCloudbuildTrigger#available_secrets}
        '''
        result = self._values.get("available_secrets")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildAvailableSecrets"], result)

    @builtins.property
    def images(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of images to be pushed upon the successful completion of all build steps.

        The images are pushed using the builder service account's credentials.
        The digests of the pushed images will be stored in the Build resource's results field.
        If any of the images fail to be pushed, the build status is marked FAILURE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#images GoogleCloudbuildTrigger#images}
        '''
        result = self._values.get("images")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logs_bucket(self) -> typing.Optional[builtins.str]:
        '''Google Cloud Storage bucket where logs should be written.  Logs file names will be of the format ${logsBucket}/log-${build_id}.txt.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#logs_bucket GoogleCloudbuildTrigger#logs_bucket}
        '''
        result = self._values.get("logs_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional["GoogleCloudbuildTriggerBuildOptions"]:
        '''options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#options GoogleCloudbuildTrigger#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildOptions"], result)

    @builtins.property
    def queue_ttl(self) -> typing.Optional[builtins.str]:
        '''TTL in queue for this build.

        If provided and the build is enqueued longer than this value,
        the build will expire and the build status will be EXPIRED.
        The TTL starts ticking from createTime.
        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#queue_ttl GoogleCloudbuildTrigger#queue_ttl}
        '''
        result = self._values.get("queue_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildSecret"]]]:
        '''secret block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret GoogleCloudbuildTrigger#secret}
        '''
        result = self._values.get("secret")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildSecret"]]], result)

    @builtins.property
    def source(self) -> typing.Optional["GoogleCloudbuildTriggerBuildSource"]:
        '''source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source GoogleCloudbuildTrigger#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildSource"], result)

    @builtins.property
    def substitutions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Substitutions data for Build resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        '''
        result = self._values.get("substitutions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags for annotation of a Build. These are not docker tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tags GoogleCloudbuildTrigger#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Amount of time that this build should be allowed to run, to second granularity.

        If this amount of time elapses, work on the build will cease and the build status will be TIMEOUT.
        This timeout must be equal to or greater than the sum of the timeouts for build steps within the build.
        The expected format is the number of seconds followed by s.
        Default time is ten minutes (600s).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeout GoogleCloudbuildTrigger#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuild(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildArtifacts",
    jsii_struct_bases=[],
    name_mapping={"images": "images", "objects": "objects"},
)
class GoogleCloudbuildTriggerBuildArtifacts:
    def __init__(
        self,
        *,
        images: typing.Optional[typing.Sequence[builtins.str]] = None,
        objects: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildArtifactsObjects", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param images: A list of images to be pushed upon the successful completion of all build steps. The images will be pushed using the builder service account's credentials. The digests of the pushed images will be stored in the Build resource's results field. If any of the images fail to be pushed, the build is marked FAILURE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#images GoogleCloudbuildTrigger#images}
        :param objects: objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#objects GoogleCloudbuildTrigger#objects}
        '''
        if isinstance(objects, dict):
            objects = GoogleCloudbuildTriggerBuildArtifactsObjects(**objects)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildArtifacts.__init__)
            check_type(argname="argument images", value=images, expected_type=type_hints["images"])
            check_type(argname="argument objects", value=objects, expected_type=type_hints["objects"])
        self._values: typing.Dict[str, typing.Any] = {}
        if images is not None:
            self._values["images"] = images
        if objects is not None:
            self._values["objects"] = objects

    @builtins.property
    def images(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of images to be pushed upon the successful completion of all build steps.

        The images will be pushed using the builder service account's credentials.

        The digests of the pushed images will be stored in the Build resource's results field.

        If any of the images fail to be pushed, the build is marked FAILURE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#images GoogleCloudbuildTrigger#images}
        '''
        result = self._values.get("images")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def objects(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerBuildArtifactsObjects"]:
        '''objects block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#objects GoogleCloudbuildTrigger#objects}
        '''
        result = self._values.get("objects")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildArtifactsObjects"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildArtifacts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildArtifactsObjects",
    jsii_struct_bases=[],
    name_mapping={"location": "location", "paths": "paths"},
)
class GoogleCloudbuildTriggerBuildArtifactsObjects:
    def __init__(
        self,
        *,
        location: typing.Optional[builtins.str] = None,
        paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param location: Cloud Storage bucket and optional object path, in the form "gs://bucket/path/to/somewhere/". Files in the workspace matching any path pattern will be uploaded to Cloud Storage with this location as a prefix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#location GoogleCloudbuildTrigger#location}
        :param paths: Path globs used to match files in the build's workspace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#paths GoogleCloudbuildTrigger#paths}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildArtifactsObjects.__init__)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument paths", value=paths, expected_type=type_hints["paths"])
        self._values: typing.Dict[str, typing.Any] = {}
        if location is not None:
            self._values["location"] = location
        if paths is not None:
            self._values["paths"] = paths

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''Cloud Storage bucket and optional object path, in the form "gs://bucket/path/to/somewhere/".

        Files in the workspace matching any path pattern will be uploaded to Cloud Storage with
        this location as a prefix.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#location GoogleCloudbuildTrigger#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Path globs used to match files in the build's workspace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#paths GoogleCloudbuildTrigger#paths}
        '''
        result = self._values.get("paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildArtifactsObjects(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetPaths")
    def reset_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaths", []))

    @builtins.property
    @jsii.member(jsii_name="timing")
    def timing(self) -> "GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList":
        return typing.cast("GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList", jsii.get(self, "timing"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="pathsInput")
    def paths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pathsInput"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="paths")
    def paths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "paths"))

    @paths.setter
    def paths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference, "paths").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjects]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjects], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjects],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildArtifactsObjectsTiming",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleCloudbuildTriggerBuildArtifactsObjectsTiming:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildArtifactsObjectsTiming(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudbuildTriggerBuildArtifactsObjectsTimingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudbuildTriggerBuildArtifactsObjectsTimingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleCloudbuildTriggerBuildArtifactsObjectsTimingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildArtifactsObjectsTimingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildArtifactsObjectsTimingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjectsTiming]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjectsTiming], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjectsTiming],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsObjectsTimingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudbuildTriggerBuildArtifactsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildArtifactsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildArtifactsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putObjects")
    def put_objects(
        self,
        *,
        location: typing.Optional[builtins.str] = None,
        paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param location: Cloud Storage bucket and optional object path, in the form "gs://bucket/path/to/somewhere/". Files in the workspace matching any path pattern will be uploaded to Cloud Storage with this location as a prefix. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#location GoogleCloudbuildTrigger#location}
        :param paths: Path globs used to match files in the build's workspace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#paths GoogleCloudbuildTrigger#paths}
        '''
        value = GoogleCloudbuildTriggerBuildArtifactsObjects(
            location=location, paths=paths
        )

        return typing.cast(None, jsii.invoke(self, "putObjects", [value]))

    @jsii.member(jsii_name="resetImages")
    def reset_images(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImages", []))

    @jsii.member(jsii_name="resetObjects")
    def reset_objects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObjects", []))

    @builtins.property
    @jsii.member(jsii_name="objects")
    def objects(self) -> GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference:
        return typing.cast(GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference, jsii.get(self, "objects"))

    @builtins.property
    @jsii.member(jsii_name="imagesInput")
    def images_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "imagesInput"))

    @builtins.property
    @jsii.member(jsii_name="objectsInput")
    def objects_input(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjects]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildArtifactsObjects], jsii.get(self, "objectsInput"))

    @builtins.property
    @jsii.member(jsii_name="images")
    def images(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "images"))

    @images.setter
    def images(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsOutputReference, "images").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "images", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerBuildArtifacts]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildArtifacts], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildArtifacts],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildArtifactsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildAvailableSecrets",
    jsii_struct_bases=[],
    name_mapping={"secret_manager": "secretManager"},
)
class GoogleCloudbuildTriggerBuildAvailableSecrets:
    def __init__(
        self,
        *,
        secret_manager: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param secret_manager: secret_manager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_manager GoogleCloudbuildTrigger#secret_manager}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildAvailableSecrets.__init__)
            check_type(argname="argument secret_manager", value=secret_manager, expected_type=type_hints["secret_manager"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_manager": secret_manager,
        }

    @builtins.property
    def secret_manager(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager"]]:
        '''secret_manager block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_manager GoogleCloudbuildTrigger#secret_manager}
        '''
        result = self._values.get("secret_manager")
        assert result is not None, "Required property 'secret_manager' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildAvailableSecrets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretManager")
    def put_secret_manager(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference.put_secret_manager)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecretManager", [value]))

    @builtins.property
    @jsii.member(jsii_name="secretManager")
    def secret_manager(
        self,
    ) -> "GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList":
        return typing.cast("GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList", jsii.get(self, "secretManager"))

    @builtins.property
    @jsii.member(jsii_name="secretManagerInput")
    def secret_manager_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager"]]], jsii.get(self, "secretManagerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerBuildAvailableSecrets]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildAvailableSecrets], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildAvailableSecrets],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager",
    jsii_struct_bases=[],
    name_mapping={"env": "env", "version_name": "versionName"},
)
class GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager:
    def __init__(self, *, env: builtins.str, version_name: builtins.str) -> None:
        '''
        :param env: Environment variable name to associate with the secret. Secret environment variables must be unique across all of a build's secrets, and must be used by at least one build step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#env GoogleCloudbuildTrigger#env}
        :param version_name: Resource name of the SecretVersion. In format: projects/*/secrets/*/versions/*. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#version_name GoogleCloudbuildTrigger#version_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager.__init__)
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "env": env,
            "version_name": version_name,
        }

    @builtins.property
    def env(self) -> builtins.str:
        '''Environment variable name to associate with the secret.

        Secret environment
        variables must be unique across all of a build's secrets, and must be used
        by at least one build step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#env GoogleCloudbuildTrigger#env}
        '''
        result = self._values.get("env")
        assert result is not None, "Required property 'env' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_name(self) -> builtins.str:
        '''Resource name of the SecretVersion. In format: projects/*/secrets/*/versions/*.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#version_name GoogleCloudbuildTrigger#version_name}
        '''
        result = self._values.get("version_name")
        assert result is not None, "Required property 'version_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="versionNameInput")
    def version_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionNameInput"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "env"))

    @env.setter
    def env(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference, "env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "env", value)

    @builtins.property
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference, "version_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildOptions",
    jsii_struct_bases=[],
    name_mapping={
        "disk_size_gb": "diskSizeGb",
        "dynamic_substitutions": "dynamicSubstitutions",
        "env": "env",
        "logging": "logging",
        "log_streaming_option": "logStreamingOption",
        "machine_type": "machineType",
        "requested_verify_option": "requestedVerifyOption",
        "secret_env": "secretEnv",
        "source_provenance_hash": "sourceProvenanceHash",
        "substitution_option": "substitutionOption",
        "volumes": "volumes",
        "worker_pool": "workerPool",
    },
)
class GoogleCloudbuildTriggerBuildOptions:
    def __init__(
        self,
        *,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        dynamic_substitutions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        env: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging: typing.Optional[builtins.str] = None,
        log_streaming_option: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        requested_verify_option: typing.Optional[builtins.str] = None,
        secret_env: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_provenance_hash: typing.Optional[typing.Sequence[builtins.str]] = None,
        substitution_option: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildOptionsVolumes", typing.Dict[str, typing.Any]]]]] = None,
        worker_pool: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_size_gb: Requested disk size for the VM that runs the build. Note that this is NOT "disk free"; some of the space will be used by the operating system and build utilities. Also note that this is the minimum disk size that will be allocated for the build -- the build may run with a larger disk than requested. At present, the maximum disk size is 1000GB; builds that request more than the maximum are rejected with an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#disk_size_gb GoogleCloudbuildTrigger#disk_size_gb}
        :param dynamic_substitutions: Option to specify whether or not to apply bash style string operations to the substitutions. NOTE this is always enabled for triggered builds and cannot be overridden in the build configuration file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dynamic_substitutions GoogleCloudbuildTrigger#dynamic_substitutions}
        :param env: A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value. The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#env GoogleCloudbuildTrigger#env}
        :param logging: Option to specify the logging mode, which determines if and where build logs are stored. Possible values: ["LOGGING_UNSPECIFIED", "LEGACY", "GCS_ONLY", "STACKDRIVER_ONLY", "CLOUD_LOGGING_ONLY", "NONE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#logging GoogleCloudbuildTrigger#logging}
        :param log_streaming_option: Option to define build log streaming behavior to Google Cloud Storage. Possible values: ["STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#log_streaming_option GoogleCloudbuildTrigger#log_streaming_option}
        :param machine_type: Compute Engine machine type on which to run the build. Possible values: ["UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32", "E2_HIGHCPU_8", "E2_HIGHCPU_32"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#machine_type GoogleCloudbuildTrigger#machine_type}
        :param requested_verify_option: Requested verifiability options. Possible values: ["NOT_VERIFIED", "VERIFIED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#requested_verify_option GoogleCloudbuildTrigger#requested_verify_option}
        :param secret_env: A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's Secret. These variables will be available to all build steps in this build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_env GoogleCloudbuildTrigger#secret_env}
        :param source_provenance_hash: Requested hash for SourceProvenance. Possible values: ["NONE", "SHA256", "MD5"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source_provenance_hash GoogleCloudbuildTrigger#source_provenance_hash}
        :param substitution_option: Option to specify behavior when there is an error in the substitution checks. NOTE this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden in the build configuration file. Possible values: ["MUST_MATCH", "ALLOW_LOOSE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitution_option GoogleCloudbuildTrigger#substitution_option}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#volumes GoogleCloudbuildTrigger#volumes}
        :param worker_pool: Option to specify a WorkerPool for the build. Format projects/{project}/workerPools/{workerPool}. This field is experimental. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#worker_pool GoogleCloudbuildTrigger#worker_pool}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOptions.__init__)
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument dynamic_substitutions", value=dynamic_substitutions, expected_type=type_hints["dynamic_substitutions"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument log_streaming_option", value=log_streaming_option, expected_type=type_hints["log_streaming_option"])
            check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            check_type(argname="argument requested_verify_option", value=requested_verify_option, expected_type=type_hints["requested_verify_option"])
            check_type(argname="argument secret_env", value=secret_env, expected_type=type_hints["secret_env"])
            check_type(argname="argument source_provenance_hash", value=source_provenance_hash, expected_type=type_hints["source_provenance_hash"])
            check_type(argname="argument substitution_option", value=substitution_option, expected_type=type_hints["substitution_option"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument worker_pool", value=worker_pool, expected_type=type_hints["worker_pool"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disk_size_gb is not None:
            self._values["disk_size_gb"] = disk_size_gb
        if dynamic_substitutions is not None:
            self._values["dynamic_substitutions"] = dynamic_substitutions
        if env is not None:
            self._values["env"] = env
        if logging is not None:
            self._values["logging"] = logging
        if log_streaming_option is not None:
            self._values["log_streaming_option"] = log_streaming_option
        if machine_type is not None:
            self._values["machine_type"] = machine_type
        if requested_verify_option is not None:
            self._values["requested_verify_option"] = requested_verify_option
        if secret_env is not None:
            self._values["secret_env"] = secret_env
        if source_provenance_hash is not None:
            self._values["source_provenance_hash"] = source_provenance_hash
        if substitution_option is not None:
            self._values["substitution_option"] = substitution_option
        if volumes is not None:
            self._values["volumes"] = volumes
        if worker_pool is not None:
            self._values["worker_pool"] = worker_pool

    @builtins.property
    def disk_size_gb(self) -> typing.Optional[jsii.Number]:
        '''Requested disk size for the VM that runs the build.

        Note that this is NOT "disk free";
        some of the space will be used by the operating system and build utilities.
        Also note that this is the minimum disk size that will be allocated for the build --
        the build may run with a larger disk than requested. At present, the maximum disk size
        is 1000GB; builds that request more than the maximum are rejected with an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#disk_size_gb GoogleCloudbuildTrigger#disk_size_gb}
        '''
        result = self._values.get("disk_size_gb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dynamic_substitutions(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Option to specify whether or not to apply bash style string operations to the substitutions.

        NOTE this is always enabled for triggered builds and cannot be overridden in the build configuration file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dynamic_substitutions GoogleCloudbuildTrigger#dynamic_substitutions}
        '''
        result = self._values.get("dynamic_substitutions")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of global environment variable definitions that will exist for all build steps in this build.

        If a variable is defined in both globally and in a build step,
        the variable will use the build step value.

        The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#env GoogleCloudbuildTrigger#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging(self) -> typing.Optional[builtins.str]:
        '''Option to specify the logging mode, which determines if and where build logs are stored.

        Possible values: ["LOGGING_UNSPECIFIED", "LEGACY", "GCS_ONLY", "STACKDRIVER_ONLY", "CLOUD_LOGGING_ONLY", "NONE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#logging GoogleCloudbuildTrigger#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_streaming_option(self) -> typing.Optional[builtins.str]:
        '''Option to define build log streaming behavior to Google Cloud Storage. Possible values: ["STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#log_streaming_option GoogleCloudbuildTrigger#log_streaming_option}
        '''
        result = self._values.get("log_streaming_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def machine_type(self) -> typing.Optional[builtins.str]:
        '''Compute Engine machine type on which to run the build. Possible values: ["UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32", "E2_HIGHCPU_8", "E2_HIGHCPU_32"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#machine_type GoogleCloudbuildTrigger#machine_type}
        '''
        result = self._values.get("machine_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requested_verify_option(self) -> typing.Optional[builtins.str]:
        '''Requested verifiability options. Possible values: ["NOT_VERIFIED", "VERIFIED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#requested_verify_option GoogleCloudbuildTrigger#requested_verify_option}
        '''
        result = self._values.get("requested_verify_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key.

        These values must be specified in the build's Secret. These variables
        will be available to all build steps in this build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_env GoogleCloudbuildTrigger#secret_env}
        '''
        result = self._values.get("secret_env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_provenance_hash(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Requested hash for SourceProvenance. Possible values: ["NONE", "SHA256", "MD5"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source_provenance_hash GoogleCloudbuildTrigger#source_provenance_hash}
        '''
        result = self._values.get("source_provenance_hash")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def substitution_option(self) -> typing.Optional[builtins.str]:
        '''Option to specify behavior when there is an error in the substitution checks.

        NOTE this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden
        in the build configuration file. Possible values: ["MUST_MATCH", "ALLOW_LOOSE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitution_option GoogleCloudbuildTrigger#substitution_option}
        '''
        result = self._values.get("substitution_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildOptionsVolumes"]]]:
        '''volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#volumes GoogleCloudbuildTrigger#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildOptionsVolumes"]]], result)

    @builtins.property
    def worker_pool(self) -> typing.Optional[builtins.str]:
        '''Option to specify a WorkerPool for the build. Format projects/{project}/workerPools/{workerPool}.

        This field is experimental.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#worker_pool GoogleCloudbuildTrigger#worker_pool}
        '''
        result = self._values.get("worker_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putVolumes")
    def put_volumes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildOptionsVolumes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOptionsOutputReference.put_volumes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolumes", [value]))

    @jsii.member(jsii_name="resetDiskSizeGb")
    def reset_disk_size_gb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskSizeGb", []))

    @jsii.member(jsii_name="resetDynamicSubstitutions")
    def reset_dynamic_substitutions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicSubstitutions", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetLogStreamingOption")
    def reset_log_streaming_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogStreamingOption", []))

    @jsii.member(jsii_name="resetMachineType")
    def reset_machine_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMachineType", []))

    @jsii.member(jsii_name="resetRequestedVerifyOption")
    def reset_requested_verify_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestedVerifyOption", []))

    @jsii.member(jsii_name="resetSecretEnv")
    def reset_secret_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretEnv", []))

    @jsii.member(jsii_name="resetSourceProvenanceHash")
    def reset_source_provenance_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceProvenanceHash", []))

    @jsii.member(jsii_name="resetSubstitutionOption")
    def reset_substitution_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubstitutionOption", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @jsii.member(jsii_name="resetWorkerPool")
    def reset_worker_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerPool", []))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> "GoogleCloudbuildTriggerBuildOptionsVolumesList":
        return typing.cast("GoogleCloudbuildTriggerBuildOptionsVolumesList", jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicSubstitutionsInput")
    def dynamic_substitutions_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "dynamicSubstitutionsInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="logStreamingOptionInput")
    def log_streaming_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logStreamingOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="machineTypeInput")
    def machine_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "machineTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="requestedVerifyOptionInput")
    def requested_verify_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "requestedVerifyOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretEnvInput")
    def secret_env_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secretEnvInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceProvenanceHashInput")
    def source_provenance_hash_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceProvenanceHashInput"))

    @builtins.property
    @jsii.member(jsii_name="substitutionOptionInput")
    def substitution_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "substitutionOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildOptionsVolumes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildOptionsVolumes"]]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="workerPoolInput")
    def worker_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workerPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="dynamicSubstitutions")
    def dynamic_substitutions(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "dynamicSubstitutions"))

    @dynamic_substitutions.setter
    def dynamic_substitutions(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "dynamic_substitutions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicSubstitutions", value)

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "env"))

    @env.setter
    def env(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "env", value)

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logging"))

    @logging.setter
    def logging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logging", value)

    @builtins.property
    @jsii.member(jsii_name="logStreamingOption")
    def log_streaming_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logStreamingOption"))

    @log_streaming_option.setter
    def log_streaming_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "log_streaming_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logStreamingOption", value)

    @builtins.property
    @jsii.member(jsii_name="machineType")
    def machine_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "machineType"))

    @machine_type.setter
    def machine_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "machine_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "machineType", value)

    @builtins.property
    @jsii.member(jsii_name="requestedVerifyOption")
    def requested_verify_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "requestedVerifyOption"))

    @requested_verify_option.setter
    def requested_verify_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "requested_verify_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestedVerifyOption", value)

    @builtins.property
    @jsii.member(jsii_name="secretEnv")
    def secret_env(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secretEnv"))

    @secret_env.setter
    def secret_env(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "secret_env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretEnv", value)

    @builtins.property
    @jsii.member(jsii_name="sourceProvenanceHash")
    def source_provenance_hash(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceProvenanceHash"))

    @source_provenance_hash.setter
    def source_provenance_hash(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "source_provenance_hash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceProvenanceHash", value)

    @builtins.property
    @jsii.member(jsii_name="substitutionOption")
    def substitution_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "substitutionOption"))

    @substitution_option.setter
    def substitution_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "substitution_option").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "substitutionOption", value)

    @builtins.property
    @jsii.member(jsii_name="workerPool")
    def worker_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workerPool"))

    @worker_pool.setter
    def worker_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "worker_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workerPool", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerBuildOptions]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildOptionsVolumes",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path"},
)
class GoogleCloudbuildTriggerBuildOptionsVolumes:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the volume to mount. Volume names must be unique per build step and must be valid names for Docker volumes. Each named volume must be used by at least two build steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        :param path: Path at which to mount the volume. Paths must be absolute and cannot conflict with other volume paths on the same build step or with certain reserved volume paths. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#path GoogleCloudbuildTrigger#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOptionsVolumes.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the volume to mount.

        Volume names must be unique per build step and must be valid names for Docker volumes.
        Each named volume must be used by at least two build steps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path at which to mount the volume.

        Paths must be absolute and cannot conflict with other volume paths on the same
        build step or with certain reserved volume paths.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#path GoogleCloudbuildTrigger#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildOptionsVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildOptionsVolumesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildOptionsVolumesList",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOptionsVolumesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOptionsVolumesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsVolumesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsVolumesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsVolumesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildOptionsVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildOptionsVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildOptionsVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsVolumesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildOptionsVolumes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildOptionsVolumes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildOptionsVolumes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudbuildTriggerBuildOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putArtifacts")
    def put_artifacts(
        self,
        *,
        images: typing.Optional[typing.Sequence[builtins.str]] = None,
        objects: typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildArtifactsObjects, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param images: A list of images to be pushed upon the successful completion of all build steps. The images will be pushed using the builder service account's credentials. The digests of the pushed images will be stored in the Build resource's results field. If any of the images fail to be pushed, the build is marked FAILURE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#images GoogleCloudbuildTrigger#images}
        :param objects: objects block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#objects GoogleCloudbuildTrigger#objects}
        '''
        value = GoogleCloudbuildTriggerBuildArtifacts(images=images, objects=objects)

        return typing.cast(None, jsii.invoke(self, "putArtifacts", [value]))

    @jsii.member(jsii_name="putAvailableSecrets")
    def put_available_secrets(
        self,
        *,
        secret_manager: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param secret_manager: secret_manager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_manager GoogleCloudbuildTrigger#secret_manager}
        '''
        value = GoogleCloudbuildTriggerBuildAvailableSecrets(
            secret_manager=secret_manager
        )

        return typing.cast(None, jsii.invoke(self, "putAvailableSecrets", [value]))

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        *,
        disk_size_gb: typing.Optional[jsii.Number] = None,
        dynamic_substitutions: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        env: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging: typing.Optional[builtins.str] = None,
        log_streaming_option: typing.Optional[builtins.str] = None,
        machine_type: typing.Optional[builtins.str] = None,
        requested_verify_option: typing.Optional[builtins.str] = None,
        secret_env: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_provenance_hash: typing.Optional[typing.Sequence[builtins.str]] = None,
        substitution_option: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleCloudbuildTriggerBuildOptionsVolumes, typing.Dict[str, typing.Any]]]]] = None,
        worker_pool: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_size_gb: Requested disk size for the VM that runs the build. Note that this is NOT "disk free"; some of the space will be used by the operating system and build utilities. Also note that this is the minimum disk size that will be allocated for the build -- the build may run with a larger disk than requested. At present, the maximum disk size is 1000GB; builds that request more than the maximum are rejected with an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#disk_size_gb GoogleCloudbuildTrigger#disk_size_gb}
        :param dynamic_substitutions: Option to specify whether or not to apply bash style string operations to the substitutions. NOTE this is always enabled for triggered builds and cannot be overridden in the build configuration file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dynamic_substitutions GoogleCloudbuildTrigger#dynamic_substitutions}
        :param env: A list of global environment variable definitions that will exist for all build steps in this build. If a variable is defined in both globally and in a build step, the variable will use the build step value. The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#env GoogleCloudbuildTrigger#env}
        :param logging: Option to specify the logging mode, which determines if and where build logs are stored. Possible values: ["LOGGING_UNSPECIFIED", "LEGACY", "GCS_ONLY", "STACKDRIVER_ONLY", "CLOUD_LOGGING_ONLY", "NONE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#logging GoogleCloudbuildTrigger#logging}
        :param log_streaming_option: Option to define build log streaming behavior to Google Cloud Storage. Possible values: ["STREAM_DEFAULT", "STREAM_ON", "STREAM_OFF"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#log_streaming_option GoogleCloudbuildTrigger#log_streaming_option}
        :param machine_type: Compute Engine machine type on which to run the build. Possible values: ["UNSPECIFIED", "N1_HIGHCPU_8", "N1_HIGHCPU_32", "E2_HIGHCPU_8", "E2_HIGHCPU_32"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#machine_type GoogleCloudbuildTrigger#machine_type}
        :param requested_verify_option: Requested verifiability options. Possible values: ["NOT_VERIFIED", "VERIFIED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#requested_verify_option GoogleCloudbuildTrigger#requested_verify_option}
        :param secret_env: A list of global environment variables, which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's Secret. These variables will be available to all build steps in this build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_env GoogleCloudbuildTrigger#secret_env}
        :param source_provenance_hash: Requested hash for SourceProvenance. Possible values: ["NONE", "SHA256", "MD5"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source_provenance_hash GoogleCloudbuildTrigger#source_provenance_hash}
        :param substitution_option: Option to specify behavior when there is an error in the substitution checks. NOTE this is always set to ALLOW_LOOSE for triggered builds and cannot be overridden in the build configuration file. Possible values: ["MUST_MATCH", "ALLOW_LOOSE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitution_option GoogleCloudbuildTrigger#substitution_option}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#volumes GoogleCloudbuildTrigger#volumes}
        :param worker_pool: Option to specify a WorkerPool for the build. Format projects/{project}/workerPools/{workerPool}. This field is experimental. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#worker_pool GoogleCloudbuildTrigger#worker_pool}
        '''
        value = GoogleCloudbuildTriggerBuildOptions(
            disk_size_gb=disk_size_gb,
            dynamic_substitutions=dynamic_substitutions,
            env=env,
            logging=logging,
            log_streaming_option=log_streaming_option,
            machine_type=machine_type,
            requested_verify_option=requested_verify_option,
            secret_env=secret_env,
            source_provenance_hash=source_provenance_hash,
            substitution_option=substitution_option,
            volumes=volumes,
            worker_pool=worker_pool,
        )

        return typing.cast(None, jsii.invoke(self, "putOptions", [value]))

    @jsii.member(jsii_name="putSecret")
    def put_secret(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildSecret", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOutputReference.put_secret)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecret", [value]))

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        *,
        repo_source: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildSourceRepoSource", typing.Dict[str, typing.Any]]] = None,
        storage_source: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildSourceStorageSource", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param repo_source: repo_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_source GoogleCloudbuildTrigger#repo_source}
        :param storage_source: storage_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#storage_source GoogleCloudbuildTrigger#storage_source}
        '''
        value = GoogleCloudbuildTriggerBuildSource(
            repo_source=repo_source, storage_source=storage_source
        )

        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putStep")
    def put_step(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildStep", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildOutputReference.put_step)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStep", [value]))

    @jsii.member(jsii_name="resetArtifacts")
    def reset_artifacts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArtifacts", []))

    @jsii.member(jsii_name="resetAvailableSecrets")
    def reset_available_secrets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvailableSecrets", []))

    @jsii.member(jsii_name="resetImages")
    def reset_images(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImages", []))

    @jsii.member(jsii_name="resetLogsBucket")
    def reset_logs_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogsBucket", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetQueueTtl")
    def reset_queue_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueueTtl", []))

    @jsii.member(jsii_name="resetSecret")
    def reset_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecret", []))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetSubstitutions")
    def reset_substitutions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubstitutions", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="artifacts")
    def artifacts(self) -> GoogleCloudbuildTriggerBuildArtifactsOutputReference:
        return typing.cast(GoogleCloudbuildTriggerBuildArtifactsOutputReference, jsii.get(self, "artifacts"))

    @builtins.property
    @jsii.member(jsii_name="availableSecrets")
    def available_secrets(
        self,
    ) -> GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference:
        return typing.cast(GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference, jsii.get(self, "availableSecrets"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> GoogleCloudbuildTriggerBuildOptionsOutputReference:
        return typing.cast(GoogleCloudbuildTriggerBuildOptionsOutputReference, jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> "GoogleCloudbuildTriggerBuildSecretList":
        return typing.cast("GoogleCloudbuildTriggerBuildSecretList", jsii.get(self, "secret"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "GoogleCloudbuildTriggerBuildSourceOutputReference":
        return typing.cast("GoogleCloudbuildTriggerBuildSourceOutputReference", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="step")
    def step(self) -> "GoogleCloudbuildTriggerBuildStepList":
        return typing.cast("GoogleCloudbuildTriggerBuildStepList", jsii.get(self, "step"))

    @builtins.property
    @jsii.member(jsii_name="artifactsInput")
    def artifacts_input(self) -> typing.Optional[GoogleCloudbuildTriggerBuildArtifacts]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildArtifacts], jsii.get(self, "artifactsInput"))

    @builtins.property
    @jsii.member(jsii_name="availableSecretsInput")
    def available_secrets_input(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerBuildAvailableSecrets]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildAvailableSecrets], jsii.get(self, "availableSecretsInput"))

    @builtins.property
    @jsii.member(jsii_name="imagesInput")
    def images_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "imagesInput"))

    @builtins.property
    @jsii.member(jsii_name="logsBucketInput")
    def logs_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logsBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(self) -> typing.Optional[GoogleCloudbuildTriggerBuildOptions]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildOptions], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="queueTtlInput")
    def queue_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queueTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildSecret"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildSecret"]]], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional["GoogleCloudbuildTriggerBuildSource"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildSource"], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="stepInput")
    def step_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStep"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStep"]]], jsii.get(self, "stepInput"))

    @builtins.property
    @jsii.member(jsii_name="substitutionsInput")
    def substitutions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "substitutionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="images")
    def images(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "images"))

    @images.setter
    def images(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOutputReference, "images").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "images", value)

    @builtins.property
    @jsii.member(jsii_name="logsBucket")
    def logs_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logsBucket"))

    @logs_bucket.setter
    def logs_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOutputReference, "logs_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logsBucket", value)

    @builtins.property
    @jsii.member(jsii_name="queueTtl")
    def queue_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queueTtl"))

    @queue_ttl.setter
    def queue_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOutputReference, "queue_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueTtl", value)

    @builtins.property
    @jsii.member(jsii_name="substitutions")
    def substitutions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "substitutions"))

    @substitutions.setter
    def substitutions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOutputReference, "substitutions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "substitutions", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerBuild]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuild], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuild],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSecret",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName", "secret_env": "secretEnv"},
)
class GoogleCloudbuildTriggerBuildSecret:
    def __init__(
        self,
        *,
        kms_key_name: builtins.str,
        secret_env: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param kms_key_name: Cloud KMS key name to use to decrypt these envs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#kms_key_name GoogleCloudbuildTrigger#kms_key_name}
        :param secret_env: Map of environment variable name to its encrypted value. Secret environment variables must be unique across all of a build's secrets, and must be used by at least one build step. Values can be at most 64 KB in size. There can be at most 100 secret values across all of a build's secrets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_env GoogleCloudbuildTrigger#secret_env}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSecret.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
            check_type(argname="argument secret_env", value=secret_env, expected_type=type_hints["secret_env"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }
        if secret_env is not None:
            self._values["secret_env"] = secret_env

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''Cloud KMS key name to use to decrypt these envs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#kms_key_name GoogleCloudbuildTrigger#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_env(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of environment variable name to its encrypted value.

        Secret environment variables must be unique across all of a build's secrets,
        and must be used by at least one build step. Values can be at most 64 KB in size.
        There can be at most 100 secret values across all of a build's secrets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_env GoogleCloudbuildTrigger#secret_env}
        '''
        result = self._values.get("secret_env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildSecret(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildSecretList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSecretList",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSecretList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudbuildTriggerBuildSecretOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSecretList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudbuildTriggerBuildSecretOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSecretList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSecretList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSecretList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildSecret]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildSecret]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildSecret]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSecretList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudbuildTriggerBuildSecretOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSecretOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSecretOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSecretEnv")
    def reset_secret_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretEnv", []))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretEnvInput")
    def secret_env_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secretEnvInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSecretOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="secretEnv")
    def secret_env(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secretEnv"))

    @secret_env.setter
    def secret_env(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSecretOutputReference, "secret_env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretEnv", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildSecret, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildSecret, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildSecret, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSecretOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSource",
    jsii_struct_bases=[],
    name_mapping={"repo_source": "repoSource", "storage_source": "storageSource"},
)
class GoogleCloudbuildTriggerBuildSource:
    def __init__(
        self,
        *,
        repo_source: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildSourceRepoSource", typing.Dict[str, typing.Any]]] = None,
        storage_source: typing.Optional[typing.Union["GoogleCloudbuildTriggerBuildSourceStorageSource", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param repo_source: repo_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_source GoogleCloudbuildTrigger#repo_source}
        :param storage_source: storage_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#storage_source GoogleCloudbuildTrigger#storage_source}
        '''
        if isinstance(repo_source, dict):
            repo_source = GoogleCloudbuildTriggerBuildSourceRepoSource(**repo_source)
        if isinstance(storage_source, dict):
            storage_source = GoogleCloudbuildTriggerBuildSourceStorageSource(**storage_source)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSource.__init__)
            check_type(argname="argument repo_source", value=repo_source, expected_type=type_hints["repo_source"])
            check_type(argname="argument storage_source", value=storage_source, expected_type=type_hints["storage_source"])
        self._values: typing.Dict[str, typing.Any] = {}
        if repo_source is not None:
            self._values["repo_source"] = repo_source
        if storage_source is not None:
            self._values["storage_source"] = storage_source

    @builtins.property
    def repo_source(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerBuildSourceRepoSource"]:
        '''repo_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_source GoogleCloudbuildTrigger#repo_source}
        '''
        result = self._values.get("repo_source")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildSourceRepoSource"], result)

    @builtins.property
    def storage_source(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerBuildSourceStorageSource"]:
        '''storage_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#storage_source GoogleCloudbuildTrigger#storage_source}
        '''
        result = self._values.get("storage_source")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildSourceStorageSource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSourceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRepoSource")
    def put_repo_source(
        self,
        *,
        repo_name: builtins.str,
        branch_name: typing.Optional[builtins.str] = None,
        commit_sha: typing.Optional[builtins.str] = None,
        dir: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project_id: typing.Optional[builtins.str] = None,
        substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tag_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repo_name: Name of the Cloud Source Repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_name GoogleCloudbuildTrigger#repo_name}
        :param branch_name: Regex matching branches to build. Exactly one a of branch name, tag, or commit SHA must be provided. The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at https://github.com/google/re2/wiki/Syntax Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch_name GoogleCloudbuildTrigger#branch_name}
        :param commit_sha: Explicit commit SHA to build. Exactly one a of branch name, tag, or commit SHA must be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#commit_sha GoogleCloudbuildTrigger#commit_sha}
        :param dir: Directory, relative to the source root, in which to run the build. This must be a relative path. If a step's dir is specified and is an absolute path, this value is ignored for that step's execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        :param invert_regex: Only trigger a build if the revision regex does NOT match the revision regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        :param project_id: ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project_id GoogleCloudbuildTrigger#project_id}
        :param substitutions: Substitutions to use in a triggered build. Should only be used with triggers.run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        :param tag_name: Regex matching tags to build. Exactly one a of branch name, tag, or commit SHA must be provided. The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at https://github.com/google/re2/wiki/Syntax Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag_name GoogleCloudbuildTrigger#tag_name}
        '''
        value = GoogleCloudbuildTriggerBuildSourceRepoSource(
            repo_name=repo_name,
            branch_name=branch_name,
            commit_sha=commit_sha,
            dir=dir,
            invert_regex=invert_regex,
            project_id=project_id,
            substitutions=substitutions,
            tag_name=tag_name,
        )

        return typing.cast(None, jsii.invoke(self, "putRepoSource", [value]))

    @jsii.member(jsii_name="putStorageSource")
    def put_storage_source(
        self,
        *,
        bucket: builtins.str,
        object: builtins.str,
        generation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Google Cloud Storage bucket containing the source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#bucket GoogleCloudbuildTrigger#bucket}
        :param object: Google Cloud Storage object containing the source. This object must be a gzipped archive file (.tar.gz) containing source to build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#object GoogleCloudbuildTrigger#object}
        :param generation: Google Cloud Storage generation for the object. If the generation is omitted, the latest generation will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#generation GoogleCloudbuildTrigger#generation}
        '''
        value = GoogleCloudbuildTriggerBuildSourceStorageSource(
            bucket=bucket, object=object, generation=generation
        )

        return typing.cast(None, jsii.invoke(self, "putStorageSource", [value]))

    @jsii.member(jsii_name="resetRepoSource")
    def reset_repo_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoSource", []))

    @jsii.member(jsii_name="resetStorageSource")
    def reset_storage_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageSource", []))

    @builtins.property
    @jsii.member(jsii_name="repoSource")
    def repo_source(
        self,
    ) -> "GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference":
        return typing.cast("GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference", jsii.get(self, "repoSource"))

    @builtins.property
    @jsii.member(jsii_name="storageSource")
    def storage_source(
        self,
    ) -> "GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference":
        return typing.cast("GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference", jsii.get(self, "storageSource"))

    @builtins.property
    @jsii.member(jsii_name="repoSourceInput")
    def repo_source_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerBuildSourceRepoSource"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildSourceRepoSource"], jsii.get(self, "repoSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageSourceInput")
    def storage_source_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerBuildSourceStorageSource"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerBuildSourceStorageSource"], jsii.get(self, "storageSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerBuildSource]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSourceRepoSource",
    jsii_struct_bases=[],
    name_mapping={
        "repo_name": "repoName",
        "branch_name": "branchName",
        "commit_sha": "commitSha",
        "dir": "dir",
        "invert_regex": "invertRegex",
        "project_id": "projectId",
        "substitutions": "substitutions",
        "tag_name": "tagName",
    },
)
class GoogleCloudbuildTriggerBuildSourceRepoSource:
    def __init__(
        self,
        *,
        repo_name: builtins.str,
        branch_name: typing.Optional[builtins.str] = None,
        commit_sha: typing.Optional[builtins.str] = None,
        dir: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project_id: typing.Optional[builtins.str] = None,
        substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tag_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param repo_name: Name of the Cloud Source Repository. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_name GoogleCloudbuildTrigger#repo_name}
        :param branch_name: Regex matching branches to build. Exactly one a of branch name, tag, or commit SHA must be provided. The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at https://github.com/google/re2/wiki/Syntax Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch_name GoogleCloudbuildTrigger#branch_name}
        :param commit_sha: Explicit commit SHA to build. Exactly one a of branch name, tag, or commit SHA must be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#commit_sha GoogleCloudbuildTrigger#commit_sha}
        :param dir: Directory, relative to the source root, in which to run the build. This must be a relative path. If a step's dir is specified and is an absolute path, this value is ignored for that step's execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        :param invert_regex: Only trigger a build if the revision regex does NOT match the revision regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        :param project_id: ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project_id GoogleCloudbuildTrigger#project_id}
        :param substitutions: Substitutions to use in a triggered build. Should only be used with triggers.run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        :param tag_name: Regex matching tags to build. Exactly one a of branch name, tag, or commit SHA must be provided. The syntax of the regular expressions accepted is the syntax accepted by RE2 and described at https://github.com/google/re2/wiki/Syntax Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag_name GoogleCloudbuildTrigger#tag_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSourceRepoSource.__init__)
            check_type(argname="argument repo_name", value=repo_name, expected_type=type_hints["repo_name"])
            check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
            check_type(argname="argument commit_sha", value=commit_sha, expected_type=type_hints["commit_sha"])
            check_type(argname="argument dir", value=dir, expected_type=type_hints["dir"])
            check_type(argname="argument invert_regex", value=invert_regex, expected_type=type_hints["invert_regex"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument substitutions", value=substitutions, expected_type=type_hints["substitutions"])
            check_type(argname="argument tag_name", value=tag_name, expected_type=type_hints["tag_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "repo_name": repo_name,
        }
        if branch_name is not None:
            self._values["branch_name"] = branch_name
        if commit_sha is not None:
            self._values["commit_sha"] = commit_sha
        if dir is not None:
            self._values["dir"] = dir
        if invert_regex is not None:
            self._values["invert_regex"] = invert_regex
        if project_id is not None:
            self._values["project_id"] = project_id
        if substitutions is not None:
            self._values["substitutions"] = substitutions
        if tag_name is not None:
            self._values["tag_name"] = tag_name

    @builtins.property
    def repo_name(self) -> builtins.str:
        '''Name of the Cloud Source Repository.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_name GoogleCloudbuildTrigger#repo_name}
        '''
        result = self._values.get("repo_name")
        assert result is not None, "Required property 'repo_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def branch_name(self) -> typing.Optional[builtins.str]:
        '''Regex matching branches to build.

        Exactly one a of branch name, tag, or commit SHA must be provided.
        The syntax of the regular expressions accepted is the syntax accepted by RE2 and
        described at https://github.com/google/re2/wiki/Syntax

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch_name GoogleCloudbuildTrigger#branch_name}
        '''
        result = self._values.get("branch_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_sha(self) -> typing.Optional[builtins.str]:
        '''Explicit commit SHA to build. Exactly one a of branch name, tag, or commit SHA must be provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#commit_sha GoogleCloudbuildTrigger#commit_sha}
        '''
        result = self._values.get("commit_sha")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dir(self) -> typing.Optional[builtins.str]:
        '''Directory, relative to the source root, in which to run the build.

        This must be a relative path. If a step's dir is specified and is an absolute path,
        this value is ignored for that step's execution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        '''
        result = self._values.get("dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invert_regex(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Only trigger a build if the revision regex does NOT match the revision regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        '''
        result = self._values.get("invert_regex")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''ID of the project that owns the Cloud Source Repository.

        If omitted, the project ID requesting the build is assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project_id GoogleCloudbuildTrigger#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def substitutions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Substitutions to use in a triggered build. Should only be used with triggers.run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        '''
        result = self._values.get("substitutions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tag_name(self) -> typing.Optional[builtins.str]:
        '''Regex matching tags to build.

        Exactly one a of branch name, tag, or commit SHA must be provided.
        The syntax of the regular expressions accepted is the syntax accepted by RE2 and
        described at https://github.com/google/re2/wiki/Syntax

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag_name GoogleCloudbuildTrigger#tag_name}
        '''
        result = self._values.get("tag_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildSourceRepoSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranchName")
    def reset_branch_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranchName", []))

    @jsii.member(jsii_name="resetCommitSha")
    def reset_commit_sha(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitSha", []))

    @jsii.member(jsii_name="resetDir")
    def reset_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDir", []))

    @jsii.member(jsii_name="resetInvertRegex")
    def reset_invert_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvertRegex", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="resetSubstitutions")
    def reset_substitutions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubstitutions", []))

    @jsii.member(jsii_name="resetTagName")
    def reset_tag_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagName", []))

    @builtins.property
    @jsii.member(jsii_name="branchNameInput")
    def branch_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchNameInput"))

    @builtins.property
    @jsii.member(jsii_name="commitShaInput")
    def commit_sha_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitShaInput"))

    @builtins.property
    @jsii.member(jsii_name="dirInput")
    def dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dirInput"))

    @builtins.property
    @jsii.member(jsii_name="invertRegexInput")
    def invert_regex_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "invertRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="repoNameInput")
    def repo_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoNameInput"))

    @builtins.property
    @jsii.member(jsii_name="substitutionsInput")
    def substitutions_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "substitutionsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagNameInput")
    def tag_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagNameInput"))

    @builtins.property
    @jsii.member(jsii_name="branchName")
    def branch_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchName"))

    @branch_name.setter
    def branch_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "branch_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branchName", value)

    @builtins.property
    @jsii.member(jsii_name="commitSha")
    def commit_sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitSha"))

    @commit_sha.setter
    def commit_sha(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "commit_sha").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitSha", value)

    @builtins.property
    @jsii.member(jsii_name="dir")
    def dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dir"))

    @dir.setter
    def dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dir", value)

    @builtins.property
    @jsii.member(jsii_name="invertRegex")
    def invert_regex(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "invertRegex"))

    @invert_regex.setter
    def invert_regex(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "invert_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invertRegex", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="repoName")
    def repo_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoName"))

    @repo_name.setter
    def repo_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "repo_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoName", value)

    @builtins.property
    @jsii.member(jsii_name="substitutions")
    def substitutions(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "substitutions"))

    @substitutions.setter
    def substitutions(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "substitutions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "substitutions", value)

    @builtins.property
    @jsii.member(jsii_name="tagName")
    def tag_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagName"))

    @tag_name.setter
    def tag_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "tag_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerBuildSourceRepoSource]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildSourceRepoSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildSourceRepoSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSourceStorageSource",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "object": "object", "generation": "generation"},
)
class GoogleCloudbuildTriggerBuildSourceStorageSource:
    def __init__(
        self,
        *,
        bucket: builtins.str,
        object: builtins.str,
        generation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: Google Cloud Storage bucket containing the source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#bucket GoogleCloudbuildTrigger#bucket}
        :param object: Google Cloud Storage object containing the source. This object must be a gzipped archive file (.tar.gz) containing source to build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#object GoogleCloudbuildTrigger#object}
        :param generation: Google Cloud Storage generation for the object. If the generation is omitted, the latest generation will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#generation GoogleCloudbuildTrigger#generation}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSourceStorageSource.__init__)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument generation", value=generation, expected_type=type_hints["generation"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
            "object": object,
        }
        if generation is not None:
            self._values["generation"] = generation

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Google Cloud Storage bucket containing the source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#bucket GoogleCloudbuildTrigger#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object(self) -> builtins.str:
        '''Google Cloud Storage object containing the source. This object must be a gzipped archive file (.tar.gz) containing source to build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#object GoogleCloudbuildTrigger#object}
        '''
        result = self._values.get("object")
        assert result is not None, "Required property 'object' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def generation(self) -> typing.Optional[builtins.str]:
        '''Google Cloud Storage generation for the object.  If the generation is omitted, the latest generation will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#generation GoogleCloudbuildTrigger#generation}
        '''
        result = self._values.get("generation")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildSourceStorageSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGeneration")
    def reset_generation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeneration", []))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="generationInput")
    def generation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generationInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference, "bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generation"))

    @generation.setter
    def generation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference, "generation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generation", value)

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "object"))

    @object.setter
    def object(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference, "object").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "object", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerBuildSourceStorageSource]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuildSourceStorageSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerBuildSourceStorageSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildStep",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "args": "args",
        "dir": "dir",
        "entrypoint": "entrypoint",
        "env": "env",
        "id": "id",
        "secret_env": "secretEnv",
        "timeout": "timeout",
        "timing": "timing",
        "volumes": "volumes",
        "wait_for": "waitFor",
    },
)
class GoogleCloudbuildTriggerBuildStep:
    def __init__(
        self,
        *,
        name: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        dir: typing.Optional[builtins.str] = None,
        entrypoint: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        secret_env: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeout: typing.Optional[builtins.str] = None,
        timing: typing.Optional[builtins.str] = None,
        volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildStepVolumes", typing.Dict[str, typing.Any]]]]] = None,
        wait_for: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: The name of the container image that will run this particular build step. If the image is available in the host's Docker daemon's cache, it will be run directly. If not, the host will attempt to pull the image first, using the builder service account's credentials if necessary. The Docker daemon's cache will already have the latest versions of all of the officially supported build steps (see https://github.com/GoogleCloudPlatform/cloud-builders for images and examples). The Docker daemon will also have cached many of the layers for some popular images, like "ubuntu", "debian", but they will be refreshed at the time you attempt to use them. If you built an image in a previous build step, it will be stored in the host's Docker daemon's cache and is available to use as the name for a later build step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        :param args: A list of arguments that will be presented to the step when it is started. If the image used to run the step's container has an entrypoint, the args are used as arguments to that entrypoint. If the image does not define an entrypoint, the first element in args is used as the entrypoint, and the remainder will be used as arguments. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#args GoogleCloudbuildTrigger#args}
        :param dir: Working directory to use when running this step's container. If this value is a relative path, it is relative to the build's working directory. If this value is absolute, it may be outside the build's working directory, in which case the contents of the path may not be persisted across build step executions, unless a 'volume' for that path is specified. If the build specifies a 'RepoSource' with 'dir' and a step with a 'dir', which specifies an absolute path, the 'RepoSource' 'dir' is ignored for the step's execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        :param entrypoint: Entrypoint to be used instead of the build step image's default entrypoint. If unset, the image's default entrypoint is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#entrypoint GoogleCloudbuildTrigger#entrypoint}
        :param env: A list of environment variable definitions to be used when running a step. The elements are of the form "KEY=VALUE" for the environment variable "KEY" being given the value "VALUE". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#env GoogleCloudbuildTrigger#env}
        :param id: Unique identifier for this build step, used in 'wait_for' to reference this build step as a dependency. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#id GoogleCloudbuildTrigger#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param secret_env: A list of environment variables which are encrypted using a Cloud Key Management Service crypto key. These values must be specified in the build's 'Secret'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_env GoogleCloudbuildTrigger#secret_env}
        :param timeout: Time limit for executing this build step. If not defined, the step has no time limit and will be allowed to continue to run until either it completes or the build itself times out. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeout GoogleCloudbuildTrigger#timeout}
        :param timing: Output only. Stores timing information for executing this build step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timing GoogleCloudbuildTrigger#timing}
        :param volumes: volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#volumes GoogleCloudbuildTrigger#volumes}
        :param wait_for: The ID(s) of the step(s) that this build step depends on. This build step will not start until all the build steps in 'wait_for' have completed successfully. If 'wait_for' is empty, this build step will start when all previous build steps in the 'Build.Steps' list have completed successfully. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#wait_for GoogleCloudbuildTrigger#wait_for}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStep.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument dir", value=dir, expected_type=type_hints["dir"])
            check_type(argname="argument entrypoint", value=entrypoint, expected_type=type_hints["entrypoint"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument secret_env", value=secret_env, expected_type=type_hints["secret_env"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument timing", value=timing, expected_type=type_hints["timing"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
            check_type(argname="argument wait_for", value=wait_for, expected_type=type_hints["wait_for"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if args is not None:
            self._values["args"] = args
        if dir is not None:
            self._values["dir"] = dir
        if entrypoint is not None:
            self._values["entrypoint"] = entrypoint
        if env is not None:
            self._values["env"] = env
        if id is not None:
            self._values["id"] = id
        if secret_env is not None:
            self._values["secret_env"] = secret_env
        if timeout is not None:
            self._values["timeout"] = timeout
        if timing is not None:
            self._values["timing"] = timing
        if volumes is not None:
            self._values["volumes"] = volumes
        if wait_for is not None:
            self._values["wait_for"] = wait_for

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the container image that will run this particular build step.

        If the image is available in the host's Docker daemon's cache, it will be
        run directly. If not, the host will attempt to pull the image first, using
        the builder service account's credentials if necessary.

        The Docker daemon's cache will already have the latest versions of all of
        the officially supported build steps (see https://github.com/GoogleCloudPlatform/cloud-builders
        for images and examples).
        The Docker daemon will also have cached many of the layers for some popular
        images, like "ubuntu", "debian", but they will be refreshed at the time
        you attempt to use them.

        If you built an image in a previous build step, it will be stored in the
        host's Docker daemon's cache and is available to use as the name for a
        later build step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of arguments that will be presented to the step when it is started.

        If the image used to run the step's container has an entrypoint, the args
        are used as arguments to that entrypoint. If the image does not define an
        entrypoint, the first element in args is used as the entrypoint, and the
        remainder will be used as arguments.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#args GoogleCloudbuildTrigger#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def dir(self) -> typing.Optional[builtins.str]:
        '''Working directory to use when running this step's container.

        If this value is a relative path, it is relative to the build's working
        directory. If this value is absolute, it may be outside the build's working
        directory, in which case the contents of the path may not be persisted
        across build step executions, unless a 'volume' for that path is specified.

        If the build specifies a 'RepoSource' with 'dir' and a step with a
        'dir',
        which specifies an absolute path, the 'RepoSource' 'dir' is ignored
        for the step's execution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        '''
        result = self._values.get("dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entrypoint(self) -> typing.Optional[builtins.str]:
        '''Entrypoint to be used instead of the build step image's default entrypoint. If unset, the image's default entrypoint is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#entrypoint GoogleCloudbuildTrigger#entrypoint}
        '''
        result = self._values.get("entrypoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of environment variable definitions to be used when running a step.

        The elements are of the form "KEY=VALUE" for the environment variable
        "KEY" being given the value "VALUE".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#env GoogleCloudbuildTrigger#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier for this build step, used in 'wait_for' to reference this build step as a dependency.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#id GoogleCloudbuildTrigger#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_env(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of environment variables which are encrypted using a Cloud Key Management Service crypto key.

        These values must be specified in
        the build's 'Secret'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret_env GoogleCloudbuildTrigger#secret_env}
        '''
        result = self._values.get("secret_env")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[builtins.str]:
        '''Time limit for executing this build step.

        If not defined,
        the step has no
        time limit and will be allowed to continue to run until either it
        completes or the build itself times out.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeout GoogleCloudbuildTrigger#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timing(self) -> typing.Optional[builtins.str]:
        '''Output only. Stores timing information for executing this build step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timing GoogleCloudbuildTrigger#timing}
        '''
        result = self._values.get("timing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volumes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStepVolumes"]]]:
        '''volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#volumes GoogleCloudbuildTrigger#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStepVolumes"]]], result)

    @builtins.property
    def wait_for(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ID(s) of the step(s) that this build step depends on.

        This build step will not start until all the build steps in 'wait_for'
        have completed successfully. If 'wait_for' is empty, this build step
        will start when all previous build steps in the 'Build.Steps' list
        have completed successfully.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#wait_for GoogleCloudbuildTrigger#wait_for}
        '''
        result = self._values.get("wait_for")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildStep(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildStepList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildStepList",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudbuildTriggerBuildStepOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudbuildTriggerBuildStepOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildStep]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildStep]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildStep]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudbuildTriggerBuildStepOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildStepOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putVolumes")
    def put_volumes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleCloudbuildTriggerBuildStepVolumes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepOutputReference.put_volumes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVolumes", [value]))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetDir")
    def reset_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDir", []))

    @jsii.member(jsii_name="resetEntrypoint")
    def reset_entrypoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntrypoint", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecretEnv")
    def reset_secret_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretEnv", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="resetTiming")
    def reset_timing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTiming", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @jsii.member(jsii_name="resetWaitFor")
    def reset_wait_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitFor", []))

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> "GoogleCloudbuildTriggerBuildStepVolumesList":
        return typing.cast("GoogleCloudbuildTriggerBuildStepVolumesList", jsii.get(self, "volumes"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="dirInput")
    def dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dirInput"))

    @builtins.property
    @jsii.member(jsii_name="entrypointInput")
    def entrypoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entrypointInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretEnvInput")
    def secret_env_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secretEnvInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="timingInput")
    def timing_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timingInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStepVolumes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleCloudbuildTriggerBuildStepVolumes"]]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForInput")
    def wait_for_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "waitForInput"))

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="dir")
    def dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dir"))

    @dir.setter
    def dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dir", value)

    @builtins.property
    @jsii.member(jsii_name="entrypoint")
    def entrypoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entrypoint"))

    @entrypoint.setter
    def entrypoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "entrypoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entrypoint", value)

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "env"))

    @env.setter
    def env(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "env", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="secretEnv")
    def secret_env(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secretEnv"))

    @secret_env.setter
    def secret_env(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "secret_env").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretEnv", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="timing")
    def timing(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timing"))

    @timing.setter
    def timing(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "timing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timing", value)

    @builtins.property
    @jsii.member(jsii_name="waitFor")
    def wait_for(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "waitFor"))

    @wait_for.setter
    def wait_for(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "wait_for").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitFor", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildStep, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildStep, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildStep, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildStepVolumes",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "path": "path"},
)
class GoogleCloudbuildTriggerBuildStepVolumes:
    def __init__(self, *, name: builtins.str, path: builtins.str) -> None:
        '''
        :param name: Name of the volume to mount. Volume names must be unique per build step and must be valid names for Docker volumes. Each named volume must be used by at least two build steps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        :param path: Path at which to mount the volume. Paths must be absolute and cannot conflict with other volume paths on the same build step or with certain reserved volume paths. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#path GoogleCloudbuildTrigger#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepVolumes.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "path": path,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the volume to mount.

        Volume names must be unique per build step and must be valid names for
        Docker volumes. Each named volume must be used by at least two build steps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''Path at which to mount the volume.

        Paths must be absolute and cannot conflict with other volume paths on
        the same build step or with certain reserved volume paths.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#path GoogleCloudbuildTrigger#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerBuildStepVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerBuildStepVolumesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildStepVolumesList",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepVolumesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleCloudbuildTriggerBuildStepVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepVolumesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleCloudbuildTriggerBuildStepVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepVolumesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepVolumesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepVolumesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildStepVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildStepVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleCloudbuildTriggerBuildStepVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepVolumesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleCloudbuildTriggerBuildStepVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerBuildStepVolumesOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerBuildStepVolumesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepVolumesOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepVolumesOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildStepVolumes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildStepVolumes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudbuildTriggerBuildStepVolumes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerBuildStepVolumesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "approval_config": "approvalConfig",
        "build_attribute": "buildAttribute",
        "description": "description",
        "disabled": "disabled",
        "filename": "filename",
        "filter": "filter",
        "git_file_source": "gitFileSource",
        "github": "github",
        "id": "id",
        "ignored_files": "ignoredFiles",
        "include_build_logs": "includeBuildLogs",
        "included_files": "includedFiles",
        "location": "location",
        "name": "name",
        "project": "project",
        "pubsub_config": "pubsubConfig",
        "service_account": "serviceAccount",
        "source_to_build": "sourceToBuild",
        "substitutions": "substitutions",
        "tags": "tags",
        "timeouts": "timeouts",
        "trigger_template": "triggerTemplate",
        "webhook_config": "webhookConfig",
    },
)
class GoogleCloudbuildTriggerConfig(cdktf.TerraformMetaArguments):
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
        approval_config: typing.Optional[typing.Union[GoogleCloudbuildTriggerApprovalConfig, typing.Dict[str, typing.Any]]] = None,
        build_attribute: typing.Optional[typing.Union[GoogleCloudbuildTriggerBuild, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filename: typing.Optional[builtins.str] = None,
        filter: typing.Optional[builtins.str] = None,
        git_file_source: typing.Optional[typing.Union["GoogleCloudbuildTriggerGitFileSource", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["GoogleCloudbuildTriggerGithub", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ignored_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        include_build_logs: typing.Optional[builtins.str] = None,
        included_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        location: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        pubsub_config: typing.Optional[typing.Union["GoogleCloudbuildTriggerPubsubConfig", typing.Dict[str, typing.Any]]] = None,
        service_account: typing.Optional[builtins.str] = None,
        source_to_build: typing.Optional[typing.Union["GoogleCloudbuildTriggerSourceToBuild", typing.Dict[str, typing.Any]]] = None,
        substitutions: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleCloudbuildTriggerTimeouts", typing.Dict[str, typing.Any]]] = None,
        trigger_template: typing.Optional[typing.Union["GoogleCloudbuildTriggerTriggerTemplate", typing.Dict[str, typing.Any]]] = None,
        webhook_config: typing.Optional[typing.Union["GoogleCloudbuildTriggerWebhookConfig", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param approval_config: approval_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#approval_config GoogleCloudbuildTrigger#approval_config}
        :param build_attribute: build block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#build GoogleCloudbuildTrigger#build}
        :param description: Human-readable description of the trigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#description GoogleCloudbuildTrigger#description}
        :param disabled: Whether the trigger is disabled or not. If true, the trigger will never result in a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#disabled GoogleCloudbuildTrigger#disabled}
        :param filename: Path, from the source root, to a file whose contents is used for the template. Either a filename or build template must be provided. Set this only when using trigger_template or github. When using Pub/Sub, Webhook or Manual set the file name using git_file_source instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#filename GoogleCloudbuildTrigger#filename}
        :param filter: A Common Expression Language string. Used only with Pub/Sub and Webhook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#filter GoogleCloudbuildTrigger#filter}
        :param git_file_source: git_file_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#git_file_source GoogleCloudbuildTrigger#git_file_source}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#github GoogleCloudbuildTrigger#github}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#id GoogleCloudbuildTrigger#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignored_files: ignoredFiles and includedFiles are file glob matches using https://golang.org/pkg/path/filepath/#Match extended with support for '**'. If ignoredFiles and changed files are both empty, then they are not used to determine whether or not to trigger a build. If ignoredFiles is not empty, then we ignore any files that match any of the ignored_file globs. If the change has no files that are outside of the ignoredFiles globs, then we do not trigger a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#ignored_files GoogleCloudbuildTrigger#ignored_files}
        :param include_build_logs: Build logs will be sent back to GitHub as part of the checkrun result. Values can be INCLUDE_BUILD_LOGS_UNSPECIFIED or INCLUDE_BUILD_LOGS_WITH_STATUS Possible values: ["INCLUDE_BUILD_LOGS_UNSPECIFIED", "INCLUDE_BUILD_LOGS_WITH_STATUS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#include_build_logs GoogleCloudbuildTrigger#include_build_logs}
        :param included_files: ignoredFiles and includedFiles are file glob matches using https://golang.org/pkg/path/filepath/#Match extended with support for '**'. If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is empty, then as far as this filter is concerned, we should trigger the build. If any of the files altered in the commit pass the ignoredFiles filter and includedFiles is not empty, then we make sure that at least one of those files matches a includedFiles glob. If not, then we do not trigger a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#included_files GoogleCloudbuildTrigger#included_files}
        :param location: The `Cloud Build location <https://cloud.google.com/build/docs/locations>`_ for the trigger. If not specified, "global" is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#location GoogleCloudbuildTrigger#location}
        :param name: Name of the trigger. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project GoogleCloudbuildTrigger#project}.
        :param pubsub_config: pubsub_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#pubsub_config GoogleCloudbuildTrigger#pubsub_config}
        :param service_account: The service account used for all user-controlled operations including triggers.patch, triggers.run, builds.create, and builds.cancel. If no service account is set, then the standard Cloud Build service account ([PROJECT_NUM]@system.gserviceaccount.com) will be used instead. Format: projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#service_account GoogleCloudbuildTrigger#service_account}
        :param source_to_build: source_to_build block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source_to_build GoogleCloudbuildTrigger#source_to_build}
        :param substitutions: Substitutions data for Build resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        :param tags: Tags for annotation of a BuildTrigger. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tags GoogleCloudbuildTrigger#tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeouts GoogleCloudbuildTrigger#timeouts}
        :param trigger_template: trigger_template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#trigger_template GoogleCloudbuildTrigger#trigger_template}
        :param webhook_config: webhook_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#webhook_config GoogleCloudbuildTrigger#webhook_config}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(approval_config, dict):
            approval_config = GoogleCloudbuildTriggerApprovalConfig(**approval_config)
        if isinstance(build_attribute, dict):
            build_attribute = GoogleCloudbuildTriggerBuild(**build_attribute)
        if isinstance(git_file_source, dict):
            git_file_source = GoogleCloudbuildTriggerGitFileSource(**git_file_source)
        if isinstance(github, dict):
            github = GoogleCloudbuildTriggerGithub(**github)
        if isinstance(pubsub_config, dict):
            pubsub_config = GoogleCloudbuildTriggerPubsubConfig(**pubsub_config)
        if isinstance(source_to_build, dict):
            source_to_build = GoogleCloudbuildTriggerSourceToBuild(**source_to_build)
        if isinstance(timeouts, dict):
            timeouts = GoogleCloudbuildTriggerTimeouts(**timeouts)
        if isinstance(trigger_template, dict):
            trigger_template = GoogleCloudbuildTriggerTriggerTemplate(**trigger_template)
        if isinstance(webhook_config, dict):
            webhook_config = GoogleCloudbuildTriggerWebhookConfig(**webhook_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument approval_config", value=approval_config, expected_type=type_hints["approval_config"])
            check_type(argname="argument build_attribute", value=build_attribute, expected_type=type_hints["build_attribute"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            check_type(argname="argument git_file_source", value=git_file_source, expected_type=type_hints["git_file_source"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignored_files", value=ignored_files, expected_type=type_hints["ignored_files"])
            check_type(argname="argument include_build_logs", value=include_build_logs, expected_type=type_hints["include_build_logs"])
            check_type(argname="argument included_files", value=included_files, expected_type=type_hints["included_files"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument pubsub_config", value=pubsub_config, expected_type=type_hints["pubsub_config"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
            check_type(argname="argument source_to_build", value=source_to_build, expected_type=type_hints["source_to_build"])
            check_type(argname="argument substitutions", value=substitutions, expected_type=type_hints["substitutions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument trigger_template", value=trigger_template, expected_type=type_hints["trigger_template"])
            check_type(argname="argument webhook_config", value=webhook_config, expected_type=type_hints["webhook_config"])
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
        if approval_config is not None:
            self._values["approval_config"] = approval_config
        if build_attribute is not None:
            self._values["build_attribute"] = build_attribute
        if description is not None:
            self._values["description"] = description
        if disabled is not None:
            self._values["disabled"] = disabled
        if filename is not None:
            self._values["filename"] = filename
        if filter is not None:
            self._values["filter"] = filter
        if git_file_source is not None:
            self._values["git_file_source"] = git_file_source
        if github is not None:
            self._values["github"] = github
        if id is not None:
            self._values["id"] = id
        if ignored_files is not None:
            self._values["ignored_files"] = ignored_files
        if include_build_logs is not None:
            self._values["include_build_logs"] = include_build_logs
        if included_files is not None:
            self._values["included_files"] = included_files
        if location is not None:
            self._values["location"] = location
        if name is not None:
            self._values["name"] = name
        if project is not None:
            self._values["project"] = project
        if pubsub_config is not None:
            self._values["pubsub_config"] = pubsub_config
        if service_account is not None:
            self._values["service_account"] = service_account
        if source_to_build is not None:
            self._values["source_to_build"] = source_to_build
        if substitutions is not None:
            self._values["substitutions"] = substitutions
        if tags is not None:
            self._values["tags"] = tags
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if trigger_template is not None:
            self._values["trigger_template"] = trigger_template
        if webhook_config is not None:
            self._values["webhook_config"] = webhook_config

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
    def approval_config(self) -> typing.Optional[GoogleCloudbuildTriggerApprovalConfig]:
        '''approval_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#approval_config GoogleCloudbuildTrigger#approval_config}
        '''
        result = self._values.get("approval_config")
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerApprovalConfig], result)

    @builtins.property
    def build_attribute(self) -> typing.Optional[GoogleCloudbuildTriggerBuild]:
        '''build block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#build GoogleCloudbuildTrigger#build}
        '''
        result = self._values.get("build_attribute")
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerBuild], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human-readable description of the trigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#description GoogleCloudbuildTrigger#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the trigger is disabled or not. If true, the trigger will never result in a build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#disabled GoogleCloudbuildTrigger#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def filename(self) -> typing.Optional[builtins.str]:
        '''Path, from the source root, to a file whose contents is used for the template.

        Either a filename or build template must be provided. Set this only when using trigger_template or github.
        When using Pub/Sub, Webhook or Manual set the file name using git_file_source instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#filename GoogleCloudbuildTrigger#filename}
        '''
        result = self._values.get("filename")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filter(self) -> typing.Optional[builtins.str]:
        '''A Common Expression Language string. Used only with Pub/Sub and Webhook.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#filter GoogleCloudbuildTrigger#filter}
        '''
        result = self._values.get("filter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git_file_source(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerGitFileSource"]:
        '''git_file_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#git_file_source GoogleCloudbuildTrigger#git_file_source}
        '''
        result = self._values.get("git_file_source")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGitFileSource"], result)

    @builtins.property
    def github(self) -> typing.Optional["GoogleCloudbuildTriggerGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#github GoogleCloudbuildTrigger#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGithub"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#id GoogleCloudbuildTrigger#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignored_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''ignoredFiles and includedFiles are file glob matches using https://golang.org/pkg/path/filepath/#Match extended with support for '**'.

        If ignoredFiles and changed files are both empty, then they are not
        used to determine whether or not to trigger a build.

        If ignoredFiles is not empty, then we ignore any files that match any
        of the ignored_file globs. If the change has no files that are outside
        of the ignoredFiles globs, then we do not trigger a build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#ignored_files GoogleCloudbuildTrigger#ignored_files}
        '''
        result = self._values.get("ignored_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def include_build_logs(self) -> typing.Optional[builtins.str]:
        '''Build logs will be sent back to GitHub as part of the checkrun result.

        Values can be INCLUDE_BUILD_LOGS_UNSPECIFIED or
        INCLUDE_BUILD_LOGS_WITH_STATUS Possible values: ["INCLUDE_BUILD_LOGS_UNSPECIFIED", "INCLUDE_BUILD_LOGS_WITH_STATUS"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#include_build_logs GoogleCloudbuildTrigger#include_build_logs}
        '''
        result = self._values.get("include_build_logs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def included_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''ignoredFiles and includedFiles are file glob matches using https://golang.org/pkg/path/filepath/#Match extended with support for '**'.

        If any of the files altered in the commit pass the ignoredFiles filter
        and includedFiles is empty, then as far as this filter is concerned, we
        should trigger the build.

        If any of the files altered in the commit pass the ignoredFiles filter
        and includedFiles is not empty, then we make sure that at least one of
        those files matches a includedFiles glob. If not, then we do not trigger
        a build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#included_files GoogleCloudbuildTrigger#included_files}
        '''
        result = self._values.get("included_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The `Cloud Build location <https://cloud.google.com/build/docs/locations>`_ for the trigger. If not specified, "global" is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#location GoogleCloudbuildTrigger#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the trigger. Must be unique within the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project GoogleCloudbuildTrigger#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pubsub_config(self) -> typing.Optional["GoogleCloudbuildTriggerPubsubConfig"]:
        '''pubsub_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#pubsub_config GoogleCloudbuildTrigger#pubsub_config}
        '''
        result = self._values.get("pubsub_config")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerPubsubConfig"], result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''The service account used for all user-controlled operations including triggers.patch, triggers.run, builds.create, and builds.cancel.

        If no service account is set, then the standard Cloud Build service account
        ([PROJECT_NUM]@system.gserviceaccount.com) will be used instead.

        Format: projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT_ID_OR_EMAIL}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#service_account GoogleCloudbuildTrigger#service_account}
        '''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_to_build(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerSourceToBuild"]:
        '''source_to_build block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#source_to_build GoogleCloudbuildTrigger#source_to_build}
        '''
        result = self._values.get("source_to_build")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerSourceToBuild"], result)

    @builtins.property
    def substitutions(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Substitutions data for Build resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#substitutions GoogleCloudbuildTrigger#substitutions}
        '''
        result = self._values.get("substitutions")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Tags for annotation of a BuildTrigger.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tags GoogleCloudbuildTrigger#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleCloudbuildTriggerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#timeouts GoogleCloudbuildTrigger#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerTimeouts"], result)

    @builtins.property
    def trigger_template(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerTriggerTemplate"]:
        '''trigger_template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#trigger_template GoogleCloudbuildTrigger#trigger_template}
        '''
        result = self._values.get("trigger_template")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerTriggerTemplate"], result)

    @builtins.property
    def webhook_config(self) -> typing.Optional["GoogleCloudbuildTriggerWebhookConfig"]:
        '''webhook_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#webhook_config GoogleCloudbuildTrigger#webhook_config}
        '''
        result = self._values.get("webhook_config")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerWebhookConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGitFileSource",
    jsii_struct_bases=[],
    name_mapping={
        "path": "path",
        "repo_type": "repoType",
        "revision": "revision",
        "uri": "uri",
    },
)
class GoogleCloudbuildTriggerGitFileSource:
    def __init__(
        self,
        *,
        path: builtins.str,
        repo_type: builtins.str,
        revision: typing.Optional[builtins.str] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: The path of the file, with the repo root as the root of the path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#path GoogleCloudbuildTrigger#path}
        :param repo_type: The type of the repo, since it may not be explicit from the repo field (e.g from a URL). Values can be UNKNOWN, CLOUD_SOURCE_REPOSITORIES, GITHUB, BITBUCKET Possible values: ["UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB", "BITBUCKET"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_type GoogleCloudbuildTrigger#repo_type}
        :param revision: The branch, tag, arbitrary ref, or SHA version of the repo to use when resolving the filename (optional). This field respects the same syntax/resolution as described here: https://git-scm.com/docs/gitrevisions If unspecified, the revision from which the trigger invocation originated is assumed to be the revision from which to read the specified path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#revision GoogleCloudbuildTrigger#revision}
        :param uri: The URI of the repo (optional). If unspecified, the repo from which the trigger invocation originated is assumed to be the repo from which to read the specified path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#uri GoogleCloudbuildTrigger#uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGitFileSource.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument repo_type", value=repo_type, expected_type=type_hints["repo_type"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
            "repo_type": repo_type,
        }
        if revision is not None:
            self._values["revision"] = revision
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def path(self) -> builtins.str:
        '''The path of the file, with the repo root as the root of the path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#path GoogleCloudbuildTrigger#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo_type(self) -> builtins.str:
        '''The type of the repo, since it may not be explicit from the repo field (e.g from a URL).  Values can be UNKNOWN, CLOUD_SOURCE_REPOSITORIES, GITHUB, BITBUCKET Possible values: ["UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB", "BITBUCKET"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_type GoogleCloudbuildTrigger#repo_type}
        '''
        result = self._values.get("repo_type")
        assert result is not None, "Required property 'repo_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> typing.Optional[builtins.str]:
        '''The branch, tag, arbitrary ref, or SHA version of the repo to use when resolving the  filename (optional).

        This field respects the same syntax/resolution as described here: https://git-scm.com/docs/gitrevisions
        If unspecified, the revision from which the trigger invocation originated is assumed to be the revision from which to read the specified path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#revision GoogleCloudbuildTrigger#revision}
        '''
        result = self._values.get("revision")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The URI of the repo (optional).

        If unspecified, the repo from which the trigger
        invocation originated is assumed to be the repo from which to read the specified path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#uri GoogleCloudbuildTrigger#uri}
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerGitFileSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerGitFileSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGitFileSourceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGitFileSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRevision")
    def reset_revision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRevision", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="repoTypeInput")
    def repo_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="revisionInput")
    def revision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGitFileSourceOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="repoType")
    def repo_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoType"))

    @repo_type.setter
    def repo_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGitFileSourceOutputReference, "repo_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoType", value)

    @builtins.property
    @jsii.member(jsii_name="revision")
    def revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "revision"))

    @revision.setter
    def revision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGitFileSourceOutputReference, "revision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revision", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGitFileSourceOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerGitFileSource]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerGitFileSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerGitFileSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGitFileSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGithub",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "owner": "owner",
        "pull_request": "pullRequest",
        "push": "push",
    },
)
class GoogleCloudbuildTriggerGithub:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        owner: typing.Optional[builtins.str] = None,
        pull_request: typing.Optional[typing.Union["GoogleCloudbuildTriggerGithubPullRequest", typing.Dict[str, typing.Any]]] = None,
        push: typing.Optional[typing.Union["GoogleCloudbuildTriggerGithubPush", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the repository. For example: The name for https://github.com/googlecloudplatform/cloud-builders is "cloud-builders". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        :param owner: Owner of the repository. For example: The owner for https://github.com/googlecloudplatform/cloud-builders is "googlecloudplatform". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#owner GoogleCloudbuildTrigger#owner}
        :param pull_request: pull_request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#pull_request GoogleCloudbuildTrigger#pull_request}
        :param push: push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#push GoogleCloudbuildTrigger#push}
        '''
        if isinstance(pull_request, dict):
            pull_request = GoogleCloudbuildTriggerGithubPullRequest(**pull_request)
        if isinstance(push, dict):
            push = GoogleCloudbuildTriggerGithubPush(**push)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGithub.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
            check_type(argname="argument pull_request", value=pull_request, expected_type=type_hints["pull_request"])
            check_type(argname="argument push", value=push, expected_type=type_hints["push"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if owner is not None:
            self._values["owner"] = owner
        if pull_request is not None:
            self._values["pull_request"] = pull_request
        if push is not None:
            self._values["push"] = push

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the repository. For example: The name for https://github.com/googlecloudplatform/cloud-builders is "cloud-builders".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#name GoogleCloudbuildTrigger#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def owner(self) -> typing.Optional[builtins.str]:
        '''Owner of the repository. For example: The owner for https://github.com/googlecloudplatform/cloud-builders is "googlecloudplatform".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#owner GoogleCloudbuildTrigger#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pull_request(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerGithubPullRequest"]:
        '''pull_request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#pull_request GoogleCloudbuildTrigger#pull_request}
        '''
        result = self._values.get("pull_request")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGithubPullRequest"], result)

    @builtins.property
    def push(self) -> typing.Optional["GoogleCloudbuildTriggerGithubPush"]:
        '''push block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#push GoogleCloudbuildTrigger#push}
        '''
        result = self._values.get("push")
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGithubPush"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGithubOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPullRequest")
    def put_pull_request(
        self,
        *,
        branch: builtins.str,
        comment_control: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param branch: Regex of branches to match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch GoogleCloudbuildTrigger#branch}
        :param comment_control: Whether to block builds on a "/gcbrun" comment from a repository owner or collaborator. Possible values: ["COMMENTS_DISABLED", "COMMENTS_ENABLED", "COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#comment_control GoogleCloudbuildTrigger#comment_control}
        :param invert_regex: If true, branches that do NOT match the git_ref will trigger a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        '''
        value = GoogleCloudbuildTriggerGithubPullRequest(
            branch=branch, comment_control=comment_control, invert_regex=invert_regex
        )

        return typing.cast(None, jsii.invoke(self, "putPullRequest", [value]))

    @jsii.member(jsii_name="putPush")
    def put_push(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: Regex of branches to match. Specify only one of branch or tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch GoogleCloudbuildTrigger#branch}
        :param invert_regex: When true, only trigger a build if the revision regex does NOT match the git_ref regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        :param tag: Regex of tags to match. Specify only one of branch or tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag GoogleCloudbuildTrigger#tag}
        '''
        value = GoogleCloudbuildTriggerGithubPush(
            branch=branch, invert_regex=invert_regex, tag=tag
        )

        return typing.cast(None, jsii.invoke(self, "putPush", [value]))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @jsii.member(jsii_name="resetPullRequest")
    def reset_pull_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPullRequest", []))

    @jsii.member(jsii_name="resetPush")
    def reset_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPush", []))

    @builtins.property
    @jsii.member(jsii_name="pullRequest")
    def pull_request(self) -> "GoogleCloudbuildTriggerGithubPullRequestOutputReference":
        return typing.cast("GoogleCloudbuildTriggerGithubPullRequestOutputReference", jsii.get(self, "pullRequest"))

    @builtins.property
    @jsii.member(jsii_name="push")
    def push(self) -> "GoogleCloudbuildTriggerGithubPushOutputReference":
        return typing.cast("GoogleCloudbuildTriggerGithubPushOutputReference", jsii.get(self, "push"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="pullRequestInput")
    def pull_request_input(
        self,
    ) -> typing.Optional["GoogleCloudbuildTriggerGithubPullRequest"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGithubPullRequest"], jsii.get(self, "pullRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="pushInput")
    def push_input(self) -> typing.Optional["GoogleCloudbuildTriggerGithubPush"]:
        return typing.cast(typing.Optional["GoogleCloudbuildTriggerGithubPush"], jsii.get(self, "pushInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "owner"))

    @owner.setter
    def owner(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubOutputReference, "owner").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "owner", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerGithub]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerGithub],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGithubPullRequest",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "comment_control": "commentControl",
        "invert_regex": "invertRegex",
    },
)
class GoogleCloudbuildTriggerGithubPullRequest:
    def __init__(
        self,
        *,
        branch: builtins.str,
        comment_control: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param branch: Regex of branches to match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch GoogleCloudbuildTrigger#branch}
        :param comment_control: Whether to block builds on a "/gcbrun" comment from a repository owner or collaborator. Possible values: ["COMMENTS_DISABLED", "COMMENTS_ENABLED", "COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#comment_control GoogleCloudbuildTrigger#comment_control}
        :param invert_regex: If true, branches that do NOT match the git_ref will trigger a build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGithubPullRequest.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument comment_control", value=comment_control, expected_type=type_hints["comment_control"])
            check_type(argname="argument invert_regex", value=invert_regex, expected_type=type_hints["invert_regex"])
        self._values: typing.Dict[str, typing.Any] = {
            "branch": branch,
        }
        if comment_control is not None:
            self._values["comment_control"] = comment_control
        if invert_regex is not None:
            self._values["invert_regex"] = invert_regex

    @builtins.property
    def branch(self) -> builtins.str:
        '''Regex of branches to match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch GoogleCloudbuildTrigger#branch}
        '''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def comment_control(self) -> typing.Optional[builtins.str]:
        '''Whether to block builds on a "/gcbrun" comment from a repository owner or collaborator. Possible values: ["COMMENTS_DISABLED", "COMMENTS_ENABLED", "COMMENTS_ENABLED_FOR_EXTERNAL_CONTRIBUTORS_ONLY"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#comment_control GoogleCloudbuildTrigger#comment_control}
        '''
        result = self._values.get("comment_control")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invert_regex(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, branches that do NOT match the git_ref will trigger a build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        '''
        result = self._values.get("invert_regex")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerGithubPullRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerGithubPullRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGithubPullRequestOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGithubPullRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCommentControl")
    def reset_comment_control(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommentControl", []))

    @jsii.member(jsii_name="resetInvertRegex")
    def reset_invert_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvertRegex", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="commentControlInput")
    def comment_control_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commentControlInput"))

    @builtins.property
    @jsii.member(jsii_name="invertRegexInput")
    def invert_regex_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "invertRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPullRequestOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="commentControl")
    def comment_control(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commentControl"))

    @comment_control.setter
    def comment_control(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPullRequestOutputReference, "comment_control").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commentControl", value)

    @builtins.property
    @jsii.member(jsii_name="invertRegex")
    def invert_regex(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "invertRegex"))

    @invert_regex.setter
    def invert_regex(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPullRequestOutputReference, "invert_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invertRegex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleCloudbuildTriggerGithubPullRequest]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerGithubPullRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerGithubPullRequest],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPullRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGithubPush",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "invert_regex": "invertRegex", "tag": "tag"},
)
class GoogleCloudbuildTriggerGithubPush:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: Regex of branches to match. Specify only one of branch or tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch GoogleCloudbuildTrigger#branch}
        :param invert_regex: When true, only trigger a build if the revision regex does NOT match the git_ref regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        :param tag: Regex of tags to match. Specify only one of branch or tag. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag GoogleCloudbuildTrigger#tag}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGithubPush.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument invert_regex", value=invert_regex, expected_type=type_hints["invert_regex"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if invert_regex is not None:
            self._values["invert_regex"] = invert_regex
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''Regex of branches to match.  Specify only one of branch or tag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch GoogleCloudbuildTrigger#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invert_regex(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, only trigger a build if the revision regex does NOT match the git_ref regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        '''
        result = self._values.get("invert_regex")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''Regex of tags to match.  Specify only one of branch or tag.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag GoogleCloudbuildTrigger#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerGithubPush(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerGithubPushOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerGithubPushOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerGithubPushOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetInvertRegex")
    def reset_invert_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvertRegex", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="invertRegexInput")
    def invert_regex_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "invertRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPushOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="invertRegex")
    def invert_regex(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "invertRegex"))

    @invert_regex.setter
    def invert_regex(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPushOutputReference, "invert_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invertRegex", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPushOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerGithubPush]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerGithubPush], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerGithubPush],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerGithubPushOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerPubsubConfig",
    jsii_struct_bases=[],
    name_mapping={"topic": "topic", "service_account_email": "serviceAccountEmail"},
)
class GoogleCloudbuildTriggerPubsubConfig:
    def __init__(
        self,
        *,
        topic: builtins.str,
        service_account_email: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param topic: The name of the topic from which this subscription is receiving messages. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#topic GoogleCloudbuildTrigger#topic}
        :param service_account_email: Service account that will make the push request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#service_account_email GoogleCloudbuildTrigger#service_account_email}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerPubsubConfig.__init__)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument service_account_email", value=service_account_email, expected_type=type_hints["service_account_email"])
        self._values: typing.Dict[str, typing.Any] = {
            "topic": topic,
        }
        if service_account_email is not None:
            self._values["service_account_email"] = service_account_email

    @builtins.property
    def topic(self) -> builtins.str:
        '''The name of the topic from which this subscription is receiving messages.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#topic GoogleCloudbuildTrigger#topic}
        '''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_account_email(self) -> typing.Optional[builtins.str]:
        '''Service account that will make the push request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#service_account_email GoogleCloudbuildTrigger#service_account_email}
        '''
        result = self._values.get("service_account_email")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerPubsubConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerPubsubConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerPubsubConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerPubsubConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceAccountEmail")
    def reset_service_account_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccountEmail", []))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="subscription")
    def subscription(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscription"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmailInput")
    def service_account_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountEmail")
    def service_account_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountEmail"))

    @service_account_email.setter
    def service_account_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerPubsubConfigOutputReference, "service_account_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccountEmail", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerPubsubConfigOutputReference, "topic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerPubsubConfig]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerPubsubConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerPubsubConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerPubsubConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerSourceToBuild",
    jsii_struct_bases=[],
    name_mapping={"ref": "ref", "repo_type": "repoType", "uri": "uri"},
)
class GoogleCloudbuildTriggerSourceToBuild:
    def __init__(
        self,
        *,
        ref: builtins.str,
        repo_type: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param ref: The branch or tag to use. Must start with "refs/" (required). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#ref GoogleCloudbuildTrigger#ref}
        :param repo_type: The type of the repo, since it may not be explicit from the repo field (e.g from a URL). Values can be UNKNOWN, CLOUD_SOURCE_REPOSITORIES, GITHUB, BITBUCKET Possible values: ["UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB", "BITBUCKET"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_type GoogleCloudbuildTrigger#repo_type}
        :param uri: The URI of the repo (required). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#uri GoogleCloudbuildTrigger#uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerSourceToBuild.__init__)
            check_type(argname="argument ref", value=ref, expected_type=type_hints["ref"])
            check_type(argname="argument repo_type", value=repo_type, expected_type=type_hints["repo_type"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "ref": ref,
            "repo_type": repo_type,
            "uri": uri,
        }

    @builtins.property
    def ref(self) -> builtins.str:
        '''The branch or tag to use. Must start with "refs/" (required).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#ref GoogleCloudbuildTrigger#ref}
        '''
        result = self._values.get("ref")
        assert result is not None, "Required property 'ref' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo_type(self) -> builtins.str:
        '''The type of the repo, since it may not be explicit from the repo field (e.g from a URL). Values can be UNKNOWN, CLOUD_SOURCE_REPOSITORIES, GITHUB, BITBUCKET Possible values: ["UNKNOWN", "CLOUD_SOURCE_REPOSITORIES", "GITHUB", "BITBUCKET"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_type GoogleCloudbuildTrigger#repo_type}
        '''
        result = self._values.get("repo_type")
        assert result is not None, "Required property 'repo_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''The URI of the repo (required).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#uri GoogleCloudbuildTrigger#uri}
        '''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerSourceToBuild(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerSourceToBuildOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerSourceToBuildOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerSourceToBuildOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="refInput")
    def ref_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refInput"))

    @builtins.property
    @jsii.member(jsii_name="repoTypeInput")
    def repo_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="ref")
    def ref(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ref"))

    @ref.setter
    def ref(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerSourceToBuildOutputReference, "ref").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ref", value)

    @builtins.property
    @jsii.member(jsii_name="repoType")
    def repo_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoType"))

    @repo_type.setter
    def repo_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerSourceToBuildOutputReference, "repo_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoType", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerSourceToBuildOutputReference, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerSourceToBuild]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerSourceToBuild], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerSourceToBuild],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerSourceToBuildOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleCloudbuildTriggerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#create GoogleCloudbuildTrigger#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#delete GoogleCloudbuildTrigger#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#update GoogleCloudbuildTrigger#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#create GoogleCloudbuildTrigger#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#delete GoogleCloudbuildTrigger#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#update GoogleCloudbuildTrigger#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudbuildTriggerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudbuildTriggerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudbuildTriggerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerTriggerTemplate",
    jsii_struct_bases=[],
    name_mapping={
        "branch_name": "branchName",
        "commit_sha": "commitSha",
        "dir": "dir",
        "invert_regex": "invertRegex",
        "project_id": "projectId",
        "repo_name": "repoName",
        "tag_name": "tagName",
    },
)
class GoogleCloudbuildTriggerTriggerTemplate:
    def __init__(
        self,
        *,
        branch_name: typing.Optional[builtins.str] = None,
        commit_sha: typing.Optional[builtins.str] = None,
        dir: typing.Optional[builtins.str] = None,
        invert_regex: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        project_id: typing.Optional[builtins.str] = None,
        repo_name: typing.Optional[builtins.str] = None,
        tag_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch_name: Name of the branch to build. Exactly one a of branch name, tag, or commit SHA must be provided. This field is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch_name GoogleCloudbuildTrigger#branch_name}
        :param commit_sha: Explicit commit SHA to build. Exactly one of a branch name, tag, or commit SHA must be provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#commit_sha GoogleCloudbuildTrigger#commit_sha}
        :param dir: Directory, relative to the source root, in which to run the build. This must be a relative path. If a step's dir is specified and is an absolute path, this value is ignored for that step's execution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        :param invert_regex: Only trigger a build if the revision regex does NOT match the revision regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        :param project_id: ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project_id GoogleCloudbuildTrigger#project_id}
        :param repo_name: Name of the Cloud Source Repository. If omitted, the name "default" is assumed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_name GoogleCloudbuildTrigger#repo_name}
        :param tag_name: Name of the tag to build. Exactly one of a branch name, tag, or commit SHA must be provided. This field is a regular expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag_name GoogleCloudbuildTrigger#tag_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerTriggerTemplate.__init__)
            check_type(argname="argument branch_name", value=branch_name, expected_type=type_hints["branch_name"])
            check_type(argname="argument commit_sha", value=commit_sha, expected_type=type_hints["commit_sha"])
            check_type(argname="argument dir", value=dir, expected_type=type_hints["dir"])
            check_type(argname="argument invert_regex", value=invert_regex, expected_type=type_hints["invert_regex"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
            check_type(argname="argument repo_name", value=repo_name, expected_type=type_hints["repo_name"])
            check_type(argname="argument tag_name", value=tag_name, expected_type=type_hints["tag_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch_name is not None:
            self._values["branch_name"] = branch_name
        if commit_sha is not None:
            self._values["commit_sha"] = commit_sha
        if dir is not None:
            self._values["dir"] = dir
        if invert_regex is not None:
            self._values["invert_regex"] = invert_regex
        if project_id is not None:
            self._values["project_id"] = project_id
        if repo_name is not None:
            self._values["repo_name"] = repo_name
        if tag_name is not None:
            self._values["tag_name"] = tag_name

    @builtins.property
    def branch_name(self) -> typing.Optional[builtins.str]:
        '''Name of the branch to build.

        Exactly one a of branch name, tag, or commit SHA must be provided.
        This field is a regular expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#branch_name GoogleCloudbuildTrigger#branch_name}
        '''
        result = self._values.get("branch_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def commit_sha(self) -> typing.Optional[builtins.str]:
        '''Explicit commit SHA to build. Exactly one of a branch name, tag, or commit SHA must be provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#commit_sha GoogleCloudbuildTrigger#commit_sha}
        '''
        result = self._values.get("commit_sha")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dir(self) -> typing.Optional[builtins.str]:
        '''Directory, relative to the source root, in which to run the build.

        This must be a relative path. If a step's dir is specified and
        is an absolute path, this value is ignored for that step's
        execution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#dir GoogleCloudbuildTrigger#dir}
        '''
        result = self._values.get("dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def invert_regex(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Only trigger a build if the revision regex does NOT match the revision regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#invert_regex GoogleCloudbuildTrigger#invert_regex}
        '''
        result = self._values.get("invert_regex")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''ID of the project that owns the Cloud Source Repository. If omitted, the project ID requesting the build is assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#project_id GoogleCloudbuildTrigger#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_name(self) -> typing.Optional[builtins.str]:
        '''Name of the Cloud Source Repository. If omitted, the name "default" is assumed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#repo_name GoogleCloudbuildTrigger#repo_name}
        '''
        result = self._values.get("repo_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_name(self) -> typing.Optional[builtins.str]:
        '''Name of the tag to build.

        Exactly one of a branch name, tag, or commit SHA must be provided.
        This field is a regular expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#tag_name GoogleCloudbuildTrigger#tag_name}
        '''
        result = self._values.get("tag_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerTriggerTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerTriggerTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerTriggerTemplateOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerTriggerTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranchName")
    def reset_branch_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranchName", []))

    @jsii.member(jsii_name="resetCommitSha")
    def reset_commit_sha(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitSha", []))

    @jsii.member(jsii_name="resetDir")
    def reset_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDir", []))

    @jsii.member(jsii_name="resetInvertRegex")
    def reset_invert_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInvertRegex", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @jsii.member(jsii_name="resetRepoName")
    def reset_repo_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoName", []))

    @jsii.member(jsii_name="resetTagName")
    def reset_tag_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagName", []))

    @builtins.property
    @jsii.member(jsii_name="branchNameInput")
    def branch_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchNameInput"))

    @builtins.property
    @jsii.member(jsii_name="commitShaInput")
    def commit_sha_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commitShaInput"))

    @builtins.property
    @jsii.member(jsii_name="dirInput")
    def dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dirInput"))

    @builtins.property
    @jsii.member(jsii_name="invertRegexInput")
    def invert_regex_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "invertRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="repoNameInput")
    def repo_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagNameInput")
    def tag_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagNameInput"))

    @builtins.property
    @jsii.member(jsii_name="branchName")
    def branch_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branchName"))

    @branch_name.setter
    def branch_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "branch_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branchName", value)

    @builtins.property
    @jsii.member(jsii_name="commitSha")
    def commit_sha(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commitSha"))

    @commit_sha.setter
    def commit_sha(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "commit_sha").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitSha", value)

    @builtins.property
    @jsii.member(jsii_name="dir")
    def dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dir"))

    @dir.setter
    def dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dir", value)

    @builtins.property
    @jsii.member(jsii_name="invertRegex")
    def invert_regex(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "invertRegex"))

    @invert_regex.setter
    def invert_regex(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "invert_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "invertRegex", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="repoName")
    def repo_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoName"))

    @repo_name.setter
    def repo_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "repo_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoName", value)

    @builtins.property
    @jsii.member(jsii_name="tagName")
    def tag_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagName"))

    @tag_name.setter
    def tag_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "tag_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerTriggerTemplate]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerTriggerTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerTriggerTemplate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerTriggerTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerWebhookConfig",
    jsii_struct_bases=[],
    name_mapping={"secret": "secret"},
)
class GoogleCloudbuildTriggerWebhookConfig:
    def __init__(self, *, secret: builtins.str) -> None:
        '''
        :param secret: Resource name for the secret required as a URL parameter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret GoogleCloudbuildTrigger#secret}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerWebhookConfig.__init__)
            check_type(argname="argument secret", value=secret, expected_type=type_hints["secret"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret": secret,
        }

    @builtins.property
    def secret(self) -> builtins.str:
        '''Resource name for the secret required as a URL parameter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloudbuild_trigger#secret GoogleCloudbuildTrigger#secret}
        '''
        result = self._values.get("secret")
        assert result is not None, "Required property 'secret' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudbuildTriggerWebhookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudbuildTriggerWebhookConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudbuildTrigger.GoogleCloudbuildTriggerWebhookConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudbuildTriggerWebhookConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="secretInput")
    def secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretInput"))

    @builtins.property
    @jsii.member(jsii_name="secret")
    def secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secret"))

    @secret.setter
    def secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerWebhookConfigOutputReference, "secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudbuildTriggerWebhookConfig]:
        return typing.cast(typing.Optional[GoogleCloudbuildTriggerWebhookConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudbuildTriggerWebhookConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudbuildTriggerWebhookConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleCloudbuildTrigger",
    "GoogleCloudbuildTriggerApprovalConfig",
    "GoogleCloudbuildTriggerApprovalConfigOutputReference",
    "GoogleCloudbuildTriggerBuild",
    "GoogleCloudbuildTriggerBuildArtifacts",
    "GoogleCloudbuildTriggerBuildArtifactsObjects",
    "GoogleCloudbuildTriggerBuildArtifactsObjectsOutputReference",
    "GoogleCloudbuildTriggerBuildArtifactsObjectsTiming",
    "GoogleCloudbuildTriggerBuildArtifactsObjectsTimingList",
    "GoogleCloudbuildTriggerBuildArtifactsObjectsTimingOutputReference",
    "GoogleCloudbuildTriggerBuildArtifactsOutputReference",
    "GoogleCloudbuildTriggerBuildAvailableSecrets",
    "GoogleCloudbuildTriggerBuildAvailableSecretsOutputReference",
    "GoogleCloudbuildTriggerBuildAvailableSecretsSecretManager",
    "GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerList",
    "GoogleCloudbuildTriggerBuildAvailableSecretsSecretManagerOutputReference",
    "GoogleCloudbuildTriggerBuildOptions",
    "GoogleCloudbuildTriggerBuildOptionsOutputReference",
    "GoogleCloudbuildTriggerBuildOptionsVolumes",
    "GoogleCloudbuildTriggerBuildOptionsVolumesList",
    "GoogleCloudbuildTriggerBuildOptionsVolumesOutputReference",
    "GoogleCloudbuildTriggerBuildOutputReference",
    "GoogleCloudbuildTriggerBuildSecret",
    "GoogleCloudbuildTriggerBuildSecretList",
    "GoogleCloudbuildTriggerBuildSecretOutputReference",
    "GoogleCloudbuildTriggerBuildSource",
    "GoogleCloudbuildTriggerBuildSourceOutputReference",
    "GoogleCloudbuildTriggerBuildSourceRepoSource",
    "GoogleCloudbuildTriggerBuildSourceRepoSourceOutputReference",
    "GoogleCloudbuildTriggerBuildSourceStorageSource",
    "GoogleCloudbuildTriggerBuildSourceStorageSourceOutputReference",
    "GoogleCloudbuildTriggerBuildStep",
    "GoogleCloudbuildTriggerBuildStepList",
    "GoogleCloudbuildTriggerBuildStepOutputReference",
    "GoogleCloudbuildTriggerBuildStepVolumes",
    "GoogleCloudbuildTriggerBuildStepVolumesList",
    "GoogleCloudbuildTriggerBuildStepVolumesOutputReference",
    "GoogleCloudbuildTriggerConfig",
    "GoogleCloudbuildTriggerGitFileSource",
    "GoogleCloudbuildTriggerGitFileSourceOutputReference",
    "GoogleCloudbuildTriggerGithub",
    "GoogleCloudbuildTriggerGithubOutputReference",
    "GoogleCloudbuildTriggerGithubPullRequest",
    "GoogleCloudbuildTriggerGithubPullRequestOutputReference",
    "GoogleCloudbuildTriggerGithubPush",
    "GoogleCloudbuildTriggerGithubPushOutputReference",
    "GoogleCloudbuildTriggerPubsubConfig",
    "GoogleCloudbuildTriggerPubsubConfigOutputReference",
    "GoogleCloudbuildTriggerSourceToBuild",
    "GoogleCloudbuildTriggerSourceToBuildOutputReference",
    "GoogleCloudbuildTriggerTimeouts",
    "GoogleCloudbuildTriggerTimeoutsOutputReference",
    "GoogleCloudbuildTriggerTriggerTemplate",
    "GoogleCloudbuildTriggerTriggerTemplateOutputReference",
    "GoogleCloudbuildTriggerWebhookConfig",
    "GoogleCloudbuildTriggerWebhookConfigOutputReference",
]

publication.publish()
